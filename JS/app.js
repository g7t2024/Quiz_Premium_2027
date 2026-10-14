/* Quiz Concursos Pro — lógica principal */
(function () {
  'use strict';

  var QUIZ_SIZE = 20;
  var BANK = window.QUESTION_BANK || [];
  var FINAL_MSG = 'Parabéns, se chegou até aqui é porque tem um propósito e objetivo, vai passar!';

  /* ---------- utilidades ---------- */
  function $(s, r) { return (r || document).querySelector(s); }
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  var mem = {};
  var store = {
    get: function (k, d) {
      try { var v = localStorage.getItem(k); return v == null ? (k in mem ? mem[k] : d) : JSON.parse(v); }
      catch (e) { return k in mem ? mem[k] : d; }
    },
    set: function (k, v) {
      mem[k] = v;
      try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* modo privado */ }
    }
  };
  var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var LETTERS = ['A', 'B', 'C', 'D', 'E'];

  /* ---------- elementos ---------- */
  var screens = { start: $('#screen-start'), quiz: $('#screen-quiz'), result: $('#screen-result') };
  var elOptions = $('#options'), elFeedback = $('#feedback'), btnNext = $('#btn-next');

  /* ---------- estado ---------- */
  var seen = new Set(store.get('cq_seen', []));
  var stats = store.get('cq_stats', { quizzes: 0, hits: 0, total: 0 });
  var quiz = null;

  /* =========================================================
     Tema claro / escuro
     ========================================================= */
  var themeBtn = $('#theme-toggle');
  function applyTheme(t, persist) {
    document.documentElement.setAttribute('data-theme', t);
    themeBtn.setAttribute('aria-checked', String(t === 'dark'));
    themeBtn.setAttribute('aria-label', t === 'dark' ? 'Modo escuro ativado. Mudar para claro' : 'Modo claro ativado. Mudar para escuro');
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', t === 'dark' ? '#070b16' : '#eef2fb');
    if (persist) store.set('cq_theme', t);
    window.dispatchEvent(new Event('cq:themechange'));
  }
  themeBtn.addEventListener('click', function () {
    var cur = document.documentElement.getAttribute('data-theme');
    applyTheme(cur === 'dark' ? 'light' : 'dark', true);
  });
  applyTheme(document.documentElement.getAttribute('data-theme') || 'light', false);

  /* =========================================================
     Modal (pop-up)
     ========================================================= */
  var modal = $('#modal'), modalOnClose = null, lastFocus = null;

  function openModal(o) {
    lastFocus = document.activeElement;
    $('#modal-icon').textContent = o.icon || '🎯';
    $('#modal-title').textContent = o.title || '';
    $('#modal-text').textContent = o.text || '';
    var box = $('#modal-actions');
    box.textContent = '';
    (o.actions || []).forEach(function (a) {
      var b = el('button', 'btn ' + (a.primary ? 'btn-primary' : 'btn-ghost'), a.label);
      b.type = 'button';
      b.addEventListener('click', function () { closeModal(); if (a.onClick) a.onClick(); });
      box.appendChild(b);
    });
    modalOnClose = o.onClose || null;
    modal.classList.remove('closing');
    modal.hidden = false;
    document.body.classList.add('modal-open');
    $('#modal-x').focus();
  }
  function closeModal() {
    if (modal.hidden || modal.classList.contains('closing')) return;
    modal.classList.add('closing');
    var cb = modalOnClose; modalOnClose = null;
    setTimeout(function () {
      modal.hidden = true;
      modal.classList.remove('closing');
      document.body.classList.remove('modal-open');
      if (lastFocus && lastFocus.focus && document.contains(lastFocus)) { try { lastFocus.focus(); } catch (e) {} }
      if (cb) cb();
    }, reducedMotion ? 0 : 230);
  }
  modal.addEventListener('click', function (e) { if (e.target.hasAttribute('data-close')) closeModal(); });
  $('#modal-x').addEventListener('click', closeModal);
  document.addEventListener('keydown', function (e) {
    if (modal.hidden) return;
    if (e.key === 'Escape') { closeModal(); return; }
    if (e.key === 'Tab') { // foca dentro do pop-up
      var f = modal.querySelectorAll('button');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  /* =========================================================
     Navegação entre telas
     ========================================================= */
  function show(name) {
    Object.keys(screens).forEach(function (k) { screens[k].hidden = k !== name; });
    window.scrollTo({ top: 0, behavior: reducedMotion ? 'auto' : 'smooth' });
  }

  /* =========================================================
     Banco de questões
     ========================================================= */
  function refreshBank() {
    var n = seen.size, t = BANK.length;
    $('#bank-seen').textContent = n;
    $('#bank-total').textContent = t;
    $('#hero-total').textContent = t;
    $('#bp-text').textContent = n + ' / ' + t;
    $('#bp-bar').style.width = (t ? (n / t) * 100 : 0) + '%';
    var left = t - n;
    $('#bp-hint').textContent = n === 0
      ? 'Cada quiz traz questões inéditas até você completar todo o banco.'
      : 'Faltam ' + left + ' questões inéditas para completar o banco. Continue assim! 💪';
    var h = $('#history');
    if (stats.total > 0) {
      h.hidden = false;
      h.innerHTML = '';
      h.append('Seu histórico: ');
      var b1 = el('b', null, stats.quizzes + (stats.quizzes === 1 ? ' quiz' : ' quizzes'));
      var b2 = el('b', null, Math.round(stats.hits / stats.total * 100) + '% de acertos');
      h.append(b1, ' concluídos · ', b2, ' no total');
    } else h.hidden = true;
  }

  function pickQuestions() {
    if (seen.size >= BANK.length) { seen.clear(); store.set('cq_seen', []); }
    var pool = shuffle(BANK.filter(function (q) { return !seen.has(q.id); }));
    var chosen = [], groups = {};
    pool.forEach(function (q) {            // evita questões "gêmeas" no mesmo quiz
      if (chosen.length < QUIZ_SIZE && !groups[q.g]) { groups[q.g] = 1; chosen.push(q); }
    });
    pool.forEach(function (q) {
      if (chosen.length < QUIZ_SIZE && chosen.indexOf(q) < 0) chosen.push(q);
    });
    if (chosen.length < QUIZ_SIZE) {       // banco pequeno: completa com questões já vistas
      shuffle(BANK.slice()).forEach(function (q) {
        if (chosen.length < QUIZ_SIZE && chosen.indexOf(q) < 0) chosen.push(q);
      });
    }
    return chosen.map(function (q) {
      var opts = q.o.map(function (t, i) { return { text: t, ok: i === q.a }; });
      return { id: q.id, cat: q.c, text: q.q, expl: q.e, opts: shuffle(opts) };
    });
  }

  /* =========================================================
     Quiz
     ========================================================= */
  function startQuiz() {
    Confetti.stop();
    quiz = { list: pickQuestions(), i: 0, hits: 0, misses: 0, answers: [], answered: false };
    $('#q-total').textContent = quiz.list.length;
    $('#quiz-progress').setAttribute('aria-valuemax', quiz.list.length);
    $('#s-hit').textContent = '0';
    $('#s-miss').textContent = '0';
    show('quiz');
    renderQuestion();
    openModal({
      icon: '🎯',
      title: 'Vamos testar seus conhecimentos!',
      text: 'Responda com calma, leia a explicação de cada questão e bons estudos.',
      actions: [{ label: 'Bora! 🚀', primary: true }],
      onClose: function () { $('#q-text').focus({ preventScroll: true }); }
    });
  }

  function renderQuestion() {
    var q = quiz.list[quiz.i];
    quiz.answered = false;
    $('#q-num').textContent = quiz.i + 1;
    $('#q-cat').textContent = q.cat;
    $('#q-text').textContent = q.text;
    var pct = (quiz.i / quiz.list.length) * 100;
    $('#bar').style.width = pct + '%';
    $('#quiz-progress').setAttribute('aria-valuenow', quiz.i);

    elOptions.textContent = '';
    q.opts.forEach(function (o, idx) {
      var b = el('button', 'option');
      b.type = 'button';
      b.dataset.idx = idx;
      b.appendChild(el('span', 'opt-letter', LETTERS[idx]));
      b.appendChild(el('span', 'opt-text', o.text));
      b.appendChild(el('span', 'opt-mark', ''));
      b.addEventListener('click', function () { choose(idx); });
      elOptions.appendChild(b);
    });

    elFeedback.hidden = true;
    elFeedback.className = 'feedback';
    btnNext.disabled = true;
    btnNext.textContent = quiz.i === quiz.list.length - 1 ? 'Ver resultado 🏁' : 'Próxima questão →';
    var card = $('#qcard');
    card.style.animation = 'none'; void card.offsetWidth; card.style.animation = '';
  }

  function choose(idx) {
    if (!quiz || quiz.answered) return;
    quiz.answered = true;
    var q = quiz.list[quiz.i];
    var correctIdx = q.opts.findIndex(function (o) { return o.ok; });
    var hit = idx === correctIdx;
    var nodes = elOptions.children;

    for (var k = 0; k < nodes.length; k++) {
      nodes[k].classList.add('locked');
      nodes[k].setAttribute('aria-disabled', 'true');
      if (k === correctIdx) {
        nodes[k].classList.add('correct');
        nodes[k].querySelector('.opt-mark').textContent = '✓';
      } else if (k === idx) {
        nodes[k].classList.add('wrong');
        nodes[k].querySelector('.opt-mark').textContent = '✕';
      } else nodes[k].classList.add('dim');
    }

    if (hit) quiz.hits++; else quiz.misses++;
    quiz.answers.push({ q: q, chosen: idx, correct: correctIdx, hit: hit });
    bump(hit ? '#s-hit' : '#s-miss', hit ? quiz.hits : quiz.misses);

    seen.add(q.id);
    store.set('cq_seen', Array.from(seen));
    refreshBank();

    // feedback com emoji + explicação
    var happy = ['😄', '🥳', '😁', '🤩', '😃'], sad = ['😢', '😞', '😭', '🥺'];
    var emoji = (hit ? happy : sad)[Math.floor(Math.random() * (hit ? happy.length : sad.length))];
    var msgOk = ['Acertou!', 'Mandou bem!', 'Isso mesmo!', 'Perfeito!'];
    var msgBad = ['Não foi dessa vez.', 'Quase lá!', 'Errou, mas aprendeu.', 'Vamos revisar!'];
    $('#fb-emoji').textContent = emoji;
    $('#fb-title').textContent = (hit ? msgOk : msgBad)[Math.floor(Math.random() * 4)];
    var p = $('#fb-expl');
    p.textContent = '';
    p.appendChild(el('span', 'exp-label', '💡 Explicação'));
    if (!hit) p.appendChild(document.createTextNode('A alternativa correta é a letra ' + LETTERS[correctIdx] + '. '));
    p.appendChild(document.createTextNode(q.expl));
    elFeedback.className = 'feedback ' + (hit ? 'ok' : 'bad');
    elFeedback.hidden = false;

    floatEmojis(hit ? ['😄', '🎉', '✨', '😁'] : ['😢', '💧', '😞'], nodes[idx]);
    btnNext.disabled = false;
    setTimeout(function () {
      elFeedback.scrollIntoView({ behavior: reducedMotion ? 'auto' : 'smooth', block: 'nearest' });
    }, 80);
  }

  function bump(sel, val) {
    var n = $(sel);
    n.textContent = val;
    n.classList.remove('bump'); void n.offsetWidth; n.classList.add('bump');
  }

  function floatEmojis(list, origin) {
    if (reducedMotion) return;
    var layer = $('#fx-layer');
    var r = origin.getBoundingClientRect();
    var x0 = r.left + Math.min(r.width, 90);
    var y0 = r.top + r.height / 2;
    var up = list.indexOf('😢') < 0;
    for (var i = 0; i < 9; i++) {
      var s = el('span', 'fx-emoji', list[i % list.length]);
      s.style.left = (x0 + (Math.random() * 120 - 40)) + 'px';
      s.style.top = y0 + 'px';
      s.style.fontSize = (22 + Math.random() * 20) + 'px';
      s.style.setProperty('--x', (Math.random() * 160 - 80) + 'px');
      s.style.setProperty('--y', (up ? -1 : 1) * (110 + Math.random() * 130) + 'px');
      s.style.setProperty('--r', (Math.random() * 60 - 30) + 'deg');
      s.style.setProperty('--d', (1.2 + Math.random() * .9) + 's');
      s.style.animationDelay = (i * 45) + 'ms';
      s.addEventListener('animationend', function (e) { e.target.remove(); });
      layer.appendChild(s);
    }
  }

  function next() {
    if (!quiz || !quiz.answered) return;
    if (quiz.i < quiz.list.length - 1) {
      quiz.i++;
      renderQuestion();
      $('#q-text').focus({ preventScroll: true });
      window.scrollTo({ top: 0, behavior: reducedMotion ? 'auto' : 'smooth' });
    } else finish();
  }

  /* =========================================================
     Resultado
     ========================================================= */
  var TIERS = [
    { min: 100, emoji: '🏆', cls: 'anim-trophy', title: 'Perfeito! 100%', msg: 'Gabaritou! Você está pronto para a prova.' },
    { min: 90, emoji: '🥳', cls: 'anim-party', title: 'Excelente!', msg: 'Desempenho de aprovado. Continue nesse ritmo!' },
    { min: 70, emoji: '😄', cls: 'anim-smile', title: 'Muito bom!', msg: 'Você domina boa parte do conteúdo. Revise os erros e avance.' },
    { min: 50, emoji: '🙂', cls: 'anim-smile', title: 'No caminho certo', msg: 'Já tem uma boa base. Mais algumas rodadas e você chega lá.' },
    { min: 30, emoji: '😕', cls: 'anim-meh', title: 'Dá para melhorar', msg: 'Leia as explicações com atenção e tente novamente.' },
    { min: 0, emoji: '😢', cls: 'anim-sad', title: 'Hora de revisar', msg: 'Sem desânimo: errar faz parte. Revise as explicações e tente outra vez.' }
  ];

  function finish() {
    var total = quiz.list.length;
    var pct = Math.round(quiz.hits / total * 100);
    var tier = TIERS.find(function (t) { return pct >= t.min; });

    stats.quizzes++; stats.hits += quiz.hits; stats.total += total;
    store.set('cq_stats', stats);
    refreshBank();

    $('#bar').style.width = '100%';
    show('result');
    var em = $('#r-emoji');
    em.textContent = tier.emoji;
    em.className = 'r-emoji ' + tier.cls;
    $('#r-title').textContent = tier.title;
    $('#r-msg').textContent = quiz.hits + ' de ' + total + ' questões corretas. ' + tier.msg;
    $('#lg-hit').textContent = pct + '%';
    $('#lg-hit-n').textContent = quiz.hits + (quiz.hits === 1 ? ' acerto' : ' acertos');
    $('#lg-miss').textContent = (100 - pct) + '%';
    $('#lg-miss-n').textContent = quiz.misses + (quiz.misses === 1 ? ' erro' : ' erros');
    $('#review').hidden = true;
    $('#btn-review').setAttribute('aria-expanded', 'false');
    buildReview();

    setTimeout(function () { DonutChart.render($('#chart'), { hits: quiz.hits, misses: quiz.misses }); }, 120);
    if (pct >= 90) setTimeout(function () { Confetti.fire(2600); }, 500);
    $('#r-title').focus({ preventScroll: true });

    // fim do banco inteiro: confete + mensagem final
    if (seen.size >= BANK.length) {
      setTimeout(function () {
        Confetti.fire(9000);
        openModal({
          icon: '🎊',
          title: 'Banco concluído!',
          text: FINAL_MSG,
          actions: [{ label: 'Fechar', primary: true }]
        });
      }, 1100);
    }
  }

  function buildReview() {
    var box = $('#review');
    box.textContent = '';
    quiz.answers.forEach(function (a, n) {
      var d = el('details', 'rv-item');
      var s = el('summary');
      s.appendChild(el('span', null, a.hit ? '✅' : '❌'));
      s.appendChild(el('span', null, (n + 1) + '. ' + a.q.text));
      d.appendChild(s);
      var body = el('div', 'rv-body');
      var l1 = el('p'); l1.append('Sua resposta: ');
      l1.appendChild(el('b', a.hit ? 'ok' : 'bad', LETTERS[a.chosen] + ') ' + a.q.opts[a.chosen].text));
      body.appendChild(l1);
      if (!a.hit) {
        var l2 = el('p'); l2.append('Correta: ');
        l2.appendChild(el('b', 'ok', LETTERS[a.correct] + ') ' + a.q.opts[a.correct].text));
        body.appendChild(l2);
      }
      body.appendChild(el('p', null, '💡 ' + a.q.expl));
      d.appendChild(body);
      box.appendChild(d);
    });
  }

  /* =========================================================
     Eventos
     ========================================================= */
  $('#btn-start').addEventListener('click', startQuiz);
  $('#btn-reset').addEventListener('click', startQuiz);   // reset => novas questões aleatórias
  btnNext.addEventListener('click', next);
  $('#btn-review').addEventListener('click', function () {
    var r = $('#review'), open = r.hidden;
    r.hidden = !open;
    this.setAttribute('aria-expanded', String(open));
    if (open) r.scrollIntoView({ behavior: reducedMotion ? 'auto' : 'smooth', block: 'start' });
  });
  $('#btn-quit').addEventListener('click', function () {
    openModal({
      icon: '↺',
      title: 'Reiniciar o quiz?',
      text: 'Você perderá o progresso desta rodada e receberá novas questões aleatórias.',
      actions: [
        { label: 'Continuar', primary: false },
        { label: 'Reiniciar', primary: true, onClick: function () { startQuiz(); } }
      ]
    });
  });

  document.addEventListener('keydown', function (e) {
    if (!modal.hidden || screens.quiz.hidden || !quiz || e.ctrlKey || e.metaKey || e.altKey) return;
    var k = e.key.toLowerCase(), idx = -1;
    if (/^[a-e]$/.test(k)) idx = k.charCodeAt(0) - 97;
    else if (/^[1-5]$/.test(k)) idx = Number(k) - 1;
    if (idx >= 0) { e.preventDefault(); choose(idx); return; }
    if ((e.key === 'Enter' || e.key === 'ArrowRight') && quiz.answered) {
      if (document.activeElement === btnNext && e.key === 'Enter') return; // o clique nativo já avança
      e.preventDefault();
      next();
    }
  });

  /* ---------- início ---------- */
  refreshBank();
  show('start');
  window.scrollTo(0, 0);
})();
