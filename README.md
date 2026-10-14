# Quiz Concursos Pro

Quiz para concursos com **banco de 1000 questões** (5 alternativas + explicação), sorteio de 20 por rodada,
modo claro/escuro, gráfico de acertos/erros, emojis, confete e pop-ups. Funciona 100% offline, sem build.

## Como usar
Abra `index.html` no navegador (duplo clique). Não precisa de servidor.

## Estrutura
```
index.html            página principal
css/style.css         estilos (tema claro/escuro, animações, responsivo)
js/questions.js       banco com 1000 questões (gerado)
js/app.js             lógica do quiz, tema, pop-ups, resultado
js/chart.js           gráfico de rosca (canvas)
js/confetti.js        animação de confete (canvas)
tools/                scripts Python que geram o banco (opcional)
```

## Como funciona
- Cada quiz sorteia 20 questões **ainda não vistas**; ao responder, a questão é marcada como vista (localStorage).
- Ao completar as 1000 questões: confete + pop-up final, e o ciclo recomeça.
- Botão "Resetar e novo quiz" traz novas questões aleatórias.
- Atalhos: `A–E` ou `1–5` respondem; `Enter` avança; `Esc` fecha pop-ups.

## Editar ou ampliar o banco
Edite `tools/dados.py`, `tools/dados2.py` (termo | descrição | base legal) ou `tools/dados3.py`
(atribuições por órgão e questões manuais) e rode:

    python3 tools/gerar_questoes.py

O script regenera `js/questions.js` (ajuste `ALVO` em `gerar_questoes.py` se quiser outro tamanho).
Revise sempre os textos jurídicos antes de usar em estudo.
