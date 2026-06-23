---
title: "Ark Repository Governance ADR"
status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
document_identity: "repository_governance_adr"
canonical_path: "_projects/ark/indexes/ark-repository-governance_adr.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
adr_id: "ark-repository-governance-adr"
adr_version: "v002"
ai_side_review_status: "living_review_applied"
github_canonicalization: "created_by_explicit_user_request / revised_by_reality_response"
updated_reason:
  - "Convert to Japanese-first OKF"
  - "Reflect _thread-end topology"
  - "Clarify what the previous-thread AI was trying to accomplish"
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

# Ark Repository Governance ADR

## §0. Status / Decision Summary

このADRは、Ark repository structure のためのGitHub正準Governance文書である。

この文書の目的は、ファイルを大量に作ることではない。  
目的は、Future AIが **Source / Protocol / Harvest / Mission / Handoff / Index / Archive** を誤読しないように、文書身分と住所の決定原則を固定することである。

このADRのGitHub作成・更新は、Ark01 migration、Bulk Migration、Mission Card作成、Final Sealを自動承認しない。

```yaml id="adr-status"
adr_status:
  document_identity: "repository_governance_adr"
  status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
  canonical_path: "_projects/ark/indexes/ark-repository-governance_adr.md"
  adr_version: "v002"
  future_github_commit_requires_human_final_seal: true
  tail_rule_version: "v0.8"
  ai_living_review_default: true
  human_editable_is_wait_state: false
```

### §0.1 King Sentence

```text id="king-sentence"
ファイルを置く場所を決めているのではない。
Future AIが誤読しない文書の身分と住所を定めている。
```

### §0.2 Core Decision

```text id="core-decision"
Directory structure is not storage.
Directory structure is interpretation.
```

日本語：

```text id="core-decision-ja"
Directory structureは保管場所ではない。
Directory structureは解釈である。
```

---

## §1. 前Thread AIは何をしたかったのか

前Thread AIは、単にRepositoryを複雑にしたかったのではない。  
本当にやろうとしていたことは、**ArkをGitHub上でFuture AIが誤読せず再起動できる状態にすること** だった。

特に守りたかったのは、次の区別である。

```yaml id="previous-ai-purpose"
previous_ai_purpose:
  protect_document_identity:
    - "ProtocolをHarvestと誤読しない"
    - "HarvestをMission Cardと誤読しない"
    - "handoff.mdをphase-level mapと誤読しない"
    - "phase-handoff.mdをlatest rolling pointerと誤読しない"
    - "RegistryをProtocol本文と誤読しない"

  prevent_wrong_migration:
    - "Ark01:01-26を一気にBulk Migrationしない"
    - "Pilot-firstでReality Responseを見る"
    - "local file名だけでGitHub正準住所を決めない"

  preserve_human_ai_collaboration:
    - "ReviewはAIが進める"
    - "Sealは人間が握る"
    - "human_editableをmandatory wait stateにしない"
```

圧縮すると：

```text id="intent-compression"
前Thread AIは、ファイルを増やしたかったのではない。
Future AIがArkの文書を取り違えないように、文書身分OSを作りたかった。
```

ただし、前Thread作成時点では、`_thread-end/` topologyやQuery layer削除がまだ起きていなかった。  
そのため、本v002では現在Realityに合わせて修正する。

---

## §2. Context / なぜこのADRが必要か

ArkのGitHub移行で危険なのは、移行が遅いことではない。  
危険なのは、**間違った正準構造を作ること** である。

Arkには、少なくとも以下が混在する。

```yaml id="context"
ark_contains:
  - "rolling handoff"
  - "phase handoff"
  - "primary thread harvest"
  - "mission card"
  - "protocol parent markdown"
  - "activation query"
  - "thread-end system"
  - "protocol registry"
  - "migration manifest"
  - "vision core"
  - "archive"
```

これらをfolder名だけで曖昧に置くと、Future AIは必ず誤読する。  
したがって、folder分類より前に、document_identityを固定する。

---

## §3. Root / Fruit Guard

RootはGitHubではない。  
RootはMarkdownではない。  
RootはADRではない。  
Rootはfolder structureではない。  
RootはAIではない。

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

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

Repository structureはFuture AIの航路を助ける。  
しかし、それはRootではない。

---

## §4. Ark File Ontology

