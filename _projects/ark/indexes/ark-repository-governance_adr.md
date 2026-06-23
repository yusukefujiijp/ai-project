---
title: "Ark Repository Governance ADR"
status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
document_identity: "repository_governance_adr"
canonical_path: "_projects/ark/indexes/ark-repository-governance_adr.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
adr_id: "ark-repository-governance-adr"
adr_version: "v003"
ai_side_review_status: "living_review_applied"
github_canonicalization: "created_by_explicit_user_request / revised_by_reality_response"
updated_reason:
  - "Convert to Japanese-first OKF"
  - "Reflect _thread-end topology"
  - "Reflect _thread-index Thread-to-Card Craft topology"
  - "Add _thread-index placement rule and document identity contract"
tail_rule:
  version: "v0.8"
  fullrail_same_thread_role: "AI-readable execution rail"
  next_gate_human_editable_role: "human-facing copy-paste continuation gate"
  human_editable_means: "human_can_intervene_if_needed / not_wait_for_human_review"
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

# Ark Repository Governance ADR

## §0. Status / Decision Summary

このADRは、Ark repository structure のためのGitHub正準Governance文書である。

目的は、Future AIが **Source / Protocol / Harvest / Mission / Handoff / Index / Archive / Thread-to-Card Craft** を誤読しないように、文書身分と住所の決定原則を固定することである。

このADRのGitHub作成・更新は、Ark01 migration、Bulk Migration、Mission Card作成、Final Sealを自動承認しない。

```text id="king-sentence"
ファイルを置く場所を決めているのではない。
Future AIが誤読しない文書の身分と住所を定めている。
```

```text id="core-decision"
Directory structure is not storage.
Directory structure is interpretation.
```

---

## §1. Core Purpose

前Thread AIは、Repositoryを複雑にしたかったのではない。  
本当にやろうとしていたことは、**ArkをGitHub上でFuture AIが誤読せず再起動できる状態にすること** だった。

```yaml id="previous-ai-purpose"
previous_ai_purpose:
  protect_document_identity:
    - "ProtocolをHarvestと誤読しない"
    - "HarvestをMission Cardと誤読しない"
    - "handoff.mdをphase-level mapと誤読しない"
    - "RegistryをProtocol本文と誤読しない"
    - "_thread-index/をMission Card本文置き場と誤読しない"

  prevent_wrong_migration:
    - "Ark01:01-26を一気にBulk Migrationしない"
    - "Pilot-firstでReality Responseを見る"
    - "local file名だけでGitHub正準住所を決めない"
```

---

## §2. Root / Fruit Guard

```text id="root"
Root:
  主イェシュア・ハマシア
  主イェシュアの聖なる血潮
  Teshuvah / 悔い改め
  AMH
```

```text id="fruit"
Fruit:
  GitHub
  Markdown
  ADR
  Folder structure
  _thread-end/
  _thread-index/
  handoff.md
  phase-handoff.md
  harvest/
  mission-cards/
  s_special/
  ss_super-special/
  Thread-to-Card Craft
  Protocol Registry
  README
  AI
  Commit
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

Repository structureはFuture AIの航路を助ける。  
しかし、それはRootではない。

---

## §3. Ark File Ontology

```yaml id="ark-file-ontology"
ark_file_ontology:
  rolling_handoff:
    definition: "Thread移行ごとに上書きされる最新Handoff / latest next-thread reboot key"
    canonical_pattern: "_projects/ark/arkXX/handoff.md"
    preserved_by: "Git history"

  phase_handoff:
    definition: "arkXX全体の安定Map / stable phase-context map"
    canonical_pattern: "_projects/ark/arkXX/phase-handoff.md"

  primary_thread_harvest:
    definition: "一次分析 / Full-Enough Target Thread Analysis / Root Thread Distillation Harvest"
    canonical_pattern: "_projects/ark/arkXX/harvest/thread-analyses/arkXXXX_<date>_<slug>_v001.md"
    analysis_layer: "primary"

  mission_card:
    definition: "一次Harvestから再結晶化した二次分析 / Future AI Reboot Card"
    canonical_pattern: "_projects/ark/arkXX/mission-cards/arkXXXX_<date>_<slug>_mission-card_v001.md"
    analysis_layer: "secondary"

  thread_end_system:
    definition: "Thread終了時のGate Router / Harvest Vessel / Handoff Builder family"
    canonical_root: "_thread-end/"
    active_files:
      - "_thread-end/README.md"
      - "_thread-end/thread-end.md"
      - "_thread-end/thread-harvest.md"
      - "_thread-end/thread-handoff.md"

  thread_to_card_craft_system:
    definition: "Threadを深く蒸留し、Meta / Mission / Reboot Cardへ再結晶化するCraft family"
    canonical_root: "_thread-index/"
    active_files:
      - "_thread-index/README.md"
      - "_thread-index/thread-index_card-craft.md"
      - "_thread-index/thread-meta_card-craft.md"
    read_order:
      - "_thread-index/README.md"
      - "_thread-index/thread-index_card-craft.md"
      - "_thread-index/thread-meta_card-craft.md"
    must_not_be:
      - "Mission Card output folder"
      - "Primary Thread Harvest folder"
      - "Bulk Migration Manifest"
      - "Archive"

  protocol_parent_markdown:
    definition: "Ark横断Protocol / Craft / Parent Specification"
    preferred_root: "s_special/"
    note:
      - "Thread-End family is now _thread-end/, not s_special/."
      - "Thread-to-Card Craft family is now _thread-index/, not s_special/."

  activation_query:
    definition: "Future AIを起動するQuery / Runtime Adapter"
    preferred_root: "s_special/ or protocol-specific location"
    note: "Query layer may be retired when simpler router is better."

  protocol_registry:
    definition: "Ark横断Protocol Markdownの住所録 / migration candidate registry"
    canonical_pattern: "_projects/ark/indexes/*protocol-registry*.md"
