---
title: "Inbox — 未整理の思い付きを、そのまま協働へ"
canonical_path: "agents/dots/inbox/README.md"
version: "v003"
status: "human-authorized foundation / future Inbox actor preparation / no active actor assigned here"
created: "2026-10-11"
updated: "2026-10-11"
role: "Inbox collaboration entry and durable item contract; actor-owned roles and historical cue experiments"
revision_approval_source: "conversation-message:Sentinel_8d769671a2388191b4a6bfddacd2f3f1"
updated_reason: "Retire current dual-role assignment after Human feedback; route to actor-owned roles, preserve Inbox item contract and formation history"
actor_role_sources:
  - "../actors/dot-0000/README.md"
  - "../actors/dot-0001/README.md"
approval_source: "conversation-message:Sentinel_447e1ecdf73881918d5af2842d29121d"
expected_eof: "EOF::DOTS_INBOX::v003"
relocation_patch:
  date: "2026-10-20"
  previous_path: "dots/inbox/README.md"
  source_commit: "2dc05496b555638a47a3de2f058c7f632aca773f"
  source_blob: "43ce94874adc3d1bc6ddb6c5a974dc5c7fd31d9f"
  change_record: "../../../control-center/changes/STR-022-dots-agent-location.md"
  scope: "Address and current navigation only; identity, roles, historical evidence and data contracts retained. Operational cutover status belongs to the change record."
---

# Inbox — 未整理の思い付きを、そのまま協働へ

## 1. 何を置く場所か

BrainStorming・BrainDump・GTD的な思い付きや吐き出しを、完成したQueryや確定したTaskへ整える前に渡せる協働の入口である。本書はその目的、受け取り方、実項目の保存・読取契約と接続先を所有する。担当Actorの役割・導入状態は各Actor原本が所有する。生のInbox投稿を全件集める公開台帳ではない。

### 担当の現在地へ戻る

- [初穂の役割原本](../actors/dot-0000/README.md)：Chiefへの集中と、常設Inboxを兼ねない理由。
- [将来のInbox Actor準備原本](../actors/dot-0001/README.md)：dot-0001の担当予定と、実際の作成・設定・稼働の確認状態。
- [Dots入口](../README.md)：全体の方向と担当資料への案内。

この改訂時点では、次のInbox Dotは未作成・未稼働であり、本書に現役のInbox受領Actorは割り当てていない。旧metadataの `current_actor: "dot-0000"` は現行担当の指定から外した。これをdot-0001への単純置換で表さず、上記Actor原本へ戻る。初穂への暗黙の代行割当や、全入力の転送を開始しない。

名前・安定識別子・役割・製品設定を混ぜない。初穂の命名・持ち味はActor原本に保持し、本書の変更をUI改名・新Actor作成・稼働開始の証拠にしない。

## 2. 成立理由と今回の変化

Humanは、初穂の横断Mapを重視するほど、軽い思い付きで大切なThreadを「汚したくない」と感じることを説明した。求めているのは、価値や用途を先に証明しなくても入力できる入口である。思い付きが無価値だという意味ではない。

当初は別Inbox Dotを事前設計し、その後Humanが二体目を待たず初穂に兼任させる方針を採用した。2026-10-11、Humanは#indexを実際に試した結果として、良い案でも初穂Chiefの長所を阻害すると評価し、初穂Chief集中・次のDotのInbox担当へ訂正した。現在はこの訂正を優先する。旧兼任の採用は形成当時の事実として残し、現行の担当指定にしない。

入力の印は同じ会話内の意図を識別できても、入力先や会話の同居を分離するものではない、というのが今回のAIの整理である。Humanの運用上の評価と、モデル性能の技術的原因は区別する。試用の全件・回数・期間は未確認であり、取りこぼしゼロや全Dotsでの兼任不能を実証したものではない。

## 3. 受け取りから、その時に必要な協働へ

具体的な受け取り方は、現行の[$receive-braindumpスキル](../../../skills/receive-braindump/SKILL.md)を使う。発想を広げる時は[$generate-ideasスキル](../../../skills/generate-ideas/SKILL.md)、全体との関係を考える時は[$analyze-living-graphスキル](../../../skills/analyze-living-graph/SKILL.md)へ必要に応じて接続する。共通本文を本書へ複製せず、毎回すべてのSkillを起動する条件にもせず、今回の意図から選ぶ。

