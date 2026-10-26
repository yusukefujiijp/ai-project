---
title: "STR-023 — 共有Referencesの三本柱と、成功の本文を保持するJSONL移行"
canonical_path: "control-center/changes/STR-023-shared-references-three-pillars.md"
version: "v002"
created: "2026-10-26"
updated: "2026-10-26"
status: "Implementation published; all 21 changed files fully reread and matched; downstream effects unverified"
change_reason: "実装commitと全変更対象の全文・blob再取得一致を観測し、同じ記録へ完了証拠を追記する"
base_commit: "4869052151a33ce3b2f66b450686d462214ad0b7"
owner_thread: "Ark28:07"
expected_eof: "EOF::STR_023_SHARED_REFERENCES::v002"
---

# STR-023 — 共有Referencesの三本柱

## 1. 目的と現在の権限

HumanはReport側で成立したfeedback・lessons・success-casesの三本柱を、共有Referencesへ広げたいと希望した。目的は、元の反応をAIのその時点の一般化へ閉じ込めず、次のAIが条件と根拠へ戻って判断を育てること。三本への必須登録、全領域の一括移設、全AIの自動学習を意味しない。

共有側のPlan Modeでは、Feedback原本の追加、成功九件の豊かな本文を保つJSONL化、Report側の共通契約への接続、通常案内と固定証拠・厳密Bindingの区別を提示した。直後のCurrent Humanは「途中まで実行できたが止まったようだ続行して下さい！」と指示した。この限定継続の範囲で実装・必要な検証・保存後再取得へ進む。過去のGoや好評価を今回の権限の根拠にしない。

検査済み二十一ファイルの保存へ進む旨を返した後、Humanは現在の入力で「Execute GitHub OK!」「Human Seal OK!」「実行して下さい！」と明示した。この後続承認も同じ対象・範囲の保存と確認に適用し、別案件・設定・外部AI送信へ拡張しない。

再開時のRemote mainは`4869052151a33ce3b2f66b450686d462214ad0b7`で前回Plan基準と同一だった。Report側のFeedback二件・lesson一件・成功一件は保存済み、共有側への今回の差分は未保存だった。Humanの中断報告を、未観測のWrite成功や失敗へ置き換えず、保存済みのReport側を重複実行しない。

## 2. 対象と保持する原本

共有References入口、共有Feedback README/JSONL、成功事例README/JSONL、九つの旧Markdownの互換案内を整える。Report側は親・Feedback・success-case READMEの契約接続だけを更新する。Root READMEの既存一行案内、GitHub専門入口/PLANの限定参照、本記録を合わせる。

共有lesson五件、Skills lesson七件、Report側の全三JSONL、Dots固有原本、AGENTS・ARK・GCI・登録Skill・Project/予定・他ThreadのState・wikiは対象外で保持する。全16 references系フォルダへの機械的な三ファイル設置や、私的Work・長期メモリの公開は行わない。初期共有Feedbackは改善希望の原文抜粋一件で、公開可能な本対話のその一文以外を新たに収集しない。

## 3. 九事例の識別と完全復元

現行本文は[共有success-cases JSONL](../../references/success-cases/success-cases.jsonl)。元metadata・本文・EOFはそれぞれlegacy_document.front_matter、case、legacy_document.suffixに保ち、初回移行版では連結して元のUTF-8全文とblob SHAを照合できる。既存case_id五件も保持する。新行の登録日時`2026-10-26T11:37:53Z`は、元の出来事・作成日とは異なる。

| 旧Markdown | 現行行ID | 移行元blob |
|---|---|---|
| `ark27-03-to-04-transition.md` | `32f01804-5fba-4589-98f0-96dd61a15ccd` | `bbe3435a83489a4dbfce4355e6a546a46552290c` |
| `decisive-choice-single-log-preserved-history.md` | `af7d65da-b84c-4444-905f-430ea4ba7c3b` | `762bb42ed5c19ba7864db30fb49fb57b4ce52fd8` |
| `leading-response-status-markers.md` | `96f52571-27ed-47bb-8861-89404e009a84` | `d90f4450b542d741ee34f2774ddcc5cf5cbb9764` |
| `next-query-as-continuation-interface.md` | `9fe92b09-027d-4043-9bd6-33c47f794d2d` | `d4808436f6299356b46aef126689960623b691f1` |
| `one-skill-entry-multiple-benefits.md` | `6fc3fb1c-2858-4ecc-92f3-012d816c319b` | `3a6d7d28d264d57bb7c8b26bb2bfb525eb5af0de` |
| `one-transition-entry.md` | `502586fb-490c-4f2b-bfc2-67c2e62461bf` | `6706da2cc1457bd10504742e840acd078d07d18a` |
| `puzzle-emoji-and-agency.md` | `5b70cf11-24d4-48f5-b4e9-24df0d13f860` | `e7ebf211213943f29315b3b716e8c998021a23b4` |
| `skill-naming-as-reusable-handles.md` | `8dbee71a-5270-42d6-b022-c89d3bb5dd05` | `19bf95186739c7a37cfa03b31ce6a7149f4977e9` |
| `wake-up-one-choice.md` | `04d636c0-c86a-489e-b121-8199e5d51da5` | `b674393e202e457ede404c4ae3b4cfd460b109ad` |

