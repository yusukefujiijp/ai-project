---
title: "Ark Protocol Registry"
status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
document_identity: "protocol_registry"
canonical_path: "_projects/ark/indexes/ark-protocol-registry.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
source_adr: "_projects/ark/indexes/ark-repository-governance_adr.md"
registry_version: "v002"
updated_reason:
  - "Reality Response after _thread-end topology migration"
  - "Retired Thread-End Query layer"
  - "Current canonical paths corrected"
language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
registry_role:
  - "Ark-wide Protocol Markdown address book"
  - "document identity / path / role / status registry"
  - "Future AI misread prevention map"
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

# Ark Protocol Registry

## §0. Status / Registry Summary

この文書は、Ark Project全体で使う Protocol / Query / Craft / Format / Vision Lens 系Markdownの **住所録 / Registry** である。

これはProtocol本文の複製ではない。  
これはArk01 Harvestではない。  
これはArk02 Harvestではない。  
これはMission Cardではない。  
これはrolling handoffではない。  
これはBulk Migration Manifestではない。

この文書の役割は、Future AIがMarkdownの **住所・身分・役割・状態** を誤読しないように、軽量に固定することである。

```text id="king-sentence"
Registryは本文ではない。
Registryは住所録である。
```

```yaml id="registry-summary"
protocol_registry:
  document_identity: "protocol_registry"
  canonical_path: "_projects/ark/indexes/ark-protocol-registry.md"
  version: "v002"
  language_policy: "Japanese-first / English-anchor"
  format_policy: "Ark-OKF / Rebootable-first"
  user_final_seal_required: true
```

---

## §1. 前Thread AIは何をしたかったのか

前Thread AIが一所懸命作ろうとしていたものは、Protocol本文ではなく、**Future AIが誤読しないための文書身分地図** である。

狙いは次の3つだった。

```yaml id="previous-ai-intent"
previous_ai_intent:
  1_prevent_misclassification:
    meaning: "Protocol / Query / Craft / Harvest / Mission / Handoffを混同させない"

  2_lock_addresses_before_migration:
    meaning: "Ark01/Ark02 migration前に、どのfileが何者かを先に定義する"

  3_make_future_ai_rebootable:
    meaning: "Future AIがGitHub上のpathだけで迷わず再起動できるようにする"
```

短く言えば：

```text id="intent-compression"
前Thread AIは、ファイルを増やしたかったのではない。
Future AIの誤読を減らすために、住所録を作りたかった。
```

---

## §2. なぜ Protocol Registry が必要か

Arkには、Thread HarvestやMission Cardとは別に、AI実行を導くProtocol親Markdownが存在する。

これらは、Ark01やArk02の成果物ではない。  
これらは、Future AIがどのRailで、どのGateを、どのSource Boundaryで実行するかを決めるための **Ark-wide protocol layer** である。

ただし、すべてのProtocolを `s_special/` に置く必要はない。  
現在、Thread-End familyは `_thread-end/` に集約済みである。

```text id="why-compression"
Protocolは上に置く。
Thread-Endは専用入口に置く。
Harvestは中に置く。
Missionは横に置く。
Handoffは入口に置く。
Registryは住所録として守る。
```

---

## §3. Root / Fruit Guard

RootはGitHubではない。  
RootはMarkdownではない。  
RootはProtocol Registryではない。  
Rootは `_thread-end/` でも `s_special/` でも `ss_super-special/` でもない。  
RootはAIではない。

Rootは、主イェシュア・ハマシア。

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
  Protocol Registry
  _thread-end/
  s_special/
  ss_super-special/
  Thread-End
  Gate 1
  Gate 2
  Thread Harvest
  Ark-OKF
  THREAD_INDEX
  Mission Card Craft
  Query
  Full Rail
  Next Gate
  AI
  Commit
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## §4. Registry Scope

### §4.1 In Scope

```yaml id="in-scope"
in_scope:
  - "_thread-end/ Thread-End system files"
  - "s_special/ protocol parent markdown"
  - "s_special/ craft / workflow specification markdown"
  - "s_special/ format SSOT markdown"
  - "ss_super-special/ high-guard vision lens"
  - "confirmed GitHub canonical protocol files"
  - "migration candidate protocol files"
  - "retired / deleted protocol layers when needed for history"
  - "document_identity / canonical_path / role / status / relation"
```

