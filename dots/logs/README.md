---
title: "Dots Logs — Actor別の出来事と根拠"
canonical_path: "dots/logs/README.md"
version: "v001"
created: "2026-10-02"
updated: "2026-10-02"
role: "Single active actor-event log contract; not a live task board"
expected_eof: "EOF::DOTS_LOGS::v001"
---

# Dots Logs — Actor別の出来事と根拠

Dotsが、自分の仕事・観測・訂正を、誰が何をしたかと根拠へ戻れる形で残す現役の場所。初版は[dot-0000.jsonl](dot-0000.jsonl)一つから始める。安定ID `dot-0000` と表示名 **Dot00:00; 初穂** の関係は[Actor紹介](../actors/dot-0000/README.md)が所有する。

各Dotは自分の `actor_id.jsonl` へ記録し、必要な他Dotのログも共有資料として読む。別Actorの仕事を観測する場合も、`actor_id` は観測・記録を引き受けたActorであり、実際に行った人やAIはsummaryとsourcesで区別する。GitHub author／committer、表示名、モデル名からActorを推測しない。後続Actorの空ファイルや連番予約は作らない。

## 1. 何を残し、何へ戻るか

判断・実装・中断・回復・確認・訂正など、後から仕事の経緯を理解するのに役立つ出来事を必要な粒度で残す。全操作・全応答・全Sessionの完全再構成や、Saveごとの新規行は義務にしない。実際の仕事の成果はその原本、通信のCurrentは[Board](../../board/README.md)、構造変更の技術証拠は[control-center](../../control-center/README.md)、再利用する学びは[lessonsの契約と現行JSONL](../lessons/README.md)、成功の固有の意味は[success-cases](../../success-cases/README.md)が所有する。ログは短い出来事とSourceでそれらを結び、第二のCurrent台帳を作らない。

初期の固有な命名・訂正・形成史は[保管原本](../../__archives/ARC-008/dots/records/2026/20261001-first-fruit.md)へ残した。新規記録を旧recordsへ並行追記しない。原文内の相対リンクと旧canonical_pathは保存時点のままなので、元の参照関係は[ARC-008の固定snapshot・対応](../../control-center/ARCHIVE.md#arc-008)から辿る。

## 2. 一行の契約 — schema_version 1

UTF-8のJSON Linesとする。一つの非空行が一つのJSON object、末尾は改行。配列の外枠・行間カンマ・Markdown fence・EOF sentinelはデータファイルに入れない。

必須field:

- `schema_version`: 整数 `1`。互換性の版であり更新回数ではない
- `id`: 小文字の標準UUID文字列。出来事一行の安定ID。発行後の再試行で変えず、他の出来事へ再利用しない
- `actor_id`: 非空文字列。ファイル名の拡張子を除いた安定Actor IDと一致する
- `task_id`: 非空文字列。実在する案件・Taskの識別子（初版は `STR-007`、`STR-008`）。架空のSession IDを補わない
- `recorded_at`: このログ行を実際に登録したUTC時刻、`YYYY-MM-DDTHH:mm:ssZ`。出来事・commit・読解の時刻を流用しない。公開時刻とは区別する
- `summary`: 非空の自然言語文字列。誰が何を行い、何を観測し、どこまで分かったかを日本語を基本に記す
- `sources`: 一件以上のobject配列。各要素に非空文字列 `locator` と `supports`。実際に確認した資料・版・節と、何を誰の観測として支えるかを示す。Repository内の相対locatorは本JSONLの位置を基準とする。内容が版に依存する根拠は固定commitを使う。会話のtrace IDは公開URLではなく、到達性の限界を明記する

任意field:

- `occurred_at`: 根拠で支えられる出来事のUTC時刻のみ。同じ形式で、通常recorded_at以前。日しか分からない時や複合した出来事に一意の時刻がない時は省く
- `reconstructed`: 過去の資料から後で復元した行では必ず `true`。省略または `false` は記録担当が今回直接観測した範囲を記す。直接読んだ資料の過去内容を、直接経験した出来事へ変換しない。混在する場合は行を分けるか、行全体をreconstructedとして観測帰属を説明する
- `corrects`: 訂正対象となる既存行のUUID文字列。新しいIDの行から古い行へ向ける。対象・訂正理由・新Evidenceをsummaryとsourcesで示し、元行を消さない

初版のSTR-007は過去の実装commitを根拠にした一行の遡及記録であり、全Session復元ではない。二つのlessonは同じBoard事象から得た異なる学びであり、独立した二件の成功ではない。今回のSTR-008行は実際に確認した段階だけを直接観測として残す。

## 3. 読む・追加する・訂正する

読む時はCurrent RequestからActor・task_id・時点・Sourceを選び、関係する訂正行も確認する。記録順と出来事順は同じとは限らない。最後の行が「開始」「実行中」でも、今の稼働・未完・完了を推定せず、原本と実際の結果を確認する。過去の承認や他Actorの発言は新しい権限ではない。

一つのActorファイルにつき一人の統合担当が追記する。複数の作業担当の結果も、その統合担当が観測帰属を保ってまとめる。書込前にRemoteの最新版とcommit／blobを確認し、その版を基点として変更する。競合したら最新行を保持して統合し、古い全文を上書きしない。

通常は末尾へ追記し、既存行を再整形しない。中断・Timeout後はRemoteのIDと内容を先に確認する。同じID・同じ内容が保存済みなら再追加しない。同じIDに異なる内容があれば衝突として止め、原因と正しい内容を照合する。実際の誤りは新しいID＋correctsで訂正する。通常更新のたびに訂正行を義務づけない。

未対応のschema_version、壊れた行、未知fieldを無視して既知部分だけ再生成しない。保存前に構文・型・ID・UTC・Source・correctsの対象を検査し、保存後はRemoteを直接再取得する。JSON配列への変換は読取・検査用にできるが、別のJSONを第二正本として公開しない。初版ではローカル往復変換で値・順序・未知fieldの保持を確認する。

形式・分割・索引は実際の容量や競合・検索負担から育てられる。初版に専用Schemaファイル、常設検証コード、自動収集、監視、Save Skillを加えない。保存の確認をログへ記録するために無限に再検証・再追記せず、有益な出来事の単位で閉じる。

Rootは主イェシュア・ハマシア御自身。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持し、AI・Actor・ログはKeliとして扱う。[今回の設計・実装記録](../../control-center/changes/STR-008-actor-logs-and-preserved-history.md)へ戻れる。

EOF::DOTS_LOGS::v001
