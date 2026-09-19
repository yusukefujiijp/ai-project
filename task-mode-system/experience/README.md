---
title: "Task Mode System — 経験とSourceの索引"
version: "0.3.3"
status: "source-linked index / not an independent record store"
role: "Experience discovery, coverage and provenance"
primary_reader: "Current AI / other AI / Future AI"
updated_reason: "Index Ark27:04 revision 3: collaborative problem solving, holiday Action Mode feedback and Future AI skill discretion."
canonical_path: "task-mode-system/experience/README.md"
created: "2026-09-15"
updated: "2026-09-19"
expected_eof: "EOF::TASK_MODE_SYSTEM_EXPERIENCE_INDEX::v0.3.3"
---

# 経験とSourceの索引

## 1. この索引の使い方

AIが現在の疑問から対象経験へ進む。索引や原本の管理をHumanに要求しない。[形成経緯](formation.md)は意味を追う補助説明、以下のJSONは出典を持つ経験原本である。記録形式を初めて読むAIは[共有ガイド](../../formats/task-records/README.md)を理解し、構造検査時には[Schema](../../formats/task-records/v001.schema.json)を使う。

本書では収録済み経験の範囲と判断の入口を把握し、現在の問いに関係する原本へ進む。継続AIは確認済みの経緯を再利用できる。短い案内で適用条件やEvidenceを解決できなければ、対象NodeのSource・関係するEdge・Correction・Unknownへ戻る。明示された全文読解条件は省略しない。

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
- record_id：`ark27-03:task-records`、revision：`3`、format_version：`v001`。
- coverage：`selected_thread_material`、`thread_complete:false`。
- 主な内容：B-Gateの事前準備、chocoZAP限定からのCorrection、不定の発生場面、報告項目と選択、Double-Spiral、独立フォルダ構想、計画と今回の実装承認。
- 追加内容：AI主読者・内部運用の継続委任、根本改訂、反復対策。さらに、既存保存先とリンク、一つの入口と継続利用、選択読解と漏れ防止、Node & Edge、必要な内部複雑さ、Black box化と可読性の両立、0.3.0の計画・承認。
- 境界：revision 1・2の時点と既存IDを保持し、revision 3で後続の対話と確認済み0.2.0のRepository状態を追加した。今回の0.3.0保存結果・独立AI検証・新しい生活Actualは先取りしない。旧q03は初期九文書時点の問いとして保持する。
- 原本の自己blobは埋め込まない。現在の版は原本とGit履歴で確認する。

### 2.4 R04 — Ark27:04：就寝前想起・開始時・選択報告・Token Reset・協働方針

- [原本](../../ark-project/ark27/ark27-04/task-records.json)
- record_id：`ark27-04:task-records`、revision：`3`、format_version：`v001`。
- coverage：`selected_thread_material`、`thread_complete:false`。
- revision 1の内容：就寝前に合図から思い出したい希望、耳揉み・肌スキンケア兼マッサージ・就寝前用サプリ、失念と終了の難しさ、継続BrainDump集約へのHuman Material Correction、就寝前リコール計画の実行承認。
- revision 2の追加：開始時の締切を時刻設定中心からキリ待ち解除へ訂正した意味、当時の重点テーマ、成功報告の意図的省略と資源配分、Token Reset跨ぎの経験と未確認、三つのSeedの編集定義、長期記憶へ保持したい意向。
- revision 3の追加：人間–AI協働による積極的な問題解決、複数問題同時解決の探索、休日のAction ModeがAI対話時間を減らしたという報告、Future AIの深化・進化を妨げないSkill設計方針と今回の実行承認。
- 時点：現場報告日2026/09/19、初版保存環境のUTC日付2026-09-18、revision 2・3更新日2026-09-19を区別する。追加発言の正確な時刻・timezoneは補完しない。
- 境界：希望と採用、実行、効果、Repository保存、ChatGPT長期記憶への保存を区別する。個別の未報告実績やサービス内部計上仕様を補完しない。就寝前の既存Source・Node・Unknownは保持し、ThreadのREADME／handoff／stateは変更しない。

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

### 3.7 一つの入口と、毎回全てを読まない運用を両立したい

R03の`reading-weight-tradeoff`、`keep-ark-storage`、`single-entry-goal`、`continuing-ai-use`、`selective-reading-request`、`coverage-preservation`（`s24`–`s29`）を読む。01・02分はR01・R02の原本にあり、本フォルダへの全文移設を意味しない。今回の具体的読取経路は[System入口](../README.md)が所有する。

### 3.8 内部の複雑さ、Black box化、別AIの運用可能性を判断したい

R03の`ai-experiment-field`、`node-edge-practice`、`portable-complexity`、`black-box-thought-experiment`、`black-box-balance-proposal`（`s30`・`s31`・`s33`–`s35`）を読む。Humanの目標、AIの設計候補、採用への承認、実地効果を分ける。0.3.0の計画・承認は`revision-plan-v03`／`revision-approval-v03`（`s32`・`s35`・`s36`）、改訂前の0.2.0確認は`prior-v02-remote`（`s37`）にある。

