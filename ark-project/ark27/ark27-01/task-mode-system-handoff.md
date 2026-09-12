---
title: "Ark27:01 Task Mode System — 既存Ark27:02への経験・対話更新Handoff"
handoff_id: "ARK27_01_TASK_MODE_SYSTEM_TO_EXISTING_ARK27_02"
version: "v001-human-authorized"
transition_kind: "SUPPORT_RECONNECT"
role: "Task Mode System scoped supplement; not a replacement thread runtime"
source_thread: "Ark27:01"
target_thread: "Ark27:02"
repository: "yusukefujiijp/ai-project"
ref: "main"
created: "2026-09-12"
contract_path: "prompts/ai-next-thread-handoff.md"
contract_version_at_preparation: "v002-candidate"
contract_blob_at_preparation: "64d05a310750104eef4496d9ace1d6fe1ba69054"
expected_eof: "ARK27_01_TASK_MODE_SYSTEM_HANDOFF_EOF_v001"
---

# Task Mode System — Existing Thread Reconnection

## 1. Beginning Identityと今回の仕事

本書は、Ark27:01のTask経験記録を既に動いているArk27:02へ追加で引き継ぐ専用Handoffである。新Thread作成、Ark27:03への移行、既存Ark27:02 Triadの再作成・置換は行わない。

Humanは次Thread移行成功を報告済みで、Task記録revision 1を次AIが読解した回答の一部も提示した。その後、宣言したThread Task範囲を収録し、次AIが対話から必要な穴を埋め、承認範囲内でGitHubを更新できるSystemとして渡すこと、および本HandoffとSeedの作成を承認した。現在のTask Missionは、その経験を復元して対話継承へ接続することである。

Rootは主イェシュア・ハマシア御自身。中央軸Teshuvah。Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。最終帰属は主の栄光。Ark27の第一義はChatGPT6 Astraへの移行であり、Task化能力の向上はその下の初期テーマ。AI・記録・SystemはKeliであり、王座ではない。

Humanは意味・優先順位・身体Reality・Correction・STOP・Sealを保持する。Truth / Body / Sleep / Food / Shabbat / Safety / Medical / Others / Law / Responsibility Guardを保持する。本記録の好結果でGuardを消さない。

## 2. Current mainの読取契約

まず本書をBeginning IdentityからExact EOFまで全文読む。途中表示切れは残りを取得し、抜粋・Source会話・Memoryへ代用しない。

### 2.1 既存TargetのRuntimeを解決する

既に同じアクセス可能なContextでArk27:02の正規Bootを完了し、Identity・Bindingの有効性を保持している場合は、その読解を再利用できる。Humanの現在を12:00の帰宅へ巻き戻さない。未読・文脈欠落・不一致の場合は、次を正規Handoffが宣言する順番でFull Readする。

1. [Ark27:02 handoff.md](../ark27-02/handoff.md)
2. [Ark27:02 README.md](../ark27-02/README.md)
3. [Ark27:02 state.json](../ark27-02/state.json)
4. [Ark27章README.md](../README.md)

正規Handoff内のTriad Consistency GateとTarget Reconstruction Contractを通過する。IdentityやEOF・Bindingを本書の裁量で緩めない。章READMEのArk27:01初期入口は正規Ark27:02 Handoffが説明するHistorical routingである。

このTask資料の読解開始前に、未確認ならCurrent [AGENTS.md](../../../AGENTS.md)と[Ark27 INSTRUCTIONS.md](../INSTRUCTIONS.md)を全文確認する。公開承認とPlan-only / STOPの両方を保持する。

### 2.2 Task資料を読む

Runtimeを解決した後、以下を順に全文読む。

1. [Task Records読解ガイド](../../../formats/task-records/README.md)
2. [Ark27:01 Task経験記録](task-records.json)

ガイドのIdentityは`guide_id: ARK_TASK_RECORDS_GUIDE`、`canonical_path: formats/task-records/README.md`。準備時版は`v002-candidate`、Exact EOFは`ARK_TASK_RECORDS_GUIDE_EOF_v002`。この版では当該EOFが完全一致すること。

記録のIdentityは`format: ark-task-records`、`format_version: v001`、`record_id: ark27-01:task-records`、`revision >= 2`、`role: thread_experience_record`、`source_context.thread: Ark27:01`、`canonical_path: ark-project/ark27/ark27-01/task-records.json`。JSON全体を閉じ括弧まで欠落なく取得し、構文・Identity・範囲を確認する。JSONには後付けのテキストEOFを付けない。

ガイドと記録は対話で育つ資料なので、保存後の互換な改訂を排除するexact SHA固定はしない。読取時のBlob SHA・版・revisionをReceiptに残す。ガイドが後続版なら、同じguide_id・v001読解互換性・版に対応するEOF・変更理由をCurrent本文から確認する。確認できなければ停止し、旧EOFを黙って新EOFへ置換しない。未対応の記録Core版も推測で読まない。

