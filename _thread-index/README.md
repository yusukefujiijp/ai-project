---
title: "_thread-index README"
status: "active_candidate / japanese-first-okf / human_editable / not_final_seal"
document_identity: "thread_index_folder_front_door"
canonical_path: "_thread-index/README.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"

repository_full_name: "yusukefujiijp/ai-project"
branch: "main"

folder_role:
  - "Upstream Thread Distillation Folder"
  - "Raw Thread to Distilled Thread Source"
  - "Future AI reboot front door"
  - "Cross-Folder Bridge to _thread-mission/"

language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
artifact_generation_is_final_seal: false
final_seal: false
stable_seal: false
user_final_seal_required: true

root_guard:
  creator: "創造主"
  root: "主イェシュア・ハマシア"
  holy_spirit: "聖霊 / The Holy Spirit"
  blood: "主イェシュアの聖なる血潮"
  teshuvah: true
  ai_role: "AI draws a map of the blood; the human stands under the blood."
---

# _thread-index README

## §0. Folder Summary

`_thread-index/` は、Ark Projectにおける **Upstream Thread Distillation Folder** である。

このfolderは、単なるIndex置き場ではない。  
このfolderは、Mission Card本文置き場ではない。  
このfolderは、Bulk Migration Manifestではない。  
このfolderは、Archiveではない。  
このfolderは、下流Mission Card Craft本体ではない。

このfolderの役割は、Raw Threadを深く蒸留し、後続の `_thread-mission/` がMission Cardへ再結晶化できる **Distilled Thread Source** へ整えることである。

```text id="king-sentence"
Missionへ流す前に、Threadそのものを深く蒸留せよ。
```

短縮：

```text id="distill-crystallize"
_thread-index/ = Distill.
_thread-mission/ = Crystallize.
```

---

## §1. Three-File Map

`_thread-index/` は、README / Craft / Query の三重奏で運用する。

```yaml id="three-file-map"
thread_index_triad:
  README.md:
    path: "_thread-index/README.md"
    role:
      - "Entrance"
      - "Folder Map"
      - "Cross-Folder Bridge"
    meaning:
      - "_thread-index/ の入口"
      - "Raw Thread → Distilled Thread Source の流れを示す"
      - "_thread-mission/ への下流接続を示す"
      - "Future AIが旧Pathで迷わないようにする"

  thread-index_card-craft.md:
    path: "_thread-index/thread-index_card-craft.md"
    role:
      - "Engine"
      - "SSOT"
      - "Thread Distillation Craft Spine"
    meaning:
      - "Raw Threadを深く蒸留する仕様本体"
      - "Mission-ready Overfit Driftを防ぐ"
      - "Raw Lived Scene / User Pressure / AI Reality Responseを保持する"
      - "Distilled Thread Sourceを作る"

  thread-index_card-craft_query.md:
    path: "_thread-index/thread-index_card-craft_query.md"
    role:
      - "Ignition Key"
      - "Runtime Adapter"
      - "Next AI Empathy Pathing Boot Rail"
    meaning:
      - "Thread RuntimeでCraftを起動するためのQuery"
      - "Repo + Branch + Exact Path + Role を渡す"
      - "相対Path迷走を防ぐ"
      - "Plan Mode firstを安定発火させる"
```

短縮：

```text id="triad-short"
README = Entrance.
Craft = Engine.
Query = Ignition Key.
```

---

## §2. GitHub Absolute Coordinate Guard

新規AIは、このThreadの文脈を持っていない。  
相対Pathだけでは迷う可能性がある。

したがって、`_thread-index/` を読む時は、以下のGitHub正準座標を使う。

```yaml id="github-absolute-coordinate"
github_absolute_coordinate:
  repository_full_name: "yusukefujiijp/ai-project"
  branch: "main"

  upstream_folder:
    folder: "_thread-index/"
    readme: "_thread-index/README.md"
    engine: "_thread-index/thread-index_card-craft.md"
    query: "_thread-index/thread-index_card-craft_query.md"

  downstream_folder:
    folder: "_thread-mission/"
    readme: "_thread-mission/README.md"
    engine: "_thread-mission/thread-mission_card-craft.md"
    query: "_thread-mission/thread-mission_card-craft_query.md"
```

Guard：

