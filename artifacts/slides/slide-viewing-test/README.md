---
title: "スライドを、スライドとして見る｜閲覧テスト"
canonical_path: "artifacts/slides/slide-viewing-test/README.md"
version: "v001"
created: "2026-10-18"
updated: "2026-10-18"
date_timezone: "Asia/Tokyo"
role: "Three-slide viewing experiment and export provenance"
expected_eof: "EOF::SLIDE_VIEWING_TEST::v001"
---

# スライドを、スライドとして見る

**編集は不要。完成したスライドを、順番・レイアウトを保って閲覧できることが目的。** この三枚は、その閲覧経路を試すためにこの会話で作った作品。既存の[残作業とGoal](../remaining-work-and-goal/README.md)の五枚とは別作品である。

## 開く

- [PPTXをダウンロード](https://github.com/yusukefujiijp/ai-project/raw/refs/heads/main/artifacts/slides/slide-viewing-test/slide-viewing-test.pptx)
- [PPTXのファイルページ](slide-viewing-test.pptx)
- 下のPNGは、書き出したPPTXを再読み込みして表示した閲覧用プレビュー。

配布先は公開GitHub。ChatGPTのログイン画面や元のSlidesページを経由せず、ファイルを取得する経路である。GitHubのファイル保存と、GitHub画面内のPPTXスライドショー対応は別問題。PPTXの閲覧は端末側の対応ビューアで試す。

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
| 未確認 | YusukeJPのiPhoneでの取得、表示、ページ送り。PowerPoint／Keynote等での実行確認。Web版公式ダウンロードとのバイト一致 |

次の実地確認は、上のPPTXリンクをiPhoneで開き、**日本語を含む三枚が、編集操作なしで順番に見られるか**を試すこと。保存成功と、このHuman側の閲覧成功は分けて扱う。

検査フォントは[Noto CJK公式リポジトリ](https://github.com/notofonts/noto-cjk/tree/f8d157532fbfaeda587e826d4cd5b21a49186f7c/Sans/OTF/Japanese)のNotoSansCJKjp-Regular/Bold（[SIL OFL 1.1](https://github.com/notofonts/noto-cjk/blob/f8d157532fbfaeda587e826d4cd5b21a49186f7c/Sans/LICENSE)）を使用。フォントファイル自体はこの作品フォルダへ追加していない。

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

EOF::SLIDE_VIEWING_TEST::v001
