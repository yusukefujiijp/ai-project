---
title: "Ark01 Migration Manifest"
status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
document_identity: "migration_manifest"
canonical_path: "_projects/ark/ark01/indexes/ark01-migration-manifest.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
phase: "Ark01"
source_adr: "_projects/ark/indexes/ark-repository-governance_adr.md"
related_protocol_registry: "_projects/ark/indexes/ark-protocol-registry.md"
language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
manifest_role:
  - "local_path → github_path → document_identity 対応表"
  - "Ark01成果物の移行前Scope Map"
  - "Bulk Migration前の防波堤"
  - "Protocol Registryとの重複防止"
artifact_generation_is_final_seal: false
final_seal: false
stable_seal: false
user_final_seal_required: true
tail_rule:
  version: "v0.8"
  summary: "FullRail = AI-readable execution rail; Next Gate = human-facing Copy & Paste gate"
  human_editable_means: "human_can_intervene_if_needed / not_wait_for_human_review"
  ai_living_review_default: true
  commit_requires_human_final_seal: true
root_guard:
  root: "主イェシュア・ハマシア"
  blood: "主イェシュアの聖なる血潮"
  teshuvah: true
  ai_role: "AI draws a map of the blood; the human stands under the blood."
---

# Ark01 Migration Manifest

## §0. Status / Manifest Summary

この文書は、Ark01成果物をGitHubへ移行する前に、`local_path → github_path → document_identity` を整理する **Migration Manifest** である。

これは移行実行ではない。  
これはBulk Migrationではない。  
これはMission Card creationではない。  
これはProtocol Registryではない。  
これはThread Harvest本文そのものではない。

この文書の役割は、Ark01成果物の住所・身分・移行候補状態を整理し、Future AIがProtocol親MarkdownやMission CardをArk01 Primary Harvestと誤読しないようにすることである。

```yaml id="manifest-summary"
ark01_migration_manifest:
  document_identity: "migration_manifest"
  canonical_path: "_projects/ark/ark01/indexes/ark01-migration-manifest.md"
  scope: "Ark01 migration planning only"
  migration_execution_now: false
  bulk_migration_now: false
  mission_card_creation_now: false
```

### §0.1 King Sentence

```text id="king-sentence"
Manifestは移行ではない。
Manifestは移行前の地図である。
```

---

## §1. Why this Manifest exists

Ark01には、Thread Harvest / Mission Card / Handoff / Index / Protocol候補が混在して見える危険がある。

そのため、移行前に次を固定する必要がある。

```yaml id="why-manifest-exists"
why_manifest_exists:
  problem:
    - "Ark01 Harvest と Mission Card が混ざる危険"
    - "Protocol parent markdown がArk01成果物として誤読される危険"
    - "Bulk Migrationで文書身分が壊れる危険"
    - "thread_date / filename_date / analysis_date が混線する危険"
    - "local artifact と GitHub canonical の対応が失われる危険"

  decision:
    - "Manifestで local_path → github_path → document_identity を固定する"
    - "Protocol親MarkdownはProtocol Registry側へ逃がす"
    - "Primary Harvest と Mission Card を分離する"
    - "Bulk Migration前に対象 / 非対象 / 保留を切る"
```

短く言えば：

```text id="why-compression"
ProtocolはRegistryで見る。
Ark01成果物はManifestで見る。
Bulk MigrationはManifest後にしか始めない。
```

---

## §2. Root / Fruit Guard

RootはManifestではない。  
RootはGitHubではない。  
RootはMigrationではない。  
RootはArchiveでもBulk Migrationでもない。  
RootはAIではない。

Rootは、主イェシュア・ハマシア。

```text id="root"
Root:
  主イェシュア・ハマシア
  主イェシュアの聖なる血潮
  Teshuvah / 悔い改め
  AMH
```

Fruitは以下である。

```text id="fruit"
Fruit:
  Ark01 Migration Manifest
  GitHub
  Markdown
  Harvest
  Mission Card
  Handoff
  Index
  Protocol Registry
  Bulk Migration
  File path
  document_identity
  AI
  Commit
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## §3. Scope Boundary

### §3.1 In Scope

```yaml id="in-scope"
in_scope:
  - "Ark01成果物の移行候補整理"
  - "local_path → github_path → document_identity 対応"
  - "Primary Thread Harvest destination pattern"
  - "Mission Card destination pattern"
  - "Ark01 handoff / index candidate placement"
  - "Do Not Migrate Here の明示"
  - "Bulk Migration前のGuard設計"