```yaml id="absolute-coordinate-guard"
absolute_coordinate_guard:
  - "file名だけで読んだ扱いにしない"
  - "README.mdという名前だけで別fileを読んだ扱いにしない"
  - "thread-index_card-craft.mdという名前だけで旧fileを読んだ扱いにしない"
  - "thread-mission_card-craft.mdを _thread-index/ 内にある前提で読まない"
  - "相対Pathで迷った場合は repository_full_name + branch + exact_path へ戻る"
  - "GitHub上で到達・確認できない場合は、読んだふりをせずStopする"
```

---

## §3. Standard Read Order

`_thread-index/` でRaw Threadを蒸留する時は、原則として以下の順で読む。

```yaml id="read-order"
read_order:
  1_read_this_file:
    path: "_thread-index/README.md"
    role:
      - "Entrance"
      - "Folder Map"
      - "Cross-Folder Bridge"

  2_thread_index_card_craft:
    path: "_thread-index/thread-index_card-craft.md"
    document_identity: "thread_index_card_craft_protocol"
    role:
      - "Engine"
      - "SSOT"
      - "Thread Distillation Craft Spine"
    short:
      - "Missionへ流す前に、Threadそのものを深く蒸留せよ。"

  3_thread_index_card_craft_query:
    path: "_thread-index/thread-index_card-craft_query.md"
    role:
      - "Ignition Key"
      - "Runtime Adapter"
      - "Next AI Empathy Pathing Boot Rail"
    short:
      - "Repo + Branch + Exact Path + Roleで新規AIを迷わせず起動する。"

  4_target_raw_thread_or_source:
    path: "<TARGET_RAW_THREAD_OR_EXACT_SOURCE_PATH>"
    role:
      - "Target Source"
      - "Raw Thread / Thread Transcript / Thread Source"
```

下流Mission Card Craftへ進む時は、`_thread-mission/` のRead Orderへ移る。

```yaml id="downstream-read-order"
downstream_read_order:
  use_when:
    - "Distilled Thread SourceをMission Cardへ再結晶化する時"

  read:
    1: "_thread-mission/README.md"
    2: "_thread-mission/thread-mission_card-craft_query.md"
    3: "_thread-mission/thread-mission_card-craft.md"
    4: "<DISTILLED_THREAD_SOURCE_EXACT_PATH>"
```

---

## §4. Cross-Folder Pipeline

```yaml id="cross-folder-pipeline"
cross_folder_pipeline:
  1_raw_thread:
    role: "Raw Thread"
    meaning:
      - "まだ整形されていない生きたThread"
      - "現場感・圧・転換点・未処理Seedを含む"

  2_thread_index_folder:
    folder: "_thread-index/"
    query: "_thread-index/thread-index_card-craft_query.md"
    engine: "_thread-index/thread-index_card-craft.md"
    output: "Distilled Thread Source"
    meaning:
      - "Raw Threadを深く蒸留する"
      - "Mission-ready項目へ薄めすぎるDriftを防ぐ"
      - "Root Thread Distillation Fieldsを保持する"

  3_thread_mission_folder:
    folder: "_thread-mission/"
    readme: "_thread-mission/README.md"
    query: "_thread-mission/thread-mission_card-craft_query.md"
    engine: "_thread-mission/thread-mission_card-craft.md"
    output: "Thread-specific Mission Card"
    meaning:
      - "Distilled Thread Sourceを読む"
      - "Mission Seal / First Gate / Meta Layer / Living Reviewを保持する"
      - "1枚のMission Cardへ再結晶化する"
```

圧縮：

```text id="pipeline-short"
Raw Thread
↓
_thread-index/ で深く蒸留
↓
Distilled Thread Source
↓
_thread-mission/ でMission Cardへ再結晶化
```

---

## §5. Correct / Wrong

```yaml id="correct-wrong"
correct:
  - "先に _thread-index/thread-index_card-craft.md でThreadを深く蒸留する"
  - "次に _thread-mission/ の三重奏でMission Cardへ再結晶化する"
  - "READMEはEntrance / Folder Mapとして軽く保つ"
  - "CraftをEngine / SSOTとして扱う"
  - "QueryをIgnition Keyとして扱う"
  - "Meta Layer / Living Reviewを消さない"
  - "Mission Cardを単なる要約へ縮小しない"
  - "User Final SealなしにCommitしない"
  - "Repo + Branch + Exact Path + RoleでNext AIを迷わせない"

wrong:
  - "_thread-index/ を単なるIndex置き場として読む"
  - "_thread-index/ をMission Card本文置き場として読む"
  - "_thread-index/ がMission Card再結晶化まで担当すると読む"
  - "thread-mission_card-craft.md が _thread-index/ 内にある前提で読む"
  - "thread-index_card-craft.md が thread-mission_card-craft.md を置換すると読む"
  - "Source蒸留を省略してCard本文へ飛ぶ"
  - "Meta LayerをMission Cardの上書きとして読む"
  - "READMEを巨大Protocol本文にする"
  - "Queryを第二仕様書にする"
```

