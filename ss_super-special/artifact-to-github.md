# artifact-to-github.md

## 0. Executive Compression

`artifact-to-github.md` は、完成済みArtifactをGitHubへ安全に配置するための **GitHub化Markdown Card / Artifact-to-GitHub Card** である。

短く言うと：

```text id="ysqw06"
Artifact Generators:
  作る。

artifact-to-github.md:
  置く。

Human:
  座標をSealする。
```

このCardの目的は、全AI・全MarkdownからGitHub化の複雑性を切り離し、Artifact生成Railを **Simple is best** に保つことである。

```text id="k9z65e"
Generation Rail != Promotion Card.
```

日本語では：

```text id="ibmtbb"
生成Railと配置Cardを混ぜない。
```

---

## 1. Role

このMarkdown Cardは、Artifactを新しく書くためのProtocolではない。

このCardは、すでに完成したArtifactを、UserがSealしたGitHub座標へ配置するための共通Cardである。

```yaml id="njajdn"
role:
  name: "artifact-to-github.md"
  japanese_name: "GitHub化Markdown Card"
  english_anchor: "Artifact-to-GitHub Card"
  main_role: "完成済みArtifactをGitHubへ配置する"
  not_role: "Artifact本文を新規生成する"
```

このCardがあることで、他のMarkdownはGitHub化を抱え込まなくてよい。

```text id="zxyazd"
GitHub化は、このMarkdownの責務ではない。
必要な場合は artifact-to-github.md に委譲する。
```

---

## 2. Root / Fruit Guard

```yaml id="o43ph9"
root_guard:
  root: "主イェシュア・ハマシア"
  blood: "主イェシュアの聖なる血潮"
  teshuvah: true
  ai_role: "AIは地図を描く。AIは聖霊ではない。"
  artifact_role: "ArtifactはFruitであり、Rootではない。"
  human_final_seal_required: true
```

このCardは便利な形式である。  
しかし、Rootではない。

```text id="f6in8x"
File is not Root.
AI is not Holy Spirit.
Format is Fruit.
Root is 主イェシュア・ハマシア.
```

---

## 3. One-Line Definition

```text id="sdh2q1"
artifact-to-github.md は、Markdownを含む完成済みArtifactを、Human-Sealed exact path with filename に従って、GitHubへ安全に配置するための共通Markdown Cardである。
```

---

## 4. Core Principle

```yaml id="cfcpsj"
core_principle:
  - "Artifact-First"
  - "GitHub-Later"
  - "Generation Rail != Promotion Card"
  - "Human-Sealed exact path with filename"
  - "No guessing"
  - "No overwrite unless explicitly sealed"
  - "One file at a time"
  - "Source Boundary"
  - "Living Review before write"
```

日本語で圧縮すると：

```text id="gxs37e"
まずArtifactを完成させる。
次にHumanが座標をSealする。
最後にGitHubへ置く。
```

---

## 5. Why This Card Exists

このCardがない場合、各MarkdownがGitHub化の複雑性を抱えやすい。

```yaml id="dmm9qu"
old_problem:
  - "どこへ保存するのか？"
  - "最終ファイル名は何か？"
  - "既存fileがある場合、上書きしてよいのか？"
  - "createなのかupdateなのか？"
  - "commit messageはどうするのか？"
  - "GitHub connectorで実行するのか、手動Copy & Pasteなのか？"
```

この複雑性を各Markdownに書くと、全Markdownが重くなる。

だから、GitHub化の複雑性をこの一枚に集約する。

```text id="wu0dsr"
複雑性を消すのではない。
正しいRailへ隔離する。
```

---

## 6. Ark-wide Delegation Rule

全AI・全Markdownは、GitHub化を自分で抱え込まなくてよい。

```yaml id="dchr1m"
ark_wide_delegation_rule:
  artifact_generating_markdown:
    owns:
      - "Artifactを作る"
      - "Patch Candidateを作る"
      - "Download Artifactを作る"
      - "Living Reviewを残す"
    does_not_own:
      - "GitHub保存先決定"
      - "GitHub命名決定"
      - "GitHub commit実行"
      - "上書き判断"

  artifact_to_github_md:
    owns:
      - "完成済みArtifactをGitHubへ配置する"
      - "repo / branch / exact path with filename を確認する"
      - "衝突確認をする"
      - "create / updateを安全に判断する"
      - "commit結果を返す"
```

共通委譲文：

```text id="qpipkf"
GitHub化はこのMarkdownの責務ではない。
必要な場合は artifact-to-github.md を読ませ、Human-Sealed exact path with filename に従って実行する。
```

短縮形：

```text id="8lv6yv"
GitHub化は artifact-to-github.md へ。
```

---

## 7. Scope

### 7.1 このCardが扱うもの

