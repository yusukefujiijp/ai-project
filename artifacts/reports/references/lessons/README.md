---
title: "Report Lessons — 条件付きの判断を次へ渡す"
canonical_path: "artifacts/reports/references/lessons/README.md"
version: "v001"
created: "2026-10-26"
updated: "2026-10-26"
updated_reason: "Route Report-specific lessons to the existing row schema 2 and update contract without duplicating it."
role: "Report lesson use and format-contract entry"
row_schema_version: 2
expected_eof: "EOF::REPORT_LESSONS::v001"
---

# Report Lessons

Reportの執筆・構成・伝達・保存・再利用に固有の条件付き判断を、[lessons.jsonl](lessons.jsonl)で育てる。作品固有の訂正、成功事例、全体共有の学びとの分担は[親のReferences](../README.md)が所有する。

## 1. 必要な判断へ戻す

現在の問いに関係するlessonを選び、本文・sources・必要なcaveatを合わせて読む。今回の目的・読者・条件へ適用できる部分を判断し、過去の経験を現在の事実や承認へ置き換えない。既存の[共有lesson](../../../../references/lessons/README.md)で十分なら同じ意味を追加せず、Report固有の再利用条件を残す。

## 2. 形式・更新・検証

[既存lessons契約](../../../../agents/dots/lessons/README.md)の第3〜5節にあるrow schema 2・読取・更新・検証契約を参照して再利用する。各行はlesson object一件とし、管理行やMarkdownをデータへ入れない。形式契約の所在から、Dots固有の起動・全件読込・所有範囲・書込権限を移植しない。

更新前には最新版の全文とrevisionを確認し、全行を検証する。同じlessonの訂正は同じIDの現行行へ反映し、変更前の内容はGit履歴で辿る。未知field・根拠・並行変更を保持し、保存後に本文と版を再取得確認する。既存内容で足りる場合は変更しない。専用schemaや共通契約の複製を増やさない。

このREADMEは使い方と契約への接続を、JSONLは判断・根拠・限界を所有する。Root・権限・公開範囲は[親のReferences](../README.md)と適用指示を保持する。記録の保存と、次のAIによる理解・実際の改善は別の成立条件である。

EOF::REPORT_LESSONS::v001
