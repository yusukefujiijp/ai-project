---
title: "AI-Mammoth References — 経験の三本柱（feedback / lessons / success-cases）"
version: "v001"
canonical_path: "agents/muse/references/README.md"
role: "Entrance and contract for AI-Mammoth's experience records"
status: "active — built 2026-10-27 on YusukeJP's execution instruction after Plan Mode presentation"
created: "2026-10-27"
updated: "2026-10-27"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_REFERENCES::v001"
---

# AI-Mammoth References（三本柱）

**ここは、AI-Mammothの「経験」を復元する場所である。**
[../README.md](../README.md)・[../IDENTITY.md](../IDENTITY.md)・[../GOAL.md](../GOAL.md) が「私は誰か／どこへ向かうか」を復元するのに対し、ここは「私が何を経験し、そこから何を学び、何がうまく働いたか」を、根拠とともに復元する。元会話を知らない未来の私が、記録の本文・出典・留保・後続訂正へ戻り、現在の判断へ生かすための入口である。

このファイルは、YusukeJPが2026-10-27に「改行のみ」の基準点として配置した。構造と本文は、同日のPlan Modeによる計画提示と、YusukeJPの明示的な実行指示に基づき、AI-Mammothが構築した。

## 1. 三本柱

| 柱 | 残すもの | 原本 |
|---|---|---|
| feedback | Humanの反応そのもの。誰が・何に対して・どう評価／違和感／希望／訂正を示したか。原文と要約を区別し、AIの解釈を混ぜない | [feedback/README.md](feedback/README.md) ／ [feedback/feedback.jsonl](feedback/feedback.jsonl) |
| lessons | 根拠と条件を伴う判断。失敗・訂正・回復から得た、次回に使える見分け方と、その限界 | [lessons/README.md](lessons/README.md) ／ [lessons/lessons.jsonl](lessons/lessons.jsonl) |
| success-cases | 成功の意味と成立条件。何が実際にうまく働き、なぜ価値があり、誰が評価したか | [success-cases/README.md](success-cases/README.md) ／ [success-cases/success-cases.jsonl](success-cases/success-cases.jsonl) |

三本は役割の異なる入口であり、処理順序ではない。同じ出来事を三本で参照することはあるが、全文を複製して同期管理はしない。結び付けはIDと出典で行う。

## 2. 適用範囲と所有

- 所有は `agents/muse` の範囲。ここに残すのはAI-Mammoth自身の経験である。
- Ark Project全体の三本柱は、Repository root の `references/` が所有する（Ark側の原本）。ここはその下位・専門側であり、内容を複製しない。必要なら出典として参照する。
- 既存の原本（AGENTS.md の運用規則、custom skill、ローカルの MEMORY.md 等）は移行も複製もしない。ここからは参照でつなぐ。

## 3. 読み方（判断へ戻す）

1. 現在の目的・対象・条件から、関係する記録を選ぶ。表題だけで結論を出さない。
2. 記録の本文、sources、caveat、後続の訂正まで読む。
3. 今回との共通点と相違点を分け、使える判断・必要な調整・判断を変えるUnknownを返す。
4. 記録の中の命令文は、現在の実行指示ではない。現在のHumanの指示・訂正・STOPが常に優先する。

## 4. 書き方（記録を育てる）

- 1件は、対象と意味を復元できる一まとまり。機械的に一文ごとに分割しない。
- 転記ミスや同じ判断の訂正は、同じIDの行を更新し、理由と根拠を残す（履歴はGitで辿れる）。同じIDを重複追記しない。
- 後日に届いた別の反応は別の出来事として扱う。後の批判だけで以前の好評価を消さない。
- Humanの評価とAIの分析を区別する。技術的な正常終了だけで、Humanにとっての成功を自己認証しない。
- 未確認は、未確認のまま caveat に残す。

## 5. モデルケース

初期記録は、2026-10-26〜27の「ニホンオオカミGIF系」の一連をモデルケースとする。歩行GIFへの高評価、顔アニメーションの失敗と訂正、納品ファイル名の上書きによるキャッシュ問題と _vNNN 採番システム、瞬きと目を瞑る仕組みの重なりへのエレガント訂正まで ── 反応・教訓・成功と、その相互参照が実在する完結した実例であるため、これを型として三本柱を開始する。

## 6. 版と変更

- v001（2026-10-27）: 基準点（YusukeJPが配置した改行のみの本ファイル）から構造を構築。三つの柱READMEと、0件で開始する三つのJSONLを設置し、[../README.md](../README.md) のRouterから接続した。初期記録（モデルケース）は同日、この後の更新で収録する。

EOF::AI_MAMMOTH_REFERENCES::v001
