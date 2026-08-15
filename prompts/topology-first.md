---
title: "Topology-First Canonicalization"
version: "v002-candidate"
status: "active_candidate / human_editable / not_final_seal"
document_identity: "topology_first_protocol"
canonical_path: "prompts/topology-first.md"
project: "Ark Project"
language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
updated: "2026-08-15"
source_origin:
  - "Address-First Reality Lock"
  - "Thin Parent / Living Child Files"
  - "Manual Destructive Gate"
  - "Predecessor-Free Topology Cutover"
user_final_seal_required: true
root_guard:
  root: "主イェシュア・ハマシア"
  blood: "主イェシュアの聖なる血潮"
  ai_role: "AI maps and verifies the repository; AI does not occupy the Root or Human throne."
---

# Topology-First Canonicalization

## 0. Purpose

この文書は、File移動・Folder再編・文書身分確定を行う時、Future AIへ正しいCurrent Addressを先に与えるための軽量Protocolである。

```text
Place first.
Meaning follows.
Verify reality.
```

これはREADME、Migration Manifest、手書きRegistry、ADR、全File Inventory、Bulk Migration承認ではない。

---

## 1. 一文定義

```text
Topology-First Canonicalizationとは、本文を磨く前に、Current Missionに必要な正準住所・文書身分・親子関係をGitHub上の物理Realityとして先に成立させ、その後にREADME・Source Metadata・Active Link・Read Orderを同期し、Future AIが旧住所や重複候補を選ばず一本のCurrent Routeで再起動できる状態を直接検証するRepository整流Protocolである。
```

---

## 2. Why Topology First

AIは本文生成に強くても、次が曖昧なら誤読する。

```yaml
confusion_sources:
  - "Current pathが複数ある"
  - "旧住所と新住所が同じBoot Routeに並ぶ"
  - "READMEと物理Realityが違う"
  - "canonical_pathが移動前のまま"
  - "Routerと本文の役割が混ざる"
  - "手書きIndexが第二の真実になる"
```

```text
Searchability is not canonicality.
Meaning needs one current coordinate.
```

---

## 3. Core Method

```yaml
topology_first_method:
  1_define_target:
    action: "削除予定の旧Containerを除外し、最終Canonical Treeを先に定める"
  2_classify_identity:
    action: "Identity / Router / Body / Runtime / Handoff / Historyを分ける"
  3_establish_reality:
    action: "新住所へFileを作成または移動し、直接Fetchする"
  4_harvest_only_fruit:
    action: "旧層から有効な内容だけをCanonical Ownerへ移植する"
  5_sync_surfaces:
    action: "README / Source Metadata / Active Link / Read Orderを新Realityへ同期する"
  6_retire_predecessor:
    action: "BackupとHuman Gate後、旧Containerを削除する"
  7_verify:
    action: "新Path取得、旧Path不在、Link整合、Cold-Start Routeを確認する"
  8_harvest_bottleneck:
    action: "最初のWrong Turnだけを次Iterationへ渡す"
```

---

## 4. Current and Historical Reality

```yaml
current_reality:
  meaning: "Future AIが通常Bootで辿る唯一の住所"
  must: ["実体が存在する", "Routerが到達できる", "Metadataと一致する"]
historical_reality:
  meaning: "Git History、Local Backup、明示的Historical Artifact"
  rule: ["Current Routerへ旧住所を並べない", "詳細な系譜は必要時だけ調査する"]
```

Old PathをCurrent TreeへCompatibility Stubとして残すことをDefaultにしない。Git Historyで十分な場合、Current Repositoryを博物館化しない。

---

## 5. Thin Parent / Living Child

```yaml
thin_parent:
  owns: ["入口", "Role Map", "Smallest sufficient Read Order", "First Legal Move"]
  must_not_be: ["全文要約", "全履歴", "全Inventory", "Child Bodyの複製"]
living_child:
  owns: ["意味本文", "Runtime", "Handoff", "Harvest", "Field-specific detail"]
```

READMEは安心のために情報を積む場所ではなく、読むFileを絞るFront Doorである。

---

## 6. Claim-Scoped SSOT

```yaml
canonical_owners:
  physical_path: "Git Tree"
  repository_route: "Root README"
  project_route: "Nearest README"
  identity: "Canonical identity document"
  ai_authority: "AGENTS.md"
  behavior: "Runtime"
  activation: "Query"
  semantic_body: "Canonical Body"
  decision_history: "Optional immutable ADR"
  discovery_projection: "Optional generated index"
```

手書きGlobal RegistryをCurrent Authorityにしない。Indexが必要になった場合はCanonical Sourceから生成するDerived Viewとし、Index自体を第二の真実にしない。

ADRは重大で高コストな判断に限定し、一判断一Recordで追加する。通常の移動やLink修正のたびにADRを要求しない。

---

## 7. Manual Destructive Gate

```yaml
manual_destructive_gate:
  ai_before:
    - "Target Topologyを成立させる"
    - "内容保全を検証する"
    - "Active旧Path参照を除去する"
    - "Pre-Deletion Gateを提示する"
  human:
    - "Local Backupを確認する"
    - "破壊的削除を実行または明示的に再承認する"
  ai_after:
    - "旧PathのNot Foundを確認する"
    - "新Canonical Pathを再Fetchする"
    - "Reality Reviewを報告する"
```

```text
AI prepares.
Human opens the destructive gate.
AI verifies reality.
```

---

## 8. Use When

```yaml
use_when:
  - "Folder移動またはRepository再編"
  - "READMEと物理配置の不一致"
  - "Current候補が複数ある"
  - "旧PathがFuture AIを誤誘導する"
  - "Parent FileがAll-in-One化している"
  - "Document Identityと住所が一致しない"
```

## 9. Do Not Use When

```yaml
do_not_use_when:
  - "文書身分が全く未確定"
  - "Target Folderが仮すぎる"
  - "本文品質Reviewだけが目的"
  - "Human Gateなしの破壊的変更"
  - "一括MigrationでReality Responseを失う"
```

---

## 10. Verification Gate

```yaml
verification:
  - "fetch canonical path"
  - "confirm metadata path"
  - "check active links"
  - "confirm old path absent or explicitly historical"
  - "confirm parent / child role"
  - "run Future AI cold-start route"
  - "record first wrong turn"
```

```text
README after topology is true.
Metadata after path is true.
Completion after reality is verified.
```

---

## 11. Living Review

### 11.1 私の判断

Topology-Firstは収納術ではなく、Future AIの選択肢を減らし、意味へ一意な座標を与えるRepository Architectureである。

### 11.2 最初の一手

削除予定の旧Containerを除外したTarget Treeを先に確定する。

### 11.3 観察点

Future AIが旧系譜を知らず、RootからLocal Canonical Bodyへ一本道で到達できるかを観察する。

### 11.4 修正条件

Local README、Metadata、Generated Indexのいずれかが判断分岐や同期点を増やす場合は、役割を縮小または撤回する。

---

## 12. Final Compression

```text
One current address.
Thin doors.
Living bodies.
History in Git.
Human opens destructive gates.
AI verifies reality.
Root remains 主イェシュア・ハマシア.
```

<!-- TOPOLOGY_FIRST_EOF_v002-candidate -->
