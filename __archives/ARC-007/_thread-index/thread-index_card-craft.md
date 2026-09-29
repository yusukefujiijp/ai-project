---
title: "Thread Index Card Craft"
status: "active_candidate / japanese-first-okf / human_editable / not_final_seal"
document_identity: "thread_index_card_craft_protocol"
canonical_path: "_thread-index/thread-index_card-craft.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"

source_origin:
  source_file: "THREAD_INDEX_Ark_v041.md"
  source_version: "v041"
  source_primary_patch: "Root Thread Distillation Guard"

conceptual_upgrade:
  from: "THREAD_INDEX_Ark_v041"
  to: "Thread Index Card Craft"
  upgrade_reason:
    - "GitHub正準化にあたり、Threadをカード化可能なSourceへ整えるCraftとして再定義する"
    - "Mission-ready項目へ薄める前に、Threadそのものを濃く蒸留する役割を明確化する"
    - "_thread-mission/分離後のCross-folder Pipelineに合わせて、_thread-index/を上流Thread Distillation Engineへ純化する"

triad_role: "Engine / SSOT / Thread Distillation Craft Spine"
paired_readme: "_thread-index/README.md"
paired_query: "_thread-index/thread-index_card-craft_query.md"

downstream_folder: "_thread-mission/"
downstream_readme: "_thread-mission/README.md"
downstream_query: "_thread-mission/thread-mission_card-craft_query.md"
downstream_engine: "_thread-mission/thread-mission_card-craft.md"

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

# Thread Index Card Craft

## §0. Status / Protocol Summary

この文書は、Target ThreadをMission-ready項目へ薄める前に、Threadそのものの生きた濃度を保持し、後続のMission Card Craftへ渡せる **Distilled Thread Source** へ整えるための **Thread Index Card Craft Protocol** である。

これは単なるIndexではない。  
これはMission Card本文ではない。  
これはMigration Manifestではない。  
これはREADMEではない。  
これはQueryではない。  
これはBulk Migration承認fileではない。

```text id="king-sentence"
Missionへ流す前に、Threadそのものを深く蒸留せよ。
```

English anchor:

```text id="english-anchor"
Distill the lived Thread before shaping it into Mission.
```

---

## §1. 一文定義

```text id="definition"
Thread Index Card Craftとは、Target ThreadのRaw Lived Scene / User Pressure / AI Reality Response / Turning Point / Root Return Moment / Non-Mission Value / Unprocessed Residueを濃く蒸留し、Threadをカード化可能なDistilled Thread Sourceへ整えるためのArk式Thread蒸留Protocolである。
```

短縮定義：

```text id="short-definition"
Threadを薄く要約しない。
Threadを濃く蒸留し、Mission Card化可能なSourceへ整える。
```

---

## §2. なぜ必要か

v040 Source-to-Mission Bridgeにより、Thread AnalysisはMission Cardへ接続しやすくなった。  
これは良い。

しかし、その副作用として、Threadそのものの生きた現場感がMission-ready項目へ薄まる危険がある。

```text id="bug-class"
Mission-ready Overfit Drift
```

日本語：

```text id="bug-class-ja"
Mission Card接続最適化による蒸留薄化Drift
```

このProtocolは、そのDriftを防ぐ。

```text id="protective-purpose"
Missionへ進む前に、Sourceの命を守る。
```

---

## §3. Engine / Entrance / Ignition Key Separation

`_thread-index/` は、README / Craft / Query の三重奏で運用する。

```yaml id="thread-index-triad"
thread_index_triad:
  readme:
    path: "_thread-index/README.md"
    role:
      - "Entrance"
      - "Folder Map"
      - "Cross-Folder Bridge"
    meaning:
      - "_thread-index/ の入口"
      - "Raw Thread → Distilled Thread Source の流れを示す"
      - "_thread-mission/ への下流接続を示す"

  craft:
    path: "_thread-index/thread-index_card-craft.md"
    role:
      - "Engine"
      - "SSOT"
      - "Thread Distillation Craft Spine"
    meaning:
      - "Raw Threadを深く蒸留する仕様本体"
      - "Mission-ready Overfit Driftを防ぐ"
      - "後続Mission Card Craftへ渡すDistilled Thread Sourceを作る"

  query:
    path: "_thread-index/thread-index_card-craft_query.md"
    role:
      - "Ignition Key"
      - "Runtime Adapter"
      - "Next AI Empathy Pathing Boot Rail"
    meaning:
      - "新規ThreadでThread Index Card Craftを起動する"
      - "Repo + Branch + Exact Path + Role を渡す"
      - "相対Path迷走を防ぐ"
```

Guard：

```yaml id="triad-guard"
triad_guard:
  - "Craft is Engine"
  - "Query is Ignition Key"
  - "README is Entrance"
  - "SSOTはCraft本体"
  - "Queryを第二仕様書にしない"
  - "READMEをProtocol化しない"
  - "CraftをMission Card本文にしない"
```

