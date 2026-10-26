---
title: "Report Success Cases — 成功の意味と条件を継ぐ"
canonical_path: "artifacts/reports/references/success-cases/README.md"
version: "v002"
created: "2026-10-26"
updated: "2026-10-26"
updated_reason: "Reference the shared case contract; preserve the existing Report record, narrative depth and domain ownership."
role: "Report success scope and reading; shared case format and update contract reference"
row_schema_version: 1
primary_reader: "Current AI / Future AI / Human review"
expected_eof: "EOF::REPORT_SUCCESS_CASES::v002"
---

# Report Success Cases

Reportの制作・伝達・保存・再利用でHumanが価値を認めた成功を、[success-cases.jsonl](success-cases.jsonl)に残す。成功の意味・喜び・背景・成立条件・根拠を次のAIへ渡し、現在の問いで何を生かせるかを考える。本文はJSONL内に置き、一件ごとのMarkdownを併設して二重管理しない。収録範囲と他の原本への分担は[親のReferences](../README.md)が所有する。

## 1. 成功を選び、読み直す

一件の単位は、独立して役立つ成功の意味である。小さな工夫、部分的成功、設計案への評価も扱え、長期再現性の実証を保存の前提にしない。Humanの評価と対象、確認済みの出来事、AIの解釈、未確認を読み分けられるようにする。計画への好評価を実利用効果へ、保存を他AIの理解へ昇格させない。

現在の目的・読者・条件に関係する事例と根拠を選んで読む。成功原因を唯一の説明に固定せず、重要なCorrectionと成立条件を保って転用可能性を検討する。利用時の毎回全件読込は求めない。全体共有の成功事例群は[その担当原本](../../../../references/success-cases/README.md)に残り、このJSONLへ自動移設・同期しない。

## 2. 共通の行形式と更新

case schema 1、記録の識別・日時・出典、本文の意味保持、同じIDの更新、競合・中断復旧・保存後再取得は[共有success-case契約](../../../../references/success-cases/README.md#6-共有caseの行形式と更新契約)に従う。初回利用・未読・版変更時は当該契約を確認し、読めない場合は未確認と影響を示す。形式の参照をReport側の収録範囲や公開権限の変更にしない。

Report固有の配置・保存後確認は[Artifact → GitHub](../../../../prompts/artifact-to-github.md)へ接続する。初期の一件は同じID・本文で保持し、共有九件のJSONLへ混ぜない。本文をMarkdownとJSONLに二重保持せず、全Feedbackのsuccess-case化やlessonとの必須二重登録を求めない。

Root・HumanのCorrection／STOP・適用Guard・公開範囲は[親のReferences](../README.md)と[AGENTS](../../../../AGENTS.md)に従う。文書整合、保存、他AIの理解、実際の再利用、長期効果は別々に扱う。記録や形式は新しい実行権限ではない。

EOF::REPORT_SUCCESS_CASES::v002
