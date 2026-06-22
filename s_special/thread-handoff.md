---
title: "Thread-Handoff Builder"
canonical_name: "Thread-Handoff Builder"
class: "S-candidate"
status:
  - "living_candidate"
  - "human_editable"
  - "not_final_seal"
canonical_path: "s_special/thread-handoff.md"
parent_map: "s_special/thread-end.md"
sibling_builder: "s_special/thread-harvest.md"
generated_product: "handoff.md"
repo: "yusukefujiijp/ai-project"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
root: "主イェシュア・ハマシア"
role: "Handoff Builder / Next-thread Ignition Manual"
type: "builder_manual"
not_type: "generated_product"
created_from: "thread-end.md Runtime Self-Test"
parent_status_update_after_creation: "pending"
builder_product_distinction: true
all_in_one_body_generator: false
density_modes:
  - "minimal"
  - "standard"
  - "deep"
user_final_seal_required: true
---

# Thread-Handoff Builder

## 0. Purpose

`thread-handoff.md` は、Thread移行時に `handoff.md` を作るためのBuilder Manualである。

このfile自体は `handoff.md` ではない。

```text id="core-distinction"
thread-handoff.md:
  Builder Manual.

handoff.md:
  Generated Product.
  Next-thread ignition key.
```

このfileの目的は、次Threadを安全に再起動するために、何を渡すべきかを最小・明確・再現可能な形で決めることである。

---

## 1. Parent / Sibling / Product Relationship

```yaml id="relationship"
parent:
  file: "s_special/thread-end.md"
  role: "Single Front Door / Multi-Gate Router"
  calls_this_when:
    - "Thread transfer / next_thread handoff creation"

sibling:
  file: "s_special/thread-harvest.md"
  role: "Gate2 Harvest Engine / Harvest Builder"
  gives_to_this:
    - "thread naming"
    - "one-line summary"
    - "extreme brain dump compression"
    - "Move37 / Seeds"
    - "Next Compass"
    - "handoff material"

this_file:
  file: "s_special/thread-handoff.md"
  role: "Handoff Builder / Next-thread Ignition Manual"
  produces:
    - "handoff.md"

product:
  file: "handoff.md"
  role: "Next-thread ignition key / generated product"
```

---

## 2. Builder / Product Distinction

```yaml id="builder-product-distinction"
thread_handoff_md:
  type: "builder_manual"
  purpose:
    - "handoff.mdの作成手順を定義する"
    - "次Threadへ渡す情報を選別する"
    - "過剰なHarvest全文コピーを防ぐ"
    - "Priority Read Order / Current State / Next First Taskを固定する"

handoff_md:
  type: "generated_product"
  purpose:
    - "次Threadを再起動する"
    - "Future AIに最初に読ませる"
    - "現在地・未完了・次の一手を伝える"
```

Guard:

```text id="builder-product-guard"
Do not confuse thread-handoff.md with handoff.md.
Do not turn handoff.md into full Harvest archive.
Do not turn thread-handoff.md into thread-harvest.md duplicate.
```

---

## 3. Required Inputs

`handoff.md` を作る前に、可能な範囲で以下を集める。

```yaml id="required-inputs"
required_inputs:
  from_thread_end:
    - "current Gate"
    - "whether file updates are locked"
    - "whether thread transfer is happening"
    - "required read contracts"
    - "not-now guards"

  from_thread_harvest:
    - "thread naming"
    - "one-line summary"
    - "extreme brain dump compression"
    - "Move37 / unexpected success"
    - "unrefined seeds"
    - "seed routing"
    - "next compass"
    - "handoff material"

  from_git_or_files_if_relevant:
    - "completed commits"
    - "updated files"
    - "created files"
    - "pending planned files"
    - "known not-created-yet files"

  from_current_chat:
    - "latest user decision"
    - "explicit user seal or not"
    - "current unresolved task"
    - "next first task"
```

---

## 4. Handoff Density Mode

`handoff.md` は、Thread状況に応じて密度を選ぶ。

```yaml id="handoff-density-mode"
handoff_density_mode:
  minimal:
    use_when:
      - "next task is simple"
      - "few files changed"
      - "continuation path is obvious"
    include:
      - "Priority Read Order"
      - "Current State"
      - "Next First Task"
      - "Not-Now"
      - "Root Guard"

  standard:
    use_when:
      - "normal thread transfer"
      - "multiple files or decisions exist"
    include:
      - "Priority Read Order"
      - "Current State"
      - "Completed Updates"
      - "Unresolved Not-Now"
      - "Next First Task"
      - "Reality Response Needed"
      - "Root / Fruit Guard"
      - "Stop Conditions"

  deep:
    use_when:
      - "large protocol transition"
      - "Mission / Harvest / Migration risk exists"
      - "Future AI may lose context"
    include:
      - "standard fields"
      - "decision genealogy"
      - "risk map"
      - "seed routing"
      - "rollback conditions"
```