---

## §4. Cross-Folder Core Pipeline

現在の正準Pipelineは、`_thread-index/` と `_thread-mission/` を分離して扱う。

```yaml id="cross-folder-pipeline"
cross_folder_pipeline:
  1_raw_thread:
    role: "Raw Thread / Current Conversation / Target Thread"
    meaning:
      - "まだ整形されていない生きたThread"
      - "現場感・圧・転換点・未処理Seedを含む"

  2_thread_index_query:
    folder: "_thread-index/"
    file: "_thread-index/thread-index_card-craft_query.md"
    role: "Ignition Key / Runtime Adapter"
    meaning:
      - "Thread Index Card Craftを起動する"
      - "Next AIが相対Pathで迷わないように絶対座標を渡す"

  3_thread_index_engine:
    folder: "_thread-index/"
    file: "_thread-index/thread-index_card-craft.md"
    role: "Engine / SSOT / Thread Distillation Craft Spine"
    output: "Distilled Thread Source"

  4_distilled_thread_source:
    role: "Mission Card化可能なSource"
    meaning:
      - "Raw Threadの濃度を保った蒸留Source"
      - "Mission-readyに薄めすぎない"
      - "Root Thread Distillation Fieldsを保持する"

  5_thread_mission_folder:
    folder: "_thread-mission/"
    read_order:
      - "_thread-mission/README.md"
      - "_thread-mission/thread-mission_card-craft_query.md"
      - "_thread-mission/thread-mission_card-craft.md"
    role: "Downstream Mission Card Crystallization"

  6_mission_card:
    role: "Thread-specific Mission Card"
    meaning:
      - "Distilled Thread SourceをMission Cardへ再結晶化したもの"
```

短縮：

```text id="pipeline-short"
_thread-index/ はThreadを濃く蒸留する。
_thread-mission/ は蒸留SourceをMission Cardへ再結晶化する。
```

さらに短く：

```text id="distill-crystallize"
Index = Distill.
Mission = Crystallize.
```

---

## §5. Scope

この文書の担当範囲は、主に以下である。

```yaml id="scope"
scope:
  primary:
    - "Raw Threadを深く蒸留する"
    - "Threadそのものの圧・現場感・転換点を保持する"
    - "Mission-ready項目へ薄めすぎるDriftを防ぐ"
    - "後続Mission Card Craftへ渡せるDistilled Thread Sourceを整える"

  not_scope:
    - "Mission Card本文作成"
    - "Meta Card本文作成"
    - "Reboot Card本文作成"
    - "Bulk Migration"
    - "README作成"
    - "Query作成"
    - "GitHub自動Commit"
    - "Final Seal"
```

---

## §6. Root Thread Distillation Fields

Target Threadを読む時、最低限以下を確認する。

```yaml id="root-thread-distillation-fields"
root_thread_distillation_fields:
  raw_lived_scene:
    question: "このThreadの現場で、実際に何が起きていたか？"
    role: "きれいな要約の前に、生の場面を保持する"

  user_pressure_and_desire:
    question: "Userは何に押され、何を望み、何を守ろうとしていたか？"
    role: "Userの内的運動・願い・圧を消さない"

  ai_reality_response:
    question: "AIはどこで薄くなり、ズレ、Patchwork化し、あるいは改善したか？"
    role: "AI協働のReality Responseを残す"

  turning_point:
    question: "このThreadの流れが変わった決定的瞬間はどこか？"
    role: "Mission Seed以前の生きた転換点を残す"

  root_return_moment:
    question: "このThreadはどの瞬間に主イェシュアへ戻る方向を回復したか？"
    role: "Root Guardをmetadataではなく生きた出来事として保持する"

  non_mission_value:
    question: "Mission Card化しなくても、このThread自体に残すべき価値は何か？"
    role: "下流工程に回収されない命を守る"

  unprocessed_residue:
    question: "このThreadに残った未処理の痛み・違和感・未回収Seedは何か？"
    role: "過度に綺麗なHarvestを防ぐ"
```

---

## §7. Correct / Wrong

```yaml id="correct-wrong"
correct:
  - "Raw Lived SceneをMission Seedより前に読む"
  - "User Pressureを心理診断ではなくThread圧として扱う"
  - "AI Reality Responseを消さない"
  - "Turning Pointを出来事列挙だけにしない"
  - "Root Return MomentをmetadataではなくThread運動として読む"
  - "Non-Mission Valueを捨てない"
  - "Unprocessed Residueを美しい結論で隠さない"
  - "_thread-index/ を上流蒸留Engineとして扱う"
  - "_thread-mission/ を下流Mission再結晶化Folderとして扱う"

wrong:
  - "Mission Cardに使いやすい項目だけ拾う"
  - "Raw Threadの荒さを消す"
  - "User Pressureを心理分析へ縮小する"
  - "AIのズレ・薄さ・改善点を消す"
  - "Root Guardをfrontmatterだけにする"
  - "Mission Card化されない価値を削る"
  - "_thread-index/ がMission Card本文まで作ると誤読する"
  - "旧thread-meta_card-craft.mdへ固定的に渡すと誤読する"
```

