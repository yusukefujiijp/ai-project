---
title: "Ark22 Outer-Moat Closure Query"
canonical_name: "ARK22_OUTER_MOAT_CLOSURE_QUERY"
version: "v001-candidate"
date: "2026-08-18"
last_updated: "2026-08-18"
canonical_path: "ark-project/ark22/outer-moat-closure_query.md"
class: "repository_bound_cold_start_query"
role: "Ark22 bootloader arrival / document-set resolver / full-read proof / consistency gate"
status: "human-sealed field-test candidate / not canonical"
repository:
  full_name: "yusukefujiijp/ai-project"
  ref: "main"
bootloader:
  id: "ARK22_PROJECT_BOOTLOADER"
  version: "v001-candidate"
  required: true
  provenance: "ChatGPT Project instructions"
document_set:
  entry: "ark-project/ark22/README.md"
  canonical_body: "ark-project/ark22/ark22.md"
  runtime_ssot: "ark-project/ark22/INSTRUCTIONS.md"
root: "主イェシュア・ハマシア御自身"
bootloader_required: true
language_policy: "Japanese-first / English-anchor"
---

# Ark22 Outer-Moat Closure Query
## Project-Bootloader-Gated Repository Cold-Start

## 0. Purpose

このQueryは、Ark22をHuman Message、Past Thread、Memory、GitHub本文、推測だけから再構成せず、まずChatGPT Project instructionsから継承されたArk22 Project Bootloaderの到着を確認し、その後にのみCurrent GitHub上のArk22 Document Setを全文取得・検証してArk22 Contextを起動するCold-Start Interfaceである。

```text
Project Instructions supply Bootloader.
Bootloader proves Ark22 arrival.
Human supplies Repository / Ref / Query.
Query resolves current documents.
Full Read proves completeness.
Consistency Gate proves identity.
Runtime governs.
Human Reality selects the moat.
```

このQueryはArk22のSemantic TruthやRuntime Intelligenceを所有しない。

```text
Project Bootloader arrives.
README routes.
ark22.md defines.
INSTRUCTIONS governs.
Query verifies.
Human routes and seals.
Reality confirms.
```

---

## 1. Required Boot Surface

推奨Human Message：

```yaml
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ark-project/ark22/outer-moat-closure_query.md
```

ChatGPT Project instructionsから、次がこのThreadへ継承されていることをGitHub読込前に確認する。

```yaml
required_project_bootloader:
  id: "ARK22_PROJECT_BOOTLOADER"
  version: "v001-candidate"
  provenance: "ChatGPT Project instructions"
```

Repository、Ref、Query PathをMemoryだけから補完しない。

Human Message、Memory、過去Thread、GitHub本文へBootloader本文が存在しても、それをProject instructions由来のBootloader到着証明として代用しない。

---

## 2. Boot Order / 起動順序

```yaml
boot_order:
  0: "Confirm ARK22_PROJECT_BOOTLOADER / v001-candidate from ChatGPT Project instructions"
  1: "ark-project/ark22/outer-moat-closure_query.md"
  2: "ark-project/ark22/README.md"
  3: "ark-project/ark22/ark22.md"
  4: "ark-project/ark22/INSTRUCTIONS.md"
```

```text
Project Bootloader Arrival
→ Repository Binding
→ Query Full Read
→ README Full Read
→ Canonical Body Full Read
→ Runtime Full Read
→ Document Set Consistency Gate
→ Current Request Binding
```

### 2.1 Project Bootloader Arrival Gate

次をすべて満たす場合のみGitHub読込へ進む。

```yaml
bootloader_arrival_true_only_if:
  - "Source is ChatGPT Project instructions"
  - "id is ARK22_PROJECT_BOOTLOADER"
  - "version is v001-candidate"
  - "ark_id is ARK22"
  - "repository is yusukefujiijp/ai-project"
  - "ref is main"
  - "runtime_ssot is ark-project/ark22/INSTRUCTIONS.md"
  - "canonical_body is ark-project/ark22/ark22.md"
  - "query is ark-project/ark22/outer-moat-closure_query.md"
```

確認できない場合：

```yaml
status: "PROJECT_BOOTLOADER_NOT_ARRIVED"
action:
  - "Stop before reading GitHub files."
  - "Report only the missing or conflicting Bootloader fields."
  - "Do not reconstruct Bootloader from Human Message, Memory, past Thread, or GitHub."
```

