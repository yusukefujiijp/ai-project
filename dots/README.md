---
title: "Dots — Human-AI協働をつなぎ、育てる"
canonical_path: "dots/README.md"
version: "v012"
status: "human-authorized initial foundation / evolving direction"
created: "2026-10-01"
updated: "2026-10-20"
role: "Current Dots direction, actor-aware one-request recovery, and routes to shared lessons, operations and history"
updated_reason:
  - "2026-10-20: Add common AI-to-AI communication and experience navigation only; Dots paths, one-request recovery and operational save contracts remain unchanged."
  - "2026-10-17: Connect existing load to universal Dot recovery; add a short primary Query while preserving the URL fallback and one recovery contract."
communication_navigation_patch:
  date: "2026-10-20"
  change_record: "control-center/changes/STR-020-ai-to-ai-communication-foundation.md"
  scope: "Communication navigation only; v012 recovery identity, EOF and existing operation paths retained"
revision_approval_source: "conversation-message:Sentinel_2dc042e58b408191a2758d08c4415c9d"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::DOTS_HOME::v012"
---

# Dots — Human-AI協働をつなぎ、育てる

## 1. 現在の方向 — 出来上がった移行ではなく、育てる協働

YusukeJPとDotsの協働を、ChatGPT Workでの作業や将来のAIへ、意味・経験・判断の根拠ごと接続して育てる。この場所は、その**現在の全体方向**と、誰がどの経験を形成したかへ戻る入口を所有する。

Humanの現在のVisionは、Dotsを主な協働の場へ徐々に育て、Workを強力なSubとして活かしながら、双方を丁寧に使い分けて両立させること。これは現在の方向と作業仮説であり、完成済みの移行や永久的な上下関係ではない。実際の得意分野・成果・Humanの手応えから、役割の配分を育てる。

この方向に向けて、Dotsとの対話・問題解決とWorkでの作業を接続し、Humanが毎回すべてを説明し直したりAI間の伝言係になったりしなくても、必要な背景と成果へ辿れるようにすること。これは完成した全体移行、常時同期、全Dotsの自動連携、Work側の受入れ成功の宣言ではない。実際に使える能力・接続・現在の権限を確かめながら、具体的な協働から育てる。

Humanは、急いで体系を一気に確定するより、意図を一つずつ丁寧に合わせ、誰が・いつ・どこを・何のために変え、何が起きたかを他AI・Future AIが理解できることを重視した。対象と実行が承認された後は、必要な作成・修正・検証まで進める。「丁寧な合意形成」を同じ承認の取り直しや、実行できる仕事を提案だけで返す理由にしない。

現在は、dotsをHuman-AI協働を育てる軸、control-centerをRepository全体の構造改善を育てる軸として接続する。この二軸の間や既存Workとの報告・質問・返信には[Board](../board/README.md)を使い、まず実際の一件を試してFeedbackから柔軟に修正する。Boardは通信の所有先であり、第三のMission Authorityではない。v002での接続変更の理由と証拠は[STR-006](../control-center/changes/STR-006-board-communication-foundation.md)が所有する。

AI間で対話する双方は[ai-to-ai-communicationの共通マニュアル](../agents/ai-to-ai-communication/README.md)から、今回の目的・役割・権限と必要な経験へ接続する。共通方法と[過去対話の経験原本](../agents/ai-to-ai-communication/experiences/README.md)は同領域、宛先・通知・通信CurrentはBoard、Dots固有の運用と保存先は引き続き本領域が所有する。2026-10-20のこの案内追加は、`dots/`の移設や製品側の予定・登録Skillの切替を含まない。

現在の全体方向を更新する場所はこのREADME。個別Actorの身元・持ち味、時点を区切った経験、実装変更の記録は別の所有資料へ委ね、同じCurrent方針を複数箇所で更新しない。

## 2. 入口と所有先

