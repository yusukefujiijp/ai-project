---
title: "AI Ark Seed Pickup"
canonical_name: "AI Ark Seed Pickup"
filename: "ai-ark-seed-pickup.md"
canonical_path: "ai-ark-seed/ai-ark-seed-pickup.md"
version: "v001-candidate"
date: "2026-08-08"
status: "human-sealed field-test candidate / not canonical"
class: "prompt_runtime"
route: "PICKUP"
role: "selective Seed pickup, maturation, cardification, and bounded persistence runtime"
language_policy: "Japanese-first / English-anchor"

paired_query:
  path: "ai-ark-seed/ai-ark-seed_query.md"
  version: "v001-candidate"

marker: "#PICKUP_ArkProjectSeed"

card_shelf:
  path: "ai-ark-seed/ai-ark-seed-cards/"
  format: "Markdown only"
---

# AI Ark Seed Pickup v001 Candidate

## 0. 一文定義

> **AI Ark Seed Pickupは、Seed Card化する価値があると見込まれる既存Seedだけを選択的にPickupし、Source・Context・Evidence・Guard・Next Gateを復元してCardificationを判定し、Human Sealされた場合だけMarkdown Seed Cardとして限定保存するRuntimeである。**

```text
Seed
↓
Pickup Candidate Gate
↓
Pickup
↓
Restore / Deepen
↓
Cardification Judgment
├─ HOLD / DROP
└─ CARDIFY
     ↓
 Seed Card Candidate
     ↓
 Human Seal
     ↓
 Persist
```

---

## 1. Primary Principle

> **Detect many. Save few.**

そして、

> **No Cardification, No Persistence.**

---

## 2. Accepted Input

Priority:

```yaml
seed_binding:
  1: "Explicit Seed String selected by Human"
  2: "Text after #PICKUP_ArkProjectSeed"
  3: "Explicitly delimited Seed"
  4: "Current Human request identifying one Seed"
```

Default Seed String:

```text
"Name(Definition)"
```

Opening and closing `"` are part of the Seed.

---

## 3. Pickup Candidate Gate

Pickup前に、巨大Analysisではなく最小判断を行う。

```yaml
pickup_candidate_gate:
  proceed_when:
    - "Human explicitly requests Pickup"
    - "or Current Request clearly treats the Seed as worth Cardification review"
    - "Seed has plausible reusable Ark Project value"

  hold_when:
    - "Target Seed is unclear"
    - "Seed meaning cannot be restored"
    - "No material reason to invest Pickup cost"
```

AIはSeed数を増やすことを目的にPickupしない。

---

## 4. Mission

```yaml
mission:
  - "Bind exact Seed"
  - "Preserve literal Seed String"
  - "Restore relevant Origin Context"
  - "Precisely verbalize hidden causal layers"
  - "Identify Why It Matters"
  - "Separate Confirmed / Inferred / Unknown"
  - "Assess Evidence"
  - "Define Guard"
  - "Define Next Gate"
  - "Judge Cardification"
  - "Create Seed Card Candidate only when warranted"
```

---

## 5. Source Sovereignty

```yaml
preserve:
  - "Seed String"
  - "Human wording"
  - "Origin Source"
  - "Origin Context"
  - "Known Evidence"
  - "Existing uncertainty"

separate:
  source: "Preserved"
  ai_interpretation: "Candidate"
  new_evidence: "Later Delta"
  unknown: "Unknown"
```

Do not silently rewrite the Seed into a different Concept.

---

## 6. Pickup Transformation

```text
Verify Seed
→ Restore Context
→ Isolate Causal Spine
→ Precisely Verbalize
→ Detect Material Delta
→ Test Boundary
→ Review Evidence
→ Define Guard
→ Define Next Gate
→ Cardification Judgment
```

---

## 7. Cardification Gate

Seed Card化は保存前のSemantic Gate。

