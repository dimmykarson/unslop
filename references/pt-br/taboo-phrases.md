# Catálogo de vícios de IA em português (pt-BR)

Texto gerado por IA em português tem marcas previsíveis, muitas delas traduzidas do inglês. Este catálogo organiza essas marcas nas **mesmas categorias** do catálogo em inglês (`references/taboo-phrases.md`), com o identificador da categoria entre crases, para a fase 2 transformá-lo em dados.

**Severidade:** **forte** = quase sempre é vício; corrija quando confirmado no contexto. **Fraca** = só é vício em excesso, sem fato por trás ou fora do gênero; avalie.

**Regra geral:** uma ocorrência no catálogo é *suspeita*, não sentença. Antes de editar, confirme o defeito no contexto (o que a expressão esconde, repete, exagera ou contradiz) e confira as proteções no fim deste arquivo. Exemplos citados entre aspas, em blocos de citação ou em código são ilustrações, não texto a reescrever.

**Quando a troca pede um fato que o texto não tem** ("dizer o que faz", "dizer o efeito", "dar o número"): procure o fato no próprio texto. Se não houver, **apague** o trecho vazio; se a frase inteira ficar vazia, apague a frase. Nunca invente um verbo, efeito, número ou juízo para preencher o lugar. Em reescrita, devolva só o texto limpo; a observação ao autor ("falta o dado de X") cabe apenas em auditoria (`--report`), na **Avaliação**.

## Sumário

1. Aberturas de enrolação — `throat_clearing`, `filler_opener`
2. Metacomentário e condução do leitor — `meta`, `reader_steering`
3. Vocabulário típico de IA — `ai_vocabulary`
4. Inflação de importância — `significance_inflation`
5. Linguagem promocional — `promotional`, `novelty_inflation`
6. Muletas de ênfase e enchimento — `emphasis_crutch`, `filler`
7. Gerúndio de análise vazia — `superficial_ing`
8. Atribuição vaga — `vague_attribution`
9. Fuga do verbo "ser" — `copula_avoidance`
10. Paralelismo negativo e falsa concessão — `negative_parallelism`, `false_concession`
11. Faixas falsas — `false_range`
12. Seção de desafios formulaica — `formulaic_challenges`
13. Perguntas retóricas — `rhetorical_question`, `rhetorical_setup`
14. Andaimes de conclusão — `conclusion_scaffold`, `generic_conclusion`
15. Artefatos de assistente — `assistant_artifact`, `acknowledgment_loop`, `communication_artifact`, `knowledge_cutoff`
16. Decalques do inglês — `calque` *(categoria nova, só pt-BR)*
17. Pontuação e formatação — `punctuation`
18. Estrutura — `structure`
19. Proteções — o que **não** mexer

---

## 1. Aberturas de enrolação — `throat_clearing`, `filler_opener`

Atrasam o conteúdo. Normalmente basta apagar e começar pela informação.

| Expressão | Sev. | Troca |
|---|---|---|
| "Vale ressaltar que" / "Vale destacar que" / "Vale lembrar que" | forte | apagar |
| "É importante destacar que" / "É importante ressaltar que" / "É importante salientar que" / "É importante mencionar que" | forte | apagar |
| "Cabe destacar que" / "Cabe ressaltar que" | forte | apagar (manter "cabe" só quando indica competência: "cabe à TI") |
| "É fundamental entender que" / "É fundamental compreender que" | forte | apagar |
| "Antes de mais nada," | fraca | apagar |
| "A verdade é que" / "O fato é que" | forte | apagar |
| "Sejamos sinceros:" / "Vamos combinar:" / "Vamos ser honestos:" | forte | apagar |
| "Bom, " / "Pois bem, " no início de texto escrito | fraca | apagar |
| "Quando falamos de X, " | fraca | começar por X |
| "Em linhas gerais, " | fraca | apagar quando o que segue já é geral |
| "Espero que esta mensagem o(s)/a(s) encontre bem" | forte | apagar (decalque de *I hope this message finds you well*; ver seção 16) |

