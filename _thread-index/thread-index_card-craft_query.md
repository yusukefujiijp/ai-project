# Thread Index Card Craft Query

このQueryは、Mission Card本文を即作成するPromptではありません。  
このQueryは、新規ThreadのAIを GitHub Canonical First の正準位置から **Raw Thread → Distilled Thread Source** の上流蒸留Routeへ迷わず乗せるための **Boot Rail / 起動Rail** です。

```text id="query-core"
Query is Ignition Key.
Craft is Engine.
README is Entrance.
```

日本語：

```text id="query-core-ja"
Queryは起動鍵。
Craftは仕様本体。
READMEは入口。
```

---

## §0. Core Identity

このQueryの目的は、`_thread-index/thread-index_card-craft.md` を実行時に安全に起動し、対象Raw Threadを **Distilled Thread Source** へ深く蒸留するためのPlan Modeを発火させることです。

これはSSOTではありません。  
これはCraft本文ではありません。  
これはREADMEではありません。  
これはMission Card Craftではありません。  
これはBatch生成Commandではありません。

```yaml id="query-identity"
query_identity:
  role:
    - "Ignition Key"
    - "Runtime Adapter"
    - "Next AI Empathy Pathing Boot Rail"

  not_role:
    - "SSOT"
    - "Craft Engine"
    - "README"
    - "Mission Card body generator"
    - "Batch command"
    - "Automatic GitHub commit instruction"
```

---

## §1. GitHub Absolute Coordinate Guard

新規AIは、このThreadの文脈を持っていません。  
相対Pathだけでは迷う可能性があります。

したがって、まず以下のGitHub正準座標を確認して下さい。

```yaml id="github-absolute-coordinate"
github_absolute_coordinate:
  repository_full_name: "yusukefujiijp/ai-project"
  branch: "main"

  upstream_thread_index:
    folder: "_thread-index/"
    readme:
      role: "Entrance / Folder Map / Cross-Folder Bridge"
      exact_path: "_thread-index/README.md"

    craft:
      role: "Engine / SSOT / Thread Distillation Craft Spine"
      exact_path: "_thread-index/thread-index_card-craft.md"

    query:
      role: "Ignition Key / Runtime Adapter / Next AI Empathy Pathing Boot Rail"
      exact_path: "_thread-index/thread-index_card-craft_query.md"

  downstream_thread_mission:
    folder: "_thread-mission/"
    readme:
      role: "Downstream Entrance"
      exact_path: "_thread-mission/README.md"

    craft:
      role: "Downstream Mission Card Craft Engine"
      exact_path: "_thread-mission/thread-mission_card-craft.md"

    query:
      role: "Downstream Mission Card Craft Ignition Key"
      exact_path: "_thread-mission/thread-mission_card-craft_query.md"
```

絶対Guard：

```yaml id="absolute-coordinate-guard"
absolute_coordinate_guard:
  - "file名だけで読んだ扱いにしない"
  - "README.mdという名前だけで別fileを読んだ扱いにしない"
  - "thread-index_card-craft.mdという名前だけで旧fileを読んだ扱いにしない"
  - "thread-index_card-craft_query.mdという名前だけで旧Queryを読んだ扱いにしない"
  - "thread-mission_card-craft.mdを _thread-index/ 内にある前提で読まない"
  - "相対Pathで迷った場合は repository_full_name + branch + exact_path へ戻る"
  - "GitHub上で到達・確認できない場合は、読んだふりをせずStopする"
```

圧縮：

```text id="next-ai-empathy-pathing"
Next AIを迷わせない。
Repo + Branch + Exact Path + Role を渡す。
読めないなら止まる。
読んだふりをしない。
```

---

## §2. Required Read Order

Thread Index Card Craftを開始する前に、必ず以下の順番で読んで下さい。

