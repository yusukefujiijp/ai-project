---
title: "GitHubのPPTXをiPhoneの共有から見る"
version: "v001"
created: "2026-10-24"
updated: "2026-10-24"
date_timezone: "Asia/Tokyo"
status: "手順の机上確認・URL変換を検査済み / iPhoneへの組立・共有入力の実機確認は未実施"
expected_eof: "EOF::GITHUB_PPTX_IPHONE_SHORTCUT::v001"
---

# GitHubのPPTXをiPhoneの共有から見る

**一度だけ「スライドを見る」を作り、普段はGitHubのPPTX画面で「共有…」→「スライドを見る」。** URLの手作業での書き換えは不要になる構成。共有が合わない時は、同じショートカットを直接起動してURLを貼る。

今すぐ作品を見たい時は、[閲覧テストのスライドを開く](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fyusukefujiijp%2Fai-project%2Fmain%2Fartifacts%2Fslides%2Fslide-viewing-test%2Fslide-viewing-test.pptx)。この直リンクにショートカットの導入は不要。

## 今回の対応範囲

公開GitHubの `main` に置いた `.pptx` 一件を対象にする。GitHubアプリが共有するファイルページURL、GitHubのrawリンク、raw.githubusercontent.comの直接URLを同じ処理へつなぐ。複数URLを渡した場合は最初の一件だけを使う。

ファイルはGitHubに置いたまま、MicrosoftのWeb Viewerで表示する。ChatGPTログインは閲覧経路に含まれない。Microsoftが取得できる公開URLが必要で、private repositoryや期限付きの認証URLは対象外。別branch、slashを含むref、特殊な共有形式、日本語・空白を含むファイル名の端末上の変換は、この初版の実機保証に含めない。既に閲覧用URLなら、そのリンクを直接開けばよい。

この文書は実際に組める設定手順であり、インストール済みショートカットやiCloud追加リンクではない。作成環境にはAppleのShortcuts署名CLIとiPhone操作機能がないため、最初の組み立てと端末確認はiPhoneで行う。未署名ファイルを配って導入済みと扱わない。

## 一度だけ設定する

1. iPhoneの「ショートカット」で新規作成し、名前を **スライドを見る** にする。
2. 詳細で **共有シートに表示** をオンにする。
3. 先頭の受け取り設定を **URL・テキスト** にする。
4. **入力がない場合 → 入力を要求 → テキスト** にする。これで直接起動した場合も、コピーしたURLを貼って同じ処理を使える。

以下のアクションを順に追加する。日本語の表示名はiOSの版で多少変わり得るため、括弧内の英語名も検索の手掛かりにする。角括弧の変数名は文字として打たず、アクションの出力を変数として挿入する。

1. **入力からURLを取得（Get URLs from Input）**：入力を「ショートカットの入力」にする。
2. **リストから項目を取得（Get Item from List）**：1のURL一覧から「最初の項目」。
3. **テキストを置き換え（Replace Text）**：2の出力を対象に、下の検索文字列と置換文字列を設定する。**正規表現をオン**にする。

検索文字列：

```text
\Ahttps://github\.com/([^/]+)/([^/]+)/(?:blob/|raw/(?:refs/heads/)?)(main/)
```

置換文字列：

```text
https://raw.githubusercontent.com/$1/$2/$3
```

4. **テキストを照合（Match Text）**：3の結果から、次に一致する部分を取得する。直接PPTXだけを選び、末尾の `?raw=true` や `#...` は除く。

```text
\Ahttps://raw\.githubusercontent\.com/[^/?#\s]+/[^/?#\s]+/main/[^?#\s]+(?i:\.pptx)(?=[?#]|\z)
```

5. **もし（If）**：4の「一致」に **値がある** 場合に、次の6〜9を置く。
6. **テキスト（Text）**：内容を4の「一致」の変数だけにする。URL型のまま渡さず、エンコード対象の文字列にする。
7. **URLエンコード（URL Encode）**：6のテキストを「エンコード」。
8. **テキスト（Text）**：下の固定部分に、7の出力を改行なしで続ける。

```text
https://view.officeapps.live.com/op/view.aspx?src=
```

