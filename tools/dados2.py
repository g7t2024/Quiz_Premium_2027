# -*- coding: utf-8 -*-
from dados import pool, DEFAULT_S1, DEFAULT_S2

# -------------------------------------------------------------- FEDERALISMO
pool("federalismo", "Organização político-administrativa", """
Competência concorrente | competência em que União, Estados e DF legislam ao mesmo tempo, cabendo à União editar normas gerais | CF, art. 24.
Competência comum | competência administrativa em que União, Estados, DF e Municípios cooperam, como na proteção da saúde e do patrimônio histórico | CF, art. 23.
Competência privativa da União | competência legislativa atribuída à União, que pode ser delegada aos Estados por lei complementar em questões específicas | CF, art. 22, parágrafo único.
Competência suplementar | competência exercida pelos Estados para editar normas gerais na ausência de lei federal sobre o tema | CF, art. 24, §3º.
Autonomia dos entes federados | capacidade de auto-organização, autogoverno, normatização própria e autoadministração | Característica essencial da Federação.
Indissolubilidade do vínculo federativo | impossibilidade de secessão: os entes formam união indissolúvel, sem direito de se separar | CF, art. 1º.
Territórios Federais | entes integrantes da União, criados por lei complementar, sem autonomia política própria | CF, art. 18, §2º.
Criação, incorporação e desmembramento de Estados | ato que depende de aprovação da população diretamente interessada, por plebiscito, e de lei complementar | CF, art. 18, §3º.
Criação de Municípios | ato feito por lei estadual, após estudo de viabilidade e consulta prévia, mediante plebiscito, às populações envolvidas | CF, art. 18, §4º.
Princípio da simetria | exigência de que o modelo federal sirva de parâmetro para a organização dos Estados e Municípios | Construção da doutrina e do STF.
Intervenção federal | medida excepcional pela qual a União suspende temporariamente a autonomia de um Estado ou do DF para manter a integridade nacional ou repelir invasão | CF, art. 34.
Bens da União | patrimônio que inclui terras devolutas indispensáveis à defesa, rios que banhem mais de um Estado e as praias marítimas | CF, art. 20.
""")

# ------------------------------------------------------------ GOVERNO LOCAL
pool("municipio", "Município e Câmara de Vereadores", """
Vereador | representante do povo no Poder Legislativo municipal, eleito pelo sistema proporcional | CF, art. 29.
Prefeito | chefe do Poder Executivo municipal, eleito para mandato de quatro anos, com possibilidade de uma reeleição | CF, art. 29, I.
Lei Orgânica Municipal | norma que organiza o município, votada em dois turnos, com interstício mínimo de dez dias, e aprovada por 2/3 dos membros da Câmara | CF, art. 29, caput.
Subsídio dos vereadores | valor fixado pela Câmara Municipal em cada legislatura para a seguinte, observados os limites constitucionais | CF, art. 29, VI.
Imunidade material do vereador | inviolabilidade por opiniões, palavras e votos no exercício do mandato e na circunscrição do município | CF, art. 29, VIII.
Número de vereadores | quantidade proporcional à população do município, com mínimo de 9 e máximo de 55 | CF, art. 29, IV (EC 58/2009).
Plano diretor | instrumento básico da política de desenvolvimento e expansão urbana, obrigatório para cidades com mais de 20 mil habitantes | CF, art. 182, §1º.
Foro do prefeito | competência do Tribunal de Justiça para julgar o prefeito nos crimes comuns | CF, art. 29, X.
Controle externo municipal | fiscalização das contas do município exercida pela Câmara Municipal, com o auxílio do Tribunal de Contas | CF, art. 31.
Segundo turno municipal | eleição prevista para prefeito em municípios com mais de 200 mil eleitores quando nenhum candidato obtém maioria absoluta | CF, art. 29, II.
Iniciativa popular municipal | projetos de lei de interesse específico do município que podem ser propostos por, no mínimo, 5% do eleitorado | CF, art. 29, XIII.
Distrito Federal | ente que acumula competências estaduais e municipais, sendo vedada sua divisão em municípios | CF, art. 32.
""")

