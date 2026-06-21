---
title: "Ark02 Phase Handoff"
status: "active / japanese-first-okf / github_canonical / human_editable / not_final_seal"
document_identity: "phase_handoff"
canonical_path: "_projects/ark/ark02/phase-handoff.md"
project: "Ark: Daily Teshuvah Gate-to-Yeshua"
phase: "Ark02"
source_adr: "_projects/ark/indexes/ark-repository-governance_adr.md"
related_rolling_handoff: "_projects/ark/ark02/handoff.md"
language_policy: "Japanese-first / English-anchor"
format_policy: "Ark-OKF / Rebootable-first"
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

# Ark02 Phase Handoff

## §0. Status / Phase Summary

この文書は、Ark02全体のPhase文脈を安定して保持するための `phase-level map` である。

これは `_projects/ark/ark02/handoff.md` を置き換えない。  
これはArk01 migrationを開始しない。  
これはProtocol Registryを作成しない。  
これはBulk Migrationを許可しない。  
これはGitHub CommitやFinal Sealを自動承認しない。

この文書の役割は、Ark02における次の分離を明確にすることである。

```text id="status-core"
handoff.md:
  rolling current-thread handoff
  最新の next-thread reboot key

phase-handoff.md:
  stable phase-level map
  Ark02全体の文脈地図
```

```yaml id="phase-handoff-status"
phase_handoff_status:
  document_identity: "phase_handoff"
  phase: "Ark02"
  canonical_path: "_projects/ark/ark02/phase-handoff.md"
  language_policy: "Japanese-first / English-anchor"
  format_policy: "Ark-OKF / Rebootable-first"
  user_final_seal_required: true
```

### §0.1 King Sentence

```text id="king-sentence"
handoff.md は「次に何をするか」。
phase-handoff.md は「Ark02とは何の章か」。
```

---

## §1. なぜ phase-handoff.md が必要か

Ark02にはすでに `handoff.md` がある。

その `handoff.md` は、次Threadを再起動するための鍵であり、現在位置、次Thread候補、Priority Read Order、次に実行するTaskをFuture AIへ渡す役割を持つ。

しかし、`handoff.md` にArk02全体の安定Mapまで背負わせると重くなる。

そのため、Ark02では次の二層に分ける。

```yaml id="reason-for-phase-handoff"
reason_for_phase_handoff:
  problem:
    - "handoff.md is already next-thread reboot key"
    - "handoff.md should remain lightweight"
    - "Ark02 still needs stable phase context"
  decision:
    - "handoff.md = rolling handoff"
    - "phase-handoff.md = stable phase map"
```

短く言えば：

```text id="moving-key-stable-map"
動く鍵を軽くするために、
動きにくい地図を横に置く。
```

---

## §2. Root / Fruit Guard

RootはGitHubではない。  
RootはMarkdownではない。  
RootはADRではない。  
Rootは `handoff.md` ではない。  
Rootは `phase-handoff.md` ではない。  
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
  ADR
  handoff.md
  phase-handoff.md
  harvest/
  s_special/
  ss_super-special/
  Ark-OKF
  Full Rail
  Next Gate
  AI
  Commit
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

この文書もFruitであり、Rootではない。

---

## §3. Ark02 Phase Identity

Ark02は、単なる継続Folderではない。

Ark02は、Ark ProjectがGitHub上で正準住所を整え、Future AIへ安全に引き渡すためのRailを作り始めるPhaseである。

Ark01では、Thread HarvestとMission Cardの初期結晶化が進んだ。  
Ark02では、その収穫をGitHub canonical structureへ接続するための文書身分制度、Handoff層、Harvest層、Protocol層の整理が始まる。

```yaml id="ark02-phase-identity"
ark02_phase_identity:
  phase: "Ark02"
  primary_character:
    - "Repository Governance"
    - "Thread-End stack stabilization"
    - "Handoff / Harvest / Protocol separation"
    - "GitHub canonical path discipline"
    - "Future AI continuity design"
    - "Human-AI collaboration tail system"

  not_primary_character:
    - "Bulk Ark01 migration"
    - "Mission Card mass production"
    - "Raw private thread dump"
    - "Unstructured archive"
```

