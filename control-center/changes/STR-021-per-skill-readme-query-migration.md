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
status: "GitHub migration and two registered-skill navigation saves verified; conversation retrieval differs by route"
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

2026-10-20、Codexが[実装commit 91d859d](https://github.com/yusukefujiijp/ai-project/commit/91d859d466b6fc5071ede9ddb39035e58ccf5fff)をmainへ公開した。公開前の基点一致を確認し、期待する旧headを指定してRefを更新した。GitHub上のtree `8c6fa6462f34eab87ec919da1f5158fa7a5702ee` は検証した候補treeと完全一致した。

変更後の43本文をmainから再取得し、候補の全文と一致することを確認した。削除対象2件を含むQuery専用フォルダはtree上に残っていない。対象外609ファイルは基点とblob・modeが同じであり、並行更新や別の成果を巻き戻していない。保存後のmain先端も実装commitと一致した。

旧Hubの14 QueryとMAPの2 Query、現行32件のREADME、内部リンク・anchor、コードフェンス、SKILLの3箇所の案内差分、Ark28:06の17 SourceとREADME/Handoff/StateのBindingを確認した。独立した文書レビューでも公開を妨げる不整合は検出されなかった。これらは移行整合と保存の確認であり、全Skillの実行試験・全Runtimeでの取得・利用効果の証明ではない。

### 登録済み二Skillの案内整合

GitHub公開後、`resolve-github-runtime` と `markdown-to-html` の既存登録物でも、共有SKILLと同じREADME案内の一行へ更新した。元の作業木には他の未commit変更と旧版が残っていたため、最新Remoteの本文と旧共有版の一致を確認して隔離作業先を使用した。README本体の複製や、新しい登録物の作成は行っていない。

二件を同時にpushする試行はHTTP 422となり、Remote未反映を確認した。同じ正規経路で一件ずつ保存し、runtimeは登録commit `6b12139a5316a037815ae2120737eca5a699e724`、Markdownは `ab410f4dc59e22a68445d45d68ad35c19877073a` で成功した。422の原因は未特定であり、保存成功だけで原因を解決済みとは扱わない。

保存後Remoteの2本文は共有版と全バイト一致した。runtimeは8,956 bytes／blob `0bf35e2e30bb26777002869a4bb67d7eecccda72`、Markdownは10,644 bytes／blob `a7d4e62e896ec39744876c651803a9ae8a0e2d24`。本対話のCloud Skill読取経路でもruntime本文を末尾まで取得し、新しいREADME URLを含む共有本文との完全一致を確認した。

その後、環境の公開Skill一覧が更新され、Cloud Skill経路は利用できなくなった。現在宣言されたexecutor経路でMarkdown Skillを読むと8,585文字の旧本文が返り、新しいREADME案内は含まれなかった。登録先の新本文保存と、この会話の読取結果を分ける。差が生じた原因・会話側の更新時点は未確定であり、保存失敗と断定したり、旧作業木を根拠に登録本文を戻したり、同名Skillを再作成したりしない。UIの自然な選択や各処理の実行結果も別の確認である。

担当AIによる上記二commitでは、対象外109エントリのblob・modeと全pathを保持した。保存後の登録Remoteには別の後続commit `58c161c453c6ecf41deb1b4be62252ec390e8a1c`（表示メッセージ `Materialized from stored content`）があり、Markdownの `assets/icon.svg` だけが変更された。二SKILL本文と他108エントリは同一。このアイコン差分は本作業の二commitに含まれず、主体・原因は未確定のため巻き戻していない。GitHub共有資源の変更として報告せず、登録先の後続観測として区別する。

この追記自体の保存後照合は本対話の完了報告で扱い、自己SHAを更新し続ける記録の連鎖を作らない。

EOF::STR_021_SKILL_README_QUERY::v001