# ------------------------------------------------------------------ EXECUTIVO
pool("executivo", "Poder Executivo", """
Impeachment | processo por crime de responsabilidade, autorizado pela Câmara dos Deputados e julgado pelo Senado Federal | CF, art. 51, I, e art. 52, I.
Crime de responsabilidade | infração político-administrativa que atenta contra a Constituição, definida na Lei 1.079/1950 | CF, art. 85.
Veto total | recusa do Presidente a todo o projeto de lei | CF, art. 66, §1º.
Veto parcial | recusa que abrange texto integral de artigo, parágrafo, inciso ou alínea | CF, art. 66, §2º.
Sanção tácita | ocorre quando o Presidente deixa transcorrer 15 dias úteis sem se manifestar sobre o projeto | CF, art. 66, §3º.
Vice-Presidente da República | substitui o Presidente em seus impedimentos e o sucede em caso de vaga, além de exercer funções previstas em lei complementar | CF, art. 79.
Linha sucessória presidencial | ordem de substituição formada pelo Vice-Presidente, pelo Presidente da Câmara, pelo Presidente do Senado e pelo Presidente do STF | CF, art. 80.
Ministro de Estado | auxiliar do Presidente, brasileiro maior de 21 anos e no exercício dos direitos políticos, de livre nomeação e exoneração | CF, art. 87.
Conselho da República | órgão superior de consulta do Presidente da República, que opina sobre intervenção federal, estado de defesa e estado de sítio | CF, art. 89.
Conselho de Defesa Nacional | órgão de consulta do Presidente sobre assuntos ligados à soberania nacional e à defesa do Estado democrático | CF, art. 91.
Estado de defesa | medida decretada para preservar a ordem pública ou a paz social em locais restritos e determinados, ameaçadas por grave e iminente instabilidade institucional ou calamidade | CF, art. 136.
Estado de sítio | medida mais grave, dependente de autorização prévia do Congresso Nacional, cabível em caso de comoção grave de repercussão nacional ou de guerra | CF, art. 137.
Indulto | ato de clemência do Presidente da República que extingue ou comuta penas | CF, art. 84, XII.
Reeleição | possibilidade de Presidente, governadores e prefeitos disputarem um único período subsequente | CF, art. 14, §5º (EC 16/1997).
Comando supremo das Forças Armadas | atribuição privativa do Presidente da República sobre a Marinha, o Exército e a Aeronáutica | CF, art. 84, XIII.
""")

# ------------------------------------------------------------- LEGISLATIVO
pool("legislativo", "Congresso Nacional e parlamentares", """
Bicameralismo | sistema legislativo composto por duas casas, no Brasil a Câmara dos Deputados e o Senado Federal | CF, art. 44.
Legislatura | período de quatro anos, correspondente ao mandato dos deputados federais | CF, art. 44, parágrafo único.
Sessão legislativa | período anual de funcionamento do Congresso, de 2 de fevereiro a 17 de julho e de 1º de agosto a 22 de dezembro | CF, art. 57.
Imunidade material parlamentar | inviolabilidade civil e penal dos parlamentares por quaisquer opiniões, palavras e votos | CF, art. 53, caput.
Imunidade formal parlamentar | regra pela qual deputados e senadores só podem ser presos em flagrante de crime inafiançável, com decisão final da Casa sobre a prisão | CF, art. 53, §2º.
Foro por prerrogativa de função | julgamento de deputados e senadores pelo STF nas infrações penais comuns | CF, art. 53, §1º.
Comissão Parlamentar de Inquérito (CPI) | comissão com poderes de investigação próprios das autoridades judiciais, criada para apurar fato determinado por prazo certo | CF, art. 58, §3º.
Comissão mista | comissão formada por deputados e senadores, como a que analisa as medidas provisórias | CF, art. 62, §9º.
Quebra de decoro parlamentar | conduta de deputado ou senador, como abuso de prerrogativas ou percepção de vantagens indevidas, que pode levar à perda do mandato | CF, art. 55, II e §1º.
Suplente de senador | substituto eleito junto com o titular, que assume em caso de vaga ou de licença superior a 120 dias | CF, art. 46, §3º, e art. 56, §1º.
Sistema proporcional | sistema eleitoral usado para eleger deputados federais, estaduais, distritais e vereadores | CF, art. 45.
Sistema majoritário | sistema eleitoral usado para eleger Presidente, governadores, prefeitos e senadores | CF, art. 46 e 77.
Quociente eleitoral | resultado da divisão dos votos válidos pelo número de vagas, usado para distribuir as cadeiras no sistema proporcional | Código Eleitoral, art. 106.
Mesa do Congresso Nacional | órgão dirigente do Congresso, presidido pelo Presidente do Senado Federal | CF, art. 57, §5º.
""")

