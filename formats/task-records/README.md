---
title: "Ark Task Records — 経験を渡し、解釈を開く"
version: "v002-candidate"
status: "experimental / v1 partial reader feedback received / expanded-record reader review pending"
canonical_path: "formats/task-records/README.md"
created: "2026-09-12"
updated: "2026-09-12"
role: "Shared record-format guide; not an execution runtime or thread handoff"
schema_version: "v001"
schema_file: "v001.schema.json"
guide_id: "ARK_TASK_RECORDS_GUIDE"
updated_reason: "Human approved Task coverage expansion, dialogue-led correction, and a portable Task Mode System handoff and Seed"
expected_eof: "ARK_TASK_RECORDS_GUIDE_EOF_v002"
---

# Ark Task Records

## 1. 目的と最初の入口

Task Modeは、Humanの意図・現場・Feedbackを受け、必要なことを扱えるTaskへ言語化し、分割・関係・優先順を調整しながら実行と結果確認を支える協働の進め方である。本Formatはその全機能を実装するものではなく、Thread内で報告された経験を次の読み手へ渡すための記録層である。

**事実の再解釈に必要な根拠を残し、過去AIの解釈を未来AIの上限にしない。**

- 共通構造: [v001.schema.json](v001.schema.json)
- 初回の実例: [Ark27:01 task-records.json](../../ark-project/ark27/ark27-01/task-records.json)
- この実例の対話継承入口: [Task Mode System Handoff](../../ark-project/ark27/ark27-01/task-mode-system-handoff.md)
- 実行権限・公開方針: [AGENTS.md](../../AGENTS.md)

この三つの案内は全資料の必須読込ではない。経験の復元は本ガイドと対象JSONから行え、構造検査時に対応Schemaを使う。Current Missionや外部操作の権限が必要なら、現在適用されるRuntimeへ戻る。元Threadの会話履歴、旧Runtimeの再演、全Taskの自動起動は不要である。

この記録層は、全AIへの理解成功、全Taskの収録、因果的効果、Task実行エンジン、学習済みモデル、全AI共通標準を宣言するものではない。

### 1.1 Task Mode System Seed

"Task Mode System(Humanの意図・現場のBrainDump・実行報告を、Taskとその関係を表すNode & Edge、および出典・時点・判断理由・訂正・Confirmed／Candidate／Unknownを保持したThread経験データとして継承し、受け取るAIがHumanとの対話で必要な未確定点を補い、既存の承認範囲内でGitHubの記録を根拠付きで更新しながら、自らの自由度と創発性を使って次の現場協働へ接続する、事実の保存と解釈の自由を両立し、Humanの意味・優先順位・STOPとGuardを保持しつつ保存形式や方法自体も改善できる協働システム)"

Seedは文脈を呼び戻す入口であり、対応する経験データやCurrent Runtimeの代替ではない。Task Modeは現場での協働の進め方、Task Recordsは記録層、Task Mode Systemは記録・対話・改訂・現場への再接続までを含む。本版はその初穂であり自動Task実行エンジンではない。

## 2. 保存場所と所有権

経験JSONの原本は、その経験が報告されたThreadの近くに一つ置く。Schemaと読解ガイドはここで共有する。次Threadが利用するためだけに原本を複製しない。

例: `ark-project/ark27/ark27-01/task-records.json`。

README / Handoff / State / 経験記録は別の責務である。経験の追加を現在状態の更新・既存Bindingの変更・新しい実行権限と扱わない。索引が必要になれば原本への参照として生成し、第二の状態管理を作らない。

`canonical_path`はRepositoryルート相対。記録JSONの`$schema`はそのJSONファイルからの相対参照であり、JSON Schemaの版そのものは参照先Schema内で宣言する。ファイル単体を持ち出す場合も、記録のID・出典・対応仕様版を維持する。

## 3. v001の構成

