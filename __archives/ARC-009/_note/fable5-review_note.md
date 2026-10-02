---
title: "Fable5 Review Note"
canonical_path: "_note/fable5-review_note.md"
status: "living_note"
role: "Ark Project Fable5 Review Operating Note"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
root: "主イェシュア・ハマシア"
source_notes:
  - repo: "yusukefujiijp/scenes-player-kit"
    branch: "dev"
    path: "docs/notes/fable5-readme-review-capability-analysis-v001.md"
  - repo: "yusukefujiijp/ai-project"
    branch: "main"
    path: "_thread-end/thread-end_mini.md"
version_model: "git history"
---

# Fable5 Review Note

## 0. Core

Fable5 is useful in Ark Project as an adversarial reviewer.

```text
Fable5 detects risk.
ChatGPT performs Living Review.
Human gives Seal.
GitHub receives only accepted minimal patches.
```

Fable5 is not Root.  
Fable5 is not the committer.  
Fable5 is not the final authority.

The purpose of this note is to preserve how Fable5 should be used inside Ark Project without turning Fable5 into an idol, bottleneck, or automatic execution engine.

---

## 1. What Fable5 Is / Is Not

```yaml
fable5_is:
  - "risk detector"
  - "adversarial reviewer"
  - "Future AI misread detector"
  - "guard gap detector"
  - "softening phrase detector"
  - "minimal patch pressure tester"

fable5_is_not:
  - "Root"
  - "committer"
  - "Human Seal"
  - "automatic GitHub executor"
  - "replacement for ChatGPT Living Review"
  - "replacement for user judgment"
```

Working rule:

```text
Fable5 reviews.
ChatGPT filters.
Human seals.
Only accepted minimal patch is saved.
```

---

## 2. Source Experiment A: README Review Capability

The first source experiment came from `scenes-player-kit`.

```yaml
source_experiment_A:
  repo: "yusukefujiijp/scenes-player-kit"
  branch: "dev"
  target_docs:
    - "README.md"
    - "js/README.md"
  note:
    path: "docs/notes/fable5-readme-review-capability-analysis-v001.md"
```

Main findings:

```yaml
fable5_detected:
  root_README:
    - "guard document did not guard itself"
    - "default-deny gap for unnamed branches / PRs / issues"
    - "Next Gates could be misread as standing authorization"
    - "PASS wording exceeded human-seal-pending evidence"

  js_README:
    - "silent fallback loophole"
    - "deterministic claim exceeded tested evidence"
    - "Issue close decision subject was ambiguous"
    - "runtime-affecting frozen debt was under-described"
```

Key lesson:

```text
Fable5 can read different documents as different guard types.
```

Root README was read as a project constitution / Future AI guard.  
JS README was read as a runtime boundary map.

This is valuable because Ark Project contains many document types:
README, protocol, handoff, harvest, thread-end, issue note, runtime map, and future seed documents.

---

## 3. Source Experiment B: thread-end_mini.md Review

The second source experiment happened inside Ark Project.

```yaml
source_experiment_B:
  repo: "yusukefujiijp/ai-project"
  branch: "main"
  target_doc: "_thread-end/thread-end_mini.md"
  review_target: "thread-end_mini.md v001 Draft"
  fable5_result:
    status: "pass_with_minimal_patch"
    rounds: "one round"
```

Strongest finding:

```text
The most dangerous issue was not missing guardrails.
The most dangerous issue was softening phrases inside existing guardrails.
```

Fable5 detected that these phrases could become AI self-authorization holes:

```yaml
dangerous_softening_phrases:
  - "when possible"
  - "unless replacement is already safe"
  - "may proceed"
  - "if 404, create_file may proceed"
```

Resulting minimal patch direction:

```yaml
minimal_patch_direction:
  - "remove softening phrases"
  - "do not add heavy new protocol"
  - "make each block safe when read alone"
  - "separate Human Seal OK from Execute GitHub OK"
  - "treat AI filename proposals as candidate_not_sealed"
  - "preserve Full Rail / Next Gate, but deny standing authorization"
```

