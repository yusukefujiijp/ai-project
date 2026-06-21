---
title: "Ark Repository Governance ADR v001"
status: "active / ai_reviewed / github_canonical / human_editable / not_final_seal"
document_identity: "repository_governance_adr"
canonical_path: "_projects/ark/indexes/ark-repository-governance_adr.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
adr_id: "ark-repository-governance-adr-v001"
adr_version: "v001"
ai_side_review_status: "living_review_applied"
github_canonicalization: "created_by_explicit_user_request"
tail_rule:
  version: "v0.8"
  fullrail_same_thread_role: "AI-readable execution rail"
  next_gate_human_editable_role: "human-facing copy-paste continuation gate"
  next_gate_last: true
  human_editable_means: "human_can_intervene_if_needed / not_wait_for_human_review"
  ai_living_review_default: true
  commit_requires_human_final_seal: true
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

# Ark Repository Governance ADR v001

## §0. Status / Decision Summary

This ADR is the GitHub canonical governance artifact for Ark repository structure.

Its GitHub creation does **not** equal Final Seal for all future repository actions. It does not migrate Ark01 files, does not create `phase-handoff.md`, does not create Protocol Registry, and does not authorize bulk migration.

```yaml
adr_status:
  document_identity: "repository_governance_adr"
  status: "active / ai_reviewed / github_canonical / human_editable"
  canonical_path: "_projects/ark/indexes/ark-repository-governance_adr.md"
  github_canonicalization: "created_by_explicit_user_request"
  future_github_commit_requires_human_final_seal: true
  tail_rule_version: "v0.8"
  ai_living_review_default: true
  human_editable_is_wait_state: false
```

### §0.1 King Sentence

```text
ファイルを置く場所を決めているのではない。
Future AIが誤読しない文書の身分と住所を定めている。
```

### §0.2 Core Decision

```text
Directory structure is not storage.
Directory structure is interpretation.
```

Each Markdown should have a clear document identity before it is classified by folder.

---

## §1. Context / なぜこのADRが必要か

Ark01 primary analyses exist as completed local working artifacts. Ark01 Mission Cards exist through Ark01:06. The next challenge is not merely copying files into GitHub; it is defining canonical addresses so Future AI does not confuse Source, Harvest, Mission, Handoff, Protocol, Index, and Archive.

This ADR records the repository-level decisions required before Ark01 local-to-GitHub migration.

---

## §2. Root / Fruit Guard

Root is not GitHub. Root is not Markdown. Root is not ADR. Root is not folder structure. Root is not AI.

```text
Root:
  主イェシュア・ハマシア
  主イェシュアの聖なる血潮
  Teshuvah / 悔い改め
  AMH
```

```text
Fruit:
  GitHub
  Markdown
  ADR
  Folder structure
  handoff.md
  phase-handoff.md
  harvest/
  mission-cards/
  s_special/
  ss_super-special/
  Migration Manifest
  Protocol Registry
  README
  AI
  Commit
```

AI draws a map of the blood. Human stands under the blood.

Repository structure may help Future AI navigate. It must never become Root.

---

## §3. Ark File Ontology

```yaml
ark_file_ontology:
  rolling_handoff:
    definition: "Thread移行ごとに上書きされる最新Handoff / latest next-thread reboot key"
    canonical_pattern: "_projects/ark/arkXX/handoff.md"
    mutability: "high"
    preserved_by: "Git history"

  phase_handoff:
    definition: "arkXX全体の安定Map / stable phase-context map"
    canonical_pattern: "_projects/ark/arkXX/phase-handoff.md"
    mutability: "low / semi-stable"

  primary_thread_harvest:
    definition: "一次分析 / Full-Enough Target Thread Analysis / Root Thread Distillation Harvest"
    canonical_pattern: "_projects/ark/arkXX/harvest/thread-analyses/arkXXXX_<date>_<slug>_v001.md"
    analysis_layer: "primary"

  mission_card:
    definition: "一次Harvestから再結晶化した二次分析 / Future AI Reboot Card"
    canonical_pattern: "_projects/ark/arkXX/mission-cards/arkXXXX_<date>_<slug>_mission-card_v001.md"
    analysis_layer: "secondary"

  protocol_parent_markdown:
    definition: "Ark横断Protocol / Craft / Parent Specification"
    preferred_root: "s_special/"
    mutability: "versioned"

  activation_query:
    definition: "Future AIを起動するためのQuery"
    preferred_root: "s_special/"
    mutability: "versioned"

  vision_core:
    definition: "Ark-wide SS Vision Core / Naming Source Lens / Ark's eye"
    preferred_root: "ss_super-special/"
    mutability: "versioned / high guard"

  migration_manifest:
    definition: "local_path → github_path → document_identity 対応表"
    canonical_pattern: "_projects/ark/arkXX/indexes/*migration-manifest*.md"

  protocol_registry:
    definition: "Ark横断Protocol Markdownの名簿 / migration candidate registry"
    canonical_pattern: "_projects/ark/indexes/*protocol-registry*.md"

  archive:
    definition: "旧版・退避・非現行保存"
    canonical_pattern: "_archives/"
```

