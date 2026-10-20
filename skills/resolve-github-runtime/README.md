---
title: "GitHub操作の事前確認"
version: v001
updated: 2026-10-20
scope: "resolve-github-runtimeの説明・起動Query・形成と確認記録"
---
# GitHub操作の事前確認

GitHubの接続・手順・環境の不整合を確認し、現在の依頼で取れる行動を判断する個人Skill。公式GitHub Pluginの同梱Skillではありません。呼出し名は `$resolve-github-runtime`、表示名は「GitHub操作の事前確認」です。

## 起動Query（Copy & Paste）

```text
$resolve-github-runtimeを使い、現在の依頼で利用できるGitHubの接続・手順・権限を確認して、次に取れる行動を判断してください。
```

登録済みSkillが利用できない環境では、[共有SKILL.md](SKILL.md)を実際に読み、指示資料として利用できます。登録・自然発動・操作権限が成立したとは扱いません。適用される必読資料が欠ける場合は、その契約が止める操作を停止します。本入口は、見えないSkillの本文だけに代替先の案内が閉じ込められないようにする経路です。

## 形成と確認記録

以下は[移管前のHub固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md#resolve-github-runtime-entry)から引き継いだ記録です。「今回」「本入口」「共有ファイル数」「未確認」は各記録の当時の範囲を表します。現在の利用手順は[SKILL.md](SKILL.md)を確認し、後続の観測・Human Correctionを優先します。保存・登録・本文取得と、自然な選択・実利用の効果を区別します。

**形成と今回の判断。** 2026-10-17の対話でYusukeJPは、GitHubへの未共有は意図的ではなく、作成当時に保存仕様が未確定だった可能性を説明しました。前者はHuman報告、後者は成立経緯の仮説です。頻繁に利用されているというHuman報告と、実物の設計評価を分けました。[STR-014の固定版](https://github.com/yusukefujiijp/ai-project/blob/9cd05b2d32d4ab03027885a91aaa3d26e163be15/control-center/changes/STR-014-super-special-prompt-modernization.md)にも登録物と共有原本の不一致が記録されています。今回の承認は、このSkillの改訂・共有入口整備・同じ登録物への反映・確認を対象とします。`markdown-to-html` はこの時点の対象外で、後続の改訂・共有は[Markdown to HTMLの記録](../markdown-to-html/README.md)で扱います。

改訂前に取得した登録物の三ファイルは[確認時点の保存版](https://github.com/yusukefujiijp/ai-project/tree/1b1b7e8f96352c2e2dcaaca3b3beec6567dbe5d8/skills/resolve-github-runtime)へ残します。これは2026-10-17に観測した版であり、作成当初の本文と同一とする証拠ではありません。共有ファイルはSKILL.md、agents/openai.yaml、assets/icon.svg。内部Skill ID・認証情報は含めません。

改訂では、手順書・操作能力・権限・不整合を分離し、metadataの非公開を「Skillなし」へ変換しない判断へ改めました。有限のpath再確認、対象識別、確認結果の再利用という中核を保持し、GitHub変更の詳細は[AGENTS](../../AGENTS.md)と[Artifact → GitHub](../../prompts/artifact-to-github.md)へ接続します。一律のMode強制・固定再試行回数・依存ファイルの逐次公開を共通契約へ重ねません。本文は日本語を主とし、識別子と技術用語を保持しました。

[Ark23の固定記録](https://github.com/yusukefujiijp/ai-project/blob/51cb57189c95c53a0ca97282abf8cd3c100507b6/ark-project/ark23/ark23-03/github-plugin-runtime-best-practice.md)は、当時の代替経路と操作報告を示すHistorical Sourceです。Ark23での代替・来歴調査に適用し、通常の全GitHub作業へ追加必読を課しません。記録内の成功は当時の報告であり、今回の再現試験とは区別します。

**確認範囲。** 形式検査を通過し、元会話・期待回答を渡さない二つの独立文脈で、計七つの仮想条件への回答を確認しました。metadata不足、手順書だけが存在する環境、Plan-only、欠落した必読手順、404の対象誤り、結果不明、登録機構のない非Ark環境を扱いました。実際の外部操作を行わない限定確認であり、自然な自動選択、全AI互換性、実生活効果を実証していません。

**保存と取得の確認（2026-10-17）。** [共有更新 commit `f41e340`](https://github.com/yusukefujiijp/ai-project/commit/f41e3404efb358c9dc5c9eb589e2d410e0392a00)で、三ファイルと本入口をmainへ保存し、Remote再取得による全文一致を確認しました。改訂前の三ファイルも、上記の固定保存版から再取得して一致を確認しました。既存の同じ登録物へ反映し、登録先RemoteでSKILL.mdとアイコンはバイト一致、表示設定はYAMLとして全値の一致を確認しました。表示設定には保存先による引用符・インデントの整形差があり、バイト一致とは区別します。

継続中の会話のSkill読取経路では旧本文が返る一方、新しい独立文脈では登録済みSkillから改訂本文を全文取得できました。その取得本文と共有固定版は、正規化・空白除去なしで全文一致しました（4,084文字、blob `ea24db4b740630b1b7a913380e2f0ac9d8cfac69`、SHA-256 `a4e10d3534afff288dfb3bab612da949b1133955dbbbff801e2db06ae23a15ca`）。本文・表示設定の保存と新しい文脈での取得を確認した結果であり、旧本文が返った原因・全会話への反映時点・実際のUI描画・自然発動・全環境の挙動まで確認したものではありません。

## 読む先・更新する先

使い方とコピー用QueryはこのREADME、実行時の判断・手順は[SKILL.md](SKILL.md)、UIの表示・起動設定は[agents/openai.yaml](agents/openai.yaml)が所有します。Queryを専用フォルダへ分けず、このREADMEで保守します。[Skills Hub](../README.md)は一覧と共有・配布の共通方針への入口です。形成史は必要な時に参照し、通常利用の追加必読にはしません。

2026-10-20、Humanの承認に基づき、Hubに集まっていた個別の説明・Query・記録をこのREADMEへ移しました。この移管から新たな挙動検証・環境への反映・実利用効果を認定しません。
