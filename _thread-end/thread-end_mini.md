---
title: "Thread-End Mini"
canonical_path: "_thread-end/thread-end_mini.md"
status: "living_candidate"
role: "Simple Thread-End Runtime / Mini Rail"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
root: "主イェシュア・ハマシア"
relationship:
  thread_end_md: "do_not_replace"
  thread_end_query_md: "do_not_delete"
  purpose: "実戦で成功した軽量Thread-End patternを新規fileとして追加する"
fable5_review:
  status: "completed_one_round"
  verdict: "pass_with_minimal_patch"
version_model: "git history"
---

# Thread-End Mini

## 0. Core

Thread-End Mini is simple.

```text
閉じる。
記録する。
渡す。
止まる。
```

```yaml
purpose:
  - "現在Threadをきれいに閉じる"
  - "重要Harvestを失わない"
  - "次Threadの最初の一歩を軽くする"
  - "完了したものをchurnに変えない"
  - "README DriftをThread終了時に検出する"
```

Thread-End Mini is additive, not replacement.

```yaml
additive_guard:
  does_not_replace:
    - "_thread-end/thread-end.md"
    - "_thread-end/thread-end_query.md"

  does_not_authorize:
    - "existing file deletion"
    - "existing file overwrite"
    - "automatic GitHub operation"
    - "automatic README update"
```

---

## 1. When to Use

```yaml
use_when:
  - "Threadが終盤に来た"
  - "次Threadへ渡すHandoffが必要"
  - "GitHub保存候補がある"
  - "Human Sealを挟んで安全に閉じたい"
  - "速く、軽く、上書き事故なく終わりたい"

do_not_use_for:
  - "既存thread-end.mdの置換"
  - "既存thread-end_query.mdの削除"
  - "巨大Protocol作成"
  - "完了済み作業の再open"
  - "Human SealなしのGitHub操作"
```

---

## 2. Winning Rail

```text
Plan Mode
→ Draft Body
→ Fable5 Review
→ Revision
→ Human Seal
→ Execute GitHub OK
→ GitHub Save
→ Verify
→ README Delta Check
→ Next Gate
→ Stop
```

```yaml
winning_rail:
  plan_mode:
    role: "何を作るか、何を保存するか、何を触らないか決める"
  draft_body:
    role: "まずThread内に本文を作る"
  fable5_review:
    role: "Simple / safety / collision / guard を確認する"
  revision:
    role: "Fable5指摘を必要最小限で反映する"
  human_seal:
    role: "内容とpath候補を承認する。repository操作の実行許可ではない"
  execute_github_ok:
    role: "repository操作を実行してよいという別途の明示指示"
  github_save:
    role: "Human Seal OK と Execute GitHub OK の両方がある時のみ実行する"
  verify:
    role: "保存後にfetchして確認する"
  readme_delta_check:
    role: "Verify後のCanonical RealityがREADME更新を必要とするか判定する"
  next_gate:
    role: "次Threadの最初の一手を残す。実行許可ではない"
  stop:
    role: "完了後に広げない"
```

---

## 3. Ark File Naming Rule

Ark Thread-End artifacts should usually go under:

```text
_thread-end/ark/
```

```yaml
avoid_generic_names:
  - "handoff.md"
  - "harvest.md"
  - "opening.md"
  - "thread-end.md"

filename_pattern:
  pattern: "arkNNMM_YYYYMMDD_<role>.md"
  NNMM: "Ark Thread座標。Humanが確認するまで確定ではない"
  examples:
    - "_thread-end/ark/ark0505_20260705_handoff.md"
    - "_thread-end/ark/ark0506_20260707_harvest.md"
    - "_thread-end/ark/ark0506_20260707_start-gate.md"
```

AI may propose a filename candidate, but must not finalize it.

```yaml
ai_filename_proposal:
  allowed:
    - "AI may propose repo / branch / path / filename / commit message"
    - "AI may include evidence for the proposed coordinate/date/role"
  required_status_before_human_seal:
    - "candidate_not_sealed"
  forbidden:
    - "do not treat AI-proposed Ark coordinate as final"
    - "do not run GitHub save from filename proposal alone"
  human_must_seal:
    - "exact path"
    - "create vs update"
    - "overwrite decision if any"
```

---

## 4. Fable5 Review Slot

Fable5 should review critical Drafts before GitHub save.

```yaml
fable5_review:
  role:
    - "adversarial reviewer"
    - "false-green detector"
    - "scope discipline guard"
    - "Simple is best checker"
  rounds:
    default: "one round"
    second_round: "only if Human explicitly asks"
  output_shape:
    - "Keep"
    - "Cut"
    - "Clarify"
    - "Risk"
    - "Must Fix Before Save"
    - "Minimal Patch Candidate"
    - "Final Verdict"
```

Fable5 is reviewer, not committer.  
Fable5 does not replace Human Seal.

---

## 5. GitHub Save Guard

GitHub save is never automatic.