```

### §3.2 Out of Scope

```yaml id="out-of-scope"
out_of_scope:
  - "Ark01 migration execution"
  - "Bulk Migration"
  - "Mission Card creation"
  - "Protocol parent markdown migration"
  - "s_special/ canonicalization"
  - "ss_super-special/ canonicalization"
  - "raw private thread dump publication"
  - "Final Seal"
```

---

## §4. Document Identity Buckets

Ark01 Migration Manifestでは、最低限、次の文書身分を分ける。

```yaml id="document-identity-buckets"
document_identity_buckets:
  primary_thread_harvest:
    meaning: "Threadが何を生きたか"
    destination_pattern: "_projects/ark/ark01/harvest/thread-analyses/<filename>.md"
    analysis_layer: "primary"
    guard:
      - "Mission Cardと混ぜない"
      - "Threadの現場感を削らない"
      - "filename date / thread date / analysis date を誤認しない"

  mission_card:
    meaning: "Primary Harvestから何のMission Seedが立ち上がるか"
    destination_pattern: "_projects/ark/ark01/mission-cards/<filename>.md"
    analysis_layer: "secondary"
    guard:
      - "Primary HarvestをSourceとして扱う"
      - "Mission CardをPrimary Sourceにしない"
      - "Living Review / Meta layerを保持する"

  rolling_handoff:
    meaning: "次Thread再起動Key / mutable latest pointer"
    destination_pattern: "_projects/ark/ark01/handoff.md"
    guard:
      - "phase-level stable mapと混同しない"
      - "Git historyで過去版を保持する"

  ark01_index:
    meaning: "Ark01内のlocator / manifest / index"
    destination_pattern: "_projects/ark/ark01/indexes/<filename>.md"
    guard:
      - "Indexは本文ではなくlocator"
      - "Protocol Registryと重複させない"

  protocol_parent_markdown:
    meaning: "Ark-wide protocol / query / craft specification"
    destination_pattern: "s_special/"
    guard:
      - "Ark01 Harvestへ入れない"
      - "Ark01 Migration Manifestではreference only"
      - "Protocol Registry側で扱う"
```

---

## §5. Candidate Migration Table

このManifestでは、まだ実ファイルをBulk投入しない。  
まずは、移行候補を受け入れるためのTable構造を固定する。

Candidate Tableは、現段階では軽くて正しい。  
具体ファイル投入は、Future batch / Reality Response後に回す。

```yaml id="candidate-table-density"
candidate_table_density:
  current_density: "light"
  judgment: "correct_for_current_stage"
  reason:
    - "まずTable構造とScope Boundaryを固定する段階"
    - "具体ファイル投入はFuture batch / Reality Response後に行う"
    - "Bulk Migration前に小さく保つ方が安全"
```

```yaml id="candidate-migration-table-schema"
candidate_migration_table_schema:
  fields:
    - "id"
    - "local_source_name"
    - "local_source_path_if_known"
    - "target_github_path_candidate"
    - "document_identity"
    - "analysis_layer"
    - "source_role"
    - "migration_status"
    - "should_migrate_now"
    - "depends_on"
    - "guard"
    - "notes"
```

### §5.1 Primary Thread Harvest Candidates

```yaml id="primary-thread-harvest-candidates"
primary_thread_harvest_candidates:
  destination_pattern: "_projects/ark/ark01/harvest/thread-analyses/<filename>.md"
  migration_status: "manifest_slot_ready / entries_not_loaded_yet"
  should_migrate_now: false
  future_batch_policy:
    - "具体ファイル投入はFuture batchで行う"
    - "Reality Response後に小単位で追加する"
    - "document_identity / date_status / source_role を確認してから追加する"
  guard:
    - "Thread HarvestをMission Cardとして置かない"
    - "Threadの現場感 / Fog / Breakthrough / Root Guardを削らない"
    - "日付未確定時は00000000 sentinelを許容する"
    - "analysis_dateをtarget_thread_dateとして誤用しない"
