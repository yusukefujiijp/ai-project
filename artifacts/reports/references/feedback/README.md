---
title: "Report Feedback — 反応を、読み直せる根拠として残す"
canonical_path: "artifacts/reports/references/feedback/README.md"
version: "v002"
created: "2026-10-26"
updated: "2026-10-26"
updated_reason: "Reference the shared feedback contract; retain Report scope, initial records, provenance and artifact storage route."
role: "Report feedback scope and formation; shared format and update contract reference"
row_schema_version: 1
primary_reader: "Current AI / Future AI / Human review"
expected_eof: "EOF::REPORT_FEEDBACK::v002"
---

# Report Feedback

Reportの制作・内容・表現・閲覧・保存・再利用に対する反応、評価、希望、提案、訂正を、[feedback.jsonl](feedback.jsonl)へ対象と文脈を保って残す。AIがまだ教訓や成功事例へ整理していない反応も、後から読み直せる根拠にする。三本の分担と他の原本への接続は[親のReferences](../README.md)が所有する。

## 1. Reportでの利用と共通契約

対象はReportの制作・内容・表現・閲覧・保存・再利用への反応である。今回の目的・読者・条件に関係する記録と後続の訂正を選び、対象・Human原文または編集要約・出典・補足を合わせて読む。

行形式（feedback schema 1）、原文と解釈の区別、訂正と新しい反応の区別、並行変更・中断復旧・保存後再取得は[共有Feedback契約](../../../../references/feedback/README.md)に従う。初回利用・未読・版変更時は当該契約を確認し、読めない場合は未確認と影響を示す。この参照だけでReportの収録範囲・権限・データを共有側へ移さない。

Report固有の配置と再取得は[Artifact → GitHub](../../../../prompts/artifact-to-github.md)へ接続する。現在の二件は同じID・本文で保持し、共有Feedbackへ同期・再登録しない。反応からの新Task化や全件lesson化を求めない。

## 2. 初期収録と権限の境界

初期二件は、Ark28:07でHumanが提供した、表現形式・調査範囲へのFeedbackと、初回Reportの内容評価・読書体験へのFeedbackである。Feedbackとして囲まれた本文を原文で保持し、周囲の会話全文やAI回答は転記しない。発言の正確な日時・message ID・実閲覧版は未確認とし、登録日時や確認用snapshotで代用しない。

「何倍も良かった」という期待を実測効果に、「初回実験として合格」を内容全体の高評価に、「番号が必要かも」を採用済み規則に変えない。記録の成立は、Reportの改訂・番号付け・HTML化・Skill登録・GCI変更・実利用効果の確認とは別である。

公開範囲と権限は[親のReferences](../README.md)と[AGENTS](../../../../AGENTS.md)に従う。承認された公開可能な対象だけを保存し、私的Work全体や長期メモリの収集・転記・同期へ広げない。過去の提案・承認やFeedback保存から、新しい実行・送信・自動収録の権限を作らない。Root・Teshuvah・HumanのMeaning／Correction／STOPと適用Guardを保持し、三本の記録とAIはKeliとして扱う。

EOF::REPORT_FEEDBACK::v002
