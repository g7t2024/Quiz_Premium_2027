/* Gráfico de rosca (acertos x erros) em canvas, sem dependências.
   Uso: DonutChart.render(canvas, { hits: 12, misses: 8 }) */
(function () {
  'use strict';

  var state = { canvas: null, hits: 0, misses: 0, progress: 1, raf: 0 };

  function css(name, fallback) {
    var v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    return v || fallback;
  }
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }
  function reduced() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function draw() {
    var c = state.canvas;
    if (!c) return;
    var size = c.clientWidth || 260;
    var dpr = Math.min(window.devicePixelRatio || 1, 3);
    if (c.width !== Math.round(size * dpr)) {
      c.width = Math.round(size * dpr);
      c.height = Math.round(size * dpr);
    }
    var ctx = c.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, size, size);

    var total = state.hits + state.misses;
    var cx = size / 2, cy = size / 2;
    var thick = size * 0.17;
    var r = size / 2 - thick / 2 - 4;
    var start = -Math.PI / 2;
    var p = state.progress;
    var okColor = css('--ok', '#16a34a');
    var badColor = css('--bad', '#dc2626');
    var track = css('--track', 'rgba(0,0,0,.1)');
    var text = css('--text', '#111');
    var muted = css('--muted', '#666');

    // trilho
    ctx.lineWidth = thick;
    ctx.lineCap = 'butt';
    ctx.strokeStyle = track;
    ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.stroke();

    if (total > 0) {
      var full = Math.PI * 2 * p;
      var hitAng = (state.hits / total) * full;
      var missAng = (state.misses / total) * full;
      var gap = (state.hits > 0 && state.misses > 0) ? 0.05 : 0;

      ctx.lineCap = 'round';
      if (state.hits > 0) {
        ctx.strokeStyle = okColor;
        ctx.beginPath();
        ctx.arc(cx, cy, r, start + gap, start + Math.max(hitAng - gap, 0.001));
        ctx.stroke();
      }
      if (state.misses > 0) {
        ctx.strokeStyle = badColor;
        ctx.beginPath();
        ctx.arc(cx, cy, r, start + hitAng + gap, start + hitAng + Math.max(missAng - gap, 0.001));
        ctx.stroke();
      }
    }

    // texto central
    var pct = total ? Math.round((state.hits / total) * 100 * p) : 0;
    ctx.fillStyle = text;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '800 ' + Math.round(size * 0.22) + 'px "Plus Jakarta Sans", system-ui, sans-serif';
    ctx.fillText(pct + '%', cx, cy - size * 0.03);
    ctx.fillStyle = muted;
    ctx.font = '600 ' + Math.round(size * 0.07) + 'px "Plus Jakarta Sans", system-ui, sans-serif';
    ctx.fillText('de acertos', cx, cy + size * 0.12);
  }

  function render(canvas, data) {
    cancelAnimationFrame(state.raf);
    state.canvas = canvas;
    state.hits = data.hits;
    state.misses = data.misses;
    var total = data.hits + data.misses;
    canvas.setAttribute('aria-label',
      'Gráfico de rosca: ' + data.hits + ' acertos e ' + data.misses + ' erros, ' +
      (total ? Math.round(data.hits / total * 100) : 0) + '% de acertos');

    if (reduced()) { state.progress = 1; draw(); return; }

    var t0 = null, dur = 1300;
    state.progress = 0;
    function step(ts) {
      if (t0 === null) t0 = ts;
      var k = Math.min((ts - t0) / dur, 1);
      state.progress = easeOut(k);
      draw();
      if (k < 1) state.raf = requestAnimationFrame(step);
    }
    state.raf = requestAnimationFrame(step);
  }

  window.addEventListener('resize', function () { if (state.canvas && state.canvas.offsetParent) draw(); });
  window.addEventListener('cq:themechange', function () { if (state.canvas) draw(); });

  window.DonutChart = { render: render, redraw: draw };
})();