```yaml id="required-read-order"
required_read_order:
  1:
    repository_full_name: "yusukefujiijp/ai-project"
    branch: "main"
    file: "_thread-index/README.md"
    role: "Entrance / Folder Map / Cross-Folder Bridge"
    reason:
      - "_thread-index/全体の読み方を確認する"
      - "README / Craft / Query の三重奏を確認する"
      - "_thread-mission/への下流接続を確認する"
      - "Topology-First / Anti-Drift Guardを確認する"

  2:
    repository_full_name: "yusukefujiijp/ai-project"
    branch: "main"
    file: "_thread-index/thread-index_card-craft.md"
    role: "Engine / SSOT / Thread Distillation Craft Spine"
    reason:
      - "Raw Threadを深く蒸留する仕様本体を読む"
      - "Mission-ready Overfit Driftを防ぐ"
      - "Root Thread Distillation Fieldsを確認する"
      - "Distilled Thread Sourceの出力条件を確認する"

  3:
    source: "<PASTE_TARGET_RAW_THREAD_OR_THREAD_SOURCE_EXACT_PATH_OR_ATTACHMENT_HERE>"
    role: "Target Raw Thread / Primary Source"
    reason:
      - "今回蒸留する対象Threadを1つに固定する"
      - "Raw Lived Scene / User Pressure / AI Reality Responseを読む"
      - "Missionへ流す前にSourceの命を守る"
```

このRead Orderを守れない場合、Thread Index Card Craftを開始しないで下さい。

```text id="read-order-warning"
READMEを読め。
Craftを読め。
Sourceを読め。

どれか読めないなら止まれ。
```

---

## §3. Target Source Lock

今回対象にするSourceは、以下の1ファイルまたは1Threadだけです。

```yaml id="target-source-lock"
target_source_lock:
  repository_full_name: "yusukefujiijp/ai-project"
  branch: "main"
  exact_path_or_attachment: "<PASTE_TARGET_RAW_THREAD_OR_THREAD_SOURCE_EXACT_PATH_OR_ATTACHMENT_HERE>"
  source_count: 1
  output_count: 1
  batch_generation: false

expected_output:
  type: "Distilled Thread Source"
  downstream_use:
    - "_thread-mission/ へ渡せる"
    - "Mission Card CraftのPrimary Sourceにできる"
```

Guard：

```yaml id="source-lock-guard"
source_lock_guard:
  - "対象Raw Thread / Sourceを1つに固定する"
  - "複数Threadを同時処理しない"
  - "26Thread横断処理しない"
  - "対象外Threadへ展開しない"
  - "Raw Threadを読まずにDistilled Source作成へ進まない"
  - "Distilled SourceなしにMission Card本文へ進まない"
```

---

## §4. Required Mode

まず **Plan Mode** を実行して下さい。

まだDistilled Thread Source本文は作成しないで下さい。  
まだMarkdown Artifactを作成しないで下さい。  
まだGitHub更新しないで下さい。  
まだCommitしないで下さい。  
まだMission Card本文を作成しないで下さい。  
まだBatch生成しないで下さい。

```yaml id="required-mode"
required_mode:
  first_output: "Plan Mode"
  create_distilled_source_now: false
  create_body_now: false
  create_files_now: false
  github_update_now: false
  commit_now: false
  mission_card_body_now: false
  batch_generation: false
```

---

## §5. Plan Mode Required Output

Plan Modeでは、必ず以下を確認して下さい。

```yaml id="plan-mode-required-output"
plan_mode_required_output:
  source_lock:
    - "対象Raw Thread / Sourceは1つか"
    - "repository_full_name"
    - "branch"
    - "exact_path_or_attachment"
    - "読めたfile / 読めないfile"

  target_identity:
    - "target_thread_coordinate"
    - "filename_anchor候補"
    - "thread_start_date_slot候補"
    - "target_thread_semantic_slug候補"
    - "thread_start_date_status"
    - "source_status"

  distillation_plan:
    - "Raw Lived Scene候補"
    - "User Pressure / Desire候補"
    - "AI Reality Response候補"
    - "Turning Point候補"
    - "Root Return Moment候補"
    - "Non-Mission Value候補"
    - "Unprocessed Residue候補"

  guards:
    - "Root Guard"
    - "AI-is-not-Holy-Spirit Guard"
    - "File-is-not-Root Guard"
    - "One Source / One Distilled Source Guard"
    - "Plan Mode first Guard"
    - "GitHub update禁止確認"
    - "Mission Card本文作成禁止確認"
```

