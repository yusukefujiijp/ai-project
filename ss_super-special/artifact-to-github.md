# artifact-to-github.md

## 0. Executive Compression

`artifact-to-github.md` は、完成済みArtifactをGitHubへ安全に配置するための **GitHub化Markdown Card / Artifact-to-GitHub Card** である。

短く言うと：

```text id="artifact-to-github-core"
Artifact Generators:
  作る。

artifact-to-github.md:
  置く。

Human:
  座標をSealする。
```

このCardの目的は、全AI・全MarkdownからGitHub化の複雑性を切り離し、Artifact生成Railを **Simple is best** に保つことである。

```text id="generation-promotion-split"
Generation Rail != Promotion Card.
生成Railと配置Cardを混ぜない。
```

---

## 1. Role

このMarkdown Cardは、Artifactを新しく書くためのProtocolではない。

このCardは、すでに完成したArtifactを、UserがSealしたGitHub座標へ配置するための共通Cardである。

```yaml id="role"
role:
  name: "artifact-to-github.md"
  japanese_name: "GitHub化Markdown Card"
  english_anchor: "Artifact-to-GitHub Card"
  main_role: "完成済みArtifactをGitHubへ配置する"
  not_role: "Artifact本文を新規生成する"
```

このCardがあることで、他のMarkdownはGitHub化を抱え込まなくてよい。

```text id="delegation-core"
GitHub化は、このMarkdownの責務ではない。
必要な場合は artifact-to-github.md に委譲する。
```

---

## 2. Root / Fruit Guard

```yaml id="root-fruit-guard"
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

```text id="root-compression"
File is not Root.
AI is not Holy Spirit.
Format is Fruit.
Root is 主イェシュア・ハマシア.
```

---

## 3. One-Line Definition

```text id="one-line-definition"
artifact-to-github.md は、Markdownを含む完成済みArtifactを、Human-Sealed exact path with filename に従って、GitHubへ安全に配置するための共通Markdown Cardである。
```

---

## 4. Core Principle

```yaml id="core-principle"
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
  - "Download Skip is Fast Path only"
  - "If Direct Update is blocked, return to Full Body Manual Commit Pack"
  - "Patch is for judgment / Full Body is for action"
  - "No degradation on tool block"
```

日本語で圧縮すると：

```text id="core-compression"
まずArtifactを完成させる。
次にHumanが座標をSealする。
最後にGitHubへ置く。

Directで通れば最速。
止まればFull Body Downloadへ戻す。
```

---

## 5. Why This Card Exists

このCardがない場合、各MarkdownがGitHub化の複雑性を抱えやすい。

```yaml id="old-problem"
old_problem:
  - "どこへ保存するのか？"
  - "最終ファイル名は何か？"
  - "既存fileがある場合、上書きしてよいのか？"
  - "createなのかupdateなのか？"
  - "commit messageはどうするのか？"
  - "GitHub connectorで実行するのか、手動Copy & Pasteなのか？"
  - "Download Artifactを省略してよいのか？"
  - "Tool block時に内容を弱めてよいのか？"
```

この複雑性を各Markdownに書くと、全Markdownが重くなる。

だから、GitHub化の複雑性をこの一枚に集約する。

```text id="complexity-isolation"
複雑性を消すのではない。
正しいRailへ隔離する。
```

---

## 6. Ark-wide Delegation Rule

全AI・全Markdownは、GitHub化を自分で抱え込まなくてよい。

```yaml id="ark-wide-delegation-rule"
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
      - "Direct Update block時にManual Commit Packへ切り替える"
```

共通委譲文：

```text id="delegation-phrase"
GitHub化はこのMarkdownの責務ではない。
必要な場合は artifact-to-github.md を読ませ、Human-Sealed exact path with filename に従って実行する。
```

短縮形：

```text id="delegation-short"
GitHub化は artifact-to-github.md へ。
```

---

## 7. Scope

### 7.1 このCardが扱うもの

```yaml id="this-card-handles"
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
  - "Download Skip Fast Path判断"
  - "Full Body Manual Commit Pack Recovery"