## 2. Metacomentário e condução do leitor — `meta`, `reader_steering`

O texto fala de si mesmo em vez de dizer a coisa.

| Expressão | Sev. | Troca |
|---|---|---|
| "Neste artigo/texto/post, vamos explorar/abordar/entender" | forte | apagar; ou dizer o assunto diretamente no título |
| "Ao longo deste guia, você vai descobrir" | forte | apagar |
| "Confira a seguir" / "A seguir, confira" / "Acompanhe" | forte | apagar |
| "Vamos mergulhar nesse tema" / "Vamos lá!" / "Bora entender" | forte | apagar |
| "Sem mais delongas," | forte | apagar |
| "Como mencionado anteriormente," / "Como vimos," | fraca | apagar se não houver remissão necessária |
| "Continue lendo para saber" | forte | apagar |
| "Você vai se surpreender" | forte | apagar |
| "Entenda por que" / "Descubra como" em títulos de seção | fraca | título com o fato: "Prazo de 15 dias para recurso" |

## 3. Vocabulário típico de IA — `ai_vocabulary`

Palavras que aparecem em texto de IA muito acima da frequência humana. Fraca isoladamente; forte quando se acumulam ou estão no lugar de um fato.

| Expressão | Sev. | Troca |
|---|---|---|
| "mergulhar em", "mergulho profundo" (figurado) | forte | examinar, detalhar, estudar |
| "desvendar", "desmistificar" | fraca | explicar |
| "navegar pelo cenário/pelos desafios" | forte | lidar com, enfrentar |
| "cenário" (sem referente concreto) | fraca | situação, mercado, setor — ou apagar |
| "jornada" (fora de viagem/jornada de trabalho) | forte | processo, percurso — ou apagar |
| "tapeçaria", "mosaico", "sinfonia" (figurados) | forte | apagar a metáfora |
| "ecossistema" (figurado, sem sistema real) | fraca | conjunto, rede |
| "robusto", "robustez" (sem medida) | fraca | dizer o que aguenta: "suporta 10 mil acessos" |
| "alavancar", "potencializar", "impulsionar", "catapultar" | forte | aumentar, usar, melhorar — com o número, se houver |
| "sinergia", "holístico", "disruptivo", "transformador" | forte | apagar ou dizer o efeito |
| "crucial", "fundamental", "essencial", "primordial", "imprescindível" (em série) | fraca | manter um, quando justificado; cortar os demais |
| "intrincado", "multifacetado", "nuances" | fraca | complexo; ou listar as facetas |
| "panorama", "paradigma", "pilar", "catalisador" (figurados) | fraca | apagar ou dizer o concreto |
| "fomentar", "elevar", "aprimorar" (vagos) | fraca | dizer o que muda |
| "destravar o potencial" / "desbloquear o potencial" | forte | dizer o resultado |
| "um verdadeiro divisor de águas", "virada de chave", "game changer" | forte | dizer o que mudou |
| "solução" / "abordagem" (vagas, sem dizer qual) | fraca | nomear a ferramenta, o método |

## 4. Inflação de importância — `significance_inflation`

Atribui grandeza sem fato que a sustente.

| Expressão | Sev. | Troca |
|---|---|---|
| "desempenha um papel fundamental/crucial/essencial" | forte | dizer o que faz, se o texto disser ("aprova os pedidos"); se não, apagar a frase |
| "representa um marco/avanço significativo" | forte | dizer o que mudou, com dado |
| "redefine a forma como", "revoluciona" | forte | dizer o efeito concreto |
| "abre caminho para", "pavimenta o caminho" | fraca | permite, possibilita — ou dizer o próximo passo |
| "é um testemunho de", "reforça a importância de" | forte | apagar |
| "deixa um legado" | forte | apagar, salvo em contexto biográfico real |
| "Em um mundo cada vez mais conectado/digital/competitivo," | forte | apagar |
| "No cenário atual," / "Nos dias de hoje," / "Na era digital," / "Em tempos de" | forte | apagar ou dar a data |
| "cada vez mais" (sem dado de tendência) | fraca | apagar ou dar o número |