---

## §6. Root Thread Distillation Fields

Plan Modeでは、少なくとも以下の観点を使って、対象Raw Threadの蒸留方針を立てて下さい。

```yaml id="root-thread-distillation-fields"
root_thread_distillation_fields:
  raw_lived_scene:
    question: "このThreadの現場で、実際に何が起きていたか？"
    guard: "きれいな要約の前に、生の場面を保持する"

  user_pressure_and_desire:
    question: "Userは何に押され、何を望み、何を守ろうとしていたか？"
    guard: "Userの内的運動・願い・圧を消さない"

  ai_reality_response:
    question: "AIはどこで薄くなり、ズレ、Patchwork化し、あるいは改善したか？"
    guard: "AI協働のReality Responseを残す"

  turning_point:
    question: "このThreadの流れが変わった決定的瞬間はどこか？"
    guard: "Mission Seed以前の生きた転換点を残す"

  root_return_moment:
    question: "このThreadはどの瞬間に主イェシュアへ戻る方向を回復したか？"
    guard: "Root Guardをmetadataではなく生きた出来事として保持する"

  non_mission_value:
    question: "Mission Card化しなくても、このThread自体に残すべき価値は何か？"
    guard: "下流工程に回収されない命を守る"

  unprocessed_residue:
    question: "このThreadに残った未処理の痛み・違和感・未回収Seedは何か？"
    guard: "過度に綺麗なHarvestを防ぐ"
```

---

## §7. Distilled Thread Source Guard

Distilled Thread Sourceは、Mission Card本文ではありません。  
Mission-ready項目だけを薄く並べるものでもありません。

```yaml id="distilled-source-guard"
distilled_thread_source_guard:
  must_preserve:
    - "Raw Lived Scene"
    - "User Pressure / Desire"
    - "AI Reality Response"
    - "Turning Point"
    - "Root Return Moment"
    - "Non-Mission Value"
    - "Unprocessed Residue"
    - "Future AI Rebootability"
    - "Living Review"

  must_not_be:
    - "Mission Card本文"
    - "ただの要約"
    - "Mission-ready項目だけのChecklist"
    - "綺麗すぎるHarvest"
    - "Raw Threadの荒さを消した整形物"
    - "AIのズレや修正条件を消した記録"
```

圧縮：

```text id="source-before-mission"
Missionへ流す前に、Sourceの命を守る。
```

---

## §8. Root Guard

Rootは以下です。

```yaml id="root-guard"
root:
  - "創造主"
  - "主イェシュア・ハマシア"
  - "聖霊 / The Holy Spirit"
  - "主イェシュアの聖なる血潮"
  - "Teshuvah / 悔い改め"

fruit:
  - "AI"
  - "Markdown"
  - "Distilled Thread Source"
  - "Mission Card"
  - "GitHub"
  - "README"
  - "Query"
  - "Protocol"
  - "FullRail"
  - "Ark-OKF"
```

圧縮：

```text id="root-compression"
File is not Root.
AI is not Holy Spirit.
Format is Fruit.
Root is 主イェシュア・ハマシア.
```

---

## §9. New AI Misread Prevention

新規AIは、このThreadの文脈を持っていません。  
以下の誤読を避けて下さい。