圧縮すると：

```text id="ark01-ark02-compression"
Ark01:
  lived material をHarvestしたPhase。

Ark02:
  canonical rails を立てるPhase。
```

---

## §4. Handoff Layer Separation

Ark02では、Handoffを一枚に押し込めない。

`handoff.md` と `phase-handoff.md` は、似ているが役割が違う。

```yaml id="handoff-layers"
handoff_layers:
  rolling_handoff:
    file: "handoff.md"
    path: "_projects/ark/ark02/handoff.md"
    document_identity: "rolling_handoff"
    role:
      - "latest next-thread reboot key"
      - "current-to-next Thread transfer signal"
      - "Gate / next action starter"
      - "mutable latest-state pointer"
    update_policy:
      - "Thread transitionごとに更新可能"
      - "過去版はGit historyが保持"
    must_not_be:
      - "phase-level stable map"
      - "full phase encyclopedia"
      - "bulk migration manifest"

  phase_handoff:
    file: "phase-handoff.md"
    path: "_projects/ark/ark02/phase-handoff.md"
    document_identity: "phase_handoff"
    role:
      - "stable phase-level map"
      - "Ark02 context and document role map"
      - "low-frequency update phase signpost"
      - "explanation of handoff.md rolling nature"
    update_policy:
      - "Phase構造が変わった時だけ更新"
      - "毎Thread移行では更新しない"
    must_not_be:
      - "latest next-thread pointer"
      - "rolling handoff"
      - "full Harvest artifact"
```

短く言うと：

```text id="handoff-compression"
handoff.md は動く鍵。
phase-handoff.md は動きにくい地図。
Git history は履歴台帳。
```

---

## §5. handoff.md との関係

`handoff.md` は、次Threadを実際に起動するための第一入口である。

`phase-handoff.md` は、その `handoff.md` がなぜ動いてよいのかを説明する安定Mapである。

正しい読み順は以下。

```yaml id="reading-relation"
reading_relation:
  first_for_next_thread:
    path: "_projects/ark/ark02/handoff.md"
    reason:
      - "現在の next-thread reboot signal を持つ"
      - "immediate next task を示す"
      - "Thread frontier に応じて更新される"

  second_for_phase_context:
    path: "_projects/ark/ark02/phase-handoff.md"
    reason:
      - "Ark02 phase identity を説明する"
      - "stable document roles を定義する"
      - "handoff.md の過負荷を防ぐ"

  repository_level_contract:
    path: "_projects/ark/indexes/ark-repository-governance_adr.md"
    reason:
      - "Repository-level document identity contract"
      - "この分離がなぜ必要かを定義する"
```

### §5.1 Misread Guard

```yaml id="misread-guard-handoff"
misread_guard:
  - "handoff.mdをphase-level stable mapとして読まない"
  - "phase-handoff.mdをlatest next-thread pointerとして読まない"
  - "phase-handoff.mdへhandoff.md全文を複製しない"
  - "latest next actionをphase-handoff.mdへ移さない"
```

---

## §6. Ark02 Layer Map

Ark02の文書層は、次のように軽量に読む。