### 3.9 就寝前に思い出したいことを復元する

R04の`bedtime-trigger-request`・`bedtime-braindump-correction`から、Humanが思いついた時に短く預け、AIが整理・更新し、就寝前の自然な合図で使える形へ戻す意図を読む。個別希望は`bedtime-ear-care`・`bedtime-skin-care`・`bedtime-supplement`、理由は`bedtime-ear-recall-gap`・`bedtime-stop-boundary-experience`。Source `bedtime-s01`–`bedtime-s07`と関係するUnknownを合わせて確認する。

`bedtime-ear-only-reception`から`bedtime-braindump-correction`への関係は、耳揉み一項目への応答だけで閉じず、継続的な集約を支えるための重要なCorrectionである。耳揉みの希望を撤回したわけではない。登録の希望と、今回実施済み・今回だけ見送り・恒久的取消しは別の意味として扱う。

対応の方法は[Bedtime Recall](../../skills/recall-bedtime-care/SKILL.md)が所有する。本索引は個別項目の第二の台帳ではなく、原本と変更先の案内である。以後、新しい就寝前想起の希望・適用方針・取消し・Correctionが別Threadへ記録されたら、この項からその原本・対象Nodeと読取条件も辿れるようにする。初期のR04だけを永続的な最新リストとみなさず、Current Humanの入力と後続訂正を照合する。一夜の実施済みは次の就寝機会へ自動転用しない。


### 3.10 開始時の締切・選択報告・利用枠の関係を理解する

R04の `start-without-closure`・`finish-deadline-working`・`start-focus-current` と `connect-s01`–`connect-s02` から、終了側のある程度の成立を背景に開始側へ重点を移し、開始時刻の設定だけでなくキリのよい完了待ちを外すCorrectionを読む。

`selective-success-reporting`・`reporting-memory-importance`・`reporting-unexpected-success` と `connect-s03`–`connect-s05` から、報告の問題密度が生活全体の失敗率ではないこと、順調な実績を省略して時間・注意・利用枠を問題解決に使う理由を復元する。全件成功報告を再要求せず、未報告個別状態はUnknownのままにする。長期記憶へ保持したいという意向は、書込み成功の確認ではない。

`token-reset-boundary-report`・`token-budget-ongoing` と `token-s01`–`token-s03` は、Reset跨ぎ後の新期間残量減少のHuman報告と、週内配分・失効前余剰活用の改善課題を所有する。全処理の終了時刻一括計上などの内部仕様はUnknown。

一文定義は `seed-start-deadline`・`seed-selective-reporting`・`seed-token-reset` のdescriptionへ進む。三つとも二重引用符付きのAI編集定義であり、意図の確認・文言へのHuman Review・実地効果は別である。今回の共通対応は[運用文書](../operation.md)§1.1・§4.1・§6、個別経験と根拠はR04が所有する。

### 3.11 協働の目的と、Skillを固定しない理由を理解する

R04の `collaborative-problem-solving`・`multi-problem-discovery`（Source `work-s01`・`work-s03`）から、Human–AI協働による問題解決と、複数の難所へ効く接続を積極的に探す意図を読む。RootやTeshuvahを実務目的へ置き換えるものではなく、画期的成果を毎回保証するものでもない。

`holiday-action-connection`（`work-s02`）は、実生活への接続が進み、休日のAI対話時間が減ったことを利用枠余剰の一因としたHumanの説明を保持する。対話・報告・消費の減少だけで成果の低下を推定せず、個別実績や因果の寄与量は補完しない。実際に使える共通対応は[運用文書](../operation.md)§1.2・§3へ。

`problem-solving-skill-possibility`・`future-ai-skill-discretion`・`problem-solving-plan-authorized`（`work-s03`–`work-s05`）から、Skillの作成価値への問い、Future AIを拘束しないCorrection、Plan-onlyから今回の実行承認への移行を区別する。採否判断と成長方針は[Skill共有Hub](../../skills/README.md#51-future-aiへの開放性とskill追加の判断)が所有する。経験原本は導入成功や実地効果を先取りしない。

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

過去経験への補足はその経験原本へ、新しい出来事は発言元Threadの原本へ戻す。形成経緯や索引にも影響すれば対応箇所を更新する。原本を移設・複製して参照切れを修復したことにしない。各原本のcoverage・excludes・収録終端を確認し、「索引に見当たらない」を「出来事がなかった」と読み替えない。今回の目的に必要な未収録が分かったら所在や不足を明示し、必要な取得・Humanへの補足確認だけを行う。

このフォルダ単体にはJSONと共有仕様の全実体を同梱していない。Repository内リンクやアクセス可能な原本が必要である。資料の持ち出しを設計する場合は[改訂ガイド](../maintenance.md)の配布境界を扱う。

EOF::TASK_MODE_SYSTEM_EXPERIENCE_INDEX::v0.3.3
