---
title: "Shared Lessons — 過ちから戻り、次の判断へ生かす"
canonical_path: "references/lessons/README.md"
version: "v001"
status: "human-authorized lesson entry / evolving through feedback"
created: "2026-10-20"
updated: "2026-10-20"
updated_reason: "Separate shared-lesson use and update routing from the references parent while retaining the existing JSONL contract and lesson meaning"
role: "Cross-domain lesson use and update entry; JSONL owns the lessons"
change_record: "control-center/changes/STR-019-references-learning-memory.md"
expected_eof: "EOF::SHARED_LESSONS_README::v001"
---

# Shared Lessons — 過ちから戻り、次の判断へ生かす

領域やActorを越えて再利用できるlessonの入口。失敗・行き詰まり・訂正・復帰から学び、特にAIが同じ過ちを繰り返さず、現在の状況に合う判断へ戻れるようにする。本文の担当原本は[lessons.jsonl](lessons.jsonl)。success-casesとの関係と、領域ごとの保存先選択は[親のReferences](../README.md)が案内する。

## 1. 現在の問いから使う

現在の問いに関係するlessonを選び、判断と成立条件、sources、caveatを一緒に読む。設計判断を含む既存lessonの意味と適用範囲も保持する。過去の指示や承認は、現在の実行権限とは別に扱う。Humanの報告・評価、直接観測、AIの解釈、未確認を区別する。

## 2. 形式・更新・確認

JSONLの形式と更新・検証には、[既存lessons契約の第3〜5節](../../dots/lessons/README.md#3-全行がlesson--row-schema-2)を参照して再利用する。各行はschema 2のlessonとし、管理行やMarkdownを入れない。形式契約の所在から、Dots固有の読込義務・所有範囲・書込権限を全体へ移植しない。

意味の訂正は同じlesson IDの現行行へ反映し、同じIDを重複追記して最新版とする方式にはしない。既存内容で十分ならNO_CHANGEを選べる。更新前の最新版・版条件、未知field、他AIの変更、重要な根拠と履歴を保持する。保存後は担当原本を再取得し、意図した内容を確認する。

このREADMEはlessonの使い方と更新契約への接続を、JSONLは判断・根拠・条件を所有する。保存の判断は[save](../../skills/save/SKILL.md)と現在の権限・公開範囲に従う。構文の成立、保存確認、別AIの理解、実利用の効果はそれぞれの証拠で扱う。

## 3. 所在の変化と継承

全体用lessonは、references初版で用意された本文をこのフォルダへ引き継ぐ。役割の分離と現在の参照経路は[親のReferences](../README.md)、移設範囲・旧参照・保持確認は[変更記録](../../control-center/changes/STR-019-references-learning-memory.md)へ戻れる。所在が変わったことだけで、lessonの観測・判断・ID・形成時点を更新済みとしない。

EOF::SHARED_LESSONS_README::v001