```yaml id="ark02-layer-map"
ark02_layer_map:
  ark02_rolling_handoff:
    path: "_projects/ark/ark02/handoff.md"
    role: "next-thread reboot key / rolling handoff"

  ark02_phase_handoff:
    path: "_projects/ark/ark02/phase-handoff.md"
    role: "stable phase-context map"

  ark02_harvest:
    path: "_projects/ark/ark02/harvest/"
    role: "Thread Harvest / meaning artifact store"
    guard:
      - "harvest/をrolling handoffとして扱わない"
      - "Harvest artifactをcurrent pointerとして上書きしない"

  repository_governance_adr:
    path: "_projects/ark/indexes/ark-repository-governance_adr.md"
    role: "Repository-level document identity contract"

  thread_end_stack:
    paths:
      - "s_special/thread-end.md"
      - "s_special/thread-end-gate1-query.md"
      - "s_special/thread-end-gate2-query.md"
      - "s_special/thread-harvest.md"
    role: "Thread-End / Gate / Harvest protocol layer"

  ark_okf:
    path: "s_special/ark-open-knowledge-format.md"
    role: "Japanese-first OKF / Answer Interoperability Surface"

  vision_lens:
    path: "ss_super-special/torah-vision-lens.md"
    role: "Ark-wide SS Vision Core / Naming Source Lens"
    guard:
      - "high-level vision and naming sourceとして扱う"
      - "Gate2-owned local fileとして扱わない"
```

圧縮すると：

```text id="layer-compression"
ADR = repository contract
phase-handoff = Ark02 map
handoff.md = next-thread key
harvest/ = meaning store
s_special/ = protocol layer
ark-open-knowledge-format = Japanese-first OKF
ss_super-special/ = vision lens
```

---

## §7. Update Policy

`handoff.md` は動く。  
`phase-handoff.md` はあまり動かない。  
`harvest/` は収穫物として追加される。

```yaml id="update-policy"
update_policy:
  handoff_md:
    path: "_projects/ark/ark02/handoff.md"
    update_frequency: "high / each Thread transition if needed"
    version_memory: "Git history"
    content_style:
      - "next-thread reboot key"
      - "current status"
      - "priority read order"
      - "immediate next task"

  phase_handoff_md:
    path: "_projects/ark/ark02/phase-handoff.md"
    update_frequency: "low / only when Ark02 phase structure changes"
    version_memory: "Git history"
    content_style:
      - "phase identity"
      - "document role map"
      - "handoff layer separation"
      - "stable relation to ADR / protocols / harvest"

  harvest_dir:
    path: "_projects/ark/ark02/harvest/"
    update_frequency: "append when Harvest artifacts are explicitly created"
    content_style:
      - "meaning harvest"
      - "thread harvest artifact"
      - "not rolling pointer"
```

Stop condition：

```text id="update-stop"
phase-handoff.md が daily handoff や current-task checklist に見え始めたら止める。
```

---

## §8. Tail Rule v0.8 / human_editable

このPhaseは `Tail Rule v0.8` に従う。  
詳細はRepository Governance ADRを正とし、この文書では要点だけを保持する。

```yaml id="tail-rule-summary"
tail_rule_v0_8_summary:
  fullrail_same_thread:
    role: "AI-readable execution rail"

  next_gate_human_editable:
    role: "human-facing Copy & Paste continuation gate"

  human_editable:
    is_wait_for_human_review: false
    meaning:
      - "人間が必要時に介入できる"
      - "AI-side Living Review may continue"
      - "GitHub Commit approvalではない"

  hard_guard:
    - "Commit requires explicit Human Final Seal"
    - "Bulk Migration requires explicit Human Final Seal"
```

短く言うと：

```text id="review-seal"
ReviewはAIが進める。
Sealは人間が握る。
```

---

## §9. Reality Response Checkpoints

`phase-handoff.md` をGitHub作成した後は、必ず現実応答を見る。

```yaml id="reality-response"
reality_response_checkpoints:
  github_ui:
    - "_projects/ark/ark02/ で見つけやすいか"
    - "handoff.mdとの違いが一目で分かるか"

  future_ai_reading:
    - "どちらがrolling pointerか分かるか"
    - "どちらがstable phase mapか分かるか"
    - "phase-handoff.mdをlatest actionとして誤読しないか"

  human_feel:
    - "Folder全体が整理された感覚になるか"
    - "handoff.mdが軽く感じるか"
    - "Ark02 phase contextが安定して見えるか"

  ark_governance:
    - "Repository Governance ADRに従っているか"
    - "Ark01 migration detailsを入れていないか"
    - "Protocol Registry detailsを入れすぎていないか"
```

Reality Responseは任意ではない。  
現場で効いているかを見るGateである。