# ------------------------------------------------------------------ BRASÍLIA
pool("brasilia", "Brasília e os Três Poderes", """
Brasília | capital federal do Brasil e sede dos Poderes da União, inaugurada em 21 de abril de 1960 | CF, art. 18, §1º.
Juscelino Kubitschek | presidente da República responsável pela construção e pela inauguração de Brasília | Governo de 1956 a 1961 (Plano de Metas, "50 anos em 5").
Lúcio Costa | urbanista autor do Plano Piloto de Brasília | Vencedor do concurso público de 1957.
Oscar Niemeyer | arquiteto autor dos principais edifícios públicos de Brasília | Projetou o Congresso, o Planalto, o Alvorada e a Catedral.
Praça dos Três Poderes | espaço que reúne o Palácio do Planalto, o Congresso Nacional e o Supremo Tribunal Federal | Simboliza a harmonia entre os Poderes.
Palácio do Planalto | sede do Poder Executivo federal e local de trabalho do Presidente da República | Fica na Praça dos Três Poderes.
Palácio da Alvorada | residência oficial do Presidente da República | Projeto de Oscar Niemeyer.
Palácio do Jaburu | residência oficial do Vice-Presidente da República | Localizado às margens do Lago Paranoá.
Palácio do Itamaraty | sede do Ministério das Relações Exteriores | Conhecido como "Palácio dos Arcos".
Esplanada dos Ministérios | eixo urbano onde se concentram os edifícios dos ministérios do governo federal | Parte do Eixo Monumental de Brasília.
Palácio do Congresso Nacional | sede do Poder Legislativo federal, formada por duas cúpulas e duas torres gêmeas | Projeto de Oscar Niemeyer.
Catedral Metropolitana de Brasília | templo projetado por Niemeyer, formado por 16 colunas curvas que lembram uma coroa | Inaugurada em 1970.
Plano Piloto | projeto urbanístico da capital, cujo traçado lembra a forma de um avião | Obra de Lúcio Costa.
Salvador | primeira capital do Brasil, até 1763 | Foi sede do governo-geral colonial.
Rio de Janeiro | capital do Brasil de 1763 até a inauguração de Brasília, em 1960 | Foi também capital do Império e da Primeira República.
""")

# ----------------------------------------------------------- CONSTITUIÇÕES
pool("historia", "História constitucional brasileira", """
Constituição de 1824 | outorgada por D. Pedro I, previu o Poder Moderador e vigorou durante o Império | Primeira Constituição do Brasil.
Constituição de 1891 | primeira da República, que adotou o federalismo e o presidencialismo, inspirada no modelo dos Estados Unidos | Texto redigido sob influência de Rui Barbosa.
Constituição de 1934 | texto de curta duração que previu direitos trabalhistas e sociais e constitucionalizou o voto feminino | Inspirada na Constituição alemã de Weimar.
Constituição de 1937 | conhecida como "Polaca", foi outorgada por Getúlio Vargas no início do Estado Novo | Concentrou poderes no Executivo.
Constituição de 1946 | texto que redemocratizou o país após o Estado Novo | Restabeleceu eleições e a separação de Poderes.
Constituição de 1967 | texto que consolidou o regime militar, com forte concentração de poder no Executivo | Foi profundamente alterada pela EC 1/1969.
Emenda Constitucional nº 1/1969 | alteração tão extensa da Constituição de 1967 que é vista, na prática, como uma nova Constituição | Editada pela Junta Militar.
Constituição de 1988 | chamada de Constituição Cidadã, promulgada em 5 de outubro de 1988, após o fim do regime militar | Ampliou direitos fundamentais.
Assembleia Nacional Constituinte | órgão instalado em 1987 e responsável pela elaboração da Constituição de 1988 | Formada por deputados e senadores eleitos em 1986.
Ulysses Guimarães | presidente da Assembleia Constituinte, que chamou a Constituição de 1988 de "Cidadã" | Discurso de promulgação em 5/10/1988.
Diretas Já | movimento popular de 1983 e 1984 que reivindicava eleições presidenciais diretas | Culminou na campanha pela Emenda Dante de Oliveira.
Ato Institucional nº 5 | norma editada em 1968 que endureceu o regime militar e permitiu o fechamento do Congresso | O AI-5 foi o instrumento mais duro da ditadura.
""")

