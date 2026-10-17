---
title: "STR-017: Problem Solvingの命名とSkill・案件入口の接続"
id: "STR-017"
version: "v002"
canonical_path: "control-center/changes/STR-017-problem-solving-skill-alignment.md"
created: "2026-10-17"
updated: "2026-10-17"
status: "shared and registered README verified; new-name skill read and legacy retirement complete"
source_thread: "Ark99:03"
base_commit: "4ef585733ffeb698357eb56ac586e1b581d86db2"
expected_eof: "EOF::STR_017_PROBLEM_SOLVING_SKILL_ALIGNMENT::v002"
---

# STR-017: Problem Solvingの命名とSkill・案件入口の接続

**問題解決という一つの意味から、現在必要な協働と既存の知見へ戻れるよう、Skillを `solve-problems` から `problem-solving` へ揃え、案件原本への条件付き案内を追加する。** 共有原本、既存の登録物、取得・挙動、実生活での効果を別々に確認する。

## 1. Humanの意味・Correction・承認

[Ark99:03経験原本](../../ark-project/ark99/ark99-03/task-records.json)の `naming-s01`–`naming-s07` と関係するNodesが形成を所有する。HumanはSkillとproblem-solvingフォルダの連携を問い、名称差を分かりづらいと指摘した。

AIが「Humanが自然に使った名前」と解釈したことに対し、Humanは「問題解決をAIで翻訳しただけ」と訂正し、一から最善を考えることを求めた。翻訳結果、使用した表記、好み、設計の採用承認を同じ証拠にしない。意味・用途・共通入口の一貫性から比較し直し、共通名を「問題解決 / Problem Solving」、Skillを `$problem-solving`、問題の入口を `problem-solving/` とする方向を提案した。

方向への合意後、HumanはPlan Modeで調査・計画提示だけを指定した。その段階では変更しなかった。2026-10-17 17:46:52 Asia/Tokyoの後続発言で、既存登録確認、改名、条件付き案件案内、共有と登録の切替、検証という五工程計画への実行承認を受けた。過去の初期構成承認だけを本変更へ転用したものではない。

## 2. 役割と変更範囲

