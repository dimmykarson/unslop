# TODO mestre — unslop pt-BR

- [x] feat: fase 1 — camada de instruções pt-BR (catálogo, guia, exemplos, predefinição oficial, roteamento no SKILL.md, amostras) → [spec](specs/pt-br.md)
- [x] chore: substituir a cópia em `~/.claude/skills/unslop` por link simbólico para este fork
- [x] feat: fase 2 — scripts com idioma (`--lang pt-br`, frases em arquivo de dados, tokenização Unicode, Flesch PT, restrições em formato brasileiro, ramificação no rewrite.md) → [spec](specs/pt-br.md)
- [ ] feat: fase 3 — estrutura e voz em pt-BR, incluindo alertas de negação/modalidade em português no validate_preservation → [spec](specs/pt-br.md)
- [ ] fix(upstream): `ENC-01` depende de `printf '\xHH'`, que o dash não suporta; propor `printf '\377\376'` (octal, POSIX)