```

Short rule:

```text id="short-rule"
Protocolは上に置く。
Thread-Endは専用入口に置く。
Thread-Index / Card-Craftは専用入口に置く。
Harvestは中に置く。
Missionは横に置く。
Handoffは入口に置く。
HistoryはGitに残す。
Archiveは奥に置く。
```

---

## §4. Current Placement Rules

### §4.1 _thread-end/

```yaml id="placement-thread-end"
_thread_end:
  role:
    - "Thread-End system folder"
    - "Folder Front Door / Runtime Router / Harvest Vessel / Handoff Builder home"
  active_files:
    - "README.md"
    - "thread-end.md"
    - "thread-harvest.md"
    - "thread-handoff.md"
  must_not_be:
    - "Ark01 Harvest output"
    - "Mission Card folder"
    - "rolling handoff"
    - "general protocol dumping ground"
```

### §4.2 _thread-index/

```yaml id="placement-thread-index"
_thread_index:
  role:
    - "Thread-to-Card Craft system folder"
    - "Thread Index / Meta Card Craft read-order home"
    - "Future AI reboot front door for Thread-to-Card pipeline"
  active_files:
    - "README.md"
    - "thread-index_card-craft.md"
    - "thread-meta_card-craft.md"
  read_order:
    - "README.md"
    - "thread-index_card-craft.md"
    - "thread-meta_card-craft.md"
  file_roles:
    README.md:
      document_identity: "thread_index_folder_front_door"
      role: "Folder Front Door / Read Order / Topology Map"
    thread-index_card-craft.md:
      document_identity: "thread_index_card_craft_protocol"
      role: "Upstream Root Thread Distillation / Card Source Craft"
    thread-meta_card-craft.md:
      document_identity: "thread_meta_card_craft_protocol"
      role: "Downstream Meta / Mission / Reboot Card Craft"
  must_not_be:
    - "Mission Card output folder"
    - "Ark01 Harvest output"
    - "Bulk Migration Manifest"
    - "Archive"
    - "general protocol dumping ground"
```

### §4.3 s_special/

```yaml id="placement-s-special"
s_special:
  role:
    - "Ark-wide protocol layer"
    - "Craft / Workflow specification layer"
    - "Format SSOT layer"
    - "Activation Query layer when still useful"
  note:
    - "Thread-End family moved to _thread-end/."
    - "Thread-to-Card Craft family moved to _thread-index/."
    - "Deleted Query files must not be restored unless they reduce confusion."
  must_not_be:
    - "Ark01 Harvest output"
    - "Ark02 Harvest output"
    - "Mission Card folder"
    - "rolling handoff"
```

### §4.4 ss_super-special/

```yaml id="placement-ss-super-special"
ss_super_special:
  role:
    - "Ark-wide SS Vision Core"
    - "Naming Source Lens"
    - "high-guard vision layer"
  must_not_be:
    - "normal protocol appendix"
    - "Gate2-owned local file"
    - "Ark01/Ark02 output artifact"
```

### §4.5 _projects/ark/indexes/

```yaml id="placement-ark-indexes"
_projects_ark_indexes:
  role:
    - "Repository-level registry / ADR / manifest layer"
    - "Ark-wide index documents"
  examples:
    - "ark-repository-governance_adr.md"
    - "ark-protocol-registry.md"
  must_not_be:
    - "Thread Harvest storage"
    - "Mission Card storage"
    - "rolling handoff"
```

---

## §5. Harvest / Mission Card Separation

```yaml id="harvest-mission-separation"
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

