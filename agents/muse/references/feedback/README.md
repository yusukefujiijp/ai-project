---
title: "AI-Mammoth References — feedback（反応の柱）"
version: "v001"
canonical_path: "agents/muse/references/feedback/README.md"
role: "Contract for receiving, recording and re-reading Human feedback"
status: "active — built 2026-10-27"
created: "2026-10-27"
updated: "2026-10-27"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_REFERENCES_FEEDBACK::v001"
---

# feedback ── 対象を伴う反応を残す

誰が、何に対して、どのような評価・違和感・希望・提案・訂正を示したかを残す柱。肯定と批判が同居する反応は、その関係のまま保つ。原文と編集要約を明示し、AIの解釈をHumanの発言へ混ぜない。

- 本文の原本：[feedback.jsonl](feedback.jsonl)
- 入口と全体契約：[../README.md](../README.md)

## 読取

現在の対象に関係する行を選び、target と feedback.text、sources、caveat を読む。反応は当時の対象と条件に結び付いているため、現在の判断へは「共通点と相違点」を分けて適用する。Feedbackは lesson 化待ちのTaskではない。期限も追催も発生させない。

## 行形式（JSONL契約）

- UTF-8、LF区切り、1物理行に1つのJSON object。非空ファイルは末尾LFを持つ。0件は0バイト。BOM・空行・配列の外枠・行間カンマ・Markdown fenceをデータに入れない。
- 共通必須field：`schema_version`（整数 **1**）、`id`（UUID v4。訂正や再試行で付け直さない）、`created_at`／`updated_at`（UTC、`YYYY-MM-DDTHH:mm:ssZ`。登録と意味更新の時刻。初回は同値）、`sources`（1件以上の object 配列。各要素は非空文字列 `locator` と `supports` を持つ）。
- 柱の必須field：`target`（何への反応か、非空文字列）、`feedback`（object：`speaker`＝確認できる発言者、`representation`＝`verbatim` または `summary`、`text`＝原文または編集要約。いずれも非空）。
- 任意：`title`（非空文字列）、`caveat`（非空文字列。抜粋の範囲、識別子の限界などの留保）。
- 未知fieldは保持する。既知項目だけで行を再生成しない。

## 更新

- 転記ミスや同じ反応の訂正は、同じIDの行を更新し、理由と根拠を残す。
- 後日に届いた別の反応は、別の行として追加する。明示的な撤回・訂正は、対象IDと訂正範囲を結ぶ。
- 原文（verbatim）へAIの補足を混ぜない。抜粋なら、その範囲と重要な留保を sources や caveat で説明する。

## 版と変更

- v001（2026-10-27）: 柱を新設。feedback.jsonl は0件で開始し、初期記録はモデルケース（GIF系）から同日収録する。

EOF::AI_MAMMOTH_REFERENCES_FEEDBACK::v001
