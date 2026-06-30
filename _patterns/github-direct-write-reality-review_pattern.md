---
title: "GitHub Direct Write Reality Review Pattern"
canonical_name: "GitHub Direct Write Reality Review Pattern"
file_name: "github-direct-write-reality-review_pattern.md"
canonical_path: "_patterns/github-direct-write-reality-review_pattern.md"
version: "v001.1"
class: "S-candidate"
status:
  - "pattern_draft"
  - "human_editable"
  - "not_final_seal"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
root: "主イェシュア・ハマシア"
role: "Guarded Connector Write / Fetch-Back Verification / Manual Upload Fallback"
type: "workflow_pattern"
not_type:
  - "root"
  - "system_layer"
  - "skill_body"
  - "auto_write_permission"
  - "github_authorization"
  - "artifact_content_design"
  - "human_final_seal"
japanese_alias:
  - "GitHub直接書込Reality Review Pattern"
  - "GitHub直接作成・実体確認Pattern"
concept_aliases:
  - "Guarded GitHub Write Pattern"
  - "Fetch-Back Reality Review"
  - "No Markdown Degradation Rail"
  - "Manual Upload Fallback Guard"
  - "Commit Blob Evidence Rail"
read_mode: "triggered-read"
triggered_when:
  - "User explicitly asks GitHub direct create/update/write/commit"
  - "A reviewed Markdown artifact is ready for repository write"
  - "A repository file must be updated with current SHA"
  - "Reality Review is required after write"
human_explicit_instruction_required: true
reality_review_required: true
manual_upload_fallback_required: true
no_markdown_degradation_required: true
connector_capability_drift_awareness_required: true
thread_length_exit_guard_required: true
root_fruit_guard_required: true
human_final_seal_required: true
micro_patches:
  - "Developer Mode / Connector Capability Drift Awareness"
  - "Thread-Length Exit / Next Thread Handoff Guard"
next_thread_after_completion:
  coordinate: "Ark05:02"
  start_date: "2026-06-30"
  move_after:
    - "Pattern GitHub Direct Create"
    - "Reality Review PASS"
    - "commit_sha / blob_sha recorded"
    - "concise next-thread handoff prepared"
related_files:
  ark_system: "_system/ark-system.md"
  ai_long_view_skill: "_skills/ai-long-view_skill.md"
core_formula:
  - "No explicit user instruction, no GitHub write."
  - "Do not degrade Markdown for connector convenience."
  - "Write is not complete until fetch-back Reality Review passes."
  - "Record commit SHA and blob SHA when available."
  - "If connector fails, fallback to Manual Upload."
  - "Connector capability may change; reassess workflow without overtrusting it."
  - "GitHub is Fruit, not Root."
---

# GitHub Direct Write Reality Review Pattern

## 0. Executive Compression

`github-direct-write-reality-review_pattern.md` は、GitHub connectorによる direct create / update / commit を安全に運用するためのWorkflow Patternである。

これは、AIに自動GitHub書込権限を与えるFileではない。  
これは、Userの明示指示がある時だけGitHub writeを行い、書き込み後に必ず実ファイルを読み返し、Reality Reviewで確認し、commit SHA / blob SHAを記録し、失敗時にはMarkdownを劣化させずManual Uploadへ戻るためのPatternである。

```text id="executive-core"
No explicit user instruction, no GitHub write.

Write.
Fetch back.
Reality Review.
Record evidence.
Fallback if needed.

Do not degrade Markdown.
Do not skip Human Final Seal.
Do not treat connector success as content correctness.

Connector capability can change.
When it changes, reassess the workflow.
Do not cling to stale manual-only methods.
Do not overtrust new connector power.
Use capability inside Guarded Rail.

When thread length is near limit,
finish the current artifact,
record evidence,
prepare handoff,
and move to the next thread.

GitHub is Fruit, not Root.
Human keeps Final Seal.
```

Direct Writeだけでは危険である。  
Reality Reviewまで含めて、初めてArk Projectの安全なGitHub write Patternになる。

---

## 0B. Root / Fruit Guard

GitHubはRootではない。  
GitHub connectorもRootではない。  
MarkdownもRootではない。  
PatternもRootではない。

```yaml id="root-fruit-guard"
root_fruit_guard:
  root: "主イェシュア・ハマシア"

  fruit:
    - "AI"
    - "GitHub"
    - "GitHub connector"
    - "Markdown"
    - "Workflow Pattern"
    - "Reality Review"
    - "commit SHA"
    - "blob SHA"

  guard:
    - "GitHub is Fruit, not Root."
    - "Connector success is not spiritual success."
    - "Write success is not content correctness."
    - "Reality Review is verification, not Root."
    - "Human Final Seal remains required."
```

