---
title: "Codex Runtime — 確認した条件と再開時の判断"
canonical_path: "agents/codex/runtime.md"
version: "v001"
created: "2026-10-31"
updated: "2026-10-31"
date_basis: "UTC; activity records use their own Asia/Tokyo placement contract"
role: "Codex environment evidence and resumption routing; shared methods retain their own originals"
expected_eof: "EOF::ARK_CODEX_RUNTIME::v001"
---

# Codexの実行条件

この文書は、Codexの次の仕事で何を確認し、どの原本へ戻るかを案内する。初版の資料照合はUTC 2026-10-31、基準mainは`673cdc2776a21e47f048fc544dbadd8f76c58fe2`。過去に成立した経路と、今回実際に確認した環境を区別する。時刻が新しい文書へ転記したことだけで、過去の観測が再試験済みになるわけではない。

## 確認範囲

| 対象 | 確認したこと | 境界と原本 |
|---|---|---|
| GitHub資料へのアクセス | この初版作業ではGitHub Pluginの公開された読取ツールで対象main・本文・blobを照合した | 保存結果は[STR-025](../../control-center/changes/STR-025-codex-home-and-reference-pillars.md)とGit履歴が所有。ツールの存在だけで任意のRepositoryへの権限を推定しない |
| ChatGPT接続 | 既存の[接続README固定版](https://github.com/yusukefujiijp/ai-project/blob/673cdc2776a21e47f048fc544dbadd8f76c58fe2/skills/connect-chatgpt/README.md)に、同じ保存プロフィールでHumanの再ログインなしに本人一致・会話一覧到達を確認した実行がある | 今回はブラウザを開いておらず、現在のセッション有効性は未確認。実績詳細と現行の個別案内は[接続README](https://github.com/yusukefujiijp/ai-project/blob/main/skills/connect-chatgpt/README.md)が所有 |
| ローカルCodexへのSkill導入・発見 | 上記固定版には、導入ファイルの照合と新しいローカルCodexプロセスの`skills/list`による発見が記録されている | 当時の実行環境での観測。クラウド会話の個人Skill登録や新規Threadの自然選択を実証したものではない |
| 環境を跨ぐ利用・長期安定性 | この初版では新たな確認をしていない | 同じ接続・プロフィールが利用可能か、その環境で確認する。期限や完全無人復帰を推測しない |

当時の保存プロフィールの識別・本人照合・再認証の扱いは[connect-chatgptの手順](https://github.com/yusukefujiijp/ai-project/blob/main/skills/connect-chatgpt/SKILL.md)が所有する。ここへプロフィール情報や手順全文を再定義しない。認証情報や期限付き設定URLを保存しない。

## 再開する場面

接続を依頼されたら、現在使える正規の道具と対象環境を確かめ、共有Skillへ進む。既知の条件を再利用し、欠けている接続・本人確認だけを解決する。Skillが利用環境で発見できない場合も、共有原本を読めることと登録済みであることを区別する。

プロフィール情報と実際の画面が食い違う時は、[プロフィールの学び](references/lessons/README.md)へ。ローカル導入の成功からクラウドでの利用を期待している時は、同じ入口の環境別発見の学びへ進む。今回の依頼が読取・計画限定なら、ブラウザ接続や設定変更は開始しない。

## 新しい結果が分かったら

- Codex全体の実行環境・使える経路の変化は、この文書の該当箇所へ確認環境・時点・根拠とともに反映する。
- connect-chatgpt固有の方法・導入・接続結果の詳細は、その共有SkillとREADMEへ戻す。本書は必要な参照と今回への意味を更新する。
- 条件付きの判断は[lessons](references/lessons/README.md)、Humanの反応は[feedback](references/feedback/README.md)、価値ある成功は[success-cases](references/success-cases/README.md)の所有関係を確認する。

いずれも現在の保存承認の範囲で行う。この記録から追加試験・再認証・自動運用の権限を作らない。

EOF::ARK_CODEX_RUNTIME::v001