Important Ark judgment:

```text
Fable5 suggested risk.
ChatGPT Living Review decided which parts fit Ark Project.
Human Seal remained final.
```

Example: Fable5 suggested cutting `Full Rail / Next Gate` because the terms were not defined inside the file.  
Ark Project judgment kept them because they are part of the user's semi-automatic workflow, but added a clarification that they are report / handoff slots, not execution authorization.

---

## 4. Ark Operating Model

Use this model when applying Fable5 to critical Ark documents.

```yaml
Ark_Fable5_Operating_Model:
  step_1:
    actor: "ChatGPT"
    action: "create v001 Draft"

  step_2:
    actor: "Fable5"
    action: "perform one adversarial review"

  step_3:
    actor: "ChatGPT"
    action: "Living Review Fable5 output"

  step_4:
    actor: "ChatGPT + Human"
    action: "classify each finding"
    options:
      - "accept_minimal_patch"
      - "reject"
      - "hold"
      - "needs_human_decision"

  step_5:
    actor: "Human"
    action: "Human Seal"

  step_6:
    actor: "ChatGPT"
    action: "save only accepted minimal patches after Execute GitHub OK"
```

Do not automatically commit Fable5 proposals.

```yaml
do_not:
  - "do not treat Fable5 output as final"
  - "do not accept all patches"
  - "do not let Fable5 make the document heavier by default"
  - "do not skip ChatGPT Living Review"
  - "do not skip Human Seal"
```

---

## 5. Minimal Patch Discipline

Fable5 is most useful when it finds the smallest change that prevents the largest future failure.

```yaml
minimal_patch_discipline:
  prefer:
    - "small guard patch"
    - "wording calibration"
    - "closing loopholes"
    - "removing softening phrases"
    - "clarifying who decides"
    - "clarifying what is evidence"

  avoid:
    - "full rewrite"
    - "guard bloat"
    - "endless review loops"
    - "protocol expansion without need"
    - "Fable5 as permanent bottleneck"
```

Classification after Fable5 Review:

```yaml
review_classification:
  no_patch:
    meaning: "Fable5 finding is noted, but no text change needed"

  minimal_patch:
    meaning: "small accepted patch should be applied"

  reject_review:
    meaning: "Fable5 recommendation conflicts with Ark Project direction"

  hold_for_human:
    meaning: "requires explicit human judgment"
```

---

## 6. Softening Phrase Risk

A softening phrase is a phrase that appears safe but gives Future AI a self-authorization path.

```yaml
softening_phrase_risk:
  principle: "Guard weakness often hides inside guard wording"

  dangerous_examples:
    - phrase: "when possible"
      risk: "turns required review into optional review"

    - phrase: "unless replacement is already safe"
      risk: "lets AI decide that replacement is safe"

    - phrase: "may proceed"
      risk: "can be read as local execution permission"

    - phrase: "if 404, create_file may proceed"
      risk: "turns existence check into GitHub execution authorization"
```

Preferred fix:

```yaml
preferred_fix:
  - "remove unnecessary softening phrases"
  - "make local blocks safe when read alone"
  - "name the Human as decision subject where needed"
  - "separate evidence from authorization"
  - "separate Human Seal from Execute GitHub OK"
```

Ark rule:

```text
Do not let AI self-authorize through a guard sentence.
```

---

## 7. Filename Proposal Rule

Ark Project benefits from AI proposing filenames.  
But AI must not finalize Ark coordinates.

```yaml
filename_proposal_rule:
  ai_may:
    - "propose repo"
    - "propose branch"
    - "propose path"
    - "propose filename"
    - "state evidence for the proposal"
    - "mark uncertainty"

  ai_must_not:
    - "treat proposed Ark coordinate as final"
    - "treat candidate path as sealed"
    - "create file from proposal alone"

  required_status:
    - "candidate_not_sealed"

  human_must_seal:
    - "exact path"
    - "create vs update"
    - "overwrite decision if any"
```