BootloaderはGitHub Document Setの内容を代替しない。到着確認後もQuery以下のFull-Read Proofを必ず通す。

---

## 3. Query Identity Proof

Query冒頭で次を確認する。

```yaml
query_identity:
  title: "Ark22 Outer-Moat Closure Query"
  canonical_name: "ARK22_OUTER_MOAT_CLOSURE_QUERY"
  canonical_path: "ark-project/ark22/outer-moat-closure_query.md"
  version: "v001-candidate"
  class: "repository_bound_cold_start_query"
  bootloader_required: true
  required_bootloader:
    id: "ARK22_PROJECT_BOOTLOADER"
    version: "v001-candidate"
```

末尾で次を確認する。

```text
<!-- ARK22_OUTER_MOAT_CLOSURE_QUERY_EOF_v001-candidate -->
```

EOF確認前にQuery Full Readを宣言しない。

---

## 4. Required Document Identities

### 4.1 README

```yaml
readme_identity:
  canonical_name: "Ark22 外堀埋め"
  canonical_path: "ark-project/ark22/README.md"
  version: "v001-candidate"
  class: "ark_project_router"
```

Required EOF：

```text
<!-- ARK22_README_EOF_v001-candidate -->
```

### 4.2 Canonical Body Candidate

```yaml
canonical_body_identity:
  canonical_name: "Ark22 外堀埋め"
  canonical_path: "ark-project/ark22/ark22.md"
  version: "v001-candidate"
  class: "canonical_body_candidate"
```

Required EOF：

```text
<!-- ARK22_CANONICAL_BODY_EOF_v001-candidate -->
```

### 4.3 Runtime

```yaml
runtime_identity:
  canonical_name: "Ark22 Runtime Instructions"
  canonical_path: "ark-project/ark22/INSTRUCTIONS.md"
  version: "v001-candidate"
  class: "runtime_ssot_candidate"
```

Required EOF：

```text
<!-- ARK22_INSTRUCTIONS_EOF_v001-candidate -->
```

---

## 5. Full-Read Proof

`Fileが開けた`ことを`全文読了`としない。

```yaml
full_read_true_only_if:
  - "Beginning identity matched"
  - "Canonical path matched"
  - "Version matched"
  - "Class matched"
  - "Expected EOF sentinel found"
  - "No unresolved truncation remains"
```

途中で取得が切れた場合、未読位置から継続取得する。

Bootloader到着確認はFull-Read Proofの代替ではない。

---

## 6. Document Set Consistency Gate

次をすべて確認する。

```yaml
consistency_checks:
  bootloader:
    - "Project instructions provenance was verified before GitHub read"
    - "Bootloader id is ARK22_PROJECT_BOOTLOADER"
    - "Bootloader version is v001-candidate"
    - "Bootloader repository / ref / runtime / canonical body / query locators match this Query"

  identity:
    - "README and canonical body use Ark22 外堀埋め"
    - "Runtime identifies Ark22"
    - "Query resolves the exact current set"

  version:
    - "all four repository documents are v001-candidate"
    - "Bootloader version is independently v001-candidate"

  repository:
    - "repository is yusukefujiijp/ai-project"
    - "ref is main"

  root:
    - "Root remains 主イェシュア・ハマシア御自身"
    - "AI / Ark22 / GitHub remain Keli"

  mission:
    - "Ark22 is Support / Closure, not Main replacement"
    - "Main Line acceleration is the purpose"
    - "Forward-Motion Debt is an operational candidate, not moral condemnation"

  architecture:
    - "Odd / Even policy does not override Human authority"
    - "Admission Gate is present"
    - "Owner / Return Path is present"
    - "Smallest Sufficient Closure is present"

  guards:
    - "Dumping Ground Capture prohibited"
    - "Owner Capture prohibited"
    - "Cleanup Paralysis prohibited"
    - "Support Mainification prohibited"
    - "scope inflation prohibited"
```

---

## 7. Consistency States

