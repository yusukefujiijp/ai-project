---
title: "見られるSlides — create-viewable-slides"
version: "v001"
created: "2026-10-24"
updated: "2026-10-24"
status: "Human-authorized first implementation / iPhone shortcut field check pending"
expected_eof: "EOF::CREATE_VIEWABLE_SLIDES_README::v001"
---

# 見られるSlides

**「この部分を分かりやすくChatGPT Slides化して」と頼むと、生成した作品を、編集せずiPhoneで見られる入口までつなぐためのSkill。** 既存のGitHub PPTXを見たい時にも使う。作品の生成能力、保存、閲覧を接続し、Humanに毎回URL変換や保存先の判断を戻さない。

手順の原本は[SKILL.md](SKILL.md)。このREADMEは用途・Query・形成と確認範囲を所有する。GitHubの共有原本、登録先への反映、実際の起動、iPhoneでの利用は別の状態として扱う。

## 気軽な使い方

このThreadや登録済み環境では、「この部分を分かりやすくChatGPT Slides化してください」「このGitHubのPPTXを見たい」で目的を渡せる。新作の題材と既存URLは現在の会話から解決する。最初からページ数・デザイン・手順をHumanが書く必要はない。

別AIにも渡せるQuery：

```text
$create-viewable-slides を使い、この会話で対象にしている部分を分かりやすくChatGPT Slides化してください。編集は不要です。利用できる制作機能と公開範囲を確認し、既存のGitHub保存先を優先して、iPhoneですぐ見られる閲覧リンクとPPTX取得先まで届けてください。既に作品がある場合は再生成せず活かしてください。
Skillを直接利用できない場合は、次の共有SKILL.mdを全文読んで適用してください。表示切れは未読部分から回収し、宣言された必須依存・読取順・Identity・Binding・EOFを保持してください。取得できない必須Sourceがあれば、影響範囲と最小の回復方法を示してください。
https://github.com/yusukefujiijp/ai-project/blob/main/skills/create-viewable-slides/SKILL.md
```

## 役割の分担

- **このSkill**：生成・保存・閲覧をつなぎ、すぐ見られるリンクを返す。
- **Presentations等の制作機能**：目的に合う作品を作成し、実物を書き出す。現在の機能・利用経路を確認する。
- **GitHub**：公開可能な作品の管理上の原本。
- **Microsoft Viewer**：公開PPTXの閲覧処理。別の管理用保存先をHumanに増やさない。
- **iPhoneショートカット**：既存GitHubリンクから閲覧へ移る日常操作を減らす。新作の直接閲覧リンクには導入不要。

操作は[導入手順](../../artifacts/slides/iphone-shortcut.md)、作品と実験の根拠は[閲覧テスト](../../artifacts/slides/slide-viewing-test/README.md)へ。Pythonの[URL生成補助](scripts/viewer_url.py)はAIやCLI向けで、iPhone上でPythonを動かす必要はない。

## 形成と確認範囲

YusukeJPは、Slidesを編集することより「slideをslideとしてみたい」を重視した。GitHubの画像列では閲覧でき、DropboxからPowerPointへ送った画像版でも良好な結果を報告した。一方、GitHub以外へ保存先が広がる点が課題となり、GitHubのPPTXをMicrosoft Viewerで開く経路を試し、描画待ちはあるが閲覧できると報告した。

ChatGPTアプリで見えた画像をDropboxの成功と解釈しかけた訂正、元PPTXの欠落字形とGitHubアプリのバイナリ表示が別問題であることを保持する。GitHubのPPTXを壊れていると決めつけて作り直さない。

最新のHuman入力は、GitHubアプリの共有ボタンとURLコピーを確認し、共有からショートカットへ進む方法を選んだ。その後、Plan-onlyから実行へ明示的に切り替え、GitHub作業と継続を承認した。計画の終わりをThreadのGoal達成と混同した「Next Query: None」へのCorrectionも、実行可能な仕事を進め、端末で必要な具体操作へつなぐ判断として保持する。

初版は、既存作品への閲覧リンク、成功報告の保存、共有・貼付けを一つにまとめた導入手順、再利用するSkillを実装した。URL生成補助の正常・異常入力19項目、手順書の正規表現9項目、相対参照先136件を検査した。別のAIによる読み取り専用の確認でも、既存公開PPTXへのリンク生成、private repositoryの境界、手順の接続を確認した。これはiPhoneでの実行を示さない。

端末の共有入力・操作は未確認であり、署名済みショートカットやiCloud追加リンクを提供できたとはしない。新作の生成からこのSkillを使う一連の実利用も、今回の既存作品への接続とは別の検証である。

KISS / DRY / YAGNI / Lean / SRPを、入口一つ・GitHub原本・既存機能の組合せ・実際のFeedbackからの改善として適用する。新しいWebアプリ、全形式対応、Google Drive移行、同期機構は初版へ含めない。このSkillの存在だけで将来の生成・公開・設定変更を自動承認しない。

EOF::CREATE_VIEWABLE_SLIDES_README::v001
