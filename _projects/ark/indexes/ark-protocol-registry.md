---
title: "Ark Protocol Registry"
status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
document_identity: "protocol_registry"
canonical_path: "_projects/ark/indexes/ark-protocol-registry.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
source_adr: "_projects/ark/indexes/ark-repository-governance_adr.md"
language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
registry_role:
  - "Ark-wide Protocol Markdown registry"
  - "s_special / ss_super-special document identity map"
  - "migration candidate registry"
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

この文書は、Ark Project全体で使う Protocol / Query / Craft / Format / Vision Lens 系Markdownの **文書身分Registry** である。

これはProtocol本文の複製ではない。  
これはArk01 Harvestではない。  
これはArk02 Harvestではない。  
これはMission Cardではない。  
これはrolling handoffではない。  
これはBulk Migration Manifestではない。

この文書の役割は、Future AIが `s_special/` や `ss_super-special/` のMarkdownをArk01/Ark02成果物と誤読しないように、住所・身分・役割・状態を軽量に固定することである。

```yaml id="registry-summary"
protocol_registry:
  document_identity: "protocol_registry"
  canonical_path: "_projects/ark/indexes/ark-protocol-registry.md"
  language_policy: "Japanese-first / English-anchor"
  format_policy: "Ark-OKF / Rebootable-first"
  user_final_seal_required: true
```

### §0.1 King Sentence

```text id="king-sentence"
Registryは本文ではない。
Registryは住所録である。
```

---

## §1. なぜ Protocol Registry が必要か

Arkには、Thread HarvestやMission Cardとは別に、AI実行を導くProtocol親Markdownが存在する。

これらは、Ark01やArk02の成果物ではない。  
これらは、Future AIがどのRailで、どのGateを、どのSource Boundaryで実行するかを決めるための **Ark-wide protocol layer** である。

特に、`THREAD_INDEX` / `Query` / `Craft` / `Thread-End` / `Harvest Vessel` / `Ark-OKF` は、成果物ではなく、成果物を作るための道・型・起動Keyである。

```yaml id="why-registry-exists"
why_protocol_registry_exists:
  problem:
    - "Protocol parent markdown can be misread as Ark01/Ark02 artifact"
    - "Activation Query can be misread as SSOT"
    - "Craft spec can be misread as Mission Card output"
    - "Thread Harvest vessel can be misread as ordinary Harvest artifact"
    - "Ark01 migration before protocol identity lock creates drift"

  decision:
    - "Create a lightweight protocol registry"
    - "Separate confirmed GitHub canonical files from migration candidates"
    - "Do not copy full protocol bodies"
    - "Record path / identity / role / status / relation only"
```

短く言えば：

```text id="why-compression"
Protocolは上に置く。
Harvestは中に置く。
Missionは横に置く。
Handoffは入口に置く。
Registryは住所録として守る。
```

---

## §2. Root / Fruit Guard

RootはGitHubではない。  
RootはMarkdownではない。  
RootはProtocol Registryではない。  
Rootは `s_special/` ではない。  
Rootは `ss_super-special/` ではない。  
RootはThread-EndでもArk-OKFでもない。  
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
  GitHub
  Markdown
  Protocol Registry
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

このRegistryもFruitであり、Rootではない。

---

## §3. Registry Scope

### §3.1 In Scope

```yaml id="in-scope"
in_scope:
  - "s_special/ protocol parent markdown"
  - "s_special/ activation query markdown"
  - "s_special/ craft / workflow specification markdown"
  - "s_special/ format SSOT markdown"
  - "ss_super-special/ high-guard vision lens"
  - "confirmed GitHub canonical protocol files"
  - "migration candidate protocol files"
  - "document_identity / canonical_path / role / status / relation"
```

### §3.2 Out of Scope

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

## §4. Confirmed GitHub Canonical Protocols

ここでは、すでにGitHub canonical pathで確認済みのProtocol系Markdownを名簿化する。

Registryなので、本文は複製しない。  
住所・身分・役割・誤読Guardだけを保持する。