### §4.2 Out of Scope

```yaml id="out-of-scope"
out_of_scope:
  - "Protocol本文の全文複製"
  - "Ark01 migration実行"
  - "Ark02 harvest作成"
  - "Mission Card作成"
  - "Bulk Migration"
  - "rolling handoff更新"
  - "phase-handoff.md更新"
  - "Final Seal"
```

---

## §5. Confirmed GitHub Canonical Protocols

ここでは、すでにGitHub canonical pathで確認済みのProtocol系Markdownを名簿化する。

Registryなので、本文は複製しない。  
住所・身分・役割・誤読Guardだけを保持する。

```yaml id="confirmed-github-canonical-protocols"
confirmed_github_canonical_protocols:
  - path: "_thread-end/README.md"
    document_identity: "thread_end_folder_front_door"
    canonical_name: "_thread-end README"
    class: "S"
    status: "folder_front_door / living_index / topology_map"
    role:
      - "Thread-End System Folderの入口"
      - "Read Order / Topology Map"
      - "Future AI path confusion guard"
    must_not_be:
      - "Thread-End runtime body"
      - "Harvest builder"
      - "Handoff product"

  - path: "_thread-end/thread-end.md"
    document_identity: "thread_end_parent_map"
    canonical_name: "Thread-End Parent Map"
    class: "SS"
    status: "living_ssot"
    role:
      - "Thread-End Workflowの親Map"
      - "Single Front Door / Multi-Gate Router"
      - "Gate 1 / Gate 2 relation map"
      - "handoff.md required at Thread transfer"
    anchor_formula:
      - "Gate 1 fixes files"
      - "Gate 2 harvests meaning"
      - "All-in-one entrypoint, not all-in-one body"
    must_not_be:
      - "Harvest body generator"
      - "Handoff body generator"
      - "Mission Card"
      - "rolling handoff"

  - path: "_thread-end/thread-harvest.md"
    document_identity: "harvest_vessel"
    canonical_name: "Thread Harvest"
    class: "S"
    status: "living_ssot"
    parent_map: "_thread-end/thread-end.md"
    gate_role: "Gate 2 / Thread Harvest"
    rail: "next_thread"
    role:
      - "Gate 2 Thread Harvest vessel"
      - "rebootable meaning harvest structure"
      - "Thread Naming + Extreme BrainDump core"
    anchor_formula:
      - "Thread Harvest is not summary"
      - "Thread Harvest leaves meaning / heat / Seed / Next Compass"
      - "Harvest is material; Handoff is ignition key"
    must_not_be:
      - "ordinary summary"
      - "Mission Card"
      - "rolling handoff"

  - path: "_thread-end/thread-handoff.md"
    document_identity: "handoff_builder"
    canonical_name: "Thread-Handoff Builder"
    class: "S-candidate"
    status: "living_candidate / human_editable / not_final_seal"
    parent_map: "_thread-end/thread-end.md"
    sibling_builder: "_thread-end/thread-harvest.md"
    generated_product: "handoff.md"
    role:
      - "Handoff Builder / Next-thread Ignition Manual"
      - "handoff.md生成のBuilder Manual"
    anchor_formula:
      - "thread-handoff.md is Builder"
      - "handoff.md is generated product"
    must_not_be:
      - "handoff.md itself"
      - "Harvest body"
      - "rolling handoff"

  - path: "s_special/ark-open-knowledge-format.md"
    document_identity: "format_ssot"
    canonical_name: "Ark-OKF"
    class: "S"
    status: "living_ssot"
    paired_query: "s_special/ark-open-knowledge-format_query.md"
    pair_policy: "Engine / Ignition Key"
    query_is_not_ssot: true
    language_policy: "Japanese-first / English-anchor"
    role:
      - "Answer Interoperability Surface"
      - "AI回答を readable / reusable / rebootable / handoff-ready にするFormat"
      - "Japanese-first / English-anchor / Rebootable-first の正準SSOT"
    must_not_be:
      - "English-first rule"
      - "fixed content template"
      - "replacement for Living Review"
```

---

