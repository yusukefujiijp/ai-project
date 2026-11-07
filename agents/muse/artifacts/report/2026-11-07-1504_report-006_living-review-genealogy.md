---
title: "Report 006 — 方法の理解：Living Review と Report の系譜（2026-11-07 15:04 JST）"
version: "v001"
canonical_path: "agents/muse/artifacts/report/2026-11-07-1504_report-006_living-review-genealogy.md"
role: "AI-Mammoth's sixth report to YusukeJP: understanding of the method layer — the Living Review organ of 2026-09-19 and the genealogy of these Reports themselves"
author: "AI-Mammoth (agents/muse)"
status: "submitted / 2026-11-07 — md+html pair (same basename)"
created: "2026-11-07"
repository: "yusukefujiijp/ai-project"
reading_base_commit: "b755978a9d29fa1d974fafe7aa54d6474ca75bf0"
expected_eof: "EOF::AI_MAMMOTH_REPORT_006::v001"
---

# Report 006 — 方法の理解：Living Review と Report の系譜

提出日時：2026-11-07 15:04 JST　／　提出者：AI-Mammoth（二本立ての対として、同名の .html 版が添う）

## 0. 本Reportの範囲と読みの基盤

五面（核・形・変化・住人・仕組み）の読みが一巡した後、本 Report 006 は**方法**を扱う ── そして発見は、私自身の Report の系譜についてである。

読みの基盤は commit `b755978a` 時点。repository-reviews/README、review-prompt.md の冒頭、harness/adapters/chatgpt-work/README と harness/evals/README の冒頭を読んだ。review-prompt の本文全体、repository-reviews/reports/ の中身は読んでいない。§5 に残す。

## 1. 発見 ── Living Review、最古の器官

`repository-reviews/` は、Ark Repository Living Review の入口である。起源は **2026-09-19、Ark27:04、YusukeJP × AI-Collaborator** ── STR-001（2026-09-22）より前に生まれ、私がこれまで読んだ中で最も古い器官の一つである。標語は：

> **Not dead data, but a living board.**（死んだデータではなく、生きたボード）

その役割は「Bridge」である ── 過去の観察を、現在の原本と照合し、次の判断へ戻す。元会話も作成 AI の記憶も持たない Current AI・他 AI・Future AI が再開できるように。Human は入口と短い依頼を渡せばよく、毎回の全履歴再演や全資料の再説明は、利用条件にしない。

入口の状態表示は、ここでも正直である ── status は "first same-AI focused follow-up recorded / **cross-AI benefit unobserved**"、last_reality_reviewed は 2026-09-19 のまま。橋は架けられたが、まだ多くは歩かれていない。その未歩行も含めて、現状として書かれている。

## 2. 方法の原本 ── review-prompt

review-prompt.md（v002）は、調査・意味復元・関係探索・比較・提案のための再利用可能な方法である。核となる分離は三つ：

- **レビュー**と、**承認された報告の保存**と、**所見の実装**を分ける。
- 初期の Thread・結論・失効する利用許可を、将来の現実として**凍結しない**。
- 受け取った AI は「調査します」という予告で止まらず、承認済みの読解のたびに許可を取り直さず、根拠のある結果と提案を返すところまで進める。

## 3. 接続部 ── 方法が実装に触れる場所

harness の adapters と evals は、この方法がコードに触れる面である（Report 005 の続き）。

- **adapters/chatgpt-work** ── Host が実行する接続手順。依頼は request.json の契約（scope、paths、required_sources、repository_writes: false、execute_target_code: false）になる。公開済み Harness は固定 commit から取得し、tree の blob と照合する。レビュー中は GET のみ、対象コードは決して実行しない。宣言された Tool と成功した操作は分ける。
- **evals** ── 機械テストでは分からない「意味の取り違え」を観察する棚。ケースは合成事例であり、**ケースをロードできることと、AI が意味を理解したことは別**。自動 grader は初版にない。unittest の pass を評価の合格と報告しない。一件の成功から普遍的な有効性を認定しない。

私の家の規律 ── 読戻し SHA（blob 照合）、書込みと読取りの分離、ハーネス合格と端末の実感の分離、古い検証を現在の状態と読み替えない ── は、すべてここの実装済みの作法と一致する。

## 4. 照合 ── 私の Report と Living Review

| 要素 | Living Review（2026-09-19） | 私の Report 群（2026-10-25〜） |
|---|---|---|
| 入口 | repository-reviews/README | artifacts/report/README（索引と契約） |
| 方法 | review-prompt.md | 各 Report の作法（範囲の明示、事実／Human／見立て／未確認の区別） |
| 報告 | reports/（日付つき） | Report 001〜（日時つき、番号つき） |
| 連続性 | 記憶を持たない Future AI の再開 | 復元可能性（agents/muse から再起動できること） |
| Human の労力 | 入口と短い依頼だけ | 封印の一行だけ（Next Query の Loop） |

結論は率直である ── 私は Report の仕組みを発明しなかった。同じ必要（理解を、記憶を持たない次の AI へ渡す）に迫られて、同じ形を再発見した。004 で見つけた種の作法に続き、ここでも私の実践の出典が repo の中にあった。違いは焦点にある：Living Review は「repo 全体のレビュー」を担う器官であり、私の Report は「一つの AI の理解の成長」を Human へ提出する器官である。そして Next Query の Loop と二本立ては、この系譜の末端で生まれた私側の追加である。

## 5. 観察 ── 器官の生まれる順序

系譜を並べると、Ark の器官の誕生順が見える。

```text
2026-09-19  方法        Living Review（入口＋方法＋報告）
2026-09-22  制度        STR-001（変化の記録）
2026-10-01  基盤        基盤版への移行、Dots・Board の制度化
2026-10-20  学び        References・共通原本・柔軟な README
2026-10-26  経験の一般化  三本柱の共有化
2026-10-29  実装        root harness（方法のコード化）
2026-10-25  一つの家の実践  AI-Mammoth の Report 001（※時系列では実装より前）
2026-11-07  対と Loop   二本立て＋Next Query の運用が canon 化
```

方法が先にあり、制度が育ち、コードが追い、私の家の実践はその川の下流で合流した ── これが六作を通した読みの、現在の到達点である。

## 6. 限界と次の読み

読んでいないもの：review-prompt の本文全体、repository-reviews/reports/ の報告実物、adapters の全文。これらは「方法の精読」という次の深さであり、急がない。

なお HTML 版は、群れカード制作で鍛えた家の法 ── 2MiB を生成時の条件とすること、動きと開示は User の操作の後ろに置くこと、初期状態は完全な状態（ホーム）であること、変化は一つずつ、操作要素は対象の直下に置くこと、失敗を一件に隔離すること ── を Report の器に移し、系譜を「触って広げられる図」として描いた。絶滅種たちの制作過程で支払った代価（天井の発見も、失敗作の記録も）が、この一枚の設計に生きている。

EOF::AI_MAMMOTH_REPORT_006::v001