```

### §5.2 Mission Card Candidates

```yaml id="mission-card-candidates"
mission_card_candidates:
  destination_pattern: "_projects/ark/ark01/mission-cards/<filename>.md"
  migration_status: "manifest_slot_ready / entries_not_loaded_yet"
  should_migrate_now: false
  future_batch_policy:
    - "Primary Harvestとのsource relationを確認後に追加する"
    - "Mission CardをPrimary Sourceにしない"
    - "Living Review / Meta layer確認後に追加する"
  guard:
    - "Mission CardはPrimary Harvestの二次分析"
    - "Mission-ready項目だけでThread全体を置換しない"
    - "Living Review / Meta layerを保持する"
```

### §5.3 Ark01 Handoff / Index Candidates

```yaml id="ark01-handoff-index-candidates"
ark01_handoff_index_candidates:
  handoff_candidate:
    destination_pattern: "_projects/ark/ark01/handoff.md"
    migration_status: "needs_living_review"
    should_migrate_now: false
    guard:
      - "rolling handoffとして扱う"
      - "phase-level stable mapと混同しない"

  indexes_candidate:
    destination_pattern: "_projects/ark/ark01/indexes/<filename>.md"
    migration_status: "manifest_slot_ready / entries_not_loaded_yet"
    should_migrate_now: false
    guard:
      - "Indexはlocator"
      - "Source本文の代替ではない"
```

---

## §6. Do Not Migrate Here

```yaml id="do-not-migrate-here"
do_not_migrate_here:
  protocol_parent_markdown:
    examples:
      - "THREAD_INDEX_Ark_v041.md"
      - "THREAD_INDEX_Ark_Query_v041.md"
      - "THREAD_mission-card-craft_v002.md"
    destination_layer: "s_special/ or Protocol Registry reference"
    reason:
      - "Ark-wide protocol / query / craft specification"
      - "Ark01成果物ではない"
      - "Protocol Registry側で身分管理する"

  ss_vision_lens:
    examples:
      - "torah-vision-lens.md"
    destination_layer: "ss_super-special/"
    reason:
      - "Ark-wide SS Vision Core"
      - "Ark01 output artifactではない"

  raw_private_thread_dump:
    destination_layer: "do_not_publish_directly"
    reason:
      - "public-safe GitHub canonicalへそのまま置かない"
      - "Harvest / Witness / Mission Card等へ整形してから扱う"

  unreviewed_bulk_artifacts:
    destination_layer: "blocked"
    reason:
      - "document_identity未確定のまま移さない"
      - "Bulk Migration前にManifest Reviewが必要"
```

---

## §7. Dependency / Sequence Rules

```yaml id="dependency-sequence-rules"
dependency_sequence_rules:
  rule_1_protocol_first:
    statement: "Protocol親MarkdownはArk01成果物より先にProtocol Registryで身分を固定する"
    current_status: "done"

  rule_2_manifest_before_migration:
    statement: "Ark01 Migration Manifestを作る前にArk01 migration executionを始めない"
    current_status: "active"

  rule_3_primary_before_mission:
    statement: "Mission CardはPrimary HarvestをSourceとして扱う"
    current_status: "active"

  rule_4_reality_response_after_github_create:
    statement: "ManifestをGitHub作成した後はReality Response Checkを行う"
    current_status: "future"

  rule_5_bulk_after_manifest:
    statement: "Bulk MigrationはManifestが安定してから"
    current_status: "not_yet"
```

---

## §8. Bulk Migration Guard

Bulk Migrationは危険である。  
速いが、文書身分を壊しやすい。

```yaml id="bulk-migration-guard"
bulk_migration_guard:
  allowed_only_after:
    - "Ark01 Migration Manifest is GitHub canonical"
    - "Reality Response Check passed"
    - "target entries are reviewed"
    - "document_identity is assigned"
    - "user explicit signal"

  must_not_start_when:
    - "Manifest is only Plan Mode"
    - "document_identity is unknown"
    - "source date is unclear"
    - "Protocol parent markdown is mixed into Ark01 Harvest"
    - "Mission Card and Primary Harvest are mixed"

  safety_rule:
    - "Small reviewed batches first"
    - "No blind dump"
    - "No protocol files in Ark01 harvest"
