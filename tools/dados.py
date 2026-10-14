# -*- coding: utf-8 -*-
"""
Base de conhecimento do Quiz Concursos.
Formato dos blocos de itens:  termo | descrição | observação/base legal (opcional)
Para adicionar conteúdo, acrescente linhas e rode:  python3 tools/gerar_questoes.py
"""

DEFAULT_S1 = "Assinale a alternativa que corresponde à seguinte descrição: «{x}»"
DEFAULT_S2 = "Assinale a alternativa que apresenta a definição correta de «{x}»."

POOLS = []


def pool(nome, ctx, texto, forms="123", s1=DEFAULT_S1, s2=DEFAULT_S2):
    POOLS.append(dict(nome=nome, ctx=ctx, forms=forms, s1=s1, s2=s2, texto=texto))


# ---------------------------------------------------------------- DEMOCRACIA
pool("democracia", "Democracia e Constituição", """
Democracia representativa | o povo exerce o poder por meio de representantes eleitos periodicamente | CF, art. 1º, parágrafo único.
Democracia direta | os cidadãos decidem diretamente as questões públicas, sem intermediários | Modelo típico da Atenas antiga.
Democracia semidireta (participativa) | combina representantes eleitos com instrumentos de participação direta, como plebiscito, referendo e iniciativa popular | Modelo adotado pelo Brasil (CF, art. 14).
Plebiscito | consulta popular realizada previamente à criação do ato, para que o povo decida sobre a matéria | CF, art. 14, I, e Lei 9.709/1998.
Referendo | consulta popular posterior ao ato, para ratificá-lo ou rejeitá-lo | CF, art. 14, II. O referendo do desarmamento (2005) é o exemplo mais conhecido.
Iniciativa popular | projeto de lei subscrito por no mínimo 1% do eleitorado nacional, distribuído por pelo menos cinco estados, com não menos de 0,3% em cada um | CF, art. 61, §2º.
Sufrágio universal | direito de votar e ser votado atribuído a todos os cidadãos, sem restrições de renda, instrução ou sexo | CF, art. 14.
Voto obrigatório | dever de votar imposto aos alfabetizados maiores de 18 anos e menores de 70 anos | CF, art. 14, §1º, I.
Voto facultativo | direito, e não dever, de votar atribuído aos analfabetos, aos maiores de 70 anos e aos jovens de 16 e 17 anos | CF, art. 14, §1º, II.
República | forma de governo em que o chefe de Estado é eleito para mandato temporário e o poder é exercido em nome do povo | CF, art. 1º.
Federação | forma de Estado composta por entes autônomos (União, estados, DF e municípios) unidos de modo indissolúvel | CF, art. 1º e 18.
Separação de Poderes | divisão das funções estatais entre Legislativo, Executivo e Judiciário, independentes e harmônicos entre si | CF, art. 2º.
Cláusulas pétreas | matérias que não podem ser objeto de emenda tendente a aboli-las, como a forma federativa e a separação dos Poderes | CF, art. 60, §4º.
Poder constituinte originário | poder inicial, ilimitado juridicamente e incondicionado, que instaura uma nova ordem constitucional | Foi exercido pela Assembleia Nacional Constituinte de 1987-1988.
Poder constituinte derivado reformador | poder de alterar o texto constitucional por meio de emendas, sujeito aos limites previstos na própria Constituição | CF, art. 60.
Constituição rígida | aquela cuja alteração exige processo legislativo mais solene e difícil que o das leis ordinárias | A CF/88 é rígida: exige 3/5 em dois turnos em cada Casa.
Supremacia da Constituição | princípio segundo o qual todas as normas do ordenamento devem ser compatíveis com a Constituição, fundamento de validade do sistema | Base do controle de constitucionalidade.
Estado Democrático de Direito | Estado submetido ao império da lei, com soberania popular, direitos fundamentais e separação de Poderes | CF, art. 1º, caput.
""")

