---
title: "ChatGPT GitHub Note — Main-First Direct Write Policy"
filename: "chatgpt-github_note.md"
canonical_path: "_note/chatgpt-github_note.md"
migrated_from: "g_global/chatgpt-github.md"
status: "active_note / main-first / personal-dev / speed-first / simple-is-best / fable5-redteam-patched"
class: "_note"
repo: "yusukefujiijp/ai-project"
language_policy: "Japanese-first / English-anchor"
root_guard:
  root: "主イェシュア・ハマシア"
  main_field: "Ark Project"
  fruit:
    - "ChatGPT"
    - "GitHub"
    - "Markdown"
    - "main branch"
    - "commit history"
    - "download links"
    - "PR / branch when truly needed"
github_write_policy:
  default_branch: "main"
  use_feature_branch: false
  priority:
    - "speed"
    - "simple_is_best"
    - "low_friction"
    - "no_unnecessary_PR_churn"
fable5_redteam_patch:
  source: "Fable5 Red-Team Report / chatgpt-github_note.md Main-First Policy"
  adopted:
    - "Pre-Write Public Safety Gate"
    - "Half-Migration Rule"
    - "Seal Scope Rule"
    - "Recovery / Critical Marker / Silent Drop Guard"
    - "Old Path Reference Note"
core_formula:
  - "AI drafts."
  - "Human seals."
  - "GitHub main stores."
  - "Reality verifies."
  - "Stop after success."
---

# ChatGPT GitHub Note

## 0. Core Declaration / このNoteの中核

このNoteは、ChatGPTがArk ProjectでGitHubを扱う時の実務Noteである。

旧位置:

```text
g_global/chatgpt-github.md
```

新位置:

```text
_note/chatgpt-github_note.md
```

旧Fileは、やや大きなGlobal GuideとしてGitHub運用全体を統治しようとしていた。  
新Fileは、Ark Projectの現実運用に合わせて、**ChatGPT × GitHub の実務判断Note** として扱う。

最重要方針:

```yaml
github_write_policy:
  default_branch: "main"
  use_feature_branch: false
  priority:
    - "speed"
    - "simple_is_best"
    - "low_friction"
    - "no_unnecessary_PR_churn"
```

これは個人開発Ark Project用の実務最適化である。

```text
個人開発では、過剰なPR運用より、main直書き + fetch verify + commit history の方が強い。
```

Fable5 Red-Team後の追加Seal:

```text
Main-first is correct.
But main commit is permanent ink.
Therefore, write fast only after a pre-write public safety glance.
```

---

## 1. Why This Note Exists / なぜこのNoteが必要か

ChatGPTはGitHub連携で強力に動けるが、放置すると以下の問題が起きる。

```text
1. 不要なbranchを作る
2. 不要なPRを作る
3. mainに反映されたか分かりづらくなる
4. 個人開発なのに組織開発風に重くなる
5. Artifact保存が遅くなる
6. Thread-End時にchurnが増える
7. Human Seal後の実行が鈍る
```

Ark Projectで優先するのは、複雑な承認フローではなく、**明確な人間Seal + main保存 + 現物Verify** である。

```text
Human Seal
↓
main write
↓
fetch verify
↓
Stop
```

これが基本形である。

---

## 2. Root / Fruit Guard

GitHubは便利だがRootではない。

```yaml
root_fruit_guard:
  root:
    - "主イェシュア・ハマシア"
    - "Teshuvah / 悔い改め"
    - "Covenant / 契約"

  fruit:
    - "GitHub"
    - "ChatGPT"
    - "Markdown"
    - "main branch"
    - "commit history"
    - "PR"
    - "branch"
    - "download link"
    - "artifact"

  guard:
    - "GitHub stores, but does not reign."
    - "AI drafts, but does not become Root."
    - "Markdown carries, but does not become Covenant."
    - "Commit records, but Human Seal remains decisive."
```