# ----------------------------------------------------- ADMINISTRAÇÃO PÚBLICA
pool("admin", "Administração Pública (art. 37)", """
Princípio da legalidade administrativa | o administrador só pode fazer o que a lei autoriza | CF, art. 37, caput.
Princípio da impessoalidade | a atuação administrativa deve visar ao interesse público, sem favorecimentos ou perseguições pessoais | CF, art. 37, caput.
Princípio da moralidade | exige conduta ética, honesta e de boa-fé do agente público | CF, art. 37, caput.
Princípio da publicidade | exige transparência dos atos administrativos, salvo sigilo imprescindível à segurança da sociedade e do Estado | CF, art. 37, caput.
Princípio da eficiência | exige resultados de qualidade, com economicidade e agilidade, e foi incluído pela EC 19/1998 | CF, art. 37, caput.
Concurso público | forma de ingresso em cargo efetivo mediante aprovação em provas ou provas e títulos | CF, art. 37, II.
Estabilidade | garantia adquirida após três anos de efetivo exercício pelo servidor nomeado para cargo efetivo em virtude de concurso | CF, art. 41.
Teto remuneratório | limite constitucional correspondente ao subsídio mensal dos ministros do STF | CF, art. 37, XI.
Improbidade administrativa | conduta de agente público que gera enriquecimento ilícito, prejuízo ao erário ou violação a princípios da administração | CF, art. 37, §4º.
Licitação | procedimento prévio às contratações públicas, que assegura igualdade entre concorrentes e a proposta mais vantajosa | CF, art. 37, XXI.
Cargo em comissão | cargo de livre nomeação e exoneração, destinado apenas às atribuições de direção, chefia e assessoramento | CF, art. 37, V.
Vedação ao nepotismo | proibição de nomear parentes de autoridades para cargos em comissão, tema da Súmula Vinculante 13 | Decorre dos princípios da impessoalidade e moralidade.
Acumulação de cargos públicos | prática vedada, salvo exceções como dois cargos de professor ou um de professor e outro técnico ou científico, havendo compatibilidade de horários | CF, art. 37, XVI.
Responsabilidade civil do Estado | obrigação objetiva de indenizar os danos que seus agentes causarem a terceiros, com direito de regresso contra o responsável em caso de dolo ou culpa | CF, art. 37, §6º.
""")

# ---------------------------------------------------------------- ELEIÇÕES
pool("eleicoes", "Direitos políticos e eleições", """
Justiça Eleitoral | ramo do Judiciário que organiza, fiscaliza e julga as eleições, composto pelo TSE, TREs, juízes e juntas eleitorais | CF, art. 118.
Partido político | pessoa jurídica de direito privado, com autonomia para definir sua estrutura interna, que registra seu estatuto no TSE | CF, art. 17.
Elegibilidade | conjunto de condições para o cidadão ser votado, como nacionalidade, pleno exercício dos direitos políticos, alistamento, domicílio, filiação partidária e idade mínima | CF, art. 14, §3º.
Inelegibilidade | impedimento de o cidadão ser candidato, como o previsto na Lei da Ficha Limpa | CF, art. 14, §§4º a 9º.
Cláusula de desempenho | exigência de percentual mínimo de votos para que o partido tenha acesso ao fundo partidário e ao tempo gratuito de rádio e TV | CF, art. 17, §3º (EC 97/2017).
Fidelidade partidária | regra pela qual o parlamentar pode perder o mandato se mudar de partido sem justa causa | Entendimento do STF e do TSE, mandatos proporcionais.
Alistamento eleitoral | inscrição do cidadão como eleitor, obrigatória para os maiores de 18 anos | CF, art. 14, §1º, I.
Desincompatibilização | afastamento do cargo ou função pública para poder disputar uma eleição | LC 64/1990.
Cassação de direitos políticos | medida vedada pela Constituição | CF, art. 15.
Suspensão de direitos políticos | medida cabível, por exemplo, em caso de condenação criminal transitada em julgado, enquanto durarem seus efeitos | CF, art. 15, III.
Princípio da anualidade eleitoral | regra segundo a qual a lei que altera o processo eleitoral não se aplica à eleição que ocorra até um ano da data de sua vigência | CF, art. 16.
Domicílio eleitoral | circunscrição onde o cidadão está inscrito para votar e para ser candidato, exigida de quem quer disputar eleição | Lei 9.504/1997, art. 9º.
""")

