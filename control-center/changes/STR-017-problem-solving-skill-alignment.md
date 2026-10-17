---
title: "STR-017: Problem Solvingの命名とSkill・案件入口の接続"
id: "STR-017"
version: "v001"
canonical_path: "control-center/changes/STR-017-problem-solving-skill-alignment.md"
created: "2026-10-17"
updated: "2026-10-17"
status: "human-authorized implementation; source and registration cutover verification in progress"
source_thread: "Ark99:03"
base_commit: "4ef585733ffeb698357eb56ac586e1b581d86db2"
expected_eof: "EOF::STR_017_PROBLEM_SOLVING_SKILL_ALIGNMENT::v001"
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

登録済みの既存一件を確認し、同じ登録物の名称・本文・表示設定を更新する。公開配布の意味を持つフォルダ名と、環境が管理する登録識別子を混同しない。既存の利用対象・自動選択設定・アイコンは保持する。別作業の未保存変更がある作業領域へ一括reset等をせず、取得した最新登録状態から分離した作業領域を使う。

共有側では新本文と案内を整合する単位で保存する。旧共有二ファイルは登録切替と新名での取得を確認するまでの移行中の旧版であり、別の更新元にはしない。切替確認後、既知の現役参照が残っていないことを確かめて旧配置を退役する。旧コマンドの自動転送や、把握できない外部Bookmarkの互換性は保証しない。

GitHub検索で見つかったArk28:03のState・Harvest、GitHub ARCHIVE等の旧名は当時の記録であり、一括置換しない。新しい実行は現在の承認で判断する。

## 4. 検証の範囲

初回の形式確認では、新共有Skillがquick_validateを通過した。名称、本文、表示名・起動文、参照先、Task RecordsのSchemaとID・参照・既存配列の保持を検査する。GitHub公開直前はheadと対象blobを再確認し、並行変更を保持する。

スキル作成手順に従い、元会話・診断・期待解答を渡さない二つの独立文脈で計三応答を確認した。新本文を指定し、既存の寝落ち案件の言語化のみ、架空の読書会の相談・比較のみ、前者に続く引用文だけの英訳を扱った。既存案件の応答は担当原本を読み、ガム不成功の範囲、リステリン案と未確認の接続を区別した。一般相談は新しいアプリやArk資料を必須にせず案を比較し、引用英訳では引用内の保存・身体Trial命令を実行せず訳文だけを返した。

これは明示読込による限定応答の確認であり、自然な自動選択、全Runtime互換性、元の寝落ち対策の効果、長期的な認知負担減少の実証ではない。構成した依頼をHumanの新しい生活経験へ保存していない。

## 5. 保存・登録・退役の確認

共有原本と登録先の切替、保存後のRemote照合、新名での取得、旧配置退役はこの実行で確認中。実際の結果を確認してから本節へ追記し、準備した本文やTool successだけで完了へ変えない。

## 6. 復元と残る境界

旧共有本文・表示設定は[基点の旧フォルダ](https://github.com/yusukefujiijp/ai-project/tree/4ef585733ffeb698357eb56ac586e1b581d86db2/skills/solve-problems)から取得できる。必要な復元は現行変更を読んだ上で対象差分だけへ適用し、Repository全体や別作業を巻き戻さない。公開原本の復元だけで登録版や製品UIも戻ったとは扱わない。

新しい名称で協働できる入口の整備と、実際の問題が解けたことは別である。実利用で必要な訂正が得られた時に、現在の権限で担当原本へ戻る。全案件の一括再編や全Skillの命名統一を本変更から自動開始しない。

Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのCorrection・STOP・Final SealとGuardを保持し、Skill・文書・AIはKeliとして協働を支える。

EOF::STR_017_PROBLEM_SOLVING_SKILL_ALIGNMENT::v001