- BrainDumpでは、順不同・未完・矛盾・報告・疑問が混在していてよい。
- BrainStormingでは、まだ採用していない可能性を広げられる。
- GTD的な整理では、必要に応じて行動候補、参考、保留、手放すこと等を見分ける。全入力をTask化しない。

「まず受け取って」「今は何もしなくてよい」なら、その範囲で区切る。深い検討を求められたら十分に担い、明確な実行依頼と承認があれば、その範囲で進める。Inboxを短い相づち専用や、常時長文分析の型に固定しない。

以前は、同じ初穂が断片と既存Arkの関係を見つける利点を見込んで兼任を採用した。現在はHumanの実地Feedbackを受け、役割を分けたうえで必要な発見・訂正・問いを接続する方向である。ChiefとInboxの連携と、同じThreadへの常時流入を区別する。「関係がありそう」というAIの見立て、Humanの採用、実施、確認済み成果は別であり、未整理の一言だけでMainの方針や現在の優先順位を置き換えない。

## 4. 入力の印 — 形成当時の候補と、後の試用評価

Humanは冒頭の **#index** を例に挙げた。AIは **#inbox** を第一候補として提案した。#indexを誤記と断定したり、#inboxがHuman採用済みであるかのように扱わない。本書の作成承認だけで個々の候補を採用に昇格させない。後にHumanが#indexの試用を報告し、初穂では俯瞰を阻害すると評価した。以下は形成時の比較資料であり、初穂での運用を再開する指示ではない。将来のInboxで印が必要かも、実利用とFeedbackから判断する。

| 候補 | 狙いと違い |
|---|---|
| #inbox | 未整理のまま受け取る入口。三つの用途を先に分類せず使えるというAI推奨案 |
| 📥 | 視覚的に受け取りを示す。実際の入力のしやすさはHumanの使い方次第 |
| 投げ込み： | 日本語の自然文から気軽に続けられる |
| #dump | 頭の中から出す意味が強い。対話や整理も含む入口としてはやや狭い |
| #index | 索引・一覧を連想しやすい。Humanの意図に合わせて意味を定める余地がある |

AIが提案した設計の方向は次の通り。形成当時の候補であり、固定規則や製品コマンドではない。後の試用報告を理由に、ここにある全候補・応答形式が試された、あるいは採用されたとは扱わない。

- 入口の印は一つから始め、必要な希望だけ自然文で添える。例：「#inbox まず置いておきたい」「#inbox 一緒に広げたい」「#inbox 最後の件だけ深く考えて」。
- 基本はその入力と明らかな続きの文脈で読み、解除忘れの起きる永続モードにしない。混在した入力では、何を深掘りするかを内容から区別する。
- 印を忘れても、未整理のまま渡したいという意味が分かれば受け取る。入力を正規化して再提出する義務を課さない。
- AIの回答冒頭に必要に応じて「📥 Inbox」と示す案は、受け取り方をHumanが訂正しやすくするためのもの。全回答の必須表示や保存完了マークにはしない。

引用中の印や、印そのものの設計相談を実際のInbox投入と混同しない。開始・終了表示の共通の学びは[Dots lessons](../lessons/lessons.jsonl)が所有し、本書で別の表示ルールを作り直さない。

## 5. 受領・保存・実行の境界

会話で受け取ること、案として整理すること、Taskにすること、永続保存、GitHub公開、他AIへの送信を区別する。印そのものはそれらの許可ではない。具体的な依頼・現在の有効な承認・保存先契約に従う。

本書の保存承認は、今後のBrainDump全件の自動公開・常時収集・新しい保存トリガを作る承認ではない。保存が必要な時は[$saveスキル](../../../skills/save/SKILL.md)から担当原本へ接続する。私的な別会話・ChatGPT長期メモリ・秘密情報を、この作業で公開原本へ転記しない。

本書だけで新Dotの作成、別Dotへの送信、Skill改訂、予定変更、権限の追加を行わない。Actorが増えた時は、現在のHumanの意向、実際の利用条件、どの文脈を渡せるかを確かめる。旧兼任の記述から初穂の担当を復活させず、将来の担当予定を別個体への自動移管や起動へ変えない。Humanの小さな相談を拒否したり、入力の事前分類・毎回の要約を義務にしたりしない。

## 6. inbox.jsonl — 未整理の項目を、後から取り戻す