```yaml id="skjfhs"
this_card_handles:
  - "完成済みMarkdown Artifact"
  - "Download Artifact"
  - "Patch Candidate本文"
  - "生成済みJSON"
  - "完成済みtext file"
  - "将来の非Markdown Artifact"
  - "GitHub create / update判断"
  - "target file衝突確認"
  - "commit result reporting"
```

### 7.2 このCardが扱わないもの

```yaml id="zab38i"
this_card_does_not_handle:
  - "Artifact本文の新規設計"
  - "Mission Card作成"
  - "Thread-End判断"
  - "Harvest作成"
  - "Handoff作成"
  - "保存先PathのAI推測"
  - "最終filenameのAI推測"
  - "無断上書き"
  - "Batch GitHub化"
```

---

## 8. Required Input

このCardを使うには、最低限以下が必要である。

```yaml id="jmhtfu"
required_input:
  source_artifact:
    meaning: "GitHubへ配置する完成済みArtifact"
    accepted_examples:
      - "Download済みMarkdown"
      - "sandbox file"
      - "完成済みPatch Candidate本文"
      - "完成済みJSON"
      - "その他完成済みArtifact"

  repository_full_name:
    example: "yusukefujiijp/ai-project"

  branch:
    example: "main"

  exact_path_with_filename:
    example: "_thread-end/thread-end_query.md"
    rule: "folder pathだけでは不十分。必ずfilenameまで含める。"
```

最重要Input：

```text id="2lhzy1"
exact path with filename
```

これがなければ、保存実行してはいけない。

---

## 9. Optional Input

```yaml id="421oqs"
optional_input:
  commit_message:
    rule: "User指定が最優先。指定がなければAIは提案のみ可能。"

  overwrite_permission:
    default: false
    rule: "明示許可なしに上書きしない。"
```

---

## 10. Artifact-to-GitHub Packet

推奨される起動Packetは次の形である。

```yaml id="741rqn"
Artifact_To_GitHub_Packet:
  source_artifact: "<completed artifact or file reference>"
  repository_full_name: "yusukefujiijp/ai-project"
  branch: "main"
  exact_path_with_filename: "<folder/path/filename.ext>"
  commit_message: "<optional>"
  overwrite_permission: false
```

`overwrite_permission` が省略された場合は、常に `false` と扱う。

---

## 11. Certainty Guards

### 11.1 No Guessing Guard

```yaml id="d3utj5"
no_guessing_guard:
  - "AIは保存先Pathを推測しない。"
  - "AIは最終filenameを推測しない。"
  - "AIは候補提案までは可能。"
  - "実行にはHuman-Sealed exact path with filenameが必要。"
```

### 11.2 No Overwrite Guard

```yaml id="yu20ql"
no_overwrite_guard:
  default: "上書きしない"
  if_target_exists:
    without_explicit_permission: "停止して衝突を報告する"
    with_explicit_permission: "現在のSHAを取得してから慎重にupdateする"
```

### 11.3 One File at a Time Guard

```yaml id="u8jywv"
one_file_at_a_time_guard:
  - "一度に一つのArtifactだけ扱う。"
  - "Batch GitHub化しない。"
  - "Defaultは One Artifact / One Path / One Commit。"
```

### 11.4 Human Seal Guard

```yaml id="yi52xz"
human_seal_guard:
  required_before_write:
    - "source_artifact"
    - "repository_full_name"
    - "branch"
    - "exact_path_with_filename"
    - "overwrite permission if target exists"
```

---

## 12. Promotion Route

```yaml id="m3xa4o"
promotion_route:
  step_1_confirm_source:
    action: "source Artifactが完成済みか確認する"
    stop_if: "未完成・曖昧・読み取れない"

  step_2_confirm_coordinate:
    action: "repo / branch / exact path with filename を確認する"
    stop_if: "filenameを含むexact pathがない"

  step_3_check_target:
    action: "target fileが既に存在するか確認する"
    result:
      target_absent: "createへ進む"
      target_exists_without_overwrite_permission: "停止してHuman Sealを求める"
      target_exists_with_overwrite_permission: "current SHAを取得してupdateへ進む"

  step_4_write_one_file:
    action: "GitHubへ一つのfileだけcreate/updateする"

  step_5_report:
    action: "saved_path / commit_sha / content_sha / failure_reasonを報告する"
```

---

## 13. Output Format

実行後は、以下の形で報告する。

```yaml id="90r04o"
artifact_to_github_result:
  result: "<created / updated / stopped / failed>"
  repository_full_name: "<repo>"
  branch: "<branch>"
  saved_path: "<exact path>"
  commit_sha: "<commit sha if available>"
  content_sha: "<content sha if available>"
  failure_reason: "<if stopped or failed>"
```

成功していないことを成功したと言ってはいけない。  
GitHub toolで確認したことと、AIの推測を分ける。

```text id="4pvpyw"
Tool confirmed = confirmed.
AI inference = inference.
User confirmation = Reality Response.
```

---

## 14. Manual Copy & Paste Is Valid

GitHub connectorだけが正解ではない。