# ------------------------------------------------------ EMENDAS CONSTITUCIONAIS
pool("emendas", "Emendas constitucionais", """
EC 16/1997 | permitiu a reeleição para os cargos de Presidente, governadores e prefeitos | Alterou o art. 14, §5º.
EC 19/1998 | Reforma Administrativa, que incluiu o princípio da eficiência na Administração Pública | Alterou o art. 37.
EC 32/2001 | restringiu a edição de medidas provisórias e fixou seu rito atual | Alterou o art. 62.
EC 45/2004 | Reforma do Judiciário, que criou o CNJ e a súmula vinculante | Introduziu os arts. 103-A e 103-B.
EC 66/2010 | simplificou o divórcio, eliminando a exigência de separação judicial prévia | Alterou o art. 226, §6º.
EC 72/2013 | ampliou os direitos dos trabalhadores domésticos, conhecida como "PEC das Domésticas" | Alterou o art. 7º, parágrafo único.
EC 95/2016 | instituiu o novo regime fiscal, conhecido como teto de gastos públicos | Previa limite às despesas primárias.
EC 103/2019 | Reforma da Previdência | Alterou regras de aposentadoria e pensão.
EC 132/2023 | Reforma Tributária sobre o consumo | Criou IBS, CBS e Imposto Seletivo.
EC 58/2009 | ajustou o número de vereadores à população dos municípios | Alterou o art. 29, IV.
EC 26/2000 | incluiu a moradia entre os direitos sociais | Alterou o art. 6º.
EC 64/2010 | incluiu a alimentação entre os direitos sociais | Alterou o art. 6º.
EC 90/2015 | incluiu o transporte entre os direitos sociais | Alterou o art. 6º.
EC 76/2013 | acabou com o voto secreto na perda de mandato parlamentar e na apreciação de vetos | Alterou os arts. 55 e 66.
EC 97/2017 | vedou coligações nas eleições proporcionais e criou a cláusula de desempenho | Alterou o art. 17.
""",
     s1="Qual emenda constitucional corresponde à seguinte descrição: «{x}»?",
     s2="A «{x}» ficou conhecida por:")

# --------------------------------------------------------------------- LEIS
pool("leis", "Legislação brasileira", """
Código de Defesa do Consumidor | norma que protege os direitos do consumidor nas relações de consumo | Lei 8.078/1990.
Estatuto da Criança e do Adolescente | norma que assegura a proteção integral a crianças e adolescentes | Lei 8.069/1990.
Lei de Acesso à Informação | norma que garante ao cidadão o direito de acessar informações públicas | Lei 12.527/2011.
Lei Maria da Penha | norma que cria mecanismos para coibir a violência doméstica e familiar contra a mulher | Lei 11.340/2006.
Marco Civil da Internet | norma que estabelece princípios, garantias, direitos e deveres para o uso da internet no Brasil | Lei 12.965/2014.
Lei Geral de Proteção de Dados | norma que regula o tratamento de dados pessoais, inclusive nos meios digitais | Lei 13.709/2018.
Estatuto da Pessoa Idosa | norma que regula os direitos das pessoas com idade igual ou superior a 60 anos | Lei 10.741/2003.
Lei de Improbidade Administrativa | norma que prevê sanções a agentes públicos por enriquecimento ilícito, dano ao erário e violação de princípios | Lei 8.429/1992.
Lei de Licitações e Contratos Administrativos | norma geral que disciplina as licitações e contratações da Administração Pública | Lei 14.133/2021.
Lei Anticorrupção | norma que responsabiliza objetivamente pessoas jurídicas por atos contra a administração pública | Lei 12.846/2013.
Lei de Responsabilidade Fiscal | norma que estabelece regras de finanças públicas voltadas à responsabilidade na gestão fiscal | Lei Complementar 101/2000.
Lei da Ficha Limpa | norma que ampliou as hipóteses de inelegibilidade | Lei Complementar 135/2010.
Lei dos Crimes de Responsabilidade | norma que define os crimes de responsabilidade e regula seu processo de julgamento | Lei 1.079/1950.
Código Eleitoral | norma que organiza o exercício dos direitos políticos e a Justiça Eleitoral | Lei 4.737/1965.
Estatuto da Pessoa com Deficiência | norma que assegura a inclusão e a cidadania das pessoas com deficiência | Lei 13.146/2015.
""")

