# -*- coding: utf-8 -*-
"""Atribuições por órgão (questões de associação) e questões escritas à mão."""

# Cada grupo: (nome, nome com artigo, base legal, [atribuições])
GRUPOS = [
    ("Congresso Nacional", "do Congresso Nacional", "CF, art. 49", """
resolver definitivamente sobre tratados, acordos ou atos internacionais que acarretem encargos ou compromissos gravosos ao patrimônio nacional
autorizar o Presidente da República a declarar guerra e a celebrar a paz
autorizar o Presidente e o Vice-Presidente a se ausentarem do País por mais de quinze dias
sustar os atos normativos do Poder Executivo que exorbitem do poder regulamentar
julgar anualmente as contas prestadas pelo Presidente da República
fixar os subsídios do Presidente, do Vice-Presidente e dos Ministros de Estado
aprovar o estado de defesa e a intervenção federal e autorizar o estado de sítio
autorizar referendo e convocar plebiscito
apreciar os atos de concessão e renovação de concessão de emissoras de rádio e televisão
zelar pela preservação de sua competência legislativa em face da atribuição normativa dos outros Poderes
"""),
    ("Câmara dos Deputados", "da Câmara dos Deputados", "CF, art. 51 e 64", """
autorizar, por dois terços de seus membros, a instauração de processo contra o Presidente, o Vice-Presidente e os Ministros de Estado
proceder à tomada de contas do Presidente quando não apresentadas ao Congresso no prazo de sessenta dias após a abertura da sessão legislativa
iniciar a discussão e votação dos projetos de lei de iniciativa do Presidente da República, do STF, dos Tribunais Superiores e dos cidadãos
"""),
    ("Senado Federal", "do Senado Federal", "CF, art. 52", """
processar e julgar o Presidente e o Vice-Presidente da República nos crimes de responsabilidade
processar e julgar os ministros do STF, o Procurador-Geral da República e o Advogado-Geral da União nos crimes de responsabilidade
aprovar previamente, após arguição pública, a escolha de ministros do Supremo Tribunal Federal
aprovar previamente a escolha dos chefes de missão diplomática de caráter permanente (embaixadores)
suspender a execução, no todo ou em parte, de lei declarada inconstitucional por decisão definitiva do STF
autorizar operações externas de natureza financeira de interesse da União, dos Estados, do Distrito Federal e dos Municípios
fixar limites globais para o montante da dívida consolidada da União, dos Estados, do Distrito Federal e dos Municípios
aprovar previamente a escolha do presidente e dos diretores do Banco Central
"""),
    ("Presidente da República", "do Presidente da República", "CF, art. 84", """
sancionar, promulgar e fazer publicar as leis, bem como expedir decretos e regulamentos para sua fiel execução
vetar projetos de lei, total ou parcialmente
nomear e exonerar os Ministros de Estado
manter relações com Estados estrangeiros e acreditar seus representantes diplomáticos
celebrar tratados, convenções e atos internacionais
editar medidas provisórias com força de lei
exercer o comando supremo das Forças Armadas
conceder indulto e comutar penas
nomear os ministros do Supremo Tribunal Federal
prover os cargos públicos federais, na forma da lei
enviar ao Congresso Nacional o plano plurianual, o projeto de lei de diretrizes orçamentárias e as propostas de orçamento
"""),
    ("Supremo Tribunal Federal", "do Supremo Tribunal Federal", "CF, art. 102 e 103-A", """
processar e julgar originariamente a ação direta de inconstitucionalidade de lei ou ato normativo federal ou estadual
processar e julgar originariamente a ação declaratória de constitucionalidade de lei ou ato normativo federal
julgar o Presidente da República, o Vice-Presidente, os membros do Congresso e o Procurador-Geral da República nas infrações penais comuns
julgar, mediante recurso extraordinário, as causas decididas em única ou última instância que contrariem dispositivo da Constituição
julgar originariamente o habeas corpus quando o paciente for o Presidente da República, o Vice-Presidente ou membros do Congresso Nacional
julgar os litígios entre Estados estrangeiros ou organismos internacionais e a União, os Estados, o Distrito Federal ou os Territórios
julgar a extradição solicitada por Estado estrangeiro
apreciar a arguição de descumprimento de preceito fundamental decorrente da Constituição
aprovar súmula com efeito vinculante, após reiteradas decisões sobre matéria constitucional
"""),
    ("Superior Tribunal de Justiça", "do Superior Tribunal de Justiça", "CF, art. 105", """
processar e julgar, nos crimes comuns, os Governadores dos Estados e do Distrito Federal
julgar, em recurso especial, as causas que contrariem tratado ou lei federal ou lhes neguem vigência
homologar sentenças estrangeiras e conceder exequatur às cartas rogatórias
processar e julgar originariamente os mandados de segurança contra atos de Ministro de Estado
julgar os conflitos de competência entre tribunais
"""),
    ("Ministério Público", "do Ministério Público", "CF, art. 129", """
promover, privativamente, a ação penal pública
zelar pelo efetivo respeito dos Poderes Públicos aos direitos assegurados na Constituição
promover o inquérito civil e a ação civil pública para proteção do patrimônio público e social, do meio ambiente e de outros interesses difusos e coletivos
exercer o controle externo da atividade policial
requisitar diligências investigatórias e a instauração de inquérito policial
expedir notificações nos procedimentos administrativos de sua competência, requisitando informações e documentos
"""),
    ("Municípios", "dos Municípios", "CF, art. 30", """
legislar sobre assuntos de interesse local
suplementar a legislação federal e a estadual no que couber
instituir e arrecadar o IPTU, o ISS e o ITBI
organizar e prestar, diretamente ou sob regime de concessão, os serviços públicos de interesse local, incluído o transporte coletivo
promover o adequado ordenamento territorial, mediante planejamento e controle do uso, do parcelamento e da ocupação do solo urbano
manter, com cooperação técnica e financeira da União e do Estado, programas de educação infantil e de ensino fundamental
"""),
    ("União", "da União", "CF, art. 21 e 22", """
emitir moeda
manter o serviço postal e o correio aéreo nacional
organizar e manter a polícia civil, a polícia militar e o corpo de bombeiros militar do Distrito Federal
explorar, diretamente ou mediante autorização, concessão ou permissão, os serviços de telecomunicações
elaborar e executar planos nacionais e regionais de ordenação do território e de desenvolvimento econômico e social
instituir sistema nacional de gerenciamento de recursos hídricos
executar os serviços de polícia marítima, aeroportuária e de fronteiras
legislar privativamente sobre direito civil, comercial, penal, processual, eleitoral, agrário, marítimo, aeronáutico, espacial e do trabalho
"""),
    ("Estados", "dos Estados", "CF, art. 25, 144 e 155", """
organizar-se e reger-se pelas Constituições e leis que adotarem, observados os princípios da Constituição Federal
exercer as competências remanescentes, isto é, as que não lhes sejam vedadas pela Constituição
explorar diretamente, ou mediante concessão, os serviços locais de gás canalizado
instituir regiões metropolitanas, aglomerações urbanas e microrregiões, mediante lei complementar estadual
instituir o ICMS, o IPVA e o ITCMD
manter as polícias civis, as polícias militares e os corpos de bombeiros militares, subordinados aos Governadores
"""),
]

