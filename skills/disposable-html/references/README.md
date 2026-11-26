---
title: "disposable-html references"
version: v001
updated: 2026-11-26
status: cultivation entry, not a second procedure
---

# disposable-html の育成床

このフォルダは、使い捨て単一HTMLの手順を次の完成版へ導く情報群です。完成品は上位の [SKILL.md](../SKILL.md) です。生成するAIは、このフォルダを読みません。

記録のあとも、この床は閉じません。新しい反応はここへ残り、繰り返し使える判断だけが手順へ昇ります。手順が厚くなること自体は向上ではありません。向上は、次の一枚がより直感的になることです。

## いつ開くか

| 問い | 開くもの |
|---|---|
| HTMLを一枚出す | 開かない。SKILL.md だけ |
| 誰が何と言ったか | [feedback/feedback.jsonl](feedback/feedback.jsonl) |
| 同じ過ちを、どの条件で止めるか | [lessons/lessons.jsonl](lessons/lessons.jsonl) |
| 何を成功と認め、どこまで保証しないか | [success-cases/success-cases.jsonl](success-cases/success-cases.jsonl) |
| 手順の一文を変えるべきか | 関係する記録を読み、変える判断だけを SKILL.md へ蒸留する |

locator の `#` 以降は記録のIDです。GitHubがJSONLのIDへ自動アンカーを作るとは扱いません。

## 三本の役割

意味と行形式は、次の共有契約を参照します。契約本文はここに複製しません。

- feedback は schema 1。[共有Feedback](https://github.com/yusukefujiijp/ai-project/blob/main/references/feedback/README.md)
- lesson は schema 2。[Dots lessons 第3〜5節](https://github.com/yusukefujiijp/ai-project/blob/main/agents/dots/lessons/README.md#3-%E5%85%A8%E8%A1%8C%E3%81%8Clesson----row-schema-2)
- success-case は schema 1。[共有Success Cases](https://github.com/yusukefujiijp/ai-project/blob/main/references/success-cases/README.md)

同じ出来事を三本へ全文複製しても、三件の実証には数えません。必要なIDで結びます。

Humanの言葉、確認した事実、AIの解釈、未確認は、記録の中で分けます。公開できない会話の所在は、その旨をlocatorに書きます。架空のURLは作りません。

## どこへ戻すか

- ページの事実が違う：そのHTML、または投稿。
- 次のコンパイル判断が変わる：SKILL.md。
- このSkillに固有の反応、条件、成功：このフォルダの該当JSONL。
- 領域を越える判断：共有referencesへ、参照で提案する。全文は移さない。
- 行形式そのもの：上の共有契約。ここでは変えない。

## 初期の実記録

2026-11-26の初期記録は、feedback八件、lesson六件、success-case一件です。見本行ではありません。登録時刻は `2026-11-26T11:40:00Z` であり、発言の時刻そのものではありません。

各AIへの登録、実際の起動、読者の理解は、この保存とは別に未確認です。