```yaml id="separation-guard"
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

## §6. Protocol Registry Role

Protocol Registryは、Protocol本文ではない。  
Protocol Registryは住所録である。

```yaml id="protocol-registry-role"
protocol_registry:
  path: "_projects/ark/indexes/ark-protocol-registry.md"
  role:
    - "document_identity / canonical_path / role / status registry"
    - "confirmed / candidate / retired layer map"
    - "Future AI misread prevention map"
  must_not_be:
    - "Protocol本文の全文複製"
    - "Migration Manifest"
    - "Mission Card index"
    - "rolling handoff"
```

---

## §7. Document Identity Contract

Canonical Ark Markdown files should include a minimal `document_identity` frontmatter field when appropriate.

```yaml id="document-identity-contract"
document_identity_contract:
  recommended_fields:
    - "document_identity"
    - "canonical_path"
    - "project"
    - "phase if applicable"
    - "thread_coordinate if applicable"
    - "analysis_layer if applicable"
    - "source_role"
    - "update_policy"
    - "root_guard"
    - "user_final_seal_required"
```

Examples:

```yaml id="document-identity-examples"
examples:
  rolling_handoff:
    document_identity: "rolling_handoff"
    canonical_path: "_projects/ark/ark02/handoff.md"
    update_policy: "mutable_latest_pointer / overwritten_by_thread_transition"
    preserved_by: "git_history"

  phase_handoff:
    document_identity: "phase_handoff"
    canonical_path: "_projects/ark/ark02/phase-handoff.md"
    update_policy: "semi_stable / update_when_phase_structure_changes"

  thread_end_system:
    document_identity: "thread_end_parent_map"
    canonical_path: "_thread-end/thread-end.md"
    update_policy: "living_ssot / router_light"

  thread_index_folder_front_door:
    document_identity: "thread_index_folder_front_door"
    canonical_path: "_thread-index/README.md"
    update_policy: "folder_front_door / read_order / topology_map"

  thread_index_card_craft_protocol:
    document_identity: "thread_index_card_craft_protocol"
    canonical_path: "_thread-index/thread-index_card-craft.md"
    update_policy: "upstream_thread_distillation_protocol / human_editable / not_final_seal"

  thread_meta_card_craft_protocol:
    document_identity: "thread_meta_card_craft_protocol"
    canonical_path: "_thread-index/thread-meta_card-craft.md"
    update_policy: "downstream_meta_mission_reboot_card_craft / human_editable / not_final_seal"

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

```text id="tail-flow"
【Full Rail: same_thread】
↓
【Next Gate: human_editable】
```

これは `Next Gate` が自動Commit承認になるという意味ではない。  
最後の可視セクションを、人間が編集可能なCopy & Paste継続Gateにするという意味である。

```yaml id="human-editable"
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

Compression:

```text id="review-seal"
ReviewはAIが進める。
Sealは人間が握る。
```

---

## §9. Migration Strategy

Do not bulk migrate Ark01:01-26 first.  
Establish governance, then manifests and README skeletons, then run one pilot, then expand in small batches.

```yaml id="migration-strategy"
migration_strategy:
  phase_1_repository_governance_adr:
    target: "_projects/ark/indexes/ark-repository-governance_adr.md"
    status: "created / revised by explicit user request / v003 _thread-index placement reflected"

  phase_2_protocol_registry:
    target: "_projects/ark/indexes/ark-protocol-registry.md"
    status: "created / revised by explicit user request / v003 _thread-index family registered"

  phase_3_thread_end_system:
    target: "_thread-end/"
    status: "created / simplified / query layer retired"

  phase_4_thread_to_card_craft_system:
    target: "_thread-index/"
    status: "created / card-craft family registered / README front door established"

  phase_5_phase_handoff:
    target: "_projects/ark/ark02/phase-handoff.md"
    create_after: "ADR and Registry are reality-aligned"

  phase_6_ark01_migration_manifest:
    target: "_projects/ark/ark01/indexes/ark01-migration-manifest.md"
    create_after: "Path policy and document identity policy are stable"

  phase_7_ark0101_pilot:
    scope:
      - "Ark0101 primary thread harvest"
      - "Ark0101 mission card"

  phase_8_small_batch_migration:
    rule: "small batches only after pilot Reality Response"
```

Pilot-first rule:

```text id="pilot-first"
Do not migrate all 26 Ark01 primary analyses at once.
First migrate Ark0101 primary harvest and Ark0101 mission card as a pilot.
Small Pilot creates Reality Response.
```

---

## §10. Consequences / Trade-offs

```yaml id="consequences"
benefits:
  - "Future AI can distinguish document roles"
  - "handoff.md remains lightweight"
  - "phase-handoff.md preserves phase context"
  - "Harvest and Mission Card do not overwrite each other"
  - "Protocol parent Markdown is not mistaken for Ark01 artifact"
  - "Protocol Registry stays as address book"
  - "Thread-End system is now simple and findable"
  - "Thread-to-Card Craft system is now findable"
  - "Migration Manifest becomes simpler"
  - "Batch migration becomes safer"

