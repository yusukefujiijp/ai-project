---
name: create-viewable-slides
description: Create or deliver slides that YusukeJP can view casually on iPhone without editing. Use for この部分をChatGPT Slides化して, making an existing PPTX viewable from GitHub, or connecting GitHub sharing to an iPhone shortcut. Preserve the requested Slides provider, export provenance, and one managed GitHub source; return a ready-to-open viewing link when possible.
---

# 見られるSlides

## 目的から始める

完成したスライドを、順番・レイアウトを保って気軽に見られる状態まで届ける。編集は既定の要件にしない。Humanの「Simple is best」を優先し、一つの短い依頼からAI側で制作・保存・閲覧の接続を引き受ける。必要な方法は実環境とFeedbackで改善する。

新作の生成か、既存作品の保存・閲覧かを文脈から判断する。既知の対象・保存先・成功報告を再質問しない。Plan-onlyとSTOPは守り、現在有効な実行委任があれば必要な修正・検証・保存後確認まで進める。Root・Human Authority・適用Guardは保持し、SkillはKeliとして扱う。

## 原本と制作経路を保持する

- 新作では、何を分かりやすくするかを明確にし、利用可能なPresentationsの現行Skill・実際の制作機能を使う。ページ数・構成・デザインは目的に合わせて判断する。
- HumanがChatGPT Slidesを指定したら、その経路が実際に使えるか確認する。別ツールで作ったPPTXを「ChatGPT Slidesで生成した」と呼ばない。利用不能なら制約と実行可能な代案を明示する。
- 既存PPTXは取得した実体を優先し、閲覧リンクの作成だけなら再生成・再書き出しをしない。元ファイルと派生版を区別する。
- UIの「ダウンロード → PowerPoint」で取得したもの、保存版データからの書き出し、画像を使った派生版を区別する。元のSlidesを編集しなかったことと、公式UI出力とのバイト一致を混同しない。

## 保存と閲覧を一つにつなぐ

Arkで公開可能な作品は、既存のGitHub保存先を優先する。既定の候補は `yusukefujiijp/ai-project` の `artifacts/slides/<作品名>/`。現在の依頼の公開範囲と既存Ownerを確認し、[Slides入口](https://github.com/yusukefujiijp/ai-project/blob/main/artifacts/slides/README.md)、[AGENTS](https://github.com/yusukefujiijp/ai-project/blob/main/AGENTS.md)、[Artifact → GitHub](https://github.com/yusukefujiijp/ai-project/blob/main/prompts/artifact-to-github.md)の適用契約に従う。確認済みの読解を同一性条件の範囲で再利用する。

PPTXを保存し、作品READMEの先頭付近と回答に、すぐ使える「スライドを見る」とPPTX取得先を示す。画像プレビューが既にあれば再利用し、必要な時だけ追加する。同じ作品をDropbox等へ自動的に重複保存しない。

公開PPTXでは、GitHubを管理上の原本とし、Microsoft Office Web Viewerへ直接ファイルURLを渡す方法を使える。GitHubの `blob` ページURLをそのまま `src` に渡さない。

```text
https://view.officeapps.live.com/op/view.aspx?src=<直接PPTXのURLをクエリ値としてエンコード>
```

同梱の `scripts/viewer_url.py` は、公開GitHubの `main` または40桁commit SHAを使うPPTXリンクから閲覧URLを組み立てる。`blob`、`raw`、`raw.githubusercontent.com` と、この方法で作った閲覧URLを扱う。ネットワーク取得や公開判定は行わない。別refや特殊なURLは、実在する直接ファイルURLを確認してから扱う。

```bash
python scripts/viewer_url.py 'https://github.com/OWNER/REPO/blob/main/PATH/DECK.pptx'
```

ファイルがMicrosoft側から認証なしで取得できることが成立条件。private repository、ログイン前提URL、期限付き認証URLはこの経路へ流さない。HumanのGitHubログイン状態はMicrosoftへ引き継がれない。Microsoft側の描画・キャッシュ等が存在しないとは主張せず、管理する保存先と閲覧処理を区別する。

## 確認して渡す

必要な範囲で、PPTX実体、ページ数・日本語・レイアウト、Remote再取得と元バイト、閲覧URLの復号先を確認する。既存の成功を再試験のために未確認へ戻さない。GitHub保存、リンク組立、ブラウザ描画、HumanのiPhone操作は別々の確認である。

GitHubアプリの `PK` 等の表示は、PPTXバイナリのテキスト表示と整合し、それだけで破損とはしない。PowerPointの欠落字形は別の描画問題として扱う。見た目の保持が必要で編集不要なら、元ページの高品質画像から画像版PPTXまたはPDFを作る案がある。必要性と現在の権限がある時だけ追加し、元PPTXを上書きしない。

完成時は閲覧リンクを主に返し、出力・保存・表示のうち未確認な点だけを明確にする。端末確認が必要なら具体的な操作へ接続し、実行可能な残作業を単なる提案で返さない。

## iPhone共有とFeedback

既存GitHubリンクを日常的に開く場合は、共有 →「スライドを見る」を主入口、同じショートカットへのURL貼付けを補助入口にする。[導入手順](https://github.com/yusukefujiijp/ai-project/blob/main/artifacts/slides/iphone-shortcut.md)は、その設定・確認方法を所有する。新作へ直接閲覧リンクを付ける仕事を、ショートカット完成待ちで止めない。

署名済みショートカットやiCloud追加リンクを実際に作れない環境では、作成・インストール済みと称さない。iPhoneを操作できない時はその一点を示し、組み立てと初回試験へつなぐ。共有メニューの存在と、実際に渡る入力型・URL・表示成功を区別する。

改善はHumanの実際の摩擦から行う。新しいWebアプリ、認証機構、同期、複数保存先、全形式対応を先回りして足さない。成立経緯と確認範囲は[閲覧実験](https://github.com/yusukefujiijp/ai-project/blob/main/artifacts/slides/slide-viewing-test/README.md)、共有入口は[Skill README](https://github.com/yusukefujiijp/ai-project/blob/main/skills/create-viewable-slides/README.md)を必要な時に参照する。
