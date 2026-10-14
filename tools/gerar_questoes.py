# -*- coding: utf-8 -*-
"""
Gera js/questions.js (banco com 1000 questões) a partir de dados.py, dados2.py e dados3.py.
Uso:  python3 tools/gerar_questoes.py
"""
import json, os, random, sys

sys.path.insert(0, os.path.dirname(__file__))
import dados, dados2  # noqa: F401  (registram os POOLS)
from dados import POOLS
from dados3 import GRUPOS, MANUAIS

ALVO = 1000
rnd = random.Random(20261014)  # semente fixa => resultado reproduzível


def cap(s):
    return s[:1].upper() + s[1:]


def fim(s):
    s = s.strip()
    return s if s.endswith((".", "!", "?")) else s + "."


def parse(texto):
    itens = []
    for ln in texto.strip().splitlines():
        ln = ln.strip()
        if not ln:
            continue
        p = [x.strip() for x in ln.split("|")]
        assert len(p) >= 2, ln
        itens.append((p[0], p[1], p[2] if len(p) > 2 else ""))
    return itens


def monta(cat, q, correta, erradas, expl, g):
    assert len(erradas) == 4 and len(set(erradas + [correta])) == 5, (q, erradas)
    opts = erradas + [correta]
    rnd.shuffle(opts)
    return dict(c=cat, q=q, o=opts, a=opts.index(correta), e=expl, g=g)


def questoes_pool(p):
    itens = parse(p["texto"])
    assert len(itens) >= 6, p["nome"]
    out = []
    n = len(itens)
    for i, (t, d, ex) in enumerate(itens):
        outros = [j for j in range(n) if j != i]
        base = f"{t}: {d}"
        expl = f"Resposta correta: {t} — {d}. {fim(ex) if ex else ''}".strip()
        g = f"{p['nome']}#{i}"
        if "1" in p["forms"]:
            cand = [j for j in outros if itens[j][0] != t]
            err = [itens[j][0] for j in rnd.sample(cand, 4)]
            out.append(monta(p["ctx"], p["s1"].format(x=cap(d)), t, err, expl, g))
        if "2" in p["forms"]:
            cand = [j for j in outros if itens[j][1] != d]
            err = [cap(itens[j][1]) for j in rnd.sample(cand, 4)]
            out.append(monta(p["ctx"], p["s2"].format(x=t), cap(d), err, expl, g))
        if "3" in p["forms"]:
            cand = rnd.sample(outros, 4)
            err = []
            for j in cand:
                k = rnd.choice([m for m in range(n) if m != j and itens[m][1] != itens[j][1]])
                err.append(f"{itens[j][0]}: {itens[k][1]}")
            q = f"({p['ctx']}) Assinale a alternativa em que o termo está CORRETAMENTE associado à sua descrição."
            out.append(monta(p["ctx"], q, base, err, expl, g))
    return out


def questoes_grupos():
    grupos = []
    for nome, art, ref, texto in GRUPOS:
        itens = [x.strip() for x in texto.strip().splitlines() if x.strip()]
        grupos.append(dict(nome=nome, art=art, ref=ref, itens=itens))
    out = []
    for gi, G in enumerate(grupos):
        outros_g = [h for h in grupos if h is not G]
        for ii, it in enumerate(G["itens"]):
            gk = f"grp#{gi}#{ii}"
            expl = f"É atribuição {G['art']}: {it}. ({G['ref']})."
            # A) qual atribuição pertence ao órgão X?
            hs = rnd.sample(outros_g, 4)
            err = [cap(rnd.choice(h["itens"])) for h in hs]
            out.append(monta("Atribuições dos órgãos",
                             f"Assinale a alternativa que apresenta uma atribuição {G['art']}.",
                             cap(it), err, expl, gk))
            # B) a atribuição Y pertence a qual órgão?
            hs = rnd.sample(outros_g, 4)
            err = [h["nome"] for h in hs]
            out.append(monta("Atribuições dos órgãos",
                             f"A atribuição de «{it}» é de competência de:",
                             G["nome"], err, expl, gk))
            # C) qual NÃO é atribuição do órgão X?
            if len(G["itens"]) >= 5:
                h = rnd.choice(outros_g)
                alheia = rnd.choice(h["itens"])
                proprias = rnd.sample([x for x in G["itens"] if x != it], 4)
                out.append(monta("Atribuições dos órgãos",
                                 f"Assinale a alternativa que NÃO apresenta uma atribuição {G['art']}.",
                                 cap(alheia), [cap(x) for x in proprias],
                                 f"Não é atribuição {G['art']}, mas {h['art']}: {alheia}. ({h['ref']}).", gk))
    return out


def questoes_manuais():
    out, cat, k = [], "Conhecimentos gerais", 0
    for ln in MANUAIS.strip().splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith("##"):
            cat = ln[2:].strip()
            continue
        p = [x.strip() for x in ln.split("#")]
        assert len(p) == 7, ln
        q, certa, *err, expl = p
        k += 1
        out.append(monta(cat, q, certa, err, expl, f"man#{k}"))
    return out


def main():
    gerais = []
    for p in POOLS:
        gerais += questoes_pool(p)
    gerais += questoes_grupos()
    manuais = questoes_manuais()

    # deduplica enunciados idênticos
    vistos, unicas = set(), []
    for q in manuais + gerais:
        chave = (q["q"], q["o"][q["a"]])
        if chave in vistos:
            continue
        vistos.add(chave)
        unicas.append(q)

    manuais_ok = [q for q in unicas if q["g"].startswith("man#")]
    resto = [q for q in unicas if not q["g"].startswith("man#")]
    falta = ALVO - len(manuais_ok)
    assert len(resto) >= falta, f"Faltam questões: {len(resto)} < {falta}"
    rnd.shuffle(resto)
    banco = manuais_ok + resto[:falta]
    rnd.shuffle(banco)
    for i, q in enumerate(banco, 1):
        q["id"] = i

    destino = os.path.join(os.path.dirname(__file__), "..", "js", "questions.js")
    with open(destino, "w", encoding="utf-8") as f:
        f.write("/* Banco de questões — gerado por tools/gerar_questoes.py */\n")
        f.write("window.QUESTION_BANK = ")
        json.dump(banco, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")
    cats = {}
    for q in banco:
        cats[q["c"]] = cats.get(q["c"], 0) + 1
    print(f"{len(banco)} questões (manuais: {len(manuais_ok)}; geradas disponíveis: {len(resto)})")
    for c, n in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {n:4d}  {c}")


if __name__ == "__main__":
    main()