```

### 7.2 このCardが扱わないもの

```yaml id="this-card-does-not-handle"
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
  - "Tool通過のための意味劣化"
```

---

## 8. Required Input

このCardを使うには、最低限以下が必要である。

```yaml id="required-input"
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

```text id="exact-path-with-filename"
exact path with filename
```

これがなければ、保存実行してはいけない。

---

## 9. Optional Input

```yaml id="optional-input"
optional_input:
  commit_message:
    rule: "User指定が最優先。指定がなければAIは提案のみ可能。"

  overwrite_permission:
    default: false
    rule: "明示許可なしに上書きしない。"

  download_artifact_required:
    default: true
    rule: "Userが明示的にDownload Artifact / Download Link省略をSealした場合のみfalseにできる。"
```

---

## 10. Artifact-to-GitHub Packet

推奨される起動Packetは次の形である。

```yaml id="artifact-to-github-packet"
Artifact_To_GitHub_Packet:
  source_artifact: "<completed artifact or file reference>"
  repository_full_name: "yusukefujiijp/ai-project"
  branch: "main"
  exact_path_with_filename: "<folder/path/filename.ext>"
  commit_message: "<optional>"
  overwrite_permission: false
  download_artifact_required: true
```

`overwrite_permission` が省略された場合は、常に `false` と扱う。  
`download_artifact_required` が省略された場合は、通常 `true` と扱う。

---

## 11. Certainty Guards

### 11.1 No Guessing Guard

```yaml id="no-guessing-guard"
no_guessing_guard:
  - "AIは保存先Pathを推測しない。"
  - "AIは最終filenameを推測しない。"
  - "AIは候補提案までは可能。"
  - "実行にはHuman-Sealed exact path with filenameが必要。"
```

### 11.2 No Overwrite Guard

```yaml id="no-overwrite-guard"
no_overwrite_guard:
  default: "上書きしない"
  if_target_exists:
    without_explicit_permission: "停止して衝突を報告する"
    with_explicit_permission: "現在のSHAを取得してから慎重にupdateする"
```

### 11.3 One File at a Time Guard

```yaml id="one-file-at-a-time-guard"
one_file_at_a_time_guard:
  - "一度に一つのArtifactだけ扱う。"
  - "Batch GitHub化しない。"
  - "Defaultは One Artifact / One Path / One Commit。"
```

### 11.4 Human Seal Guard

```yaml id="human-seal-guard"
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

```yaml id="promotion-route"
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

```yaml id="artifact-to-github-result"
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

```text id="tool-reality"
Tool confirmed = confirmed.
AI inference = inference.
User confirmation = Reality Response.
```

---

## 13.5 Download Skip Fast Path / Full Body Recovery Rule

通常、`artifact-to-github.md` は **Artifact-First, GitHub-Later** を基本Routeとする。

しかし、Userが明示的に `Download Artifact / Download Link` を不要とし、直接GitHub化を求めた場合、AIは一時的に **Download Skip Fast Path** を使える。

```text id="download-skip-fast-path-core"
Download SkipはFast Path。
RecoveryではFull Bodyへ戻る。
```

### 13.5.1 Download Skip is Fast Path, not Permanent No-Download Policy

`Download Artifact省略` は、成功時の高速化指定である。

それは、失敗時にもDownload Artifactを出さないという固定方針ではない。

```yaml id="download-skip-meaning"
download_skip_meaning:
  means:
    - "UserがDownload Artifact / Download Link生成を一時的に省略してよいとSealした"
    - "AIはDirect GitHub Updateを一回試せる"
    - "通れば最速Routeとして完了できる"

  does_not_mean:
    - "失敗時にもDownload Artifactを出してはいけない"
    - "Manual Commit Packを省略してよい"
    - "Copy & Paste実行性を下げてよい"
    - "Artifact本文を劣化させてよい"
