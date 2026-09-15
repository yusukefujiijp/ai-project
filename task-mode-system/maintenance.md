---
title: "Task Mode System — 根拠を保って改訂する"
version: "0.1.0"
status: "human-authorized prototype"
role: "Ownership and revision guidance"
canonical_path: "task-mode-system/maintenance.md"
created: "2026-09-15"
updated: "2026-09-15"
expected_eof: "EOF::TASK_MODE_SYSTEM_MAINTENANCE::v0.1.0"
---

# 根拠を保って改訂する

## 1. 権限と責務

Current Humanの依頼・訂正・承認Scope、適用Runtimeと[AGENTS.md](../AGENTS.md)に従う。Plan-only／STOPを保持し、実行が承認されている場合は必要な作成・検証・保存確認まで完了する。同じ承認を毎回取り直さず、過去の引用を新しい操作の許可にも変えない。

この文書は既存の[Task Records共有ガイド](../formats/task-records/README.md)の所有権・改訂規則を、このSystemへ接続する。Schema、Root、ThreadのHandoffやStateを独自に再定義しない。

## 2. 何をどこへ戻すか

- **過去の出来事への補足・訂正**：その経験が報告されたThreadの原本へ戻す。後日の発言元は新しいThreadと明記する。
- **現在のThreadで新しく起きたこと**：現在のThreadの経験原本へ追加する。前Threadの原本をコピーしない。
- **報告欄・候補の変更**：`interfaces/`の対象フォームへ。理由となったHuman Feedbackは該当経験原本へ残す。
- **共通の協働原則**：`operation.md`へ。個別場面だけの条件を全Task共通規則へ広げない。
- **B-Gate対応条件**：`responses/b-gate.md`へ。形成経緯・根拠・反例が変わる場合は該当説明と索引も更新する。
- **形成経緯・案内**：`experience/formation.md`と`experience/README.md`へ。ここを第二のTask状態原本にしない。
- **記録構造・Evidenceの意味**：共有ガイドと対応Schemaへ。実際に必要な形式改訂として扱う。
- **実際のThread移行**：[共通移行契約](../prompts/ai-next-thread-handoff.md)、利用可能な[移行準備Skillの共有本文](../skills/prepare-ark-transition/SKILL.md)、Current Handoffを使う。このフォルダに別の移行成立条件を作らない。

新しいHuman Realityを理解したことと、Repositoryへ反映済みであることを区別する。経験追加はThreadのState更新を自動的に意味しない。

## 3. 経験原本の改訂

同じ出来事を訂正する場合、意味が同じIDを保持し、Sourceと変更理由を追加する。別実行を同じIDへ上書きしない。以前の時点が正しかった場合、後の変化は必ずしも`corrects`ではない。

`revision`と`updated`を進め、旧説明・時点・新しい根拠を追えるようにする。`created`はTask発生日ではなく記録作成日である。発言の日時やtimezoneが不明なら推測で埋めない。

Sourceの逐語引用は連続した原文を保つ。空白の正規化、抜粋をつないだ再構成、要約は編集であることを明示し、`paraphrase`で扱う。存在しない会話URLや外部メッセージIDを作らない。

一つのNodeにHuman報告、AI仮説、未確認を混ぜない。採用した方針の確認は、方針の実行や効果の確認ではない。`source_refs`、Edgeの両端、未確認事項の対象を検査する。

03原本で用いる`source_context.extensions.record_cutoff`は収録の終端、`governance`はRuntimeとの責務、`extensions.revision_history`は改訂理由、`coverage_review`は収録範囲とSourceの対応である。Coreの意味は変えない。

## 4. 文書の版と採用状態

このSystemの文書版`0.1.0`、経験JSONの`revision`、記録形式の`v001`、共有ガイドの版は別である。文書の版を進めてもSchemaの意味は変わらない。

各文書のrole・canonical_path・version・status・updatedと、必要な変更理由を整合させる。初期実装への承認を、全提案の普遍的正しさと扱わない。設計候補、採用、実装、応答確認、実生活の効果を必要な箇所で区別する。

軽微な表現修正に全資料の再設計を課さない。意味を変える変更では、依存する説明・フォーム・検証ケースを点検する。非互換のSchema変更が必要なら新しい版を追加し、既存v001の意味を黙って書き換えない。

## 5. GitHub更新と検証

1. 対象repository／ref／pathと承認Scopeを確認し、Current本文・Blob・適用指示を読む。
2. CREATE／UPDATE／NO_CHANGEを判断する。他者の変更を保持し、同じ対象へ並行書込みをしない。
3. 対象文書・記録を作成し、[構造と意味の確認](validation.md)を行う。
4. 承認された方法で保存する。複数ファイルを一つの整合した変更として扱う場合も、対象外を保持する。
5. Remoteから変更対象を再取得し、本文・参照・EOF・SHAまたはcommitを確認する。
6. 達成部分、重要な未確認、変更前からの差分を返す。UI、別AI、実生活の未観測成功は加えない。

競合があれば最新内容と差を読み、必要な調整をする。自動承認やToolの拒否を別経路で迂回しない。止める場合は対象操作と最小の再開条件を示す。

## 6. フォルダの独立性と将来の配布

この版は専用入口と正本参照で構成する。フォルダ単体のオフライン完全復元は未実装である。

将来、読み取り専用の配布Snapshotを採用する場合は、編集可能な正本、配布版、対象commit／blob、収録範囲、相対参照、更新先、配布物の再生成方法を定義する。共有ガイドの「継承のためだけに原本を複製しない」という方針との関係も、明示的な設計判断として扱う。今の本文をコピー例外の成立済み承認にしない。

新しいフォルダ、専用Skill、選択UI、自動化、実行エンジンは、具体的な利用上の不足とCurrent Requestに基づいて検討する。ファイル数の増加そのものをSystem完成と扱わない。

EOF::TASK_MODE_SYSTEM_MAINTENANCE::v0.1.0