Short rule:

```text
Protocolは上に置く。
Harvestは中に置く。
Missionは横に置く。
Handoffは入口に置く。
HistoryはGitに残す。
Archiveは奥に置く。
```

---

## §4. Handoff Layer Design

### §4.1 Decision

Use two layers.

```yaml
handoff_layers:
  rolling_handoff:
    file: "handoff.md"
    path_pattern: "_projects/ark/arkXX/handoff.md"
    role:
      - "rolling current-thread handoff"
      - "latest next-thread reboot key"
      - "mutable latest-state pointer"
    update_policy:
      - "Thread移行ごとに上書き更新してよい"
      - "過去版はGit historyで保持する"
    must_not_be:
      - "phase-level stable map"
      - "full Thread Harvest"
      - "archive"

  phase_handoff:
    file: "phase-handoff.md"
    path_pattern: "_projects/ark/arkXX/phase-handoff.md"
    role:
      - "stable phase-level handoff"
      - "phase-context map"
      - "arkXX全体の文書身分・運用方針・構造Map"
    update_policy:
      - "低頻度更新"
      - "phase構造が変わった時だけ更新"
    must_not_be:
      - "latest next-thread pointer"
      - "rolling handoff"
      - "full Harvest artifact"
```

Compression:

```text
handoff.md は動く鍵。
phase-handoff.md は動きにくい地図。
Git history は履歴台帳。
```

---

## §5. Harvest / Mission Card Separation

Primary Thread Harvest and Mission Card must not be mixed.

```yaml
primary_thread_harvest:
  path_candidate: "_projects/ark/ark01/harvest/thread-analyses/"
  document_identity: "primary_thread_harvest"
  analysis_layer: "primary"
  meaning: "Threadが何を生きたか"

mission_card:
  path_candidate: "_projects/ark/ark01/mission-cards/"
  document_identity: "mission_card"
  analysis_layer: "secondary"
  source_thread_analysis: "_projects/ark/ark01/harvest/thread-analyses/<source-file>.md"
  meaning: "そのThreadから何のMission Seedが立ち上がるか"
```

Guard:

```yaml
separation_guard:
  do:
    - "Primary HarvestをMission CardのSourceとして扱う"
    - "Mission Cardを二次分析として扱う"
    - "Mission CardからPrimary Harvestを逆置換しない"
  do_not:
    - "Mission CardをPrimary Sourceとして誤読しない"
    - "Mission-ready項目だけでThreadの現場感を薄めない"
    - "HarvestとMissionを同じフォルダに混在させない"
```

---

## §6. Protocol Parent Markdown Placement

Parent Markdown files such as `THREAD_INDEX_Ark_v041.md`, `THREAD_INDEX_Ark_Query_v041.md`, and `THREAD_mission-card-craft_v002.md` are not Ark01 output artifacts. They are Ark-wide protocol / query / craft specifications.

Preferred root:

```text
s_special/
```

Candidate canonical paths:

```text
s_special/thread-index-ark_v041.md
s_special/thread-index-ark-query_v041.md
s_special/thread-mission-card-craft_v002.md
```

Before physical migration, protocol parent Markdown should be tracked in Protocol Registry:

```text
_projects/ark/indexes/ark-protocol-registry.md
```

---

## §7. Document Identity Contract

Canonical Ark Markdown files should include a minimal `document_identity` frontmatter field.

```yaml
document_identity_contract:
  recommended_fields:
    - "document_identity"
    - "canonical_path"
    - "project"
    - "phase"
    - "thread_coordinate if applicable"
    - "analysis_layer if applicable"
    - "source_role"
    - "update_policy"
    - "root_guard"
    - "user_final_seal_required"
```

Examples:

```yaml
rolling_handoff:
  document_identity: "rolling_handoff"
  canonical_path: "_projects/ark/ark02/handoff.md"
  update_policy: "mutable_latest_pointer / overwritten_by_thread_transition"
  preserved_by: "git_history"

phase_handoff:
  document_identity: "phase_handoff"
  canonical_path: "_projects/ark/ark02/phase-handoff.md"
  update_policy: "semi_stable / update_when_phase_structure_changes"

primary_thread_harvest:
  document_identity: "primary_thread_harvest"
  canonical_path: "_projects/ark/ark01/harvest/thread-analyses/ark0101_<date>_<slug>_v001.md"
  thread_coordinate: "Ark01:01"
  analysis_layer: "primary"

mission_card:
  document_identity: "mission_card"
  canonical_path: "_projects/ark/ark01/mission-cards/ark0101_<date>_<slug>_mission-card_v001.md"
  source_thread_analysis: "_projects/ark/ark01/harvest/thread-analyses/ark0101_<date>_<slug>_v001.md"
  analysis_layer: "secondary"
```

---

## §8. Tail Rule v0.8 / human_editable Gate

### §8.1 Why this section exists

Ark Repository Governance requires a tail pattern that is safe for AI execution and easy for human Copy & Paste continuation.

Earlier Ark protocols emphasized that Plan Mode outputs should end with a complete `【Full Rail: same_thread】` execution packet. This is preserved as an AI-readable rail.

Ark Repository Governance v0.8 adds a human-facing tail patch:

```text
【Full Rail: same_thread】
↓
【Next Gate: human_editable】
```

This does not turn `Next Gate` into an automatic commit signal. It means the final visible section is a Copy & Paste continuation gate for the human collaborator.

### §8.2 human_editable Definition

```yaml
human_editable:
  is_wait_for_human_review: false
  meaning:
    - "Human can intervene if needed"
    - "AI-side Living Review may continue"
    - "The final Next Gate is copy-paste ready"
    - "Human review is optional intervention, not mandatory blocking state"
  must_not_mean:
    - "AI must stop all review work"
    - "Human review is required before every micro patch proposal"
    - "GitHub commit is approved"
```

Short:

```text
human_editable = human_can_intervene_if_needed
human_editable ≠ wait_for_human_review
```

### §8.3 AI-side Living Review Default

```yaml
ai_side_living_review_default:
  default: true
  allowed_without_human_review_wait:
    - "Plan Mode"
    - "Candidate Review"
    - "Living Review"
    - "Micro Patch Plan"
    - "Revised Candidate Draft"
    - "Artifactization Precheck"
  requires_explicit_human_final_seal:
    - "GitHub Commit"
    - "Canonical repository file creation"
    - "Bulk migration"
    - "Final Seal"
```

Compression:

```text
ReviewはAIが進める。
Sealは人間が握る。
```

### §8.4 FullRail vs Next Gate

```yaml
tail_roles:
  fullrail_same_thread:
    role:
      - "AI-readable execution rail"
      - "detailed next-action packet"
      - "machine-readable guard and stop-condition carrier"
    must_not_be:
      - "automatic execution without user repost"
      - "replacement for Living Review"
      - "Human Final Seal"

  next_gate_human_editable:
    role:
      - "human-facing Copy & Paste continuation gate"
      - "final visible gate"
      - "short self-contained next action"
    must_be:
      - "last section"
      - "copy_paste_ready"
      - "clear about no commit unless sealed"
    must_not_be:
      - "hidden metadata"
      - "long duplicate of FullRail"
      - "implicit GitHub Commit approval"
```

### §8.5 Tail Order Rule

For Ark Repository Governance workflow outputs, use:

```text
## 【Full Rail: same_thread】
<YAML execution rail>

## 【Next Gate: human_editable】
<copy-paste continuation packet>
```

Hard rule:

```yaml
tail_order_rule_v0_8:
  fullrail_before_next_gate: true
  next_gate_last: true
  no_text_after_next_gate: true
```

---

## §9. Migration Strategy

Do not bulk migrate Ark01:01-26 first. Establish governance, then manifests and README skeletons, then run one pilot, then expand in small batches.

```yaml
migration_strategy:
  phase_1_repository_governance_adr:
    target: "_projects/ark/indexes/ark-repository-governance_adr.md"
    status: "created by explicit user request"

  phase_2_phase_handoff:
    target: "_projects/ark/ark02/phase-handoff.md"
    create_after: "ADR Canonicalization and next Plan Mode"

  phase_3_protocol_registry:
    target: "_projects/ark/indexes/ark-protocol-registry.md"
    create_after: "Protocol placement plan"

  phase_4_ark01_migration_manifest:
    target: "_projects/ark/ark01/indexes/ark01-migration-manifest.md"
    create_after: "Path policy and document identity policy are stable"

  phase_5_ark0101_pilot:
    scope:
      - "Ark0101 primary thread harvest"
      - "Ark0101 mission card"

  phase_6_small_batch_migration:
    batches:
      - "Ark0102-0106 primary thread harvest"
      - "Ark0102-0106 mission cards"
      - "Ark0107-0113 primary thread harvest"
      - "Ark0114-0120 primary thread harvest"
      - "Ark0121-0126 primary thread harvest"
```