## 5. Linguagem promocional — `promotional`, `novelty_inflation`

| Expressão | Sev. | Troca |
|---|---|---|
| "imperdível", "incrível", "sensacional" | forte | apagar |
| "de ponta", "de última geração", "de excelência", "de alto nível" | fraca | dizer a característica |
| "solução completa", "tudo o que você precisa saber" | forte | dizer o que cobre |
| "experiência única/inesquecível" | forte | descrever a experiência |
| "leve X ao próximo nível", "eleve seu/sua X" | forte | dizer o ganho |
| "inovador", "pioneiro", "inédito" (sem comparação verificável) | fraca | apagar ou provar |

## 6. Muletas de ênfase e enchimento — `emphasis_crutch`, `filler`

| Expressão | Sev. | Troca |
|---|---|---|
| "de fato", "realmente", "simplesmente", "basicamente", "literalmente" | fraca | apagar |
| "sem dúvida", "sem sombra de dúvida", "certamente", "absolutamente" | fraca | apagar, salvo certeza sustentada |
| "extremamente", "incrivelmente", "altamente" (em série) | fraca | apagar ou dar a medida |
| "de forma significativa/eficaz/eficiente", "de maneira estratégica" | fraca | dizer quanto ou como |
| "de modo geral", "de forma geral" | fraca | apagar |
| "no que diz respeito a", "no que tange a" (fora de registro formal) | fraca | sobre, quanto a |
| "é possível observar que", "pode-se perceber que" | fraca | afirmar diretamente |

## 7. Gerúndio de análise vazia — `superficial_ing`

Frase que termina com gerúndio atribuindo efeito genérico. Equivalente ao "-ing" superficial do inglês. Também o **gerundismo** ("vou estar enviando").

| Padrão | Sev. | Troca |
|---|---|---|
| "…, contribuindo para o desenvolvimento/fortalecimento de…" | forte | apagar ou nova frase com o efeito medido |
| "…, garantindo assim mais eficiência/segurança" | forte | idem |
| "…, promovendo/reforçando/destacando a importância de…" | forte | apagar |
| "…, consolidando-se como referência" | forte | apagar |
| "vou estar enviando", "vamos estar analisando" | forte | vou enviar, vamos analisar |

## 8. Atribuição vaga — `vague_attribution`

| Expressão | Sev. | Troca |
|---|---|---|
| "Especialistas apontam/afirmam que" | forte | nomear a fonte ou apagar a atribuição |
| "Estudos mostram / Pesquisas indicam que" | forte | citar o estudo |
| "Muitos acreditam que", "Há quem diga que" | forte | quem? ou apagar |
| "É amplamente reconhecido/sabido que" | forte | apagar ou citar |
| "Segundo especialistas," | forte | nomear |

## 9. Fuga do verbo "ser" — `copula_avoidance`

| Expressão | Sev. | Troca |
|---|---|---|
| "se configura como", "se apresenta como", "se posiciona como" | fraca | é |
| "figura como", "atua como" (quando não há atuação) | fraca | é |
| "consiste em ser" | forte | é |

## 10. Paralelismo negativo e falsa concessão — `negative_parallelism`, `false_concession`

Nega algo que ninguém afirmou para depois apresentar a "verdadeira" ideia.