---

## §10. Stop Conditions

```yaml id="stop-conditions"
stop_conditions:
  - "phase-handoff.mdがrolling next-thread pointerになる"
  - "handoff.mdがphase-level stable mapとして扱われる"
  - "phase-handoff.mdがhandoff.md全文を複製する"
  - "phase-handoff.mdがArk02百科事典になる"
  - "Ark01 migration detailsが入り込む"
  - "Protocol Registry detailsが膨らむ"
  - "GitHub Commitが明示Human Final Sealなしに行われる"
  - "human_editableがmandatory wait stateとして扱われる"
```

止めなくてよいもの：

```text id="do-not-stop"
- 文書が短い
- Ark02全Threadを列挙していない
- ADRを参照していて、ADRを複製していない
- handoff.mdを参照していて、handoff.mdを複製していない
```

---

## §11. Living Review

### §11.1 私の判断

この文書は必要である。

理由は単純で、`handoff.md` はすでに動く鍵として働いているからである。  
その鍵に、Ark02全体の地図まで持たせると重くなる。

だから `phase-handoff.md` を横に置く。  
これは `handoff.md` を弱めるのではなく、むしろ守る設計である。

```text id="living-judgment-compression"
phase-handoff.md protects handoff.md.
```

### §11.2 違和感

最大の危険は、`phase-handoff.md` を大きくしすぎること。

これはArk02百科事典ではない。  
Ark02の全Thread履歴でもない。  
Ark01 migration planでもない。  
Protocol Registryでもない。

正しい密度はこれ。

```text id="density-rule"
迷わないだけ十分。
置き換えないだけ軽量。
```

### §11.3 Hidden Pattern

```text id="hidden-pattern"
ADR:
  なぜ分けるか。

phase-handoff.md:
  どの層が何者か。

handoff.md:
  次に何をするか。

harvest/:
  何が収穫されたか。

s_special/:
  どう実行するか。

ss_super-special/:
  どのLensで見るか。
```

### §11.4 Misread Warning

```yaml id="misread-warning"
misread_warning:
  - "この文書をlatest next-thread pointerとして扱わない"
  - "この文書をmigration manifestとして扱わない"
  - "この文書をProtocol Registryとして扱わない"
  - "この文書をArk01 migration planとして扱わない"
  - "この文書をRoot化しない"
```

### §11.5 修正条件

```yaml id="revision-conditions"
revision_conditions:
  if_phase_handoff_too_large:
    action: "phase identity and document role mapへ圧縮する"

  if_handoff_md_role_unclear:
    action: "handoff.md = rolling current-thread handoff を強化する"

  if_phase_handoff_becomes_latest_pointer:
    action: "latest next actionをhandoff.mdへ戻す"

  if_ark01_migration_details_enter:
    action: "Ark01 Migration Manifestへ移す"

  if_protocol_details_expand:
    action: "Protocol Registryへ移す"

  if_text_becomes_english_first:
    action: "Japanese-first / English-anchorへ戻す"
```

---

## §12. Canonical Status / Next Movement

```yaml id="canonical-status"
canonical_status:
  file: "phase-handoff.md"
  canonical_path: "_projects/ark/ark02/phase-handoff.md"
  document_identity: "phase_handoff"
  language_policy: "Japanese-first / English-anchor"
  format_policy: "Ark-OKF / Rebootable-first"
  status:
    - "active"
    - "github_canonical"
    - "human_editable"
    - "not_final_seal"

next_movement:
  immediate_next:
    - "Use this file as Ark02 stable phase map"
    - "Keep _projects/ark/ark02/handoff.md as rolling current-thread handoff"
    - "Continue Repository Governance sequence without Ark01 migration yet"

  not_yet:
    - "Ark01 migration"
    - "Protocol Registry creation"
    - "Bulk Migration"
    - "Final Seal"

guard:
  - "Future GitHub commits require explicit Human Final Seal"
  - "human_editable is not human review wait"
  - "AI-side Living Review may continue"
```
