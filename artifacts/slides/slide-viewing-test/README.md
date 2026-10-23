---
title: "スライドを、スライドとして見る｜閲覧テスト"
canonical_path: "artifacts/slides/slide-viewing-test/README.md"
version: "v002"
created: "2026-10-18"
updated: "2026-10-24"
date_timezone: "Asia/Tokyo"
role: "Three-slide viewing experiment and export provenance"
expected_eof: "EOF::SLIDE_VIEWING_TEST::v002"
---

# スライドを、スライドとして見る

**編集は不要。完成したスライドを、順番・レイアウトを保って閲覧できることが目的。** この三枚は、その閲覧経路を試すためにこの会話で作った作品。既存の[残作業とGoal](../remaining-work-and-goal/README.md)の五枚とは別作品である。

## 開く

- **[スライドを見る（ブラウザ）](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fyusukefujiijp%2Fai-project%2Fmain%2Fartifacts%2Fslides%2Fslide-viewing-test%2Fslide-viewing-test.pptx)** — この作品についてYusukeJPがiPhoneで閲覧できることを確認済み。描画待ちはあり得る。
- [PPTXをダウンロード](https://github.com/yusukefujiijp/ai-project/raw/refs/heads/main/artifacts/slides/slide-viewing-test/slide-viewing-test.pptx)
- [PPTXのファイルページ](slide-viewing-test.pptx)
- [GitHubの共有から開くためのiPhone設定](../iphone-shortcut.md)
- [画像版PPTXを取得](https://github.com/yusukefujiijp/ai-project/raw/refs/heads/main/artifacts/slides/slide-viewing-test-image.pptx) — フォント依存を減らした別版。
- 下のPNGは、書き出したPPTXを再読み込みして表示した閲覧用プレビュー。

配布先は公開GitHub。ChatGPTのログイン画面や元のSlidesページを経由せず、ファイルを取得する経路である。GitHubのファイル保存と、GitHub画面内のPPTXスライドショー対応は別問題。上の閲覧リンクでは、公開されたPPTXをMicrosoftのWeb Viewerへ渡す。管理する原本はGitHubにあり、Microsoft側の描画・キャッシュ等が存在しないという意味ではない。

## 今回の工夫と由来

2026-10-18 JST、YusukeJPから、この作品を指定の `artifacts/slides` に保存する実験を依頼された。以前の「元のSlidesのダウンロードメニューから取得したPPTXを、そのまま保存する」経路を基準にしつつ、今回は次を実施した。

1. 既に接続されたChatGPTの文書機能から、同名Native Slidesの保存版（sequence 1）を読み取り専用で取得。
2. `presentation.toProto()` のデータを、全チャンク同じ保存版であることを確認して連結。
3. Artifact Tool 2.8.99 の `Presentation.load(proto)` → `PresentationFile.exportPptx()` でPPTX化。
4. 内容・構造・表示を検証し、PPTX本体とPNGをGitHubへ保存。

**この実験ではChatGPTのWeb画面を開く操作も、新しいログイン操作も行っていない。** ただし、原本の取得とGitHubへの書き込みには既存の認証済み接続を使用した。「認証なしで非公開原本を取得できる」という意味ではない。

元のNative Slidesは編集していない。文章の再生成や、画像を貼り直したPPTX化でもない。ただし、今回はWeb版の「ダウンロード → PowerPoint (PPTX)」を押して取得したファイルではない。その公式UI出力との完全なバイト一致は未検証であり、「以前と同じ取得経路の未変更ファイル」とは扱わない。ここに保存したPPTXは、今回のローカル書き出し後に内容を変更していない。

## 確認結果と残る実験

| 対象 | AI側で確認したこと／境界 |
|---|---|
| 構造 | 三枚、16:9、1280×720相当。PPTXのパッケージ整合・レイアウト検査に合格 |
| 内容の保持 | PPTX再読み込み後の全文、改行、形状の位置・大きさ、背景、文字のフォント名・サイズ・太字・色が取得原本と一致 |
| 表示 | 元と同じNoto Sans CJK JPのRegular/Boldを検査環境へ読み込み、再読み込みしたPPTXの全三枚をPNG化して目視確認。日本語の欠落・はみ出しなし |
| フォントの注意 | 最初は検査環境の日本語フォント不足で本文が見えなかった。元フォントの読み込みで解消し、PPTX自体は変更していない。PPTXにフォントは埋め込んでいないため、他端末での置換や差異は残り得る |
| GitHub保存 | [初回保存commit](https://github.com/yusukefujiijp/ai-project/commit/2f47b6391c41e63e487e0beeb6effd92bdccb86a)の全六ファイルをGitHubから再取得し、ローカルとバイト一致を確認。既存作品フォルダのtree SHAも不変 |
| 公開ダウンロード | Cookie・認証情報を指定しないHTTP取得で、上のPPTXリンクがHTTP 200、25,896 bytesを返すことを確認。ダウンロードしたPPTXのSHA-256も一致。ChatGPTログインを経由していない |
| Human確認済み | 後続の会話で、GitHubのこのPPTXをMicrosoft Viewerで開き、描画に多少時間はかかるがスライドが見えると報告。画像でも日本語表示を確認。閲覧経路ごとの結果は下記に保持 |
| 未確認 | iPhoneショートカットの共有入力と一連の操作、全端末・全ファイルの互換性、Keynote、Web版公式ダウンロードとのバイト一致 |

2026-10-18時点ではiPhone閲覧は未確認だった。2026-10-24の記録更新では、後続のHuman報告を反映し、既に成立した閲覧を未確認へ戻さない。残る実地確認は[共有ショートカット](../iphone-shortcut.md)から同じ閲覧へ接続できるかである。

検査フォントは[Noto CJK公式リポジトリ](https://github.com/notofonts/noto-cjk/tree/f8d157532fbfaeda587e826d4cd5b21a49186f7c/Sans/OTF/Japanese)のNotoSansCJKjp-Regular/Bold（[SIL OFL 1.1](https://github.com/notofonts/noto-cjk/blob/f8d157532fbfaeda587e826d4cd5b21a49186f7c/Sans/LICENSE)）を使用。フォントファイル自体はこの作品フォルダへ追加していない。

## 後続のHuman報告と訂正

以下はこのThreadの報告を2026-10-24に編集要約したもの。各出来事の正確な日時は確定せず、記録更新日と区別する。

- **GitHubアプリのバイナリ表示**：`PK` やXML名を含む表示はPPTXをテキストとして見た状態と整合する。ファイル破損の証拠にはしない。
- **元PPTXとPowerPoint**：一度、見出しが欠落字形になり本文は読める画像が報告された。フォント描画が関係する可能性はあるが、正確な原因は未確定。
- **ChatGPTアプリの画像**：綺麗に見えた画像の一つはChatGPTアプリの画面であり、Dropboxでの成功ではないとHumanが明示訂正した。
- **画像版PPTX**：ページ画像を全面に配置した別版をDropbox経由でPowerPointへ渡し、Humanが「綺麗に見えました」と報告。元のテキストPPTXとは別実体。2026-10-24のGitHub確認では、同じ画像版が親フォルダにも既に存在し、git blobとローカル実体が一致した。今回新しくアップロードしたものではない。
- **GitHub → Microsoft Viewer**：元のテキストPPTXがリンクから見えるとHumanが報告。画像では日本語を含むスライドを表示している。描画待ちや将来のサービス可用性、全PPTXへの一般化は別問題。
- **GitHubの共有入口**：Humanが共有ボタンとURLコピーを確認。これはショートカットへ実際に渡る内容・型や、ショートカット導入済みの証明ではない。

画像版の照合情報：`../slide-viewing-test-image.pptx`、171,452 bytes、SHA-256 `c2ecb00bcc8b467907d06776eb74f3941581c190ce2810f0c8f19411dc4024af`、git blob `b034e9e1671c54b925abd9154087f22e669a1a40`。この版は元ページ画像を使用し、可視テキストの編集は目的にしていない。

今回のv002は入口と確認記録を更新した。下記PPTX・PNG・原本来歴は変更していない。方法の再利用は[見られるSlides](../../../skills/create-viewable-slides/README.md)へ。

## 三枚のプレビュー

### 01 — スライドを、スライドとして見る

![01 スライドを、スライドとして見る。完成した一枚を、そのまま楽しむ。](slide-01.png)

### 02 — 一枚の中に、意味がまとまる

![02 一枚の中に、意味がまとまる。文字の大きさ、余白、配置も伝わる。](slide-02.png)

### 03 — 順番にめくって、全体をつかむ

![03 順番にめくって、全体をつかむ。編集は不要。自然に見られることがゴール。](slide-03.png)

## ファイル照合情報

- PPTX: `slide-viewing-test.pptx` / 25,896 bytes
- PPTX SHA-256: `504f263d37f4d9382e752777c42db9918482ba1b5abea070f549e69a369c3c2f`
- 取得した保存版データのJSON SHA-256: `31bb7e469e293e5da1f6a3d6bbc34000b9ff973db02dee03560bbe45b3da8790`（連結した文字列、末尾改行なし）

サービス側原本と、この書き出しは自動同期しない。この一件の実験を、あらゆるSlidesやアカウントで成立する共通方式の実証へ拡張しない。

EOF::SLIDE_VIEWING_TEST::v002