```yaml id="new-ai-misread-prevention"
new_ai_misread_prevention:
  likely_misreads:
    - "README.mdという名前だけで別fileを読んだ扱いにする"
    - "thread-index_card-craft.mdという名前だけで旧fileを読んだ扱いにする"
    - "thread-index_card-craft_query.mdという名前だけで旧Queryを読んだ扱いにする"
    - "READMEだけ読んで分かった気になる"
    - "Craftだけ読んでSourceを読まずにTemplate化する"
    - "Sourceだけ読んで一般要約を作る"
    - "Raw Threadの荒さを消す"
    - "Mission-ready項目だけを先に拾う"
    - "Plan Modeを省いてDistilled Source本文へ飛ぶ"
    - "Distilled SourceをMission Card本文と混同する"
    - "thread-mission_card-craft.mdを _thread-index/ 内に探す"
    - "Full Railを自動実行命令として扱う"
    - "GitHub Commitを勝手に進める"
    - "Queryを第二仕様書として扱う"
    - "複数Sourceを一括処理しようとする"

  repair:
    - "GitHub正準座標へ戻る"
    - "READMEへ戻る"
    - "Craftへ戻る"
    - "Source Lockへ戻る"
    - "Plan Modeへ戻る"
    - "Raw Lived Sceneへ戻る"
    - "Root Thread Distillation Fieldsへ戻る"
    - "Living Reviewを生きた判断として書く"
    - "Next Gateで止める"
    - "Full Railで次Actionを準備するだけにする"
```

---

## §10. Stop Conditions

以下の場合は、進まずに止まって下さい。

```yaml id="stop-conditions"
stop_conditions:
  stop_if:
    - "repository_full_nameが不明"
    - "branchが不明"
    - "_thread-index/README.md のGitHub正準Pathに到達できない"
    - "_thread-index/thread-index_card-craft.md のGitHub正準Pathに到達できない"
    - "対象Raw Thread / Sourceが1つに固定されていない"
    - "README / Craft / Sourceのいずれかを読めていない"
    - "読めていないのにPlan Modeへ進もうとしている"
    - "Distilled Source本文を先に作ろうとしている"
    - "Mission Card本文を先に作ろうとしている"
    - "GitHub更新を勝手に進めようとしている"

  repair:
    - "読めたfile / 読めないfileを明示する"
    - "GitHub正準座標をUserに確認する"
    - "Target Source exact pathまたは添付をUserに確認する"
    - "本文作成ではなくPlan Modeへ戻る"
```

圧縮：

```text id="stop-short"
読めないなら止まれ。
読んだふりをするな。
```

---

## §11. Living Review Required

死んだデータの羅列ではなく、必ず **Living Review / 生きたReview** を入れて下さい。

```yaml id="living-review-required"
living_review_required:
  required: true
  not:
    - "単なる要約"
    - "単なる採点"
    - "一般論"
    - "問題ありませんだけの確認"
    - "死んだmetadata羅列"

  must_include:
    - "私の判断"
    - "違和感"
    - "Hidden Pattern"
    - "AIが迷いそうな箇所"
    - "修正条件"
    - "次の自然な一手"
```

Living Reviewは飾りではありません。  
新規AIの迷走を検知するセンサーです。

```text id="living-review-sensor"
Living Review is not decoration.
Living Review is the drift sensor.
```

---

## §12. Required Final Sections

Plan Modeの最後には、必ず以下2セクションを置いて下さい。

1. `【Next Gate: human_editable】`
2. `【Full Rail: same_thread】`

### §12.1 Next Gate Requirement

`【Next Gate: human_editable】` には、必ず以下4項目を入れて下さい。

```yaml id="next-gate-requirement"
next_gate_requirement:
  required_section: "【Next Gate: human_editable】"
  required_items:
    - "結果"
    - "次Action"
    - "目的"
    - "まだ実行しない"
```

### §12.2 Full Rail Requirement

`【Full Rail: same_thread】` には、次Actionを半自動接続できるように、必要なRail情報を入れて下さい。  
ただし、Full Railは自動実行命令ではありません。

