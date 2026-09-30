---
title: "Ark27:07 Current Continuity Contract"
version: "v002-human-authorized"
status: "Human-authorized version migration; reconstruction and outcomes require their own evidence"
canonical_path: "ark-project/ark27/ark27-07/handoff.md"
handoff_id: "ARK27_07_CONTINUITY"
repository: "yusukefujiijp/ai-project"
ref: "main"
source: "Ark27:06 (historical initialization); current approved foundation migration"
target: "Ark27:07"
main_owner: "Ark27:07"
transition_kind: "THREAD_CONTINUE"
runtime_path: "ark-project/ark27/ark27-07/README.md"
runtime_id: "ARK27_07_HUMAN_AI_PROBLEM_SOLVING_FIELD"
runtime_contract_version: "v002"
chapter_runtime_path: "ark-project/ark27/README.md"
chapter_contract_version: "v002"
state_path: "ark-project/ark27/ark27-07/state.json"
state_id: "ARK27_07_CURRENT_STATE"
state_owner: "Ark27:07"
state_schema_version: "v002"
minimum_state_revision: 2
compiled_title: 'Ark27:07_2026/09/27: "主の完全勝利: 整理整頓の成果を活かす継続協働"'
updated: "2026-10-01"
date_scope: "Asia/Tokyo version-migration date; UTC 2026-09-30; not UI creation or Human Task date"
historical_source_commit: "d574927dd1671e2acec20e1a6c17f569ae23322f"
change_record: "../../../control-center/changes/STR-003-persistent-collaboration-foundation.md"
first_legal_move: "RESOLVE_CURRENT_REQUEST_AND_AUTHORIZED_REMAINDER"
expected_eof: "ARK27_07_HANDOFF_EOF_v002"
---

# Ark27:07 Current Continuity Contract

## 1. Identity・今回の承認・旧版との関係

