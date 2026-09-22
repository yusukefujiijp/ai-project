---
title: "ai-project Archives — 退役した資料と判断の由来への入口"
version: "0.1.0"
canonical_path: "__archives/README.md"
role: "Archive storage entry and provenance index"
status: "human-authorized entry"
repository: "yusukefujiijp/ai-project"
primary_reader: "Current AI / other AI / Future AI / YusukeJP"
created: "2026-09-22"
updated: "2026-09-22"
expected_eof: "EOF::AI_PROJECT_ARCHIVES_README::v0.1.0"
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

たとえばARC-001の提案先は `__archives/ARC-001/tools/check_repo_reality.py`。これは候補の説明であり、保存済みパスではない。

## 3. 保存実体の索引

この入口の設置基点（2026-09-22、[commit d8c744d](https://github.com/yusukefujiijp/ai-project/commit/d8c744dd68d5a366855bb33e3167147adfc213cd)）では、__archivesには改行のみのREADME一つがあり、案件配下の保存実体はなかった。

初期の候補は[ARC-001](../control-center/ARCHIVE.md#arc-001)で確認できる。承認・進捗の最新判断は同案件が所有する。実体の移動と確認が完了したら、本節へ案件ID・保存物のリンク・案件記録へのリンクを追加する。

既存のArk21:06 sandboxは、その場所に保存された実験の由来である。__archivesへ移設済みと数えず、必要な案件から参照する。全ての歴史資料をこの入口整備と同時に移す意味ではない。

## 4. 利用と復元

過去の知恵を調べる場合は、保存物と案件の理由を合わせて読む。再利用・再設計・復元を行う場合は、現在の目的・依存・Human判断に照らして検討する。復元した事実と理由も同じ案件へ追記し、当初の退役判断を無言で消さない。

本入口、案件ID、保存形式は改善できる。他AI・Future AIが、どの実体をどの判断で保存したかへ到達できることを保持する。

EOF::AI_PROJECT_ARCHIVES_README::v0.1.0