```yaml id="ark-file-ontology"
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

  thread_end_system:
    definition: "Thread終了時のGate Router / Harvest Vessel / Handoff Builder family"
    canonical_root: "_thread-end/"
    active_files:
      - "_thread-end/README.md"
      - "_thread-end/thread-end.md"
      - "_thread-end/thread-harvest.md"
      - "_thread-end/thread-handoff.md"
    retired_layer:
      - "thread-end-gate1-query.md"
      - "thread-end-gate2-query.md"

  protocol_parent_markdown:
    definition: "Ark横断Protocol / Craft / Parent Specification"
    preferred_root: "s_special/"
    note: "Thread-End family is now _thread-end/, not s_special/."
    mutability: "versioned"

  activation_query:
    definition: "Future AIを起動するためのQuery / Runtime Adapter"
    preferred_root: "s_special/ or protocol-specific location"
    note: "Query layer may be retired when simpler router is better."
    mutability: "versioned / optional"

  vision_core:
    definition: "Ark-wide SS Vision Core / Naming Source Lens / Ark's eye"
    preferred_root: "ss_super-special/"
    mutability: "versioned / high guard"

  migration_manifest:
    definition: "local_path → github_path → document_identity 対応表"
    canonical_pattern: "_projects/ark/arkXX/indexes/*migration-manifest*.md"

  protocol_registry:
    definition: "Ark横断Protocol Markdownの住所録 / migration candidate registry"
    canonical_pattern: "_projects/ark/indexes/*protocol-registry*.md"

  archive:
    definition: "旧版・退避・非現行保存"
    canonical_pattern: "_archives/"
```

Short rule:

```text id="short-rule"
Protocolは上に置く。
Thread-Endは専用入口に置く。
Harvestは中に置く。
Missionは横に置く。
Handoffは入口に置く。
HistoryはGitに残す。
Archiveは奥に置く。
```

---

## §5. Current Placement Rules

### §5.1 _thread-end/

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

### §5.2 s_special/

```yaml id="placement-s-special"
s_special:
  role:
    - "Ark-wide protocol layer"
    - "Craft / Workflow specification layer"
    - "Format SSOT layer"
    - "Activation Query layer when still useful"
  note:
    - "Thread-End family moved to _thread-end/."
    - "Deleted Query files must not be restored unless they reduce confusion."
  must_not_be:
    - "Ark01 Harvest output"
    - "Ark02 Harvest output"
    - "Mission Card folder"
    - "rolling handoff"
```

### §5.3 ss_super-special/

```yaml id="placement-ss-super-special"
ss_super_special:
  role:
    - "Ark-wide SS Vision Core"
    - "Naming Source Lens"
    - "high-guard vision layer"
  examples:
    - "torah-vision-lens.md"
  must_not_be:
    - "normal protocol appendix"
    - "Gate2-owned local file"
    - "Ark01/Ark02 output artifact"
```

### §5.4 _projects/ark/indexes/

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

## §6. Handoff Layer Design

Use two layers.

```yaml id="handoff-layers"
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

```text id="handoff-compression"
handoff.md は動く鍵。
phase-handoff.md は動きにくい地図。
Git history は履歴台帳。
```

---

## §7. Harvest / Mission Card Separation

Primary Thread Harvest and Mission Card must not be mixed.

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

## §8. Protocol Registry Role

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

## §9. Document Identity Contract

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

## §10. Tail Rule v0.8 / human_editable Gate

Ark Repository Governanceでは、AIが実行しやすく、人間がCopy & Pasteで継続しやすいtail patternを使う。

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

Hard rule:

```yaml id="tail-order-rule-v0-8"
tail_order_rule_v0_8:
  fullrail_before_next_gate: true
  next_gate_last: true
  no_text_after_next_gate: true
```

---

## §11. Migration Strategy

Do not bulk migrate Ark01:01-26 first.  
Establish governance, then manifests and README skeletons, then run one pilot, then expand in small batches.

```yaml id="migration-strategy"
migration_strategy:
  phase_1_repository_governance_adr:
    target: "_projects/ark/indexes/ark-repository-governance_adr.md"
    status: "created / revised by explicit user request"

  phase_2_protocol_registry:
    target: "_projects/ark/indexes/ark-protocol-registry.md"
    status: "created / revised by explicit user request"

  phase_3_thread_end_system:
    target: "_thread-end/"
    status: "created / simplified / query layer retired"

  phase_4_phase_handoff:
    target: "_projects/ark/ark02/phase-handoff.md"
    create_after: "ADR and Registry are reality-aligned"

  phase_5_ark01_migration_manifest:
    target: "_projects/ark/ark01/indexes/ark01-migration-manifest.md"
    create_after: "Path policy and document identity policy are stable"

  phase_6_ark0101_pilot:
    scope:
      - "Ark0101 primary thread harvest"
      - "Ark0101 mission card"

  phase_7_small_batch_migration:
    rule: "small batches only after pilot Reality Response"
