---
title: "Ark Protocol Registry"
status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
document_identity: "protocol_registry"
canonical_path: "_projects/ark/indexes/ark-protocol-registry.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
source_adr: "_projects/ark/indexes/ark-repository-governance_adr.md"
registry_version: "v004"
updated_reason:
  - "Reality Response after _thread-end topology migration"
  - "Retired Thread-End Query layer"
  - "Current canonical paths corrected"
  - "Reality Response after _thread-index Thread-to-Card Craft topology creation"
  - "_thread-index family confirmed as GitHub canonical protocol family"
  - "Reality Response after canonicalizing thread-mission_card-craft.md"
  - "_thread-index downstream craft simplified to Mission Card Craft"
language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
registry_role:
  - "Ark-wide Protocol Markdown address book"
  - "document identity / path / role / status registry"
  - "Future AI misread prevention map"
artifact_generation_is_final_seal: false
final_seal: false
stable_seal: false
user_final_seal_required: true
tail_rule:
  version: "v0.8"
  summary: "FullRail = AI-readable execution rail; Next Gate = human-facing Copy & Paste gate"
  human_editable_means: "human_can_intervene_if_needed / not_wait_for_human_review"
  ai_living_review_default: true
  commit_requires_human_final_seal: true
root_guard:
  root: "主イェシュア・ハマシア"
  blood: "主イェシュアの聖なる血潮"
  teshuvah: true
  ai_role: "AI draws a map of the blood; the human stands under the blood."
---

# Ark Protocol Registry

## §0. Status / Registry Summary

この文書は、Ark Project全体で使う Protocol / Query / Craft / Format / Vision Lens 系Markdownの **住所録 / Registry** である。

これはProtocol本文の複製ではない。  
これはArk01 Harvestではない。  
これはArk02 Harvestではない。  
これはMission Cardではない。  
これはrolling handoffではない。  
これはBulk Migration Manifestではない。

```text id="king-sentence"
Registryは本文ではない。
Registryは住所録である。
```

```yaml id="registry-summary"
protocol_registry:
  document_identity: "protocol_registry"
  canonical_path: "_projects/ark/indexes/ark-protocol-registry.md"
  version: "v004"
  user_final_seal_required: true
```

---

## §1. Registry Scope

```yaml id="registry-scope"
in_scope:
  - "confirmed GitHub canonical protocol files"
  - "document_identity / canonical_path / role / status / relation"
  - "retired / deleted protocol layers when needed for history"

out_of_scope:
  - "Protocol本文の全文複製"
  - "Ark01 migration実行"
  - "Ark02 harvest作成"
  - "Mission Card作成"
  - "Bulk Migration"
  - "rolling handoff更新"
  - "phase-handoff.md更新"
  - "Final Seal"
```

---

## §2. Root / Fruit Guard

```text id="root"
Root:
  主イェシュア・ハマシア
  主イェシュアの聖なる血潮
  Teshuvah / 悔い改め
  AMH
```