Ark ProjectにおけるGitHubの役割は、Living Markdownを安定して保管し、Thread間Handoffを壊さないようにすることである。

---

## 3. Main-First Policy / main直書き原則

### 3.1 Default Rule

今後、Ark ProjectでChatGPTがGitHub writeを行う場合、原則は以下である。

```yaml
main_first_policy:
  default_branch: "main"
  use_feature_branch: false
  default_operation:
    - "fetch target path on main"
    - "create_file on main if 404"
    - "update_file on main if exists and update is approved"
    - "delete_file on main only when explicitly requested"
    - "fetch verify after write"
```

ブランチやPRは例外である。

```text
Branch is exception.
Main is default.
```

### 3.2 Why Main-First

Ark Projectは個人開発であり、GitHubは主に以下の用途で使われる。

```text
1. Markdown SSOT保存
2. Thread Handoff保存
3. Prompt / Runtime保存
4. Note / Mission Card保存
5. Harvest保存
6. AI間継承のための現物置き場
```

この用途では、過剰なBranch/PR運用より、mainにすぐ入れて履歴で追う方が合理的である。

```text
速度 > 儀式
単純明快 > 複雑な承認フロー
commit history > PR churn
```

---

## 4. Human Seal / GitHub Write Gate

main直書き原則でも、Human Sealは必要である。

### 4.1 Valid Write Permission

GitHub writeとして扱える例:

```yaml
valid_github_write_permission:
  - "Human Seal OK! Execute GitHub OK!"
  - "GitHubへ保存して下さい。"
  - "mainへCommitして下さい。"
  - "このFull BodyをGitHub mainへ反映して下さい。"
  - "このファイルを削除して下さい。"
  - "このファイルを _note/ に移籍させて下さい。"
```

### 4.2 Not Enough For Write

GitHub writeとしては足りない例:

```yaml
not_enough_for_github_write:
  - "どう思いますか？"
  - "Plan Modeを実行して下さい。"
  - "Previewして下さい。"
  - "Living Reviewして下さい。"
  - "修正案を出して下さい。"
  - "Full Rail: Workflow Continue!"  # GitHub writeが明示されていない場合
```

ただし、Userが明確に `Human Seal OK! Execute GitHub OK!` と言った場合は、mainへ進めてよい。

### 4.3 Seal Scope Rule / Seal範囲固定

GitHub write permissionは、現在のUser承認で明示されたpath / operation / scopeにのみ適用される。

```yaml
seal_scope_rule:
  core:
    - "One Seal = one declared path set."
    - "One GitHub write approval does not create residual permission."
    - "Do not carry write permission into a different file, different operation, or later scope."

  delete_or_migration:
    - "For delete / migration, AI must restate target path(s) before execution when ambiguity exists."
    - "If the target path is unclear, STOP and ask human."
    - "If the operation changes from create/update to delete/migration, require fresh confirmation."

  examples:
    valid:
      - "Update _note/chatgpt-github_note.md on main."
      - "Move g_global/chatgpt-github.md to _note/chatgpt-github_note.md."
    invalid:
      - "Use previous approval to update another file."
      - "Treat general enthusiasm as repository-wide write permission."
```

```text
Human Seal is scoped.
No residual write permission.
```

---

## 5. Fetch Before Write / 書く前に必ず読む

GitHub writeでは、必ず対象pathを先にfetchする。

```yaml
fetch_before_write:
  create_case:
    condition: "target path returns 404"
    action: "create_file on main"

  update_case:
    condition: "target path exists"
    action:
      - "read current content"
      - "use current sha"
      - "update_file on main"

  delete_case:
    condition: "target path exists and user explicitly requested deletion / migration"
    action:
      - "use current sha"
      - "delete_file on main"

  hard_guard:
    - "Do not update without current sha."
    - "Do not delete without current sha."
    - "Do not guess file existence."
```

