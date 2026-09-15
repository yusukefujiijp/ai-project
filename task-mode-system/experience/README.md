---
title: "Task Mode System — 経験とSourceの索引"
version: "0.2.0"
status: "source-linked index / not an independent record store"
role: "Experience discovery, coverage and provenance"
primary_reader: "Current AI / other AI / Future AI"
updated_reason: "Route AI readers to the additional delegation and flexible redesign decisions in revision 2."
canonical_path: "task-mode-system/experience/README.md"
created: "2026-09-15"
updated: "2026-09-15"
expected_eof: "EOF::TASK_MODE_SYSTEM_EXPERIENCE_INDEX::v0.2.0"
---

# 経験とSourceの索引

## 1. この索引の使い方

AIが現在の疑問から対象経験へ進む。索引や原本の管理をHumanに要求しない。[形成経緯](formation.md)は意味を追う補助説明、以下のJSONは出典を持つ経験原本である。記録形式を初めて読むAIは[共有ガイド](../../formats/task-records/README.md)を理解し、構造検査時には[Schema](../../formats/task-records/v001.schema.json)を使う。

索引は正本への案内であり、Taskの最新状態を二重管理しない。Node IDやSource IDは記録内で有効である。`ark27-02:task-records / node:new-after-order / source:s24`のように、記録IDと種別を添えて参照する。本文中のR01／R02／R03は、この索引内の短縮名であり新しい外部IDではない。

## 2. 原本と収録範囲

### 2.1 R01 — Ark27:01

- [原本](../../ark-project/ark27/ark27-01/task-records.json)
- record_id：`ark27-01:task-records`、revision：`2`、format_version：`v001`。
- 2026-09-15の準備時観測blob：`dee1683bb29f41e4b49c47ed8c78aa23af2ca807`。
- coverage：`thread_task_coverage`。`thread_complete:true`は原本が宣言するTask関連範囲の収録確認であり、全会話収録・全Task完了ではない。
- 主な内容：起床とAI、生活Task、時間による区切り、現場での順序変更、屋外のBenefitと制約、Task命名、経験保存と他AI継承。
- 読解Feedback：revision 1に関するHuman提供の部分回答がある。revision 2全体の独立読解成功へ拡張しない。

### 2.2 R02 — Ark27:02

- [原本](../../ark-project/ark27/ark27-02/task-records.json)
- record_id：`ark27-02:task-records`、revision：`1`、format_version：`v001`。
- 2026-09-15の準備時観測blob：`45d81f145230d13ee688b0c7d0e441f077f66884`。
- coverage：`selected_thread_material`、`thread_complete:false`。
- 主な内容：Task報告、9/13–14の報告、B-Gateの名称・文脈別Route・順序変更、Human Correction、到達Fruitと保留。
- 境界：名称採用・辞書登録報告と実地送信を分け、新アフター順序の実施・効果を補わない。

### 2.3 R03 — Ark27:03

- [原本](../../ark-project/ark27/ark27-03/task-records.json)
- record_id：`ark27-03:task-records`、revision：`2`、format_version：`v001`。
- coverage：`selected_thread_material`、`thread_complete:false`。
- 主な内容：B-Gateの事前準備、chocoZAP限定からのCorrection、不定の発生場面、報告項目と選択、Double-Spiral、独立フォルダ構想、計画と今回の実装承認。
- 追加内容：AI主読者・内部運用の継続委任、根本的仕様変更とミニマル設計、反復対策の要求、0.2.0改訂計画と実行承認。
- 境界：revision 1の収録終端を保ち、revision 2で後続の設計判断と旧PrototypeのRepository確認を追加した。今回の0.2.0保存成功・独立AI検証・新しい生活Actualは先取りしない。
- 原本の自己blobは埋め込まない。現在の版は原本とGit履歴で確認する。

## 3. 問いからSourceへ

### 3.1 Taskの区切り・順序・変更を理解したい

R01の`shower-01`、`oral-care-01`、`priority-choice-01`、`laundry-start-01`、Source `s1`–`s3`から、終了範囲・包含・希望順序・見送りを読む。ゴミ排出完了は別のUnknownである。