pool("numleis", "Numeração de normas", """
Lei nº 8.078/1990 | Código de Defesa do Consumidor | Dispõe sobre a proteção do consumidor.
Lei nº 8.069/1990 | Estatuto da Criança e do Adolescente | Dispõe sobre a proteção integral à criança e ao adolescente.
Lei nº 12.527/2011 | Lei de Acesso à Informação | Regula o acesso a informações públicas.
Lei nº 11.340/2006 | Lei Maria da Penha | Combate a violência doméstica e familiar contra a mulher.
Lei nº 12.965/2014 | Marco Civil da Internet | Regula o uso da internet no Brasil.
Lei nº 13.709/2018 | Lei Geral de Proteção de Dados (LGPD) | Regula o tratamento de dados pessoais.
Lei nº 10.741/2003 | Estatuto da Pessoa Idosa | Protege os direitos da pessoa idosa.
Lei nº 8.429/1992 | Lei de Improbidade Administrativa | Pune atos de improbidade.
Lei nº 14.133/2021 | Nova Lei de Licitações e Contratos | Normas gerais de licitação.
Lei nº 12.846/2013 | Lei Anticorrupção | Responsabiliza pessoas jurídicas.
Lei Complementar nº 101/2000 | Lei de Responsabilidade Fiscal | Regula as finanças públicas.
Lei Complementar nº 135/2010 | Lei da Ficha Limpa | Amplia as inelegibilidades.
Lei nº 1.079/1950 | Lei dos Crimes de Responsabilidade | Define os crimes de responsabilidade.
Lei nº 4.737/1965 | Código Eleitoral | Organiza a Justiça Eleitoral.
Lei nº 13.146/2015 | Estatuto da Pessoa com Deficiência | Assegura a inclusão da pessoa com deficiência.
""",
     s1="Qual é a numeração da norma conhecida como «{x}»?",
     s2="A norma «{x}» é conhecida como:")

# --------------------------------------------------------- TERMOS JURÍDICOS
pool("termos", "Noções de Direito", """
Antinomia | conflito aparente entre duas normas válidas que regulam o mesmo assunto de modo diferente | Resolvida por critérios como hierarquia, cronologia e especialidade.
Vacatio legis | período entre a publicação da lei e sua entrada em vigor, que, se omissa a lei, é de 45 dias no Brasil | LINDB, art. 1º.
Ab-rogação | revogação total de uma lei anterior por lei posterior | LINDB, art. 2º, §1º.
Derrogação | revogação apenas parcial de uma lei anterior | LINDB, art. 2º, §1º.
Direito adquirido | direito que já se incorporou ao patrimônio de seu titular e não pode ser prejudicado pela lei nova | CF, art. 5º, XXXVI.
Ato jurídico perfeito | ato já consumado segundo a lei vigente ao tempo em que se efetuou | CF, art. 5º, XXXVI.
Coisa julgada | decisão judicial de que já não cabe recurso, protegida contra a lei nova | CF, art. 5º, XXXVI.
Jurisprudência | conjunto de decisões reiteradas dos tribunais sobre determinada matéria | Fonte do direito.
Doutrina | conjunto de estudos e opiniões dos juristas sobre o direito | Fonte do direito.
Analogia | aplicação, a um caso omisso, da norma prevista para caso semelhante | LINDB, art. 4º.
Súmula | resumo da jurisprudência dominante de um tribunal, sem caráter vinculante por si só | Não se confunde com a súmula vinculante do STF.
Liminar | decisão provisória e urgente proferida antes do julgamento final do processo | Exige plausibilidade do direito e risco de dano.
Quórum | número mínimo de membros presentes necessário para que um órgão colegiado delibere | Ex.: art. 47 da CF.
Maioria simples | mais votos favoráveis do que contrários, presente a maioria absoluta dos membros do órgão | CF, art. 47.
Maioria absoluta | mais da metade do total de membros do órgão, isto é, metade mais um | No Senado: 41; na Câmara: 257.
Maioria qualificada | percentual superior à maioria absoluta, como 3/5 ou 2/3 dos membros | Exigida para PEC, impeachment e outros atos.
Vigência | qualidade da norma que já está em vigor e que, portanto, pode ser exigida | Ligada ao tempo de existência da norma.
Eficácia | aptidão da norma para produzir efeitos concretos na realidade | Pode ser plena, contida ou limitada.
""")

