---
title: "ai-project Archives — 退役した資料と判断の由来への入口"
version: "0.4.0"
canonical_path: "__archives/README.md"
role: "Archive storage entry and provenance index"
status: "human-authorized entry"
repository: "yusukefujiijp/ai-project"
primary_reader: "Current AI / other AI / Future AI / YusukeJP"
created: "2026-09-22"
updated: "2026-09-24"
expected_eof: "EOF::AI_PROJECT_ARCHIVES_README::v0.4.0"
---

# ai-project Archives

**現在の運用から退役させた資料を、判断理由と再検討の経路を保って保存する場所。**

ai-project全体の構造整理は[control-center](../control-center/README.md)、優先順位は[PLAN](../control-center/PLAN.md)、個別候補の提案・Human判断・実施記録は[ARCHIVE](../control-center/ARCHIVE.md)から辿る。ここは承認理由の第二原本を作る場所ではなく、保存実体からその案件と由来へ戻る入口である。

## 1. 保管の意味

「不要」は、現在の運用に残す必要がないという判断であり、資料の知恵や歴史が無価値という意味ではない。AIが具体案を提示し、YusukeJPが対象と変更内容を承認した後、案件に従って実体をここへ移す。

保存原本内の `current`、`active`、過去の承認、起動指示、元の `canonical_path` は当時の記述として読む。現在の作業へ適用する権限や、通常運用への再採用を意味しない。元の意味を確認するには対応する案件と原資料の文脈へ戻る。

このフォルダ名は技術的な読取専用化・実行停止機能ではない。現役の入口や実際の呼出し元がある場合は、承認された移動の作業範囲で案内・参照も整える。

## 2. 保存先の対応

基本案は `__archives/<案件ID>/<元の相対パス>`。案件IDからARCHIVEの同じ記録へ戻り、元の役割・移動理由・承認範囲・復元方法を確認できるようにする。案件の性質に合わない場合は、対応と理由を残して別の構成を選べる。

ARC-001では、元の `tools/check_repo_reality.py` を [ARC-001/tools/check_repo_reality.py](ARC-001/tools/check_repo_reality.py) に保存する。現在の実施・確認状態は[同じ案件](../control-center/ARCHIVE.md#arc-001)が所有する。

ARC-002では、旧Bootの固定参照を保つため元パスの同一原本も互換用に保持する。アーカイブへの保存と、元パスからの完全な移動を区別する。詳細と残点は[ARC-002](../control-center/ARCHIVE.md#arc-002)を参照する。

## 3. 保存実体の索引

この入口の設置基点（2026-09-22、[commit d8c744d](https://github.com/yusukefujiijp/ai-project/commit/d8c744dd68d5a366855bb33e3167147adfc213cd)）では、__archivesには改行のみのREADME一つがあり、案件配下の保存実体はなかった。

上の設置基点から、次の保存実体を追加した。承認・実施・Remote確認の詳細は案件記録で確認する。

| Node | Edge | 元の配置と保存する内容 |
|---|---|---|
| [ARC-001のchecker](ARC-001/tools/check_repo_reality.py) | [案件の理由・承認・実施・復元](../control-center/ARCHIVE.md#arc-001) → [実験の由来](../ark-project/ark21/Ark21-06/sandbox/README.md) | `tools/check_repo_reality.py`。撤回済み実験のコードを内容変更なしで保存。現在のRepository正常条件を定めるツールではない |
| [ARC-002のBridge原本](ARC-002/ai-ark-seed/ai-ark-seed-cards/next-cycle-workout-bridge.md) | [廃止理由・固定参照・残点](../control-center/ARCHIVE.md#arc-002) → [現在の棚の案内](../ai-ark-seed/ai-ark-seed-cards/README.md) | 一原本を保存。元パスは同一blobの互換原本として保持し、物理移動完了とは数えない |
| [ARC-003の旧Stage 02](ARC-003/prompts/x-deepquote/x-deepquote_02-quote-completion-gate_v001-8.md)・[監査Packet](ARC-003/prompts/fable5/fable5-x-deepquote-markdown-handoff-ai-output-polish-audit_packet_v001.md) | [旧方式の退役と保存価値](../control-center/ARCHIVE.md#arc-003) → [現在のPrompt入口](../prompts/README.md) | 二原本を移動。Stage 01・後続Stage 02・02Rは保持 |
| [ARC-004の旧Compile](ARC-004/prompts/ai-compile-ark-seed.md)・[Compile Query](ARC-004/prompts/ai-compile-ark-seed_query.md)・[旧Pickup](ARC-004/prompts/ai-pickup-ark-seed.md)・[Pickup Query](ARC-004/prompts/ai-pickup-ark-seed_query.md) | [役割差と退役理由](../control-center/ARCHIVE.md#arc-004) → [文脈を保持する現在の案内](../ai-ark-seed/README.md#10-context-preservation) | 四原本を移動。軽量Seedとの完全同等やRuntimeの再設計を意味しない |
| [ARC-005の旧chocoZAP案内](ARC-005/chocozap/README.md)・[日別記録](ARC-005/chocozap/records/2026/2026-09-24.md)・[旧移動案内](ARC-005/chocozap/records/undated/cz-visit-0001.md) | [退役理由・予期せぬ成功の評価・復帰条件](../control-center/ARCHIVE.md#arc-005) → [現行の記録入口](../chocozap/README.md) | 三資料を保管注記付きで保存。原文は注記を除いて保持。現役の正本はJSONへ移行し、旧日別方式は追記・集計対象外 |

既存のArk21:06 sandboxは、その場所に保存された実験の由来である。__archivesへ移設済みと数えず、必要な案件から参照する。全ての歴史資料をこの入口整備と同時に移す意味ではない。

## 4. 利用と復元

過去の知恵を調べる場合は、保存物と案件の理由を合わせて読む。再利用・再設計・復元を行う場合は、現在の目的・依存・Human判断に照らして検討する。復元した事実と理由も同じ案件へ追記し、当初の退役判断を無言で消さない。

本入口、案件ID、保存形式は改善できる。他AI・Future AIが、どの実体をどの判断で保存したかへ到達できることを保持する。

EOF::AI_PROJECT_ARCHIVES_README::v0.4.0