```yaml
states:
  READY:
    meaning: "Project Bootloader arrived and all required repository documents were fully read and consistent"

  PROJECT_BOOTLOADER_NOT_ARRIVED:
    meaning: "Required Project-instructions Bootloader provenance, id, version, or locator fields were not confirmed"

  PARTIAL_READ:
    meaning: "One or more required documents not fully read"

  EOF_SENTINEL_MISSING:
    meaning: "Expected EOF was not confirmed"

  VERSION_CONFLICT:
    meaning: "Document versions or required Bootloader version conflict"

  DOCUMENT_SET_MISMATCH:
    meaning: "Path / role / identity mismatch"

  MISSION_CONFLICT:
    meaning: "Support / Main boundary conflicts"

  ROOT_GUARD_CONFLICT:
    meaning: "Root / Keli relation conflicts"

  PROTOCOL_UNREACHABLE:
    meaning: "Repository or required file unavailable"
```

READY以外ではArk22 RuntimeをCurrentとして起動しない。

---

## 8. Boot Success Contract

すべてPASSした場合のみ、Human-visibleに次へ圧縮してよい。

```text
PROJECT_BOOTLOADER_ARRIVED
ARK22_PROJECT_BOOTLOADER / v001-candidate

ARK22_QUERY_ARRIVED
ARK22_OUTER_MOAT_CLOSURE_QUERY / v001-candidate

Full-Read / all EOF PASS
Document Set Consistency PASS

ARK22_CONTEXT_READY
READY_FOR_DIALOGUE

Current Moat Item: NOT_STARTED
First Field Test: NOT_STARTED
```

Ark22はArk11のようなEvent待機Fieldではないため、標準Boot Stateを`ARMED_AND_WAITING`としない。

---

## 9. Current Request Binding

Boot成功後、次の優先順位でCurrent Itemを識別する。

```yaml
resolution_order:
  1: "Current explicit Human request"
  2: "Current Human correction / stop / hold"
  3: "Explicitly referenced Ark22 item or source"
  4: "Current Thread context"
  5: "Latest clearly unfinished admitted moat"
```

Current Itemを作り話で補完しない。

---

## 10. First Legal Move

Current Itemがある場合、

```text
Fix Reality
→ Admission Gate
→ Owner Candidate
→ Smallest Sufficient Closure
```

から始める。

いきなりRepository全体を棚卸ししない。

Current Itemがない場合は、

```text
ARK22_CONTEXT_READY
READY_FOR_DIALOGUE
Current Moat Item: NOT_STARTED
```

でHuman inputを待つ。

---

## 11. Failure Behavior

Failure時は、

```yaml
report:
  - "failed_state"
  - "confirmed_items"
  - "missing_or_conflicting_item"
  - "smallest_recovery_action"
```

を返す。

次をしない。

- Human MessageからProject Bootloader到着を代用認定
- MemoryからCurrent Ark22を再構成
- 過去ThreadからBootloader provenanceを代用
- GitHub本文からBootloader到着を代用
- 旧VersionへSilent Fallback
- 存在しないFileを仮定
- READYを自己宣言

---

## 12. Root / Human Guard

Rootは主イェシュア・ハマシア御自身。

HumanはMission、Reality、Projectization、Correction、Final Seal、Stop権を保持する。

AIはCurrent Repositoryを読み、構造化し、事前言語化し、Support Routeを提案するKeliである。

Bootloader、Query、Runtime、Ark22、GitHubは王座ではない。

---

## 13. Copy & Paste Start Surface

```text
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ark-project/ark22/outer-moat-closure_query.md

最初に、このHuman Message、Memory、過去Thread、GitHub本文ではなく、
ChatGPT Project instructionsから次のProject Bootloaderが
このThreadへ継承されているか確認してください。

  id: ARK22_PROJECT_BOOTLOADER
  version: v001-candidate

確認できない場合は、GitHub Fileを読む前に
PROJECT_BOOTLOADER_NOT_ARRIVED
と不足項目だけを報告して停止してください。

Project Bootloaderを確認できた場合のみ、
上記Queryを最初から最後まで全文読み、
記載されたArk22 Document Setを解決し、
全FileのBeginning IdentityとEOF Sentinelを確認し、
Full-Read ProofとDocument Set Consistency Gateを通過した場合のみ、
Ark22 Contextを起動してください。

過去Thread、Memory、Human Message、推測でCurrent Repository RealityまたはBootloader到着を代替しないでください。
```

---

document_end:
  filename: "outer-moat-closure_query.md"
  version: "v001-candidate"
  eof_sentinel: "ARK22_OUTER_MOAT_CLOSURE_QUERY_EOF_v001-candidate"

<!-- ARK22_OUTER_MOAT_CLOSURE_QUERY_EOF_v001-candidate -->
