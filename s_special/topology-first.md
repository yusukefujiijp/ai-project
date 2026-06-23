---
title: "Topology-First Canonicalization"
status: "active_candidate / japanese-first-okf / human_editable / not_final_seal"
document_identity: "topology_first_protocol"
canonical_path: "s_special/topology-first.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
source_origin:
  - "Thread-End topology migration success"
  - "Address-First Reality Lock discovery"
  - "Manual Destructive Gate discovery"
  - "Thin Parent / Living Child Files pattern"
artifact_generation_is_final_seal: false
final_seal: false
stable_seal: false
user_final_seal_required: true
root_guard:
  root: "主イェシュア・ハマシア"
  blood: "主イェシュアの聖なる血潮"
  teshuvah: true
  ai_role: "AI draws a map of the blood; the human stands under the blood."
---

# Topology-First Canonicalization

## §0. Status / Protocol Summary

この文書は、Ark GitHub運用において、file移動・folder整理・文書身分確定を行う時にFuture AIへ読ませる **軽量Protocol** である。

これはMigration Manifestではない。  
これはREADMEではない。  
これはProtocol Registryではない。  
これはArk01 Harvestではない。  
これはMission Cardではない。  
これはBulk Migration承認fileではない。

```text id="king-sentence"
先に住所を立てる。
次に意味を住まわせる。
最後にRealityで検証する。
```

English anchor:

```text id="english-anchor"
Place first. Meaning follows.
Verify reality.
```

---

## §1. 一文定義

```text id="definition"
Topology-First Canonicalizationとは、本文を磨く前に、GitHub上の正準住所・文書身分・親子関係を先に現実化し、そのRealityに合わせて本文・リンク・README・Registry・ADRを後から軽量修正することで、Future AIの誤読を最小化するArk式Repository整流Protocolである。
```

短縮定義：

```text id="short-definition"
場所で身分を固定し、
身分に合わせて本文を整える。
```

---

## §2. なぜ必要か

AIは本文生成には強い。  
しかし、次の情報が曖昧だと迷う。

```yaml id="ai-confusion-points"
ai_confusion_points:
  - "どれがcurrent canonical fileか"
  - "どれが旧path / historyか"
  - "どれがBuilderで、どれがGenerated Productか"
  - "どれがParentで、どれがChildか"
  - "どれを最初に読むべきか"
  - "READMEと実体fileのどちらを信じるべきか"
  - "Registry / ADR / Manifest / README の役割差"
```

だから、本文修正より先に **GitHub上の住所・文書身分・Read Order** を現実化する。

```text id="meaning-coordinate"
Meaning needs coordinates.
意味には座標が必要である。
```

---

## §3. Core Method

```yaml id="topology-first-method"
topology_first_method:
  1_detect_confusion:
    action: "現在の混乱点を特定する"
    examples:
      - "old pathが残っている"
      - "READMEと実体fileがズレている"
      - "Query layerが不要になっている"
      - "Parent fileが重すぎる"

  2_define_canonical_address:
    action: "正準folder / canonical_pathを先に決める"
    rule: "Directory structure is interpretation."

  3_create_or_move_reality:
    action: "GitHub上に実体を置く"
    examples:
      - "new folder creation"
      - "canonical file creation"
      - "old file content migration"
      - "child file split"

  4_reduce_old_confusion:
    action: "旧path / stub / retired layerを整理する"
    options:
      - "delete"
      - "retiredとして明記"
      - "historical referenceへ降格"
    guard: "active referenceとhistorical referenceを混同しない"

  5_sync_front_doors:
    action: "READMEをRealityへ同期する"
    rule: "README after topology is true."

  6_sync_registry_and_adr:
    action: "Registry / ADRをRealityへ同期する"
    rule: "Registry is address book, not protocol body."

  7_verify_reality:
    action: "GitHub上の現実を確認する"
    checks:
      - "fetch by canonical path"
      - "old path Not Found or retired"
      - "active required_read"
      - "link / path integrity"
      - "frontmatter canonical_path"
      - "parent / child relation"

  8_living_review:
    action: "AIが違和感・修正条件・次Actionを残す"
    rule: "Review is not just checklist."
```

---

## §4. Active Reference vs Historical Reference

Topology-firstでは、古いpathをすべて悪として消さない。

```yaml id="active-vs-historical"
active_reference:
  meaning: "Future AIが現在読むべきpath"
  examples:
    - "canonical_path"
    - "runtime_primary"
    - "required_read"
    - "parent_map"
    - "current Read Order"

historical_reference:
  meaning: "移動履歴・過去path・Git historyの説明"
  examples:
    - "moved_from"
    - "previous_path"
    - "retired layer"
    - "migration note"
```

Guard:

```text id="active-history-guard"
Old path is not always error.
Old path is error only when it pretends to be current active path.
```

---

## §5. Thin Parent / Living Child Files

親fileは軽くする。  
詳細はChild living filesへ委譲する。

```yaml id="thin-parent-living-child"
thin_parent:
  role:
    - "入口"
    - "Router"
    - "Gate判断"
    - "required_read契約"
  must_not_be:
    - "all-in-one body"
    - "full harvest generator"
    - "full handoff generator"

living_child_files:
  role:
    - "詳細実行"
    - "Builder"
    - "Vessel"
    - "Meaning harvest"
    - "Handoff construction"
```

