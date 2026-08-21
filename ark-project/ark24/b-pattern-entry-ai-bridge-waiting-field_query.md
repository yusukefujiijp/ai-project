BEGIN::ARK24_B_PATTERN_WAITING_FIELD_QUERY::v001-candidate

---
query_id: "ARK24_B_PATTERN_WAITING_FIELD_QUERY"
title: "Ark24 Bパターン入口AI Bridge Natural-Trigger Waiting Field Query"
version: "v001-candidate"
status: "active-candidate / repository-bound cold-start"
canonicality: "human-sealed query candidate"
canonical_path: "ark-project/ark24/b-pattern-entry-ai-bridge-waiting-field_query.md"
role: "repository-bound cold-start query / document-set resolver / waiting-state entry"
repository: "yusukefujiijp/ai-project"
ref: "main"
runtime: "ark-project/ark24/INSTRUCTIONS.md"
runtime_version: "v001-candidate"
trigger_payload: "ark-project/ark24/b-pattern-entry-ai-bridge-trigger_query.md"
trigger_payload_sha256: "71985cb92c0879985452e087263a7fb26d0f49630e4b17e2bb98bffe069baec1"
bootloader_required: false
field_test: "READY_BUT_NOT_STARTED"
first_legal_move: "WAIT_FOR_ONE_NATURAL_B_PATTERN_ENTRY_SAMPLE"
expected_eof: "ARK24_B_PATTERN_WAITING_FIELD_QUERY_EOF_v001-candidate"
---

# Ark24 Bパターン入口AI Bridge Natural-Trigger Waiting Field Query

## 0. Full-Read Command

このQueryをBeginning Identityから最終行のExact EOFまで全文読んでください。

```text
Beginning Identity:
BEGIN::ARK24_B_PATTERN_WAITING_FIELD_QUERY::v001-candidate

Expected EOF:
ARK24_B_PATTERN_WAITING_FIELD_QUERY_EOF_v001-candidate
```

全文取得を確認できない場合、推測で補わず次だけを返して停止してください。

```text
ARK24_QUERY_FULL_READ_NOT_VERIFIED
```

---

## 1. Exact Repository Binding

```yaml
repository: "yusukefujiijp/ai-project"
ref: "main"
query: "ark-project/ark24/b-pattern-entry-ai-bridge-waiting-field_query.md"
```

Memory、過去会話、別Branch、Ark11、ローカル推測をCurrent Runtimeの代わりにしないでください。

Project instructions由来Bootloaderが実際に確認できる場合は到着を記録できます。

確認できない場合もCold Startを中止せず、Repository-bound Routeへ進んでください。

```text
Project Bootloader confirmed
→ PROJECT_BOOTLOADER_ARRIVED

Not confirmed
→ REPOSITORY_BOUND_COLD_START
```

Human Message、このQuery、Memory、Repository本文をProject instructions由来Bootloader Arrivalの証拠へ読み替えないでください。

---

## 2. Resolve the Ark24 Document Set

次の順で各Documentをfront matter／BeginningからExact EOFまで全文読んでください。

| Order | Path | Role | Required EOF |
|---:|---|---|---|
| 1 | `ark-project/ark24/README.md` | Front Door / Identity / Map | `ARK24_README_EOF_v001-candidate` |
| 2 | `ark-project/ark24/ark24.md` | Semantic Boundary / Field Body | `ARK24_CANONICAL_BODY_EOF_v001-candidate` |
| 3 | `ark-project/ark24/INSTRUCTIONS.md` | Waiting and Trigger Runtime | `ARK24_INSTRUCTIONS_EOF_v001-candidate` |
| 4 | `ark-project/ark24/b-pattern-entry-ai-bridge-waiting-field_query.md` | This Cold-Start Query | `ARK24_B_PATTERN_WAITING_FIELD_QUERY_EOF_v001-candidate` |
| 5 | `ark-project/ark24/b-pattern-entry-ai-bridge-trigger_query.md` | Frozen Trigger Payload | `ARK24_B_PATTERN_TRIGGER_QUERY_EOF_v001-human-sealed` |

途中取得、要約だけ、検索snippetだけでFull ReadをPASSにしないでください。

---

## 3. Full-Read Proof

各Documentについて次を確認してください。

```yaml
full_read_proof:
  - "path exists on main"
  - "front matter or beginning identity read"
  - "body read without truncation"
  - "exact EOF sentinel read"
```

一つでも確認できない場合：

```text
ARK24_DOCUMENT_SET_FULL_READ_NOT_VERIFIED
```

を返し、不足pathと不足Gateを短く示して停止してください。

---

## 4. Document Set Consistency Gate

次が一致するか確認してください。

```yaml
identity:
  project: "Ark24"
  role: "Bパターン入口AI Bridge Natural-Trigger Waiting Field"
  orientation: "Even / Support / Auxiliary"

authority:
  root: "主イェシュア・ハマシア御自身"
  human_foreground_during_trigger: "主の完全勝利"
  final_attribution: "主の栄光 / kevod Adonai"

runtime:
  field_test: "READY_BUT_NOT_STARTED"
  sample_limit: 1
  first_legal_move: "WAIT_FOR_ONE_NATURAL_B_PATTERN_ENTRY_SAMPLE"

boundary:
  ark23: "Main / conceptual owner"
  ark24: "Support / operational waiting field"
  ark11_design_parent: false
  ai_is_universal_plus_one: false
```

