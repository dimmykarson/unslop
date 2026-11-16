#!/usr/bin/env python3
"""Shared cheap English-detection helpers for banned_phrase_scan.py,
structure_scan.py, and silhouette_scan.py. All three scanners must decline the
same non-English inputs, so this table and its two functions live in exactly
one place.

Also home to the shared prose-view helpers (tokenizer, markdown stripper,
paragraph splitter) used by structure_scan.py and silhouette_scan.py. Those
two scanners previously carried private copies of these functions that had
drifted from each other (structure blanked blockquote lines, silhouette
didn't; silhouette stripped **bold**, structure didn't). strip_markdown_for_prose
below is the UNION of both original code paths, gated behind flags so each
caller reconciles the drift deliberately rather than silently: structure_scan
passes blank_blockquotes=True, silhouette_scan passes strip_bold=True."""

from __future__ import annotations

import re


# A small set of high-frequency English function words used only for a cheap
# language check. The words are chosen to be distinctively English: Spanish,
# French, German, etc. rarely use them, so their share of tokens is a robust
# signal without a language-model dependency.
ENGLISH_FUNCTION_WORDS = frozenset({
    "the", "and", "is", "are", "was", "were", "of", "to", "in", "that", "it",
    "for", "with", "on", "this", "but", "not", "you", "have", "be", "as", "at",
    "or", "we", "they", "will", "would", "there", "their", "what", "which",
    "when", "from", "been", "has", "had", "its", "an", "by", "our", "your",
    "if", "than", "then", "them", "these", "those", "about", "into", "over",
    "after", "before", "how", "why", "where", "who", "can", "could", "should",
    "do", "does", "did", "so", "out", "just", "more", "most", "some", "such",
    "only", "also", "because", "while", "between", "through", "during", "being",
})


def english_function_share(text: str) -> float:
    """Share of word tokens that are common English function words."""
    tokens = re.findall(r"[a-z']+", text.lower())
    if not tokens:
        return 1.0
    hits = sum(1 for t in tokens if t in ENGLISH_FUNCTION_WORDS)
    return hits / len(tokens)


def is_probably_english(text: str, threshold: float = 0.10, min_tokens: int = 15) -> bool:
    """Cheap English detector backing a graceful non-English decline.

    Conservative on purpose: inputs below ``min_tokens`` are always treated as
    English (too little signal to decline), and ``threshold`` is low enough that
    even terse or ESL-flavored English clears it. Only prose with almost no
    English function words (i.e. another language) is declined.
    """
    tokens = re.findall(r"[a-z']+", text.lower())
    if len(tokens) < min_tokens:
        return True
    return english_function_share(text) >= threshold


# Portuguese function words, chosen to be ABSENT from Spanish and English so a
# Spanish or English paragraph scores near zero: Spanish shares "de", "que",
# "para", "como", "no", "a", "o"; English shares "as", "do". Contractions
# ("da", "ao", "à", "pelo") and nasal forms ("não", "são") are the strongest
# signal. Used only to route pt-BR text to its own catalog (docs/specs/pt-br.md).
PORTUGUESE_FUNCTION_WORDS = frozenset({
    "não", "são", "é", "uma", "umas", "uns", "um", "também", "você", "vocês",
    "pelo", "pela", "pelos", "pelas", "da", "dos", "das", "na", "nas", "ao",
    "aos", "à", "às", "num", "numa", "isso", "isto", "está", "estão", "estava",
    "foi", "foram", "seu", "sua", "seus", "suas", "muito", "muita", "já",
    "após", "até", "então", "porém", "ainda", "mais", "ou", "em", "com", "os",
    "ele", "ela", "eles", "elas", "esse", "essa", "esses", "essas", "pode",
    "há", "tem", "têm", "sem", "nós",
})
_ACCENTED_WORD_RE = re.compile(r"[a-zà-ÿ']+")
_PORTUGUESE_MARKERS_RE = re.compile(r"ção|ções|ão\b|ões\b|ç", re.IGNORECASE)


def portuguese_function_share(text: str) -> float:
    """Share of word tokens that are distinctively Portuguese function words."""
    tokens = _ACCENTED_WORD_RE.findall(text.lower())
    if not tokens:
        return 0.0
    hits = sum(1 for t in tokens if t in PORTUGUESE_FUNCTION_WORDS)
    return hits / len(tokens)


def is_probably_portuguese(text: str, threshold: float = 0.08, min_tokens: int = 15) -> bool:
    """Cheap pt-BR detector. Short texts need an orthographic marker (ç, -ção,
    -ão) plus one Portuguese function word, because function-word share is too
    noisy below ``min_tokens``."""
    tokens = _ACCENTED_WORD_RE.findall(text.lower())
    if not tokens:
        return False
    if len(tokens) < min_tokens:
        return bool(_PORTUGUESE_MARKERS_RE.search(text)) and any(
            t in PORTUGUESE_FUNCTION_WORDS for t in tokens
        )
    return portuguese_function_share(text) >= threshold


def should_route_portuguese(text: str) -> bool:
    """Auto-mode routing: pt-BR only when the text fails the English check AND
    passes the Portuguese one, so every English input keeps its original path."""
    return not is_probably_english(text) and is_probably_portuguese(text)


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?", text.lower())


def strip_markdown_for_prose(
    text: str, *, blank_blockquotes: bool = False, strip_bold: bool = False
) -> str:
    """Strip markdown structure down to a prose view for cadence/discourse
    metrics. UNION of structure_scan's and silhouette_scan's original
    strippers -- each original branch is preserved verbatim, gated behind the
    flag that reproduces that caller's exact prior behavior.

    blank_blockquotes=True reproduces structure_scan's prior strip (blanks
    both blockquote and heading lines in one combined check). strip_bold=True
    reproduces silhouette_scan's prior strip (also collapses **bold** markers
    after list/ordinal stripping).
    """
    text = re.sub(r"```[\s\S]*?```", "\n\n", text)
    kept = []
    for line in text.splitlines():
        if blank_blockquotes:
            if re.match(r"\s*>", line) or re.match(r"\s{0,3}#{1,6}\s+", line):
                kept.append("")
                continue
        else:
            if re.match(r"\s{0,3}#{1,6}\s+", line):
                kept.append("")  # drop heading text from the prose view
                continue
        line = re.sub(r"^\s*[-*+]\s+", "", line)
        line = re.sub(r"^\s*\d+[.)]\s+", "", line)
        if strip_bold:
            line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
        kept.append(line)
    return "\n".join(kept)


def paragraphs(
    text: str, *, blank_blockquotes: bool = False, strip_bold: bool = False
) -> list[str]:
    stripped = strip_markdown_for_prose(
        text, blank_blockquotes=blank_blockquotes, strip_bold=strip_bold
    )
    return [
        re.sub(r"\s+", " ", p).strip()
        for p in re.split(r"\n\s*\n", stripped)
        if p.strip()
    ]