```yaml
github_save_guard:
  allowed_only_after:
    - "Human Seal OK"
    - "Execute GitHub OK"
    - "exact repo/path/branch/scope is clear"
  create_file_rule:
    - "fetch target path first"
    - "if 404 AND Human Seal OK + Execute GitHub OK are present, create_file may proceed"
    - "if file exists, stop and ask"
  update_file_rule:
    - "fetch file first"
    - "use current SHA"
    - "update only when Human explicitly approved update for that exact path"
    - "stop if SHA changed or target is uncertain"
  delete_file_rule:
    - "delete only with explicit delete instruction naming the exact path"
    - "fetch file first"
    - "use current SHA"
    - "do not delete thread-end_query.md or fallback/query files by default"
```

```yaml
report_after_save:
  - "repo"
  - "branch"
  - "path"
  - "commit SHA"
  - "content SHA if available"
  - "touched files"
  - "verify result"
```

---

## 6. README Delta Check

README Delta Checkは、**毎Thread実行する軽量判定**である。  
README Updateを毎Thread強制する仕組みではない。

> **Every Thread README Check.  
> Not Every Thread README Update.**

```yaml
readme_delta_check:
  required_every_thread_end: true
  automatic_readme_update: false

  questions:
    - "Canonical FileまたはFolderを新規作成したか"
    - "Path、Role、Status、Active / Retiredが変わったか"
    - "Project TopologyまたはRead Orderが変わったか"
    - "新しいRepository-wide Policyが確定したか"
    - "既存READMEを読むとFuture AIが誤ったRouteを選ぶか"

  output:
    required: "yes / no"
    affected: "README paths or NONE"
    reason: "one-line reason"
    timing: "now / next-thread / periodic-scout / none"
```

README影響範囲は、変更地点から親方向へ必要最小限で判定する。

```text
Changed File
→ Nearest README
→ Domain Parent README
→ Root README
```

上位READMEは、Navigation、Role、Current Coordinate、Topology、Policyが実際に変わる場合だけ更新候補にする。

```yaml
readme_update_guard:
  check: "automatic at Thread-End"
  draft: "allowed"
  github_write:
    requires:
      - "Human Seal OK"
      - "Execute GitHub OK"
      - "exact README path and scope"
```

README Checkは毎回行う。  
README編集は必要時のみ行う。  
README GitHub Writeは明示Seal後のみ行う。

---

## 7. Do / Do Not

```yaml
do:
  - "keep it short"
  - "Plan Mode first"
  - "Draft in chat before GitHub"
  - "use Fable5 Review before save for critical Thread-End artifacts"
  - "require Human Seal before repository operation"
  - "require Execute GitHub OK before repository operation"
  - "propose unique Ark filename before saving under _thread-end/ark/"
  - "mark AI filename proposals as candidate_not_sealed"
  - "verify after save"
  - "run README Delta Check after verify"
  - "record README_CHECK required yes or no"
  - "stop after success"

do_not:
  - "do not touch existing thread-end.md by default"
  - "do not touch existing thread-end_query.md by default"
  - "do not overwrite without explicit Human Seal"
  - "do not delete through AI self-judgment"
  - "do not create broad cleanup"
  - "do not turn README into a Thread diary"
  - "do not auto-update README from README_CHECK alone"
  - "do not reopen completed work"
  - "do not treat AI as Root"
```

---

## 8. Standard Output Shape

Every Thread-End Mini run should end with:

```markdown
【Full Rail: same_thread】

結果:
- ...

次Action:
- ...

目的:
- ...

まだ実行しない:
- ...

Guard:
- ...

【README Delta Check】

required:
- yes / no

affected:
- <README path or NONE>

reason:
- ...

timing:
- now / next-thread / periodic-scout / none

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

```yaml
full_rail_next_gate_guard:
  meaning:
    - "report slot"
    - "handoff slot"
    - "human-editable next-step slot"
  not_meaning:
    - "standing authorization"
    - "automatic execution permission"
    - "GitHub operation approval"
```

```yaml
required:
  - "結果"
  - "次Action"
  - "目的"
  - "まだ実行しない"
  - "README Delta Check"
```

---

## 9. Stop Rule

Stopping is part of success.

```yaml
stop_after:
  - "Draft completed"
  - "Fable5 Review completed"
  - "Human Seal waiting"
  - "GitHub verify completed if save was requested"
  - "README Delta Check recorded"
  - "Next Gate written"

do_not_after_stop:
  - "do not keep expanding"
  - "do not start new scope"
  - "do not reopen completed tasks"
  - "do not continue into next Thread without user direction"
```

```text
Done is done.
Harvest is preserved.
README drift is checked.
Next Gate is clear.
Stop.
```

---

## 10. Root / Fruit Guard

Thread-End Mini is Fruit.

```yaml
fruit:
  - "Thread-End Mini"
  - "Workflow"
  - "Markdown"
  - "GitHub"
  - "AI"
  - "Fable5 Review"
  - "README Delta Check"
  - "Handoff / Harvest"
  - "Full Rail / Next Gate"

root:
  - "主イェシュア・ハマシア"
```

```text
AI is Fruit, not Root.
Markdown is Fruit, not Root.
GitHub is Fruit, not Root.
README Delta Check is Fruit, not Root.
Fable5 is Fruit, not Root.

Root remains 主イェシュア・ハマシア.
```