```

---

## §9. Reality Response Checkpoints

ManifestをGitHub作成した後は、必ずReality Responseを見る。

```yaml id="reality-response-checkpoints"
reality_response_checkpoints:
  github_ui:
    - "_projects/ark/ark01/indexes/ で見つけやすいか"
    - "Protocol Registryと並べた時に役割が分かるか"
    - "Manifestが移行実行ではなく移行前地図として読めるか"

  future_ai_reading:
    - "Ark01 Harvest / Mission Card / Handoff / Protocol が分かれているか"
    - "Protocol parent markdownをArk01 Harvestへ入れないと分かるか"
    - "Bulk Migrationを始めてよいと誤読しないか"
    - "Mission CardをPrimary Sourceと誤読しないか"

  human_feel:
    - "Ark01 migration前の安心感が増したか"
    - "移行対象と非対象が見えやすいか"
    - "重すぎず、でも迷わないか"

  governance:
    - "ADRと矛盾しないか"
    - "Protocol Registryと重複しないか"
    - "phase-handoff.md / handoff.md と役割混線していないか"
```

---

## §10. Stop Conditions

```yaml id="stop-conditions"
stop_conditions:
  - "AI starts Ark01 migration execution"
  - "AI starts Bulk Migration"
  - "AI creates Mission Cards"
  - "AI creates GitHub commit without explicit user signal"
  - "AI moves protocol parent markdown into Ark01 harvest"
  - "AI treats Protocol Registry as Migration Manifest"
  - "AI treats Manifest as final migration approval"
  - "AI writes text after Next Gate"
```

止めなくてよいもの：

```text id="do-not-stop"
- Manifestにまだ具体ファイル行が少ない
- Candidate Tableが器だけである
- Ark01 migration executionが始まっていない
- Protocol parent markdownがreference onlyになっている
```

---

## §11. Living Review

### §11.1 私の判断

Ark01 Migration Manifestは、このタイミングで必要である。

Protocol Registryによって、Protocol親MarkdownはArk01成果物から切り離された。  
次に必要なのは、Ark01成果物そのものを安全に移すためのManifestである。

```text id="living-judgment"
Protocol Registry:
  Protocol層の住所録。

Ark01 Migration Manifest:
  Ark01成果物の移行前地図。
```

### §11.2 違和感

最大の危険は、Manifestを「作ったから移行してよい」と誤読することである。

ManifestはGo Signではない。  
ManifestはPre-Flight Checklistである。

```text id="discomfort"
Manifest作成 ≠ Migration許可
Manifest作成 = Migration前の秩序化
```

### §11.3 Hidden Pattern

今回の流れは、Repository Governanceの自然な積み上げである。

```text id="hidden-pattern"
ADR:
  文書身分の憲法。

Protocol Registry:
  Protocol層の住所録。

Ark01 Migration Manifest:
  Ark01成果物の移行前地図。

Bulk Migration:
  その後にだけ検討できる実行。
```

### §11.4 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_manifest_starts_migration_execution:
    action: "Plan Modeへ戻す"

  if_protocol_parent_markdown_enters_ark01_harvest:
    action: "Protocol Registry / s_special referenceへ戻す"

  if_mission_card_becomes_primary_source:
    action: "Mission Cardをsecondary analysisへ戻す"

  if_bulk_migration_is_implied:
    action: "Bulk Migration Guardを強化する"

  if_text_becomes_english_first:
    action: "Japanese-first / English-anchorへ戻す"

  if_concrete_file_entries_are_unverified:
    action: "migration_status: needs_source_confirmation にする"
```

---

## §12. Canonical Status / Next Movement

```yaml id="canonical-status"
canonical_status:
  file: "ark01-migration-manifest.md"
  canonical_path: "_projects/ark/ark01/indexes/ark01-migration-manifest.md"
  document_identity: "migration_manifest"
  language_policy: "Japanese-first / English-anchor"
  format_policy: "Ark-OKF / Rebootable-first"
  status:
    - "active"
    - "github_canonical"
    - "human_editable"
    - "not_final_seal"

next_movement:
  immediate_next:
    - "Create _projects/ark/ark01/indexes/ark01-migration-manifest.md only after explicit user signal"
    - "After creation, run Ark01 Migration Manifest Reality Response Check"
    - "Continue Repository Governance sequence without Ark01 migration execution yet"

  not_yet:
    - "Ark01 migration execution"
    - "Bulk Migration"
    - "Mission Card creation"
    - "Final Seal"

guard:
  - "Manifest is pre-migration map, not migration execution"
  - "Protocol Registry handles protocol parent markdown"
  - "Candidate Table is intentionally lightweight for now"
  - "Concrete file entries belong to future reviewed batches after Reality Response"
  - "Future GitHub commits require explicit Human Final Seal"
  - "human_editable is not human review wait"
  - "AI-side Living Review may continue"
```