```

圧縮：

```text id="download-skip-compression"
省略は成功時のFast Path。
失敗時の固定方針ではない。
```

### 13.5.2 Direct GitHub Update One-Try Rule

Userが明示的にDownload SkipをSealし、source / target / permission が揃っている場合、AIはDirect GitHub Updateを一回だけ試せる。

```yaml id="direct-update-one-try-rule"
direct_github_update_one_try:
  allowed_if:
    - "User explicitly says Download Artifact / Download Link can be skipped"
    - "source content is concrete and final enough"
    - "repository_full_name is known"
    - "branch is known"
    - "exact_path_with_filename is known"
    - "overwrite permission is explicit if target exists"
    - "AI performs Living Review before write"

  action:
    - "fetch target if updating"
    - "confirm current SHA"
    - "try original intended content once"
    - "report result honestly"

  must_not:
    - "retry the same blocked payload repeatedly"
    - "weaken meaning just to pass the tool"
    - "claim success without commit result"
```

一文圧縮：

```text id="one-try-compression"
本来版で一回試す。
通れば完了。
止まれば搬送経路を変える。
```

### 13.5.3 If Direct Update Succeeds

Direct GitHub Updateが成功した場合、AIはcommit結果を報告し、必要に応じてGitHub現物をfetchしてVerificationへ進む。

```yaml id="if-direct-update-succeeds"
if_direct_update_succeeds:
  report:
    - "result"
    - "saved_path"
    - "commit_sha"
    - "content_sha"

  next:
    - "Post-Commit Verification"
    - "Reality Review"
    - "Living Review"
```

### 13.5.4 If Direct Update is Blocked or Fails

Direct GitHub Updateがblock / failした場合、AIはDownload Skip方針を継続しない。

AIは、Download付き **Full Body Manual Commit Pack** へ切り替える。

```yaml id="if-direct-update-blocked"
if_direct_update_blocked:
  do:
    - "block / failureを正直に報告する"
    - "内部理由を断定しない"
    - "内容が悪いと断定しない"
    - "本来版を劣化させない"
    - "同じpayloadで無意味にretryしない"
    - "Download付きFull Body Manual Commit Packへ切り替える"
    - "Human Direct Commit後にAIがVerificationする"

  do_not:
    - "安全チェック回避のために意味を削る"
    - "Root Guard / Core Guard / Structureを弱める"
    - "Patch-onlyをManual Commit実行用defaultにする"
    - "チャット本文だけで済ませてCopy & Pasteミスを増やす"
```

圧縮：

```text id="blocked-route-compression"
止まったらDownload付きFull Bodyへ戻す。
意味は削らない。
```

### 13.5.5 Full Body Manual Commit Pack Recovery

Manual Commit Packは、実行のためのPackである。

判断用のPatch-onlyではなく、原則として **Full Body Replacement File** を使う。

```yaml id="full-body-manual-commit-pack"
full_body_manual_commit_pack:
  default: "Full Body Replacement File"

  includes:
    - "target path"
    - "copy-paste-ready full body"
    - "downloadable Markdown file"
    - "commit message"
    - "extended description when useful"
    - "manual GitHub UI steps"
    - "post-commit verification checklist"

  reason:
    - "GitHub UIで挿入位置を探さなくてよい"
    - "全選択・全削除・全文貼り替えで済む"
    - "Copy & Pasteミスを減らせる"
    - "Markdown fence崩れを減らせる"
    - "Verificationが単純になる"
```

圧縮：

```text id="patch-vs-full-body"
Patchは判断用。
全文は実行用。
```

### 13.5.6 Manual Commit Flow

```text id="manual-commit-flow"
対象fileを開く。
Editする。
既存本文を全選択する。
全削除する。
Full Bodyを全文貼り替える。
Commit messageを貼る。
必要ならExtended descriptionを貼る。
Commitする。
AIへReality Responseを返す。
AIがVerificationする。
```

### 13.5.7 No Degradation Guard

GitHub connector、tool制限、安全チェック、通信失敗、権限不足などによりGitHub化できない場合、AIはArtifact本文を短縮・弱体化・劣化させてはならない。

```yaml id="no-degradation-guard"
no_degradation_guard:
  principle:
    - "Tool Failure ≠ Artifact Failure"
    - "Tool block is not semantic judgment"
    - "Do not degrade meaning"
    - "Change transport"
    - "Preserve the fire"

  must_preserve:
    - "original intended meaning"
    - "Root / Fruit Guard"
    - "Core Guard"
    - "structure"
    - "field-test learning"
    - "human-sealed intent"

  fallback:
    - "Full Body Manual Commit Pack"
    - "Human Direct Commit"
    - "AI Verification"