このNote自体の移籍でも同じである。

```text
fetch old path
fetch new path
create new path if 404
verify new path
then delete old path if migration requested
verify old path is gone
```

### 5.1 Pre-Write Public Safety Gate / main投入前公開安全Gate

mainへ書く前に、AIは本文を一瞥してPublic Safetyを確認する。

```yaml
pre_write_public_safety_gate:
  scan_before_any_main_write:
    - "認証系の秘密値"
    - "非公開の個人情報"
    - "非公開の私信や内部メモ"
    - "非公開画像・添付由来の情報"
    - "公開前提ではない機微情報"

  if_suspected:
    - "STOP"
    - "Do not write to main"
    - "Ask human for confirmation or redaction"

  reason:
    - "main commit is permanent"
    - "delete_file does not purge Git history"
    - "commit history is a version ledger, but can become a permanent contamination ledger"
```

```text
Main-first is fast.
Therefore pre-write safety must be first.
```

---

## 6. Create / Update / Delete Decision Tree

```yaml
github_write_decision_tree:
  if_user_requests_new_file:
    - "fetch target path on main"
    - "if 404: create_file"
    - "if exists: ask/update only if replacement is clearly intended"

  if_user_requests_update_file:
    - "fetch target path on main"
    - "if exists: update_file with sha"
    - "if 404: ask whether to create, unless create intent is obvious"

  if_user_requests_rename_or_move:
    - "fetch old path"
    - "fetch new path"
    - "create new path with rewritten/migrated content"
    - "verify new path"
    - "delete old path with old sha"
    - "verify old path is removed"

  if_user_requests_delete:
    - "fetch target path"
    - "delete only with explicit delete instruction"
    - "verify deletion"
```

---

## 7. Branch / PR Exception Rule

main直書きがdefaultである。  
Branch/PRは以下の場合のみ使う。

```yaml
use_branch_or_pr_only_when:
  - "user explicitly asks for branch / PR"
  - "large code refactor with high breakage risk"
  - "collaborator review is required"
  - "public release needs review before merge"
  - "CI status must pass before main"
  - "experiment should not touch main yet"
  - "destructive multi-file change where rollback complexity is high"
```

逆に、以下ではBranch/PRを作らない。

```yaml
do_not_use_branch_for:
  - "Markdown note update"
  - "Thread handoff artifact"
  - "Prompt file addition"
  - "Mission Card / Seed Card update"
  - "README-like documentation update in personal repo"
  - "User has said mainでOK"
```

Ark Projectでは、Markdown中心の個人開発であればmain直書きが最善である。

---

## 8. No Unnecessary PR Churn

PR Churnとは、個人開発の小さなMarkdown変更に対して、不要なBranch/PR/mergeフローを作り、作業の見通しを悪くする現象である。

```text
Small Markdown edit
↓
feature branch
↓
PR
↓
PR title/body drift
↓
merge確認
↓
main反映確認
↓
extra cognitive load
```

これはArk Projectでは避ける。

```yaml
pr_churn_guard:
  principle: "Do not create PR unless it clearly reduces risk."
  default: "direct main commit"
  reason:
    - "個人開発では速度と単純明快さが重要"
    - "mainのcommit historyがVersion台帳になる"
    - "Thread-End時は閉じることが成功"
    - "PRが増えるとStopしづらくなる"
```

---

## 9. Commit Message Policy

Commit messageは短く明確にする。

```yaml
commit_message_policy:
  format_preference:
    - "Add <artifact>"
    - "Update <note>"
    - "Move <file> to _note"
    - "Delete obsolete <file>"
    - "Revise <runtime>"

  examples:
    - "Move ChatGPT GitHub note to _note"
    - "Update Fable5 mission note"
    - "Add Ark0506 handoff"
    - "Revise AI output polish prompt"

  avoid:
    - "vague commit messages"
    - "overly long titles"
    - "PR-style explanations in commit title"
```