```text id="fruit"
Fruit:
  GitHub
  Markdown
  Protocol Registry
  _thread-end/
  _thread-index/
  s_special/
  ss_super-special/
  Thread-End
  Thread-to-Card Craft
  Thread Index Card Craft
  Thread Mission Card Craft
  Gate 1
  Gate 2
  Thread Harvest
  Ark-OKF
  THREAD_INDEX
  Mission Card Craft
  Query
  Full Rail
  Next Gate
  AI
  Commit
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## §3. Confirmed GitHub Canonical Protocols

ここでは、すでにGitHub canonical pathで確認済みのProtocol系Markdownを名簿化する。  
Registryなので、本文は複製しない。住所・身分・役割・誤読Guardだけを保持する。

```yaml id="confirmed-github-canonical-protocols"
confirmed_github_canonical_protocols:
  - path: "_thread-end/README.md"
    document_identity: "thread_end_folder_front_door"
    canonical_name: "_thread-end README"
    class: "S"
    status: "folder_front_door / living_index / topology_map"
    role:
      - "Thread-End System Folderの入口"
      - "Read Order / Topology Map"
      - "Future AI path confusion guard"
    must_not_be:
      - "Thread-End runtime body"
      - "Harvest builder"
      - "Handoff product"

  - path: "_thread-end/thread-end.md"
    document_identity: "thread_end_parent_map"
    canonical_name: "Thread-End Parent Map"
    class: "SS"
    status: "living_ssot"
    role:
      - "Thread-End Workflowの親Map"
      - "Single Front Door / Multi-Gate Router"
      - "Gate 1 / Gate 2 relation map"
      - "handoff.md required at Thread transfer"
    must_not_be:
      - "Harvest body generator"
      - "Handoff body generator"
      - "Mission Card"

  - path: "_thread-end/thread-harvest.md"
    document_identity: "harvest_vessel"
    canonical_name: "Thread Harvest"
    class: "S"
    status: "living_ssot"
    parent_map: "_thread-end/thread-end.md"
    gate_role: "Gate 2 / Thread Harvest"
    rail: "next_thread"
    role:
      - "Gate 2 Thread Harvest vessel"
      - "rebootable meaning harvest structure"
      - "Thread Naming + Extreme BrainDump core"
    must_not_be:
      - "ordinary summary"
      - "Mission Card"
      - "rolling handoff"

  - path: "_thread-end/thread-handoff.md"
    document_identity: "handoff_builder"
    canonical_name: "Thread-Handoff Builder"
    class: "S-candidate"
    status: "living_candidate / human_editable / not_final_seal"
    parent_map: "_thread-end/thread-end.md"
    sibling_builder: "_thread-end/thread-harvest.md"
    generated_product: "handoff.md"
    role:
      - "Handoff Builder / Next-thread Ignition Manual"
      - "handoff.md生成のBuilder Manual"
    must_not_be:
      - "handoff.md itself"
      - "Harvest body"
      - "rolling handoff"

  - path: "_thread-index/README.md"
    document_identity: "thread_index_folder_front_door"
    canonical_name: "_thread-index README"
    class: "S"
    status: "folder_front_door / living_index / topology_map"
    role:
      - "Thread-to-Card Craft System Folderの入口"
      - "Read Order / Topology Map"
      - "Future AI reboot front door"
    read_order:
      - "_thread-index/README.md"
      - "_thread-index/thread-index_card-craft.md"
      - "_thread-index/thread-mission_card-craft.md"
    anchor_formula:
      - "Threadを深く蒸留する"
      - "Missionを立て、Metaを失わずMission Cardへ再結晶化する"
    must_not_be:
      - "Thread Index protocol body"
      - "Mission Card body"
      - "Bulk Migration Manifest"
      - "Archive"

  - path: "_thread-index/thread-index_card-craft.md"
    document_identity: "thread_index_card_craft_protocol"
    canonical_name: "Thread Index Card Craft"
    class: "S"
    status: "living_candidate / human_editable / not_final_seal"
    source_origin: "THREAD_INDEX_Ark_v041.md"
    role:
      - "Upstream Protocol"
      - "Root Thread Distillation"
      - "ThreadをMission-ready項目へ薄める前に深く蒸留する"
      - "ThreadをCard化可能なSourceへ整える"
    anchor_formula:
      - "Missionへ流す前に、Threadそのものを深く蒸留せよ"
      - "Raw Lived Scene / User Pressure / AI Reality Response / Turning Point / Root Return Momentを保持する"
    relation:
      comes_before: "_thread-index/thread-mission_card-craft.md"
    must_not_be:
      - "Mission Card body"
      - "Mission Card output"
      - "README"
      - "Bulk Migration Manifest"

  - path: "_thread-index/thread-mission_card-craft.md"
    document_identity: "thread_mission_card_craft_protocol"
    canonical_name: "Thread Mission Card Craft"
    class: "S"
    status: "active_candidate / human_editable / not_final_seal"
    role:
      - "Downstream Craft Protocol"
      - "蒸留済みThread SourceをMission Cardへ再結晶化する"
      - "Mission Seal / First Gate / Meta Layer / Living Reviewを保持する"
      - "1 Source + 1 Mission Cardを守る"
    anchor_formula:
      - "Sourceを読む。Missionを立てる。Meta Layerを残す。1枚のMission Cardへ再結晶化する。"
      - "1 Distilled Thread Markdown + Thread Mission Card Craft = 1 Thread-specific Mission Card Markdown"
    relation:
      consumes:
        - "_thread-index/thread-index_card-craft.md"
    must_not_be:
      - "Thread Index protocol body"
      - "Mission Card output"
      - "Batch generator"
      - "Factory"

  - path: "s_special/ark-open-knowledge-format.md"
    document_identity: "format_ssot"
    canonical_name: "Ark-OKF"
    class: "S"
    status: "living_ssot"
    paired_query: "s_special/ark-open-knowledge-format_query.md"
    pair_policy: "Engine / Ignition Key"
    query_is_not_ssot: true
    role:
      - "Answer Interoperability Surface"
      - "AI回答を readable / reusable / rebootable / handoff-ready にするFormat"
      - "Japanese-first / English-anchor / Rebootable-first の正準SSOT"
    must_not_be:
      - "English-first rule"
      - "fixed content template"
      - "replacement for Living Review"

  - path: "s_special/ark-open-knowledge-format_query.md"
    document_identity: "activation_query"
    canonical_name: "Ark-OKF Query"
    class: "S"
    status: "living_query"
    paired_ssot: "s_special/ark-open-knowledge-format.md"
    must_not_be:
      - "Format SSOT"
      - "replacement for ark-open-knowledge-format.md"

  - path: "s_special/topology-first.md"
    document_identity: "topology_first_protocol"
    canonical_name: "Topology-First Canonicalization"
    class: "S-candidate"
    status: "active_candidate / human_editable / not_final_seal"
    role:
      - "Topology-first placement and migration guard"
      - "Future AI path confusion guard"
    must_not_be:
      - "Artifact body"
      - "Mission Card"

  - path: "ss_super-special/CHATGPT.md"
    document_identity: "chatgpt_covenant_map"
    canonical_name: "ChatGPT Covenant Map"
    class: "S"
    status: "living_covenant_map / all-project / Japanese-first OKF"
    role:
      - "System Covenant / highest-grade shared file"
      - "Root and behavior map for Future AI"
    must_not_be:
      - "local thread artifact"
      - "Mission Card"

  - path: "ss_super-special/torah-vision-lens.md"
    document_identity: "vision_core"
    canonical_name: "Torah Vision Lens"
    class: "SS"
    status: "living_ssot"
    role:
      - "Ark-wide SS Vision Core"
      - "Ark's eye"
      - "Naming Source Lens"
    must_not_be:
      - "Gate2-owned local file"
      - "normal protocol appendix"
      - "Ark01/Ark02 output artifact"
