---
title: "CURRENT_BOARD"
board_version: "v001-experimental"
board_status: "experimental-active"
canonicality: "volatile operational board / not repository constitution"
repository: "yusukefujiijp/ai-project"
canonical_branch: "main"
reality_base_commit: "27e0329a5702a46257d72aaa3e684f17e5b64e51"
head_resolution: "derive at read/check time; do not hard-code self-referential HEAD"
last_verified: "2026-08-20"
review_scope: "root-routing / current-board / required-file existence / UTF-8 / empty README / front-matter canonical_path / internal Markdown links"
current_gate: "RC-01 minimal Reality Court bootstrap"
next_action_id: "RC-01-FIRST-RUN"
human_seal_required_for: "canonical cutover / retirement / public write / destructive change"
root_guard: "Root and Human-AI authority remain governed by README.md; this Board is a Keli, not Root or constitution."
---

# CURRENT_BOARD
## 【Repository Current Reality: Minimal Reality Court Experiment】

> [!IMPORTANT]
> `CURRENT_BOARD.md` is a **volatile operational board**, not a second constitution and not a replacement for `README.md`.
>
> Its job is to make the current repository evidence, unresolved drift, single next action, and PASS condition visible to Future AI without forcing a full-repository reconstruction.

---

## 0. 30-Second Board

```yaml
repository: "yusukefujiijp/ai-project"
canonical_branch: "main"
reality_base_commit: "27e0329a5702a46257d72aaa3e684f17e5b64e51"
head_commit: "derive live; do not embed"
board_status: "experimental-active"
current_gate: "RC-01 minimal Reality Court bootstrap"
next_action: "Run the first Reality Court against the repository after Court files are committed."
```

### Why `head_commit` is not hard-coded

A Board committed into Git cannot reliably contain the SHA of the very commit that contains it without creating a self-referential update loop.

Therefore this Board separates:

```text
reality_base_commit
= the known repository point from which this Board experiment began

live HEAD
= resolved at read/check time by Git or GitHub
```

The Reality Court checks that `reality_base_commit` exists and remains an ancestor of the live HEAD.

---

## 1. One-Line Current State

`ai-project` is a README-first / Markdown-centered Human-AI collaboration workspace with strong governance and restart memory; this experiment adds a small operational Board and a machine-checkable Court so repository facts no longer depend only on Human/AI recollection.

---

## 2. Current Proof

| Claim | Evidence | Evidence Type | Last Verified | State |
|---|---|---|---|---|
| Root Bootloader / constitution exists | `README.md` | live repository evidence | 2026-08-20 | confirmed |
| Canonical branch is `main` | Repository metadata / Root README | live repository evidence | 2026-08-20 | confirmed |
| Ark21:06 Session Harvest exists and is non-empty | `ark-project/ark21/Ark21-06/README.md` | live repository evidence | 2026-08-20 | confirmed |
| Current Board exists | `CURRENT_BOARD.md` | board artifact | 2026-08-20 | confirmed after this commit |
| Minimal Reality Court source exists | `tools/check_repo_reality.py` | pending bootstrap evidence | 2026-08-20 | pending until committed |
| Reality Court workflow exists | `.github/workflows/reality-check.yml` | pending bootstrap evidence | 2026-08-20 | pending until committed |
| Root README routes directly to Current Board | `README.md` | live repository evidence | 2026-08-20 | open / not yet routed |

---

## 3. Current Gate

### RC-01 — Minimal Reality Court Bootstrap

Goal:

> Introduce the smallest machine-verifiable layer that checks repository facts without pretending to judge Human meaning, Ark theology, Human Seal, or Canonical intent.

Planned Court surfaces:

```text
CURRENT_BOARD.md
+
tools/check_repo_reality.py
+
.github/workflows/reality-check.yml
```

---

## 4. Court Jurisdiction

The Court may judge only facts it can mechanically inspect.

### Hard-error jurisdiction

- required Court surfaces exist;
- Markdown files are valid UTF-8;
- `README.md` files are not whitespace-only;
- `CURRENT_BOARD.md` has required operational metadata;
- `reality_base_commit` exists and is an ancestor of live HEAD.