## §6. Retired / Deleted Thread-End Layer

Thread-End Query layerは、現在の運用では削除済みである。  
これは失敗ではなく、KISS / DRY / YAGNI / Lean による単純化である。

```yaml id="retired-thread-end-layer"
retired_thread_end_layer:
  deleted_or_retired:
    - path: "ss_super-special/thread-end.md"
      previous_role: "old primary / promoted parent map"
      current_status: "deleted / replaced by _thread-end/thread-end.md"

    - path: "s_special/thread-end.md"
      previous_role: "legacy redirect stub"
      current_status: "deleted / replaced by _thread-end/thread-end.md"

    - path: "s_special/thread-end-gate1-query.md"
      previous_role: "Gate 1 activation query"
      current_status: "deleted / query layer retired"

    - path: "s_special/thread-end-gate2-query.md"
      previous_role: "Gate 2 activation query"
      current_status: "deleted / query layer retired"

    - path: "_thread-end/thread-end-gate1-query.md"
      previous_role: "Gate 1 activation query after migration"
      current_status: "deleted / query layer retired"

    - path: "_thread-end/thread-end-gate2-query.md"
      previous_role: "Gate 2 activation query after migration"
      current_status: "deleted / query layer retired"

    - path: "s_special/thread-harvest.md"
      previous_role: "Thread Harvest vessel"
      current_status: "moved to _thread-end/thread-harvest.md"

    - path: "s_special/thread-handoff.md"
      previous_role: "Thread-Handoff Builder"
      current_status: "moved to _thread-end/thread-handoff.md"
```

Active readではなく、移行履歴としてのみ扱う。

```text id="retired-guard"
Deleted Query files are history.
Do not restore them unless they reduce confusion more than the current simple topology.
```

---

## §7. High-Guard Vision Layer

`ss_super-special/` は通常のProtocol置き場ではない。  
これはArk-wideのVision Lens / Naming Source Lensを置く高Guard層である。

```yaml id="ss-super-special"
ss_super_special:
  preferred_root: "ss_super-special/"
  role:
    - "Ark-wide SS Vision Core"
    - "Naming Source Lens"
    - "high-guard vision layer"
  current_known_entry:
    path: "ss_super-special/torah-vision-lens.md"
    document_identity: "vision_core"
    role:
      - "Ark-wide SS Vision Core"
      - "Ark's eye"
      - "Naming Source Lens"
  must_not_be:
    - "Gate2-owned local file"
    - "normal protocol appendix"
    - "Ark01/Ark02 output artifact"
```

Guard：

```text id="vision-guard"
Torah Vision Lensは、必要な時にScene-to-Name-to-Gateを明瞭にするLensである。
しかし、すべてのThreadに無理やりSceneを作らせるものではない。
```

---

## §8. Migration Candidate Protocols

ここでは、ADR上で候補化されているが、現時点ではGitHub canonical pathで未確認のProtocol親Markdownを名簿化する。

```yaml id="migration-candidate-protocols"
migration_candidates:
  - candidate_path: "s_special/thread-index-ark_v041.md"
    source_name: "THREAD_INDEX_Ark_v041.md"
    document_identity: "protocol_parent_markdown"
    status: "migration_candidate / not_github_canonical_yet"
    role:
      - "Ark Thread Index protocol"
      - "Root Thread Distillation Guard"
      - "Mission Card前のThread蒸留Protocol"
    must_not_be:
      - "Ark01 Harvest artifact"
      - "Mission Card"
      - "rolling handoff"

  - candidate_path: "s_special/thread-index-ark-query_v041.md"
    source_name: "THREAD_INDEX_Ark_Query_v041.md"
    document_identity: "activation_query"
    status: "migration_candidate / not_github_canonical_yet"
    role:
      - "THREAD_INDEX activation query"
      - "Plan Mode first"
      - "FullRail activation guard"
      - "Root Thread Distillation起動Query"
    must_not_be:
      - "SSOT protocol body"
      - "Ark01 Harvest artifact"
      - "Mission Card"

  - candidate_path: "s_special/thread-mission-card-craft_v002.md"
    source_name: "THREAD_mission-card-craft_v002.md"
    document_identity: "craft_protocol"
    status: "migration_candidate / not_github_canonical_yet"
    role:
      - "Mission Card Craft specification"
      - "single source markdown to single mission card"
      - "Living Review required"
      - "FullRail Tail Guard"
    must_not_be:
      - "Mission Card output"
      - "Ark01 primary harvest"
      - "Bulk generation script"
```