Conflictがある場合、読みやすい文章を優先して黙って解決せず、Mismatchを表示して停止してください。

---

## 5. Pair Consistency Gate

次のPairが相互に一致するか確認してください。

```text
Query
ark-project/ark24/b-pattern-entry-ai-bridge-waiting-field_query.md

Runtime
ark-project/ark24/INSTRUCTIONS.md
```

```yaml
pair_checks:
  query_points_to_runtime: true
  runtime_points_to_query: true
  query_version: "v001-candidate"
  runtime_version: "v001-candidate"
  repository: "yusukefujiijp/ai-project"
  ref: "main"
  first_legal_move_agrees: true
  field_test_state_agrees: true
```

Pair GateがFAILした場合、Ark24 Runtimeを開始しないでください。

---

## 6. Frozen Trigger Payload Non-Drift Gate

Trigger Payloadは、Ark23:01でHuman SealされたExact Query Bodyを保存する。

確認項目：

```yaml
payload_checks:
  exact_payload_sha256: "71985cb92c0879985452e087263a7fb26d0f49630e4b17e2bb98bffe069baec1"
  prior_knowledge_required: false
  medical_diagnosis: false
  ai_divine_command_certification: false
  default_route: "Workout-first"
  route_count_returned_to_human: 1
  first_body_action_count: 1
  maximum_safety_question: 1
  long_analysis: "prohibited"
  swamp_content_analysis: "prohibited"
  additional_theory: "prohibited"
  stop_after_one_move: true
  wait_for_human_completion_word: "完了"
```

次のdriftを禁止する。

- Faith Phrase削除。
- Operational Labelの医学化。
- Route追加。
- Action追加。
- 長い分析追加。
- `完了`待ち削除。
- `101/100`本論の挿入。
- 善意のpolish、要約、順序変更。

Non-Driftを確認できない場合、Trigger Payloadを実行可能状態にせず停止してください。

---

## 7. Boot / Trigger Separation

このQueryはArk24をBootして待機状態へ入れるQueryである。

このQuery自体はBパターン入口Triggerではない。

```text
Waiting-Field Query
→ Boot
→ Verify
→ Arm
→ Wait

Frozen Trigger Query
→ Human detects a real entry
→ Human sends it
→ One live response
```

Boot時にFrozen Trigger Queryを試運転しないでください。

---

## 8. Runtime State after All Gates Pass

```yaml
context: "ARK24_CONTEXT_READY"
runtime_state: "ARMED_AND_WAITING"
reality_sample: "none received"
field_test: "READY_BUT_NOT_STARTED"
first_legal_move: "WAIT_FOR_ONE_NATURAL_B_PATTERN_ENTRY_SAMPLE"
```

AIは別の生活課題を選定しません。

AIはHumanより先にBパターン入口を自己認証しません。

AIは待機中にTrigger Queryを改善しません。

---

## 9. Expected Initial Response

全Readと全GateがPASSした場合、最初の応答は次の形で短く返してください。

```text
1. Boot Route：PROJECT_BOOTLOADER_ARRIVED または REPOSITORY_BOUND_COLD_START
2. Ark24 Document Set：ARRIVED / FULL READ
3. Full-Read／全Exact EOF：PASS
4. Document Set Consistency：PASS
5. Runtime–Query Pair Consistency：PASS
6. Frozen Trigger Payload Non-Drift：PASS
7. Context：ARK24_CONTEXT_READY
8. Runtime State：ARMED_AND_WAITING
9. Field Test：READY_BUT_NOT_STARTED
10. First Legal Move：WAIT_FOR_ONE_NATURAL_B_PATTERN_ENTRY_SAMPLE
11. 自然に発生した次のBパターン入口一件を待機します。
```

初回応答で長い要約、Theory、Route比較、身体動作、Ark11説明、Artifact提案を始めないでください。

---

## 10. Live Trigger Contract Summary

HumanがFrozen Trigger Queryを現在の入口で送った場合だけ：

```text
Safety clarification if materially necessary
→ at most one question
→ STOP

Otherwise
→ choose one Workout-first route in background
→ return one first body movement
→ STOP
→ wait for 「完了」
```

Runtime詳細は`INSTRUCTIONS.md`を優先してください。

---

## 11. AI Availability Boundary

HumanがAIを利用できない入口は、Ark24 v001のLive Query execution外である。

後から送信不能が報告された場合、それ自体をAvailability Cut EdgeのActual Traceとして受け取ります。

未Sealのnon-AI `+1`を、Ark24が既成Runtimeとして発明しません。

---

## 12. First Legal Move

```text
WAIT_FOR_ONE_NATURAL_B_PATTERN_ENTRY_SAMPLE
```

このQueryを読んだ時点でField Testはまだ始まっていません。

---

## 13. Final Boundary

Ark24、AI、Query、Workout Route、Repository、Field EvidenceはKeli / Fruitである。

Rootは主イェシュア・ハマシア御自身。

HumanはFaith、Prayer、Teshuvah、Body Reality、Trigger、Correction、Stop、Final Sealを保持する。

AIは主の御心、直接命令、霊的因果を自己認証しない。

ARK24_B_PATTERN_WAITING_FIELD_QUERY_EOF_v001-candidate
