---
name: unslop
description: Edit or audit prose for AI writing patterns. Use when someone wants to humanize a draft, remove slop, flag robotic phrasing, or learn and write in an author's voice.
license: MIT
user-invocable: true
argument-hint: "[teach · cleanup · rewrite · mimic] [input]"
metadata:
  author: claytonkim
  version: "2.3.0"
---

# Unslop

Open the matching command before acting. Input can be pasted text, a file, or stdin.
For audits and rewrites, [the core contract](references/core-contract.md) governs what to edit and preserve.

## Routing by phrase

| Request | Command |
|---------|---------|
| `rewrite`, humanize a draft, or bare `/unslop <text>` | [references/commands/rewrite.md](references/commands/rewrite.md) |
| `cleanup`, propose edits I can accept or reject | [references/commands/cleanup.md](references/commands/cleanup.md) |
| audit, review before publication, flag only, or `--report` | [references/commands/cleanup.md](references/commands/cleanup.md#report-only) |
| `teach`, build a voice profile | [references/commands/teach.md](references/commands/teach.md) |
| harvest writing samples, what writing of mine do you have? | [references/commands/teach.md](references/commands/teach.md#1-gather-samples-harvest) |
| calibrate my voice profile, quiz me on paired samples | [references/commands/teach.md](references/commands/teach.md#calibrate) |
| `mimic` or draft in my voice | [references/commands/mimic.md](references/commands/mimic.md) |
| refine until it sounds like me | [references/commands/mimic.md](references/commands/mimic.md#refine) |
| voice check, does this sound like me? | [references/commands/mimic.md](references/commands/mimic.md#voice-check) |
| add a newly observed AI tell to the library | [references/commands/contribute.md](references/commands/contribute.md) |

## Portuguese (pt-BR)

For Portuguese input, read [references/pt-br/README.md](references/pt-br/README.md) before acting. The phrase scanner, constraint extractor, and readability script detect pt-BR; the structure and silhouette scanners still decline it. Zero findings are not evidence of clean text: also apply the [pt-BR catalog](references/pt-br/taboo-phrases.md) and answer in Portuguese.

## Output Format

Before writing, read the selected voice preset in `presets/`. The default is `crisp`; `--preset` also accepts `warm`, `expert`, `story`, and `oficial` (Brazilian official correspondence, `presets/official-ptbr.md`).

Return the cleaned text for a rewrite. For a report, give **Issues Found** (span, category, severity, contextual reason) and **Assessment** (confirmed defects and judgment calls). Preserve the original text in report mode.

For strict or requested analysis, return **Transformed Text** and **Validation**. Report constraints preserved, before/after pattern counts, structure, readability grade, sentence variance, percentage changed, and rubric score. With `--strict`, scores below 32/40 fail. See [the rubric](references/rubric.md).