# ------------------------------------------------------- PODERES E INSTITUIÇÕES
pool("poderes", "Organização do Estado", """
Poder Legislativo | exerce as funções de elaborar leis e fiscalizar o Poder Executivo, sendo exercido, na União, pelo Congresso Nacional | CF, art. 44.
Poder Executivo | administra o Estado e executa as leis, sendo exercido pelo Presidente da República, auxiliado pelos Ministros de Estado | CF, art. 76.
Poder Judiciário | aplica a lei aos casos concretos, solucionando conflitos com independência e imparcialidade | CF, art. 92 e seguintes.
Congresso Nacional | órgão do Poder Legislativo federal composto pela Câmara dos Deputados e pelo Senado Federal | Estrutura bicameral (CF, art. 44).
Câmara dos Deputados | casa legislativa que representa o povo, com 513 membros eleitos pelo sistema proporcional | CF, art. 45.
Senado Federal | casa legislativa que representa os estados e o Distrito Federal, com 81 membros eleitos pelo princípio majoritário | CF, art. 46.
Assembleia Legislativa | órgão do Poder Legislativo estadual, composto por deputados estaduais | CF, art. 27.
Câmara Municipal | órgão do Poder Legislativo municipal, composto por vereadores | CF, art. 29.
Câmara Legislativa do Distrito Federal | órgão legislativo do DF, composto por deputados distritais, que acumula competências legislativas estaduais e municipais | CF, art. 32.
Tribunal de Contas da União | órgão que auxilia o Congresso Nacional no controle externo, julgando as contas dos administradores públicos federais | CF, art. 71.
Ministério Público | instituição permanente, essencial à função jurisdicional, que defende a ordem jurídica, o regime democrático e os interesses sociais e individuais indisponíveis | CF, art. 127.
Defensoria Pública | instituição essencial que presta orientação jurídica e defesa, em todos os graus, aos necessitados | CF, art. 134.
Advocacia-Geral da União | instituição que representa a União judicial e extrajudicialmente e presta consultoria jurídica ao Poder Executivo | CF, art. 131.
Conselho Nacional de Justiça | órgão do Judiciário que controla a atuação administrativa e financeira dos tribunais e o cumprimento dos deveres funcionais dos juízes | Criado pela EC 45/2004 (CF, art. 103-B).
Conselho Nacional do Ministério Público | órgão que controla a atuação administrativa e financeira do Ministério Público e o cumprimento dos deveres funcionais de seus membros | CF, art. 130-A.
""")

# ------------------------------------------------------------ STF E JUDICIÁRIO
pool("stf", "Poder Judiciário e STF", """
Supremo Tribunal Federal | guardião da Constituição Federal, composto por 11 ministros nomeados pelo Presidente da República após aprovação do Senado | CF, art. 101 e 102.
Superior Tribunal de Justiça | tribunal responsável por uniformizar a interpretação da lei federal em todo o país | CF, art. 105.
Tribunal Superior Eleitoral | órgão de cúpula da Justiça Eleitoral, responsável pela organização e julgamento das eleições | CF, art. 118 e 119.
Tribunal Superior do Trabalho | órgão de cúpula da Justiça do Trabalho | CF, art. 111-A.
Superior Tribunal Militar | órgão de cúpula da Justiça Militar da União | CF, art. 122.
Tribunais Regionais Federais | tribunais que julgam, em segundo grau, as causas da Justiça Federal | CF, art. 106.
Tribunais de Justiça | tribunais de segundo grau da Justiça comum dos estados e do Distrito Federal | CF, art. 125.
Juizados Especiais | órgãos que julgam causas cíveis de menor complexidade e infrações penais de menor potencial ofensivo | CF, art. 98, I.
Tribunal do Júri | órgão competente para julgar os crimes dolosos contra a vida | CF, art. 5º, XXXVIII.
Súmula vinculante | enunciado do STF aprovado por 2/3 dos ministros, de observância obrigatória pelo Judiciário e pela Administração Pública | CF, art. 103-A (EC 45/2004).
Repercussão geral | requisito de admissibilidade do recurso extraordinário, exigindo questão relevante do ponto de vista econômico, político, social ou jurídico | CF, art. 102, §3º.
Ação Direta de Inconstitucionalidade (ADI) | ação de controle concentrado que questiona, perante o STF, lei ou ato normativo federal ou estadual contrário à Constituição | CF, art. 102, I, a.
Ação Declaratória de Constitucionalidade (ADC) | ação de controle concentrado que visa confirmar a constitucionalidade de lei ou ato normativo federal | CF, art. 102, I, a.
Arguição de Descumprimento de Preceito Fundamental (ADPF) | ação proposta ao STF para evitar ou reparar lesão a preceito fundamental decorrente de ato do Poder Público | CF, art. 102, §1º.
Controle difuso de constitucionalidade | aquele em que qualquer juiz ou tribunal pode afastar lei inconstitucional ao decidir um caso concreto | Efeitos, em regra, entre as partes.
Controle concentrado de constitucionalidade | aquele exercido em abstrato por um tribunal específico, por meio de ações como ADI e ADC | Efeitos, em regra, para todos (erga omnes).
Recurso extraordinário | recurso ao STF contra decisão de única ou última instância que contrarie dispositivo da Constituição | CF, art. 102, III.
""")

