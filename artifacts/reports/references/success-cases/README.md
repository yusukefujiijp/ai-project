---
title: "Report Success Cases — 成功の意味と条件を継ぐ"
canonical_path: "artifacts/reports/references/success-cases/README.md"
version: "v001"
created: "2026-10-26"
updated: "2026-10-26"
updated_reason: "Define a small JSONL case contract while retaining Human meaning, evidence, narrative depth and correction history."
role: "Report success selection, use and JSONL contract owner"
row_schema_version: 1
primary_reader: "Current AI / Future AI / Human review"
expected_eof: "EOF::REPORT_SUCCESS_CASES::v001"
---

# Report Success Cases

Reportの制作・伝達・保存・再利用でHumanが価値を認めた成功を、[success-cases.jsonl](success-cases.jsonl)に残す。成功の意味・喜び・背景・成立条件・根拠を次のAIへ渡し、現在の問いで何を生かせるかを考える。本文はJSONL内に置き、一件ごとのMarkdownを併設して二重管理しない。収録範囲と他の原本への分担は[親のReferences](../README.md)が所有する。

## 1. 成功を選び、読み直す

一件の単位は、独立して役立つ成功の意味である。小さな工夫、部分的成功、設計案への評価も扱え、長期再現性の実証を保存の前提にしない。Humanの評価と対象、確認済みの出来事、AIの解釈、未確認を読み分けられるようにする。計画への好評価を実利用効果へ、保存を他AIの理解へ昇格させない。

現在の目的・読者・条件に関係する事例と根拠を選んで読む。成功原因を唯一の説明に固定せず、重要なCorrectionと成立条件を保って転用可能性を検討する。利用時の毎回全件読込は求めない。全体共有の成功事例群は[その担当原本](../../../../references/success-cases/README.md)に残り、このJSONLへ自動移設・同期しない。

## 2. 行形式 — case schema 1

UTF-8のJSON Linesとし、一つの物理行に一つのcase objectを置く。行区切りはLF、非空ファイルは末尾LFを持つ。0件は0バイトの空ファイルで表す。空行、BOM、管理用header、配列の外枠、行間カンマ、Markdown fence、EOF sentinelはデータに入れない。

必須fieldは次の六つ。内容の章数・長さ・固定ラベルを定めるものではない。

- `schema_version`：整数`1`。このcase行形式の互換性の版であり、更新回数やlessonsのschema 2とは別。
- `id`：新規は小文字・hyphen付きUUID v4。訂正で付け直さず、別事例への意図的な再利用をしない。
- `created_at`／`updated_at`：有効なUTC日時`YYYY-MM-DDTHH:mm:ssZ`。実際の登録・意味更新を表し、出来事の日時と分ける。初回は同値、更新時はcreated_atを保持し、updated_atはcreated_at以降とする。
- `case`：非空の自然言語文字列。何が成功し、なぜHumanに重要で、どの条件・根拠があり、どこが解釈・未確認かを十分に記す。逐語引用と編集要約を区別し、一物理行を一文への短縮と取り違えない。本文内の改行等はJSON escapeする。
- `sources`：一件以上のobject配列。各要素に非空文字列の`locator`と`supports`を持つ。locatorは根拠の所在・節・版、supportsは何を誰の観測として支えるかを示す。過去状態が重要なら固定commit等へ戻る。公開URLでない会話の所在説明はその性質を明示し、架空のURL・message ID・日時を作らない。相対パスはこのJSONLの位置から解決する。

`title`や`caveat`を必要な場合に非空文字列で加えられる。未知field・ネスト値・配列順は保持し、既知項目だけで再生成しない。外形を小さくそろえ、自然言語・Humanの言葉・比喩など意味を担う本文は目的に合わせて残す。固定タグ、採点、独立schemaファイルは設けない。

## 3. 同じ事例を育て、安全に保存する

同じ事例の訂正は同じIDの現行行を更新し、同一IDを追記して最後を最新版とする方式にしない。更新前の内容はGit履歴で辿り、本文でも当時の事実・評価と後の解釈を区別する。統合・整理は意味と根拠への到達性、旧IDの扱い、変更理由を保持する。全Feedbackの収録や、lessonとの必須二重登録を求めない。

更新前にRemoteの全文とrevisionを取得し、LFだけで区切って全行を検査する。空行・CRLF・末尾LF欠落・不正JSON・object以外・重複key・NaN／Infinity・不正型や日時・不正sources・重複IDを拒否する。未知schemaや壊れた入力を空データへ置き換えない。一行丸ごとの消失は構文だけでは分からないため、基準revision・内容・期待件数も照合する。

意味編集後に再検査し、読取revisionを条件に非forceで保存して、Remote全文とSHA／commitを照合する。同じファイルへの変更は一人の統合担当が扱い、競合時は最新内容を読んで並行変更を保持する。配置・保存後確認は[Artifact → GitHub](../../../../prompts/artifact-to-github.md)に従う。

送信前に選んだID・意図した本文・基準revisionを復旧時に照合できる形で保つ。Timeout等ではRemoteと履歴から実際の結果を確認し、同じID・内容が保存済みなら二重登録しない。IDがないことだけで再追加せず、保存後の削除・統合と未保存を区別する。復元できない操作は保留し、新IDでの盲目的再送はしない。

Root・HumanのCorrection／STOP・適用Guard・公開範囲は[親のReferences](../README.md)と[AGENTS](../../../../AGENTS.md)に従う。文書整合、保存、他AIの理解、実際の再利用、長期効果は別々に扱う。記録や形式は新しい実行権限ではない。

EOF::REPORT_SUCCESS_CASES::v001
