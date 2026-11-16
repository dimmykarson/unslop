# Unslop em português (pt-BR)

Leia este arquivo antes de agir sobre texto em português. Ele **complementa** o [contrato principal](../core-contract.md), que continua valendo integralmente: menor trecho com defeito concreto, edição só do que foi confirmado, o resto copiado byte a byte, preservação de fatos, escopo, atribuição, citações, registro e incerteza.

## 1. Reconhecer o idioma

Trate o texto como pt-BR quando o usuário disser, ou quando palavras como "de", "que", "não", "para", "uma", "com", "os", "das", "pelo", "também" forem frequentes. Em texto misto, aplique o catálogo do idioma de cada trecho.

## 2. Situação dos scripts em pt-BR

Os scripts foram feitos para inglês. Até a fase 2 da extensão (ver `docs/specs/pt-br.md`), **em pt-BR substitua o bloco de scripts de `references/commands/rewrite.md` e da validação do contrato pelo fluxo da seção 3 deste arquivo.** Não é preciso rodar os três scripts que recusam.

| Script | Em pt-BR | O que fazer |
|---|---|---|
| `banned_phrase_scan.py` | **Recusa** (`non_english: true`, zero achados) | Aplicar o [catálogo pt-BR](taboo-phrases.md) manualmente |
| `structure_scan.py`, `silhouette_scan.py` | **Recusam** | Conferir a seção 18 (Estrutura) e a 17 (Pontuação) do catálogo manualmente |
| `readability_metrics.py` | Roda, mas com fórmula do inglês | Ignorar a nota; se precisar, use o Flesch adaptado (abaixo) |
| `extract_constraints.py`, `validate_preservation.py` | **Parciais**: pegam anos, mas perdem datas por extenso ("12 de março"), horários ("14h"), quantidades ("27 horas") e números de normas ("nº 615"); leem o separador de milhar brasileiro como número de versão ("1.284" vira `version`) e podem marcar vocativos ("Senhor Presidente") como nome próprio | Rodar, e **também** listar à mão números, datas, valores, normas e nomes do original e conferir um a um no resultado |
| `diff_check.py` | Funciona | Usar normalmente. O alerta *Excessive change* (mais de 40% alterado) é **informativo** quando tudo o que saiu é vício confirmado; registre-o, mas não bloqueie |

**Alerta de negação** (`Negation count dropped`) de `validate_preservation.py`: aceitável quando a negação estava dentro de um trecho vazio apagado (ex.: paralelismo negativo). Releia as negações que **ficaram** e confirme que nenhuma afirmação se inverteu.

**Zero achados de um script que recusou não significa texto limpo.** Nunca devolva o texto como "sem problemas" só porque os scripts não acharam nada.

**Flesch adaptado ao português (Martins et al., 1996):** `248,835 − 1,015 × (palavras/frases) − 84,6 × (sílabas/palavras)`. Escala: 75–100 muito fácil; 50–75 fácil; 25–50 difícil; 0–25 muito difícil. Use só como indicador; não é meta.

## 3. Fluxo

1. Leia o texto inteiro antes de qualquer verificação.
2. Liste as restrições do original: números, datas, valores, percentuais, normas, nomes próprios, citações, negações e condicionais.
3. Percorra o [catálogo](taboo-phrases.md) e marque as ocorrências suspeitas.
4. Para cada suspeita, confirme o defeito no contexto e passe pelas **proteções** (seção 19 do catálogo). Sem defeito confirmado, não edite.
5. Reescreva só os trechos confirmados, na voz da predefinição escolhida.
6. Valide: confira a lista do passo 2 no resultado, item por item, e rode `validate_preservation.py original.txt transformed.txt` e `diff_check.py original.txt transformed.txt` (passe os arquivos como argumento; a entrada por `<<<` pode travar em alguns ambientes). Em pt-BR, estes dois scripts e a conferência manual **substituem** a lista de validação do contrato.
7. Sem nenhum defeito confirmado, devolva o texto original exatamente como veio.

**Ao apagar uma frase vazia:** se ela carregava o sujeito do parágrafo ou um nome necessário para entender o resto, leve esse sujeito ou nome para a frase vizinha com o mínimo de ajuste (ex.: "foram registrados" → "a Seção registrou"). Nomes que só apareciam dentro do trecho vazio, sem fato associado, podem sair junto.

**Conclusão avaliativa sem base** ("está no caminho certo", "o futuro é promissor") também é vício, mesmo que não seja mera recapitulação: apague, como o contrato manda fazer com recompensa sem sustentação.

**Trocas sugeridas** nas tabelas do catálogo são exemplos. Use a palavra mais natural no contexto ("discutir" em vez de "mergulhar" numa pauta de reunião), desde que não acrescente sentido.

## 4. Saída

Responda em português. Para auditoria (`--report`), use os rótulos **Problemas encontrados** (trecho, categoria do catálogo, severidade, motivo no contexto) e **Avaliação** (defeitos confirmados e decisões de julgamento). Para reescrita, devolva o texto limpo.

## 5. Predefinições

As predefinições em inglês valem para pt-BR: aplique as regras, não as frases de exemplo. Arquivos: `crisp` → `presets/crisp-human.md` (padrão), `warm` → `warm-human.md`, `expert` → `expert-human.md`, `story` → `story-lean.md`. Para documentos oficiais, memorandos, ofícios, despachos e pareceres, use `--preset oficial` ([official-ptbr.md](../../presets/official-ptbr.md)).

## 6. Particularidades do português

- **Norma-padrão:** corrija erros gramaticais só se o usuário pedir revisão; o objetivo da skill é tirar marcas de IA, não revisar a gramática.
- **Gerúndio:** o gerúndio é legítimo em português. O vício é o gerúndio no fim da frase atribuindo efeito genérico ("…, contribuindo para o fortalecimento") e o gerundismo ("vou estar enviando").
- **Voz passiva e impessoalidade:** são esperadas em texto oficial e científico. Não converta para voz ativa nesses gêneros.
- **Decalques:** confira o sentido antes de trocar; "realizar" no sentido de executar é correto, só no sentido de perceber é decalque.
- **Concordância após edição:** ao apagar uma expressão de abertura, reveja maiúscula inicial, concordância e pontuação da frase que sobra.

Exemplos comentados: [rewrite-examples.md](rewrite-examples.md).
