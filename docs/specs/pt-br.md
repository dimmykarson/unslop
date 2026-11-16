# Suporte a português do Brasil (pt-BR)

## Contexto

A skill `unslop` detecta e corrige padrões de escrita típicos de IA, mas é só para inglês por decisão registrada em `docs/DECISIONS.md` (2026-07-06, "English-only, with a graceful decline"). A decisão prevê revisão quando surgir "um catálogo de vícios de IA de outro idioma e uma estratégia de detecção para ele".

Hoje, com texto em português:

- `banned_phrase_scan.py`, `structure_scan.py` e `silhouette_scan.py` **recusam** a análise (`non_english: true`) e devolvem zero achados;
- `readability_metrics.py` usa Flesch–Kincaid, calibrado para inglês;
- as instruções ao modelo (`SKILL.md`, `references/`, `presets/`) só trazem exemplos em inglês.

O usuário escreve majoritariamente em pt-BR (propostas institucionais, memorandos no SEI, material de curso) e quer usar a skill nesses textos.

## Requisitos funcionais

### Fase 1 — camada de instruções (sem alterar código)

- [x] RF1: catálogo de vícios de IA em pt-BR, organizado pelas mesmas categorias do catálogo em inglês, com severidade (forte/fraca), troca sugerida e proteções de gênero.
- [x] RF2: guia de aplicação em pt-BR: como detectar o idioma, quais scripts funcionam, quais recusam e o que fazer no lugar deles.
- [x] RF3: exemplos de reescrita em pt-BR (antes/depois), incluindo um caso sem alteração e um caso de proteção de termo técnico.
- [x] RF4: predefinição `oficial` para redação oficial brasileira (Manual de Redação da Presidência da República).
- [x] RF5: `SKILL.md` encaminha textos em português para o guia pt-BR, com alteração mínima.
- [x] RF6: amostras pt-BR com vícios anotados em `evals/fixtures/pt-br/`, usadas no teste manual da fase 1 e como casos vermelhos da fase 2.

### Fase 2 — scripts com idioma (código)

- [x] RF7: `_lang.py` reconhece português; scripts aceitam `--lang pt-br` e detectam automaticamente.
- [x] RF8: frases proibidas fora do código, em arquivo de dados por idioma; `banned_phrase_scan.py` carrega o idioma ativo.
- [x] RF10: legibilidade com Flesch adaptado ao português (Martins et al., 1996).
- [x] RF13: `extract_constraints.py`/`validate_preservation.py` reconhecem formatos brasileiros: milhar com ponto e decimal com vírgula ("1.284", "R$ 1.200,00"), datas por extenso ("4 de dezembro"), horários ("14h"), quantidades com unidade ("27 horas") e números de normas ("nº 615/2025"); vocativos não contam como nome próprio.
- [x] RF14: `references/commands/rewrite.md` ramifica para o fluxo pt-BR antes do bloco de scripts, em vez de depender só do `SKILL.md`.

### Fase 3 — estrutura e voz

- [ ] RF9: tokenização com acentos (Unicode) nos scripts de estrutura e silhueta *(movido da fase 2: os dois scripts só fazem sentido junto com os padrões de estrutura)*.
- [ ] RF11: padrões de estrutura pt-BR em `structure_scan.py` (paralelismo negativo, tríades, travessões, gerúndio de análise vazia).
- [ ] RF12: `teach`/`mimic` funcionando com amostras em pt-BR.

## Requisitos não-funcionais

- **Compatibilidade:** nenhuma regressão no comportamento em inglês; `python3 evals/check.py` continua passando.
- **Contribuição upstream:** seguir as convenções do repositório (`CLAUDE.md`, `CONTRIBUTING.md`): na fase 2, todo padrão novo entra com caso de falso negativo e caso `protects` de falso positivo.
- **Segurança:** nenhuma dependência nova; nenhum acesso à rede.
- **LGPD:** as amostras usam apenas textos fictícios, sem dado pessoal.

## Breakdown modular

