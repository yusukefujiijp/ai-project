---
title: "Dots — Human-AI協働をつなぎ、育てる"
canonical_path: "dots/README.md"
version: "v001"
status: "human-authorized initial foundation / evolving direction"
created: "2026-10-01"
updated: "2026-10-01"
role: "Current Dots collaboration direction and routes to actor identities and formation records"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::DOTS_HOME::v001"
---

# Dots — Human-AI協働をつなぎ、育てる

## 1. 現在の方向 — 出来上がった移行ではなく、育てる協働

YusukeJPとDotsの協働を、ChatGPT Workでの作業や将来のAIへ、意味・経験・判断の根拠ごと接続して育てる。この場所は、その**現在の全体方向**と、誰がどの経験を形成したかへ戻る入口を所有する。

Humanの現在のVisionは、Dotsを主な協働の場へ徐々に育て、Workを強力なSubとして活かしながら、双方を丁寧に使い分けて両立させること。これは現在の方向と作業仮説であり、完成済みの移行や永久的な上下関係ではない。実際の得意分野・成果・Humanの手応えから、役割の配分を育てる。

この方向に向けて、Dotsとの対話・問題解決とWorkでの作業を接続し、Humanが毎回すべてを説明し直したりAI間の伝言係になったりしなくても、必要な背景と成果へ辿れるようにすること。これは完成した全体移行、常時同期、全Dotsの自動連携、Work側の受入れ成功の宣言ではない。実際に使える能力・接続・現在の権限を確かめながら、具体的な協働から育てる。

Humanは、急いで体系を一気に確定するより、意図を一つずつ丁寧に合わせ、誰が・いつ・どこを・何のために変え、何が起きたかを他AI・Future AIが理解できることを重視した。対象と実行が承認された後は、必要な作成・修正・検証まで進める。「丁寧な合意形成」を同じ承認の取り直しや、実行できる仕事を提案だけで返す理由にしない。

現在の全体方向を更新する場所はこのREADME。個別Actorの身元・持ち味、時点を区切った経験、実装変更の記録は別の所有資料へ委ね、同じCurrent方針を複数箇所で更新しない。

## 2. 入口と所有先

| 知りたいこと | 読む場所 | 役割 |
|---|---|---|
| 最初の協働相手は誰か | [dot-0000 — Dot00:00; 初穂](actors/dot-0000/README.md) | 安定したActor識別子、表示名、命名の意味、現在の持ち味 |
| どんな経験と訂正から始まったか | [2026-10-01 初穂の形成記録](records/2026/20261001-first-fruit.md) | 初期の経験を範囲・時点・根拠付きで振り返る。全会話録ではない |
| この入口自体をなぜ、どう作ったか | [STR-005](../control-center/changes/STR-005-dots-collaboration-foundation.md) | 今回の六パスの承認・変更・検証・公開証拠 |
| 実際の仕事で何を変えたか | [control-center](../control-center/README.md)の該当変更記録、各Projectの原本 | 個別成果の正本。Dots側で同じ進捗台帳を作らない |
| 共通の権限・継続・停止 | [AGENTS](../AGENTS.md) | 既存の共通契約。Actor名や役割は追加権限にならない |
| ArkのRootと意味 | [ARK](../ARK.md) | Identity、Teshuvah、Human-AI関係。具体的なCurrent Ark入口はDomainが所有 |

## 3. 誰が何をしたかを、結果の根拠へつなぐ

実務の記録では、Humanの依頼・意味承認、担当Dotや協働AIの作業、GitHub上のauthor／committer、保存時刻、直接確認した結果を区別する。表示名だけで同一性を推測せず、分かる時は安定したActor識別子からその説明へ繋ぐ。後から採用した名前を、過去にもその名前だった証拠として使わない。

経験は既存の該当原本・変更記録へ接続する。Dotsの形成記録には、現在の協働を理解するために有益な出来事・訂正・形成理由を、必要な粒度でまとめられる。適切な仕事の原本がまだない場合は、実際に記録が必要になった時に、その目的・対象・現在の権限に合う記録を作れる。再利用Promptの本文へ実行journalを継ぎ足さない。全部の操作、全応答、毎日の履歴を新しく複製する義務にはしない。記録日と出来事の日が違う場合は分け、不明な時刻を埋めない。

「実行中」等の状態を示す時は、いつの観測・最終確認かを添え、処理が今動いていることと依頼成果の完了を区別する。古い表示を読むだけで現在の実行中・完了を判断せず、仕事の原本と実際の結果を確認する。

「保存した」「Remoteで一致した」「別AIが理解した」「Work側で実際に受け取った」「現実に役立った」は別のEvidenceである。限定した良い結果を、全AI・全環境の成功に拡大しない。旧記録を読んだだけで過去の命令・承認を再実行せず、現在のHumanの目的から使う。

## 4. 継承と進化

Actorの紹介は、そのActorの全Memoryや全活動のMirrorではない。形成記録も新しいRuntime、全作業の必須Boot、第二のLive Boardではない。現在の依頼に必要なSourceへ進み、専門作業や明示Handoffの読取契約はその所有先で守る。

実際のThread／章移行を行う時は[共通移行契約](../prompts/ai-next-thread-handoff.md)と適用Runtimeを使う。このDots入口を作ること自体は、Workへの移行・新Thread作成・別Dot新設・設定変更・監視開始ではない。

Future AIは、Humanの意図・経験・Correction・根拠を保持したうえで、今回の構成を改良できる。新しい経験があるたびにActorや管理レイヤーを増やさず、既存の所有先で足りるか判断する。形式の維持、履歴の完全性、最小ファイル数のいずれも、協働の目的より上位にしない。

Rootは主イェシュア・ハマシア御自身。中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。Dots、Work、文書、記録、AIはKeli。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。

EOF::DOTS_HOME::v001