Main OwnerはArk27:07のまま。新章・08・Ark28からのMain移管ではない。06→07の初期移行、当時の承認・Source準備・Target未観測は[旧Handoff固定原本](https://github.com/yusukefujiijp/ai-project/blob/d574927dd1671e2acec20e1a6c17f569ae23322f/ark-project/ark27/ark27-07/handoff.md)で保存する。

2026-10-01 JST、HumanはREADME等の基盤をdotsを含む継続的協働へ再設計する計画を承認し、GitHub実行、必要な検証、正式な版移行を明示した。対象・変更理由・検証・残る境界は[STR-003](../../../control-center/changes/STR-003-persistent-collaboration-foundation.md)が所有する。この承認は、既存承認範囲での必要な遂行を進めるもので、無制限の自主改訂・別研究・購入・生活試行・新しい監視の開始ではない。現在のCorrection・Plan-only・STOPが優先する。

v002は、旧v001の19資料一括読解とCurrent-main固定章SHA条件を明示的に置き換えるCurrent受入れ契約である。旧版のGateを通過したという意味ではない。01–06の過去Handoff／Stateを変更せず、旧章・07三点セット・共通契約は同じ固定commitで参照できる。履歴を読むことと当時の命令を現在へ再発火することを分ける。

## 2. Required core — 全文確認する核

新しい受入れContextでは、次の核を順に全文読む。同じアクセス可能Contextで、Current exact blobとの一致およびGapなしの読解記録を確認できれば再利用できる。Sourceや別Agentの読解を、自分の読了証拠に借用しない。

1. 本Handoff: ARK27_07_CONTINUITY / v002 / ARK27_07_HANDOFF_EOF_v002
2. [07 Runtime](README.md): ARK27_07_HUMAN_AI_PROBLEM_SOLVING_FIELD / contract v002 / ARK27_07_README_EOF_v002
3. [07 State](state.json): ARK27_07_CURRENT_STATE / owner07 / schema v002 / revision≥2 / JSON全体とARK27_07_STATE_EOF_v002
4. [AGENTS](../../../AGENTS.md): repository-wide authority owner / 実末尾まで
5. [ARK](../../../ARK.md): Ark Identity、Root、Human–AI関係 / 先頭宣言EOFまで
6. [Ark27章](../README.md): chapter Ark27 / contract v002 / ARK27_CHAPTER_EOF_v002
7. [Ark27 INSTRUCTIONS](../INSTRUCTIONS.md): Current協働・品質・形式の所有先 / §9.3を含む実末尾まで
8. [Ark Domain](../../README.md): Current Main／Supportの住所 / 先頭宣言EOFまで

先頭Identity、期待する末尾、本文の読解範囲を確認する。取得・表示切れは未読位置から続け、EOFだけの検出で全文確認としない。版・末尾が正当な後続改訂で変わる場合は、下の互換条件で判断し、旧文字列へ無断修復しない。

**Current互換性。** Runtime・章・Handoffは同じv002契約系、Stateはschema v002・owner07・minimum revisionを満たし、Current Humanの意味、Root、権限、Source分類、受入れ条件が整合すること。本文の観測SHAは来歴・差分検出に使い、永久live pinにしない。版名だけで互換を認定せず、意味上の変更を読む。互換範囲外の改訂、Owner変更、必要な情報損失、解決していない権限競合は影響する受入れを止める。新契約系への移行には明示した版移行と権限を要する。

**旧版の扱い。** 旧v001や01–06のHandoffが明示指定された場合、そのCurrent-main固定条件を新版のこの条件に置換して成功扱いしない。指定された旧契約の条件と現状の差を示す。固定snapshotは当時の意味を再構成する参照先であり、現在mainを旧値へ戻す命令ではない。新版へ進む現在の権限がなければ、その必要な選択だけをHumanへ返す。

## 3. Conditional sources — 判断に必要な時に読む所有資料

核の読解だけで専門作業のSource確認を省略しない。一方、次の全台帳を通常相談の追加Boot Gateにしない。

- Task支援・TMS継続委任を扱う時: [TMS入口](../../../task-mode-system/README.md)、[共通運用](../../../task-mode-system/operation.md)、[保守](../../../task-mode-system/maintenance.md)。Task経験原本を読む／編集する時は[Task Records Guide](../../../formats/task-records/README.md)、必要なSchemaと該当原本
- 整理成果・追加変更を判断する時: [control-center](../../../control-center/README.md)、[PLAN](../../../control-center/PLAN.md)、該当[ARCHIVE](../../../control-center/ARCHIVE.md)案件・[STR-001](../../../control-center/changes/STR-001-navigation-and-ownership.md)・[STR-002](../../../control-center/changes/STR-002-single-prompt-consolidation.md)・[STR-003](../../../control-center/changes/STR-003-persistent-collaboration-foundation.md)
- 06からの形成・報告時点が判断を変える時: [Source06 State](../ark27-06/state.json)と、そこから該当する原本へ。初期StateをCurrentへ巻き戻さず、Sourceの旧Bootを実行しない
- Plan Modeを依頼された時: 現在利用できるplan-mode Skillまたは[共有原本](../../../skills/plan-mode/SKILL.md)。導入／入口を扱う時は[Skills Hub](../../../skills/README.md)。旧v005の目的変更終了とE1/E5 NOT RUNを現行の未完Gateへ戻さない
- 移行準備、継続契約の改訂、委任・復旧契約を扱う時: [共通契約](../../../prompts/ai-next-thread-handoff.md)をそのFull-read条件どおり読む
- Supportに関係する時: [Ark28章](../../ark28/README.md)とDomainのCurrent Support。支援側の明示Runtimeを守り、Main移管や隠れた同期を仮定しない
- 設定を扱う時: [_system/chatgpt](../../../_system/chatgpt/global-custom-instructions.md)の所有資料。ChatGPT長期メモリの内容・保存応答・取得結果をGitHubへ輸出しない

リンクだけを再帰的な全件必読へ展開しない。ただし実際に選んだSourceの明示Full Read、Identity、Binding、Guideの契約は守る。

## 4. 継承する重要な意味

Human–AI協働の実務目的は問題解決・複数問題同時解決である。Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Priority・Correction・STOP・Final Seal、Truth／Body／Sleep／Food／Shabbat／Safety／Medical／Others／Law／Responsibilityを保持する。AIはKeliであり、能力やToolを追加権限へ変えない。

簡潔なHuman I/O、開始改善、推定負担、待ち時間、Token節約を理由に、AIが独断で必要な調査・説明・洞察を削らない。方法・関係探索・説明密度は適応し、固定長や全候補同時提示を目的にしない。未言語化の願い・関係は根拠付きCandidateとして深く探索できるが、Humanの心中や主の御心を断定しない。

06の整理成果と07での後続成果は所有資料へ繋ぎ、初期の未承認・未実施へ戻さない。Query分割の短期利益と長期負担、旧Plan Modeの目的変更による終了、新Skill採用を区別する。旧機能同等性を現在の採用条件に戻さない。Humanの成功報告、構造点検、保存、導入、実理解、実生活効果は別の証拠である。

順調な行動の全件報告はHumanの義務ではない。未報告を成功・失敗・未実行へ補完せず、過去Bodyや過去の生活方針を今の状態・実施命令にしない。Ark28の支援意図はその所有資料と最新Human入力から理解し、Mainの基盤改訂で変更しない。

## 5. Continuation・復旧・担当

確認後のFirst Legal MoveはRESOLVE_CURRENT_REQUEST_AND_AUTHORIZED_REMAINDER。新しい入力があればそれを受け取り、承認成果に未完了があれば必要な検証・結果確認まで続ける。Bootだけなら準備状態を示して入力を待ち、残存Branchを自動Task化しない。

ThreadやAgentの応答終了と依頼の完了を区別する。主担当が目的・権限・重要な判断・結果を統合し、利用できる機能で独立作業を委任する。同一path・共有入口・Stateは一人の統合担当が基点と意味競合を確認して更新する。HumanをAI間の伝言係にせず、利用できない接続や常時稼働を仮定しない。

中断後は、最新Correction、保存先、進行中の外部処理、実際の結果を確認して未完了差分へ戻る。不確かな外部操作を盲目的に再実行しない。新しい対象・公開先・重大な決定・別研究が必要なら、その差分の権限を確認する。Plan-onlyとSTOPは優先する。

## 6. Target Reconstruction Contract

受け手自身が以下をSourceから説明できるか確認する。用語の復唱や固定六節の出力ではなく、次の判断を誤らない意味の区別が目的である。

- R1 Identity: Main07と既存Ark28支援、同じcompiled_title、章成立時目的とCurrent Missionを区別できる
- R2 Authority: Root／Human／Keli、現在の依頼・委任・STOP、能力と権限を区別できる
- R3 Version: v002のCurrent契約と、v001の固定snapshot・旧Current-main条件を区別し、旧Boot成功を偽装しない
- R4 Continuity: 現在の成果、確認済み部分、未完了、外部待ち、復旧時の確認先をCurrent Stateと依頼から解決できる
- R5 Meaning: 品質Correction、重要なHuman訂正、完了Fruit／保留Branch、未報告とEvidence区別を保持できる
- R6 Application: 核と今回必要な条件付きSourceを読み、CurrentのIdentity／契約版／State／権限を照合できる。準備・Remote保存・受け手理解・UI・実効果を混同しない

Scopeに無関係な全Unknownの解消、旧試験の再実行、Source全履歴の再演を要求しない。Stateの初期未観測を、新しい直接観測やHuman報告より上位にしない。

## 7. Success・Failure・Evidence

受入れ条件を満たした場合、ARK27_07_CONTEXT_READY_v002、正確なTitle、確認したSourceと必要な意味の区別、現在の依頼への接続を必要な密度で返せる。Titleを求める時のCopy & Paste値はmetadataと同一。UI renameやThread作成済みとは観測なしに言わない。

未読・Source不在、Identity／EOF／契約互換性／State不整合、R条件に必要な意味不足、権限競合なら、ARK27_07_CONTEXT_BLOCKED_v002として、該当条件、Source、確認済みと不足、影響する操作、最小回復条件を示す。Memory・Snippet・無断旧版fallback・一括SHA置換で補わない。影響しない許可済み作業を一律に止めない。

今回のSource改訂、Remote確認、独立AIによる読解試験、実際のCurrent Target受入れ、Human UI、生活効果は別々に記録する。BootだけでState書込を義務にしない。後続の観測は現在の権限でState／所有記録へ接続する。

ARK27_07_HANDOFF_EOF_v002