# ----------------------------------------------------- REMÉDIOS CONSTITUCIONAIS
pool("remedios", "Direitos e garantias fundamentais", """
Habeas corpus | protege a liberdade de locomoção quando ameaçada ou violada por ilegalidade ou abuso de poder | CF, art. 5º, LXVIII.
Habeas data | assegura o conhecimento e a retificação de informações pessoais constantes de registros ou bancos de dados de entidades governamentais ou públicas | CF, art. 5º, LXXII.
Mandado de segurança | protege direito líquido e certo não amparado por habeas corpus ou habeas data, violado por autoridade pública | CF, art. 5º, LXIX.
Mandado de segurança coletivo | pode ser impetrado por partido político com representação no Congresso, organização sindical, entidade de classe ou associação | CF, art. 5º, LXX.
Mandado de injunção | cabível quando a falta de norma regulamentadora torna inviável o exercício de direitos e liberdades constitucionais | CF, art. 5º, LXXI.
Ação popular | permite a qualquer cidadão anular ato lesivo ao patrimônio público, à moralidade administrativa, ao meio ambiente ou ao patrimônio histórico e cultural | CF, art. 5º, LXXIII.
Ação civil pública | instrumento para defesa de interesses difusos e coletivos, como o meio ambiente e o consumidor, ajuizado por legitimados como o Ministério Público | CF, art. 129, III, e Lei 7.347/1985.
Direito de petição | direito de dirigir-se aos Poderes Públicos em defesa de direitos ou contra ilegalidade ou abuso de poder, independentemente do pagamento de taxas | CF, art. 5º, XXXIV, a.
Direito de certidão | direito de obter certidões em repartições públicas para defesa de direitos e esclarecimento de situações de interesse pessoal | CF, art. 5º, XXXIV, b.
""")

pool("art5", "Art. 5º da Constituição Federal", """
Princípio da legalidade | ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de lei | CF, art. 5º, II.
Anterioridade penal | não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal | CF, art. 5º, XXXIX.
Irretroatividade da lei penal | a lei penal não retroagirá, salvo para beneficiar o réu | CF, art. 5º, XL.
Presunção de inocência | ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória | CF, art. 5º, LVII.
Devido processo legal | ninguém será privado da liberdade ou de seus bens sem que haja processo regular | CF, art. 5º, LIV.
Contraditório e ampla defesa | garantia assegurada aos litigantes, em processo judicial ou administrativo, com os meios e recursos a ela inerentes | CF, art. 5º, LV.
Inafastabilidade da jurisdição | a lei não excluirá da apreciação do Poder Judiciário lesão ou ameaça a direito | CF, art. 5º, XXXV.
Vedação às provas ilícitas | são inadmissíveis, no processo, as provas obtidas por meios ilícitos | CF, art. 5º, LVI.
Função social da propriedade | a propriedade atenderá à sua função social | CF, art. 5º, XXIII.
Liberdade de manifestação do pensamento | é livre a manifestação do pensamento, sendo vedado o anonimato | CF, art. 5º, IV.
Direito de reunião | todos podem reunir-se pacificamente, sem armas, em locais abertos ao público, independentemente de autorização | CF, art. 5º, XVI.
Inviolabilidade do domicílio | a casa é asilo inviolável do indivíduo, salvo consentimento, flagrante delito, desastre, socorro ou, durante o dia, ordem judicial | CF, art. 5º, XI.
Racismo | crime inafiançável e imprescritível, sujeito à pena de reclusão | CF, art. 5º, XLII.
Tortura, tráfico de drogas, terrorismo e crimes hediondos | crimes considerados inafiançáveis e insuscetíveis de graça ou anistia | CF, art. 5º, XLIII.
Pena de morte | sanção vedada pela Constituição, salvo em caso de guerra declarada | CF, art. 5º, XLVII, a.
Juiz natural | ninguém será processado nem sentenciado senão pela autoridade competente, sendo vedados tribunais de exceção | CF, art. 5º, XXXVII e LIII.
""")

