---
title: Ark Harness — Repository Review
version: 0.1.1
implementation_version: 0.1.0
status: initial-implementation
updated: 2026-10-31
updated_reason: 公開例・データ受渡し・状態別の利用説明と回帰検査を改訂。実行実装とHome Bの所有案内を保持。
home_b_alignment:
  design_date: "2026-10-31"
  design_base_commit: "358c1c2b4f20f2de1f97cd33bec8a13278e0df33"
  source_thread: "Ark27:12"
  scope: "Staged Home B meaning ownership and navigation; preserve explicit Source contracts, prior evidence and other owners"
---

# Ark Harness

本書とWork Adapterの文書版はv0.1.1、実行実装はv0.1.0、交換schemaは1。文書・回帰検査の改訂を、実行コードの版や新しい能力の導入と混同しない。

依頼、固定した原本、読解範囲、検証、成果物を一件の仕事として接続する実行補助。初版は **ChatGPT Work + GitHub読取Connector + Python 3.12以降のPOSIX環境**を対象にする。レビュー方法の原本は[Repository Review Prompt](../repository-reviews/review-prompt.md)。Harnessはその方法を複製・移動せず、実行時に固定commitから取得する。

RootとHuman–AI協働の意味は[Home](../README.md#ark-identity)、共通の権限・読取・実行契約は[AGENTS.md](../AGENTS.md)が所有する。初版の導入理由・観測結果・未確認事項は[STR-024](../control-center/changes/STR-024-harness-repository-review.md)を参照する。

## 配置と所有

`harness/`をRoot直下に置く。複数のActorが使える仕事の実行補助であり、[agents/](../agents/)配下のActorのIdentity・Current・予定を所有しない。ActorはHarnessを利用できるが、Harnessから特定ActorのRuntimeを必須依存にしない。`agents/harness/`はこの関係を逆に読ませるため初版では採用しない。

原本と実行状態を混ぜない。GitHubに置くのは以下の**17ファイル**。実行中のrun、取得キャッシュ、結果、製品設定はこの棚へ書かない。

| 配置先 | 所有する内容 | 読む相手 | 更新条件 |
| --- | --- | --- | --- |
| `README.md` | 目的、所有境界、構成、利用入口、能力の限界 | 利用AI、Human、保守担当 | 責務・構成・利用条件が変わる |
| `pyproject.toml` | Python要件、プロジェクト版、依存方針 | uv、保守担当 | 実装版・依存・Python要件が変わる |
| `uv.lock` | uvが解決した依存状態 | uv、保守担当 | pyproject変更後に実際に再生成する |
| `profiles/repository-review.toml` | 対象Repository、方法・入口の原本Path、初版の操作範囲 | Python、Host AI | 接続する原本Path・対象・能力契約が変わる |
| `adapters/chatgpt-work/README.md` | Work ConnectorとPythonの間の具体的な受渡し手順 | Work上の実行AI | Toolの返却形式・Host・保存経路が変わる |
| `src/ark_harness/__init__.py` | 実装の版 | Python、保守担当 | コード版が変わる |
| `src/ark_harness/__main__.py` | CLI、単一Writer、入出力 | Host AI、Python | 操作とCLI契約が変わる |
| `src/ark_harness/contracts.py` | 型、版、必須欄、相互条件、生成schema | Python、入力作成AI | データ契約が変わる。旧runとの互換性を明示する |
| `src/ark_harness/sources.py` | 原本のbyte照合、パス、読解範囲、ローカル保存 | Python | 取得・読解・byte保存の検査が変わる |
| `src/ark_harness/review.py` | runの開始、中断、再開、終了、証跡束 | Python | 一件の仕事の状態遷移・保存が変わる |
| `src/ark_harness/checks.py` | 結果・根拠・成果物・指定リンクの機械検査 | Python、検証担当 | 検証可能な条件が変わる |
| `tests/test_sources.py` | 原本・型・パス・読解の回帰検査 | unittest、保守担当 | 対応する挙動・不具合が変わる |
| `tests/test_review.py` | 状態遷移・復旧・成果物保存の回帰検査 | unittest、保守担当 | 対応する挙動・不具合が変わる |
| `tests/test_checks.py` | 結果と参照の回帰検査 | unittest、保守担当 | 対応する挙動・不具合が変わる |
| `tests/fixtures/repository-review.json` | 合成Repositoryの最小検体 | テストのみ | 検査に必要な合成条件が変わる。実原本を転記しない |
| `evals/README.md` | 意味・利用効果の評価手順と観測区分 | レビュー担当、Human | 評価目的・観測方法が変わる |
| `evals/cases/repository-review.jsonl` | 意味的な取り違えを評価する合成事例 | レビュー担当 | 現実の失敗から評価条件が増える |

レビューの依頼文・方法・経験原本を増設しない。`repository-reviews/`は方法とその領域の記録、`control-center/changes/`は導入変更、既存のReferences等は適用される経験契約を所有する。今回の初版からActorログ、lesson、Board、Report／Feedbackの新しい保存義務を作らない。配布された製品内の設定やSkillが存在しても、GitHub原本と同一と推定しない。

## 実行の入口

実際のTool接続は[Work Adapter](adapters/chatgpt-work/README.md)へ。初版はPython標準ライブラリのみを使う。ConnectorはWorkのHostから呼び、Pythonが認証情報やTool関数を取得する仕組みにはしない。対象Repositoryのコードは実行しない。

Repositoryのcheckoutルートから、既に利用可能なPythonで実行できる。

```sh
PYTHONPATH=harness/src python3 -m ark_harness --help
PYTHONPATH=harness/src python3 -m unittest discover -s harness/tests -v
```

uvがある環境では、`harness/`内で次を利用できる。オフラインでも対象Python自体が導入済みである必要はある。

```sh
uv lock --check --offline
PYTHONPATH=src uv run --frozen --offline python -m unittest discover -s tests -v
```

`uv.lock`は実際に生成したもの。外部依存を追加する場合は取得経路・lock・再構築を再検証する。`pip install`、製品登録、常駐process、API Key、予定実行は初版の成立条件ではない。

## 原本・実行状態・成果を分ける

runディレクトリはソースRepositoryの**外**に新規作成する。名前はHostが選べる。以下は実行時に生成されるもので、上記17原本の追加ではない。

| run内のPath | 内容・所有 | 更新条件 |
| --- | --- | --- |
| `request.json` / `profile.json` / `tree.json` | 受領依頼、利用Profile、固定Snapshot | 開始時に固定。以後hash照合。変更する仕事は新run |
| `run.json` | run ID、時刻、対象commit、tool commit、コードhash、状態 | 状態遷移時。Hostの権限を授与するファイルではない |
| `trees/<commit>.json` | 必要時の固定履歴Snapshot | `add-tree`。現用mainへ歴史リンクを差し替えない |
| `objects/<blob-sha>` | 照合済みUTF-8原本cache | `ingest`。正本は元Repositoryの固定commit |
| `sources.json` | Path・commit・blob・SHA256・byte数・行数・読解申告 | 取得と読解申告時。取得だけで既読にしない |
| `events.jsonl` | 開始、取得、読解、中断、再開、障害の最小事実 | 各操作時。会話全体や内部思考は保存しない |
| `deliverables/*` | Human向けReport等 | Hostが用途に応じて作成。Markdown、HTML、PDF等を選べる |
| `result.json` / `validation.json` | 結論・根拠・残点と機械検査結果 | `finish`。失敗ならrunはactiveのまま |

`bundle`は検査に受理された`complete`／`partial`の必要記録と申告済み成果物をZIPへ保存し、全memberを読み戻して照合する。原本cacheは含めない。**証跡ZIPはRepositoryの完全backupや、展開だけで再開できるrunのbackupではない。**通常の再開には記録と一致する実装コード、不変入力、登録済み原本cacheが必要。登録済みcacheが欠けると`status`や通常の`ingest`も失敗し得る。原本の再取得可能性と旧runの修復能力を分ける。現行CLIに完全復元・cache修復の専用操作はない。状態別の続行判断と新runへの接続は[Work Adapter](adapters/chatgpt-work/README.md)を参照する。固定commitが将来も取得可能とは保証しない。

ローカルZIPの成立と永続保存は別。Hostは利用可能な成果物保存先へReportとZIPを保存し、返却ID・保存状態を確認してHumanへリンクを渡す。初版のPythonにLibraryやGitHubへの書込APIはない。成果物保存用の認証情報をrunへ書かない。

## 検証と復旧

JSONは未知の版・欄・重複キー・型変換を拒否する。原本はtreeのblob SHAとGit blob計算、byte数を照合する。EOFがあるだけでは全文一致と判定しない。取得済みsourceへの読解申告を範囲で記録し、結果の根拠行がその範囲内にあることを検査する。必読原本の全文申告が不足したまま`complete`にはできない。

`paused`は`resume`できる中断状態、`complete`／`partial`は終了状態である。`active`では現物を確認して未完の工程から続け、`resume`は使わない。`partial`の残点を続ける判断と、`paused`を再開する操作を混同しない。終了したrunでも、証跡化やHostによる永続保存が残っている場合は、現在の委任内でその工程を進められる。

`pause`で中断理由を記録する。`resume`は現在も有効な依頼・STOP・権限をHostが確認して理由を渡し、同じ実装コード・不変入力・cacheを再照合してから進む。mainが進んでも途中で対象版を変えず、終了時commitとの差分評価を結果へ書く。終了状態を手で`active`へ戻さず、レビュー続行は現在の依頼と新runの必要性から判断する。

CLIはPOSIXのadvisory lockで`status`・`show`を含む同じrunの操作を排他的に扱う。逐次進め、中断や応答欠落後は現物を確認して成功済み操作を重複実行しない。lock取得はローカルの`.writer-lock`を作成し得る。ファイル単位のatomic replaceは、全操作を一括して戻せるtransactionではない。整合性不足で`status`が失敗する場合もある。開始途中で`run.json`等が不足する場合は旧状態を保持し、新runの必要性を判断する。hash不一致や不明な状態を自動修復し、状態名だけを手で変更して完了・復旧扱いにしない。

取得失敗等で依頼範囲を閉じられない時は、必要な整合性検査を通した`partial`と残点を保存できる。未取得の資料と登録済みcacheの破損は別であり、後者を`partial`の指定だけで回避できない。`finish`の終了code 0は検査に受理されたという意味で、`partial`を`complete`に昇格しない。code 1は結果検査不合格で、result・validationが保存されrunは`active`に残る。code 2は入力・実行エラーだが、処理中断や応答欠落と同様に操作が一切行われなかった保証にはしない。`status`成功だけで結果・成果物・永続保存まで確認済みとは扱わない。schemaは`python -m ark_harness schema result`等でコードから生成できるが、行範囲や複数欄の関係などの意味的条件は実際のCLIでも検証する。

## 初版が証明しないこと

- 読解申告はHostの申告。理解・主張の真偽・Reportの分かりやすさをhashで証明しない。
- `repository_writes=false`は利用契約。Work全体からGitHub書込Toolを技術的に除去するsandboxではない。今回のReview操作はHostがGETに限定する。
- 指定されたファイル参照の存在は確認できるが、全Markdown構文、anchor意味、外部サービス、製品内の設定反映は自動検査しない。
- Windows、別製品、別AIのcold start、反復利用の効果はこの初版の試験だけでは確認されない。
- 人間向けReportは自由な形式。`result.json`は根拠と検査の交換形式であり、HumanへJSONやMarkdownだけを強制するUIではない。

問題があれば入口の利用案内だけを外して使用を止め、固定commitとrunを残す。既存のReview Promptを直接利用する経路は保たれる。コードの修正・退役はその時の権限とmainに従い、共有Root・Actor・製品設定を巻き戻さない。