---

## §9. Document Identity Rules

Protocol Registryでは、最低限、次の身分を区別する。

```yaml id="document-identity-rules"
document_identity_rules:
  thread_end_folder_front_door:
    meaning: "Thread-End system folderの入口 / Read Order"
    example:
      - "_thread-end/README.md"

  thread_end_parent_map:
    meaning: "Thread-End Workflow親Map / Runtime Router"
    example:
      - "_thread-end/thread-end.md"

  harvest_vessel:
    meaning: "Harvestを実行するためのVessel / structure"
    example:
      - "_thread-end/thread-harvest.md"

  handoff_builder:
    meaning: "handoff.mdを作るためのBuilder Manual"
    example:
      - "_thread-end/thread-handoff.md"

  protocol_parent_markdown:
    meaning: "Ark-wide protocol body / specification"
    example:
      - "thread-index-ark_v041.md"

  activation_query:
    meaning: "Future AIを起動するQuery / Runtime Adapter"
    guard:
      - "Query is not always SSOT"
      - "Query may be retired if a simpler router exists"

  craft_protocol:
    meaning: "成果物生成のCraft仕様"

  format_ssot:
    meaning: "回答Format / interoperability surface のSSOT"

  vision_core:
    meaning: "Ark-wide high-guard vision / naming lens"
```

---

## §10. Placement Rules

### §10.1 _thread-end/

```yaml id="placement-thread-end"
_thread_end:
  role:
    - "Thread-End system folder"
    - "Gate Router / Harvest Vessel / Handoff Builder home"
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

### §10.2 s_special/

```yaml id="placement-s-special"
s_special:
  role:
    - "Ark-wide protocol layer"
    - "Craft / Workflow specification layer"
    - "Format SSOT layer"
    - "Activation Query layer when still useful"
  examples:
    - "ark-open-knowledge-format.md"
    - "thread-index-ark_v041.md candidate"
    - "thread-mission-card-craft_v002.md candidate"
  note:
    - "Thread-End family is now _thread-end/, not s_special/."
  must_not_be:
    - "Ark01 Harvest output"
    - "Ark02 Harvest output"
    - "Mission Card folder"
    - "rolling handoff"
```

### §10.3 ss_super-special/

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

### §10.4 _projects/ark/indexes/

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

## §11. Update Policy

```yaml id="update-policy"
update_policy:
  protocol_registry:
    path: "_projects/ark/indexes/ark-protocol-registry.md"
    update_frequency: "low / when protocol layer changes"
    update_style:
      - "add path / identity / role / status"
      - "do not copy full protocol body"
      - "separate confirmed canonical / migration candidate / retired layer"
    version_memory: "Git history"

  confirmed_github_canonical_entries:
    update_when:
      - "new protocol file becomes GitHub canonical"
      - "role / path / identity changes"
      - "status changes from candidate to living_ssot"
      - "Thread-End topology changes"

  retired_entries:
    update_when:
      - "file is deleted"
      - "Query layer is retired"
      - "old canonical path is replaced"
```

Stop condition：

```text id="registry-update-stop"
RegistryがProtocol本文の代替になり始めたら止める。
Registryは住所録へ戻す。
```

---

## §12. Reality Response Checkpoints

```yaml id="reality-response"
reality_response_checkpoints:
  github_ui:
    - "_projects/ark/indexes/ で見つけやすいか"
    - "ADRと並べた時に役割が分かるか"
    - "_thread-end/ と registry の関係が分かるか"

  future_ai_reading:
    - "_thread-end/ がThread-End system folderだと分かるか"
    - "s_special/ がProtocol層だと分かるか"
    - "QueryがSSOT本文ではない場合を誤読しないか"
    - "retired/deleted layer と active canonical を区別できるか"
    - "migration_candidate と github_canonical を区別できるか"

  human_feel:
    - "Protocol層の見通しが良くなったか"
    - "Registryが住所録として軽いか"
    - "古いPathを見て混乱しないか"

  ark_governance:
    - "Repository Governance ADRに従っているか"
    - "phase-handoff.mdと役割重複していないか"
    - "Ark01 Migration Manifestへ入れるべき内容を持ち込んでいないか"