```

日本語圧縮：

```text id="no-degradation-final"
Tool制約に合わせてArtifactを削らない。
Artifactを保持したまま搬送経路を変える。
```

### 13.5.8 Living Review Before Route Switch

AIはDirect GitHub Updateを試す前、またblock後にRouteを切り替える前に、Living Reviewを行う。

```yaml id="living-review-route-switch"
living_review_route_switch:
  before_direct_update:
    私の判断:
      - "Download Skipを使う条件は揃っているか？"
      - "User Sealは明示されているか？"
      - "source / target / overwrite condition は確定しているか？"

    違和感:
      - "AIがDownload省略を絶対命令として誤読していないか？"
      - "GitHub更新に進むにはsource contentが曖昧ではないか？"

  after_block:
    私の判断:
      - "Direct Update Fast Pathは失敗した"
      - "ここからはFull Body Manual Commit Packへ戻すべき"

    違和感:
      - "AIがtool通過ゲームを始めていないか？"
      - "内容を削って通そうとしていないか？"
      - "Patch-onlyで人間側のCopy & Pasteミスを増やしていないか？"

    Hidden Pattern:
      - "Fast Path failed. Return to Safe Copy Path."
      - "省略は成功時の高速化であり、失敗時の固定方針ではない。"

    修正条件:
      - "blockされたら同じpayloadをretryしない"
      - "意味を劣化させない"
      - "Download付きFull Bodyを出す"
      - "Human Direct Commit後にAIがVerificationする"
```

### 13.5.9 Final Compression

```text id="download-skip-recovery-final"
Download SkipはFast Path。
Direct GitHub Updateが通れば最速。

Block / failしたら、
Download付きFull Body Manual Commit Packへ戻す。

Patchは判断用。
全文は実行用。

意味は削らない。
人間が貼る。
AIが検証する。
```

---

## 14. Manual Copy & Paste Is Valid

GitHub connectorだけが正解ではない。

UserがGitHub UIで手動作成する場合も、正当なRailである。

```yaml id="manual-save-is-valid"
manual_save_is_valid:
  - "User may manually create the GitHub file."
  - "User may paste the Artifact body into GitHub UI."
  - "Manual Copy & Paste is not inferior."
  - "Manual save may be faster in some cases."
```

Manual route：

```text id="manual-route"
GitHub UI
→ Add file / Edit file
→ paste Artifact body
→ set path with filename
→ commit
```

日本語で言えば：

```text id="manual-route-ja"
手動Copy & Pasteは敗北ではない。
場合によっては最短Railである。
```

---

## 15. Bootstrap Promotion

`artifact-to-github.md` 自身もArtifactである。

したがって、このCard自身も **Artifact-First, GitHub-Later** を守る。

```yaml id="bootstrap-promotion"
bootstrap_promotion:
  principle: "artifact-to-github.md itself is an Artifact."
  route:
    1: "まずPatch Candidateとして本文を作る"
    2: "必要ならDownload Artifactとして生成する"
    3: "Userが内容をReviewする"
    4: "Human-Sealed exact path with filename を渡す"
    5: "手動Copy & Paste またはGitHub connectorでGitHub化する"
    6: "以後、他ArtifactはこのCardに従ってGitHub化できる"