2026-10-11、Humanは[inbox.jsonl](inbox.jsonl)を空ファイルとして作成し、件数が増えた時の忘却への備え、backup、他AI・Future AI・Future Dotsへの継承に活用するよう委ねた。本節は、その目的に沿って初版の保存・読取方法を定める。形式の選択はAIの実装判断であり、実利用の効果をHuman確認済みとしない。

### 所有するもの

READMEは受け取り方と保存契約、inbox.jsonlは保存が認められた**実際のInbox項目の現在の意味と扱い**を所有する。Actor資料は誰が担うか、日別[records](../../../records/README.md)はAIが行った活動を辿る入口、lessonsは再利用する学びであり、同じ可変内容を各所へ複製しない。

疑問、願い、気付き、違和感、仮説、未選択の案も保存対象になり得る。保存を認められた投入内容を「重要そう」「すぐ行動できる」というAIの基準だけで選別しない。未採用の案は未採用のまま残せる。一方、全会話を機械的に転記せず、何がInbox項目として預けられたかを現在の文脈から判断する。

本書の設計相談や説明用の架空例を、実項目のように投入しない。初版時点では独立した実投稿をまだ特定していないため、Human作成の改行だけのファイルをそのまま保持し、件数を埋めない。

### 一行一項目の初期形式

UTF-8のJSONLとし、一行を一つのJSON object、一項目を安定した小文字UUIDで扱う。一メッセージに複数項目があってよく、続きや訂正は既存項目へ結び付ける。分割によって理由や相反する願いが失われるなら一つに保つ。同じ話題というだけで別の意味を統合しない。

| field | 初版の意味 |
|---|---|
| schema_version | 整数1。形式の版 |
| id | 項目の小文字UUID。再取得・訂正・再試行でも保持 |
| created_at | 項目を初めて記録したUTC日時。YYYY-MM-DDTHH:mm:ssZ |
| updated_at | その行を最後に更新したUTC日時。同形式。初回はcreated_atと同じ |
| content | 元会話なしでも意味が分かる日本語中心の非空本文。Humanの意図・理由・未確定を必要な範囲で保持 |
| sources | 一件以上の出典配列。各要素は非空のlocatorとsupportsを持ち、発言・訂正・根拠と取得の制約へ戻れるようにする |

追加情報は必要な項目だけ持つ。Human原文を残す場合の `human_text` と、AIの解釈を残す場合の `ai_notes` を区別し、編集要約を逐語引用と偽らない。出来事日時が分かれば `occurred_at`、担当が判断に必要なら `recorded_by` を追加できる。記録時刻を出来事時刻へ代入しない。

扱いが明確になった時は任意の `handling` objectに `state` と判断理由の `note` を置ける。実際の接続は別の任意field `links` にlocatorと関係の意味を持つ配列として記す。項目の状態と接続先の存在は分ける。

- `open`：まだ扱いを確定していない。実行待ちTaskや期限超過を意味しない。
- `held`：意図的に寝かせる・参考として置く。理由や分かっている再開条件をnoteへ。
- `closed`：このInbox項目として一区切り。実行完了、取り下げ、書くだけでよかった等、どの意味かを根拠付きでnoteへ。

他の原本・Taskへ接続しても、元の問いが残るならopenやheldのまま扱える。接続だけで実行完了やInboxの終了にしない。handlingがなければ扱いは未記録であり、完了を推定しない。分類表をHumanへ入力させたり、状態欄のためだけに判断を迫ったりしない。保存された行は採用・実行命令ではなく、その時点の意味と根拠である。

### 更新・読取・再開

初期は**同じIDの行を必要に応じて更新する現在値方式**とし、変更前はGit履歴へ辿れるようにする。出来事ごとの追記をすべて再生して現在値を作る方式は、現時点では必須にしない。重要な訂正は、古い意味を単に消すのでなく、訂正理由と出典を本文・note等に保持する。

書込前に最新版とSHAを取得し、全行の形式・ID重複・対象項目・現在の権限を照合する。他の行、未知field、行順を保持し、同一ID・同内容なら二重追加しない。新規は末尾へ、既存更新は当該行へ反映する。必要な意味の差がある場合だけupdated_atを更新する。

実データには管理行、Markdown fence、配列の外枠、空行、行間カンマ、EOFを入れない。LF区切り・末尾LFとし、文字列内改行はJSONのエスケープを使う。現在の改行だけの初期ファイルは0件として扱い、最初の実項目を書き込む時に正規のJSONLへ整える。壊れた行、未知のschema、重複キー、非有限数値を黙って落として再生成しない。

