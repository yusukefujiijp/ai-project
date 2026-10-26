---
title: "Report References — 経験を、次の制作と利用へ"
canonical_path: "artifacts/reports/references/README.md"
version: "v003"
created: "2026-10-26"
updated: "2026-10-26"
updated_reason: "Connect child guides to shared feedback and case contracts while retaining completed Report data and formation history."
role: "Report learning scope and owner routing; children connect to shared data contracts"
primary_reader: "Current AI / Future AI / Human review"
validation_boundary: "Structure and persistence are distinct from reader understanding and sustained practical effects"
expected_eof: "EOF::REPORT_REFERENCES::v003"
---

# Report References

Reportの執筆・構成・読者への伝達・保存・再利用で得た反応と学びを、現在と将来のAIが次の判断へ生かす入口。Humanも意味と根拠を確認・訂正できる自然言語を保つ。作品の所在と読者への入口は[Reports](../README.md)が所有し、ここでは日付をまたいで使う学びを扱う。

## 1. 現在の問いから読む

- [feedback](feedback/README.md)：対象と文脈を保った反応・評価・希望・訂正。本文は[feedback.jsonl](feedback/feedback.jsonl)。まだ教訓へ整理していない反応も読み直せる。
- [lessons](lessons/README.md)：FeedbackやCorrectionから得た、条件付きの再利用判断。本文は[lessons.jsonl](lessons/lessons.jsonl)。
- [success-cases](success-cases/README.md)：Humanが価値を認めた成功の意味・形成経緯・成立条件・根拠。本文は[success-cases.jsonl](success-cases/success-cases.jsonl)。

Reportを作る・改訂する・保存する時や、説明の受け取られ方を見直す時に、今回の判断へ関係する記録と後続の訂正を読む。現在のGoal・読者・素材・制約と比較し、何を使い、どこを調整し、何が未確認かを判断する。利用時の毎回全件読込や、Humanによる過去の指摘の再説明を前提にしない。同一性を確認できる読解は適用契約の範囲で再利用し、更新前には対象の全文と版を確認する。取得不能と記録なしを区別する。

## 2. Feedbackの戻し先を選ぶ

反応そのものを残す価値がある場合は、対象・原文または編集要約・出典を区別してfeedbackへ置く。教訓化や成功認定を保存の条件にせず、未加工の記録を未処理Taskへ変えない。

一作品の誤り・説明不足はそのReportへ戻す。別のReportにも役立つ判断はlessonの候補、選び出す価値のある成功はsuccess-caseの候補として、既存内容との重複と固有条件を確かめる。Feedbackの件数を記録数・Task数へ変換せず、既存記録の訂正・統合・変更なしも選べる。

feedbackは根拠となる反応、lessonsは条件付きの再利用判断、success-casesは成功の意味を所有する。必要な記録のID・出典を参照して結び、三本への必須登録や全文の同期コピーは作らない。lessonや成功事例は既存の適切な根拠から直接育てることもでき、Feedback登録をすべての学習の必須前工程にしない。

lessonsとsuccess-casesは排他的な失敗／成功分類ではない。一つの経験が両方へ関係しても、再利用判断と成功の意味に独立した価値がある場合に必要な参照で結ぶ。

Reportが扱う題材の事実・経験・現在状態は、その領域の担当原本へ戻る。領域を越える一般的な学びは[共有References](../../../references/README.md)との分担を確認する。同じ意味をここへ再登録せず、Report固有の条件が必要な部分を所有する。共通Skillの方法を改訂する場合も、その担当原本と現在の承認範囲に従う。ここを全会話の保管庫、全分野の知識庫、第二のCurrentやSkill原本にしない。

## 3. 意味と更新の責任

このREADMEは収録範囲・読む場面・所有先の選択を、子READMEはReport固有の利用条件と共有形式・更新契約への接続を、JSONLは反応・判断・成功の本文を所有する。Reportの内容・読者・保存方法の現行規則を、複数の場所へ独立して定義しない。JSONLを選んだことから、作品自体の読者がAI専用になったとは判断しない。

Humanの報告・評価、直接確認した結果、AIの解釈、未確認を分ける。過去の承認を現在の実行許可にせず、読取・保存・別AIの理解・実利用効果を別々に扱う。権限と公開範囲は[AGENTS](../../../AGENTS.md)、配置とRemote再取得は[Artifact → GitHub](../../../prompts/artifact-to-github.md)に従う。私的Workや長期メモリを転記・同期せず、今回承認された公開可能な形成内容だけを扱う。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah。HumanのMeaning・Correction・STOPと適用Guardを保持し、AI・Report・学びはKeliとして扱う。

## 4. 初版の形成

Humanがこの場所にREADME・lessons.jsonl・success-cases.jsonlの改行のみのSeedを用意し、フォルダ分離、schemaの要否、成功事例本文のJSONL化を問い直した。[整備前の固定版](https://github.com/yusukefujiijp/ai-project/tree/7903d8d34d0d5977657f510edeaf729f3b35a2ae/artifacts/reports/references)に戻れる。

Ark28:07でのLiving ReviewとPlan Modeを経て、Report入口とこの配下の一組を整える実行が承認された。二つのデータファイルを子フォルダへ移し、初期のlessonと成功事例を記録する。独立schemaファイル、全体共有事例の一括変換、Skill改訂、自動収録はこの整備に含めない。採用・配置の成立を、全AIへの自動読込や長期効果の証明にはしない。

## 5. Feedback原本の追加

2026-10-26、HumanがFeedbackの独立保存と三本柱の分担を問い直し、Plan Modeで提示した四ファイルの整備と直近二件のFeedback保存を承認した。表現形式・調査範囲への反応と、初回Reportの内容評価・読書体験への反応を原文で収録する。既存のlesson・成功事例と作品本文は保持し、番号付け・HTML化・Skillや設定の変更へは広げない。保存された反応からの学習と実際の改善は、今後の利用で別に確かめる。

## 6. 共有契約との接続

2026-10-26、共有Referencesの三本柱化に合わせ、Feedbackとsuccess-caseの汎用的な読取・行形式・更新契約を共有側へ接続した。Report固有の対象と初期記録は保持し、二件のFeedback・一件のlesson・一件の成功事例を再登録していない。今回の整合と検証は[STR-023](../../../control-center/changes/STR-023-shared-references-three-pillars.md)へ戻る。

EOF::REPORT_REFERENCES::v003