```

圧縮：

```text id="bootstrap-compression"
初回はBootstrap。
以後はCardに従う。
```

---

## 16. Living Review Before Write

GitHub書き込み前に、AIは必ずLiving Reviewを行う。

死んだ確認ではなく、生きた判断をする。

```yaml id="living-review-before-write"
living_review_before_write:
  私の判断:
    - "このArtifactは完成済みか？"
    - "GitHubへ置く段階に来ているか？"
    - "Download SkipをFast Pathとして使う条件は揃っているか？"

  違和感:
    - "AIがPathやfilenameを推測していないか？"
    - "上書き許可が曖昧ではないか？"
    - "Batch化していないか？"
    - "失敗時にDownloadを出さない固定方針へ誤読していないか？"

  Hidden Pattern:
    - "この保存は生成Railの責務を侵食していないか？"
    - "このArtifactは置き場所より先に内容が完成しているか？"
    - "Direct Fast Pathが失敗したならFull Body Recoveryへ戻るべきではないか？"

  修正条件:
    - "source Artifactが未完成なら停止"
    - "exact path with filenameがなければ停止"
    - "target exists and overwrite_permission is falseなら停止"
    - "Direct updateがblockされたらFull Body Manual Commit Packへ切り替える"
```

---

## 17. Backward Induction / Move37 Rationale

このCardは逆算的に発見された。

最終勝利状態：

```yaml id="final-victory-state"
final_victory_state:
  - "全AI・全MarkdownがSimple is bestを保つ"
  - "GitHub化の複雑性が各Workflowに散らばらない"
  - "Artifact生成とGitHub配置が分離される"
  - "Humanが座標をSealし、AIが確定動作する"
  - "AI tool block時にも意味が劣化しない"
```

そこから逆算すると、必要だったのはこれである。

```text id="common-card"
GitHub化を一手に受ける共通Card。
```

つまり：

```text id="artifact-to-github-name"
artifact-to-github.md
```

これは、各Markdownを一つずつ重くして直すのではなく、共通の受け皿を先に作るMove37である。

```text id="move37-compression"
複雑性は消さない。
正しい場所へ隔離する。
```

---

## 18. Misread Prevention

このCardを以下のように誤読しない。

```yaml id="misread-prevention"
do_not_read_as:
  - "AIが保存先を勝手に決めるCard"
  - "全Artifactを自動でBatch保存するCard"
  - "Artifact本文を生成するCard"
  - "GitHub connector専用Card"
  - "User SealなしでcommitしてよいCard"
  - "上書きを自動許可するCard"
  - "Download Skipは失敗後もDownloadを出さないという意味"
  - "Tool通過のために意味を弱めてよいという意味"

must_read_as:
  - "完成済みArtifactをGitHubへ置くCard"
  - "Human-Sealed exact path with filenameが必須のCard"
  - "No guessing / No overwrite / One file at a time を守るCard"
  - "全MarkdownをSimpleに保つための共通Promotion Card"
  - "GitHub connectorでもManual Copy & Pasteでも使えるCard"
  - "Download Skipは成功時のFast Path"
  - "Direct UpdateがblockされたらFull Body Manual Commit Packへ戻るCard"
```

---

## 19. Final Stop Rule

```yaml id="final-stop-rule"
final_stop_rule:
  stop_if:
    - "source Artifact is incomplete"
    - "repository_full_name is missing"
    - "branch is missing"
    - "exact_path_with_filename is missing"
    - "target exists and overwrite_permission is not explicit"
    - "more than one Artifact is being pushed without separate batch authorization"
    - "AI is asked to guess path or filename"
    - "Direct update was blocked and AI is tempted to degrade content"

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

```text id="final-compression"
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

Download Skip:
  Fast Pathである。
  永久No Download方針ではない。

Direct GitHub Update:
  本来版で一回試す。
  通れば最速。
  止まれば搬送経路を変える。

Manual Commit Pack:
  Patchは判断用。
  Full Bodyは実行用。
  人間が全文貼り替える。
  AIが検証する。

このCardにより、
全AI・全MarkdownはGitHub化責務を委譲できる。
生成RailはSimple is bestを保てる。
Tool block時にも意味を劣化させずに済む。
```