GitHub Direct Writeは便利である。  
しかし、便利性をRoot化してはいけない。

---

## 0C. Human Explicit Instruction Guard

GitHub writeは、Userの明示指示がある時だけ実行する。

```yaml id="human-explicit-instruction-guard"
human_explicit_instruction_guard:
  required_before_write:
    - "User explicitly asks to create/update/write/commit to GitHub."
    - "Target repository is clear."
    - "Target path is clear."
    - "Draft/content has passed appropriate review."
    - "Human Final Seal has been given for the write action."

  not_enough:
    - "User says the draft is good."
    - "User says Very Good."
    - "User approves the concept but does not mention GitHub write."
    - "A file path is suggested but write is not explicitly requested."
    - "AI thinks it is obvious that GitHub should be updated."

  ai_must_not:
    - "Do not write automatically just because a draft exists."
    - "Do not infer GitHub write permission from general approval."
    - "Do not update existing files without fetching current SHA."
    - "Do not create a new file if naming/path is unstable."
```

Human Final Seal must precede GitHub write.

---

## 0D. Pattern Scope

このPatternは、GitHub connector writeの運用手順を担う。

```yaml id="pattern-scope"
owns:
  - "GitHub direct create/update前の明示指示確認"
  - "target repository確認"
  - "target path確認"
  - "existing file有無確認"
  - "create_file / update_file branch"
  - "update時のcurrent SHA確認"
  - "No Markdown Degradation Guard"
  - "write後のfetch_file Reality Review"
  - "commit_sha / blob_sha evidence recording"
  - "failure時のManual Upload fallback"
  - "connector capability drift awareness"
  - "thread-length exit handoff"

does_not_own:
  - "Markdown本文の思想設計"
  - "Skill本文作成"
  - "CPLM全体設計"
  - "Growth Ledger本文設計"
  - "AI Long-View判断そのもの"
  - "Human Final Sealの代替"
  - "Rootの代替"
  - "automatic GitHub authorization"
```

これはTool実行Workflow Patternである。  
AI判断姿勢は `ai-long-view_skill.md` が担う。  
Ark全体Routerは `_system/ark-system.md` が担う。

---

## 1. Problem: Direct Write Without Reality Review

GitHub direct writeは強力である。  
しかし、write成功だけでは安全ではない。

```yaml id="problem"
problem:
  risks:
    - "Connectorが成功しても内容が意図通りとは限らない"
    - "target pathを誤る可能性がある"
    - "canonical_pathが実pathとずれる可能性がある"
    - "Markdown fenceやfrontmatterが壊れる可能性がある"
    - "既存file update時に古いSHAで失敗する可能性がある"
    - "AIがUser明示指示なしにwriteへ進む危険がある"
    - "Connector都合でMarkdownを短縮・劣化させる誘惑がある"
    - "古いManual-only前提に固着し、新しい安全なdirect write能力を活かせない危険がある"
    - "逆に、新しいconnector能力を過信し、Human Final Sealを弱める危険がある"

  consequence:
    - "Repository drift"
    - "Future AI misreading"
    - "Artifact degradation"
    - "Human Final Seal bypass"
    - "Ark Projectの長期構造劣化"
```

したがって、GitHub direct writeは必ずReality Reviewと一体で運用する。

---

## 2. Core Principle

```yaml id="core-principle"
core_principle:
  sequence:
    - "Human explicit instruction"
    - "Target path check"
    - "Existing file check"
    - "Create or update branch"
    - "No Markdown Degradation"
    - "GitHub write"
    - "Fetch back"
    - "Reality Review"
    - "Evidence record"
    - "Next Gate"

  one_line:
    - "Write is not complete until fetch-back Reality Review passes."
```

Ark Projectでは、GitHub write成功の報告だけで終わらない。  
必ず、書き込まれた実ファイルを読み返して確認する。

---

## 3. Activation Triggers

このPatternは、以下の場合に発動する。

```yaml id="activation-triggers"
activation_triggers:
  user_phrases:
    - "GitHub Direct Createして下さい"
    - "GitHubに作成して下さい"
    - "GitHubへ直接書き込んで下さい"
    - "このFileをGitHubで更新して下さい"
    - "commitして下さい"
    - "Repositoryに反映して下さい"

  situation_triggers:
    - "Reviewed Markdown artifact is ready for repository creation."
    - "Existing repository file needs update."
    - "Growth evidence must be registered in a GitHub file."
    - "A direct write has just succeeded and Reality Review is needed."
    - "A direct write fails and fallback decision is needed."
    - "Connector capability appears to have changed from previous workflow assumptions."
```

