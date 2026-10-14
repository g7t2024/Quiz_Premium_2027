/* Confete de festa em canvas (sem dependências).
   Uso: Confetti.fire(duracaoEmMs) */
(function () {
  'use strict';

  var canvas = document.getElementById('confetti-canvas');
  var ctx = canvas ? canvas.getContext('2d') : null;
  var COLORS = ['#f94144', '#f3722c', '#f9c74f', '#90be6d', '#43aa8b', '#4d908e', '#4361ee', '#7b2cbf', '#ff5d8f', '#00bbf9'];
  var particles = [];
  var running = false;
  var spawnUntil = 0;
  var lastSpawn = 0;
  var dpr = 1;
  var W = 0, H = 0;

  function resize() {
    if (!canvas) return;
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = Math.floor(W * dpr);
    canvas.height = Math.floor(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  window.addEventListener('resize', resize);

  function rand(a, b) { return a + Math.random() * (b - a); }

  function make(x, y, vx, vy) {
    return {
      x: x, y: y, vx: vx, vy: vy,
      size: rand(7, 14),
      color: COLORS[(Math.random() * COLORS.length) | 0],
      shape: Math.random() < .25 ? 'circle' : (Math.random() < .5 ? 'rect' : 'strip'),
      rot: rand(0, Math.PI * 2),
      vr: rand(-.3, .3),
      tilt: rand(0, Math.PI * 2),
      vt: rand(.05, .2),
      drag: rand(.985, .995),
      life: 0
    };
  }

  function cannon(side, count) {
    var x = side < 0 ? -10 : W + 10;
    var dir = side < 0 ? 1 : -1;
    for (var i = 0; i < count; i++) {
      var ang = rand(-1.25, -.55); // para cima
      var speed = rand(11, 24);
      particles.push(make(x, H * rand(.55, .95), Math.cos(ang) * speed * dir, Math.sin(ang) * speed));
    }
  }

  function rain(count) {
    for (var i = 0; i < count; i++) {
      particles.push(make(rand(0, W), rand(-40, -10), rand(-2, 2), rand(1, 4)));
    }
  }

  function draw(p) {
    ctx.save();
    ctx.translate(p.x, p.y);
    ctx.rotate(p.rot);
    ctx.fillStyle = p.color;
    var squash = Math.cos(p.tilt);
    if (p.shape === 'circle') {
      ctx.beginPath(); ctx.arc(0, 0, p.size / 2.2, 0, Math.PI * 2); ctx.fill();
    } else if (p.shape === 'strip') {
      ctx.scale(1, squash); ctx.fillRect(-p.size / 2, -p.size / 6, p.size, p.size / 3);
    } else {
      ctx.scale(1, squash); ctx.fillRect(-p.size / 2, -p.size / 2.6, p.size, p.size / 1.3);
    }
    ctx.restore();
  }

  function frame(t) {
    if (!running) return;
    ctx.clearRect(0, 0, W, H);

    if (t < spawnUntil && t - lastSpawn > 160) {
      lastSpawn = t;
      rain(reduced() ? 4 : 10);
      if (Math.random() < .35) cannon(Math.random() < .5 ? -1 : 1, reduced() ? 8 : 18);
    }

    for (var i = particles.length - 1; i >= 0; i--) {
      var p = particles[i];
      p.vx *= p.drag; p.vy = p.vy * p.drag + .38;
      if (p.vy > 9) p.vy = 9;
      p.x += p.vx; p.y += p.vy;
      p.rot += p.vr; p.tilt += p.vt; p.life++;
      draw(p);
      if (p.y > H + 40 || p.x < -80 || p.x > W + 80) particles.splice(i, 1);
    }

    if (particles.length === 0 && t >= spawnUntil) {
      running = false;
      ctx.clearRect(0, 0, W, H);
      return;
    }
    requestAnimationFrame(frame);
  }

  function reduced() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  window.Confetti = {
    fire: function (duration) {
      if (!ctx) return;
      resize();
      duration = duration || 6000;
      var now = performance.now();
      spawnUntil = now + duration;
      cannon(-1, reduced() ? 40 : 110);
      cannon(1, reduced() ? 40 : 110);
      rain(reduced() ? 20 : 70);
      if (!running) {
        running = true;
        lastSpawn = now;
        requestAnimationFrame(frame);
      }
    },
    stop: function () {
      running = false; particles.length = 0;
      if (ctx) ctx.clearRect(0, 0, W, H);
    }
  };

  resize();
})();
