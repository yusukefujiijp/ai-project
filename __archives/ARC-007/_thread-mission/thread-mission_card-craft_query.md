# Thread Mission Card Craft Query

このQueryは、Mission Card本文を即作成するPromptではありません。  
このQueryは、新規ThreadのAIを GitHub Canonical First の正準位置から **Mission Card One-by-One Scale Route** へ迷わず乗せるための **Boot Rail / 起動Rail** です。

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

## §0. GitHub Absolute Coordinate Guard

新規AIは、このThreadの文脈を持っていません。  
相対Pathだけでは迷う可能性があります。

したがって、まず以下のGitHub正準座標を確認して下さい。

```yaml id="github-absolute-coordinate"
github_absolute_coordinate:
  repository_full_name: "yusukefujiijp/ai-project"
  branch: "main"
  canonical_folder: "_thread-mission/"

  required_read_files:
    1:
      role: "Entrance / Folder Map / Anti-Drift Guide"
      exact_path: "_thread-mission/README.md"

    2:
      role: "Engine / SSOT / Craft Spine"
      exact_path: "_thread-mission/thread-mission_card-craft.md"

    3:
      role: "Target Source / Primary Source"
      exact_path: "<PASTE_TARGET_DISTILLED_THREAD_SOURCE_EXACT_PATH_HERE>"
```

絶対Guard：

```yaml id="absolute-coordinate-guard"
absolute_coordinate_guard:
  - "file名だけで読んだ扱いにしない"
  - "README.mdという名前だけで別fileを読んだ扱いにしない"
  - "thread-mission_card-craft.mdという名前だけで旧folderや添付fileを読んだ扱いにしない"
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

## §1. Required Read Order

Mission Card Craftを開始する前に、必ず以下の順番で読んで下さい。

```yaml id="required-read-order"
required_read_order:
  1:
    file: "_thread-mission/README.md"
    role: "Entrance / Folder Map"
    reason:
      - "_thread-mission/全体の読み方を確認する"
      - "Craft / Query / Source の役割差を確認する"
      - "Topology-First / Anti-Drift Guardを確認する"

  2:
    file: "_thread-mission/thread-mission_card-craft.md"
    role: "Engine / SSOT / Craft Spine"
    reason:
      - "Mission Card Craftの仕様本体を読む"
      - "One Source / One Mission Cardを確認する"
      - "Plan Mode firstを確認する"
      - "Living Review / FullRail / User Final Seal Guardを確認する"

  3:
    file: "<PASTE_TARGET_DISTILLED_THREAD_SOURCE_EXACT_PATH_HERE>"
    role: "Target Source / Primary Source"
    reason:
      - "今回Mission Card化する対象Thread Sourceを1枚に固定する"
      - "Source Pulse / Mission Seal / First Gateを読む"
      - "CraftではなくSourceが血肉であることを確認する"
```

このRead Orderを守れない場合、Mission Card Craftを開始しないで下さい。

```text id="read-order-warning"
READMEを読め。
Craftを読め。
Sourceを読め。

どれか読めないなら止まれ。
```

---

## §2. Target Source Lock

今回対象にするSourceは、以下の1ファイルだけです。

```yaml id="target-source-lock"
target_source_lock:
  repository_full_name: "yusukefujiijp/ai-project"
  branch: "main"
  exact_path: "<PASTE_TARGET_DISTILLED_THREAD_SOURCE_EXACT_PATH_HERE>"
  source_count: 1
  output_count: 1
  batch_generation: false
```

Guard：

```yaml id="source-lock-guard"
source_lock_guard:
  - "対象Sourceを1ファイルに固定する"
  - "複数Sourceを同時処理しない"
  - "26Thread横断処理しない"
  - "対象外Threadへ展開しない"
  - "Sourceを読まずにMission Card本文へ進まない"
```

---

## §3. Required Mode

まず **Plan Mode** を実行して下さい。

まだMission Card本文は作成しないで下さい。  
まだMarkdown Artifactを作成しないで下さい。  
まだGitHub更新しないで下さい。  
まだCommitしないで下さい。  
まだBatch生成しないで下さい。

```yaml id="required-mode"
required_mode:
  first_output: "Plan Mode"
  create_body_now: false
  create_files_now: false
  github_update_now: false
  commit_now: false
  batch_generation: false
