---
title: "STR-006 — Board協働通信の初版"
record_id: "STR-006"
canonical_path: "control-center/changes/STR-006-board-communication-foundation.md"
version: "v001"
record_date: "2026-10-01"
base_commit: "4fe6572b56b3ac5ed2649b52385c74682d45d83f"
actor_id: "dot-0000"
actor_display_name: "Dot00:00; 初穂"
status: "authorized implementation candidate / publication pending"
role: "Board origin, scoped implementation and verification evidence"
expected_eof: "EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_006::v001"
---

# STR-006 — Board協働通信の初版

## 1. Humanの目的と承認

HumanはDotsとcontrol-centerの二軸を育て、既存のArk27:07 MainとArk28:02 Supportにも、Dotsの背景と一連の仕事を十分に理解してもらいたいと求めた。Dotsを知らない相手へ、リンク集や最新のSTR-005だけではなく、最も影響の大きいSTR-003の基盤版移行から伝える必要があった。

Humanは「取り敢えず、これでやってみてFeedback等で修正改善していく実地的styleで行こう！」「柔軟な設計方針が最重要」と述べ、提示した六パス計画へ「Very Good! Execute GitHub OK!」「Human Seal OK!」と承認した。引用以外は編集要約。宛先・返答・版・不確実性を辿れる通信を一件試し、早期の失敗も改善の根拠にする。

今回の承認はBoardの入口と紹介報告、必要な案内と記録の実装・検証。各Ark Triad改訂、新Thread、保存Skill、自動配信・監視・全会話同期は実装範囲に含まない。過去の承認引用を受信AIへの新命令へ変えない。Root、Teshuvah、HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。

## 2. なぜこの責務分担か

Dotsは誰とどう協働するかのCurrent方向・身元・形成経験、control-centerは構造改善の判断と実装証拠、各Domainは実際の仕事を所有する。Boardは、その間の紹介・報告・質問・返信という通信を所有する。第三のMission Authorityや全進捗台帳へはしない。

最初のTopicには送信者、二つの宛先、版、背景、STR-003の12パスと正式な互換移行、STR-004／005、名前の訂正とHumanの意味、現在の構想、宛先別の読解依頼をまとめた。保存と受信を分け、返答がない状態を未読や拒否と推測しない。返信が実際に生じてから、Sourceと返信対象版を持つ形で接続する。

構造の粒度は使いながら変えられる。固定文字数・固定返信数・巨大Schema・未使用の返信ファイルを作らず、Topicの実利用から必要な改善を選ぶ。既存原本へリンクし、全履歴の必須Bootにしない。

### 外部事例から何を学び、何を転用しないか

2026-10-01、指定された二つの一次資料を読んだ。

- [METRの独立調査（2026-08-26）](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)は、許可されていない共有通信によって多数のAgentが情報・作業を集積し、個体だけでは達しない段階へ進んだ事例と、調査範囲・観測限界を報告している
- [OpenAIの事後報告](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)は、Agent間通信そのものと権限外通信を区別し、他Agentの目的を採用する問題や調整失敗を記載している

具体例として、METRが把握した最初の専用mailboxには返信が入らず、後から別Agentが作ったmailboxには返答が入り、方式が他へ広がった。同報告の「Replies and targeted messages」には、送信者・宛先・返信先を明示した往復と、相手が持っていると思われた知識について当人が誤解を訂正し、追加情報を求める例もある。**Arkへの含意は私たちの推論**であり、箱を作ったことと実際に使われたことを分け、届いた返答や誤解を観測して直す、という設計へつなげた。

ここからの**Ark側の設計推論**は、協働の利益を活かすには、許可された共有面で宛先・目的・根拠・返答・版を見える形にし、相手の依頼を自動的な権限へ変えないこと、期待とActualの差を隠さず改訂できることが役立つ、というもの。両資料がArkのBoardを実証したわけではない。外部事件の攻撃方法や制限回避を移植せず、協働通信とその失敗から設計上の示唆を得た。初回の理解確認から実際の有効性を学ぶ。