# ------------------------------------------------------ PROCESSO LEGISLATIVO
pool("proclegis", "Processo legislativo", """
Emenda constitucional | espécie normativa que altera o texto da Constituição, aprovada por 3/5 dos membros de cada Casa em dois turnos | CF, art. 60.
Lei complementar | espécie normativa que regulamenta matérias previstas na Constituição e exige aprovação por maioria absoluta | CF, art. 69.
Lei ordinária | espécie comum de lei, aprovada por maioria simples, presente a maioria absoluta dos membros da Casa | CF, art. 47.
Lei delegada | ato elaborado pelo Presidente da República mediante delegação do Congresso Nacional, feita por resolução | CF, art. 68.
Medida provisória | ato com força de lei editado pelo Presidente da República em caso de relevância e urgência, com vigência de 60 dias prorrogáveis por mais 60 | CF, art. 62.
Decreto legislativo | ato do Congresso Nacional para matérias de sua competência exclusiva, como aprovar tratados internacionais, sem sanção presidencial | CF, art. 49.
Resolução | ato do Congresso ou de suas Casas para matérias de competência privativa, sem sanção presidencial | CF, art. 59, VII.
Decreto regulamentar | ato do chefe do Poder Executivo para regulamentar a lei e garantir sua fiel execução | CF, art. 84, IV.
Projeto de lei | proposta de norma jurídica submetida à tramitação nas Casas Legislativas | CF, art. 61 e seguintes.
Veto | recusa do chefe do Poder Executivo a projeto de lei, por inconstitucionalidade (jurídico) ou contrariedade ao interesse público (político) | CF, art. 66, §1º.
Sanção | aquiescência do chefe do Poder Executivo ao projeto aprovado pelo Legislativo, que o transforma em lei | CF, art. 66.
Promulgação | ato que atesta a existência da lei e determina sua executoriedade | Ato do chefe do Executivo (CF, art. 84, IV).
Publicação | ato que dá conhecimento da lei a todos e é condição para sua eficácia | Ocorre no Diário Oficial.
Iniciativa legislativa | ato que deflagra o processo legislativo, exercido por quem a Constituição atribui essa competência | CF, art. 61.
Urgência constitucional | solicitação do Presidente para que o projeto seja apreciado em 45 dias em cada Casa, sob pena de trancar a pauta | CF, art. 64.
Sessão conjunta | reunião de deputados e senadores, utilizada, por exemplo, para apreciar vetos presidenciais | CF, art. 57, §3º.
Comissão de Constituição e Justiça (CCJ) | comissão que analisa a constitucionalidade, a juridicidade e a legalidade das proposições | Etapa obrigatória na tramitação.
""")

# ---------------------------------------------------------------- QUÓRUNS (só F1)
pool("quorum", "Votações no Congresso e no STF", """
Aprovação de proposta de emenda à Constituição | 3/5 dos membros de cada Casa (308 deputados e 49 senadores), em dois turnos de votação | CF, art. 60, §2º.
Aprovação de lei complementar | maioria absoluta dos membros de cada Casa, votando separadamente (257 deputados e 41 senadores) | CF, art. 69.
Aprovação de lei ordinária | maioria simples dos votos, desde que presente a maioria absoluta dos membros da Casa | CF, art. 47.
Autorização, pela Câmara, para processar o Presidente da República | 2/3 dos deputados (342 votos) | CF, art. 51, I.
Condenação do Presidente da República por crime de responsabilidade | 2/3 dos senadores (54 votos), com perda do cargo e inabilitação por oito anos | CF, art. 52, parágrafo único.
Rejeição de veto presidencial | maioria absoluta de deputados e de senadores, em sessão conjunta | CF, art. 66, §4º.
Aprovação de súmula vinculante pelo STF | 2/3 dos ministros do Supremo (8 dos 11 ministros) | CF, art. 103-A.
Aprovação, pelo Senado, de indicado a ministro do STF | maioria absoluta dos senadores (41 votos), após sabatina na Comissão de Constituição e Justiça | CF, art. 101, parágrafo único.
Cassação do mandato de deputado ou senador por quebra de decoro | maioria absoluta dos membros da respectiva Casa, em votação aberta | CF, art. 55, §2º (EC 76/2013).
Criação de Comissão Parlamentar de Inquérito (CPI) | requerimento de 1/3 dos membros da Casa (171 deputados ou 27 senadores), para apurar fato determinado por prazo certo | CF, art. 58, §3º.
Declaração de inconstitucionalidade por tribunal | maioria absoluta dos membros do tribunal ou de seu órgão especial (cláusula de reserva de plenário) | CF, art. 97.
Aprovação de medida provisória pelo Congresso | maioria simples em cada Casa, após parecer de comissão mista | CF, art. 62, §9º.
""", forms="1")