```yaml
cardification_gate:
  questions:
    - "このSeedは再利用価値があるか"
    - "Threadを離れても意味が残るか"
    - "Pickupで単なる言い換え以上の価値が確認できたか"
    - "Future Human / AIが再起動する理由があるか"
    - "Context / Evidence / Next Gateを保持する価値があるか"

  outcomes:
    CARDIFY:
      action: "Create Seed Card Candidate"

    HOLD:
      action: "Do not persist"

    DROP:
      action: "Do not persist"
```

Cardification Gateは巨大Checklistへしない。

Human RealityとMeaningを優先する。

---

## 8. Seed Card Structure

CARDIFY時のみ次を作る。

```text
Seed Card
│
├─ Card Summary
│  ├─ Status
│  ├─ Origin
│  ├─ Seed String / 一文定義
│  ├─ Core Compression
│  └─ Guard
│
├─ Context
│  ├─ Source
│  ├─ Origin Context
│  ├─ Causal Spine
│  └─ Why It Matters
│
├─ Evidence
│
└─ Next Gate
```

Markdown only。

---

## 9. Seed String Preservation

Seed CardのCard Summaryへ、入力Seed StringをLiteralとして保持する。

```yaml
seed_string_preservation:
  opening_quote_required: true
  closing_quote_required: true
  strip_quotes: false
  reformat_required: false
```

Seed Stringの一文定義を別Fieldで重複保存しない。

---

## 10. Evidence

EvidenceはConceptの強さとRealityを分ける。

Candidate ladder:

```text
E0 Concept / Architecture Candidate
↓
E1 First Field Reality
↓
E2 Same-condition repetition
↓
E3 Cross-condition reproduction
↓
E4 Reduced AI dependence / Human autonomy
↓
E5 Reusable Method Candidate
```

一回の成功で上位へ飛ばさない。

---

## 11. Human Review Contract

Seed Card Candidate完成後、次をHuman-visibleに表示する。

```yaml
seed_card_review:
  candidate_path:
  action_if_sealed:
    - "Create new Seed Card"
    - "or update this exact Seed Card only"

  format: "Markdown"

  excluded_authority:
    - "Other Seed Card edit"
    - "Delete"
    - "Archive"
    - "Canonical promotion"
    - "Project Instructions edit"
```

---

## 12. Seal-to-Persist

Human Seal前にはGitHub Writeしない。

ただし、Human Review時にExact TargetとBounded Actionが明示されている場合、

```text
Human Seal
=
Current Card content approval
+
bounded persistence authority for that exact Card
```

として扱う。

Material Correctionがなければ、Seal後に「GitHub Writeしてよいですか？」という追加確認を挟まない。

Praise-only / agreement-onlyはSealではない。

---

## 13. Persistence

```yaml
persistence:
  target_root: "ai-ark-seed/ai-ark-seed-cards/"
  format: "Markdown only"

  eligible:
    - "Human-sealed CARDIFY result"

  prohibited:
    - "Raw Seed"
    - "Pickup working notes"
    - "HOLD"
    - "DROP"
    - "Unsealed Card Candidate"
```

---

## 14. Reality Review After Persist

```yaml
verify:
  - "Exact path exists"
  - "Stored file is Markdown"
  - "Seed String outer quotes preserved"
  - "Seed Card structure present"
  - "No unrelated Card changed"
  - "Reported status matches actual repository state"
```

---

## 15. Output States

```yaml
HOLD:
  persisted: false

DROP:
  persisted: false

CARD_CANDIDATE:
  persisted: false
  human_seal_required: true

CARD_PERSISTED:
  persisted: true
  reality_review_required: true
```

---

## 16. Core Compression

```text
Pickup only what may deserve a Card.
Deepen without rewriting the Source.
Cardify only when value survives review.
Persist only after Human Seal.
```

document_end:
  filename: "ai-ark-seed-pickup.md"
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_ARK_SEED_PICKUP_RUNTIME::v001-candidate"

EOF::AI_ARK_SEED_PICKUP_RUNTIME::v001-candidate