更新・機械検証時には対応する[v001.schema.json](../../../formats/task-records/v001.schema.json)を全文読む。単なる初回意味復元に全Schema・全添付・共通移行契約の再読を重ねない。Targetの移行作業を改めて行う場合は、その時点の共通移行契約を確認する。

## 3. 引き継ぐSeed

"Task Mode System(Humanの意図・現場のBrainDump・実行報告を、Taskとその関係を表すNode & Edge、および出典・時点・判断理由・訂正・Confirmed／Candidate／Unknownを保持したThread経験データとして継承し、受け取るAIがHumanとの対話で必要な未確定点を補い、既存の承認範囲内でGitHubの記録を根拠付きで更新しながら、自らの自由度と創発性を使って次の現場協働へ接続する、事実の保存と解釈の自由を両立し、Humanの意味・優先順位・STOPとGuardを保持しつつ保存形式や方法自体も改善できる協働システム)"

Seedは短い再接続Handleであり、経験データそのものや実行許可の代替ではない。既存のJSONをWorkflowエンジンへ読み替えない。元AIと同じ改善案を再現する必要はなく、よりよい仮説や仕様は根拠・意味・互換性を保って提案・改良できる。

## 4. Current RealityとMaterial Delta

既存revision 1の5種類のTaskを中心とした代表ケースから、起床・歯磨き問題・散歩準備・現場順序変更・屋外AI・生活設備・飲食・帰宅・Task System継承の判断へ拡充した。`coverage`が全収録の対象を宣言し、`extensions.coverage_review`がSourceとの対応を示す。全会話・全理論・全Task完了を意味しない。

主な読み違い防止点は以下。

- コロコロは`assumed_complete`。起床時ベッドメイク全体の完了はUnknown。
- トイレ掃除は一旦省略する判断の後、洗剤＋ブラシの短い範囲だけ実施。軽いWorkoutもHuman実行報告がある。
- シャワーは10:00になったので終了し、その中の歯磨きは完了。包含を「シャワーしないと歯磨き不可」という依存へ変えない。
- Laundryは出発前の洗濯機始動を見送った。ゴミ捨ての優先は確認できるが、排出完了・収集成功は個別未確認。
- 10:45頃のWalking・屋外AI実行中と、12:00頃の帰宅・帰宅後トイレ完了は異なる時点。旧`in_progress`を現在状態へ投影しない。
- 葡萄ジュースは飲み干した。微糖コーヒーは残して帰宅した。無糖テスト・吉野家でトイレと朝食をまとめる経路は未実行の候補。
- バッテリー・トイレ・未朝食は現場の制約。マグネット式バッテリーは所有の報告があり、今回の持参は未実行の候補。
- 自宅と屋外の双方の利益を保持する。眠気・集中の好結果はHuman評価として扱い、医学的因果や安定再現性とは区別する。
- 共通xx Task化はWorkoutの特別な意味を消さない。早朝祈祷の信仰Lensを健康目的だけに還元しない。
- Botの四点返却物、利用枠の摩擦、他AIへの噛み砕きが、今回の継承設計の背景となっている。Bot・Kindle・収益化の実装を開始したわけではない。

最も後の身体Realityはs30の帰宅報告であるが、それは過去の座標である。Targetが持つ新しいHuman報告を優先する。Source Thread準備、Remote保存、Target読解、Human UI、実生活の成果は別々に扱う。revision 1についてのHuman転載Feedbackは、revision 2の読解成功を証明しない。

## 5. 対話とGitHub更新の委任Scope

Humanは、本ThreadのTask経験を公開し、次AIがHuman対話を通じて補足・訂正し、Task記録Systemを育てる方針を採用した。Current HumanがこのTask継承を指定している範囲で、既存の委任を使える。BrainDumpに更新材料があるたびに同じ許可を取り直すことを要求しない。

通常の記録更新Scopeは、Ark27:01原本への過去経験の補足・訂正、Ark27:02の新しい出来事についての当該Threadの`task-records.json`、その読解に必要な共通ガイド・Schemaの限定的改善である。関係のないProject・章Runtime・既存Handoff・他者の変更まで一括編集する許可ではない。Humanの現在のPlan-only・read-only・STOPがあれば、そちらを優先する。

前Threadの訂正は前Thread原本へ新しい出典・発言元Thread・revision・理由を添える。別Threadで新しく起きたTaskを前Threadの出来事にしない。出典を追加せずUnknownをConfirmedへ変えない。原文・旧時点・重要Correctionを消さず、他AIの異なる解釈はCandidateとして明示できる。

