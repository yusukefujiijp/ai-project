---
title: "AI-Mammoth References — success-cases（成功の柱）"
version: "v001"
canonical_path: "agents/muse/references/success-cases/README.md"
role: "Contract for recording what worked, why it mattered, and under what conditions"
status: "active — built 2026-10-27"
created: "2026-10-27"
updated: "2026-10-27"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_REFERENCES_SUCCESS_CASES::v001"
---

# success-cases ── 成功の意味と成立条件を残す

何が実際にうまく働き、なぜ価値があり、誰が何を評価したかを、背景・形成経緯・根拠・未確認とともに残す柱。予期せぬ成功、大きな突破、小さな工夫、部分的成功を、それぞれの範囲で扱う。成功の喜びや驚きも、意味を担う情報として保つ。

- 本文の原本：[success-cases.jsonl](success-cases.jsonl)
- 入口と全体契約：[../README.md](../README.md)

## 選択と読解

現在の課題に関係する行を選び、`case` 本文と sources、caveat を読む。成功の条件ごと持ち帰り、条件の違う今回へそのまま複写しない。Humanの評価とAIの分析を区別し、技術的な正常終了だけでHumanにとっての価値まで自己認証しない。反復実証や完全な因果解明を、一件を残す前提にしない。

## 行形式（JSONL契約）

- UTF-8、LF区切り、1物理行に1つのJSON object。非空ファイルは末尾LFを持つ。0件は0バイト。BOM・空行・配列の外枠・行間カンマ・Markdown fenceをデータに入れない。
- 共通必須field：`schema_version`（整数 **1**）、`id`（UUID v4。訂正や再試行で付け直さない）、`created_at`／`updated_at`（UTC、`YYYY-MM-DDTHH:mm:ssZ`。登録と意味更新の時刻。初回は同値）、`sources`（1件以上の object 配列。各要素は非空文字列 `locator` と `supports` を持つ）。
- 柱の必須field：`case`（非空の自然言語文字列。何が成功し、なぜ重要で、どの条件・根拠があり、どこが解釈・未確認かを記す）。収録単位は一つの独立して役立つ成功を基本とし、重要な条件とCorrectionは一緒に保つ。
- 任意：`title`（非空文字列）、`caveat`（非空文字列）。
- 未知fieldは保持する。既知項目だけで行を再生成しない。

## 更新

- 同じ成功への訂正（評価の撤回、条件の判明など）は、同じIDの行を更新し、理由と根拠を残す。
- 後の反応が成功の意味を変えた場合は、その反応を feedback に残し、IDと出典で結ぶ。成功事例だけを静かに書き換えない。

## 版と変更

- v001（2026-10-27）: 柱を新設。success-cases.jsonl は0件で開始し、初期記録はモデルケース（GIF系）から同日収録する。

EOF::AI_MAMMOTH_REFERENCES_SUCCESS_CASES::v001
