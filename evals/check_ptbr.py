#!/usr/bin/env python3
"""pt-BR support checks (docs/specs/pt-br.md, phase 2: CA7-CA13).

Runs every pt-BR acceptance check through the public CLIs, so it exercises the
same code paths a host agent uses. One adversarial maintenance row calls this
script, keeping the repository inside its executable-example budget.

    python3 evals/check_ptbr.py                    # run all checks
    python3 evals/check_ptbr.py --write-baseline   # freeze English outputs (CA8)

Only regenerate the baseline from code whose English behaviour is known to be
correct (it was first written from the unmodified upstream scripts).

Exit codes: 0 pass, 1 finding, 2 setup broken.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _check_support import ROOT, run  # noqa: E402

FIXTURES = ROOT / "evals" / "fixtures" / "pt-br"
PHRASES = ROOT / "references" / "pt-br" / "phrases.json"
CATALOG = ROOT / "references" / "pt-br" / "taboo-phrases.md"
BASELINE = ROOT / "evals" / "golden" / "ptbr-english-baseline.json"
CONTRACTS = ROOT / "evals" / "fixtures" / "contracts"

SCAN = ["python3", "scripts/banned_phrase_scan.py"]
EXTRACT = ["python3", "scripts/extract_constraints.py"]
READABILITY = ["python3", "scripts/readability_metrics.py"]
PRESERVE = ["python3", "scripts/validate_preservation.py"]

SPANISH = (
    "El rápido zorro marrón salta sobre el perro perezoso. La casa está cerca del "
    "río y los niños juegan en el jardín todas las tardes después de la escuela."
)
ENGLISH = (
    "The quick brown fox jumps over the lazy dog. The house is near the river and "
    "the children play in the garden every afternoon after school."
)
CONSTRAINT_SAMPLE = (
    "Senhor Presidente,\n\n"
    "Em 4 de dezembro, às 14h, na sala 203, foram apresentados 1.284 atendimentos "
    "e restam 3.412 em análise, com custo de R$ 1.200,00 e carga de 27 horas, nos termos da "
    "Resolução CNJ nº 615/2025.\n"
)
EXPECTED_CONSTRAINTS = {
    "1.284 atendimentos": "quantidade",
    "3.412": "numero_br",
    "R$ 1.200,00": "moeda_brl",
    "4 de dezembro": "data_extenso",
    "14h": "hora",
    "27 horas": "quantidade",
    "Resolução CNJ nº 615/2025": "norma",
    "sala 203": "local",
}
SYLLABLES = {"cidadão": 3, "tribunal": 3, "atendimento": 5}


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.passed = 0

    def check(self, ok: bool, label: str) -> None:
        if ok:
            self.passed += 1
        else:
            self.failures.append(label)


def _json(stdout: str) -> dict:
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return {}


def _stdin_run(cmd: list[str], text: str) -> tuple[int, str]:
    # _check_support.run() has no stdin parameter; same timeout safety net.
    proc = subprocess.run(cmd, cwd=ROOT, input=text, text=True, capture_output=True, timeout=60)
    return proc.returncode, proc.stdout


def scan(text: str, *extra: str) -> tuple[int, dict]:
    code, stdout = _stdin_run(SCAN + list(extra), text)
    return code, _json(stdout)


def _flags(result: dict, item: str) -> bool:
    item = item.lower()
    for violation in result.get("violations", []):
        phrase = violation.get("phrase", "").lower()
        if phrase and (item in phrase or phrase in item):
            return True
    return False


# --- English baseline (CA8) -------------------------------------------------

def english_corpus() -> list[tuple[str, str]]:
    corpus: list[tuple[str, str]] = []
    for table in sorted(CONTRACTS.glob("*.json")):
        data = json.loads(table.read_text(encoding="utf-8"))
        for row in data.get("examples", []):
            stdin = row.get("stdin")
            if isinstance(stdin, str) and stdin.strip():
                corpus.append((f"{table.stem}:{row['id']}", stdin))
    for path in sorted((ROOT / "evals" / "fixtures").rglob("*.txt")):
        if FIXTURES in path.parents:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if text.strip():
            corpus.append((str(path.relative_to(ROOT)), text))
    return corpus


def english_outputs() -> dict[str, dict[str, str]]:
    outputs: dict[str, dict[str, str]] = {}
    for case_id, text in english_corpus():
        entry = {}
        for name, cmd in (("scan", SCAN), ("extract", EXTRACT), ("readability", READABILITY)):
            code, stdout = _stdin_run(cmd, text)
            entry[name] = f"{code}:{hashlib.sha256(stdout.encode()).hexdigest()}"
        outputs[case_id] = entry
    return outputs


def check_english_baseline(report: Report) -> None:
    if not BASELINE.exists():
        report.check(False, f"CA8: baseline missing ({BASELINE.relative_to(ROOT)})")
        return
    frozen = json.loads(BASELINE.read_text(encoding="utf-8"))["outputs"]
    current = english_outputs()
    for case_id, expected in frozen.items():
        got = current.get(case_id)
        for name, digest in expected.items():
            report.check(
                got is not None and got.get(name) == digest,
                f"CA8: English output changed: {name} on {case_id}",
            )


# --- language detection (CA9) -----------------------------------------------

def check_detection(report: Report) -> None:
    for name in ("01-relatorio-slop.txt", "02-email-slop.txt", "03-oficial-limpo.txt",
                 "04-tecnico-protegido.txt"):
        _, result = scan((FIXTURES / name).read_text(encoding="utf-8"))
        report.check(result.get("language") == "pt-br", f"CA9: {name} not detected as pt-br")
    code, result = scan(SPANISH)
    report.check(
        result.get("non_english") is True and "language" not in result and code == 0,
        "CA9: Spanish must stay declined (non_english, no language, exit 0)",
    )
    _, result = scan(ENGLISH)
    report.check("language" not in result and "non_english" not in result,
                 "CA9: English must take the original path")


# --- fixtures (CA7) ---------------------------------------------------------

def check_fixtures(report: Report) -> None:
    annotations = json.loads((FIXTURES / "annotations.json").read_text(encoding="utf-8"))
    for name, case in annotations["cases"].items():
        text = (FIXTURES / name).read_text(encoding="utf-8")
        for args in ((), ("--lang", "pt-br")):
            code, result = scan(text, *args)
            mode = " ".join(args) or "auto"
            if case["expect"] == "unchanged":
                report.check(
                    code == 0 and result.get("total_violations") == 0,
                    f"CA7: {name} ({mode}) must have zero findings, got "
                    f"{[v.get('phrase') for v in result.get('violations', [])]}",
                )
                continue
            for item in case.get("scanner_must_flag", []):
                report.check(_flags(result, item), f"CA7: {name} ({mode}) missed '{item}'")
            report.check(code == 1, f"CA7: {name} ({mode}) must exit 1 with findings")


# --- phrase data (CA10, CA11) ------------------------------------------------

def check_phrase_data(report: Report) -> None:
    if not PHRASES.exists():
        report.check(False, f"CA10: {PHRASES.relative_to(ROOT)} missing")
        return
    data = json.loads(PHRASES.read_text(encoding="utf-8"))
    report.check(data.get("version") == 1 and data.get("language") == "pt-br",
                 "CA10: phrases.json needs version 1 and language pt-br")
    catalog = CATALOG.read_text(encoding="utf-8").lower()
    entries = [("phrase", e) for e in data.get("phrases", [])] + [
        ("pattern", e) for e in data.get("patterns", [])
    ]
    report.check(bool(entries), "CA10: phrases.json has no entries")
    for kind, entry in entries:
        label = entry.get("phrase") or entry.get("id")
        for key in ("category", "severity", "suggestion", "example"):
            report.check(bool(entry.get(key)), f"CA10: {kind} '{label}' missing {key}")
        report.check(entry.get("severity") in {"hard", "soft"},
                     f"CA10: {kind} '{label}' severity must be hard or soft")
        if kind == "phrase":
            report.check(entry["phrase"] == entry["phrase"].lower(),
                         f"CA10: phrase '{label}' must be lowercase")
            report.check(entry["phrase"] in catalog,
                         f"CA11: phrase '{label}' not documented in taboo-phrases.md")
        _, result = scan(entry.get("example", ""), "--lang", "pt-br")
        report.check(
            any(v.get("category") == entry.get("category") for v in result.get("violations", [])),
            f"CA10: example for {kind} '{label}' not flagged as {entry.get('category')}",
        )
    protects = data.get("protects", [])
    report.check(len(protects) >= 5, "CA10: need at least 5 protects texts")
    for item in protects:
        code, result = scan(item["text"], "--lang", "pt-br")
        report.check(
            code == 0 and result.get("total_violations") == 0,
            f"CA10: protects text flagged ({item.get('note')}): "
            f"{[v.get('phrase') for v in result.get('violations', [])]}",
        )


# --- constraints (CA12) ------------------------------------------------------

def check_constraints(report: Report) -> None:
    _, stdout = _stdin_run(EXTRACT, CONSTRAINT_SAMPLE)
    constraints = _json(stdout).get("constraints", [])
    by_value = {c["value"]: c["type"] for c in constraints}
    for value, ctype in EXPECTED_CONSTRAINTS.items():
        report.check(by_value.get(value) == ctype,
                     f"CA12: expected {value!r} as {ctype}, got {by_value.get(value)!r}")
    report.check(not any(c["type"] == "version" for c in constraints),
                 "CA12: Brazilian numbers must not be typed as version")
    report.check(not any("Presidente" in c["value"] and c["type"] == "proper_noun"
                         for c in constraints),
                 "CA12: vocative 'Senhor Presidente' is not a proper noun")
    tmp = ROOT / "evals" / "fixtures" / "pt-br"
    original = tmp / ".tmp-original.txt"
    changed = tmp / ".tmp-changed.txt"
    try:
        original.write_text(CONSTRAINT_SAMPLE, encoding="utf-8")
        changed.write_text(CONSTRAINT_SAMPLE.replace("1.284", "1.248"), encoding="utf-8")
        proc = run(PRESERVE + [str(original), str(changed)])
        result = _json(proc.stdout)
        missing = json.dumps(result.get("missing", result), ensure_ascii=False)
        report.check("1.284" in missing and proc.returncode != 0,
                     "CA12: validate_preservation must flag 1.284 -> 1.248")
    finally:
        original.unlink(missing_ok=True)
        changed.unlink(missing_ok=True)


# --- readability (CA13) ------------------------------------------------------

def check_readability(report: Report) -> None:
    text = (FIXTURES / "01-relatorio-slop.txt").read_text(encoding="utf-8")
    _, stdout = _stdin_run(READABILITY, text)
    result = _json(stdout)
    report.check(result.get("language") == "pt-br", "CA13: readability must report pt-br")
    report.check(isinstance(result.get("flesch_reading_ease_pt"), (int, float)),
                 "CA13: flesch_reading_ease_pt missing")
    report.check(not any("grade" in flag.lower() for flag in result.get("flags", [])),
                 "CA13: English grade flags must not be emitted for pt-br")
    try:
        sys.path.insert(0, str(ROOT / "scripts"))
        from readability_metrics import count_syllables_pt  # noqa: E402
    except ImportError:
        report.check(False, "CA13: count_syllables_pt not importable")
        return
    for word, expected in SYLLABLES.items():
        report.check(count_syllables_pt(word) == expected,
                     f"CA13: {word} should have {expected} syllables")


def write_baseline() -> int:
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "description": "SHA-256 of stdout (with exit code) for English corpus texts, frozen "
                       "from the unmodified upstream scripts. Guards CA8 in docs/specs/pt-br.md.",
        "outputs": english_outputs(),
    }
    BASELINE.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"baseline written: {len(payload['outputs'])} texts -> {BASELINE.relative_to(ROOT)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--write-baseline", action="store_true")
    args = parser.parse_args()
    if not FIXTURES.exists():
        print("setup broken: evals/fixtures/pt-br missing")
        return 2
    if args.write_baseline:
        return write_baseline()

    report = Report()
    for step in (check_english_baseline, check_detection, check_fixtures, check_phrase_data,
                 check_constraints, check_readability):
        step(report)
    for failure in report.failures:
        print(f"FAIL {failure}")
    print(f"pt-br checks: {report.passed} passed, {len(report.failures)} failed")
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