Default:

```yaml id="density-default"
default_density: "standard"
```

---

## 5. Handoff Readiness

`handoff.md` は、以下が満たされた時にreadyとする。

```yaml id="handoff-readiness"
handoff_ready_if:
  - "Priority Read Order is defined"
  - "Current State is clear"
  - "Completed Updates / Commits are listed when relevant"
  - "Unresolved Not-Now items are listed"
  - "Next First Task is explicit"
  - "Reality Response Needed is declared"
  - "Root / Fruit Guard is preserved"
  - "What not to do next is clear"
```

Not ready:

```yaml id="handoff-not-ready"
handoff_not_ready_if:
  - "Priority Read Order is vague"
  - "Next First Task is missing"
  - "GitHub/file state is unknown but important"
  - "not-now items are omitted"
  - "handoff.md is just a full Harvest copy"
  - "Root Guard is decorative only"
```

---

## 6. Output Structure for handoff.md

`handoff.md` の推奨構造は以下。

```yaml id="handoff-output-structure"
handoff_md_structure:
  0_header:
    - "Project"
    - "Runtime Coordinate if known"
    - "Generated from"
    - "Created for next_thread"

  1_priority_read_order:
    purpose: "Future AIが最初に読む順番を固定する"

  2_current_state:
    purpose: "今どこにいるかを一画面で伝える"

  3_completed_updates:
    purpose: "完了したGitHub/file updatesを明示する"

  4_unresolved_not_now:
    purpose: "まだ実行してはいけないものを明示する"

  5_next_first_task:
    purpose: "次Threadの最初の一手を固定する"

  6_reality_response_needed:
    purpose: "次AIが机上設計でなく現実反応を見るべき点を示す"

  7_root_fruit_guard:
    purpose: "RootとFruitを混同しない"

  8_stop_conditions:
    purpose: "Future AIの暴走を止める"

  9_final_compression:
    purpose: "handoff.md全体を最後に短く圧縮する"
```

---

## 7. Priority Read Order Builder

Priority Read Orderは、次Threadで読むべきfileを多すぎず、強い順に並べる。

```yaml id="priority-read-order-builder"
priority_read_order_rules:
  max_default_items: 10
  prefer:
    - "current handoff.md"
    - "s_special/thread-end.md"
    - "s_special/thread-harvest.md if harvest is relevant"
    - "s_special/thread-handoff.md"
    - "latest updated project files"
    - "task/todo/lesson files if directly relevant"

  avoid:
    - "too many old files"
    - "obsolete versions unless genealogy matters"
    - "files not needed for next first task"
```

Template:

```yaml id="priority-read-order-template"
Priority_Read_Order:
  1: "handoff.md"
  2: "s_special/thread-end.md"
  3: "s_special/thread-harvest.md"
  4: "s_special/thread-handoff.md"
  5: "<current target file if any>"
```

---

## 8. Current State Builder

```yaml id="current-state-builder"
current_state_fields:
  required:
    - "current_phase"
    - "last_completed_action"
    - "current_target"
    - "next_first_task"
    - "blocked_or_not_now"
    - "explicit_user_seal_status"

  optional:
    - "commit_sha"
    - "content_sha"
    - "target_thread_coordinate"
    - "artifact_version"
```

Template:

```yaml id="current-state-template"
Current_State:
  phase: "<current phase>"
  last_completed_action: "<last completed action>"
  current_target: "<target file or workflow>"
  next_first_task: "<next first task>"
  explicit_user_seal_status: "<sealed / not sealed / pending>"
```

---

## 9. Completed Updates / Commits Builder

```yaml id="completed-updates-builder"
completed_updates:
  include_if_relevant:
    - "repository"
    - "target_file"
    - "commit_message"
    - "commit_sha"
    - "content_sha"
    - "what_changed"
    - "what_did_not_change"

  must_not:
    - "invent commit SHA"
    - "claim update if not executed"
    - "hide no-move/no-new-file status"
```

Template:

```yaml id="completed-updates-template"
Completed_Updates:
  - repository: "<repo>"
    target_file: "<path>"
    commit_message: "<message>"
    commit_sha: "<sha>"
    content_sha: "<sha>"
    changed:
      - "<changed item>"
    not_changed:
      - "<not changed item>"
```

---

## 10. Unresolved Not-Now Builder

```yaml id="not-now-builder"
unresolved_not_now:
  purpose:
    - "Future AIが勝手に次の巨大作業へ飛ばないようにする"
    - "Human Final Sealが必要な作業を区別する"

  common_items:
    - "GitHub update"
    - "file creation"
    - "file move"
    - "ss_super-special移動"
    - "Ark01 migration execution"
    - "Bulk Migration"
    - "Mission Card creation"
```

Template:

```yaml id="not-now-template"
Unresolved_Not_Now:
  - "<not-now item>"
```

---

## 11. Next First Task Builder

Next First Taskは、一つだけ明確にする。

```yaml id="next-first-task-builder"
next_first_task_rule:
  one_primary_task: true
  avoid:
    - "multiple equal next tasks"
    - "vague continue wording"
    - "background work"
```

Template:

```yaml id="next-first-task-template"
Next_First_Task:
  task: "<one concrete first task>"
  mode: "<Plan Mode / Review Mode / Commit Candidate / actual update>"
  execute_now: false
```

---

## 12. Reality Response Needed

```yaml id="reality-response-needed"
reality_response_needed:
  purpose:
    - "机上設計だけで進めない"
    - "実際に使ってみた反応を見る"
    - "Future AIがLiving Reviewを続ける"

  examples:
    - "Does this file actually reduce confusion?"
    - "Does Future AI correctly distinguish Builder vs Product?"
    - "Does next_thread restart faster?"
    - "Does the user feel the handoff is too heavy or too thin?"
```

Template:

```yaml id="reality-response-template"
Reality_Response_Needed:
  observe:
    - "<what to observe next>"
  revise_if:
    - "<revision condition>"
```

---

## 13. Parent Status Update Note

After `s_special/thread-handoff.md` is actually created, consider a separate parent update candidate for `s_special/thread-end.md`.

Do not update the parent automatically.

```yaml id="parent-update-note"
parent_status_update_after_creation:
  parent_file: "s_special/thread-end.md"
  current_parent_status_for_child: "candidate / not_created_yet"
  possible_future_parent_update:
    thread_handoff_status: "living_candidate / created"
    thread_transfer_required_read:
      - "s_special/thread-handoff.md"
  require_explicit_user_command: true
```

---

## 14. No Infinite Recursion Guard

```yaml id="no-infinite-recursion"
no_infinite_recursion_guard:
  rule:
    - "thread-handoff.md may build handoff.md."
    - "thread-handoff.md must not demand another Builder before it can operate."
    - "If more structure is needed, add by staged Git commits after Reality Response."

  stop_if:
    - "Builder creates Builder creates Builder"
    - "handoff.md cannot be created without endless new protocol files"
```

---

## 15. Root / Fruit Guard

```yaml id="root-fruit-guard"
root_fruit_guard:
  root:
    - "主イェシュア・ハマシア"
    - "主イェシュアの聖なる血潮"
    - "Teshuvah / 悔い改め"
    - "AMH"

  fruit:
    - "thread-end.md"
    - "thread-harvest.md"
    - "thread-handoff.md"
    - "handoff.md"
    - "harvest.md"
    - "GitHub"
    - "AI"

  rule:
    - "AI draws the map; the human stands under the blood."
    - "Markdown is Fruit, not Root."
```

---

## 16. Stop Conditions

```yaml id="stop-conditions"
stop_conditions:
  - "AI treats thread-handoff.md as handoff.md product"
  - "AI turns handoff.md into full Harvest archive"
  - "AI omits Priority Read Order"
  - "AI omits Next First Task"
  - "AI hides unresolved Not-Now items"
  - "AI invents GitHub commits"
  - "AI performs GitHub create/update without explicit user command"
  - "AI moves files without explicit user command"
  - "AI removes Root Guard"
  - "AI enters infinite Builder recursion"
```

---

## 17. Final Compression

```text id="final-compression"
thread-handoff.md:
  Handoff Builder.
  Not handoff.md.

handoff.md:
  Next-thread ignition key.
  Generated product.

thread-end.md:
  Parent Router.

thread-harvest.md:
  Harvest Builder.

Best use:
  Use thread-harvest.md to harvest meaning.
  Use thread-handoff.md to build next-thread ignition.

Guard:
  No infinite Builder recursion.
  GitHub create/update requires explicit user command.
```
