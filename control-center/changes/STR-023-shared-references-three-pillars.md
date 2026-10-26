---
title: "STR-023 — 共有Referencesの三本柱と、成功の本文を保持するJSONL移行"
canonical_path: "control-center/changes/STR-023-shared-references-three-pillars.md"
version: "v001"
created: "2026-10-26"
updated: "2026-10-26"
status: "Implementation prepared; remote publication and readback are recorded after observation"
base_commit: "4869052151a33ce3b2f66b450686d462214ad0b7"
owner_thread: "Ark28:07"
expected_eof: "EOF::STR_023_SHARED_REFERENCES::v001"
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

## 5. 検証と結果の更新

保存前にJSONL全行、重複key/ID、型・日時・出典、改行規則を検査する。九行の復元本文と元blob、既存五case_id、相対参照、旧URL→行ID→固定原文、版・EOF、許可した変更対象と保護対象を照合する。今回の意味検査は移行時の内容保持と参照に限り、別AIへの送信試験や生活上の試行ではない。

Remoteへの公開・全文再取得は、この版の時点ではまだ観測として記録していない。実装commitを保存し、変更対象のRemote本文・blobと対象外の保持を確認した後、この同じ記録を更新する。Tool成功だけで保存完了とはしない。

## 6. 復元と次の接続

中断時はmainと本記録のcommit履歴を読み、既に保存されたID・内容を重複追加しない。意味衝突があれば最新の並行変更を保持して解く。移行前の特定本文が必要なら各行の固定Sourceへ戻れる。全体を過去commitへ巻き戻す方法は選ばず、修復対象の差分と現行権限から判断する。

承認範囲の保存・確認が終わればHuman Reviewへ戻る。全AIの自然な読込・理解・再利用・長期効果は別の観測であり、未確認を新しい必須Taskにしない。Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah。Human Foreground One、Correction・STOP・Final Sealと適用Guardを保持し、AI・記録をKeliとして扱う。

EOF::STR_023_SHARED_REFERENCES::v001