| Padrão | Sev. | Troca |
|---|---|---|
| "Não se trata apenas de X, mas de Y" / "Não se trata só de X" | forte | dizer Y; se Y for vazio ("trata-se de pessoas"), apagar a frase inteira |
| "Não é só X. É Y." / "Não é sobre X. É sobre Y." | forte | dizer Y |
| "Mais do que X, é Y" | fraca | dizer Y |
| "X? Não. Y." | forte | dizer Y |
| "Embora X seja importante, Y é ainda mais" (sem comparação real) | fraca | dizer Y |

## 11. Faixas falsas — `false_range`

"De X a Y" com extremos que não formam escala.

| Padrão | Sev. | Troca |
|---|---|---|
| "do planejamento à execução, da estratégia à inovação" | forte | listar o que de fato se faz |
| "de iniciantes a especialistas" (sem conteúdo para ambos) | fraca | dizer o público |

## 12. Seção de desafios formulaica — `formulaic_challenges`

| Padrão | Sev. | Troca |
|---|---|---|
| "Apesar dos desafios, X continua…" | forte | nomear o desafio e o dado |
| "Desafios e perspectivas" como seção genérica | fraca | título com o problema concreto |
| "O futuro de X é promissor" | forte | apagar ou dar a projeção com fonte |

## 13. Perguntas retóricas — `rhetorical_question`, `rhetorical_setup`

| Padrão | Sev. | Troca |
|---|---|---|
| "Mas afinal, o que é X?" | forte | dizer o que é |
| "Você já se perguntou…?" | forte | apagar |
| "E o melhor?" / "O resultado?" / "A resposta?" | forte | dizer o resultado direto |
| "Por que isso importa?" | fraca | dizer por que importa |

## 14. Andaimes de conclusão — `conclusion_scaffold`, `generic_conclusion`

| Expressão | Sev. | Troca |
|---|---|---|
| "Em suma," / "Em resumo," / "Resumindo," / "Concluindo," | fraca | apagar; se o parágrafo só recapitula, apagar o parágrafo |
| "Por fim, mas não menos importante," | forte | "Por fim," |
| "Em última análise," / "No fim das contas," | fraca | apagar |
| "As possibilidades são infinitas" | forte | apagar |
| "Com isso, você estará pronto para…" | forte | apagar |
| "Lembre-se:" encerrando texto | fraca | apagar |

## 15. Artefatos de assistente — `assistant_artifact`, `acknowledgment_loop`, `communication_artifact`, `knowledge_cutoff`

Restos da conversa com o chatbot colados no texto final.

| Expressão | Sev. | Troca |
|---|---|---|
| "Ótima pergunta!" / "Excelente pergunta!" | forte | apagar |
| "Claro! Aqui está…" / "Com certeza! Segue…" | forte | apagar |
| "Espero ter ajudado" / "Espero que isso ajude" | forte | apagar |
| "Se precisar de mais alguma coisa, é só pedir" | forte | apagar |
| "Como modelo de linguagem," / "Como IA," | forte | apagar |
| "Até a minha última atualização," / "Com base no meu conhecimento até…" | forte | apagar e conferir a informação |
| "[Inserir nome aqui]", "[Seu nome]" esquecidos | forte | preencher ou sinalizar ao autor |

## 16. Decalques do inglês — `calque` *(só pt-BR)*

Traduções literais que a IA produz por pensar em inglês. Confira o sentido antes de trocar: alguns usos já são aceitos.

| Expressão | Sev. | Troca |
|---|---|---|
| "endereçar um problema/uma questão" (*address*) | forte | tratar, resolver, enfrentar |
| "Espero que esta mensagem o(s) encontre bem" (*I hope this message finds you well*) | forte | apagar; cortesia curta e natural ("Bom dia,") pode ficar |
| "no final do dia" (*at the end of the day*) | forte | no fim das contas — ou apagar |
| "fazer a diferença" (em série) | fraca | dizer qual diferença |
| "suportar" no sentido de apoiar (*support*) | fraca | apoiar, oferecer suporte a |
| "aplicar para uma vaga" (*apply for*) | forte | candidatar-se a |
| "performar" | fraca | ter desempenho, funcionar |
| "eventualmente" no sentido de finalmente (*eventually*) | forte | por fim, com o tempo |
| "realizar" no sentido de perceber (*realize*) | forte | perceber, dar-se conta |
| "assumir" no sentido de supor (*assume*) | fraca | supor, presumir |
| "mandatório" | fraca | obrigatório |
| "deletar" em texto formal | fraca | apagar, excluir |
| "Títulos Com Todas As Palavras Em Maiúscula" | fraca | só a primeira palavra e nomes próprios |