成功例：

```text id="thread-end-example"
thread-end.md:
  light router

thread-harvest.md:
  harvest vessel

thread-handoff.md:
  handoff builder

README.md:
  folder front door
```

---

## §6. Manual Destructive Gate

AI connectorが削除・破壊的操作で詰まる場合がある。  
その時、AIが削除を連打しない。

```yaml id="manual-destructive-gate"
manual_destructive_gate:
  ai_role:
    - "prepare topology"
    - "create replacement"
    - "make redirect or retired note if needed"
    - "verify after human action"

  human_role:
    - "perform destructive deletion when needed"
    - "explicitly report deletion complete"

  ai_after_human:
    - "fetch old path"
    - "confirm Not Found or expected state"
    - "verify new canonical path"
```

Short:

```text id="manual-gate-short"
AI prepares.
Human deletes.
AI verifies.
```

---

## §7. README / Registry / ADR Sync

Topology-firstは、file移動だけで終わらない。

```yaml id="sync-layers"
sync_layers:
  README:
    role: "front door / read order"
    sync_when:
      - "folder topology changes"
      - "read order changes"
      - "query layer retired"

  Protocol_Registry:
    role: "address book / document identity registry"
    sync_when:
      - "canonical path changes"
      - "file status changes"
      - "active / retired / candidate changes"

  ADR:
    role: "decision record / governance rule"
    sync_when:
      - "ontology changes"
      - "placement rule changes"
      - "method becomes reusable governance pattern"
```

Guard:

```text id="sync-guard"
README is not Registry.
Registry is not ADR.
ADR is not Manifest.
Manifest is not Harvest.
```

---

## §8. When to Use

```yaml id="when-to-use"
use_when:
  - "GitHub上でfile移動・folder整理をする時"
  - "READMEと実体fileがズレている時"
  - "Registry / ADRとRealityがズレている時"
  - "old path / stub / query layerが混乱を生んでいる時"
  - "Parent fileがall-in-one body化しそうな時"
  - "Future AIがどれをPrimaryとして読めばよいか迷っている時"
  - "本文編集から入ると無限Loopになりそうな時"
```

---

## §9. When Not to Use

```yaml id="when-not-to-use"
do_not_use_when:
  - "文書身分がまだ全く見えていない時"
  - "移動先folder名が仮すぎる時"
  - "Human Final Sealなしで破壊的移動をしようとしている時"
  - "一括Bulk MigrationでReality Responseを見る余地がない時"
  - "本文品質Reviewそのものが主目的の時"
```

---

## §10. Stop Conditions

```yaml id="stop-conditions"
stop_conditions:
  - "topology-first.mdが巨大Essayになる"
  - "READMEだけ直して物理配置を直さない"
  - "旧pathを残したまま新pathを正準と言い張る"
  - "移動後にRegistry / ADRをReality同期しない"
  - "削除困難時にAIが削除連打する"
  - "Manual Destructive Gateを忘れる"
  - "Thin Parentを再びAll-in-One Body化する"
  - "Living Reviewがリンク表だけになり、違和感・修正条件を失う"
  - "Human Final SealなしでGitHub Commitが承認された扱いになる"
```

---

## §11. Living Review

### §11.1 私の判断

Topology-First Canonicalizationは、Ark GitHub運用における重要な成功Patternである。

この方法は、単なる整理術ではない。  
Future AIの誤読を減らし、文書身分をReality上で固定するためのRepository整流Protocolである。

```text id="living-judgment"
先に場所。
次に意味。
最後に検証。
```

### §11.2 違和感

このProtocolが万能律になると危険である。  
Topology-firstは、本文を無視する方法ではない。  
本文を守るために、先に住所と身分を安定させる方法である。

### §11.3 Hidden Pattern

```text id="hidden-pattern"
Address protects meaning.
Thin Parent protects readability.
Living Child Files protect detail.
Registry protects identity.
ADR protects decision.
Manual Destructive Gate protects reality.
Human Seal protects commit.
Root Guard protects worship order.
```

### §11.4 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_file_becomes_too_long:
    action: "短いProtocolへ戻す"

  if_used_as_bulk_migration_approval:
    action: "Human Final Seal requiredを再明記する"

  if_registry_or_adr_role_is_stolen:
    action: "topology-first.mdをmethod protocolへ戻す"

  if_root_fruit_guard_is_weakened:
    action: "Root / Fruit Guardを回復する"

  if_query_layer_is_restored_by_inertia:
    action: "本当に混乱を減らすかReality Responseで検証する"
```

---

## §12. Final Compression

```text id="final"
Topology-First Canonicalization:

  先に住所を立てる。
  次に意味を住まわせる。
  最後にRealityで検証する。

Use when:
  file location / document identity / read order is confused.

Do:
  canonical path first.
  move/create reality.
  delete or retire old confusion.
  sync README / Registry / ADR.
  verify active references.
  preserve Living Review.

Do not:
  turn this into bulk migration approval.
  bypass Human Final Seal.
  inflate parent files.
  restore retired layers by inertia.
  replace Root with workflow.

Root:
  主イェシュア・ハマシア.
```