- [Skill本文](../../skills/problem-solving/SKILL.md)と[表示設定](../../skills/problem-solving/agents/openai.yaml)：名称・表示名・標準起動文を揃える。既存の柔軟な方法選択、品質、権限、基本支援の自己完結性を保持する。
- [Skills Hub](../../skills/README.md#38-問題解決の共通入口)：現役一覧・起動文・共有URLと旧名の対応を案内する。過去の形成・導入観測に現れた旧名は当時の事実として保持する。
- [Problem Solving入口](../../problem-solving/README.md)：再利用する方法の参照を更新し、Skillが方法選択、フォルダが案件と担当原本への案内を所有すると明示する。
- [経験原本](../../ark-project/ark99/ark99-03/task-records.json)：上のHuman Correction・方向採用・計画と後続承認を追加する。既存の睡眠関係の記録・Unknownを保持する。
- [GitHub整理入口](../github/README.md#change-records)：本記録への所在案内を加える。実行の日時記録は[当日records](../../records/2026/10/2026-10-17.jsonl)へ一活動として残す。

追加する案内は、Arkの既存問題の継続、または過去の成果・訂正・未解決事項が今回の判断を変える時に使う。既知の担当原本へ直接進み、所在不明なら問題の入口から探す。新規相談にcase作成・全件読込を要求せず、一般の相談へArk資料を一律に適用しない。任意資料の不足と必須Source不足を区別する。

現在判断はcase等、原発言と出来事は経験原本、専門知識は専門資料、共通方法はSkillが所有する。通常利用ごとの自動保存・方法改訂・同期コピーは追加しない。Body Trial・摂取・通信・Reset・他Task、ArkのThread Title／Handoff／Current所有関係を変更する権限は含まない。

## 3. 変更前の確認と移行方法

基点は `4ef585733ffeb698357eb56ac586e1b581d86db2`。共通AGENTSとArtifact → GitHubの確認済み原本は同一blobだった。共有SKILL.mdのblobは `4db06271ecb42b22c3f70160de577439858b37b2`、取得した登録本文と一致した。Problem Solving入口からSkillへの案内は既存だったが、Skillから案件入口への具体案内はなかった。

登録済みの既存一件を確認し、同じ登録物の名称・本文・表示設定を更新した。公開配布の意味を持つフォルダ名と、環境が管理する登録識別子を混同しない。既存の利用対象・自動選択設定・アイコンの保持を再取得で確認した。別作業の未保存変更がある作業領域へ一括reset等をせず、取得した最新登録状態から分離した作業領域を使う。

共有側では新本文と案内を整合する単位で保存する。旧共有二ファイルは登録切替と新名での取得を確認するまでの移行中の旧版であり、別の更新元にはしない。切替確認後、既知の現役参照が残っていないことを確かめて旧配置を退役する。旧コマンドの自動転送や、把握できない外部Bookmarkの互換性は保証しない。

GitHub検索で見つかったArk28:03のState・Harvest、GitHub ARCHIVE等の旧名は当時の記録であり、一括置換しない。新しい実行は現在の承認で判断する。

## 4. 検証の範囲

新共有Skillと既存登録向け本文はquick_validateを通過した。Task Recordsは24 Sources・22 Nodes・7 Edges・3 Open QuestionsでSchemaとID・参照を検査し、既存配列を保持した。追加・変更した参照16件とanchor 2件、名称・表示・metadata・Exact EOFを確認した。GitHub公開直前のheadは基点と一致し、最新Hub v0.38.2までの別作業を保持してv0.39.0へ更新した。

スキル作成手順に従い、元会話・診断・期待解答を渡さない二つの独立文脈で計三応答を確認した。改訂候補の本文を指定し、既存の寝落ち案件の言語化のみ、架空の読書会の相談・比較のみ、前者に続く引用文だけの英訳を扱った。既存案件の応答は担当原本を読み、ガム不成功の範囲、リステリン案と未確認の接続を区別した。一般相談は新しいアプリやArk資料を必須にせず案を比較し、引用英訳では引用内の保存・身体Trial命令を実行せず訳文だけを返した。

限定応答後、Arkの条件が段落全体へ係ることを一文で明確化し、公開本文の形式・参照を再確認した。これは明示読込による限定応答の確認であり、自然な自動選択、全Runtime互換性、元の寝落ち対策の効果、長期的な認知負担減少の実証ではない。構成した依頼をHumanの新しい生活経験へ保存していない。

## 5. 保存・登録・退役の確認

### 5.1 初回保存時の確認と保留（Historical）

[共有版の初回保存](https://github.com/yusukefujiijp/ai-project/commit/14e47d7a12e01b441536598a974bcdb64d1fc203)で7ファイルをmainへ反映し、全対象をRemoteから再取得して意図した全文と一致した。新SKILL.mdのblobは `69dc2fc5a3a443be040f566cc3b87fb93ab4f72a`、SHA-256は `ea971c22f8f299613b2126c1998cec5939e9dc33111bdf63db54257ff8523abb`。本文・表示設定・Hub・Problem Solving入口・経験原本・本記録・GitHub整理入口が対象だった。

同じ既存登録物への通常保存が成功した。保存先を再取得して、名称 `problem-solving`、共有SKILL.mdとの全文一致、表示名・短い説明・起動文の値の一致を確認した。登録先の対象名は一件で、旧名の別登録は増やしていない。既存の利用対象、自動選択設定、アイコンを保持し、他の登録済みSkillを変更していない。これは登録保存先の確認であり、会話での取得確認とは別である。

**初回保存時に残った取得Gate。** この会話へ提示されるSkill一覧は、再取得しても旧名 `solve-problems` を返した。旧packageからの読取は `failed to read skill resource`、新名packageは `skill package is not available` となり、同じ登録対象の新resourceを指定した読取も成立しなかった。登録先の新本文の一致と、この会話の取得機構の不一致を区別する。原因・反映時期は未確定であり、保存失敗と決めつけて再作成・再登録はしない。

したがって、旧共有 `skills/solve-problems/SKILL.md` と `agents/openai.yaml` の二ファイルは今回退役せず、切替中の参照用に保持した。新しい更新元は `skills/problem-solving/` のみ。旧パスは基点の内容を保ち、新しい原本との同期更新を行わない。既知の現役案内は新パスへ更新済みだが、取得Gateの未成立を「改名移行の全完了」としない。

再開時は、更新されたSkill一覧から同じ登録物を解決し、新名の本文を実際に取得して共有版と比較する。成功したら、最新head・既知の参照・旧二ファイルの同一性を確認し、今回の承認範囲で旧配置退役と結果記録まで進める。同じ承認の再取得は不要。Humanの新しいCorrection・STOPや対象変更があれば、その現在条件に従う。

この確認結果と保留をHubと当日recordsへ反映する最終保存は、保存先の再取得で確認する。確認記録のためだけの自己参照commit追記を反復しない。

### 5.2 後続確認と起動Queryの保存（2026-10-17）

Humanは「起動Queryを書き出して下さい！ $problem-solving スキル内のREADME.mdにもsaveして下さい！」と依頼した。同じ既存登録物の新名でSKILL.mdを全文取得でき、共有本文のblob `69dc2fc5a3a443be040f566cc3b87fb93ab4f72a` と全文一致した。前節の取得不一致は過去時点の観測となり、旧共有配置退役の再開条件を満たした。mainは `28d79b8cffe0b008e18cc00d2bcab71c10491773`、旧二ファイルのblobは第3節の基点と同一だった。検索と既知の現役案内を照合し、残る旧名は形成履歴・復元先として保持する。

Human指定により、[Skill内README](../../skills/problem-solving/README.md)へ標準起動Queryと使い方を追加する。標準文は既存の表示設定の `default_prompt` と一致させ、SKILL.mdの手順は変更しない。HubはQuery本文の重複を避けてREADMEへ案内し、同時にmetadata版と末尾の版表記を揃える。旧共有のSKILL.md・agents/openai.yamlだけを退役対象とし、新しいcaseや別Skillは作らない。

登録先へREADMEを保存し、Remoteから同じ全文を取得した。READMEのSHA-256は `00f02c0ca98a2a6674db92010c55bbefda4cf7d15b257f9c801efb8718976722`。自身の登録用commitはREADME一件だけを追加し、RemoteでもSkill本文・表示設定の不変を確認した。登録先の再取得には同じSkillのicon.svg差分も現れたが、自身のcommitには含まれず、発生理由は未確認。別Skillの変更はなかった。

新名SKILL.mdの会話内取得成功と、追加READMEの取得機構は区別する。READMEを会話のSkill resourceとして直接読む試行は `failed to read skill resource` となった一方、登録保存先の現物は上記の通り一致した。READMEの保存失敗とは扱わず、本文の取得Gateを再び未成立へ戻さない。Human向けの共有READMEと、今回の回答内のコピー用Queryから利用できるようにする。

[共有保存と退役のcommit](https://github.com/yusukefujiijp/ai-project/commit/aa0d4f85f75fc593f473a0f98cb547dd2a8ce766)をmainへ反映した。README・Hub・本記録をRemoteから再取得し、三ファイルの全文一致を確認した。完全なTreeで旧共有二ファイルの消失を確認し、変更はこの五パスだけで対象外のblobは保持された。READMEのblobは `14f3e2f62d29e0940165fbd232d1a5f14c0abc7b`。共有・登録README、表示設定の標準起動文、metadataとExact EOFを照合済み。これにより前節で保留した旧配置退役は完了した。

この後続結果を当日recordsへ追記し、本記録の現行状態へ反映する。当初の保留記録は履歴として残す。READMEの会話内resource取得、各UIの表示、実利用の効果は保存・本文取得の確認とは区別する。

## 6. 復元と残る境界

旧共有本文・表示設定は[基点の旧フォルダ](https://github.com/yusukefujiijp/ai-project/tree/4ef585733ffeb698357eb56ac586e1b581d86db2/skills/solve-problems)から取得できる。必要な復元は現行変更を読んだ上で対象差分だけへ適用し、Repository全体や別作業を巻き戻さない。公開原本の復元だけで登録版や製品UIも戻ったとは扱わない。

新しい名称で協働できる入口の整備と、実際の問題が解けたことは別である。実利用で必要な訂正が得られた時に、現在の権限で担当原本へ戻る。全案件の一括再編や全Skillの命名統一を本変更から自動開始しない。

Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのCorrection・STOP・Final SealとGuardを保持し、Skill・文書・AIはKeliとして協働を支える。

EOF::STR_017_PROBLEM_SOLVING_SKILL_ALIGNMENT::v002