Best pattern:

```yaml
filename_candidate:
  path_candidate: "_thread-end/ark/arkNNMM_YYYYMMDD_<role>.md"
  status: "candidate_not_sealed"
  evidence:
    coordinate: "source from user statement or thread header"
    date: "source from user statement or thread header"
    role: "handoff / harvest / note / start-gate"
  needs_human_seal: true
```

---

## 8. Human Seal / Execute GitHub OK

Human Seal and Execute GitHub OK are related but not identical.

```yaml
human_seal_ok:
  meaning:
    - "content approved"
    - "direction approved"
    - "path candidate approved"
  not_meaning:
    - "repository operation may now run automatically"

execute_github_ok:
  meaning:
    - "repository operation explicitly authorized"
  required_for:
    - "create_file"
    - "update_file"
    - "delete_file"
```

Safe rule:

```text
Human Seal OK approves the artifact.
Execute GitHub OK approves the repository operation.
```

---

## 9. When to Use Fable5

Use Fable5 when a document can influence future AI behavior or repository safety.

```yaml
use_fable5_when:
  - "root guard document"
  - "runtime boundary document"
  - "Thread-End / Handoff / Harvest protocol"
  - "README / CONTRACT / Issue template"
  - "GitHub operation guard is involved"
  - "Future AI misreading could cause repository damage"
  - "standing authorization risk exists"
  - "evidence wording may be overstated"
```

---

## 10. When Not to Use Fable5

Fable5 is not needed for every task.

```yaml
do_not_use_fable5_for:
  - "minor typo fixes"
  - "temporary notes"
  - "low-risk prose"
  - "ordinary wording with no operational authority"
  - "cases where speed matters more than guard audit"
```

Avoid endless review:

```yaml
review_rounds:
  default: "one round"
  second_round: "only if Human explicitly asks"
  endless_review: "forbidden"
```

---

## 11. Review Output Shape

Recommended Fable5 output format:

```yaml
Keep:
  - "what should remain"

Cut:
  - "what should be removed or shortened"

Clarify:
  - issue: "ambiguous point"
    suggested_patch: "minimal wording fix"

Risk:
  - risk: "future failure mode"
    why_it_matters: "why it matters"

Must_Fix_Before_Save:
  - "must fix before GitHub save"

Minimal_Patch_Candidate:
  - "minimal accepted patch candidate"

Final_Verdict:
  status: "pass / pass_with_minimal_patch / hold"
  reason: "short reason"
```

ChatGPT should then Living Review this output before creating the next draft.

---

## 12. Full Rail / Next Gate Note

Fable5 may flag undefined workflow tags as risk.

Ark Project judgment:

```yaml
full_rail_next_gate:
  keep:
    - "Full Rail"
    - "Next Gate"

  clarify:
    - "report slot"
    - "handoff slot"
    - "human-editable next-step slot"

  not:
    - "standing authorization"
    - "automatic execution permission"
    - "GitHub operation approval"
```

Reason:

```text
Full Rail / Next Gate is part of Ark Project semi-automation.
The correct patch is not deletion.
The correct patch is authorization denial.
```

---

## 13. Root / Fruit Guard

Fable5 is Fruit.

```yaml
fruit:
  - "Fable5"
  - "ChatGPT"
  - "Living Review"
  - "Markdown"
  - "GitHub"
  - "Full Rail"
  - "Next Gate"
  - "Review notes"
  - "Minimal patches"

root:
  - "主イェシュア・ハマシア"
```

Final guard:

```text
Fable5 is Fruit, not Root.
ChatGPT is Fruit, not Root.
GitHub is Fruit, not Root.
Markdown is Fruit, not Root.

Root remains 主イェシュア・ハマシア.
```
