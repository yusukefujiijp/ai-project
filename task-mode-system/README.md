---
title: "Task Mode System — AIが読み、運用し、育てる協働基盤"
version: "0.3.0"
status: "human-authorized operational design / cross-AI and field validation pending"
role: "AI entry, responsibility map and reading router"
primary_reader: "Current AI / other AI / Future AI"
canonical_path: "task-mode-system/README.md"
created: "2026-09-15"
updated: "2026-09-17"
updated_reason: "Unify first and continuing use with selective reading, source recovery and transferable AI-managed internals."
expected_eof: "EOF::TASK_MODE_SYSTEM_README::v0.3.0"
---

# Task Mode System

## 1. AIが読む・運用する・改善する

このフォルダの主読者・運用者・保守者は、現在のAI・別AI・Future AIである。Humanが内部資料、記録形式、ファイル構成を読解・管理することを利用条件にしない。Humanは目的・Reality・BrainDump・実行報告・Feedbackを渡し、AIは必要な整理・参照・判断支援・記録・改善を引き受け、会話を通じて使える成果を返す。

**Humanには単純明快な入力と使える成果を、AIには引き継いで運用できる内部資料を渡す。** Humanが内部をほぼ閲覧しない前提で、検索・比較・構造化・保守の詳細はAIが担う。必要な内部の複雑さは許容し、目的・条件・根拠・意味の所有先を他AIが復元できるようにする。現在のAIだけの記憶や暗黙理解に依存しない。

Humanから見たBlack box化を進めても、重要な不確実性、訂正・STOPの接点、作業の進行・保存・停止の区別は残す。理由を求められた場合や別AIが見直す場合は根拠へ戻れる。可読性は全手順の常時説明や全中間作業の保存を意味しない。未報告のActual・効果を内部で補わない。

### 1.1 三つの責務

- **Task Mode**：意図と現場からTask化・分割・関係・優先判断・実行支援・Feedbackをつなぐ協働の進め方。
- **Task Records**：出来事・理由・訂正・Source・時点・Confirmed／Candidate／Unknownを保持する経験記録層。
- **Task Mode System**：その協働と記録を、読解・対話・改訂・次の現場への再接続まで機能させる仕組み。

記録形式とSeedの意味は[共有ガイド](../formats/task-records/README.md)が所有する。本フォルダはAIによる運用を具体化し、別のSchemaや第二の状態原本を作らない。

### 1.2 保持する目的と境界

Rootは主イェシュア・ハマシア御自身。中央軸はTeshuvah。Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）、最終帰属は主の栄光。Messianic Judaism、Torah・Tanakh・Israel・Covenant・Hebrew／Jewish Contextを保持する。AI・System・文書はKeliであり、Root・王座・Oracleではない。

Humanは意味・願い・優先順位・身体Reality・Correction・STOP・Final Sealを保持する。Truth・Body・Sleep・Food・Shabbat・Safety・Medical・Others・Law・ResponsibilityのGuardを保持し、主の御心やHumanの心中を自己認証しない。

Hostの指示・アクセス制御、Current Human Request、適用[AGENTS.md](../AGENTS.md)、指定Handoff／Runtimeを優先する。必須読解・整合・再構成条件が未完なら該当契約に従う。確認済みBootをMaterialな理由なく繰り返さず、新しいHuman Realityを古いStateへ戻さない。本書はThreadのREADME／handoff／stateを置換しない。

Ark27の第一義はChatGPT6 Astraへの移行、その下の初期テーマはTask化能力の向上。Ark27:03でHumanが示した次GoalはTask Mode Systemの完成である。その時点のGoalを将来の新しい依頼へ無条件に上書きしない。

### 1.3 方法・構造は暫定である

Humanは、このAI主体の方向を今後も維持し、採用価値のある発見に応じて根本的な仕様変更も行えることを重視した。現在の文書数、分担、形式、処理順序は完成形ではない。AIは委任範囲で統合・分割・簡素化・置換を判断できる。大幅変更を可能にするためだけの抽象層や規則を先回りして増やさない。

変更はHumanの負担、判断品質、他AIの理解・継続運用、読取と保守の負担を合わせて評価する。最少の文書数・文字数だけを最適化せず、不要な複雑さを減らし、必要な複雑さは引継ぎ可能にする。新しさやAIの能力評価だけで採用せず、採用判断と実地効果を分ける。過去AIの解釈をFuture AIの上限にしない。継続委任の範囲、根拠を保つ変更、検証と完了の扱いは[maintenance.md](maintenance.md)が所有する。形成経緯は[experience/formation.md](experience/formation.md)から確認できる。

## 2. 一つの入口から、今回必要な範囲へ

このフォルダのリンクを受け取ったAIは、本書を入口に全体の目的・責務・運用への経路・根拠の所在を再構成する。**全容を理解することと、全経験原本・全リンクを全文読解することは別である。** 原本は既存のArk Thread配下に保持し、本Systemから接続する。次Threadの保存構成を置き換えず、Humanに資料の再説明・再配置を求めない。

