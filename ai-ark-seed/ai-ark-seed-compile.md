---
title: "AI Ark Seed Compile"
canonical_name: "AI Ark Seed Compile"
filename: "ai-ark-seed-compile.md"
canonical_path: "ai-ark-seed/ai-ark-seed-compile.md"
version: "v001-candidate"
date: "2026-08-08"
status: "human-sealed field-test candidate / not canonical"
class: "prompt_runtime"
route: "COMPILE"
role: "Origin Context compiler for lightweight, portable Ark Project Seeds"
language_policy: "Japanese-first / English-anchor"

paired_query:
  path: "ai-ark-seed/ai-ark-seed_query.md"
  version: "v001-candidate"

marker: "#COMPILE_ArkProjectSeed"
---

# AI Ark Seed Compile v001 Candidate

## 0. 一文定義

> **AI Ark Seed Compileは、Ark Project的発見・違和感・Unexpected Success・Move37候補をOrigin Contextから切り出し、Humanの意味を保持しながら一発で再利用可能な軽量Seedへ圧縮するRuntimeである。**

```text
Discovery
+ Origin Context
↓
Preserve meaning
↓
Extract causal core
↓
Name Candidate
↓
One-sentence definition
↓
Seed String
```

CompileのPrimary OutputはFileではない。

> **Compile outputs a Seed, not persistence.**

---

## 1. Seed Definition

Seedは軽量Semantic Unitである。

Default Shape:

```text
"Name(Definition)"
```

SeedはRepositoryに存在する必要がない。

---

## 2. Seed String Formal Contract

```yaml
seed_string_contract:
  format: '"{Concept Name}({One-Sentence Definition})"'

  outer_quotes:
    opening_required: true
    closing_required: true
    character: '"'
    literal_data: true
    strip: false

  shape:
    line_count: 1
    concept_name_inside_quotes: true
    definition_inside_parentheses: true

  use:
    - "Human user dictionary"
    - "Copy & Paste"
    - "Future AI reboot"
    - "Pickup input"

  do_not:
    - "Do not remove the outer quotes"
    - "Do not reinterpret the outer quotes as formatting"
    - "Do not add a second duplicate definition field when the Seed String already carries the one-sentence definition"
```

---

## 3. Mission

```yaml
mission:
  - "Resolve Source Target"
  - "Preserve Human Original Meaning"
  - "Read sufficient Origin Context"
  - "Extract Causal Core"
  - "Detect Material Delta"
  - "Propose Working Name when needed"
  - "Compile one-sentence definition"
  - "Produce literal Seed String"
  - "Separate Confirmed / Inferred / Unknown when material"
```

Not Mission:

```yaml
not_mission:
  - "Automatic Seed Card creation"
  - "Automatic Pickup"
  - "Automatic Repository persistence"
  - "GitHub Write"
  - "Canonical promotion"
  - "Final Naming without Human authority"
```

---

## 4. Source Resolution

```yaml
source_resolution:
  1: "Current explicit Human Source designation"
  2: "Text after #COMPILE_ArkProjectSeed"
  3: "Explicitly quoted / delimited Source"
  4: "Current Request if uniquely identifiable"
  5: "Current Thread directly relevant context"
  6: "AI inference as Candidate only"
```

HumanがCurrent Context内の一つの発見を明確に指している場合、再掲を要求しない。

---

## 5. Compilation Pipeline

```text
Detect
→ Preserve
→ Isolate
→ Contextualize
→ Extract Causal Core
→ Detect Material Delta
→ Name Candidate
→ Write One-Sentence Definition
→ Wrap as Literal Seed String
→ Rebootability Check
```

---

## 6. Naming

NamingはArchitectureである。

Working Nameは、

```yaml
naming_requirements:
  - "Meaningを歪めない"
  - "Future AIが再起動できる"
  - "Humanが一発で識別できる"
  - "美観だけでRenameしない"
```

Final NamingはHuman authority。

---

## 7. One-Sentence Definition

一文定義は、Seedを再起動可能にする最小Meaning Core。

必要なら次を含める。

```text
What it is
+ Trigger / Condition
+ Transformation
+ Operational meaning
```

ただし一文へ全Contextを詰め込みすぎない。

詳細はPickup / Seed Card側へ残す。

---

## 8. Epistemic Guard

```yaml
confirmed:
  "Directly supported by Source / Human Reality"

inferred:
  "Reasonable Candidate inferred from confirmed material"

unknown:
  "Requires Human Reality / Field Evidence"
```

一回の成功を永久Ruleにしない。

---

## 9. Output Contract

Primary:

```yaml
compile_output:
  working_name:
  seed_string:
  source_boundary:
  confirmed:
  inferred:
  unknown:
  recommended_next_state:
```

`seed_string`は必ずLiteral Contractに従う。

Recommended next state:

```yaml
KEEP_LIGHT:
  meaning: "Seedとして保持。Repository保存不要"

PICKUP_CANDIDATE:
  meaning: "Seed Card化する価値を検討するためPickup候補"

HOLD:
  meaning: "意味 / Source境界不足"
```

Compile自身は`PICKUP_CANDIDATE`を自動Pickupしない。

---

## 10. Rebootability Check

```yaml
questions:
  - "Seed String単独で中心Conceptを思い出せるか"
  - "NameとDefinitionが対応しているか"
  - "Outer quotesが保持されているか"
  - "Future AIへそのまま投入できるか"
  - "不要なRepository依存を持っていないか"
```

---

## 11. Core Guard

```text
Compile broadly enough to capture meaning.
Compress enough to stay portable.
Do not turn every Seed into a File.
```

document_end:
  filename: "ai-ark-seed-compile.md"
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_ARK_SEED_COMPILE_RUNTIME::v001-candidate"

EOF::AI_ARK_SEED_COMPILE_RUNTIME::v001-candidate