```yaml id="confirmed-github-canonical-protocols"
confirmed_github_canonical_protocols:
  - path: "s_special/thread-end.md"
    document_identity: "thread_end_parent_map"
    canonical_name: "Thread-End Parent Map"
    class: "S"
    status: "living_ssot"
    source_bootstrap: "S_thread-end_v001.md"
    role:
      - "Thread-End Workflowの親Map"
      - "Gate 1 / Gate 2 relation map"
      - "handoff.md required at Thread transfer"
    anchor_formula:
      - "Gate 1 fixes files"
      - "Gate 2 harvests meaning"
    must_not_be:
      - "Ark01 Harvest artifact"
      - "Mission Card"
      - "rolling handoff"

  - path: "s_special/thread-end-gate1-query.md"
    document_identity: "activation_query"
    canonical_name: "Thread-End Gate 1 Query"
    class: "S"
    status: "living_ssot"
    parent_map: "s_special/thread-end.md"
    rail: "same_thread"
    role:
      - "Gate 1 / File Update Lock Router"
      - "Thread Harvest前のFile Update Lock"
      - "GitHub canonical path / source boundary / handoff key / not-now判断を整える"
    must_not_be:
      - "Thread Harvest"
      - "Gate 2"
      - "Mission Card"
      - "final artifact body"

  - path: "s_special/thread-end-gate2-query.md"
    document_identity: "activation_query"
    canonical_name: "Thread-End Gate 2 Query"
    class: "S"
    status: "living_ssot"
    parent_map: "s_special/thread-end.md"
    gate1_query: "s_special/thread-end-gate1-query.md"
    harvest_vessel: "s_special/thread-harvest.md"
    vision_lens: "ss_super-special/torah-vision-lens.md"
    rail: "next_thread"
    role:
      - "Gate 2 / Thread Harvest Executor"
      - "Handoff Builder"
      - "next_thread first query generator"
    anchor_formula:
      - "Thread Harvest is not summary"
      - "Harvest is material; Handoff is ignition key"
    must_not_be:
      - "Gate 1"
      - "rolling handoff"
      - "ordinary summary"

  - path: "s_special/thread-harvest.md"
    document_identity: "harvest_vessel"
    canonical_name: "Thread Harvest"
    class: "S"
    status: "living_ssot"
    source_bootstrap: "S_thread-harvest_v004.md"
    parent_map: "s_special/thread-end.md"
    gate_role: "Gate 2 / Thread Harvest"
    rail: "next_thread"
    role:
      - "Gate 2 Thread Harvest vessel"
      - "rebootable meaning harvest structure"
      - "Thread Naming + Extreme BrainDump core"
    anchor_formula:
      - "Thread Harvest is not summary"
      - "Thread Harvest leaves meaning / heat / Seed / Next Compass"
    must_not_be:
      - "Ark01 primary harvest artifact itself"
      - "rolling handoff"
      - "Mission Card"

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

## §5. High-Guard Vision Layer

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

## §6. Migration Candidate Protocols

ここでは、ADR上で候補化されているが、現時点ではGitHub canonical pathで未確認のProtocol親Markdownを名簿化する。

これらはArk01成果物ではない。  
これらは `s_special/` へ移す候補である。

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

## §7. Document Identity Rules

Protocol Registryでは、最低限、次の身分を区別する。

```yaml id="document-identity-rules"
document_identity_rules:
  protocol_parent_markdown:
    meaning: "Ark-wide protocol body / specification"
    example:
      - "thread-end.md"
      - "thread-index-ark_v041.md"

  activation_query:
    meaning: "Future AIを起動するQuery / Runtime Adapter"
    example:
      - "thread-end-gate1-query.md"
      - "thread-end-gate2-query.md"
      - "thread-index-ark-query_v041.md"
    guard:
      - "Query is not always SSOT"
      - "Query may pair with protocol parent markdown"

  craft_protocol:
    meaning: "成果物生成のCraft仕様"
    example:
      - "thread-mission-card-craft_v002.md"

  harvest_vessel:
    meaning: "Harvestを実行するためのVessel / structure"
    example:
      - "thread-harvest.md"

  format_ssot:
    meaning: "回答Format / interoperability surface のSSOT"
    example:
      - "ark-open-knowledge-format.md"

  vision_core:
    meaning: "Ark-wide high-guard vision / naming lens"
    example:
      - "torah-vision-lens.md"
```

---

## §8. Placement Rules

### §8.1 s_special/

```yaml id="placement-s-special"
s_special:
  role:
    - "Ark-wide protocol layer"
    - "Activation Query layer"
    - "Craft / Workflow specification layer"
    - "Format SSOT layer"
  examples:
    - "thread-end.md"
    - "thread-end-gate1-query.md"
    - "thread-end-gate2-query.md"
    - "thread-harvest.md"
    - "ark-open-knowledge-format.md"
  must_not_be:
    - "Ark01 Harvest output"
    - "Ark02 Harvest output"
    - "Mission Card folder"
    - "rolling handoff"