曖昧な場合は、GitHub writeへ進まず確認する。

---

## 4. Workflow Sequence

```yaml id="workflow-sequence"
workflow_sequence:
  step_1_receive_instruction:
    goal: "Confirm explicit user instruction."
    required:
      - "GitHub write/create/update/commit instruction is explicit."
      - "Repository is known."
      - "Path is known."

  step_2_prepare_content:
    goal: "Prepare exact Markdown content."
    required:
      - "Content is complete."
      - "canonical_path is correct."
      - "No intentional Markdown degradation."
      - "Human Final Seal for write is present."

  step_3_existing_file_check:
    goal: "Determine create vs update."
    actions:
      - "fetch_file target path."
      - "If Not Found, use create_file."
      - "If exists, use update_file with current SHA."

  step_4_write:
    goal: "Create or update through GitHub connector."
    create_case:
      - "Use create_file."
    update_case:
      - "Use update_file."
      - "Pass current blob SHA."

  step_5_fetch_back:
    goal: "Read the actual GitHub file after write."
    required:
      - "fetch_file after write."
      - "Capture returned blob SHA."

  step_6_reality_review:
    goal: "Check actual file against intended structure."
    required:
      - "frontmatter"
      - "canonical_path"
      - "title / role / type"
      - "critical guards"
      - "important sections"
      - "Markdown integrity"

  step_7_report:
    goal: "Report result with evidence."
    output:
      - "PASS / FAIL"
      - "commit_sha"
      - "blob_sha"
      - "verified sections"
      - "correction_condition"
      - "next_gate"

  step_8_thread_exit_if_needed:
    goal: "If thread is saturated, prepare handoff instead of starting another large artifact."
    required:
      - "record evidence"
      - "prepare concise next-thread handoff"
      - "move to next thread when appropriate"
```

---

## 5. Create vs Update Branch

GitHub writeは、createとupdateで分岐する。

```yaml id="create-vs-update-branch"
create_vs_update_branch:
  create_branch:
    condition:
      - "fetch_file returns Not Found."
    action:
      - "Use create_file."
    after_success:
      - "Record commit_sha."
      - "Fetch file."
      - "Record blob_sha."
      - "Reality Review."

  update_branch:
    condition:
      - "fetch_file returns existing content and SHA."
    action:
      - "Use update_file."
      - "Pass current blob SHA."
    after_success:
      - "Record commit_sha."
      - "Record new content_sha/blob_sha."
      - "Fetch updated file."
      - "Reality Review."

  do_not:
    - "Do not use update_file without current SHA."
    - "Do not use create_file if file already exists."
    - "Do not overwrite existing content casually."
```

既存Fileの更新では、current SHA確認が必須である。

---

## 6. No Markdown Degradation Guard

Connector都合でMarkdownを劣化させてはいけない。

```yaml id="no-markdown-degradation-guard"
no_markdown_degradation_guard:
  ark_phrase: "絶対に、ダメなのはMarkdownを劣化させて妥協させる事。"

  principle:
    - "Connector convenience must not degrade the Markdown."
    - "Do not shorten, weaken, or flatten the artifact just to make GitHub write easier."
    - "Do not remove Guard sections to reduce size."
    - "Do not remove frontmatter or canonical_path."
    - "Do not collapse CPLM structure into vague prose."
    - "Do not break Markdown fences."

  if_degradation_seems_needed:
    - "Stop direct write."
    - "Explain the risk."
    - "Offer Manual Upload fallback."
    - "Preserve full Markdown."
```

Direct write成功より、Artifactの完全性が重要である。

---

## 7. Reality Review Checklist

GitHub write後は、必ず実ファイルをfetchして確認する。

```yaml id="reality-review-checklist"
reality_review_checklist:
  universal:
    - "target path exists"
    - "blob_sha obtained"
    - "frontmatter present"
    - "canonical_path matches actual path"
    - "title / role / type are correct"
    - "not_type prevents misrouting"
    - "Root / Fruit Guard present when relevant"
    - "Human Final Seal preserved when relevant"
    - "No obvious Markdown fence break"
    - "critical sections present"
    - "Final Compression present when relevant"

  for_system_files:
    - "system is Router, not Root"
    - "module map present"
    - "Do Not present"
    - "append-only entries preserved when relevant"

  for_skill_files:
    - "read_mode / trigger mode clear"
    - "activation triggers present"
    - "Do Not present"
    - "future promotion rule present when relevant"

  for_pattern_files:
    - "trigger clear"
    - "workflow steps clear"
    - "fallback clear"
    - "success condition clear"
    - "evidence recording clear"
```