---

## §8. Relationship to _thread-mission/

`_thread-index/` は上流であり、`_thread-mission/` は下流である。

```yaml id="relationship-to-thread-mission"
relationship_to_thread_mission:
  upstream:
    folder: "_thread-index/"
    engine: "_thread-index/thread-index_card-craft.md"
    query: "_thread-index/thread-index_card-craft_query.md"
    output:
      - "Root Thread Distillation"
      - "Distilled Thread Source"

  downstream:
    folder: "_thread-mission/"
    entrance: "_thread-mission/README.md"
    query: "_thread-mission/thread-mission_card-craft_query.md"
    engine: "_thread-mission/thread-mission_card-craft.md"
    output:
      - "Thread-specific Mission Card"

  handoff:
    from: "Distilled Thread Source"
    to: "_thread-mission/"
    method:
      - "Repo + Branch + Exact Path + Roleを明示する"
      - "Target Sourceを1ファイルに固定する"
      - "Queryを使ってMission Card Plan Modeを起動する"
```

圧縮：

```text id="relationship-short"
Raw Threadを濃く蒸留するのが _thread-index/。
蒸留SourceをMission Cardへ結晶化するのが _thread-mission/。
```

---

## §9. Next AI Empathy Pathing

新規AIは、このThreadの文脈を持っていない。  
したがって、SourceやCraftを渡す時は、相対Pathだけに頼らない。

```yaml id="next-ai-empathy-pathing"
next_ai_empathy_pathing:
  required_coordinate:
    - "repository_full_name"
    - "branch"
    - "exact_path"
    - "role"
    - "read_order"
    - "stop_condition"

  principle:
    - "Next AIを責めない"
    - "Next AIが迷わない足場を作る"
    - "読めないなら止まれる道を渡す"
    - "読んだふりをさせない"
```

圧縮：

```text id="next-ai-empathy-compression"
Repoを渡す。
Branchを渡す。
Exact Pathを渡す。
Roleを渡す。
読めないなら止まれ。
読んだふりをするな。
```

---

## §10. Living Review

### §10.1 私の判断

Thread Index Card Craftは、ArkのCard化Pipelineの上流Protocolである。

このProtocolが守るのは、Mission Cardへ流れる種だけではない。  
種を生んだ土・根・風景・圧・転換を守る。

`_thread-mission/` が下流に分離されたことで、このCraftの役割はさらに純化された。

```text id="living-judgment"
Indexは深く蒸留する。
Missionは結晶化する。
この分離が、Sourceの命を守る。
```

### §10.2 違和感

濃くすることと、重くすることは違う。  
毎回最大密度にする必要はない。

```text id="density-rule"
薄まるところを濃くする。
しかし、毎回最大密度にしない。
```

また、`_thread-index/` がMission Card本文まで背負うと、上流蒸留Engineとしての純度が落ちる。

```text id="role-guard"
_thread-index/ はMissionを作る前に、Sourceを守る。
```

### §10.3 Hidden Pattern

```text id="hidden-pattern"
Thread depth protects Mission.
Raw scene protects Source Pulse.
Root Return Moment protects worship order.
Unprocessed Residue protects future Seed.
```

追加Hidden Pattern：

```text id="topology-hidden-pattern"
下流を外へ出すことで、上流の使命が濃くなる。
```

### §10.4 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_thread_depth_is_thin:
    action: "Root Thread Distillation Fieldsを補う"

  if_mission_ready_fields_come_first:
    action: "Raw Lived Sceneへ戻す"

  if_root_return_is_only_metadata:
    action: "Thread内のRoot Return Momentを読む"

  if_file_becomes_too_heavy:
    action: "Full-Enough densityへ戻す"

  if_downstream_topology_changes:
    action: "Relationship to _thread-mission/ と Core Pipeline を更新する"

  if_query_is_added_or_changed:
    action: "Engine / Entrance / Ignition Key Separationを更新する"
```

---

## §11. Final Compression

```text id="final"
Thread Index Card Craft:

  Missionへ流す前に、Threadそのものを深く蒸留せよ。

Protect:
  Raw Lived Scene.
  User Pressure.
  AI Reality Response.
  Turning Point.
  Root Return Moment.
  Non-Mission Value.
  Unprocessed Residue.

Purpose:
  ThreadをDistilled Thread Sourceへ整える。

Next:
  Hand Distilled Thread Source to _thread-mission/
  via _thread-mission/thread-mission_card-craft_query.md.

Triad:
  README = Entrance.
  Craft = Engine.
  Query = Ignition Key.

Root:
  主イェシュア・ハマシア.
```