- **Fase 1:** `references/pt-br/` (README, catálogo, exemplos), `presets/official-ptbr.md`, seção no `SKILL.md`, `evals/fixtures/pt-br/`.
- **Fase 2:** `scripts/_lang.py` (detecção e tokenização), `references/pt-br/phrases.json` (dados), `scripts/banned_phrase_scan.py`, `scripts/extract_constraints.py` (e, por consequência, `validate_preservation.py`), `scripts/readability_metrics.py`, `references/commands/rewrite.md`; testes em `evals/check_ptbr.py` (placar documentado em `evals/CHECKS.md`) e referência congelada da saída em inglês em `evals/golden/ptbr-english-baseline.json`.
- **Fase 3:** `scripts/structure_scan.py`, `scripts/silhouette_scan.py`, `references/commands/teach.md`.

## Critérios de aceitação

### Fase 1

- [x] CA1: dado um texto pt-BR com vícios do catálogo, `/unslop rewrite` remove os vícios confirmados e preserva números, datas, nomes, normas citadas e o sentido. *Teste: reescrita independente das amostras de `evals/fixtures/pt-br/`, conferida contra as anotações.*
- [x] CA2: dado um texto pt-BR sem vícios (redação oficial correta), a skill devolve o texto sem alteração.
- [x] CA3: dado um texto pt-BR, a skill não trata o zero dos scripts que recusam como "texto limpo" e aplica o catálogo pt-BR.
- [x] CA4: com `--preset oficial`, fórmulas da redação oficial (pronomes de tratamento, "Respeitosamente", "Diante do exposto", parágrafos numerados) são preservadas.
- [x] CA5: termos técnicos e jurídicos em sentido literal ("estimador robusto", "no que tange") não são alterados.
- [x] CA6: `python3 evals/check.py` passa sem regressão.

### Fase 2

- [x] CA7: `banned_phrase_scan.py` (modo automático ou `--lang pt-br`) aponta todos os itens de `scanner_must_flag` das amostras 01 e 02 e devolve zero achados nas amostras 03 e 04.
- [x] CA8: para texto em inglês, `banned_phrase_scan.py`, `extract_constraints.py` e `readability_metrics.py` produzem saída idêntica à do código original (referência congelada gerada antes da mudança).
- [x] CA9: a detecção reconhece as amostras pt-BR como `pt-br` e não confunde espanhol nem inglês com português; texto em espanhol continua recusado (`non_english: true`).
- [x] CA10: cada entrada de `phrases.json` traz um exemplo que o detector aponta com a categoria declarada, e cada texto de proteção produz zero achados.
- [x] CA11: cada frase literal de `phrases.json` aparece no catálogo `taboo-phrases.md`.
- [x] CA12: em pt-BR, `extract_constraints.py` capta "1.284 atendimentos" (quantidade) e "3.412" (número, não versão), "R$ 1.200,00", "4 de dezembro", "14h", "27 horas", "Resolução CNJ nº 615/2025" e "sala 203"; não marca "Senhor Presidente" como nome próprio; e `validate_preservation.py` acusa perda quando "1.284" vira "1.248".
- [x] CA13: em pt-BR, `readability_metrics.py` informa `language: pt-br` e `flesch_reading_ease_pt`; conta 3 sílabas em "cidadão" e "tribunal" e 5 em "atendimento"; não emite os alertas calibrados para inglês.
- [x] CA14: `references/commands/rewrite.md` manda texto em português para o fluxo pt-BR antes do bloco de scripts.
- [x] CA15: `python3 evals/check.py` passa; a matriz de manutenção só falha no ENC-01 preexistente; o orçamento de complexidade (80 exemplos, 400 predicados) continua respeitado; `python3 evals/check_ptbr.py` passa.

## Resultado do teste da fase 1

Teste com agente independente aplicando a skill às amostras de `evals/fixtures/pt-br/` sem acesso às anotações.

- **1ª rodada:** 03 e 04 sem alteração (✓ CA2, CA4, CA5); 01 com todos os vícios removidos e fatos preservados, mas com um verbo inventado no lugar de uma frase vazia; 02 manteve "Espero que esta mensagem os encontre bem" (lacuna do catálogo e exemplo ambíguo).
- **Correções:** regra para trocas que pedem fato inexistente (apagar, nunca inventar); paralelismo negativo com Y vazio; saudação traduzida no catálogo (seções 1 e 16); proteção de "no que tange" em todo registro formal; mapeamento de predefinições para arquivos; orientação sobre os alertas de `diff_check` (mudança excessiva) e de negação; aviso de que os três scripts que recusam não precisam rodar em pt-BR.