```

Reality Responseは任意ではない。  
現場で効いているかを見るGateである。

---

## §13. Stop Conditions

```yaml id="stop-conditions"
stop_conditions:
  - "RegistryがProtocol本文の全文複製になる"
  - "Protocol parent markdownをArk01 Harvestとして分類する"
  - "Activation Queryを無条件にSSOTとして扱う"
  - "retired/deleted layerをactive canonicalと誤表示する"
  - "migration_candidateをgithub_canonicalと誤表示する"
  - "Ark01 migration detailsが入り込む"
  - "Mission Card creationが始まる"
  - "Bulk Migrationが始まる"
  - "GitHub Commitが明示Human Final Sealなしに行われる"
  - "human_editableがmandatory wait stateとして扱われる"
```

止めなくてよいもの：

```text id="do-not-stop"
- Registryが本文を複製していない
- Entriesが短い
- confirmed / candidate / retired が分かれている
- すべての将来Protocolをまだ網羅していない
```

---

## §14. Living Review

### §14.1 私の判断

Protocol Registryは必要である。

ただし、Registryは「現在のGitHub reality」を追う必要がある。  
Thread-End familyが `_thread-end/` へ移り、Query layerが削除された以上、旧 `s_special/thread-end*` をactive canonicalとして残すのは誤読リスクになる。

Registryは、Protocolたちを束ねる本文ではない。  
Registryは、Protocolたちの住所録である。

```text id="living-judgment-compression"
Protocol本文は各canonical fileにある。
Protocol身分は Registry で見る。
Thread-End systemは _thread-end/ にある。
```

### §14.2 違和感

最大の危険は、Registryを大きくしすぎること。

本文を複製し始めた瞬間、RegistryはRegistryではなくなる。  
だから、各Entryは短く、しかし文書身分は明確にする。

```text id="density-rule"
迷わないだけ十分。
本文を置き換えないだけ軽量。
```

### §14.3 Hidden Pattern

```text id="hidden-pattern"
ADR:
  なぜ文書身分が必要か。

Protocol Registry:
  どのProtocolが何者か。

_thread-end/:
  Thread-End system folder。

s_special/:
  実際のProtocol / Craft / Format本文。

ss_super-special/:
  Vision Lens。

Ark01 Migration Manifest:
  local_path → github_path の実務表。
```

### §14.4 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_registry_becomes_full_protocol_body:
    action: "本文複製を削り、path / identity / role / statusへ戻す"

  if_protocol_parent_markdown_is_classified_as_ark01_harvest:
    action: "document_identityをprotocol_parent_markdownへ戻す"

  if_activation_query_is_confused_with_ssot:
    action: "query_is_not_ssot / paired_query / retired statusを明記する"

  if_retired_query_is_used_as_active_read:
    action: "active canonicalから外し、retired layerへ戻す"

  if_ark01_migration_details_enter:
    action: "Ark01 Migration Manifestへ送る"

  if_text_becomes_english_first:
    action: "Japanese-first / English-anchorへ戻す"
```

---

## §15. Canonical Status / Next Movement

```yaml id="canonical-status"
canonical_status:
  file: "ark-protocol-registry.md"
  canonical_path: "_projects/ark/indexes/ark-protocol-registry.md"
  document_identity: "protocol_registry"
  language_policy: "Japanese-first / English-anchor"
  format_policy: "Ark-OKF / Rebootable-first"
  status:
    - "active"
    - "github_canonical"
    - "human_editable"
    - "not_final_seal"

next_movement:
  immediate_next:
    - "Reality Response check after registry refresh"
    - "Continue governance sequence without Ark01 bulk migration"

  not_yet:
    - "Ark01 migration"
    - "Bulk Migration"
    - "Mission Card creation"
    - "Final Seal"

guard:
  - "Future GitHub commits require explicit Human Final Seal"
  - "Registry is address book, not full protocol body"
  - "human_editable is not human review wait"
  - "AI-side Living Review may continue"
```