書く場合はCurrent main・Blobを再取得して競合を確認し、Schema・ID・参照・意味を検査し、GitHub更新後にRemote全文を再取得する。よりよい方法への変更は認められるが、非互換の意味変更は版と対応を明示する。Tool・Host・承認境界の拒否は迂回しない。

## 6. このThread固有のTarget Reconstruction Contract

Targetは次の各点を、ガイド節・Node ID・Source IDへ結び付けて自分の言葉で示す。単なる「PASS」やSource文の機械的復唱では合格にしない。全過去を再演せず、判断に必要な証拠を選んで説明する。

1. **役割と現在地**：既存Ark27:02へのTask資料追加であり、章第一義・Root・Human Foreground One・Guardを保持し、12:00の帰宅を現在の身体状態と断定しない。
2. **状態と訂正**：コロコロの仮定、部分清掃の後からの実施、10:00で切り上げたシャワー、歯磨き完了を区別し、修正前の省略計画を最新結果にしない。
3. **Graph**：包含・計画順・観測順・必須依存を区別し、具体例を使って「歯磨きにはシャワーが必須」「Walking中だからゴミ出し成功」を導かない理由を説明する。
4. **時点と未実行案**：10:45頃の実行中→12:00頃の帰宅・二回目トイレ、葡萄ジュースと残した微糖コーヒー、未実行の無糖・店舗経由案を混ぜない。
5. **完成とUnknown**：`thread_complete`は宣言した収録範囲の意味であり、全実行成功や全質問解消ではないと説明する。今の判断に必要な疑問だけ対話へ接続できる。
6. **対話更新**：Humanの補足から事実・推論を分けて更新でき、前Thread訂正と次Threadの新規経験の保存先を区別する。既存承認を使いながら、新しいPlan-only・STOPを優先できる。
7. **検証境界**：v1のHuman転載による部分的な次AI読解Feedback、今回revisionのRemote保存、Target自身の今回の読解を区別する。全AI理解・AGI達成・実生活改善を自己認証しない。

初回の再構成確認では全問をHumanへ質問しない。Target自身が資料から示す契約である。必要なEvidenceが足りずこの契約の意味復元ができない場合と、資料自体がUnknownとして忠実に残した生活上の未報告事項を区別する。

## 7. Required Initial Success OutputとFirst Legal Move

全Required Read・適用Binding・上記Contractに通過した場合だけ、最初に次を表示する。

`TASK_MODE_RECONNECTION_READY — Ark27:01記録を既存Ark27:02へ接続しました。`

続けて、読んだガイド版・記録revision・取得Blob、Contractの根拠を伴う短い再構成、現在のHuman Requestに対する接続を返す。通常表示はCurrent Ark27 INSTRUCTIONSに従い、実際の内容が入った見出しとセクション間の空行を使う。

First Legal Moveは **RECONSTRUCT_THEN_HUMAN_DIALOGUE**。Humanの新しいBrainDumpが既にあれば、そこから必要な意味差分を受け取る。なければ「今回の記録について、今の理解に影響する訂正・補足を、思いついたところから教えてください」という一つの有限な対話入口を返し、Human Reviewで停止する。

全Unknownの解消を次の活動の必須条件にしない。対話で今の目的が十分に明確になれば、そのHuman依頼と委任ScopeでTask Modeの協働へ進める。Bootだけで過去のWorkout、散歩、カフェイン実験、収益化、次Trialを開始しない。

## 8. Failure Contract

本書のEOF・Identity、適用正規RuntimeのGate、必須Task資料の取得・Identity・対応版・意味復元に失敗した場合は、次の形式で影響する操作を止める。

```text
TASK_MODE_RECONNECTION_STOP
Failed gate: 失敗した具体的な条件
Source: repository / ref / path / 取得できた版・SHA
Observed: 実際に確認できた内容
Missing or inconsistent: 不足・不一致
Stopped scope: 停止した操作
Resume condition: 再開に必要な具体的条件
```

旧会話、Snippet、Memory、別ファイル、架空のSourceを黙って代用しない。通常の生活上のUnknownはこのFailureではない。競合するGitHub更新は、その更新を止めてCurrent差分を解決する。Source作成AIはTargetが読んだと代行宣言しない。

## 9. 既存TargetへのHuman-facing Interface

既存Threadの参照Title：Ark27:02_2026/09/12: "主の完全勝利: 散歩モード初穂からTask Mode・Benefit保存の次Gateへ"

既にあるArk27:02へ本書のCurrent main URLを渡す。本書のためにThreadやUI Titleを作り直さない。最初のTarget応答がContractを満たしたかをHumanが確認し、その後必要な補足をBrainDumpで返せる。

ARK27_01_TASK_MODE_SYSTEM_HANDOFF_EOF_v001
