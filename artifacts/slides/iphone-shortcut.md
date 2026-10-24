---
title: "GitHubのPPTXをiPhoneの共有から見る"
version: "v002"
created: "2026-10-24"
updated: "2026-10-24"
date_timezone: "Asia/Tokyo"
status: "GitHub共有から日本語三枚のiPhone閲覧をHuman確認済 / URL貼付け経路は未確認"
expected_eof: "EOF::GITHUB_PPTX_IPHONE_SHORTCUT::v002"
---

# GitHubのPPTXをiPhoneの共有から見る

**一度だけ「スライドを見る」を作り、普段はGitHubのPPTX画面で「共有…」→「スライドを見る」。** URLの手作業での書き換えは不要になる構成。共有が合わない時は、同じショートカットを直接起動してURLを貼る。

今すぐ作品を見たい時は、[閲覧テストのスライドを開く](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fyusukefujiijp%2Fai-project%2Fmain%2Fartifacts%2Fslides%2Fslide-viewing-test%2Fslide-viewing-test.pptx)。この直リンクにショートカットの導入は不要。

## 今回の対応範囲

公開GitHubの `main` に置いた `.pptx` 一件を対象にする。GitHubアプリが共有するファイルページURL、GitHubのrawリンク、raw.githubusercontent.comの直接URLを同じ処理へつなぐ。複数URLを渡した場合は最初の一件だけを使う。

ファイルはGitHubに置いたまま、MicrosoftのWeb Viewerで表示する。ChatGPTログインは閲覧経路に含まれない。Microsoftが取得できる公開URLが必要で、private repositoryや期限付きの認証URLは対象外。別branch、slashを含むref、特殊な共有形式、日本語・空白を含むファイル名の端末上の変換は、この初版の実機保証に含めない。既に閲覧用URLなら、そのリンクを直接開けばよい。

この文書は設定手順であり、追加用ショートカットファイルやiCloud追加リンクではない。2026-10-24、YusukeJP自身がiPhoneで組み立て、共有から閲覧まで成功した。AIは画面と報告から確認し、端末はHumanが操作した。別の端末へ初めて導入する場合も、その端末上で組み立てる。

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

4. **一致するテキスト（Match Text）**：アクション検索では **一致** と入力する。対象を3の出力 **アップデートされたテキスト** の変数一個だけにし、次に一致する部分を取得する。変数名を文字入力せず、出力の青いトークンを選ぶ。直接PPTXだけを選び、末尾の `?raw=true` や `#...` は除く。

```text
\Ahttps://raw\.githubusercontent\.com/[^/?#\s]+/[^/?#\s]+/main/[^?#\s]+(?i:\.pptx)(?=[?#]|\z)
```

5. **もし（If）**：4の「一致」を入力にし、条件を **任意の値（値がある）** にする。条件は一件でよい。空の「条件」行を追加してしまった場合は、その行の青い「⊖」で取り除く。条件が真の場合の処理として、次の6〜9を置く。
6. **テキスト（Text）**：内容を4の「一致」の変数だけにする。URL型のまま渡さず、エンコード対象の文字列にする。
7. **URLエンコード（URL Encode）**：「エンコード」で検索し、6のテキストを「エンコード」。
8. **テキスト（Text）**：下の固定部分に、7の出力を改行なしで続ける。

```text
https://view.officeapps.live.com/op/view.aspx?src=
```

完成形は `固定部分[URLエンコードの出力]`。固定部分全体を再度エンコードしない。元のパス内の `%20` などが `src` 内では `%2520` になることは、二重誤変換とは限らない。`src` を一度復号すると正しい直接URLに戻ることを確認する。

9. **URLを開く（Open URLs）**：8のテキストを開く。
10. 5の **その他の場合（Otherwise）** に **アラートを表示（Show Alert）** を置き、「公開GitHubのmainにあるPPTXのURLを1件共有してください。」と表示する。ここではブラウザを開かず終える。

6〜9は「もし」と「その他の場合」の間、10のアラートは「その他の場合」と「If文の終了」の間に並べる。追加先が違った場合はカードを長押しして移動する。正規表現は `\A` の前、閲覧用テキストは `src=` と出力変数の間に手入力の空白・改行を入れない。画面上の自動折り返しとは区別する。

正常な経路では、ファイル保存先の選択、アプリ選択、確認ダイアログを独自に追加しない。iOS自身が最初にアクセス確認を表示する可能性はある。