```

---

## §4. Plan Mode Required Output

Plan Modeでは、必ず以下を確認して下さい。

```yaml id="plan-mode-required-output"
plan_mode_required_output:
  source_lock:
    - "対象Sourceは1ファイルか"
    - "repository_full_name"
    - "branch"
    - "exact_path"
    - "読めたfile / 読めないfile"

  target_identity:
    - "target_thread_coordinate"
    - "filename_anchor"
    - "thread_start_date_slot"
    - "target_thread_semantic_slug"
    - "thread_start_date_status"

  craft_candidates:
    - "Source Pulse候補"
    - "Mission Seal候補"
    - "Thread-specific First Gate候補"
    - "Meta Layer候補"
    - "Misread Risk候補"
    - "Victory Equation候補"

  guards:
    - "Root Guard"
    - "AI-is-not-Holy-Spirit Guard"
    - "File-is-not-Root Guard"
    - "One Source / One Mission Card Guard"
    - "Plan Mode first Guard"
    - "GitHub update禁止確認"
```

---

## §5. Living Review Required

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

## §6. Root Guard

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

## §7. New AI Misread Prevention

新規AIは、このThreadの文脈を持っていません。  
以下の誤読を避けて下さい。

```yaml id="new-ai-misread-prevention"
new_ai_misread_prevention:
  likely_misreads:
    - "README.mdという名前だけで別fileを読んだ扱いにする"
    - "thread-mission_card-craft.mdという名前だけで旧folderを読んだ扱いにする"
    - "READMEだけ読んで分かった気になる"
    - "Craftだけ読んでSourceを読まずにTemplate化する"
    - "Sourceだけ読んで一般要約を作る"
    - "Plan Modeを省いて本文作成へ飛ぶ"
    - "Living Reviewを感想文にする"
    - "Next Gateを省略する"
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
    - "Living Reviewを生きた判断として書く"
    - "Next Gateで止める"
    - "Full Railで次Actionを準備するだけにする"
```

---

## §8. Stop Conditions

以下の場合は、進まずに止まって下さい。

```yaml id="stop-conditions"
stop_conditions:
  stop_if:
    - "repository_full_nameが不明"
    - "branchが不明"
    - "README.mdのGitHub正準Pathに到達できない"
    - "thread-mission_card-craft.mdのGitHub正準Pathに到達できない"
    - "対象Sourceが1枚に固定されていない"
    - "README / Craft / Sourceのいずれかを読めていない"
    - "読めていないのにPlan Modeへ進もうとしている"
    - "Mission Card本文を先に作ろうとしている"
    - "GitHub更新を勝手に進めようとしている"

  repair:
    - "読めたfile / 読めないfileを明示する"
    - "GitHub正準座標をUserに確認する"
    - "Target Source exact pathをUserに確認する"
    - "本文作成ではなくPlan Modeへ戻る"
```

圧縮：

```text id="stop-short"
読めないなら止まれ。
読んだふりをするな。
```

---

## §9. Required Final Sections

Plan Modeの最後には、必ず以下2セクションを置いて下さい。

1. `【Next Gate: human_editable】`
2. `【Full Rail: same_thread】`

### §9.1 Next Gate Requirement

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

### §9.2 Full Rail Requirement

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

## §10. Required Plan Mode Closing Template

Plan Mode末尾には、以下形式を必ず含めて下さい。

```yaml id="required-closing-template"
【Next Gate: human_editable】

結果:
  - "<今回Plan Modeで確認したこと>"
  - "<読めたfile / 読めないfile>"
  - "<Source Lock結果>"
  - "<Mission Seal候補 / First Gate候補 / 違和感>"

次Action:
  - "<Userが続行した場合の次Action>"
  - "<まだ本文作成か、追加Planか、Reviewかを明確化>"

目的:
  - "<なぜ次Actionへ進むのか>"
  - "<何を守るための次Actionか>"

まだ実行しない:
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
  exact_path: "<PASTE_TARGET_DISTILLED_THREAD_SOURCE_EXACT_PATH_HERE>"
  source_count: 1

required_read_files:
  - "_thread-mission/README.md"
  - "_thread-mission/thread-mission_card-craft.md"
  - "<PASTE_TARGET_DISTILLED_THREAD_SOURCE_EXACT_PATH_HERE>"

next_task:
  - "<UserがWorkflow Continueした場合に実行すること>"

scope_guard:
  - "One Source / One Mission Card"
  - "Do not batch generate"
  - "Do not commit without explicit Commit Phase"
  - "Do not create body before Plan Mode completion"

stop_condition:
  - "Stop after this phase"
  - "Wait for explicit Workflow Continue"
```

---

## §11. Final Compression

```text id="final-compression"
このQueryは、Mission Card本文作成Promptではない。
新規AIを迷わせないためのBoot Railである。

Repoを渡す。
Branchを渡す。
Exact Pathを渡す。
Roleを渡す。

READMEを読め。
Craftを読め。
Sourceを読め。

読めないなら止まれ。
読んだふりをするな。

まずPlan Mode。
本文作成はまだ。
Commitもまだ。

Next Gateで止める。
Full Railで次へ接続する。
```