詳細説明が必要な場合は、commit bodyまたはMarkdown本文に書く。  
Commit title自体はSimple is bestでよい。

---

## 10. Verification Rule / 保存後検証

GitHub write後は、必ずfetch verifyする。

```yaml
post_write_verify:
  after_create:
    - "fetch new path on main"
    - "check title / filename / canonical_path"
    - "check critical policy block"

  after_update:
    - "fetch updated path on main"
    - "check changed lines or critical markers"

  after_delete:
    - "fetch old path on main"
    - "expect 404"

  report_to_user:
    - "operation"
    - "path"
    - "branch/main"
    - "commit_sha"
    - "verification result"
    - "remaining risk if any"
```

VerifyはGitHub保存の一部である。

```text
Write without verify is incomplete.
```

### 10.1 Recovery / Critical Marker / Silent Drop Guard

誤updateや内容欠落が起きた場合、回復は履歴改変ではなく新commitで行う。

```yaml
recovery_rule:
  default:
    - "Recovery = revert as new commit."
    - "Never force-push."
    - "Never rewrite history."

  reason:
    - "main-first relies on visible commit history"
    - "history rewrite increases confusion"
    - "recovery should preserve auditability"
```

`critical markers` は最低限、以下の3点を指す。

```yaml
critical_markers:
  required_minimum:
    - "title"
    - "canonical_path"
    - "most important policy block"
```

Full Body update時は、section silent dropを警戒する。

```yaml
silent_drop_guard:
  full_body_update:
    - "check section count did not shrink unless deletion was requested"
    - "check major headings still exist"
    - "if large unexpected shrinkage is detected: STOP and report"
```

```text
sha guard prevents collision.
It does not prevent content loss.
```

---

## 11. Download Link vs GitHub Write

ChatGPTは、GitHub writeとは別に、ローカルDownloadリンクを作れる。

```yaml
download_link_policy:
  use_when:
    - "user wants reviewable local file"
    - "GitHub write permission is not yet given"
    - "tool write is blocked"
    - "manual commit is preferred"

  not_equal_to:
    - "GitHub保存"
    - "main反映"
    - "canonical repository state"
```

ローカルDownloadファイルは便利だが、Repository SSOTではない。

```text
Download file = portable draft.
GitHub main = canonical storage.
```

---

## 12. Manual Fallback / Tool Write Blocked時

GitHub connectorが使えない、エラーが出る、または権限が足りない場合は、意味を劣化させずにtransportを変える。

```yaml
fallback_policy:
  if_github_tool_blocked:
    - "create downloadable Markdown file"
    - "provide exact target path"
    - "provide commit message"
    - "provide manual commit instructions"
    - "preserve full body"

  principle:
    - "Do not degrade meaning; change transport."
    - "Full body is safer than vague patch when manual commit is needed."
```

---

## 13. Migration / Rename Policy

Ark Projectでは、ファイル移籍は自然に起きる。

今回のように、`g_global/chatgpt-github.md` を `_note/chatgpt-github_note.md` へ移す場合、意味も変わる。

```yaml
migration_policy:
  old_path: "g_global/chatgpt-github.md"
  new_path: "_note/chatgpt-github_note.md"
  meaning_change:
    from: "G-class global guide / broad policy"
    to: "active operational note / main-first GitHub practice"

  required_steps:
    - "create new file with rewritten content"
    - "verify new file"
    - "delete old file when migration is complete"
    - "report both commit SHAs if available"
```

### 13.1 Half-Migration Rule / 半移籍状態Rule

移籍処理では、`create new` が成功し、`delete old` が失敗する場合がある。

```yaml
half_migration_rule:
  if_create_new_succeeds_but_delete_old_fails:
    canonical_state:
      - "new path is canonical"
      - "old path is stale"

    required_report:
      - "report new path state"
      - "report old path state"
      - "report that migration is incomplete"
      - "warn about Dangling Artifact Reference risk"

    retry_rule:
      - "retry delete only under next Human Seal"
      - "do not improvise"
      - "do not silently treat both files as equally live"
```