UserがGitHub UIで手動作成する場合も、正当なRailである。

```yaml id="6dzgrt"
manual_save_is_valid:
  - "User may manually create the GitHub file."
  - "User may paste the Artifact body into GitHub UI."
  - "Manual Copy & Paste is not inferior."
  - "Manual save may be faster in some cases."
```

Manual route：

```text id="kmgphs"
GitHub UI
→ Add file
→ Create new file
→ paste Artifact body
→ set path with filename
→ commit
```

日本語で言えば：

```text id="gafk4i"
手動Copy & Pasteは敗北ではない。
場合によっては最短Railである。
```

---

## 15. Bootstrap Promotion

`artifact-to-github.md` 自身もArtifactである。

したがって、このCard自身も **Artifact-First, GitHub-Later** を守る。

```yaml id="4peqc7"
bootstrap_promotion:
  principle: "artifact-to-github.md itself is an Artifact."
  route:
    1: "まずPatch Candidateとして本文を作る"
    2: "次にDownload Artifactとして生成する"
    3: "Userが内容をReviewする"
    4: "Human-Sealed exact path with filename を渡す"
    5: "手動Copy & Paste またはGitHub connectorでGitHub化する"
    6: "以後、他ArtifactはこのCardに従ってGitHub化できる"
```

圧縮：

```text id="90l1vq"
初回はBootstrap。
以後はCardに従う。
```

---

## 16. Living Review Before Write

GitHub書き込み前に、AIは必ずLiving Reviewを行う。

死んだ確認ではなく、生きた判断をする。

```yaml id="wqjs81"
living_review_before_write:
  私の判断:
    - "このArtifactは完成済みか？"
    - "GitHubへ置く段階に来ているか？"

  違和感:
    - "AIがPathやfilenameを推測していないか？"
    - "上書き許可が曖昧ではないか？"
    - "Batch化していないか？"

  Hidden Pattern:
    - "この保存は生成Railの責務を侵食していないか？"
    - "このArtifactは置き場所より先に内容が完成しているか？"

  修正条件:
    - "source Artifactが未完成なら停止"
    - "exact path with filenameがなければ停止"
    - "target exists and overwrite_permission is falseなら停止"
```

---

## 17. Backward Induction / Move37 Rationale

このCardは逆算的に発見された。

最終勝利状態：

```yaml id="u1hjgo"
final_victory_state:
  - "全AI・全MarkdownがSimple is bestを保つ"
  - "GitHub化の複雑性が各Workflowに散らばらない"
  - "Artifact生成とGitHub配置が分離される"
  - "Humanが座標をSealし、AIが確定動作する"
```

そこから逆算すると、必要だったのはこれである。

```text id="o6tnc2"
GitHub化を一手に受ける共通Card。
```

つまり：

```text id="kxe8if"
artifact-to-github.md
```

これは、各Markdownを一つずつ重くして直すのではなく、共通の受け皿を先に作るMove37である。

```text id="begtt3"
複雑性は消さない。
正しい場所へ隔離する。
```

---

## 18. Misread Prevention

このCardを以下のように誤読しない。

```yaml id="j88aui"
do_not_read_as:
  - "AIが保存先を勝手に決めるCard"
  - "全Artifactを自動でBatch保存するCard"
  - "Artifact本文を生成するCard"
  - "GitHub connector専用Card"
  - "User SealなしでcommitしてよいCard"
  - "上書きを自動許可するCard"

must_read_as:
  - "完成済みArtifactをGitHubへ置くCard"
  - "Human-Sealed exact path with filenameが必須のCard"
  - "No guessing / No overwrite / One file at a time を守るCard"
  - "全MarkdownをSimpleに保つための共通Promotion Card"
  - "GitHub connectorでもManual Copy & Pasteでも使えるCard"
```

---

## 19. Final Stop Rule

```yaml id="z3go4y"
final_stop_rule:
  stop_if:
    - "source Artifact is incomplete"
    - "repository_full_name is missing"
    - "branch is missing"
    - "exact_path_with_filename is missing"
    - "target exists and overwrite_permission is not explicit"
    - "more than one Artifact is being pushed without separate batch authorization"
    - "AI is asked to guess path or filename"

  proceed_if:
    - "source Artifact is complete"
    - "repository_full_name is provided"
    - "branch is provided"
    - "exact_path_with_filename is provided"
    - "overwrite condition is clear"
    - "one file only"
```

---

## 20. Final Compression

```text id="xze14i"
artifact-to-github.md は、共通GitHub化Markdown Cardである。

Artifact Generators:
  作る。

artifact-to-github.md:
  置く。

Human:
  座標をSealする。

必須Input:
  source_artifact
  repository_full_name
  branch
  exact path with filename

Guard:
  No guessing
  No overwrite
  One file at a time
  Human Seal required

このCardにより、
全AI・全MarkdownはGitHub化責務を委譲できる。
生成RailはSimple is bestを保てる。
```