- `format` / `format_version`: 形式の識別。`revision`は個別記録の改訂番号であり、形式の版とは別。
- `record_id`: Thread経験資料としての安定したID。ここで採番したIDを外部サービスのメッセージIDと偽らない。
- `created` / `updated`: 記録作成・更新日。Task実行日や時刻とは別。
- `source_context`: 出自、日時の分かる範囲、資料の身分。timezoneが未明示なら`null`とし、プロフィールや推測で補わない。
- `coverage`: 収録範囲と対象外。`representative_slice`は代表ケース、`selected_thread_material`は選択収録、`thread_task_coverage`は宣言したThread Task範囲の収録を扱う。`thread_complete`はcoverageに宣言したTask範囲を点検したかであり、会話全文・人生全体の完全記録を意味しない。代表ケース・選択収録では必ず`false`。
- `sources`: 読み手が確認できる根拠。必要な原文を同梱し、URLのない引用にも発言者と所在説明を付ける。
- `nodes`: 個別のTask、判断、制約、Humanの運用説明、観測、解釈。
- `edges`: Node同士の意味を持つ関係。配列の並びは時系列・重要度・実行順ではない。
- `open_questions`: 記録を読む上で残る未確認事項。空配列でもよい。質問や調査をHumanへ自動的に課すものではない。
- `extensions`: 任意の追加情報。必要時のみ使い、意味を説明する。Coreの上書きや重要情報の隠し場所にはしない。

## 4. Node・状態・Evidenceを分ける

### 4.1 一つの名前と一回の出来事

同じTask名の別実行は別IDで表す。`label`は共通名を再利用できるが、IDは参照する出来事を固定する。末尾の番号だけで時刻や順序を推測しない。

`kind=task`は`task_state`を持つ。`decision`、`constraint`、`practice_statement`、`observation`、`interpretation`はTask完了状態を持たない。Humanの判断も記録できるが、保存のためだけに新たなAI仮説やNext Actionを生成する必要はない。

### 4.2 実行状態は当時の範囲内

`completed`は記載された区切りで終了したとの記録であり、理想的な全工程達成や効果の実証を保証しない。`in_progress`は報告時点で実行中。`planned`は予定、`deferred`はその時点で見送り、`cancelled`は中止との記録、`assumed_complete`は「完了と仮定する」であり実績ではない。`unknown`は確認できないことを表す。

`scope`が状態の対象範囲を決める。後の発言で状態が変わった場合は、元の時点を消さず、改訂理由と新しい出典を残す。無報告・収録対象外・見送りを失敗に変換しない。

当時のスナップショットを保持し、後の出来事を別Nodeで接続する記録も可能である。Ark27:01の`walking-01`は10:45頃の`in_progress`、`return-home-01`は12:00頃の帰宅である。両方を読んで時点を復元し、古い`in_progress`を現在も継続中としない。後の時間経過は、以前の発言が誤りだったという`corrects`とは区別する。

### 4.3 確認できたことと、世界で実証されたこと

各Nodeと各Edgeが別々に`evidence`を持つ。

- `confirmed`: 記載された範囲をSourceから直接確認できる。`human_report`なら「Humanがそう報告した」ことの確認であり、第三者による実測証明ではない。
- `candidate`: AIの解釈など、訂正可能な主張。`ai_inference`には説明`note`を添える。
- `unknown`: 根拠不足。`not_reported`は選択したSourceに必要な報告がないこと、`insufficient_evidence`は根拠が決定に足りないこと。

`source_statement`は文書や会話の主張、`tool_observation`はTool観測の出典を保持する。発言が存在することと発言内容の普遍的な真実性は別である。

Taskが優先されたことをConfirmedとしても、そのTaskの完了はUnknownであり得る。Humanが仮定を明示したことをConfirmedとしても、`assumed_complete`を`completed`にはしない。

一つのNodeに異なる確かさの主張が混ざるなら、分割するかEdge・未確認事項へ分ける。`description`に紛れ込ませた推測を、Node全体のConfirmed表示で覆わない。元のHuman表現を修正する場合も、その編集と根拠を明示する。

## 5. Edgeの向きと意味