- **2ª rodada (agente novo):** 01 e 02 conforme as anotações — vícios removidos, fatos preservados, nada inventado. Esclarecimentos finais: validação pt-BR (`validate_preservation` + `diff_check` + conferência manual), deslocamento do sujeito ao apagar frase vazia, conclusão avaliativa sem base, trocas do catálogo como exemplos.

## Resultado da fase 2

- `evals/check_ptbr.py`: 1.099 verificações, 0 falhas — detecção, detector nas amostras, exemplos e proteções de cada entrada, paridade com o catálogo, restrições brasileiras, legibilidade e saída em inglês idêntica à referência congelada (202 textos × 3 scripts).
- `python3 evals/check.py` passa; códigos de saída de todas as verificações individuais idênticos aos do código original (as falhas `check_seeded_docs`, `check_packs` e `ENC-01` são preexistentes).
- **Limitações conhecidas:** texto com menos de 15 palavras sem marca ortográfica (ç, -ção, -ão) segue o caminho em inglês; a contagem de sílabas é aproximada (hiatos sem acento, como "dia", contam uma sílaba); `validate_preservation.py` ainda usa as listas de negação e modalidade do inglês nos alertas de deriva semântica (fase 3).

## Decisões de arquitetura

### Fase 2

- **Só o idioma detectado muda o caminho.** No modo automático, o caminho pt-BR só é usado quando o texto **não** passa no detector de inglês **e** passa no de português. Texto em inglês segue exatamente o código original (garantia do CA8); outros idiomas continuam recusados.
- **Detector de português por palavras exclusivas** ("não", "são", "uma", "também", "você", "pelo", "pela", contrações como "do", "da", "no", "na", "ao", "à"), evitando palavras que o espanhol também usa ("de", "que", "para", "como").
- **Pacote enxuto de alto sinal**, como o do autor: o detector pega só expressões fortes e literais (e alguns padrões com expressão regular, como gerundismo e paralelismo negativo). Vocabulário amplo e dependente de contexto ("robusto", "cenário", "fundamental" isolado) fica só no catálogo, para o modelo julgar. Isso evita falso positivo em texto técnico e oficial.
- **Dados em JSON com exemplos embutidos:** cada entrada traz `example` (caso de falso negativo) e o arquivo tem uma lista `protects` (casos de falso positivo), validados por `check_ptbr.py`. É o equivalente, para o pacote pt-BR, da exigência do `CLAUDE.md` de um caso de cada tipo por padrão.
- **Restrições com tipos próprios** (`numero_br`, `moeda_brl`, `data_extenso`, `hora`, `quantidade`, `norma`, `local`), sem o prefixo `date`, para não cair na comparação de meses em inglês do `validate_preservation.py`; esses tipos exigem presença literal no texto transformado.
- **Placar separado, fora do orçamento:** o repositório já estava no teto de 80 exemplos executáveis (`check_complexity_budget.py`); uma linha nova o levaria a 81. Por isso `check_ptbr.py` é um placar à parte, como `check_mimic.py`, documentado em `evals/CHECKS.md` e rodado quando a parte pt-BR muda. O comportamento em inglês segue protegido pelos contratos existentes e, de forma exaustiva, pela referência congelada que o próprio `check_ptbr.py` confere.

### Fase 1


- **Fork local com branch `feat/pt-br`**, remoto `upstream` apontando para o repositório original. A skill instalada em `~/.claude/skills/unslop` passa a ser um link simbólico para o fork, para que as mudanças valham imediatamente e as atualizações do autor possam ser mescladas.
- **Fase 1 só em instruções:** entrega valor imediato sem tocar no código e sem conflitar com as atualizações do autor; o catálogo é aplicado pelo modelo até a fase 2 transformá-lo em dados.
- **Categorias com os mesmos identificadores do inglês** (`ai_vocabulary`, `throat_clearing` etc.), para a fase 2 reaproveitar os pacotes de detecção (`references/packs/manifest.json`).
- **Categoria nova `calque`** (decalques do inglês, como "endereçar um problema"), sem equivalente no catálogo em inglês.
- **Problema preexistente:** o caso `ENC-01` da matriz de manutenção falha neste Linux porque o `sh` (dash) não interpreta `\xHH` no `printf`. Não é regressão nossa; candidato a contribuição upstream separada.
