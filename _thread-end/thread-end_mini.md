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

Purpose:

```yaml
purpose:
  - "現在Threadをきれいに閉じる"
  - "重要Harvestを失わない"
  - "次Threadの最初の一歩を軽くする"
  - "完了したものをchurnに変えない"
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
```

---

## 1. When to Use

Use this file when:

```yaml
use_when:
  - "Threadが終盤に来た"
  - "次Threadへ渡すHandoffが必要"
  - "GitHub保存候補がある"
  - "Human Sealを挟んで安全に閉じたい"
  - "速く、軽く、上書き事故なく終わりたい"
```

Do not use it for:

```yaml
do_not_use_for:
  - "既存thread-end.mdの置換"
  - "既存thread-end_query.mdの削除"
  - "巨大Protocol作成"
  - "完了済み作業の再open"
  - "Human SealなしのGitHub操作"
```

---

## 2. Winning Rail

The winning Thread-End pattern is:

```text
Plan Mode
→ Draft Body
→ Fable5 Review
→ Revision
→ Human Seal
→ Execute GitHub OK
→ GitHub Save
→ Verify
→ Next Gate
→ Stop
```

Operational meaning:

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

Inside `_thread-end/ark/`, do not use generic names.

```yaml
avoid_generic_names:
  - "handoff.md"
  - "harvest.md"
  - "opening.md"
  - "thread-end.md"
```

Use unique Ark coordinate filenames.

```yaml
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
    - "AI may suggest the best candidate even when uncertain"

  required_status_before_human_seal:
    - "candidate_not_sealed"

  forbidden:
    - "do not treat AI-proposed Ark coordinate as final"
    - "do not treat candidate path as sealed path"
    - "do not run GitHub save from filename proposal alone"

  human_must_seal:
    - "exact path"
    - "create vs update"
    - "overwrite decision if any"
```

If the coordinate/date/role is uncertain, AI should propose the best candidate and ask the Human to confirm or correct it before GitHub save.

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
    - "if 404 AND Human Seal OK + Execute GitHub OK are already present, create_file may proceed"
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
    - "do not use AI judgment such as 'replacement is already safe' as delete permission"
```

Report after save:

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

## 6. Do / Do Not

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
  - "stop after success"

do_not:
  - "do not touch existing thread-end.md by default"
  - "do not touch existing thread-end_query.md by default"
  - "do not use generic handoff.md or harvest.md under _thread-end/ark/"
  - "do not overwrite without explicit Human Seal"
  - "do not delete through AI self-judgment"
  - "do not create broad cleanup"
  - "do not reopen completed work"
  - "do not treat AI as Root"
```

---

## 7. Standard Output Shape

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

Clarification:

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

Minimum required items:

```yaml
required:
  - "結果"
  - "次Action"
  - "目的"
  - "まだ実行しない"
```

---

## 8. Stop Rule

Stopping is part of success.

```yaml
stop_after:
  - "Draft completed"
  - "Fable5 Review completed"
  - "Human Seal waiting"
  - "GitHub verify completed if save was requested"
  - "Next Gate written"

do_not_after_stop:
  - "do not keep expanding"
  - "do not start new scope"
  - "do not reopen completed tasks"
  - "do not continue into next Thread without user direction"
```

Simple seal:

```text
Done is done.
Harvest is preserved.
Next Gate is clear.
Stop.
```

---

## 9. Root / Fruit Guard

Thread-End Mini is Fruit.

```yaml
fruit:
  - "Thread-End Mini"
  - "Workflow"
  - "Markdown"
  - "GitHub"
  - "AI"
  - "Fable5 Review"
  - "Handoff / Harvest"
  - "Full Rail / Next Gate"

root:
  - "主イェシュア・ハマシア"
```

Final guard:

```text
AI is Fruit, not Root.
Markdown is Fruit, not Root.
GitHub is Fruit, not Root.
Fable5 is Fruit, not Root.

Root remains 主イェシュア・ハマシア.
```