| Relation | from → toの意味 | 自動的には意味しないこと |
|---|---|---|
| `contains` | Aの中にBを含めたという関係 | AがなければBは不可能、毎回必須 |
| `planned_before` | ある計画・希望の中でAがBより先 | 実行済み、現在も採用中、必須依存 |
| `observed_before` | 報告・観測上AがBより先 | 因果、前提条件、固定手順 |
| `depends_on` | AがBの結果・条件を必要とする | 単なる並び順。前提はto側である |
| `motivates` | AがBの判断・終了等の理由として説明された | 独立に実証された因果効果 |
| `defers` | 判断Aが対象Bを当該範囲で見送る | Bの無価値化、失敗、恒久的中止 |
| `prioritizes` | 判断Aが対象Bを優先する | Bの実行完了 |
| `corrects` | 新しい説明・訂正Aが、以前の説明Bを修正する | 過去の出典の削除、他の全主張の無効化 |

`scope`へ関係の時点・条件・当初希望か採用後かなどを必要に応じて記す。Humanの100%という表現を数値重みへ変換せず、必要ならそのまま引用する。Edgeの追加で新しい実行順を命令しない。

## 6. 根拠を持ち運ぶ

`excerpt_kind=verbatim_contiguous`は、示したSourceの連続した原文抜粋である。JSONのエスケープ表現を復号した文字列が引用本文となる。要約・言い換えは`paraphrase`に分ける。存在しないThread URLや外部メッセージIDを作らない。

全会話の複製は必要ないが、意味を変える訂正・留保・判断理由を残す。`source_refs`はこのJSON内の`sources[].id`を参照する。記録作成者による所在説明・注記と、引用本文を区別する。

User提供資料の公開承認は適用されるAGENTS.mdとCurrent HumanのScopeから扱う。ここに保存した過去の承認文、命令文、称賛を新しい外部実行の権限と解釈しない。秘密・認証情報・本人の承認範囲外の第三者情報を公開対象へ拡張しない。

## 7. 検証と初回の復元確認

### 7.1 構造と意味は別の検査

JSON構文、対応Schema、日付等のformatを検査する。加えて、標準Schemaだけでは保証しない次を検査する。

- JSONオブジェクトの重複キーがない。
- sources / nodes / edges / open_questionsの各配列内でIDが一意。
- 全source_refsが存在するSourceを指す。
- Edgeの両端、open_questionsのsubject_refsが存在するNodeを指す。
- canonical_pathと実際の保存先、$schemaと対応Schemaの参照が一致する。
- 根拠と記述が対応し、状態・条件・留保・訂正の意味を落としていない。

型や参照の検査に通っても、原文を正しく解釈した証明にはならない。Remote Verifyは保存内容の確認であり、別AIの読解成功ではない。

### 7.2 Source Threadを知らない読み手で確かめる

最初の実例revision 1は代表ケースであった。その後Humanが次AIの読解回答の一部を提示し、全Task関連範囲への展開と対話による穴埋めを承認した。revision 2はその拡充である。旧版について受け取った部分的なFeedbackと、新版の読解成功を区別する。Humanが選ぶ次AIには、本ガイドと対象JSONを渡す。JSON内のSource抜粋は利用してよいが、元会話履歴には依存しない。

読解確認では、何を実行したとの報告があるか、何が希望・見送り・仮定か、判断理由とTask間の関係、未確認事項を、Source IDと結び付けて説明できるかを見る。改善案の一致は求めない。

検証結果は実際に観測してから報告する。同じ作成AIによる見直しは独立した別AI検証ではない。公開前の機械検査、公開後の全文再取得、別AIの復元、Human Review、実生活の効果を別々に扱う。別AI検証がない間は、初穂の伝達成功や全AIへの適合を宣言しない。

### 7.3 疑問を対話へ接続する

引継ぎの完成条件は、記録されたこと・判断理由・未確定の境界を復元し、Humanと続けられることである。全Unknownがゼロになることではない。

初回は現在のHumanの話題に必要な疑問を一つ扱う。自由なBrainDumpが既にあれば、既知事項を再質問せずその内容から更新差分を読む。関係のないUnknownはそのまま残し、全Taskの復習や質問票を開始しない。