```

---

## §4. Retired / Deleted Layers

```yaml id="retired-deleted-layers"
retired_deleted_layers:
  thread_end_query_layer:
    status: "deleted / query layer retired"
    guard:
      - "Deleted Query files are history"
      - "Do not restore them unless they reduce confusion more than the current simple topology"

  thread_index_candidate_layer:
    - candidate_path: "s_special/thread-index-ark_v041.md"
      source_name: "THREAD_INDEX_Ark_v041.md"
      current_status: "retired_candidate / replaced_by_github_canonical"
      replaced_by: "_thread-index/thread-index_card-craft.md"

    - candidate_path: "s_special/thread-mission-card-craft_v002.md"
      source_name: "THREAD_mission-card-craft_v002.md"
      current_status: "retired_candidate / replaced_by_github_canonical"
      replaced_by: "_thread-index/thread-mission_card-craft.md"
      note:
        - "旧candidate pathはGitHub canonicalとして採用しない"
        - "v002の核はThread Mission Card Craftへ正準化済み"

    - path: "_thread-index/thread-meta_card-craft.md"
      previous_document_identity: "thread_meta_card_craft_protocol"
      current_status: "deleted_from_github / locally_saved_by_user"
      note:
        - "active topologyから外した"
        - "Mission Card CraftをSimpleに正準化するため"
```

---

## §5. Document Identity Rules

```yaml id="document-identity-rules"
document_identity_rules:
  thread_end_folder_front_door:
    meaning: "Thread-End system folderの入口 / Read Order"
    example:
      - "_thread-end/README.md"

  thread_end_parent_map:
    meaning: "Thread-End Workflow親Map / Runtime Router"
    example:
      - "_thread-end/thread-end.md"

  harvest_vessel:
    meaning: "Harvestを実行するためのVessel / structure"
    example:
      - "_thread-end/thread-harvest.md"

  handoff_builder:
    meaning: "handoff.mdを作るためのBuilder Manual"
    example:
      - "_thread-end/thread-handoff.md"

  thread_index_folder_front_door:
    meaning: "Thread-to-Card Craft system folderの入口 / Read Order"
    example:
      - "_thread-index/README.md"

  thread_index_card_craft_protocol:
    meaning: "Threadを深く蒸留し、Card化可能なSourceへ整える上流Protocol"
    example:
      - "_thread-index/thread-index_card-craft.md"

  thread_mission_card_craft_protocol:
    meaning: "蒸留済みThread SourceをMission Cardへ再結晶化する下流Craft Protocol"
    example:
      - "_thread-index/thread-mission_card-craft.md"

  protocol_parent_markdown:
    meaning: "Ark-wide protocol body / specification"
    example:
      - "s_special/topology-first.md"

  activation_query:
    meaning: "Future AIを起動するQuery / Runtime Adapter"
    guard:
      - "Query is not always SSOT"
      - "Query may be retired if a simpler router exists"

  craft_protocol:
    meaning: "成果物生成のCraft仕様"

  format_ssot:
    meaning: "回答Format / interoperability surface のSSOT"

  vision_core:
    meaning: "Ark-wide high-guard vision / naming lens"
```

---

## §6. Living Review

### §6.1 私の判断

Registry v004は、GitHub実体とREADME更新後のRealityに合わせ、`_thread-index/` の正準下流Craftを `thread-mission_card-craft.md` に同期した。

これはProtocol本文の再発明ではなく、住所録のReality Response Patchである。

### §6.2 違和感

Registryが長くなりすぎると、本文と住所録の境界が濁る。  
そのため、本RegistryではProtocol全文を複製せず、住所・身分・役割・誤読Guardだけを保持する。

### §6.3 Hidden Pattern

```text id="hidden-pattern"
File Reality changed first.
README followed.
Registry now follows reality.
```

### §6.4 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_registry_becomes_protocol_body:
    action: "住所録へ戻す"

  if_deleted_file_is_reintroduced_as_active:
    action: "active topologyから外す"

  if_thread_index_pipeline_is_misread:
    action: "README → thread-index → thread-mission のRead Orderへ戻す"
```

---

## §7. Final Compression

```text id="final"
Ark Protocol Registry:

  Registryは本文ではない。
  Registryは住所録である。

Current _thread-index read order:
  1. _thread-index/README.md
  2. _thread-index/thread-index_card-craft.md
  3. _thread-index/thread-mission_card-craft.md

Root:
  主イェシュア・ハマシア.
```