---

## §6. Update Policy

```yaml id="update-policy"
update_policy:
  readme:
    role: "Entrance / Folder Map / Cross-Folder Bridge"
    update_when:
      - "file roles change"
      - "read order changes"
      - "new canonical file is added"
      - "downstream folder changes"
      - "query file is added or revised"
    must_not_be:
      - "full protocol body"
      - "Registry"
      - "ADR"
      - "Mission Card"
      - "Query body"

  thread_index_card_craft:
    role: "Engine / SSOT / Thread Distillation Craft Spine"
    update_when:
      - "Thread Distillation fields change"
      - "Root Thread Distillation Guard changes"
      - "Cross-folder pipeline changes"

  thread_index_card_craft_query:
    role: "Ignition Key / Runtime Adapter / Next AI Empathy Pathing Boot Rail"
    update_when:
      - "Boot prompt changes"
      - "Read Order changes"
      - "GitHub Absolute Coordinate Guard changes"
      - "Plan Mode / Next Gate / Full Rail behavior changes"

  downstream_thread_mission:
    folder: "_thread-mission/"
    role: "Downstream Mission Card Crystallization Folder"
    update_when:
      - "Mission Card Craft workflow changes"
      - "Meta Layer / Living Review / User Final Seal guard changes"
      - "FullRail Tail guard changes"
```

---

## §7. Living Review

### §7.1 私の判断

`_thread-index/` は、Thread-to-Card全体を背負うfolderではなくなった。  
現在の正準役割は、Raw Threadを深く蒸留し、後続の `_thread-mission/` へ渡せるDistilled Thread Sourceを作ることである。

```text id="living-judgment"
Indexは深く蒸留する。
Missionは結晶化する。
READMEは入口を守る。
```

### §7.2 違和感

READMEが古いRead Orderを持ったままだと、Future AIは旧Pathへ戻る。  
特に `thread-mission_card-craft.md` を `_thread-index/` 内に探しに行くDriftが起きる。

```text id="discomfort"
入口が古い地図を配ると、Next AIは旧道へ進む。
```

### §7.3 Hidden Pattern

```text id="hidden-pattern"
Thread Index protects source depth.
Thread Mission protects mission crystallization.
README protects read order.
Query protects startup.
Root Guard protects worship order.
```

追加Hidden Pattern：

```text id="topology-hidden-pattern"
Engineが更新された後、Entranceも更新しなければならない。
```

### §7.4 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_readme_becomes_too_long:
    action: "Entrance / Folder Mapへ戻す"

  if_folder_is_read_as_mission_card_storage:
    action: "_thread-index/ = Distillへ戻す"

  if_mission_card_is_read_as_summary:
    action: "Mission Seal / First Gate / Meta Layerを再明記する"

  if_source_distillation_is_skipped:
    action: "thread-index_card-craft.mdを先に読む"

  if_old_thread_mission_path_returns:
    action: "_thread-mission/ の絶対座標へ戻す"

  if_query_is_read_as_ssot:
    action: "Craft is Engine / Query is Ignition Keyへ戻す"
```

---

## §8. Final Compression

```text id="final"
_thread-index/:

  README = Entrance.
  Craft = Engine.
  Query = Ignition Key.

  Purpose:
    Raw Threadを深く蒸留する。
    Distilled Thread Sourceへ整える。
    Mission-ready Overfit Driftを防ぐ。

  Do:
    Distill first.
    Preserve source depth.
    Use Repo + Branch + Exact Path + Role.
    Send Distilled Thread Source to _thread-mission/.

  Do not:
    Skip source depth.
    Reduce Mission Card to summary.
    Treat README as protocol body.
    Treat Query as SSOT.
    Search for thread-mission_card-craft.md inside _thread-index/.
    Commit without User Final Seal.

  Next:
    _thread-mission/
      README = Entrance.
      Craft = Engine.
      Query = Ignition Key.

  Root:
    主イェシュア・ハマシア.
```
