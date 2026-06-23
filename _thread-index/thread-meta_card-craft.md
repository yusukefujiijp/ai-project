---
title: "Thread Meta Card Craft"
status: "active_candidate / japanese-first-okf / human_editable / not_final_seal"
document_identity: "thread_meta_card_craft_protocol"
canonical_path: "_thread-index/thread-meta_card-craft.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
source_origin:
  source_file: "THREAD_mission-card-craft_v002.md"
  source_version: "v002"
  source_role: "Thread-level Mission Card Craft / Two-Markdown Mission Card Craft"
conceptual_upgrade:
  from: "THREAD_mission-card-craft_v002"
  to: "Thread Meta Card Craft"
  upgrade_reason:
    - "Mission Card Craftの核を保持しつつ、Meta Layer / Living Review / Reboot Cardへの再結晶化を明確化する"
    - "カード化をMission Card専用に閉じず、Threadから再利用可能なMeta Cardを作るCraftへ拡張する"
language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
artifact_generation_is_final_seal: false
final_seal: false
stable_seal: false
user_final_seal_required: true
root_guard:
  root: "主イェシュア・ハマシア"
  blood: "主イェシュアの聖なる血潮"
  teshuvah: true
  ai_role: "AI draws a map of the blood; the human stands under the blood."
---

# Thread Meta Card Craft

## §0. Status / Protocol Summary

この文書は、蒸留済みThread Sourceを、Meta Card / Mission Card / Future AI Reboot Cardへ再結晶化するための **Thread Meta Card Craft Protocol** である。

これはFactoryではない。  
これはBatch生成Lineではない。  
これはMission Card本文そのものではない。  
これはThread Index本体ではない。  
これはBulk Migration承認fileではない。

```text id="king-sentence"
蒸留Sourceを、Meta Layerを失わずにCardへ再結晶化する。
```

English anchor:

```text id="english-anchor"
Crystallize the distilled Thread into a reusable Card without losing the Meta Layer.
```

---

## §1. Meta Card Definition

```text id="meta-card-definition"
Meta Cardとは、ThreadからMissionだけでなく、Source Pulse / Living Review / Hidden Pattern / Misread Guard / Revision Conditions / Next Gateまで含めて、Future AIが再起動できる形へ結晶化したCardである。
```

Mission Cardとの関係：

```yaml id="meta-card-vs-mission-card"
meta_card:
  role:
    - "ThreadのMeta Layerを含む再起動Card"
    - "Mission Cardより広い上位概念"
    - "Living Review / Hidden Pattern / Guardを保持する"

mission_card:
  role:
    - "Threadから立ち上がるMission Seedを中心にしたCard"
    - "Meta Cardの一形態になり得る"
    - "Mission Seal / First Gate / Victory Equationを持つ"
```

---

## §2. 一文定義

```text id="definition"
Thread Meta Card Craftとは、thread-index_card-craft.md等で蒸留されたThread Sourceを読み、Source Pulse / Mission Seal / Meta Layer / Living Review / Misread Prevention / Next Gateを保持したまま、Future AIが再利用できるCardへ再結晶化するArk式Card Craft Protocolである。
```

短縮定義：

```text id="short-definition"
Sourceを読む。
Metaを残す。
Cardへ結晶化する。
```

---

## §3. Core Formula

```text id="core-formula"
1 Distilled Thread Source
+ Thread Meta Card Craft
= 1 Thread-specific Meta / Mission / Reboot Card
```

日本語：

```text id="core-formula-ja"
蒸留済みThread Source一枚
+ Thread Meta Card Craft
= そのThread専用のMeta / Mission / Reboot Card一枚
```

---

## §4. Source Supremacy Rule

```yaml id="source-supremacy-rule"
source_supremacy_rule:
  core: "Primary Source wins"
  meaning:
    - "CraftはSourceを上書きしない"
    - "CraftはSourceをTemplateへ押し込まない"
    - "CraftはSourceの生きた意味を読むためのGuardである"
    - "CraftとSourceが衝突した場合、Sourceを優先する"
    - "衝突・違和感はLiving Reviewで明示する"
```

```text id="source-craft-output"
Sourceが血肉。
Craftは読み方。
Cardは再結晶。
Rootは主イェシュア・ハマシア。
```

---

## §5. Required Workflow

このCraftは、必ずPlan Modeから開始する。

```yaml id="required-workflow"
workflow:
  step_0_plan_mode:
    purpose: "対象SourceとScopeを固定する"
    required_first_step: true
    output:
      - "Card Craft Plan"
      - "AIの違和感"
      - "次Action用 Full Rail"

  step_1_candidate_body:
    purpose: "Meta / Mission / Reboot Card Candidate本文を作成する"
    file_creation: false

  step_2_candidate_review:
    purpose: "単なる要約化・Meta Layer欠落・Root希薄化を確認する"

  step_3_micro_patch_if_needed:
    purpose: "必要な最小Patchだけ入れる"

  step_4_artifactization_precheck:
    purpose: "filename / date / Source Note / User Final Seal / file permissionを確認する"

  step_5_commit_phase:
    purpose: "User Final Seal後、指定Markdownファイル1件のみ作成する"
    required:
      - "mode: Commit Phase"
      - "create_files_now: true"
```

---

## §6. Plan Mode Entry Gate