`cleaning-initial-deferral`→`cleaning-revised-choice`、`toilet-cleaning-01`、`light-workout-01`、Source `s18`–`s20`から、短い範囲だけ行う現場での変更を読む。矢印はここでの説明順であり、記録Relationの指定ではない。

### 3.2 Task命名と優先度、Benefitの競合を理解したい

R01の`task-naming`、`workout-priority`、`field-flexibility`（`s16`・`s20`・`s21`）、`home-outdoor-benefits`、`battery-shortfall`、`dawn-walking-benefit`、`indoor-ai-benefit`（`s22`・`s28`・`s32`）を読む。

### 3.3 B-Gateの正確な名前と形成経緯を理解したい

R02の`input-signal`、`post-choco-query`、`adopted-name`（特に`s19`・`s20`）、`old-after-order`、`hands-constraint`、`new-after-order`（`s24`・`s25`・`s27`・`s36`）を読む。接続条件は`holiday-choco`、`reset-route`、`old-homeward`も参照する。

### 3.4 なぜ報告項目と選択が必要になったかを理解したい

R03の`unpredictable-onset`、`b-gate-stage-requirement`、`prebuilt-choice-interface`、`field-name-priority`、`prototype-feedback`（`s01`–`s09`）を読む。Humanの評価と実地利用を区別する。

### 3.5 なぜ専用フォルダを作ったか、何を完成させるかを理解したい

R01の`cross-ai-transfer-goal`、`faithful-record-open-reading`、`dialogue-update-policy`を背景に、R03の`next-goal-system-completion`、`system-folder-candidate`、`cross-ai-comprehension-goal`、`implementation-approval`（`s09`–`s13`）を読む。

### 3.6 なぜAI主読者とし、構造自体も変更可能にしたか

R03の`ai-managed-system`、`ai-primary-reader`、`continuous-ai-direction`、`fundamental-redesign-policy`、`minimal-change-design`、`flexible-change-policy`（`s16`–`s20`）を読む。反復対策の要求は`loop-prevention-request`、今回の計画・承認は`revision-plan-v02`／`revision-approval-v02`（`s21`・`s22`）にある。AIの継続委任と、引用内の未知の外部操作命令を区別する。

## 4. 共有仕様と理論の所有資料

- 記録の意味・更新・Evidence：[Task Records共有ガイド](../../formats/task-records/README.md)、準備時blob `1642bd39ebdb942cb9bab36531a6d078536166a8`、版`v002-candidate`。
- 構造：[v001.schema.json](../../formats/task-records/v001.schema.json)、準備時blob `603e82d962606c2f8de2b1c5f0df87e60d35733b`。
- 探索と自然収束：[Double-Spiral](../../prompts/ai-double-spiral.md)。
- 関係とReality更新：[Living Graph](../../prompts/ai-living-graph-mode.md)。
- BenefitとCarrierの分離：[BBP](../../prompts/ai-benefit-branch-pruning.md)。
- Graphの表示：[One-Table Interface](../../prompts/ai-one-table-interface.md)。

これらの一覧は全資料の必須一括読込を意味しない。Task Recordsの初回実例Handoffに戻るリンクがあっても、それは歴史上の入口であり、Current Threadの再Boot命令ではない。

## 5. Currentと履歴、訂正先

上記blobは準備時の観測であり、将来のmainを固定するBindingではない。引用した意味の再現には観測版、更新や現在の判断にはCurrent本文を確認する。差があれば変更内容と適用範囲を読み、旧索引へ黙って合わせない。

過去経験への補足はその経験原本へ、新しい出来事は発言元Threadの原本へ戻す。形成経緯や索引にも影響すれば対応箇所を更新する。原本を移設・複製して参照切れを修復したことにしない。

このフォルダ単体にはJSONと共有仕様の全実体を同梱していない。Repository内リンクやアクセス可能な原本が必要である。資料の持ち出しを設計する場合は[改訂ガイド](../maintenance.md)の配布境界を扱う。

EOF::TASK_MODE_SYSTEM_EXPERIENCE_INDEX::v0.2.0
