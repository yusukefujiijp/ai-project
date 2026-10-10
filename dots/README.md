---
title: "Dots — Human-AI協働をつなぎ、育てる"
canonical_path: "dots/README.md"
version: "v007"
status: "human-authorized initial foundation / evolving direction"
created: "2026-10-01"
updated: "2026-10-10"
role: "Current Dots direction and routes to shared lessons, actor logs, bounded Ark Map operation and preserved history"
updated_reason: "Link the Human-named dot-0001 Inbox preparation draft; preserve existing direction, operation and permission boundaries"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::DOTS_HOME::v007"
---

# Dots — Human-AI協働をつなぎ、育てる

## 1. 現在の方向 — 出来上がった移行ではなく、育てる協働

YusukeJPとDotsの協働を、ChatGPT Workでの作業や将来のAIへ、意味・経験・判断の根拠ごと接続して育てる。この場所は、その**現在の全体方向**と、誰がどの経験を形成したかへ戻る入口を所有する。

Humanの現在のVisionは、Dotsを主な協働の場へ徐々に育て、Workを強力なSubとして活かしながら、双方を丁寧に使い分けて両立させること。これは現在の方向と作業仮説であり、完成済みの移行や永久的な上下関係ではない。実際の得意分野・成果・Humanの手応えから、役割の配分を育てる。

この方向に向けて、Dotsとの対話・問題解決とWorkでの作業を接続し、Humanが毎回すべてを説明し直したりAI間の伝言係になったりしなくても、必要な背景と成果へ辿れるようにすること。これは完成した全体移行、常時同期、全Dotsの自動連携、Work側の受入れ成功の宣言ではない。実際に使える能力・接続・現在の権限を確かめながら、具体的な協働から育てる。

Humanは、急いで体系を一気に確定するより、意図を一つずつ丁寧に合わせ、誰が・いつ・どこを・何のために変え、何が起きたかを他AI・Future AIが理解できることを重視した。対象と実行が承認された後は、必要な作成・修正・検証まで進める。「丁寧な合意形成」を同じ承認の取り直しや、実行できる仕事を提案だけで返す理由にしない。

現在は、dotsをHuman-AI協働を育てる軸、control-centerをRepository全体の構造改善を育てる軸として接続する。この二軸の間や既存Workとの報告・質問・返信には[Board](../board/README.md)を使い、まず実際の一件を試してFeedbackから柔軟に修正する。Boardは通信の所有先であり、第三のMission Authorityではない。v002での接続変更の理由と証拠は[STR-006](../control-center/changes/STR-006-board-communication-foundation.md)が所有する。

現在の全体方向を更新する場所はこのREADME。個別Actorの身元・持ち味、時点を区切った経験、実装変更の記録は別の所有資料へ委ね、同じCurrent方針を複数箇所で更新しない。

## 2. 入口と所有先

| 知りたいこと | 読む場所 | 役割 |
|---|---|---|
| 協働相手へ何を伝え、どんな返答があったか | [Board](../board/README.md) | 宛先・通知版・実際の受信と返答。初回はMain27:07／Support28:02への紹介・変更報告 |
| 初穂の定期Ark Mapと限定saveをどう運用するか | [Ark Map運用原本](ark-map/README.md) | dot-0000固有の表示・読取・保存境界。製品側の予定・実行状態とは分ける |
| Dotsが仕事から何を学び、次にどう使うか | [lessons](lessons/README.md)／[lessons.jsonl](lessons/lessons.jsonl) | 条件・根拠付きの学びと、その読取・更新契約 |
| 最初の協働相手は誰か | [dot-0000 — Dot00:00; 初穂](actors/dot-0000/README.md) | 安定したActor識別子、表示名、命名の意味、現在の持ち味 |
| 将来のInbox Dotをどう準備するか | [dot-0001: Inbox — 準備原本](actors/dot-0001/README.md) | ID・名前はHuman採用済み。製品上の個体は未作成。成立理由・役割・接続条件を育てる設計Draft |
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

## 5. Dotsの学びを、次の判断へ戻す

Dots全体へ適用する共通知識は[lessons](lessons/README.md)で育て、現行の共通lessonの正本は[lessons.jsonl](lessons/lessons.jsonl)一つに置く。新しいDotsは専用READMEと現在の小さい蓄積の全件を読み、条件・根拠・限界を次の判断へ戻す。確認済みの文脈を再利用し、毎ターンの再読は課さない。専門領域だけに適用されるlessonは、その領域を扱う時に該当入口から読む。著者別の分割や共通lessonの複製はせず、適用範囲と一つの担当原本を守る。

読取・更新・schema 2・UUID・競合・再試行・互換性の契約は[専用README](lessons/README.md)だけが所有する。初期形成は[STR-007](../control-center/changes/STR-007-dots-lessons-foundation.md)、管理行なしJSONL採用と移設は[STR-009](../control-center/changes/STR-009-headerless-lessons-adoption.md)へ進む。Actor別ログや凍結実験を共通lessonの第二正本にしない。専門lessonも同じ契約を参照し、全Dotsへ一般化すると誤適用される学びが実際に生じた時だけ、その領域の原本へ置く。

EOF::DOTS_HOME::v007