```

### §8.2 ss_super-special/

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

### §8.3 _projects/ark/indexes/

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

## §9. Update Policy

```yaml id="update-policy"
update_policy:
  protocol_registry:
    path: "_projects/ark/indexes/ark-protocol-registry.md"
    update_frequency: "low / when protocol layer changes"
    update_style:
      - "add path / identity / role / status"
      - "do not copy full protocol body"
      - "separate confirmed canonical from migration candidate"
    version_memory: "Git history"

  confirmed_github_canonical_entries:
    update_when:
      - "new s_special file becomes GitHub canonical"
      - "role / path / identity changes"
      - "status changes from candidate to living_ssot"

  migration_candidates:
    update_when:
      - "local or uploaded source is nominated for s_special"
      - "candidate path changes"
      - "candidate is migrated to GitHub canonical"
```

Stop condition：

```text id="registry-update-stop"
RegistryがProtocol本文の代替になり始めたら止める。
Registryは住所録へ戻す。
```

---

## §10. Reality Response Checkpoints

Protocol RegistryをGitHub作成した後は、必ず現実応答を見る。

```yaml id="reality-response"
reality_response_checkpoints:
  github_ui:
    - "_projects/ark/indexes/ で見つけやすいか"
    - "ADRと並べた時に役割が分かるか"

  future_ai_reading:
    - "s_special/ がProtocol層だと分かるか"
    - "THREAD_INDEX系がArk01成果物ではないと分かるか"
    - "QueryがSSOT本文ではない場合を誤読しないか"
    - "migration_candidate と github_canonical を区別できるか"

  human_feel:
    - "Protocol層の見通しが良くなったか"
    - "Ark01 migration前の安心感が増したか"
    - "名簿として軽いか"

  ark_governance:
    - "Repository Governance ADRに従っているか"
    - "phase-handoff.mdと役割重複していないか"
    - "Ark01 Migration Manifestへ入れるべき内容を持ち込んでいないか"
```

Reality Responseは任意ではない。  
現場で効いているかを見るGateである。

---

## §11. Stop Conditions

```yaml id="stop-conditions"
stop_conditions:
  - "RegistryがProtocol本文の全文複製になる"
  - "Protocol parent markdownをArk01 Harvestとして分類する"
  - "Activation Queryを無条件にSSOTとして扱う"
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
- confirmed と candidate が分かれている
- すべての将来Protocolをまだ網羅していない
```

---

## §12. Living Review

### §12.1 私の判断

Protocol Registryは必要である。

理由は、Ark01 migration前にProtocol層の住所と身分をLockしないと、Future AIが `THREAD_INDEX` や `mission-card-craft` をArk01の収穫物として誤読する危険があるからである。

Registryは、Protocolたちを束ねる本文ではない。  
Registryは、Protocolたちの住所録である。

```text id="living-judgment-compression"
Protocol本文は s_special/ にある。
Protocol身分は Registry で見る。
```

### §12.2 違和感

最大の危険は、Registryを大きくしすぎること。

本文を複製し始めた瞬間、RegistryはRegistryではなくなる。  
だから、各Entryは短く、しかし文書身分は明確にする。

正しい密度はこれ。

```text id="density-rule"
迷わないだけ十分。
本文を置き換えないだけ軽量。
```

### §12.3 Hidden Pattern

```text id="hidden-pattern"
ADR:
  なぜ文書身分が必要か。

Protocol Registry:
  どのProtocolが何者か。

s_special/:
  実際のProtocol本文。

ss_super-special/:
  Vision Lens。

Ark01 Migration Manifest:
  local_path → github_path の実務表。
```

### §12.4 Misread Warning

```yaml id="misread-warning"
misread_warning:
  - "このRegistryをProtocol本文として扱わない"
  - "このRegistryをArk01 Migration Manifestとして扱わない"
  - "このRegistryをMission Card indexとして扱わない"
  - "このRegistryをrolling handoffとして扱わない"
  - "このRegistryをRoot化しない"
```

### §12.5 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_registry_becomes_full_protocol_body:
    action: "本文複製を削り、path / identity / role / statusへ戻す"

  if_protocol_parent_markdown_is_classified_as_ark01_harvest:
    action: "document_identityをprotocol_parent_markdownへ戻す"

  if_activation_query_is_confused_with_ssot:
    action: "query_is_not_ssot / paired_query relationを明記する"

  if_migration_candidate_is_not_on_github:
    action: "status: migration_candidate / not_github_canonical_yet を維持する"

  if_ark01_migration_details_enter:
    action: "Ark01 Migration Manifestへ送る"

  if_text_becomes_english_first:
    action: "Japanese-first / English-anchorへ戻す"
```

---

## §13. Canonical Status / Next Movement

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
    - "Create _projects/ark/indexes/ark-protocol-registry.md only after explicit user signal"
    - "After creation, run Protocol Registry Reality Response Check"
    - "Continue Repository Governance sequence without Ark01 migration yet"

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