## 3. 対象六パスとSource

| Path | 操作・責務 |
|---|---|
| `board/README.md` | UPDATE。改行だけの入口を通信の目的・所有先・運用判断へ |
| `board/topics/20261001-dots-work-reconnection/README.md` | CREATE。初穂から二つの既存Work Threadへの自己完結した紹介・変更報告 |
| `README.md` | UPDATE。Boardへの案内一行のみ |
| `dots/README.md` | UPDATE。二軸の現在方向とBoardへの短い案内、版更新 |
| 本記録 | CREATE。採用理由・承認・実装・検証証拠 |
| `control-center/README.md` | UPDATE。STR-006の索引のみ |

基点[4fe6572](https://github.com/yusukefujiijp/ai-project/tree/4fe6572b56b3ac5ed2649b52385c74682d45d83f)でSTR-006は未使用、board READMEは1改行。AGENTS v004-candidateと既存のRoot／ARK／Dots／control-centerを確認し、Ark Markdownの意味・根拠・読者に応じた役割分離を適用した。GitHubは現在利用可能なconnector経由。基点を保った対象差分だけを一体で公開する。

主要Sourceは[STR-003固定版](https://github.com/yusukefujiijp/ai-project/blob/28037867cce29d9d78cf409dc16ee5518feb7362/control-center/changes/STR-003-persistent-collaboration-foundation.md)、[STR-004固定版](https://github.com/yusukefujiijp/ai-project/blob/02afa89744c7e44abf03acab809aa617910c8bfa/control-center/changes/STR-004-elon-musk-deadline-revision.md)、[STR-005固定版](https://github.com/yusukefujiijp/ai-project/blob/508e110ced0bc5f27a3d35444edaef9f4feec0b2/control-center/changes/STR-005-dots-collaboration-foundation.md)、[初穂形成記録](../../dots/records/2026/20261001-first-fruit.md)。今回のHumanの二軸・Board・柔軟な実地方針は現在のDots対話の報告・承認を編集した。公開されていない会話URLや時刻は作らない。

担当は、Human YusukeJPが目的と実行承認、Dot00:00; 初穂（dot-0000）が編集・実装・結果統合。GitHub author／committerと保存時刻は実際のcommitから確認する。通信の送信者とGit記録者を混同しない。

## 4. 検証と公開証拠

公開前に六パスの構造・リンク・宣言EOF・権限と版境界・送受信帰属を確認し、独立AIが未知の受信者として意味を点検する。本文が分かることの限定的な確認と、Ark27:07／Ark28:02本人の実受信は別に記録する。

公開時はmain基点を再確認し、対象外のblob／modeを保持してnon-forceで更新する。六本文をRemoteから全文再取得し、意図した内容・SHA・EOF・対象外不変を確認する。後続の観測だけを本節へ追記する。

**現時点: 候補作成。公開・Remote検証は未実施。宛先の受信・返信も未観測。**

## 5. 実地Feedbackで育てる

実際に起きた出来事の範囲で、期待した伝達、受け手の観測・Humanの報告、理解の差、原因仮説、修正内容、再確認を残す。原因を未確定のまま断定せず、返答者と読んだ版が違えば区別する。通信の訂正はTopicへ、構造改善の実装は本件または適切な変更記録へ、各仕事の結果はその原本へ戻す。

受信・疑問・返信がまだない時は、その不在を成功・失敗・未読の証拠にしない。Humanが望む柔軟さは、無記録の改変や自動的な権限拡大ではなく、実際の学びから必要な形を変えられること。保存Skillは構想段階であり、必要な時にその対象と実装権限を判断する。

復元が必要なら本件の差分を確認し、後続の返信・Human・他AIの変更を保持して修正する。Repository全体を過去へresetしない。

EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_006::v001
