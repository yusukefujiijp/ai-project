---
title: "References — 共有する知見への入口"
canonical_path: "references/README.md"
version: "v001"
status: "human-authorized initial foundation / evolving through feedback"
created: "2026-10-10"
updated: "2026-10-10"
role: "Cross-domain reference entry and shared lesson ownership; not a repository inventory"
expected_eof: "EOF::SHARED_REFERENCES::v001"
---

# References — 共有する知見への入口

個別の協働で得た知見のうち、領域を越えて再利用する価値があるものへ、Current AI・他AI・Future AIが戻る入口。このREADMEは資料の役割と参照・更新先を案内し、学びの本文は[lessons.jsonl](lessons.jsonl)が所有する。通常の読取・整理はAIが担い、Humanも必要な時に意味を追える日本語を基本にする。

## 1. 現在の資料と役割

| 資料 | 所有する意味 | 読む場面 |
|---|---|---|
| [lessons.jsonl](lessons.jsonl) | ai-project全体で再利用できる、条件・根拠付きの判断 | 構成の整理、保存先の選択、似た問題の再発など、過去の学びが現在の判断を変える時 |

初版はこの一つの蓄積から始める。将来の分類や空フォルダを予約せず、別の参照資料が必要になった時に役割と接続を判断する。rootに散在する資料の一括移動先、全会話の保管庫、全体の進捗台帳にはしない。

## 2. 必要な場面で読み、現在の判断へ戻す

現在の目的と適用範囲から関連するlessonを選び、判断・根拠・条件・限界を読む。小さい蓄積は全件で比較できるが、毎ターンの無条件全読込は課さない。同じアクセス可能な文脈で確認済みかつ変化のない内容は再利用する。増加によって検索・分割が必要になれば、意味と到達性を保って方法を育てる。

Humanの報告・評価、直接確認した結果、AIの解釈、未実証の仮説を分ける。一件にも保存価値はあるが、局所的な成功を全場面の保証へ変えない。過去の命令や承認を現在の実行許可にせず、最新の依頼・Correction・Plan-only・STOPと[AGENTS](../AGENTS.md)を優先する。

入口と保存の存在は、全AIへの自動読込・理解・実利用効果を保証しない。取得できない場合は、その未確認が影響する判断を明示し、独立して可能な支援まで一律に止めない。

## 3. 学びの担当を選ぶ

- 領域やActorを越えて再利用できる判断は、この[全体用lessons](lessons.jsonl)へ。
- Dots固有の協働・運用に適用する学びは、[Dots lessons](../dots/lessons/README.md)へ。
- Radio・Voiceなどの固有条件が中心なら、該当領域の入口が指す専門lessonへ。例：[Radio](../skills/radio-mode/references/lessons.jsonl)、[Voice](../skills/voice-mode/references/lessons.jsonl)。
- 出来事の詳細・成果物・通信・日時記録は、それぞれの経験原本・成果原本・Board・[records](../records/README.md)へ。lessonは必要な根拠へ接続し、全文を集め直さない。

同じ目的・意味の現行lessonを複数箇所へ同期コピーしない。専門から全体へ広げる場合は、何を一般化し、どの条件を専門側に残すかを確かめる。既存lessonの移設・統合が必要なら、現在の権限、重要な意味、旧参照、IDと履歴を保持できる方法を選ぶ。ここを設けたことだけで既存のDots・専門lessonを一括移設しない。

保存の判断は[$saveスキル](../skills/save/SKILL.md)と現在の対象・公開範囲に従う。公開できるSourceを読めることと、その内容を保存・公開できることは別である。

## 4. 形式・更新・確認

JSONLの形式と更新・検証には、[既存lessons契約の第3〜5節](../dots/lessons/README.md#3-全行がlesson--row-schema-2)を参照して再利用する。lessons.jsonlの各行はschema 2のlessonであり、管理行やMarkdownを入れない。契約本文をここへ複製せず、Dots固有の読込義務・所有範囲・書込権限を全体へ移植しない。契約の所在と、学びの適用範囲は別である。

意味の訂正は同じlesson IDの現行行へ反映し、同じIDを追記して最新版とする方式にはしない。既存内容で十分ならNO_CHANGEを選べる。更新前の最新版・版条件、未知fieldと他AIの変更の保持、保存先からの再取得照合を守る。構文・保存の確認、別AIの読解、実利用の効果を分ける。

READMEは資料の役割・案内が変わる時、lessonは判断や根拠・条件が変わる時に更新する。同じ説明を両方で直す必要が生じたら、責務の重複を見直す。構成自体も改善対象であり、階層やファイル数の固定を目的にしない。

## 5. 初版の形成と再帰的な適用

2026-10-10、dot-0000との対話で、HumanはSkill配下のlessonsを直下へ置く案とreferences配下へ置く案を比較した。AIが通常利用・保守し、Humanはまれな確認時にも読める構成を望んだ。Radio／Voiceでは、条件付きの学びをreferencesへ置き、形式契約だけを再利用する構成を採った。[当時の形成記録](https://github.com/yusukefujiijp/ai-project/blob/8d0ab64a2fd5ffe7390fd8eb9933867176bad7ed/skills/README.md#radio-voice-formation)へ戻れる。

Humanはこの小さな工夫をai-project全体へ活かす方向を求め、最初の学びとして「Simpleさを階層の浅さだけで測らず、役割・参照先・更新先の迷いが減るかで判断する」という案を評価し、その再帰性を指摘した。rootの横への広がりも課題として述べ、READMEとlessonsの空ファイルを用意した。複数回のPlan Modeを経て、この二ファイルとroot README・saveの案内を合わせた実装を承認した。

初版では、入口は本README、判断の本文はlessons、形式の詳細は既存契約と分ける。この設計に最初の学びを適用しているが、自己適用自体を有効性の証明にはしない。Humanの評価・構成の成立と、全AIでの再現性・長期の負担軽減を区別し、実際の使用とFeedbackで修正する。計画を反復する回数を全作業へ固定しない。

形成の追跡識別子は私的対話の所在であり、公開URLではない。上記は編集要約で、会話全文の転載ではない。
- 再帰性と第一lessonの評価：conversation-message:Sentinel_7987b1e470fc819189c23b5adc3bf302
- rootの問題意識・README新設・再計画：conversation-message:Sentinel_4e2a2dc21ae881919d92b047c7fece6a
- 四対象を合わせた実行承認：conversation-message:Sentinel_0c3f6e592f608191ab898d7b6c28cd77

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利。AI・学び・文書はKeli。[ARK](../ARK.md)の意味と[AGENTS](../AGENTS.md)の権限を保持し、この入口を新しい権限者にしない。

EOF::SHARED_REFERENCES::v001