Pilot-first rule:

```text
Do not migrate all 26 Ark01 primary analyses at once.
First migrate Ark0101 primary harvest and Ark0101 mission card as a pilot.
Small Pilot creates Reality Response.
```

---

## §10. Consequences / Trade-offs

```yaml
benefits:
  - "Future AI can distinguish document roles"
  - "handoff.md remains lightweight"
  - "phase-handoff.md preserves phase context"
  - "Harvest and Mission Card do not overwrite each other"
  - "Protocol parent Markdown is not mistaken for Ark01 artifact"
  - "Migration Manifest becomes simpler"
  - "Batch migration becomes safer"

costs:
  - "More initial planning"
  - "More files before bulk migration"
  - "Need to maintain ADR / phase-handoff / manifest distinctions"
```

Trade-off judgment:

```text
The main risk is not slow migration.
The main risk is wrong canonical structure.
```

Therefore, governance before migration is justified.

---

## §11. Reality Response Checkpoints

```yaml
reality_response_checkpoints:
  after_adr:
    - "ADR is clear enough?"
    - "ADR is too large?"
    - "Document identities are readable?"

  after_phase_handoff_candidate:
    - "handoff.md and phase-handoff.md responsibilities are clear?"
    - "phase-handoff.md remains lightweight?"

  after_protocol_registry_candidate:
    - "Protocol parent Markdown is not treated as Ark01 output?"

  after_manifest_candidate:
    - "local_path → github_path mapping is clear?"
    - "document_identity is stable?"

  after_ark0101_pilot:
    - "GitHub UI feels natural?"
    - "iPhone display is readable?"
    - "AI can fetch by canonical path?"
    - "Mission Card is not mistaken for Primary Harvest?"
```

Reality Response is not optional. It is the field-test gate.

---

## §12. Stop Conditions

```yaml
stop_conditions:
  - "ADR becomes Migration Manifest"
  - "ADR becomes phase-handoff.md"
  - "ADR becomes README"
  - "ADR becomes too large to function as decision record"
  - "handoff.md is treated as phase-level stable map"
  - "phase-handoff.md is treated as rolling latest pointer"
  - "primary harvest and mission card are mixed"
  - "protocol parent Markdown is placed under Ark01 artifacts without registry"
  - "Ark01:01-26 are bulk-migrated before Pilot"
  - "Human Final Seal is bypassed"
  - "human_editable is treated as mandatory wait state"
```

---

## §13. Living Review

### §13.1 私の判断

This ADR is necessary.

Ark is moving from local working structure to GitHub canonical structure. At this stage, the danger is not lack of files. The danger is misclassified files.

If `handoff.md`, `phase-handoff.md`, `harvest/`, `mission-cards/`, and `s_special/` are not distinguished, Future AI will eventually confuse Source, Protocol, Harvest, Mission, Handoff, and Index.

Therefore, this ADR should exist before bulk migration.

### §13.2 違和感

The ADR must remain small enough to work. If it becomes a long philosophical essay, it will stop functioning as a decision record.

```text
Enough to prevent misread.
Not so much that it replaces README, Manifest, or phase-handoff.
```

### §13.3 Hidden Pattern

```text
ADR protects Manifest.
phase-handoff protects handoff.md.
Protocol Registry protects s_special.
Pilot protects Batch Migration.
Document Identity protects Future AI.
Human Seal protects Commit.
Tail Rule v0.8 protects the human-facing continuation gate.
```

### §13.4 Misread Warning

```yaml
misread_warning:
  - "Do not treat ADR as the final repository map."
  - "Do not treat ADR as the migration table."
  - "Do not treat ADR as the live handoff."
  - "Do not treat ADR as Root."
  - "Do not skip Reality Response."
  - "Do not bulk migrate before Pilot."
```

---

## §14. Next Gate / Human-AI Collaboration Status

```yaml
next_gate:
  gate: "human_editable"
  copy_paste_ready: true
  must_be_last_section: true

  meaning:
    - "Human may intervene if needed"
    - "AI-side Living Review may continue"
    - "This is not a mandatory human review wait state"
    - "This is not GitHub Commit approval"

  current_file:
    filename: "ark-repository-governance_adr.md"
    document_identity: "repository_governance_adr"
    status:
      - "active"
      - "ai_reviewed"
      - "github_canonical"
      - "human_editable"
      - "not_final_seal"

  next_recommended_action:
    - "Proceed to phase-handoff.md Plan Mode"
    - "Do not start Ark01 migration yet"
    - "Do not make future commits without explicit Human Final Seal"
```