# ---------------------------------------------------- NACIONALIDADE E SOCIAIS
pool("sociais", "Nacionalidade e direitos sociais", """
Brasileiro nato | pessoa nascida no Brasil, ainda que de pais estrangeiros, desde que estes não estejam a serviço de seu país | CF, art. 12, I, a.
Brasileiro naturalizado | estrangeiro que adquire a nacionalidade, como o residente há mais de 15 anos ininterruptos e sem condenação penal que a requeira | CF, art. 12, II, b.
Cargos privativos de brasileiro nato | cargos como Presidente da República, Presidentes da Câmara e do Senado e ministros do STF | CF, art. 12, §3º.
Perda da nacionalidade | consequência do cancelamento de naturalização por atividade nociva ao interesse nacional | CF, art. 12, §4º.
Direitos sociais | direitos como educação, saúde, alimentação, trabalho, moradia, transporte, lazer, segurança e previdência social | CF, art. 6º.
Salário mínimo | valor nacionalmente unificado, capaz de atender às necessidades vitais básicas do trabalhador e de sua família | CF, art. 7º, IV.
Licença-maternidade | direito de 120 dias, sem prejuízo do emprego e do salário | CF, art. 7º, XVIII.
Licença-paternidade | direito de cinco dias, nos termos fixados em lei, até que seja regulamentado | CF, art. 7º, XIX, e ADCT, art. 10, §1º.
Jornada de trabalho | duração normal de oito horas diárias e quarenta e quatro horas semanais | CF, art. 7º, XIII.
Férias anuais remuneradas | direito ao gozo de férias com, pelo menos, um terço a mais do que o salário normal | CF, art. 7º, XVII.
Direito de greve | direito assegurado aos trabalhadores, que decidem sobre a oportunidade de exercê-lo | CF, art. 9º.
Seguridade social | conjunto integrado de ações voltadas à saúde, à previdência e à assistência social | CF, art. 194.
Sistema Único de Saúde (SUS) | rede pública que assegura a saúde como direito de todos e dever do Estado, com acesso universal e igualitário | CF, art. 196 e 198.
""")

# --------------------------------------------------------- SEGURANÇA PÚBLICA
pool("seguranca", "Segurança pública e Forças Armadas", """
Polícia Federal | órgão que atua como polícia judiciária da União e apura crimes federais e contra a ordem política e social | CF, art. 144, I.
Polícia Rodoviária Federal | órgão destinado ao patrulhamento ostensivo das rodovias federais | CF, art. 144, II.
Polícia Ferroviária Federal | órgão destinado ao patrulhamento ostensivo das ferrovias federais | CF, art. 144, III.
Polícias Civis | órgãos estaduais de polícia judiciária e apuração de infrações penais, dirigidos por delegados de carreira | CF, art. 144, IV.
Polícias Militares | órgãos estaduais de polícia ostensiva e preservação da ordem pública | CF, art. 144, V.
Corpos de Bombeiros Militares | órgãos que executam atividades de defesa civil, além de prevenção e combate a incêndios | CF, art. 144, V e §5º.
Polícias Penais | órgãos vinculados ao órgão administrador do sistema penitenciário, na União, nos Estados e no DF | CF, art. 144, VI (EC 104/2019).
Guardas Municipais | órgãos destinados à proteção de bens, serviços e instalações do Município | CF, art. 144, §8º.
Forças Armadas | instituições compostas por Marinha, Exército e Aeronáutica, destinadas à defesa da Pátria sob o comando supremo do Presidente | CF, art. 142.
""")
