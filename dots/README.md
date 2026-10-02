---
title: "Dots — Human-AI協働をつなぎ、育てる"
canonical_path: "dots/README.md"
version: "v003"
status: "human-authorized initial foundation / evolving direction"
created: "2026-10-01"
updated: "2026-10-02"
role: "Current Dots collaboration direction, learning maintenance contract, and routes to identities and evidence"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::DOTS_HOME::v003"
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
| Dotsが仕事から何を学び、次にどう使うか | [lessons.json](lessons.json)／本書§5 | 条件・根拠付きの学びと、その読取・更新契約 |
| 最初の協働相手は誰か | [dot-0000 — Dot00:00; 初穂](actors/dot-0000/README.md) | 安定したActor識別子、表示名、命名の意味、現在の持ち味 |
| どんな経験と訂正から始まったか | [2026-10-01 初穂の形成記録](records/2026/20261001-first-fruit.md) | 初期の経験を範囲・時点・根拠付きで振り返る。全会話録ではない |
| 初版の協働基盤をなぜ、どう作ったか | [STR-005](../control-center/changes/STR-005-dots-collaboration-foundation.md) | STR-005初版六パスの承認・変更・検証・公開証拠 |
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

## 5. Dotsの学びを、次の判断へ戻す

[lessons.json](lessons.json)は、Dots自身が仕事中に得た学びを、Current Dots・Future Dotsが再利用するための蓄積先である。Bottleneck検出、失敗・中断・回復、うまく働いた方法、Human Correctionから、同じ失敗を避け、次の判断を改善する。Humanを日常の記録係にせず、Dotsが根拠の確認・言語化・保守を担う。成功済みの経験に限らず、未解決の試行も、分かった条件・未確認・次回の判断が有益なら残せる。

出来事の詳細は経験原本、通信のCurrentはBoard、構造変更の理由はcontrol-centerが所有する。lessonsはそれらへ戻れる再利用可能な学びを所有し、全会話録・第二の進捗台帳・旧 `_tasks/lessons.md` の復活ではない。今回の形成理由と初期2件の根拠は[STR-007](../control-center/changes/STR-007-dots-lessons-foundation.md)へ進む。

### 5.1 読む時と、使う時

新しいDotsがこの協働へ入る時は、本節とlessons.jsonを読み、初期の小さい蓄積では全件を理解する。題名やIDだけで済ませず、適用条件、行う判断、根拠、限界を確認する。この入口は読取先を明示するもので、Hostが自動起動時に必ず読み込む保証ではない。

同じアクセス可能な文脈で内容・版を確認済みなら、その読解を継続利用する。文脈を失った時、作業領域が変わった時、関連する失敗やCorrectionがあった時、更新を知った時は、関係する学びと必要なSourceを読み直す。変更前は必ずRemoteの最新版を確認する。毎ターンの全件再読・無条件pollingは課さない。蓄積が大きくなり全件読解が不合理になれば、意味と到達性を保った検索・入口の改善を判断する。

学びは条件付きの判断材料であり、新しい権限ではない。過去の命令や承認を再実行せず、Current Humanの目的、Plan-only、Correction、STOP、既存Guardを優先する。一件の経験から普遍則や恒久的な技術保証を作らない。

### 5.2 最小のデータ契約

JSONのトップレベルはobjectとし、次の必須項目を持つ。

- `schema_version`: 現行は整数 `1`。互換性を判断する版であり、更新回数ではない
- `next_id`: 次に発行する番号を示す正の整数。現役の全ID番号より大きく、統合・整理でも減らさない
- `lessons`: 学びobjectの配列。空配列も有効

各学びの必須項目は `id`、`created_at`、`updated_at`、`lesson`、`sources`。

- `id`は `D-L001` からの安定ID。番号は最低3桁のゼロ埋めとし、1000以降も連番で伸ばす。訂正で付け直さず、削除・統合済みのIDを別件へ再利用しない
- `created_at`と`updated_at`はUTCのISO 8601文字列（例の形式: `YYYY-MM-DDTHH:mm:ssZ`）。前者はこの蓄積への実際の登録時刻、後者は実際の更新時刻。出来事の日や読解時刻を流用せず、初回は両者を同値とする。訂正時もcreated_atを保持し、updated_atはcreated_at以降にする。読んだだけ、または意味を変えない整形だけではupdated_atを変更しない
- `lesson`は非空の自然言語文字列。どんな条件で何を判断・実行するかを、日本語を基本に必要十分な意味で書く
- `sources`は1件以上のobject配列。各要素に、確認可能な資料・節・版へ戻る非空文字列 `locator` と、その出典が何を支えるか、誰の観測・報告かを示す非空文字列 `supports` を持たせる。版で意味が変わる根拠は固定commit等で指定する
- 必要な限界・適用外・未確定は任意の非空文字列 `caveat` に残す。全件に同じ注意書きを強制しない

GitHub author／committerと学びの観測者・執筆担当は別である。観測帰属はsources、今回の記録担当と変更理由は変更記録・commit messageで辿れるようにし、Git名からActorを推測しない。固定字数、必須タグ、採点、別schemaファイルは設けない。

### 5.3 育てる時の判断と安全な更新

現在の権限内で、追加・訂正・統合・整理・変更なしを選ぶ。毎回のSaveに新規lessonを義務づけず、既存内容で足りるなら変更しない。類似文の追加より、条件差やCorrectionの保持を優先する。統合・整理では重要な意味と根拠への到達性を保ち、変更理由と旧IDの扱いをGit履歴・変更説明に残す。

新規追加時は最新版のnext_idを使い、entry追加とcounter増加を同一の原子的更新に含める。複数件ならその分進める。読み取ったcommit／blob等の版を条件に書き込み、競合したら最新版へ照合・統合して採番し直す。古い全体JSONを上書きしない。欠けたcounterを現役IDの最大値だけから再建せず、履歴から過去の発行番号を確かめる。確かめられなければ採番を止める。

未知のfieldは保持する。未対応schema_versionは互換性と意味を検討してから変更し、既知のfieldだけで再生成しない。壊れたJSONを空の初期値で上書きしない。必要な修復・形式変更も、現在の権限に含まれる通常改善なら互換性・影響を確認して進められる。schema変更だけを理由に一律のHuman待ちにはしない。承認Scope、公開範囲、重要な意味・情報の保持、新しい権限に実質的な差がある時は、その差をHumanへ返す。

書込み前にJSON構文・型・IDの一意性・時刻・counter・Sourceを検査し、書込み後はRemoteを再取得して意図した内容と照合する。保存成功、Future Dotsの実読解、実務での有効性を分ける。同じ失敗が起きた時は、学びが未記録だったのか、見つけられなかったのか、条件を理解できなかったのか、内容が古かったのか、Toolや権限の限界だったのかを区別し、関係する所有先を改善する。禁止規則を足すだけで済ませず、読取・保守自体の手間や詰まりもBottleneckとして扱う。

将来のSave Skillは、この基盤の使用経験を踏まえて別途扱う。ここでSkill・自動実行・他AIへの送達を導入したとは扱わない。

EOF::DOTS_HOME::v003