移行元の固定commitは`4869052151a33ce3b2f66b450686d462214ad0b7`。各行のsourcesと旧URLの案内から固定原文へ戻れる。本文を要約せず、Humanの喜び・評価・訂正・形成順序・根拠・未確認・当時のstatusを保つ。語句を変更していないことと、成功原因や長期効果が実証されたことは別である。

## 4. 参照と契約の境界

現在のRepository検索ではsuccess-cases/の参照が54ファイルで見つかった。通常の入口・現役Skillの任意参照・固定commitのReport証拠・歴史Handoff等を分けて確認した。宣言EOF文字列の検索では各事例とその入口が一致し、今回確認した現役の直接参照に、九本文を同一Current blob/EOFで要求する契約は見つからなかった。検索結果を全外部利用者の不存在証明にはしない。

旧MarkdownのURLは対象IDと固定原文への案内として維持する。案内だけを旧本文の全文読了にせず、厳密な契約の指定版・Identity・EOFを優先する。移行を許容しない契約が別環境で確認された場合は、影響する読取とその回復を個別に扱う。旧Handoffや過去の固定証拠、登録Skillを一括書き換えない。

Feedbackとcaseの汎用行形式・読取・更新契約は共有子READMEが所有し、Report固有の対象・初期収録・Artifact配置接続はReport側に残す。lessonの既存契約は移さない。行schemaはfeedback 1 / lesson 2 / case 1であり、同じ番号へ揃える必要はない。

## 5. 保存と再取得の確認結果

[実装commit `836e814088e444e51f52ac540a872cd7620ad23e`](https://github.com/yusukefujiijp/ai-project/commit/836e814088e444e51f52ac540a872cd7620ad23e)をmainへ保存した。親commitは`4869052151a33ce3b2f66b450686d462214ad0b7`、実装treeは`a053512f60a869b7c5a9cacd52b93de263f1b24b`。期待する親SHAを指定し、forceを使わず更新した。実装後のmain再確認時刻は`2026-10-26T11:51:44Z`で、同じ実装commitを指していた。

- 変更範囲は既存十七ファイルの更新・四ファイルの追加・削除ゼロ。Recursive treeを比較し、対象外の既存七百四blobがすべて同一であることを確認した。
- 変更対象二十一ファイルを実装commitからそれぞれ全文再取得し、保存予定本文との完全一致とblob SHA一致を全件確認した。Toolの保存成功だけを完了根拠にしていない。
- 共有Feedbackは一件、共有lessonは既存五件のまま、共有成功は九件となった。Report側のFeedback二件・lesson一件・成功一件、Skills lesson七件のデータ本文は変更していない。
- 九件すべてについて`legacy_document.front_matter + case + legacy_document.suffix`から元の全文を復元し、§3の移行元blobと一致した。既存case_id五件、元の日付・出典・評価・Correction・当時の未確認を保持した。
- JSONL全行の重複key/ID、型・日時・空でない出典、UTF-8/LF、空行・独立したEOF行の不存在を検査した。READMEと本文内の版・canonical_path・宣言EOF、旧URL→行ID→固定原文の対応も確認した。
- 対象本文と復元した原文に含まれる相対Markdown参照二百八十件の参照先が存在することを確認した。これは外部URL全件のHTTP応答や全anchor、全環境の厳密読取契約を試験したという意味ではない。
- 共有Referencesの歴史説明、Report Feedbackの初期収録説明は保存前後で一致する。AGENTS・ARK・GCI・登録Skill・設定・予定・他ThreadのState・wikiは変更していない。

主要な保存済みblobは、共有Feedback JSONLが`2ef142a2c3a33adf7ce7fe1b75df5f32512a7539`、共有成功JSONLが`cfe467b17a832e0b24dd8f9842eeabd30d2096ef`、共有References入口が`c3631c2d6a40f47c19690c22f6b41d4c98424236`である。すべて上記実装commitから取得できる。

本v002は、実装commitと二十一ファイルの再取得で既に観測した結果を記録する。実装commit内の本記録はv001であり、本v002の保存commitはGit履歴で別に識別する。記録更新を実装の再実行にせず、本記録だけの保存・再取得確認へ進む。文書・データと参照の整合が確認済みであることと、全AIによる自然な読込・理解・再利用や実生活上の効果が実証されたことは分ける。

## 6. 復元と次の接続

中断時はmainと本記録のcommit履歴を読み、既に保存されたID・内容を重複追加しない。意味衝突があれば最新の並行変更を保持して解く。移行前の特定本文が必要なら各行の固定Sourceへ戻れる。全体を過去commitへ巻き戻す方法は選ばず、修復対象の差分と現行権限から判断する。

承認範囲の保存・確認が終わればHuman Reviewへ戻る。全AIの自然な読込・理解・再利用・長期効果は別の観測であり、未確認を新しい必須Taskにしない。Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah。Human Foreground One、Correction・STOP・Final Sealと適用Guardを保持し、AI・記録をKeliとして扱う。

EOF::STR_023_SHARED_REFERENCES::v002