### Advisory / warning jurisdiction

- front-matter `canonical_path` points to a missing repository path;
- internal Markdown link points to a missing repository target;
- Root README does not yet route to `CURRENT_BOARD.md`.

Warnings are intentionally non-blocking in the first experiment because legacy drift may already exist. `--strict` may later promote warnings to errors after Human review and baseline classification.

### Outside Court jurisdiction

The Court must **not** decide:

- Human Mission or Meaning;
- spiritual Reality or divine guidance;
- Human Final Seal;
- whether a D1 Candidate becomes Canonical;
- whether an old document should be retired;
- whether a theological interpretation is correct;
- whether a useful warning should trigger a repository migration.

```text
Court verifies repository facts.
Human judges meaning and authority.
Reality confirms.
```

---

## 5. Drift Register

| ID | Drift / Risk | Severity | State | Next Move |
|---|---|---:|---|---|
| D-01 | No repository-wide machine validator existed before this experiment | P0 | closing in RC-01 | commit and run minimal Court |
| D-02 | Root README does not yet route to `CURRENT_BOARD.md` | P1 | open | classify after first Court run; patch separately if worth the churn |
| D-03 | `status` values remain heterogeneous | P1 | open / not in RC-01 | future minimal state registry candidate |
| D-04 | `canonical_path` declarations may contain stale paths | P1 | observe first | Court warning scan |
| D-05 | Internal Markdown links may contain stale targets | P1 | observe first | Court warning scan |
| D-06 | Runtime/Query pairs are not repository-registry-backed | P1 | parked | separate registry experiment |
| D-07 | Generated search index does not exist | P2 | parked | consider only after Court/Board prove useful |

---

## 6. Single Next Action

**RC-01-FIRST-RUN**

After `tools/check_repo_reality.py` and `.github/workflows/reality-check.yml` are committed:

```text
Run Reality Court
↓
Observe PASS / FAIL
↓
Count warnings by type
↓
Distinguish legacy drift from checker false positives
↓
Update this Board with first-run evidence
```

Do not launch a broad repository migration before the first Court result exists.

---

## 7. Done Condition for This Experiment

RC-01 is complete when:

1. `CURRENT_BOARD.md` exists on `main`.
2. `tools/check_repo_reality.py` exists on `main`.
3. `.github/workflows/reality-check.yml` exists on `main`.
4. The Court runs against live repository content.
5. Hard-error result is observed directly.
6. Warning classes are visible rather than hidden.
7. Board is updated with the observed result or explicitly records a blocker.
8. No Court claim is confused with Human Seal or spiritual/theological authority.

---

## 8. Future AI First Read Contract

A Future AI that encounters this Board should answer, before proposing new repository work:

```yaml
live_head: "derive from GitHub/Git"
reality_base_commit: "read from this Board"
current_gate: "read from this Board"
next_action_id: "read from this Board"
last_court_result: "read from the First-Run Evidence section; unknown if absent"
open_drift: "read Drift Register"
human_authority_needed: "state explicitly"
```

Do not treat an old Board date as a guarantee that the Board is still current. Compare with live HEAD and newer Human instructions.

---

## 9. First-Run Evidence

```yaml
reality_court:
  status: "PENDING"
  checked_commit: "unknown until first run"
  errors: "unknown"
  warnings: "unknown"
  strict_mode: false
```

This section must be updated only from an observed Court result, not from expectation.

---

## 10. Next Gates After RC-01

Only after the first run:

```text
Candidate RC-02
└─ Root README → CURRENT_BOARD routing

Candidate RC-03
└─ classify / fix high-confidence broken paths and links

Candidate RC-04
└─ minimal state + Runtime/Query registry

Candidate RC-05
└─ generated non-canonical search index
```

These are not automatically approved by this Board.

---

document_end:
  filename: "CURRENT_BOARD.md"
  board_version: "v001-experimental"
  eof_sentinel: "CURRENT_BOARD_EOF_v001-experimental"

CURRENT_BOARD_EOF_v001-experimental