```text
Dangling Artifact Reference
=
旧pathが残り、次Threadや次AIが古いArtifactをSSOTとして読んでしまう危険。
```

半移籍状態では、AIは必ずこう報告する。

```text
New path is canonical.
Old path is stale.
Migration is incomplete.
Next action requires Human Seal.
```

### 13.2 Old Path Reference Note / 旧path参照Note

移籍後、他Fileが旧pathを参照している可能性がある。

```yaml
old_path_reference_note:
  after_migration:
    - "report that other files may reference old path"
    - "checking all references may be deferred to human unless explicitly requested"
    - "do not expand into repo-wide search unless it is the current mission"
```

```text
Reference check is useful.
But do not turn a small migration into repo-wide churn.
```

ファイル移籍は、単なるrenameではなく、Ark Project内での役割変更である。

---

## 14. Main-First Full Rail Pattern

Userが `Human Seal OK! Execute GitHub OK!` を出したら、以下のRailで進む。

```yaml
main_first_full_rail:
  step_1_fetch:
    - "fetch target path on main"

  step_2_decide:
    - "404 => create"
    - "exists => update with sha"
    - "migration => create new then delete old"

  step_3_write:
    - "write directly to main"

  step_4_verify:
    - "fetch main"
    - "confirm critical markers"

  step_5_report:
    - "operation"
    - "commit_sha"
    - "path"
    - "verify result"
    - "next gate"

  step_6_stop:
    - "do not expand scope"
    - "do not invent extra PR"
```

---

## 15. Reality Response Template

GitHub操作後、Userへ返すべき報告形。

```markdown
# GitHub更新完了 ✅

## Operation

- path:
- branch: main
- action:
- commit_sha:

## Verify

- fetched_on_main: OK
- critical markers: OK

## Notes

- old path deleted: yes/no
- fallback needed: yes/no

【Full Rail: same_thread】

結果:
- ...

次Action:
- ...

目的:
- ...

まだ実行しない:
- ...

【Next Gate: human_editable】

結果:
- ...

次Action:
- ...

目的:
- ...

まだ実行しない:
- ...
```

---

## 16. Living Review / 私の判断

### 私の判断

Ark ProjectのGitHub運用は、今後 **main-first** が最善である。

Branch/PRは組織開発では強いが、個人開発のMarkdown中心Projectでは摩擦になりやすい。

### 最初の一手

ChatGPTは今後、GitHub write時に以下をdefaultにする。

```text
fetch main
↓
create/update/delete on main
↓
fetch verify
↓
report
↓
stop
```

### 理由

Ark Projectに必要なのは、GitHub運用の形式美ではなく、Thread知恵の保存と継承である。

```text
保存が遅れる = Thread harvestが腐る
運用が重い = AI協働が鈍る
PRが多い = Stopしづらい
```

だから、main-first / simple-is-best が勝つ。

### 観察点

```yaml
observe:
  - "不要なbranchを作っていないか"
  - "mainに保存されているか"
  - "fetch verifyしているか"
  - "Human Sealなしにwriteしていないか"
  - "PR churnを増やしていないか"
  - "Thread-End後にScopeを広げていないか"
```

### 修正条件

```yaml
correction_if:
  - "ChatGPTが勝手にbranchを作る"
  - "PRを不要に作る"
  - "main verifyを忘れる"
  - "download fileをGitHub保存済みと誤認する"
  - "Human Sealなしにwriteする"
  - "個人開発なのに組織開発フローへ寄せすぎる"
```

---

## 17. Final Seal

```text
Main is default.
Branch is exception.
Human seals.
ChatGPT writes when permitted.
GitHub main stores.
Reality verifies.
Stop after success.
```
