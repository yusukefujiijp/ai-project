---
name: connect-chatgpt
description: Connect or reconnect to YusukeJP's own ChatGPT in a browser using the established saved profile, verify the account, and recover when authentication is needed. Use for requests such as ChatGPTに接続して; not for general ChatGPT questions, Codex CLI authentication, or API keys.
---

# ChatGPTに接続する

Humanが長い初回設定を繰り返さず、本人のChatGPTへ接続できる状態を目指す。現在利用できる正規のブラウザ操作経路を使い、通常は保存済みプロフィールを再利用する。以下はYusukeJPの確認済み経路であり、別の利用者・アカウントへ流用しない。

## 現在の依頼と接続先

接続依頼には、既存プロフィールを使ったページ表示・本人確認までを含める。計画だけの依頼では実行しない。接続後の作業も現在の依頼で承認されていれば、その範囲を続ける。接続確認だけなら接続結果で完了する。

- サイト：`https://chatgpt.com/`
- 経路：接続済みTinyFishのBrowser Context Profile
- プロフィールID：`prof_d1578ef04cc44022`。保存時の表示名は`Default`。
- 本人確認の既知情報：ユーザー名`@yusukejp`、表示名`Yusuke Fujii`。表示名だけで同一性を決めず、固有のユーザー名、または現在の信頼できる文脈にあるアカウント情報と照合する。
- 同じIDについて、Humanのログイン・保存完了報告と本人一致の実行記録がある。新しい矛盾がなければ、既知の確認を一律に再質問しない。

現在のCorrectionは、アーカイブを停止し、復元もしないこと。過去の「10件」承認から再開しない。Gmail展開は将来のVisionであり、この接続依頼に含めない。後続の明確な変更指示があれば、その対象と範囲で判断する。

## 保存済み状態を使う

1. 実行時に公開されているTinyFishのツール仕様を確認し、`list_profiles`が使えれば一覧から上記IDを照合する。プロフィール名だけで別のIDへ切り替えない。道具や同じIDが使えなければ、その不足と回復に必要な接続先を示す。過去に使えた別環境へアクセスできると推測しない。
2. `run_web_automation`で`use_profile: true`と照合した`profile_id`を明示し、ChatGPTを開く。Vault連携はこの経路で未確立なので、認証情報の利用を無条件に有効にしない。ツール引数や機能名が変わっていれば現在の公開仕様に合わせる。
3. 会話一覧への到達と本人アカウントを、通常の画面操作で確認する。必要ならアカウント情報画面を読む。会話本文の精読や全履歴走査を接続確認へ追加しない。結果には、本人一致・一覧到達・追加認証の要否・到達URL・阻害要因を必要な範囲で返す。メールアドレス等は値の再掲より一致結果を優先する。
4. 実行がIDを返したら、同じIDを`wait_for_run`で完了まで追う。待機のタイムアウトだけで実行を重ねない。実行IDまで失われた場合の回復は、現在のツール仕様で認められた状態確認を使う。

このプロフィールは、`signed_in_sites`が空でも本人のChatGPTへ接続できた。空配列をログアウトの証拠にせず、過去の接続実績も現在の有効性の証明にしない。プロフィールの存在・保存完了・実アクセス・本人一致は別々に確認する。

## 必要な時だけ復帰する

- **ログイン要求・認証切れ：** 同じプロフィールの`start_profile_setup_session`を使う再認証を案内する。現在の依頼で再認証の開始まで認められていれば進め、不足する場合だけ確認する。HumanはiPhoneの設定ブラウザ内で認証し、本人の会話一覧まで到達してから保存する。保存後に同じIDで接続を確認する。設定ページのSaveを使った時に、別の保存呼出しを重ねない。
- **読み込み中・通信エラー：** 表示と実行状態から原因を区別する。Cloudflare等の画面が一時表示されたことだけでプロフィールを作り直さない。サイトが人の操作を要求している場合は、その通常の確認経路へ戻す。
- **別アカウント・IDの不一致：** 後続作業を止め、必要なアカウント選択だけをHumanへ返す。既知のプロフィールを黙って置換しない。

パスワード・認証コード・Cookie・トークンをチャットやGitHubへ移さない。期限付き設定URLを恒久的な入口にしない。Codexのデバイスコード認証や1Passwordの環境変数機能を、ChatGPTのブラウザセッションと同一視しない。

## 原本と実績

共有原本は[このSKILL.md](https://github.com/yusukefujiijp/ai-project/blob/main/skills/connect-chatgpt/SKILL.md)。登録機構がない環境でも全文を取得して指示資料として使えるが、導入済みとは称しない。[README](README.md)は短い起動Query・導入範囲・実績への入口であり、通常の接続で毎回読む義務はない。

成立経緯は[成功事例](https://github.com/yusukefujiijp/ai-project/blob/main/references/success-cases/success-cases.jsonl)のID `16ce6cbe-9b5e-48b5-9e76-8c57e86ab1c4`、プロフィールの性質は[TinyFish公式説明](https://docs.tinyfish.ai/key-concepts/browser-context-profiles)が所有する。履歴の調査や仕様の不一致が判断を変える時に参照し、通常の再利用を毎回の全履歴調査にしない。