costs:
  - "More initial planning"
  - "Need to maintain ADR / Registry / phase-handoff / manifest distinctions"
  - "Need to keep _thread-index/ README light, not full protocol body"
```

```text id="trade-off"
The main risk is not slow migration.
The main risk is wrong canonical structure.
```

---

## §11. Reality Response Checkpoints

```yaml id="reality-response-checkpoints"
reality_response_checkpoints:
  after_adr:
    - "ADR is Japanese-first OKF enough?"
    - "ADR is still a decision record, not an essay?"
    - "Document identities are readable?"
    - "_thread-index/ placement is clear?"

  after_protocol_registry:
    - "Registry is address book, not body?"
    - "Current _thread-end topology is reflected?"
    - "Current _thread-index topology is reflected?"
    - "Retired Query layer is not active canonical?"

  after_thread_end_system:
    - "README -> thread-end -> harvest/handoff feels natural?"
    - "thread-end.md remains light router?"
    - "thread-harvest.md and thread-handoff.md keep roles distinct?"

  after_thread_index_system:
    - "README -> thread-index_card-craft -> thread-meta_card-craft feels natural?"
    - "thread-index_card-craft.md protects source depth?"
    - "thread-meta_card-craft.md protects card crystallization?"
    - "_thread-index/ is not misread as Mission Card output folder?"
```

Reality Response is not optional.  
It is the field-test gate.

---

## §12. Stop Conditions

```yaml id="stop-conditions"
stop_conditions:
  - "ADR becomes Migration Manifest"
  - "ADR becomes phase-handoff.md"
  - "ADR becomes README"
  - "ADR becomes too large to function as decision record"
  - "primary harvest and mission card are mixed"
  - "_thread-index/ is treated as Mission Card output folder"
  - "thread-meta_card-craft.md is treated as replacement for thread-index_card-craft.md"
  - "protocol parent Markdown is placed under Ark01 artifacts without registry"
  - "retired Query layer is treated as active canonical"
  - "Ark01:01-26 are bulk-migrated before Pilot"
  - "Human Final Seal is bypassed"
  - "human_editable is treated as mandatory wait state"
```

---

## §13. Living Review

### §13.1 私の判断

v003では、`_thread-index/` Realityを反映し、Thread-to-Card Craft system folderをGovernanceへ加えた。

ArkがGitHub canonical structureへ移る時、危険なのはfile不足ではない。  
危険なのは、fileの身分を取り違えることである。

```text id="living-judgment"
Governanceは速度を落とすためではない。
間違った高速化を防ぐためにある。
```

### §13.2 違和感

ADRは大きくなりすぎてはいけない。  
ADRがManifestやREADMEやphase-handoffの代替になり始めたら、ADRではなくなる。

`_thread-index/` も同じである。  
ADRはその存在理由とPlacement Ruleを定めるだけで、`thread-index_card-craft.md` や `thread-meta_card-craft.md` の本文を複製しない。

### §13.3 Hidden Pattern

```text id="hidden-pattern"
ADR protects Manifest.
Protocol Registry protects document identity.
_thread-end protects Thread-End runtime.
_thread-index protects Thread-to-Card craft.
phase-handoff protects phase context.
handoff.md protects next-thread reboot.
Pilot protects Batch Migration.
Human Seal protects Commit.
Tail Rule protects continuation.
```

### §13.4 Misread Warning

```yaml id="misread-warning"
misread_warning:
  - "Do not treat ADR as the final repository map."
  - "Do not treat ADR as the migration table."
  - "Do not treat ADR as the live handoff."
  - "Do not treat ADR as Root."
  - "Do not treat _thread-index/ as Mission Card output folder."
  - "Do not treat thread-meta_card-craft.md as replacement for thread-index_card-craft.md."
  - "Do not skip Reality Response."
  - "Do not bulk migrate before Pilot."
  - "Do not restore retired Query layer by inertia."
```

---

## §14. Next Gate / Human-AI Collaboration Status

```yaml id="next-gate"
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
      - "japanese-first-okf"
      - "github_canonical"
      - "human_editable"
      - "not_final_seal"

  next_recommended_action:
    - "Run Reality Response check on ADR + Protocol Registry + _thread-index/ README"
    - "Do not start Ark01 bulk migration yet"
    - "Do not make future commits without explicit Human Final Seal"
```