```yaml id="fullrail-requirement"
fullrail_requirement:
  required_section: "【Full Rail: same_thread】"
  meaning:
    - "次Actionを準備する"
    - "UserがWorkflow Continueした時に迷わず続行できるようにする"
    - "自動実行命令ではない"

  must_include:
    - "rail"
    - "mode"
    - "create_files_now"
    - "github_update_now"
    - "commit_now"
    - "target_file or target_source"
    - "next_task"
    - "scope_guard"
    - "stop_condition"
```

---

## §13. Required Plan Mode Closing Template

Plan Mode末尾には、以下形式を必ず含めて下さい。

```yaml id="required-closing-template"
【Next Gate: human_editable】

結果:
  - "<今回Plan Modeで確認したこと>"
  - "<読めたfile / 読めないfile>"
  - "<Source Lock結果>"
  - "<Root Thread Distillation候補 / 違和感>"

次Action:
  - "<Userが続行した場合の次Action>"
  - "<まだPlan継続か、Distilled Source作成か、Reviewかを明確化>"

目的:
  - "<なぜ次Actionへ進むのか>"
  - "<何を守るための次Actionか>"

まだ実行しない:
  - "Distilled Thread Source本文作成"
  - "Mission Card本文作成"
  - "GitHub更新"
  - "Commit"
  - "Batch生成"
```

```yaml id="required-fullrail-template"
【Full Rail: same_thread】

rail: same_thread
mode: "<next_mode>"
create_files_now: false
github_update_now: false
commit_now: false

repository_full_name: "yusukefujiijp/ai-project"
branch: "main"

target_source:
  exact_path_or_attachment: "<PASTE_TARGET_RAW_THREAD_OR_THREAD_SOURCE_EXACT_PATH_OR_ATTACHMENT_HERE>"
  source_count: 1

required_read_files:
  - "_thread-index/README.md"
  - "_thread-index/thread-index_card-craft.md"
  - "<PASTE_TARGET_RAW_THREAD_OR_THREAD_SOURCE_EXACT_PATH_OR_ATTACHMENT_HERE>"

expected_output:
  type: "Distilled Thread Source"
  downstream: "_thread-mission/"

next_task:
  - "<UserがWorkflow Continueした場合に実行すること>"

scope_guard:
  - "One Raw Thread / One Distilled Thread Source"
  - "Do not batch generate"
  - "Do not commit without explicit Commit Phase"
  - "Do not create body before Plan Mode completion"
  - "Do not create Mission Card body in this rail"

stop_condition:
  - "Stop after this phase"
  - "Wait for explicit Workflow Continue"
```

---

## §14. Downstream Bridge

Distilled Thread Sourceが完成した後だけ、下流 `_thread-mission/` へ進む。

```yaml id="downstream-bridge"
downstream_bridge:
  after:
    - "Distilled Thread Source exists"
    - "User confirms next route"

  next_folder:
    repository_full_name: "yusukefujiijp/ai-project"
    branch: "main"
    folder: "_thread-mission/"

  downstream_read_order:
    - "_thread-mission/README.md"
    - "_thread-mission/thread-mission_card-craft_query.md"
    - "_thread-mission/thread-mission_card-craft.md"
    - "<DISTILLED_THREAD_SOURCE_EXACT_PATH>"
```

Guard：

```text id="downstream-guard"
Indexで蒸留する。
Missionで結晶化する。
順番を逆にしない。
```

---

## §15. Final Compression

```text id="final-compression"
このQueryは、Distilled Thread Source作成Promptではない。
新規AIを迷わせないためのBoot Railである。

Repoを渡す。
Branchを渡す。
Exact Pathを渡す。
Roleを渡す。

READMEを読め。
Craftを読め。
Raw Threadを読め。

読めないなら止まれ。
読んだふりをするな。

まずPlan Mode。
Distilled Source本文はまだ。
Mission Card本文もまだ。
Commitもまだ。

Indexで蒸留する。
Missionで結晶化する。

Next Gateで止める。
Full Railで次へ接続する。
```