完成形は `固定部分[URLエンコードの出力]`。固定部分全体を再度エンコードしない。元のパス内の `%20` などが `src` 内では `%2520` になることは、二重誤変換とは限らない。`src` を一度復号すると正しい直接URLに戻ることを確認する。

9. **URLを開く（Open URLs）**：8のテキストを開く。
10. 5の **その他の場合（Otherwise）** に **アラートを表示（Show Alert）** を置き、「公開GitHubのmainにあるPPTXのURLを1件共有してください。」と表示する。ここではブラウザを開かず終える。

正常な経路では、ファイル保存先の選択、アプリ選択、確認ダイアログを独自に追加しない。iOS自身が最初にアクセス確認を表示する可能性はある。

## 最初の一回だけ確かめる

GitHubアプリで[このPPTXのファイルページ](https://github.com/yusukefujiijp/ai-project/blob/main/artifacts/slides/slide-viewing-test/slide-viewing-test.pptx)を開き、**共有… → スライドを見る** を選ぶ。単に「共有…」を押しただけで自動実行される設計ではない。

完了条件は、URLを書き換えずにMicrosoft Viewerが開き、日本語を含む三枚が見えること。描画待ちは起こり得る。既にHumanが確認した直接Viewerでの表示成功と、この新しい共有経路の成功を区別する。

うまくいかない場合は、止まった箇所だけを切り分ける。

- **共有先に出ない**：共有シート表示と受け取る型を確認。URLをコピーしてショートカットを直接起動し、貼付け経路を試す。
- **対応外のアラートになる**：初回だけ2の直後に「結果を表示」を置き、実際に受け取ったURLを確認する。タイトル・URL・ファイルのどれを渡しているかを決めつけない。確認後は診断アクションを外す。
- **Viewerは開くが表示できない**：既知の[直接閲覧リンク](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fyusukefujiijp%2Fai-project%2Fmain%2Fartifacts%2Fslides%2Fslide-viewing-test%2Fslide-viewing-test.pptx)と比較する。8のURLの `src` を一度復号した値が直接PPTX URLか確認する。ショートカットがブラウザの描画完了を自動検知するとは扱わない。
- **表示が待てない・見た目が崩れる**：[作品READMEのPNG](slide-viewing-test/README.md#三枚のプレビュー)を開くか、そこからPPTXを取得する。保存先を増やす前に既存の入口で回復する。

## 確認できている範囲

2026-10-24時点で、共有ボタンとURLコピーはHuman報告・添付画像から確認済み。直接Microsoft Viewerでの閲覧もHuman確認済み。URL変換の正規表現・エンコード方針は作成環境で検査した。**iOSの実際の入力型・各アクションの連結・共有から描画までの一連の動作は、まだ実機確認していない。** 手順書の保存だけでショートカット完成とはしない。

導入後のFeedbackは、この文書の該当設定と[見られるSlidesのSkill](../../skills/create-viewable-slides/SKILL.md)の必要箇所へ反映する。設定が安定した後、iPhoneから実際にiCloud共有リンクを作れるなら、次回の導入を軽くする入口として追加できる。今回は存在しないリンクを発行済みとしない。

## 根拠

- [Apple：別のアプリからショートカットを実行](https://support.apple.com/en-au/guide/shortcuts/apd163eb9f95/ios)：共有シート表示と入力の適合。
- [Apple：入力を制限する](https://support.apple.com/en-au/guide/shortcuts/apd8195f96d6/ios)：入力なしの場合の要求設定。
- [Apple：Macのコマンドラインから実行・署名](https://support.apple.com/en-sa/guide/shortcuts-mac/apd455c82f02/mac)：配布経路と現在の実行環境の区別。
- [URL Encodeのアクション資料](https://matthewcassinelli.com/actions/url-encode/)：文字列のエンコード。実機での型の扱いは上記の確認対象。
- [Microsoft：Office Web Viewer](https://www.microsoft.com/en-us/microsoft-365/blog/2013/04/10/office-web-viewer-view-office-documents-in-a-browser/)：2013年の仕組みの説明。今回の現行iPhoneでの成立根拠はHuman報告であり、古い説明だけで将来の可用性を保証しない。

EOF::GITHUB_PPTX_IPHONE_SHORTCUT::v001