# Questões escritas à mão: pergunta # correta # d1 # d2 # d3 # d4 # explicação
MANUAIS = """
## Congresso Nacional e eleições
Quantos deputados federais compõem a Câmara dos Deputados? # 513 # 435 # 594 # 81 # 350 # A Câmara dos Deputados é composta por 513 deputados federais, eleitos pelo sistema proporcional (CF, art. 45, e LC 78/1993).
Quantos senadores compõem o Senado Federal? # 81 # 27 # 54 # 99 # 513 # Cada Estado e o Distrito Federal elegem 3 senadores. Como são 26 Estados mais o DF (27 unidades), o total é 81 (CF, art. 46, §1º).
Quantos senadores cada Estado e o Distrito Federal elegem? # 3 # 2 # 4 # 1 # 5 # Cada Estado e o DF elegem três senadores, com dois suplentes cada (CF, art. 46, §§1º e 3º).
Qual é a duração do mandato de senador? # 8 anos # 4 anos # 6 anos # 5 anos # 10 anos # O mandato de senador é de oito anos (duas legislaturas), com renovação de 1/3 e 2/3 alternadamente (CF, art. 46, §§1º e 2º).
Qual é a duração do mandato de deputado federal? # 4 anos # 2 anos # 6 anos # 8 anos # 5 anos # Os deputados federais exercem mandato de quatro anos, igual a uma legislatura (CF, art. 44, parágrafo único).
Qual é a duração do mandato de vereador? # 4 anos # 2 anos # 6 anos # 8 anos # 5 anos # Os vereadores são eleitos para mandato de quatro anos (CF, art. 29, I).
Qual é a duração do mandato do Presidente da República? # 4 anos # 5 anos # 6 anos # 8 anos # 3 anos # O mandato do Presidente da República é de quatro anos, com possibilidade de uma reeleição (CF, art. 82 e art. 14, §5º).
Como ocorre a renovação do Senado Federal? # Por um terço e dois terços, alternadamente, a cada quatro anos # Por inteiro, a cada oito anos # Pela metade, a cada dois anos # Por inteiro, a cada quatro anos # Por um quarto a cada ano # A representação de cada Estado e do DF é renovada de quatro em quatro anos, alternadamente, por um e por dois terços (CF, art. 46, §2º).
Qual é o número mínimo de deputados federais por Estado? # 8 # 6 # 10 # 12 # 3 # A lei complementar estabelece que nenhuma unidade da Federação terá menos de oito nem mais de setenta deputados federais (CF, art. 45, §1º).
Qual é o número máximo de deputados federais por Estado? # 70 # 60 # 80 # 65 # 100 # Nenhum Estado terá mais de setenta deputados federais, nem menos de oito (CF, art. 45, §1º).
O número de deputados estaduais de uma Assembleia Legislativa corresponde: # Ao triplo da representação do Estado na Câmara dos Deputados, com acréscimos a partir de 36 # Ao dobro da representação do Estado na Câmara # Ao mesmo número de deputados federais do Estado # A metade da representação do Estado na Câmara # Ao quádruplo do número de senadores do Estado # Até atingir 36, é o triplo da bancada federal; acima disso, soma-se um para cada deputado federal além de doze (CF, art. 27).
Qual é o número mínimo e o máximo de vereadores de um município? # De 9 a 55 # De 7 a 45 # De 11 a 60 # De 9 a 40 # De 5 a 50 # A Constituição fixa o número de vereadores proporcionalmente à população, entre mínimo de 9 e máximo de 55 (CF, art. 29, IV, com a EC 58/2009).
Quem preside o Congresso Nacional? # O Presidente do Senado Federal # O Presidente da Câmara dos Deputados # O Presidente do Supremo Tribunal Federal # O Vice-Presidente da República # O Presidente da República # A Mesa do Congresso Nacional é presidida pelo Presidente do Senado Federal (CF, art. 57, §5º).
Qual é a quantidade mínima de assinaturas para criar uma CPI no Senado Federal? # 27 senadores # 41 senadores # 54 senadores # 21 senadores # 14 senadores # A CPI é criada por requerimento de 1/3 dos membros da Casa (CF, art. 58, §3º). Como o Senado tem 81 membros, são necessários 27.
Qual é a quantidade mínima de assinaturas para criar uma CPI na Câmara dos Deputados? # 171 deputados # 257 deputados # 308 deputados # 342 deputados # 129 deputados # A CPI é criada por requerimento de 1/3 dos membros da Casa. Como a Câmara tem 513 deputados, são necessários 171 (CF, art. 58, §3º).
Quantos votos representam a maioria absoluta na Câmara dos Deputados? # 257 # 256 # 171 # 342 # 308 # A maioria absoluta é metade mais um do total: 513 ÷ 2 = 256,5, ou seja, 257 deputados.
Quantos votos representam a maioria absoluta no Senado Federal? # 41 # 40 # 27 # 54 # 49 # A maioria absoluta é metade mais um do total: 81 ÷ 2 = 40,5, ou seja, 41 senadores.
Quantos votos de deputados (3/5) são necessários para aprovar uma PEC na Câmara? # 308 # 257 # 342 # 171 # 310 # 3/5 de 513 deputados = 307,8, o que exige 308 votos, em dois turnos (CF, art. 60, §2º).
Quantos votos de senadores (3/5) são necessários para aprovar uma PEC no Senado? # 49 # 41 # 54 # 27 # 51 # 3/5 de 81 senadores = 48,6, o que exige 49 votos, em dois turnos (CF, art. 60, §2º).
Quantos votos de deputados (2/3) são necessários para autorizar o processo contra o Presidente da República? # 342 # 308 # 257 # 171 # 400 # 2/3 de 513 deputados = 342 votos (CF, art. 51, I).
Quantos votos de senadores (2/3) são necessários para condenar o Presidente da República por crime de responsabilidade? # 54 # 49 # 41 # 27 # 60 # 2/3 de 81 senadores = 54 votos, e a condenação acarreta perda do cargo e inabilitação por oito anos (CF, art. 52, parágrafo único).
Quantos ministros do STF são necessários (2/3) para aprovar uma súmula vinculante? # 8 ministros # 6 ministros # 7 ministros # 9 ministros # 11 ministros # A súmula vinculante exige decisão de 2/3 dos membros do Supremo, isto é, 8 dos 11 ministros (CF, art. 103-A).
Qual é o prazo de vigência de uma medida provisória? # 60 dias, prorrogáveis por mais 60 # 30 dias, prorrogáveis por mais 30 # 45 dias, prorrogáveis por mais 45 # 90 dias improrrogáveis # 120 dias improrrogáveis # A medida provisória vigora por 60 dias, prorrogáveis uma vez por igual período, e perde a eficácia se não for convertida em lei (CF, art. 62, §§3º e 7º).
Qual é o prazo de que dispõe o Presidente para sancionar ou vetar um projeto de lei? # 15 dias úteis # 10 dias úteis # 30 dias corridos # 20 dias úteis # 5 dias úteis # O Presidente tem 15 dias úteis, contados do recebimento, para sancionar ou vetar; o silêncio importa sanção tácita (CF, art. 66, §§1º e 3º).
Qual é o prazo da urgência constitucional solicitada pelo Presidente para apreciação de projeto em cada Casa? # 45 dias # 30 dias # 60 dias # 90 dias # 15 dias # Se a Câmara e o Senado não se manifestarem em até 45 dias sobre projeto com urgência, sobrestam-se as demais deliberações da Casa (CF, art. 64, §§1º e 2º).
Qual percentual do eleitorado nacional é necessário para propor um projeto de lei de iniciativa popular? # 1% # 5% # 10% # 2% # 0,5% # O projeto deve ser subscrito por pelo menos 1% do eleitorado nacional, distribuído por cinco Estados, com no mínimo 0,3% de eleitores em cada um (CF, art. 61, §2º).
Em qual data ocorre o primeiro turno das eleições para Presidente da República? # No primeiro domingo de outubro do ano anterior ao término do mandato # No último domingo de outubro # No primeiro domingo de novembro # Em 15 de novembro # Em 7 de setembro # Pela Constituição, o primeiro turno ocorre no primeiro domingo de outubro (CF, art. 77).
Em qual data ocorre o segundo turno das eleições para Presidente da República? # No último domingo de outubro # No primeiro domingo de novembro # No segundo domingo de outubro # Em 15 de novembro # No primeiro domingo de dezembro # O segundo turno, quando necessário, ocorre no último domingo de outubro (CF, art. 77).
Vagos os cargos de Presidente e Vice-Presidente nos dois últimos anos do mandato, a eleição será: # Indireta, pelo Congresso Nacional, 30 dias depois da última vaga # Direta, no prazo de 90 dias # Direta, em até 30 dias # Indireta, pelo STF, em 60 dias # Direta, em 180 dias # Na segunda metade do mandato a eleição é indireta, feita pelo Congresso Nacional em 30 dias (CF, art. 81, §1º).
Vagos os cargos de Presidente e Vice-Presidente nos dois primeiros anos do mandato, a eleição será: # Direta, 90 dias depois da última vaga # Indireta, pelo Congresso, em 30 dias # Indireta, pelo Senado, em 90 dias # Direta, em 30 dias # Indireta, em 180 dias # Na primeira metade do mandato a eleição é direta, em até 90 dias depois de aberta a última vaga (CF, art. 81).
Na ausência do Presidente e do Vice-Presidente, quem é chamado em primeiro lugar a exercer a Presidência? # O Presidente da Câmara dos Deputados # O Presidente do Senado Federal # O Presidente do STF # O Procurador-Geral da República # O Ministro da Defesa # A linha sucessória é: Presidente da Câmara, Presidente do Senado e Presidente do STF (CF, art. 80).
Quem preside a sessão de julgamento do Presidente da República por crime de responsabilidade no Senado? # O Presidente do Supremo Tribunal Federal # O Presidente do Senado Federal # O Presidente da Câmara dos Deputados # O Procurador-Geral da República # O Vice-Presidente da República # Nos julgamentos do Presidente da República, o Senado funciona sob a presidência do Presidente do STF (CF, art. 52, parágrafo único).

## Idade mínima e direitos políticos
Qual é a idade mínima para ser Presidente da República? # 35 anos # 30 anos # 21 anos # 40 anos # 18 anos # Presidente, Vice-Presidente e Senador exigem idade mínima de 35 anos (CF, art. 14, §3º, VI, a).
Qual é a idade mínima para ser Governador de Estado? # 30 anos # 35 anos # 21 anos # 25 anos # 18 anos # Governador e Vice-Governador exigem 30 anos (CF, art. 14, §3º, VI, b).
Qual é a idade mínima para ser Senador? # 35 anos # 30 anos # 21 anos # 25 anos # 40 anos # Senador exige idade mínima de 35 anos, a mesma do Presidente (CF, art. 14, §3º, VI, a).
Qual é a idade mínima para ser Deputado Federal? # 21 anos # 18 anos # 25 anos # 30 anos # 35 anos # Deputado federal, estadual ou distrital, prefeito e vice-prefeito exigem 21 anos (CF, art. 14, §3º, VI, c).
Qual é a idade mínima para ser Prefeito? # 21 anos # 18 anos # 25 anos # 30 anos # 35 anos # Prefeito e Vice-Prefeito exigem 21 anos (CF, art. 14, §3º, VI, c).
Qual é a idade mínima para ser Vereador? # 18 anos # 16 anos # 21 anos # 25 anos # 30 anos # Vereador exige idade mínima de 18 anos (CF, art. 14, §3º, VI, d).
O voto é facultativo para: # Analfabetos, maiores de 70 anos e jovens de 16 e 17 anos # Apenas os analfabetos # Maiores de 60 anos e analfabetos # Menores de 21 e maiores de 65 anos # Servidores públicos e militares # O alistamento e o voto são facultativos para analfabetos, maiores de 70 anos e maiores de 16 e menores de 18 anos (CF, art. 14, §1º, II).

## Poder Judiciário e instituições
Quantos ministros compõem o Supremo Tribunal Federal? # 11 # 9 # 7 # 13 # 15 # O STF é composto por onze ministros (CF, art. 101).
Qual é a idade exigida para ser nomeado ministro do STF? # Mais de 35 e menos de 70 anos # Mais de 30 e menos de 65 anos # Mais de 40 e menos de 75 anos # Mais de 21 e menos de 70 anos # Mais de 18 e menos de 65 anos # Os ministros do STF são escolhidos entre cidadãos com mais de 35 e menos de 70 anos, de notável saber jurídico e reputação ilibada (CF, art. 101).
Com que idade os ministros do STF se aposentam compulsoriamente? # 75 anos # 65 anos # 70 anos # 72 anos # 80 anos # A aposentadoria compulsória dos ministros do STF ocorre aos 75 anos (CF, art. 40, §1º, II, e art. 100 do ADCT, com a EC 88/2015).
Como são escolhidos os ministros do STF? # Nomeados pelo Presidente da República, após aprovação por maioria absoluta do Senado # Eleitos pelo voto direto da população # Escolhidos pelo Congresso Nacional em sessão conjunta # Indicados pelo CNJ e nomeados pelo Presidente do STF # Escolhidos por concurso público # Nomeação presidencial depois de aprovação, por maioria absoluta, do Senado Federal, após sabatina (CF, art. 101, parágrafo único).
Quantos ministros compõem o Tribunal Superior Eleitoral (TSE)? # 7 # 5 # 9 # 11 # 3 # O TSE tem sete membros: três ministros do STF, dois do STJ e dois advogados (CF, art. 119).
Quantos ministros compõem o Tribunal de Contas da União? # 9 # 7 # 11 # 15 # 5 # O TCU é composto por nove ministros (CF, art. 73).
Quantos membros compõem o Conselho Nacional de Justiça (CNJ)? # 15 # 11 # 13 # 9 # 17 # O CNJ é composto por quinze membros (CF, art. 103-B).
Quantos membros compõem o Conselho Nacional do Ministério Público (CNMP)? # 14 # 15 # 11 # 12 # 9 # O CNMP é composto por quatorze membros (CF, art. 130-A).
Qual é o número mínimo de ministros do Superior Tribunal de Justiça? # 33 # 11 # 27 # 40 # 21 # O STJ é composto de, no mínimo, trinta e três ministros (CF, art. 104).
Quantos ministros compõem o Tribunal Superior do Trabalho? # 27 # 17 # 33 # 11 # 21 # O TST é composto por vinte e sete ministros (CF, art. 111-A).
Quantos ministros compõem o Superior Tribunal Militar? # 15 # 11 # 9 # 21 # 7 # O STM é composto por quinze ministros vitalícios, três da Marinha, quatro do Exército, três da Aeronáutica e cinco civis (CF, art. 123).
Qual é a duração do mandato do Procurador-Geral da República? # 2 anos, permitidas reconduções # 4 anos, vedada a recondução # 5 anos, vedada a recondução # 3 anos, com uma recondução # Vitalício # O PGR é nomeado pelo Presidente, após aprovação pela maioria absoluta do Senado, para mandato de dois anos, permitida a recondução (CF, art. 128, §1º).
Quem NÃO tem legitimidade para propor a ação direta de inconstitucionalidade (ADI)? # Qualquer cidadão # O Presidente da República # O Procurador-Geral da República # O Conselho Federal da OAB # Partido político com representação no Congresso Nacional # O rol do art. 103 da CF não inclui o cidadão individualmente. Presidente, PGR, OAB e partidos com representação no Congresso são legitimados.

## Fundamentos, forma de Estado e Constituição
A Constituição Federal de 1988 foi promulgada em: # 5 de outubro de 1988 # 5 de outubro de 1987 # 15 de novembro de 1988 # 7 de setembro de 1988 # 1º de janeiro de 1989 # A Constituição foi promulgada em 5 de outubro de 1988 pela Assembleia Nacional Constituinte, sob a presidência de Ulysses Guimarães.
Brasília foi inaugurada em: # 21 de abril de 1960 # 21 de abril de 1956 # 7 de setembro de 1960 # 15 de novembro de 1960 # 1º de maio de 1961 # Brasília foi inaugurada pelo presidente Juscelino Kubitschek em 21 de abril de 1960.
Quantos artigos possui o texto principal da Constituição Federal de 1988? # 250 # 200 # 300 # 188 # 350 # O corpo permanente da Constituição tem 250 artigos, além do Ato das Disposições Constitucionais Transitórias (ADCT).
Quantos incisos possui o art. 5º da Constituição Federal? # 78 # 68 # 70 # 77 # 80 # O art. 5º possui 78 incisos (I a LXXVIII), que tratam dos direitos e deveres individuais e coletivos.
Quantas unidades da Federação existem, sem contar o Distrito Federal? # 26 Estados # 27 Estados # 25 Estados # 24 Estados # 28 Estados # O Brasil possui 26 Estados e o Distrito Federal, totalizando 27 unidades da Federação.
Quantas regiões geográficas compõem o território brasileiro, segundo o IBGE? # 5 # 4 # 6 # 7 # 3 # O IBGE divide o país em cinco regiões: Norte, Nordeste, Centro-Oeste, Sudeste e Sul.
Quantos são os Poderes da União, independentes e harmônicos entre si? # Três # Dois # Quatro # Cinco # Seis # São Poderes da União o Legislativo, o Executivo e o Judiciário (CF, art. 2º).
Qual é a capital federal do Brasil? # Brasília # Rio de Janeiro # Salvador # São Paulo # Goiânia # A capital federal é Brasília (CF, art. 18, §1º).
Quanto à forma de governo, o Brasil adota: # A República # A Monarquia constitucional # O Parlamentarismo # A Confederação # A Diarquia # O art. 1º da CF adota a República. O parlamentarismo é sistema de governo e a confederação é forma de Estado.
Quanto à forma de Estado, o Brasil é: # Uma Federação # Um Estado unitário # Uma Confederação # Uma Monarquia # Um Estado regional # O Brasil é uma República Federativa, formada pela união indissolúvel de Estados, Municípios e do Distrito Federal (CF, art. 1º).
Quanto ao sistema de governo, o Brasil adota: # O presidencialismo # O parlamentarismo # O semipresidencialismo # O diretório # A monarquia # No Brasil, o Presidente da República é chefe de Estado e de governo. O presidencialismo foi mantido no plebiscito de 1993.
Qual alternativa NÃO é fundamento da República Federativa do Brasil (art. 1º da CF)? # Erradicação da pobreza e da marginalização # Soberania # Cidadania # Dignidade da pessoa humana # Pluralismo político # A erradicação da pobreza é objetivo fundamental (art. 3º), não fundamento. São fundamentos do art. 1º: soberania, cidadania, dignidade da pessoa humana, valores sociais do trabalho e da livre iniciativa, e pluralismo político.
Qual alternativa NÃO é objetivo fundamental da República (art. 3º da CF)? # Soberania # Construir uma sociedade livre, justa e solidária # Garantir o desenvolvimento nacional # Erradicar a pobreza e reduzir as desigualdades sociais e regionais # Promover o bem de todos, sem preconceitos # A soberania é fundamento (art. 1º), e não objetivo fundamental. Os objetivos estão no art. 3º.
Qual alternativa lista corretamente os fundamentos da República (art. 1º da CF)? # Soberania, cidadania, dignidade da pessoa humana, valores sociais do trabalho e da livre iniciativa e pluralismo político # Soberania, cidadania, dignidade da pessoa humana, erradicação da pobreza e pluralismo político # Soberania, democracia, federalismo, valores sociais do trabalho e pluralismo político # Cidadania, legalidade, moralidade, publicidade e eficiência # Soberania, igualdade, propriedade privada, segurança e pluralismo religioso # Esses cinco são os fundamentos expressos no art. 1º, incisos I a V, da Constituição Federal.
Qual alternativa NÃO é cláusula pétrea (art. 60, §4º da CF)? # O sistema de governo presidencialista # A forma federativa de Estado # O voto direto, secreto, universal e periódico # A separação dos Poderes # Os direitos e garantias individuais # O art. 60, §4º protege a forma federativa, o voto direto, secreto, universal e periódico, a separação dos Poderes e os direitos e garantias individuais. O sistema de governo não está no rol.
A Constituição Federal de 1988 é classificada como: # Escrita, rígida, analítica e promulgada # Escrita, flexível, sintética e outorgada # Não escrita, flexível, sintética e promulgada # Escrita, semirrígida, sintética e outorgada # Costumeira, rígida, analítica e promulgada # A CF/88 é escrita, rígida (exige processo especial de reforma), analítica (extensa) e promulgada (democrática).
Quem acumula as funções de chefe de Estado e de chefe de governo no Brasil? # O Presidente da República # O Primeiro-Ministro # O Presidente do Senado # O Presidente do STF # O Vice-Presidente da República # No presidencialismo brasileiro, o Presidente da República acumula as duas funções (CF, art. 76).
"""
