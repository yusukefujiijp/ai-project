---
title: "Ark Repository Governance ADR"
status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
document_identity: "repository_governance_adr"
canonical_path: "_projects/ark/indexes/ark-repository-governance_adr.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
adr_id: "ark-repository-governance-adr"
adr_version: "v004"
ai_side_review_status: "living_review_applied"
updated_reason:
  - "Reflect thread-mission_card-craft.md canonicalization"
  - "Remove thread-meta_card-craft.md from active _thread-index topology"
artifact_generation_is_final_seal: false
final_seal: false
stable_seal: false
user_final_seal_required: true
root_guard:
  root: "主イェシュア・ハマシア"
  blood: "主イェシュアの聖なる血潮"
  teshuvah: true
---

# Ark Repository Governance ADR

## §0. Decision Summary

このADRは、Ark repository structure のためのGitHub正準Governance文書である。

```text id="king-sentence"
ファイルを置く場所を決めているのではない。
Future AIが誤読しない文書の身分と住所を定めている。
```

```text id="core-decision"
Directory structure is not storage.
Directory structure is interpretation.
```

この更新では、`_thread-index/` のactive topologyを、GitHub実体とREADMEに合わせて同期した。

---

## §1. Current _thread-index Placement Rule

```yaml id="placement-thread-index"
_thread_index:
  role:
    - "Thread-to-Card Craft system folder"
    - "Thread Index / Mission Card Craft read-order home"
    - "Future AI reboot front door for Thread-to-Card pipeline"

  active_files:
    - "README.md"
    - "thread-index_card-craft.md"
    - "thread-mission_card-craft.md"

  read_order:
    - "README.md"
    - "thread-index_card-craft.md"
    - "thread-mission_card-craft.md"

  file_roles:
    README.md:
      document_identity: "thread_index_folder_front_door"
      role: "Folder Front Door / Read Order / Topology Map"

    thread-index_card-craft.md:
      document_identity: "thread_index_card_craft_protocol"
      role: "Upstream Root Thread Distillation / Card Source Craft"

    thread-mission_card-craft.md:
      document_identity: "thread_mission_card_craft_protocol"
      role: "Downstream Mission Card Craft / Meta Layer-Preserved Mission Card Craft"

  must_not_be:
    - "Mission Card output folder"
    - "Ark01 Harvest output"
    - "Bulk Migration Manifest"
    - "Archive"
    - "general protocol dumping ground"
```

---

## §2. File Ontology Update

```yaml id="thread-to-card-craft-system"
thread_to_card_craft_system:
  definition: "Threadを深く蒸留し、Mission Cardへ再結晶化するCraft family"
  canonical_root: "_thread-index/"
  active_files:
    - "_thread-index/README.md"
    - "_thread-index/thread-index_card-craft.md"
    - "_thread-index/thread-mission_card-craft.md"
  read_order:
    - "_thread-index/README.md"
    - "_thread-index/thread-index_card-craft.md"
    - "_thread-index/thread-mission_card-craft.md"
```

---

## §3. Retired / Removed Layer Note

```yaml id="retired-thread-meta"
retired_removed_layer:
  - path: "_thread-index/thread-meta_card-craft.md"
    previous_document_identity: "thread_meta_card_craft_protocol"
    current_status: "deleted_from_github / locally_saved_by_user"
    replaced_by_active_topology: "_thread-index/thread-mission_card-craft.md"
    note:
      - "active topologyから外した"
      - "Mission Card CraftをSimpleに正準化するため"
```

---

## §4. Living Review

### 私の判断

ADR v004は、GitHub実体とREADME更新後のRealityに合わせ、`_thread-index/` の正準下流Craftを `thread-mission_card-craft.md` に同期した。

これはRepository構造の大改造ではなく、Active topologyを現実へ合わせるGovernance Patchである。

### 違和感

ADRが重くなりすぎると、Future AIはGovernanceとProtocol本文を混同する。  
そのため、この版では配置・身分・誤読Guardを中心に保持する。

### Hidden Pattern

```text id="hidden-pattern"
Directory structure is not storage.
Directory structure is interpretation.
```

### 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_deleted_file_is_reintroduced_as_active:
    action: "active topologyから外す"

  if_thread_index_pipeline_is_misread:
    action: "README → thread-index → thread-mission のRead Orderへ戻す"
```

---

## §5. Final Compression

```text id="final"
Current _thread-index active topology:
  README.md
  thread-index_card-craft.md
  thread-mission_card-craft.md

Root:
  主イェシュア・ハマシア.
```