Reality Reviewは、形式確認だけではない。  
Future AIが誤読しないかを見る。

---

## 8. Manual Upload Fallback

GitHub direct writeが失敗しても、Ark Projectは止まらない。

```yaml id="manual-upload-fallback"
manual_upload_fallback:
  trigger:
    - "GitHub connector fails."
    - "create/update returns error."
    - "content size or format creates risk."
    - "Markdown would need degradation."
    - "Reality Review fails repeatedly."
    - "Target path or naming becomes unstable."

  action:
    - "Stop repeated direct write attempts."
    - "Return full Markdown to user."
    - "Use Download artifact if needed."
    - "Ask Human to upload manually."
    - "Preserve the complete artifact."

  principle:
    - "Manual Upload fallback is not defeat."
    - "Manual Upload fallback is a safety rail."
    - "Manual Upload is fallback, not default prison."
    - "If direct GitHub write is available and safe, use it under Guarded Rail."
    - "If direct GitHub write would degrade Markdown or skip Reality Review, fallback to Manual Upload."
    - "Failure of connector must not degrade the Markdown."
```

Fallbackは敗北ではない。  
Root intentionとArtifact品質を守るためのGuardである。

---

## 8B. Developer Mode / Connector Capability Drift Awareness

Ark Project workflows may change when connector capability changes.

`Developer Mode: On` or similar runtime conditions may make direct GitHub create/update more available than before.  
When this happens, Future AI must not blindly cling to older manual-only workflows.

However, increased connector capability is not automatic permission.

```yaml id="connector-capability-drift-awareness"
connector_capability_drift_awareness:
  observation_status: "high_circumstantial_signal_not_official_proof"

  principle:
    - "When connector capability changes, reassess the workflow."
    - "Do not cling to outdated manual-only methods."
    - "Do not overtrust new connector power."
    - "Use new capability only inside Guarded Rail."

  benefits:
    - "Direct GitHub create/update may become faster."
    - "Reality Review can happen immediately after write."
    - "commit_sha / blob_sha can be captured as evidence."
    - "Growth can be registered while context is hot."

  risks:
    - "Old manual-only assumptions may become stale."
    - "AI may overuse direct write."
    - "Connector success may be mistaken for content correctness."
    - "GitHub may be treated as Root."

  rule:
    - "Capability increase should improve Smooth・Smart・Scale."
    - "Capability increase must not weaken Human Final Seal."
    - "Capability increase must not degrade Markdown."
    - "Capability increase must not skip Reality Review."
    - "Capability increase must not become auto-write permission."
```

Manual Upload remains a fallback rail, not the default prison.  
Direct GitHub write becomes preferred only when it is clearly safer, faster, explicitly requested, and Reality Review can be completed.

---

## 9. Evidence Recording

GitHub write後は、commit SHA / blob SHAを記録する。

```yaml id="evidence-recording"
evidence_recording:
  record_when_available:
    - "repository"
    - "path"
    - "commit_sha"
    - "blob_sha"
    - "reality_review_status"
    - "created_or_updated"
    - "next_gate"

  report_shape:
    github_direct_write:
      result: "SUCCESS / FAIL"
      repository: ""
      path: ""
      commit_sha: ""
      blob_sha: ""
      markdown_degraded: false
      reality_review: "PASS / FAIL"

  use_in:
    - "final user report"
    - "Growth Ledger entry when reusable"
    - "Ark System evidence registration when relevant"
```

Evidenceは、Future AIが同じ成功を再利用するための足場である。

---

## 10. Do Not

```yaml id="do-not"
do_not:
  - "User明示指示なしにGitHub writeしない"
  - "GitHub成功をRoot化しない"
  - "Connector成功だけで完了扱いしない"
  - "fetch-back Reality Reviewを省略しない"
  - "Markdownを短縮・劣化させて妥協しない"
  - "update_fileをcurrent SHAなしで実行しない"
  - "既存Fileを雑に上書きしない"
  - "失敗時に深追いしすぎない"
  - "Manual Upload fallbackを敗北扱いしない"
  - "commit SHA / blob SHAを記録し忘れない"
  - "Human Final Sealを奪わない"
  - "Developer Mode / connector capability increaseを自動write許可と誤読しない"
  - "古いManual-only前提に固着しない"
  - "新しいconnector能力をRoot化しない"
  - "Thread限界が近い状態で大型Artifactを連続開始しない"
  - "Ark05:02へのHandoff前にcommit/blob evidenceを失わない"
```