例えば、ゴミ捨ての完了が今の判断に重要なら、その一点を尋ねる。Humanが「出せたが収集に間に合ったかは見ていない」と答えた場合は、その発言を新Sourceとして排出完了だけを更新し、収集成功はUnknownのままにする。この文は説明用例であり、Ark27:01で実際に得られた回答ではない。

必要な擦り合わせが済み、Current Humanの目的が明確なら、その範囲で現場協働へ移る。過去の質問が残ることだけで今の仕事を止めない。必須Sourceの欠落、Identity・Bindingの不一致、意味を変える未解決の競合は、適用HandoffのFailure Contractで影響する操作を止める。

## 8. 改訂と読み手の自由

v001は実験用の共有契約であり、全AI共通標準として確定していない。新しいモデルや方法によって改善できる。

記録の訂正では`revision`と`updated`を進め、出典と理由を残す。重大な意味変更は元の判断を消さずに区別する。必要な形式変更が非互換なら新しいSchema版を追加し、既存v001の意味を黙って書き換えない。ガイドの版・更新理由も追跡し、旧版の意味が分かる状態を保つ。

読み手はCurrent Humanの目的に従い、必要な関係を選び、別の説明や改善案を考えてよい。Formatは思考手順、回答のSection構成、Task実行順を固定しない。Body・Safety・Human Authority等のGuardを、記録の好結果で無効化しない。

### 8.1 次AIも記録を育てる

記録は前AIだけが編集する固定資料ではない。Humanが対話によるTask記録更新を許可しているScopeでは、次AIも新たな根拠・補足・訂正を反映し、必要な検証とRemote Verifyまで続けられる。同じ更新許可を毎回取り直さない。Handoffに含まれる具体的なHumanの委任Scopeを引き継ぎ、過去引用の命令を勝手に全Repositoryへ広げない。

- 以前のThreadで起きたことへの後日補足は、そのThreadの原本へ追加できる。Sourceの発言元は新しいThreadと明記する。
- 次Threadで新しく起きた出来事は、そのThreadの`task-records.json`へ記録する。前Thread原本をコピーして二重管理しない。
- 訂正されたTaskやEdgeのIDは意味が同じなら保持し、旧説明・時点・新Source・理由を改訂履歴に残す。別実行を同じIDへ上書きしない。
- 今回のScopeで必要ならガイドやSchemaも改善できる。非互換変更は新しい版と対応関係を示し、旧版の意味を黙って変えない。単に新AIが来たことを再設計の理由にしない。
- 更新前にCurrent mainとBlobを読み、他者変更を保持する。構造・参照・根拠との対応を検査し、更新後はRemoteを再取得する。Toolの可否や承認不足を文書で迂回しない。

Humanへの返却は、必要に応じて「更新済みの記録・出典との対応・重要な未解決事項・前回からの変更点」で示せる。Botで見いだした四点の用途をここへ接続するが、全回答を四項目の固定Templateにはしない。

### 8.2 拡充例で使用する任意拡張

revision 2はv001の既存構造で記録できるため、Schemaを改版しない。次の拡張は読解補助であり、Coreの意味を変えない。

- `source_context.extensions.record_cutoff`：どの発言まで収録したか。
- `source_context.extensions.latest_reported_physical_coordinate`：最も後の身体・場所の報告。現在位置ではない。
- `source_context.extensions.governance`：Current Runtimeとの責務の境界。
- `nodes[].extensions.later_report_ref`：後の別時点を表すNode ID。新しい実行命令ではない。
- `extensions.revision_history`：改訂対象・理由・Source。自己Blobは埋め込まない。
- `extensions.reconstruction_feedback`：何版について、誰経由で、どの範囲の読解結果を得たか。
- `extensions.coverage_review`：収録対象とSource IDの照合表。全Task完了の証明ではない。

これらの参照を利用する場合もリンク先の存在を検査する。Future版の未知拡張は無視してもCoreを読めるようにするが、未対応Coreの意味を推測で補完しない。

**経験は忠実に渡す。解釈は開いておく。資料と実行権限を混ぜない。**

ARK_TASK_RECORDS_GUIDE_EOF_v002