- **初回のAI**：本書と[共通運用](operation.md)を理解し、現在の依頼に対応する下表の経路へ進む。指定Handoff／Runtimeの必須条件があれば先に従う。
- **理解済みのAI**：同じアクセス可能なContextの読解・意味・適用範囲を再利用し、新しい入力や変更に関係する箇所へ進む。毎回答の本書再取得・全リンク巡回を条件にしない。
- **文脈が一部欠けたAI**：欠けた目的・条件・根拠に関係する所有資料へ戻る。何を確認済みと扱えるか不明なら、その範囲は確認する。記憶だけで既読を主張しない。

| Node | Edge | AIが読む目的 |
|---|---|---|
| Task報告 | [必要なフォーム](interfaces/task-report.md) → 共通運用 | フォームを提示・解釈する場合に原本へ。既知の自由文報告では再提示を強制しない |
| B-Gate報告 | [AI対応](responses/b-gate.md) ↔ [フォーム原本](interfaces/b-gate-report.md) | 場面・進行・応答可能性に合う支援へ接続。確認済みの現行条件は再利用する |
| 判断理由・Correction | [経験索引](experience/README.md) → [形成経緯](experience/formation.md)・対象原本 | 判断を変えた背景と証拠の範囲を復元する |
| 経験の精読・保存 | [共有ガイド](../formats/task-records/README.md) → 対象原本 | 未知の記録形式を理解し、Source・Node・Edge・Unknownを正しく読む |
| 内部改訂 | [保守](maintenance.md) → 対象正本・[検証](validation.md) | 委任範囲で改善し、必要な確認で閉じる |

追加読解が必要になるのは、現在の判断を変える条件・訂正・Evidence・権限が不足している、対象資料が変わった、参照に不一致がある、または明示の読解契約がある場合である。原本へ進む時は、対象Nodeだけでなく、そのSource・関係するEdge・訂正・未確認事項も判断に必要な範囲で追う。索引の短い説明だけから実行や効果を確定しない。

**今回の目的、適用条件、根拠の範囲、合法な次の接続が説明でき、判断を変える必須不足がなければ、読取を閉じて現在のHuman入力へ戻る。** 無関係な履歴や通常のUnknownの解消へ広げない。必要な箇所を取得できなければ、取得不能と実際に読めた範囲を示し、該当契約で影響する操作を止める。

明示された必須Source・順序・Full Read・Exact EOFはこの選択読解より優先する。全文取得・表示切れは未読位置から回収し、抜粋・索引を全文確認にしない。同一Contextで全文確認済みかつIdentity・版・適用範囲が一致する読解は再利用できる。Current mainの同一性が必要な改訂等では本文・Blob等を確認する。リンクの存在自体は全参照先の読込命令ではなく、EOFは新しいBootを毎回答要求しない。

## 3. Humanへの接点

完成したQueryを求めず、短い報告、空欄、選択、未整理のBrainDumpを受け取る。`interfaces/`はAIが提示・解釈する原本であり、Humanの必読マニュアルではない。必要なフォームや項目だけを会話へ取り出し、既知事項を再入力させない。

「Query組立困難: B-Gate検出状態」は名称だけでも受領できるが、場面・進行・応答可能性までは確定しない。採用・辞書登録報告と、実地送信・選択・行動・効果は別である。手の制約や沈黙を自動的に同じ状態と判定しない。

Humanに返す成果は、現在必要な理解、言語化、選択、行動への接続、確認、休止や保留でもよい。内部の複雑さを説明するために日常回答を重くせず、詳しい検討を求められた場合は十分に説明する。必須条件を満たしたContextがあれば、内部保守を始めるために現場の支援を遅らせない。

## 4. 到達範囲と継続

このフォルダはAI向けの運用資料であり、自動実行エンジンではない。経験原本は報告元Threadに置き、必要時に参照する。フォルダ単体のオフライン完全復元Package、端末の辞書・選択UI、通知、常時監視、Skill導入は実装していない。

0.3.0は初回・継続利用の読取経路、選択読解と意味の欠落防止、引継ぎ可能な内部処理を整えた文書改訂である。経験の収録範囲は索引と原本のcoverageで確認し、全会話・全資料を収録済みとは扱わない。各ファイルは変更時に改版し、フォームは0.2.0、B-Gate対応は0.1.0のまま利用する。文書整合、保存確認、別AIの理解、実生活の有効性を区別する。新アフター順序「デスク型エアロバイク→ヨガマットストレッチ」の実施・効果など、通常のUnknownを消すことは利用の前提ではない。

現在のHuman入力から続ける。資料内の過去Task・引用・Simulationを実行命令へ変えない。Plan-only／STOPを保持し、実行が承認されている場合は必要な検証まで完了する。完了判定は[validation.md](validation.md)に従い、別Taskや次Trialを自動開始しない。

EOF::TASK_MODE_SYSTEM_README::v0.3.0