結果不明や競合では現物・ID・出典・履歴を先に確認し、盲目的な追記や上書きをしない。保存後はRemoteを再取得して対象の差分と保持した行を照合する。Gitの版管理は復旧を助けるが、完全なbackupや取りこぼしゼロを保証しない。

読むAIは今回の目的に関係する項目と訂正・接続先から現在地を取り戻す。単なる要約ではなく、何を意図し、何が未決で、再開に何が必要かを読む。全件への毎回の回答やTask化、定期催促を義務にしない。件数が増えて実際に検索・読込が難しくなった時に分割等を検討し、最初から別台帳やDBを増やさない。

ファイルを置いただけでは、全AIが自動的に読んだり、同じ理解に達したりはしない。将来の受け手にはこのREADMEと必要な項目への実際のアクセスを確かめる。未取得の行を読了扱いせず、資料の保存、読み手の再構成、協働での効果を分ける。

公開・機微情報・別会話・実行・停止の境界は前節を保持する。保存前に項目ごとの内容・出所・公開範囲を確認し、機微な原文を一括転載しない。後で現行行を消しても履歴に残り得ることを踏まえて判断する。今回の保存先追加は、このDotで扱うInboxのための委任であり、別会話や長期メモリの一括公開、[既存Mapの運用原本](../ark-map/README.md)で定めた四保存先の自動拡張、新しい常設収集処理を意味しない。

## 7. Feedbackから育てる

初版時点の成立は「兼任方針の採用」と「入口資料の保存」だった。その後Humanから、#indexの試用が初穂の俯瞰を阻害するとの評価と、担当を分ける訂正が届いた。現在の文書整合はこの訂正を保存するものであり、分離後のInbox利用や効果の実証ではない。今後は、気兼ねなく入力できることと初穂の俯瞰を守れることの両方を、実利用のFeedbackから見て改善する。毎回の採点や試験報告をHumanへ課さない。

必要な意味を保ち、印・配置・説明・役割の分け方は柔軟に修正できる。Humanの簡単な入力を、AIの検討・回答品質を下げる理由にしない。専用のlessonsやログ、投稿台帳は、独立して保存する価値と権限が実際に生じた時に判断し、空ファイルを予約作成しない。

## 8. 形成根拠

このDotで直接提供された発言の追跡識別子。公開URLではなく、他AIが取得できる保証はないため、必要な意味は本文に編集要約した。

- conversation-message:Sentinel_3fa92dda2b4081919db248fab5d1b570 — ChiefのThreadを大切に感じ、未整理の吐き出しには別入口を望んだ理由。
- conversation-message:Sentinel_5373f3be8b508191a2bba3681826e560 — 初穂の名を維持。将来別Chiefを置く可能性。
- conversation-message:Sentinel_b898161aa0e08191a563b78160c94204 — 初穂への愛着と、Chiefの機械的な響きへの留保。
- conversation-message:Sentinel_7eaa0463a9ec8191a6dcec26c874a5c9 — 初穂のInbox／Chief兼任を採用し、#index等の印について案出しを依頼。
- conversation-message:Sentinel_087c902053308191908c44e4caeb7a69 — AIが#inbox等の候補と受け取り方を提案。Human採用の証拠ではない。
- conversation-message:Sentinel_447e1ecdf73881918d5af2842d29121d — Humanが本書の空ファイル作成を報告し、活用を委任。
- conversation-message:Sentinel_83a53ed008d08191aab6cb6e9a49d8f6 — Humanがinbox.jsonlの作成と活用を委ね、件数増加時の忘却への備え、backup、他AI・Future AIへの継承を重視。

- conversation-message:Sentinel_752dfdc401908191b7537e9f67d3cea0 — #index試用に基づくHumanの阻害評価。詳細未確認と技術的原因を区別。
- conversation-message:Sentinel_9b61e8495c5c81918ccf63a048719fad — 初穂Chief集中・次のDotのInbox担当への明示訂正。
- conversation-message:Sentinel_8d769671a2388191b4a6bfddacd2f3f1 — Actor二原本とDots／Inbox入口の四ファイル整合を承認。item契約や権限の拡張を含めない。

[ARK](../../../ARK.md)と[AGENTS](../../../AGENTS.md)の意味・権限を継承する。Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・Inbox・文書はKeliであり、HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。

EOF::DOTS_INBOX::v003