```

Pilot-first rule:

```text id="pilot-first"
Do not migrate all 26 Ark01 primary analyses at once.
First migrate Ark0101 primary harvest and Ark0101 mission card as a pilot.
Small Pilot creates Reality Response.
```

---

## §12. Consequences / Trade-offs

```yaml id="consequences"
benefits:
  - "Future AI can distinguish document roles"
  - "handoff.md remains lightweight"
  - "phase-handoff.md preserves phase context"
  - "Harvest and Mission Card do not overwrite each other"
  - "Protocol parent Markdown is not mistaken for Ark01 artifact"
  - "Protocol Registry stays as address book"
  - "Thread-End system is now simple and findable"
  - "Migration Manifest becomes simpler"
  - "Batch migration becomes safer"

costs:
  - "More initial planning"
  - "Need to maintain ADR / Registry / phase-handoff / manifest distinctions"
```

Trade-off judgment:

```text id="trade-off"
The main risk is not slow migration.
The main risk is wrong canonical structure.
```

Therefore, governance before migration is justified.

---

## §13. Reality Response Checkpoints

```yaml id="reality-response-checkpoints"
reality_response_checkpoints:
  after_adr:
    - "ADR is Japanese-first OKF enough?"
    - "ADR is still a decision record, not an essay?"
    - "Document identities are readable?"

  after_protocol_registry:
    - "Registry is address book, not body?"
    - "Current _thread-end topology is reflected?"
    - "Retired Query layer is not active canonical?"

  after_thread_end_system:
    - "README -> thread-end -> harvest/handoff feels natural?"
    - "thread-end.md remains light router?"
    - "thread-harvest.md and thread-handoff.md keep roles distinct?"

  after_phase_handoff_candidate:
    - "handoff.md and phase-handoff.md responsibilities are clear?"
    - "phase-handoff.md remains lightweight?"

  after_manifest_candidate:
    - "local_path → github_path mapping is clear?"
    - "document_identity is stable?"

  after_ark0101_pilot:
    - "GitHub UI feels natural?"
    - "iPhone display is readable?"
    - "AI can fetch by canonical path?"
    - "Mission Card is not mistaken for Primary Harvest?"
```

Reality Response is not optional.  
It is the field-test gate.

---

## §14. Stop Conditions

```yaml id="stop-conditions"
stop_conditions:
  - "ADR becomes Migration Manifest"
  - "ADR becomes phase-handoff.md"
  - "ADR becomes README"
  - "ADR becomes too large to function as decision record"
  - "handoff.md is treated as phase-level stable map"
  - "phase-handoff.md is treated as rolling latest pointer"
  - "primary harvest and mission card are mixed"
  - "protocol parent Markdown is placed under Ark01 artifacts without registry"
  - "retired Query layer is treated as active canonical"
  - "Ark01:01-26 are bulk-migrated before Pilot"
  - "Human Final Seal is bypassed"
  - "human_editable is treated as mandatory wait state"
```

---

## §15. Living Review

### §15.1 私の判断

このADRは必要である。  
ただし、前Thread版は英語が強く、現在の `_thread-end/` Realityを反映していなかった。  
本v002では、Japanese-first OKFへ戻し、文書身分・住所・現在Topologyをより明確にした。

ArkがGitHub canonical structureへ移る時、危険なのはfile不足ではない。  
危険なのは、fileの身分を取り違えることである。

```text id="living-judgment"
Governanceは速度を落とすためではない。
間違った高速化を防ぐためにある。
```

### §15.2 違和感

ADRは大きくなりすぎてはいけない。  
ADRがManifestやREADMEやphase-handoffの代替になり始めたら、ADRではなくなる。

```text id="density-rule"
誤読を防ぐだけ十分。
実務表を置き換えないだけ軽量。
```

### §15.3 Hidden Pattern

```text id="hidden-pattern"
ADR protects Manifest.
Protocol Registry protects document identity.
_thread-end protects Thread-End runtime.
phase-handoff protects phase context.
handoff.md protects next-thread reboot.
Pilot protects Batch Migration.
Human Seal protects Commit.
Tail Rule protects continuation.
```

### §15.4 Misread Warning

```yaml id="misread-warning"
misread_warning:
  - "Do not treat ADR as the final repository map."
  - "Do not treat ADR as the migration table."
  - "Do not treat ADR as the live handoff."
  - "Do not treat ADR as Root."
  - "Do not skip Reality Response."
  - "Do not bulk migrate before Pilot."
  - "Do not restore retired Query layer by inertia."
```

---

## §16. Next Gate / Human-AI Collaboration Status

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
    - "Run Reality Response check on ADR + Protocol Registry"
    - "Do not start Ark01 bulk migration yet"
    - "Do not make future commits without explicit Human Final Seal"
```