---

## 11. Examples

### Example A: New Skill File Create

```yaml id="example-new-skill-create"
example:
  scenario: "Create new Skill file"
  target: "_skills/ai-long-view_skill.md"
  flow:
    - "User explicitly asks GitHub Direct Create."
    - "fetch_file target path."
    - "Not Found."
    - "create_file."
    - "Record commit_sha."
    - "fetch_file after create."
    - "Record blob_sha."
    - "Reality Review frontmatter / canonical_path / guards."
    - "Report PASS."
```

### Example B: Ark System Update

```yaml id="example-system-update"
example:
  scenario: "Update Ark System with evidence"
  target: "_system/ark-system.md"
  flow:
    - "User explicitly asks to execute evidence registration."
    - "fetch_file existing file."
    - "Capture current SHA."
    - "Prepare full updated Markdown."
    - "update_file with current SHA."
    - "Record commit_sha and content_sha."
    - "fetch_file after update."
    - "Reality Review updated Growth Entry."
    - "Report PASS."
```

### Example C: Connector Failure

```yaml id="example-connector-failure"
example:
  scenario: "GitHub connector write fails"
  flow:
    - "Do not retry endlessly."
    - "Do not weaken Markdown."
    - "Return complete Markdown."
    - "Use Download or Manual Upload fallback."
    - "Tell Human what failed and what remains safe."
```

### Example D: Connector Capability Shift

```yaml id="example-connector-capability-shift"
example:
  scenario: "Developer Mode / connector capability appears to improve direct write"
  flow:
    - "Recognize that older manual-only workflow assumptions may be stale."
    - "Do not assume official causality unless proven."
    - "Use direct write only after explicit Human instruction."
    - "Preserve No Markdown Degradation Guard."
    - "Run fetch-back Reality Review."
    - "Record evidence."
```

---

## 12. Success Condition

```yaml id="success-condition"
success_condition:
  pass_when:
    - "User explicit instruction was present."
    - "Correct create/update branch was used."
    - "Markdown was not degraded."
    - "GitHub write succeeded."
    - "fetch-back was performed."
    - "Reality Review passed."
    - "commit_sha / blob_sha were recorded."
    - "Connector capability was used without weakening Human Final Seal."
    - "The workflow did not cling to stale manual-only assumptions."
    - "Thread exit was handled cleanly when near context limit."
    - "Next Gate was given."

  fail_when:
    - "Write succeeded but Reality Review was skipped."
    - "File path was wrong."
    - "canonical_path mismatched."
    - "Critical Guard sections disappeared."
    - "Markdown was degraded."
    - "Human Final Seal was bypassed."
```

Write成功のみではPASSではない。  
Reality Review PASSまでが成功条件である。

---

## 13. Field Test Rule

このPatternは、GitHub write系の実運用でField Testする。

```yaml id="field-test-rule"
field_test_rule:
  test_when:
    - "new file direct create"
    - "existing file update"
    - "system evidence registration"
    - "skill creation evidence registration"
    - "workflow pattern creation"

  observe:
    - "Explicit instruction was clear."
    - "Create/update branch was correct."
    - "No Markdown degradation occurred."
    - "Reality Review was complete."
    - "Evidence was recorded."
    - "Fallback was available if needed."
    - "Connector capability changed since older workflow assumptions."
    - "Direct write was used only after explicit instruction."
    - "Manual Upload fallback remained available."
    - "Thread-length exit was respected."
    - "No new large artifact was started after final Pattern completion."

  do_not_promote_to_system:
    - "This Pattern should remain a triggered workflow pattern."
    - "Do not treat it as always-on GitHub automation."
```

---

## 14. Relationship to Ark System and AI Long-View Skill