## 最初の一回だけ確かめる

GitHubアプリで[このPPTXのファイルページ](https://github.com/yusukefujiijp/ai-project/blob/main/artifacts/slides/slide-viewing-test/slide-viewing-test.pptx)を開き、**共有… → スライドを見る** を選ぶ。単に「共有…」を押しただけで自動実行される設計ではない。

完了条件は、URLを書き換えずにMicrosoft Viewerが開き、日本語を含む三枚が見えること。描画待ちは起こり得る。この作品の共有経路は2026-10-24にHumanが確認済みであり、この手順の改訂だけを理由に再試験を要求しない。

URL貼付けの補助入口を確かめる時は、同じショートカットを直接実行し、同じGitHubのPPTXページURLを入力する。この入口の成功は別に判定する。

うまくいかない場合は、止まった箇所だけを切り分ける。

- **共有先に出ない**：共有シート表示と受け取る型を確認。URLをコピーしてショートカットを直接起動し、貼付け経路を試す。
- **対応外のアラートになる**：初回だけ2の直後に「結果を表示」を置き、実際に受け取ったURLを確認する。タイトル・URL・ファイルのどれを渡しているかを決めつけない。確認後は診断アクションを外す。
- **Viewerは開くが表示できない**：既知の[直接閲覧リンク](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fyusukefujiijp%2Fai-project%2Fmain%2Fartifacts%2Fslides%2Fslide-viewing-test%2Fslide-viewing-test.pptx)と比較する。8のURLの `src` を一度復号した値が直接PPTX URLか確認する。ショートカットがブラウザの描画完了を自動検知するとは扱わない。
- **表示が待てない・見た目が崩れる**：[作品READMEのPNG](slide-viewing-test/README.md#三枚のプレビュー)を開くか、そこからPPTXを取得する。保存先を増やす前に既存の入口で回復する。

## 確認できている範囲

2026-10-24、**GitHubアプリの共有 →「スライドを見る」→ Microsoft Viewer → 日本語三枚の表示**をHuman報告と添付画像から確認した。詳細な根拠と履歴は[閲覧実験](slide-viewing-test/README.md#後続のhuman報告と訂正)が所有する。URL変換の正規表現・エンコード方針は作成環境でも検査済み。

同じショートカットへのURL貼付け、共有される入力型・文字列の詳細、他の端末・作品での成立は今回の報告だけでは確認していない。設定画面の確認、Humanの操作報告、描画結果の確認を区別する。

導入後のFeedbackは、この文書の該当設定と[見られるSlidesのSkill](../../skills/create-viewable-slides/SKILL.md)の必要箇所へ反映する。Humanは一操作ごとの確認による往復の多さを指摘した。端末案内は目的に合うまとまりで完成・実行テストまで示し、途中画像は判断に必要な時だけ求める。細かな案内を求められた場合は、その希望へ合わせる。

設定が安定した後、iPhoneから実際にiCloud共有リンクを作れるなら、次回の導入を軽くする入口として追加できる。現在は追加リンクを発行していない。

v002では共有経路の実機成功、実際のアクション名「一致するテキスト」と条件表示「任意の値」、導入時Feedbackを反映した。

## 根拠

- [Apple：別のアプリからショートカットを実行](https://support.apple.com/en-au/guide/shortcuts/apd163eb9f95/ios)：共有シート表示と入力の適合。
- [Apple：入力を制限する](https://support.apple.com/en-au/guide/shortcuts/apd8195f96d6/ios)：入力なしの場合の要求設定。
- [Apple：Macのコマンドラインから実行・署名](https://support.apple.com/en-sa/guide/shortcuts-mac/apd455c82f02/mac)：配布経路と現在の実行環境の区別。
- [URL Encodeのアクション資料](https://matthewcassinelli.com/actions/url-encode/)：文字列のエンコード。実機での型の扱いは上記の確認対象。
- [Microsoft：Office Web Viewer](https://www.microsoft.com/en-us/microsoft-365/blog/2013/04/10/office-web-viewer-view-office-documents-in-a-browser/)：2013年の仕組みの説明。今回の現行iPhoneでの成立根拠はHuman報告であり、古い説明だけで将来の可用性を保証しない。

EOF::GITHUB_PPTX_IPHONE_SHORTCUT::v002
