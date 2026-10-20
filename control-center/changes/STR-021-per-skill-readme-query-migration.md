---
title: "STR-021 — 各SkillのREADMEへQueryと個別記録を移す"
canonical_path: "control-center/changes/STR-021-per-skill-readme-query-migration.md"
record_id: "STR-021"
version: "v001"
record_date: "2026-10-20"
repository: "yusukefujiijp/ai-project"
ref: "main"
base_commit: "369b5f1f287d212848def6121a2ad374aa3e2d77"
actor: "Codex / YusukeJPとの本対話"
status: "Implementation prepared; remote verification recorded below after publication"
expected_eof: "EOF::STR_021_SKILL_README_QUERY::v001"
---

# STR-021 — 各SkillのREADMEへQueryと個別記録を移す

**用途とQueryは各SkillのREADME、実際の手順はSKILL.md、全体の一覧と共通方針はHubへ置く。** [現行Hub](../../skills/README.md#readme-and-query-ownership)が今後の保存先を案内する。本記録は今回の訂正・移行・確認範囲を所有し、利用のたびの必読資料ではない。

## Humanの意図と訂正

YusukeJPは、`resolve-github-runtime` と `markdown-to-html` の共有・更新に続いて起動Queryの保存を求めた。その際、AIが各Skillの説明・Queryを `skills/README.md` へ集める方向を示したため、「各スキルごとにREADME.mdを書く」という意図を明示した。理由は、共通Hubが膨らみ、個別の利用・更新先が分かりにくくなる懸念である。

既存Queryフォルダを保持する案も検討した後、Humanは、Skill化で短く呼べるようになったQueryを個別READMEへ収め、Query専用フォルダを除く方針へ訂正した。「当時は長いQueryを分ける事情があったはず」という説明はHumanの仮説であり、すべての既存フォルダについて確認済みの作成理由ではない。MAPの実資料には、Skill改良途中の入口を先にbackupした経緯がある。

Plan-onlyの検討を経て、Current Humanは「Execute GitHub OK!」「Human Seal OK!」と実行・継続を承認した。本節は本対話の直接入力を編集要約したものであり、Memoryの出力、全会話の輸出、別Actorの観測ではない。

## 対象と所有関係

- 基点の現行catalogは32件。既存READMEは `problem-solving`、`b-zone`、`prepare-ark-transition` の3件。これらの成果を保ち、残る29件へREADMEを追加する。
- 各READMEへ用途、完全にコピーできるQuery、必要な個別来歴・確認範囲を配置する。短い標準Queryと固有条件のある詳しいQueryは同じREADMEに併存できる。UIの `default_prompt` はUI設定として保持し、別のQuery保存フォルダとは扱わない。
- Hubは現行一覧、共通の読み方・lesson所有先・配布と復元・確認境界を保持する。既存Hub節のURLは短い移動案内として残し、Query本文を二重管理しない。
- 新旧MAPのQueryフォルダは、内容・現用参照を移して除去する。旧Queryフォルダ内のredirect stubは残さない。旧名Skill自体は現行名への互換案内として区別し、32件に加算しない。
- `_grok`・archives・第三者Plugin・別領域のQuery構造は今回の全件対象ではない。Skillの改名、UI、実装コード、実行手順の一括改訂も行わない。

| Node | Edge | 移行後の役割 |
|---|---|---|
| `skills/README.md` の個別Query・形成記録 | → 各 `skills/<name>/README.md` | Skillごとの利用・説明・訂正の担当原本 |
| `skills/map-current-position/query/README.md` | → [MAP README](../../skills/map-current-position/README.md) | 短い標準入口、既存の詳しいMAP Query、[残作業深掘り](../../skills/map-current-position/README.md#remaining-work-goal-deep-dive)を同じREADMEへ |
| `skills/map-ark-current-position/query/README.md` | → [現行MAP README](../../skills/map-current-position/README.md) | 旧Queryフォルダを除去し、旧名Skillの案内から直接接続 |
| `SKILL.md` の利用・来歴への案内 | → 個別README | runtime・Markdownの各一行と旧MAPのリンクを訂正。判断・変換の本体は保持 |
| 現用のMAP Queryリンク | → 新READMEと同じ用途のanchor | 引継ぎ文書のBindingも整合させる |
| 固定commit・`path_at_release`・当時の検証記録 | → 当時の実体 | 過去の住所や確認結果を現在へ塗り替えない |

## 保持する意味と証拠

旧Hubの14件のfenced Query本文と、MAP Query原本の2件は、新しい各READMEで文字列の完全一致を確認した。MAPの通常Queryと「残作業・Goal深掘り」は別用途として残し、後者のread-only条件を維持する。長いQueryを置くフォルダの除去と、必要な意味の削除を同一視しない。

個別形成記録は日付と観測範囲を保って移す。登録先保存・会話内旧版取得・後日の取得成功、Human評価・限定AI応答・実生活効果を分ける。`markdown-to-html` に2026-10-07の改訂があった訂正、`resolve-github-runtime` が個人Skillであること、Ark23の代替記録が条件付き参照であることも維持する。9月12日のexport-manifestは当時のGraph/Audit二件の記録のまま保持し、現行32件の登録簿へ書き換えない。

移行前の[Hub全文](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)、[MAP Query全文](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/map-current-position/query/README.md)、[旧名Query案内](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/map-ark-current-position/query/README.md)は固定版で復元できる。過去の承認を新たな実行権限として使わない。

## 検証と限界

公開候補45パスについて、現行32件のREADME到達、Queryの意味・全文、コードフェンス、相対リンクとanchor、旧配置の除去、変更したSKILLの差分、必要なmetadata・EOF・Bindingを確認した。Hubは185,488 bytesから27,285 bytesへ縮小した。独立レビューは新しいAIに現物と目的を渡した文書検査であり、全Skillの実行試験や自然発動の実証ではない。

GitHubの保存後はmainのcommitと変更ファイルの実体を再取得し、公開候補と照合する。現在のGitHub共有版、個人Skillの登録版、会話内の読取表示、Humanの使いやすさは別の成果である。未知の外部bookmarkが旧Queryのmain URLを参照している可能性は残る。固定履歴からの復元先を示すが、外部参照の全件修復を主張しない。

## 公開後の確認

公開後の実測結果をここへ追記する。

EOF::STR_021_SKILL_README_QUERY::v001