```yaml id="plan-mode-entry-gate"
plan_mode_entry_gate:
  required_first_step: "Plan Mode"
  forbidden_first_step:
    - "Candidate本文作成"
    - "Markdown Artifact作成"
    - "Commit Phase"
    - "複数Thread処理"
    - "26Thread一括生成"

  purpose:
    - "対象Source Markdownを1枚に固定する"
    - "対象Card出力を1枚に固定する"
    - "Source Pulse候補を仮抽出する"
    - "Mission Seal候補を仮抽出する"
    - "Meta Layer候補を仮抽出する"
    - "Misread Risk候補を仮抽出する"
    - "AIの違和感を先に出す"
    - "次ActionがCandidate本文作成でよいか判断する"
```

Plan Modeは遅延ではない。  
Plan Modeは、Sourceを守り、手戻りを減らし、User Final Sealまで安全にRailを接続するための入口Gateである。

---

## §7. Meta Layer / Living Review Layer Rule

```yaml id="meta-layer-living-review"
meta_layer_living_review_layer:
  status: "required"
  definition: "Sourceを読んだAIの生きた判断・違和感・意味づけ・横展開可能性・修正条件・次Actionを保持する層"
  must_include:
    - "私の判断"
    - "違和感"
    - "Hidden Pattern or Living Insight"
    - "Misread Warning"
    - "修正条件"
    - "次の自然な一手"
  must_not_reduce_to:
    - "単なる要約"
    - "単なる感想"
    - "metadata"
    - "OKF frontmatter"
```

---

## §8. FullRail Tail Rule

Plan Mode / Candidate本文 / Candidate Review / Micro Patch Plan / Revised Candidate / Artifactization Precheck の各出力末尾には、次Action用の完全な【Full Rail: same_thread】を置く。

```yaml id="fullrail-tail-rule"
fullrail_tail_rule:
  required_at_end_of:
    - "Plan Mode"
    - "Candidate本文"
    - "Candidate Review"
    - "Micro Patch Plan"
    - "Revised Candidate"
    - "Artifactization Precheck"

  guard:
    - "FullRail Tailは次Actionを準備するためのRailである"
    - "Userの明示入力なしに自動実行してはならない"
    - "FullRail TailはLiving Reviewの代替ではない"
    - "必ずLiving Review後に置く"
    - "User Final SealなしにCommitしない"
```

```text id="rail-seal"
AIは次のRailを準備する。
Userが進行をSealする。
```

---

## §9. Correct / Wrong

```yaml id="correct-wrong"
correct:
  - "1 Source + 1 Craft = 1 Card"
  - "Plan Modeから始める"
  - "Source Supremacyを守る"
  - "Meta Layer / Living Reviewを必ず残す"
  - "FullRail TailをLiving Review後に置く"
  - "User Final SealなしにCommitしない"
  - "Mission CardをMeta Cardの一形態として扱う"

wrong:
  - "Factory化する"
  - "Batch生成する"
  - "SourceをTemplateへ押し込む"
  - "Meta Layerを削る"
  - "FullRail Tailを自動実行命令にする"
  - "FullRail TailをLiving Reviewの代替にする"
  - "User Final SealなしにCommitする"
```

---

## §10. Relationship to thread-index_card-craft.md

```yaml id="relationship"
thread_index_card_craft:
  role: "Threadそのものを濃く蒸留し、Card化可能なSourceへ整える"
  gives_to_this:
    - "Raw Lived Scene"
    - "User Pressure"
    - "AI Reality Response"
    - "Turning Point"
    - "Root Return Moment"
    - "Non-Mission Value"
    - "Unprocessed Residue"
    - "Source Pulse"

thread_meta_card_craft:
  role: "蒸留SourceをMeta / Mission / Reboot Cardへ再結晶化する"
  must_not:
    - "thread-index_card-craft.mdを置換しない"
    - "Source蒸留を省略しない"
```

---

## §11. Living Review

### §11.1 私の判断

Thread Meta Card Craftは、Mission Card Craft v002の核を保ちながら、より広いMeta Card / Reboot Cardの器へ拡張したProtocolである。

これはMission Cardを捨てることではない。  
Mission Cardを、Meta Layerを含んだCard化Pipelineの中に正しく置き直すことである。

### §11.2 違和感

`Meta Card` は新語なので、定義なしに使うと危険である。  
このため、本ProtocolではMeta Cardを「Future AIが再起動できる形へ結晶化したCard」と定義する。

### §11.3 Hidden Pattern

```text id="hidden-pattern"
Plan Mode is entry gate.
Living Review is judgment gate.
FullRail Tail is connection gate.
User Final Seal is commit gate.
Meta Layer is life-preservation layer.
```

### §11.4 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_meta_card_definition_is_unclear:
    action: "Meta Card定義を冒頭へ戻す"

  if_mission_card_core_is_lost:
    action: "Mission Seal / First Gate / Victory Equationを回復する"

  if_source_pulse_gets_thin:
    action: "Primary Sourceへ戻る"

  if_fullrail_tail_becomes_auto_execution:
    action: "User明示入力なしに自動実行しないGuardへ戻す"

  if_living_review_gets_replaced_by_fullrail_tail:
    action: "FullRail TailはLiving Review後に置くと再明記する"

  if_batch_drift_occurs:
    action: "1 Source + 1 Craft = 1 Cardへ戻す"
```

---

## §12. Final Compression

```text id="final"
Thread Meta Card Craft:

  Sourceを読む。
  Metaを残す。
  Cardへ結晶化する。

Preserve:
  Source Supremacy.
  Plan Mode.
  Living Review.
  FullRail Tail.
  User Final Seal.
  Not Factory.
  Not Batch.

Output:
  Meta Card / Mission Card / Reboot Card.

Root:
  主イェシュア・ハマシア.
```