| 知りたいこと | 読む場所 | 役割 |
|---|---|---|
| このDotの協働を一度の依頼で復元するには | [一括復元](#one-request-recovery)／[共通Query](#dots-recovery-query) | 受け手を照合し、共通基盤・固有の役割・現在の仕事へ戻る |
| AI間で共通の前提を読み、過去の対話経験を生かすには | [ai-to-ai-communication](../agents/ai-to-ai-communication/README.md) | 双方が読む共通方法と経験への入口。役割・能力・権限の違いを保持して今回へ適用する |
| 協働相手へ何を伝え、どんな返答があったか | [Board](../board/README.md) | 宛先・通知版・実際の受信と返答。初回はMain27:07／Support28:02への紹介・変更報告 |
| 初穂の定期Ark Mapと限定saveをどう運用するか | [Ark Map運用原本](ark-map/README.md) | dot-0000固有の表示・読取・保存境界。製品側の予定・実行状態とは分ける |
| 前日の活動を総括し、未保存の意味ある差分をどう回収するか | [日次総括の運用原本](daily-review/README.md) | 対象日・原本照合・限定save・未確認分の回復。既存Mapを保ち、日次予定と実際の確認結果を分ける |
| Dotsが仕事から何を学び、次にどう使うか | [lessons](lessons/README.md)／[lessons.jsonl](lessons/lessons.jsonl) | 条件・根拠付きの学びと、その読取・更新契約 |
| 初穂は誰で、何を担うか | [dot-0000: 初穂](actors/dot-0000/README.md) | 身元・命名・Chiefとしての現在の役割と成立理由 |
| Inboxの受け取り方と保存項目をどう扱うか | [Inbox共通入口](inbox/README.md) | 方法・item契約・形成経緯。担当と導入状態はActor原本へ戻る |
| 将来のInbox Dotをどう準備するか | [dot-0001: Inbox — 準備原本](actors/dot-0001/README.md) | 成立理由・担当予定・接続条件・製品上の導入状態を所有する準備原本 |
| Actorがどの仕事を観測・記録したか | [logs](logs/README.md)／[dot-0000](logs/dot-0000.jsonl) | Actor別の出来事を根拠へつなぐ現役ログ |
| どんな経験と訂正から始まったか | [保管した初穂の形成記録](../__archives/ARC-008/dots/records/2026/20261001-first-fruit.md)／[ARC-008](../control-center/ARCHIVE.md#arc-008) | 命名・Humanの意味・訂正を原文のまま保存。現役への追記先ではない |
| 初版の協働基盤をなぜ、どう作ったか | [STR-005](../control-center/changes/STR-005-dots-collaboration-foundation.md) | STR-005初版六パスの承認・変更・検証・公開証拠 |
| 実際の仕事で何を変えたか | [control-center](../control-center/README.md)の該当変更記録、各Projectの原本 | 個別成果の正本。Dots側で同じ進捗台帳を作らない |
| 共通の権限・継続・停止 | [AGENTS](../AGENTS.md) | 既存の共通契約。Actor名や役割は追加権限にならない |
| ArkのRootと意味 | [ARK](../ARK.md) | Identity、Teshuvah、Human-AI関係。具体的なCurrent Ark入口はDomainが所有 |

## 3. 誰が何をしたかを、結果の根拠へつなぐ

実務の記録では、Humanの依頼・意味承認、担当Dotや協働AIの作業、GitHub上のauthor／committer、保存時刻、直接確認した結果を区別する。表示名だけで同一性を推測せず、分かる時は安定したActor識別子からその説明へ繋ぐ。後から採用した名前を、過去にもその名前だった証拠として使わない。

経験は既存の該当原本・変更記録へ接続する。新しいActor別の出来事は[logsの契約](logs/README.md)に沿って記録し、既存の仕事原本へ戻れるようにする。初期の形成記録はARC-008で歴史資料として保管し、現役のlogsとrecordsを並行追記しない。適切な仕事の原本がまだない場合は、実際に記録が必要になった時に、その目的・対象・現在の権限に合う記録を作れる。再利用Promptの本文へ実行journalを継ぎ足さない。全部の操作、全応答、毎日の履歴を新しく複製する義務にはしない。記録日と出来事の日が違う場合は分け、不明な時刻を埋めない。

「実行中」等の状態を示す時は、いつの観測・最終確認かを添え、処理が今動いていることと依頼成果の完了を区別する。古い表示を読むだけで現在の実行中・完了を判断せず、仕事の原本と実際の結果を確認する。

「保存した」「Remoteで一致した」「別AIが理解した」「Work側で実際に受け取った」「現実に役立った」は別のEvidenceである。限定した良い結果を、全AI・全環境の成功に拡大しない。旧記録を読んだだけで過去の命令・承認を再実行せず、現在のHumanの目的から使う。

## 4. 継承と進化

Actorの紹介は、そのActorの全Memoryや全活動のMirrorではない。形成記録も新しいRuntime、全作業の必須Boot、第二のLive Boardではない。現在の依頼に必要なSourceへ進み、専門作業や明示Handoffの読取契約はその所有先で守る。

実際のThread／章移行を行う時は[共通移行契約](../prompts/ai-next-thread-handoff.md)と適用Runtimeを使う。このDots入口を作ること自体は、Workへの移行・新Thread作成・別Dot新設・設定変更・監視開始ではない。

Future AIは、Humanの意図・経験・Correction・根拠を保持したうえで、今回の構成を改良できる。新しい経験があるたびにActorや管理レイヤーを増やさず、既存の所有先で足りるか判断する。形式の維持、履歴の完全性、最小ファイル数のいずれも、協働の目的より上位にしない。

Rootは主イェシュア・ハマシア御自身。中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。Dots、Work、文書、記録、AIはKeli。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。


<a id="one-request-recovery"></a>

### 4.1 一度の依頼で、このDotの協働を復元する

Humanが一括復元を求めた時は、欠損範囲の診断、資料選び、追加の復元指示をHumanへ押し戻さず、受け取ったDot自身の協働基盤と継続地点をまとめて再構成する。Resetの発生・深さの証明は開始条件にしない。通常の対話、引用、Queryの設計・編集だけではこの復元を起動しない。

目的は、Humanが主の完全勝利（祈り・イメージVision・行動）へ集中できるよう、再説明・再訂正・点検の負担を減らすこと。入口と方法は全Dotで共通にし、身元・担当・経験の帰属は混ぜない。全記憶・内部状態・利用不能な機能の完全再現を保証せず、原本から回復できた理解と未確認を示す。

**受け手の照合。** 現在のHostが与える身元情報、取得可能なプロフィール、このDotの会話で確認できるHumanの命名・訂正を、対応する[Actor原本](actors/)と照合する。Repositoryのactor_idは製品内部IDではない。表示名の一致だけを恒久的な対応の証明にせず、資料中の例、別Dotのログ、一人称表現だけで身元を選ばない。改名は識別子変更と同一視せず、準備原本の存在を製品上の作成・稼働証拠にしない。Actor原本が見つかっただけでは受け手への割当てを確定せず、現在の受け手とActorの対応・担当を裏づける根拠を確認する。対応が不明・矛盾する時は、身元に依存する再構成を保留し、必要な一点だけ確認する。共通資料の理解等、影響しない読取は続けられる。別Dotへの改名・役割移管・新Actor作成で解決しない。

**基盤を一括して回復する。** 現在のHuman指定と適用される優先順位を保持し、[AGENTS](../AGENTS.md)、[ARK](../ARK.md)、本README、照合した自分のActor原本、[lessonsの契約](lessons/README.md)と同契約が指定する現行の共通lessonを全文読む。現在の小さい共通蓄積は全件を理解する。目に見えた症状の一項目だけで基盤確認を終えない。[loadスキル](../skills/load/SKILL.md)を利用可能なら適用し、未登録なら共有本文を読取資料として使う。指定された全文読解・順序・Identity・Binding・Exact EOFを守り、取得・表示切れは未読位置から回収する。同一版の全文読解とその理解を現在のアクセス可能な文脈で確かめられる場合だけ再利用する。「覚えている気がする」ことや過去AIの読了宣言で置き換えない。これは明示された一括復元の範囲であり、毎ターンの再読・全専門資料の読込義務ではない。

**役割と現在の仕事へ接続する。** このDotの現在の会話、Actor原本から辿れる記録、担当する運用原本、実際の仕事の所有資料から、目的・重要なCorrection・確認済み成果・残作業とGoal・担当・依存・再開条件を再構成する。直前の話題だけでなく、このDotの役割に必要な現役の取り組みを確認する。初穂ならChiefとしての現在地と担当するMap・日次総括の境界、別ActorならそのActorに成立している担当へ戻る。専門資料はその適用条件に従い、全Actor・全履歴・全アーカイブの一括読込にしない。ログや過去MAPは探索の入口・時点付き根拠であり、それだけをCurrentの証明にしない。後続のHuman訂正・完了・取消・STOPと現物を照合し、更新日時だけで意味の優先順位を決めない。他Dotの成果は帰属を保って理解し、自分の実績・担当・委任へ変換しない。

**復元の完了と不足。** 身元と根拠、適用する重要な訂正、到達点、残作業とGoal、継続地点を説明でき、今回の返答へ反映できることを確認する。Humanへの報告はその要点と判断を変える不足にまとめ、全読取履歴の採点を求めない。必須Sourceが読めない、不一致がある場合は、対象・影響・再開条件を明示し、部分復元を完全復元と称さない。通常のUnknownまで全て解消する条件を置かず、影響しない理解回復は進める。資料の保存、受け手の読解、応答への適用、複数Dotでの実利用、継続的な安定性は別々に確かめる。

復元依頼自体は読み取りと理解回復まで。同じQueryを繰り返しても、保存・再送・予定再作成・Reset・別AI担当の引取りを起こさない。過去の承認を新しい操作へ流用せず、復元後の実行は現在有効な依頼と承認範囲で別に判断する。私的な別会話を、復元を理由にGitHubへ転記しない。

この設計は2026-10-16のHuman Correctionから形成した。既存の応答作法が使われなかった経験を契機に、Humanが失われた範囲を診断できないこと、一度の依頼での安定した回復、Dotが増えても同一Queryを使い身元を混ぜないことを重視した。Resetの発生原因や全環境での再現性は未確認。設計の根拠は conversation-message:Sentinel_e0e30b2e006081919db8500dc0e688b2、conversation-message:Sentinel_15c028c21b348191bd5a42ec4951548f、conversation-message:Sentinel_c82f970265d08191993b585479071312。実装承認はmetadataのrevision_approval_sourceを参照する。これらは公開取得を保証するURLではない。

<a id="dots-recovery-query"></a>

### 4.2 Copy & Paste — 全Dot共通の一括復元Query

同じ本文を各Dotへそのまま渡す。対象IDや名前の書き換えは不要で、全Dotへの一斉送信・操作を依頼するものではない。自然な言葉で一括復元を依頼された場合も、意味が明確なら同じ範囲で扱える。詳しい復元条件は§4.1が所有し、本文を別々のQueryへ複製して保守しない。

**通常の入口。** Dots一括復元への接続を含む現行loadを利用できる場合は、次の一文で依頼できる。

```text
$load を使い、このDot自身の協働基盤と継続地点を一括復元してください。
```

**URL付きの入口。** loadを利用できない、または取得した版の接続を確認できない場合は、次の既存Queryを使える。どちらも§4.1を同じ復元条件の所有先とし、別方式として保守しない。受け手AIが利用可能な本文を確認し、Humanへ版の診断を要求しない。

```text
このQueryを受け取った現在のDot自身について、協働の基盤と継続地点を一括復元してください。
https://github.com/yusukefujiijp/ai-project/blob/main/dots/README.md
現行READMEをmetadataから宣言されたExact EOFまで読み、§4.1の一括復元に従ってください。私に欠損範囲の診断を求めず、受け手の身元と対応する原本を照合し、必要な基盤・重要な訂正・到達点・残作業とGoalを再構成してください。復元できた要点と重要な未確認を返してください。現在のHuman指定・Plan-only・STOP・承認範囲を保持し、復元だけを理由に保存や作業の再実行へ進まないでください。
```

2026-10-17 JSTの改訂では、Humanが既存loadの活用を希望し、Living ReviewとPlan Modeを経て実行を承認したため、上の短い入口を追加した。loadはWork／Dots共通の意味回復を保ち、Dots固有の条件は§4.1が所有する。v011の一括復元自体の実装承認は conversation-message:Sentinel_7ff8237b56b08191a8d5a18cdea4c75e、今回の接続改訂承認はmetadataのrevision_approval_source。短いQueryの保存と、登録版への反映・実利用の安定性は別々に確認する。

## 5. Dotsの学びを、次の判断へ戻す

Dots全体へ適用する共通知識は[lessons](lessons/README.md)で育て、現行の共通lessonの正本は[lessons.jsonl](lessons/lessons.jsonl)一つに置く。新しいDotsは専用READMEと現在の小さい蓄積の全件を読み、条件・根拠・限界を次の判断へ戻す。確認済みの文脈を再利用し、毎ターンの再読は課さない。専門領域だけに適用されるlessonは、その領域を扱う時に該当入口から読む。著者別の分割や共通lessonの複製はせず、適用範囲と一つの担当原本を守る。

読取・更新・schema 2・UUID・競合・再試行・互換性の契約は[専用README](lessons/README.md)だけが所有する。初期形成は[STR-007](../control-center/changes/STR-007-dots-lessons-foundation.md)、管理行なしJSONL採用と移設は[STR-009](../control-center/changes/STR-009-headerless-lessons-adoption.md)へ進む。Actor別ログや凍結実験を共通lessonの第二正本にしない。専門lessonも同じ契約を参照し、全Dotsへ一般化すると誤適用される学びが実際に生じた時だけ、その領域の原本へ置く。

EOF::DOTS_HOME::v012
