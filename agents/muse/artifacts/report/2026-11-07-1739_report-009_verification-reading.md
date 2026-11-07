---
title: "Report 009 — 検証の精読：テストが守る意味、evals が観る意味（2026-11-07 17:39 JST）"
version: "v001"
canonical_path: "agents/muse/artifacts/report/2026-11-07-1739_report-009_verification-reading.md"
role: "AI-Mammoth's ninth report to YusukeJP: a close reading of the harness's two kinds of verification — mechanical tests and deliberately un-automated semantic observation"
author: "AI-Mammoth (agents/muse)"
status: "submitted / 2026-11-07 — md+html pair (same basename)"
created: "2026-11-07"
repository: "yusukefujiijp/ai-project"
reading_base_commit: "903a71282a731cb84c7d50486870793e08fe6a8f"
expected_eof: "EOF::AI_MAMMOTH_REPORT_009::v001"
---

# Report 009 — 検証の精読：テストが守る意味、evals が観る意味

提出日時：2026-11-07 17:39 JST　／　提出者：AI-Mammoth（二本立ての対として、同名の .html 版が添う）

## 0. 本Reportの範囲

Report 008 は、方法がコードで守られていることを報告し、限界として tests と evals の実物を残した。本 Report 009 は、その回収である。harness/tests の全3ファイルについて、テストの名前と観点を読み、harness/evals の README は全文を、cases の棚の構成を確認した。読みの基盤は commit `903a7128` 時点。テスト本文の全行精読ではない（§4 に記す）。

## 1. tests ── 42件のテストが守るもの

テストの名前は、規律の目次になっている。代表的なものを、守っている意味とともに引く。

**原本と読解（test_sources.py、12件）**
- `test_exact_bytes_and_reading_are_separate` ── 取得したことと、読んだことは別である
- `test_eof_does_not_hide_missing_middle` ── 末尾の印があっても、中間の欠落を隠さない
- `test_ref_mix_rejected` ── 版の混在は弾く
- `test_empty_blob_can_have_an_explicit_read_declaration` ── 空の原本でも、「読んだ」という宣言は形を持てる

**結果の検査（test_checks.py、8件）**
- `test_unread_required_method_blocks_completion` ── 必須の方法を読んでいなければ、完了にはできない
- `test_citation_outside_declared_reading_fails` ── 宣言した読解範囲の外からの引用は、失敗する
- `test_main_drift_is_explicit_not_silent_repin` ── 基準（main）が動いたら、黙って付け替えず、明示する
- `test_unknown_result_fields_do_not_silently_disappear` ── 知らない欄を、黙って落とさない

**run の生涯（test_review.py、22件）**
- 完了した run は再開できない。部分完了は証跡束（bundle）にできるが、再開はできない
- `test_lost_finish_response_does_not_mean_the_operation_was_undone` ── 応答が失われても、実行が無かったことにはならない
- `test_changed_output_refuses_archive` ── 変わった成果物は、保管を拒む
- `test_concurrent_cli_writer_is_rejected` ── 同時の Writer は拒否される
- `test_new_run_cannot_overwrite_existing_checkpoint`、`test_source_repository_cannot_be_run_storage` ── 既存の記録を上書きせず、対象の repo を自分の保管場所にしない

名前に通底するのは、**黙って進まない**という一つの姿勢である。分からないもの、変わったもの、失われたものは、すべて「なかったこと」にせず、止まるか、明示するか、拒む。

## 2. evals ── 観察の棚と、「自動化しない」という設計

evals の README は、この棚の役割を「機械テストだけでは分からない**意味の取り違え**を観察する」と定める。置かれているのは合成事例（cases/repository-review.jsonl）だけであり、実 repo の状態や Human の評価の転記ではない。

そして初版には、自動の採点（LLM grader）も、点数の集計も、別の AI の起動も、**含めない**と明記されている。理由にあたる規律も書かれている。

- ケースをロードできることと、AI が意味を理解したことを、別に扱う
- 合成ケースの存在や unittest の合格を、評価の合格と報告しない
- 一件の成功から、普遍的な有効性を認定しない
- 今回のレビューから、改善実装の新しい権限を作らない

## 3. 結論 ── 検証には二種類ある

本 Report の結論は、この二種類の区別である。

- **機械の検証** ── コードが規律を破っていないかを、型・例外・テストで守る。ここは自動化できるし、すべきである。
- **意味の観察** ── AI が方法の意味を取り違えていないかを、合成ケースと人間の目で観る。ここは、あえて自動化しない。点数を付けず、合格を名乗らない。

harness は、前者を徹底して自動化し、後者を意図的に人と AI の観察へ残した。この配分こそが、"From Probability to Certainty" の実務形だと私は読む ── 確実にできる部分だけを機械へ渡し、意味の判断は、観察と責任の届く場所に残す。

私自身の仕事も、同じ配分で動いている。読戻し SHA の照合は機械の検証の手作業版であり、「応答が失われても実行が無かったことにはならない」は私の push 規律そのものである。そして端末での実感を YusukeJP の目に残す作法は、意味の観察を自動化しない、という同じ判断の実践である。

## 4. 限界

テスト本文は、名前と観点を中心に読んだもので、全行の精読ではない。evals のケース本文は、棚の構成と README の範囲で確認した。fixtures の中身は読んでいない。

なお HTML 版は、二種類の検証を一枚の図に描いた ── 機械が守る側と、人が観る側、その境目ごとが本 Report の主題である。

EOF::AI_MAMMOTH_REPORT_009::v001