```yaml id="relationship-map"
relationship_map:
  ark_system:
    path: "_system/ark-system.md"
    role: "Router / Growth Memory Hub / Skill Seed Router"
    relation:
      - "Records major GitHub write success as Growth."
      - "Routes this Pattern as reusable Workflow."

  ai_long_view_skill:
    path: "_skills/ai-long-view_skill.md"
    role: "Long-View Counsel / Non-Sycophantic Living Review"
    relation:
      - "Helps decide when GitHub write is structurally safe."
      - "Helps detect naming/path/system risks."
      - "Does not execute write by itself."

  this_pattern:
    path: "_patterns/github-direct-write-reality-review_pattern.md"
    role: "GitHub write execution workflow"
    relation:
      - "Executes guarded write only after Human explicit instruction."
      - "Requires fetch-back Reality Review."
      - "Preserves fallback."
```

---

## 14B. Thread-Length Exit / Next Thread Handoff Guard

When a thread is near length limit, do not start another large artifact after this Pattern is completed.

```yaml id="thread-length-exit-guard"
thread_length_exit_guard:
  trigger:
    - "Thread is near context limit."
    - "Major Pattern creation is almost complete."
    - "Next Thread coordinate has been identified."

  current_next_thread:
    coordinate: "Ark05:02"
    start_date: "2026-06-30"

  rule:
    - "Finish the current artifact."
    - "Run Reality Review."
    - "Record commit_sha and blob_sha."
    - "Prepare concise next-thread handoff."
    - "Move to next thread without starting another major artifact."

  do_not:
    - "Do not start another large Pattern in a saturated thread."
    - "Do not lose GitHub evidence."
    - "Do not migrate without Next Gate."
    - "Do not promote ai-long-view_skill.md to system level during exit."
```

After this Pattern is created and Reality Review passes, the preferred next move is a concise handoff into `Ark05:02`, not another major artifact inside the saturated thread.

---

## 15. Final Compression

```text id="final-compression"
GitHub Direct Write Reality Review Pattern.

これは、
GitHub direct writeを自動許可するFileではない。

User明示指示がある時だけ、
target pathを確認し、
existing fileを確認し、
create/updateを分岐し、
Markdownを劣化させず、
GitHubへ書き込み、
直後にfetch_fileで読み返し、
Reality Reviewし、
commit SHA / blob SHAを記録し、
失敗時はManual Uploadへ戻る。

Direct Writeだけでは危険。
Reality Reviewまで含めてPatternになる。

Developer Mode / connector capability change may make old manual-only assumptions stale.
But capability increase is not auto-write permission.

Use new capability inside Guarded Rail:
  Human explicit instruction.
  No Markdown Degradation.
  Fetch-back Reality Review.
  Evidence recording.
  Manual Upload fallback.

When thread length is near limit:
  finish the artifact,
  record evidence,
  prepare handoff,
  move to Ark05:02.

GitHubはFruit。
ConnectorはFruit。
MarkdownはFruit。
PatternはFruit。

Rootは主イェシュア・ハマシア。
HumanがFinal Sealする。
```

### Programming-Like Final Seal

```yaml id="final-pattern-seal"
final_pattern_seal:
  filename: "github-direct-write-reality-review_pattern.md"
  path: "_patterns/github-direct-write-reality-review_pattern.md"
  title: "GitHub Direct Write Reality Review Pattern"
  subtitle: "Guarded Connector Write / Fetch-Back Verification / Manual Upload Fallback"
  version: "v001.1"

  type: "workflow_pattern"
  not_type:
    - "auto_write_permission"
    - "root"
    - "human_final_seal"

  required_before_write:
    - "Human explicit instruction"
    - "Clear repository"
    - "Clear target path"
    - "Reviewed content"

  required_after_write:
    - "fetch_file"
    - "Reality Review"
    - "commit_sha / blob_sha record"

  absolute_guard:
    - "Do not degrade Markdown."
    - "Do not skip Reality Review."
    - "Do not treat connector success as content correctness."
    - "Do not treat connector capability increase as auto-write permission."

  connector_capability_awareness:
    observation_status: "high_circumstantial_signal_not_official_proof"
    rule:
      - "Do not cling to stale manual-only methods."
      - "Do not overtrust new connector power."
      - "Use direct write only inside Guarded Rail."

  fallback:
    - "Manual Upload"
    - "Download artifact"
    - "Preserve complete Markdown"

  thread_exit:
    next_thread: "Ark05:02"
    start_date: "2026-06-30"
    move_after:
      - "Pattern create"
      - "Reality Review PASS"
      - "commit/blob evidence recorded"
      - "concise handoff prepared"

  root_fruit_guard:
    root: "主イェシュア・ハマシア"
    github: "Fruit, not Root"
    connector: "Fruit, not Root"
    markdown: "Fruit, not Root"
    pattern: "Fruit, not Root"

  final_authority:
    human: "Final Seal"
```