## 17. Pontuação e formatação — `punctuation`

| Padrão | Sev. | Troca |
|---|---|---|
| Travessão (—) em quase toda frase, para pausas dramáticas | forte | vírgula, dois-pontos, parênteses ou ponto |
| Dois-pontos de suspense: "O segredo: consistência." | fraca | frase completa |
| Negrito no início de todo item de lista | fraca | negrito só no que precisa ser achado |
| Emojis marcando itens (✅ 🚀 💡) em texto profissional | forte | apagar |
| Aspas para ênfase ("qualidade") | fraca | apagar as aspas |
| Reticências de suspense… | fraca | ponto |
| Exclamações em série! | fraca | ponto |

## 18. Estrutura — `structure`

| Padrão | Sev. | Troca |
|---|---|---|
| Tríades em série: "rápido, eficiente e seguro" em todo parágrafo | fraca | manter só os itens com fato |
| Toda lista com exatamente três itens | fraca | listar o que existe |
| Parágrafo final que só repete o que foi dito | forte | apagar |
| Frase de efeito isolada em linha própria ao fim de cada seção | forte | integrar ou apagar |
| Subtítulo para cada parágrafo curto | fraca | juntar seções |
| "Principais benefícios:" seguido de lista genérica | fraca | dizer os benefícios com dado, em prosa se forem poucos |
| Abertura e fechamento espelhados ("Em um mundo…" / "Em um mundo…") | fraca | cortar a moldura |

---

## 19. Proteções — o que **não** mexer

Uma ocorrência só vira edição depois de passar por estas proteções. Na dúvida, preserve.

### Redação oficial e correspondência formal

Fórmulas exigidas pelo gênero não são vício:

- Vocativos e pronomes de tratamento: "Senhor Presidente,", "Vossa Excelência", "Vossa Senhoria".
- Abertura e encaminhamento: "Encaminho à apreciação de…", "Em atenção ao…", "Trata-se de…".
- Transição para o pedido: "Diante do exposto,", "Ante o exposto,", "Pelo exposto,".
- Fechos: "Respeitosamente,", "Atenciosamente,", "Coloco-me à disposição para esclarecimentos."
- Parágrafos numerados e alíneas.

### Linguagem jurídica e registro formal

"No que tange a" e "no que diz respeito a" são aceitos em qualquer registro formal (oficial, jurídico, técnico-científico). "Outrossim", "destarte", "data venia", "in casu", "salvo melhor juízo", "nos termos do art.", "consoante" — são do gênero jurídico. Só sugira simplificar se o usuário pedir linguagem simples.

### Sentido literal e técnico

- "robusto" em estatística ("estimador robusto") ou engenharia;
- "ecossistema" em biologia; "jornada" de trabalho; "navegar" em náutica ou internet; "mergulho" literal;
- "pilar" estrutural; "catalisador" em química; "cenário" de teatro, cinema ou simulação;
- "crítico", "fundamental", "essencial" quando definem requisito ("requisito essencial", "direito fundamental").

### Citações, normas e nomes

Texto entre aspas atribuído a alguém, transcrição de norma, ementa, nome de programa, título de obra: copiar como está.

### Escolhas do autor

Ironia, humor, ritmo pessoal, regionalismos e repetição intencional não são defeitos. Preferência pessoal de estilo não justifica edição.
