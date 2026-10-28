---
id: STR-024
title: Harness初版 — 読み取り専用Repositoryレビューの実行補助
version: 0.1.0
created: 2026-10-29
updated: 2026-10-29
status: foundation-implemented / remote-and-live-trial-follow
scope: root harness 17 files; additive adoption record and narrow entry links after trial
---

# STR-024 — Harness初版

## Humanの採用と境界

Humanは今回の設計を採用し、`yusukefujiijp/ai-project`直下の`harness/`へ17ファイルの初版、必要なテスト、一件の重点Repositoryレビュー、成果と最小証跡の保存、GitHubへの導入記録とRemote確認を依頼した。入口掲載は通し試験後の限定差分とする。試験で発見した改善の実装、既存ファイルの移動・削除、Root文書統合、製品設定変更、自動実行の設定は対象外。

実装開始のmainは`79770085364871cd026cb12ff669593fbf6cf6f4`。適用原本はAGENTS v004.12-candidate、artifact-to-github v001-human-authorized、ARK v003-candidate、現行keybindings、Rootと各所有入口。公開準備中にmainが`1e8399449a09f83e34d255bdc246060c33f96e9c`へ進み、Ark-OKF等の他担当成果を確認した。公開は最新headのtreeを基礎にし、期待head一致を条件にする。

Home Bは既存Mainの根本再設計に属し、その比較・本文案の進展と統合実装の権限を分ける。Main27、Support28、Ark29、Ark30の現在と受入れは[Domain入口](../../ark-project/README.md)と各Stateが所有する。本件はそれらを再定義・巻戻ししない。Report／Feedback・共有References・他担当の成果も既存所有先へ残す。

## 構成と理由

実装の所有は[`harness/README.md`](../../harness/README.md)。Actorから独立した仕事の接続なのでRoot直下に置き、`agents/harness/`へ所属させない。方法は[`repository-reviews/review-prompt.md`](../../repository-reviews/review-prompt.md) v002を固定commitから読む。本文をHarnessへコピー・移設しない。

17ファイルはREADME、pyproject、uv.lock、Profile、Work Adapter、六つのPython原本、三つのtest、合成fixture、eval READMEと合成JSONL。個別の配置・所有内容・読む相手・更新条件はHarness入口に記載した。run状態・原本cache・Report・証跡はソースRepository外へ置き、これらを17原本と混ぜない。

利用環境から、ChatGPT Work上のGitHub読取ConnectorとPythonを選んだ。PythonからConnectorを直接呼び出せるとは仮定せず、HostがToolの返却を正規化して渡す。Python 3.12.14、uv 0.13.4を観測。既存Pydanticを使う案は、オフライン解決用の依存cache不足を確認したため、外部依存ゼロの標準ライブラリ実装へ調整した。`uv.lock`は実生成済み。新しいAPI Key・製品設定・daemon・予定を要求しない。

取得byteのGit blob照合、固定Snapshot、読解範囲の申告、根拠行と出力hashの検証、中断・別process再開、POSIX単一Writer、結果のcomplete/partial、証跡ZIPの読み戻しを実装した。Human向けReportはmedia typeを持つ自由形式で、Markdownだけに固定しない。

## 公開前の機械検査

`PYTHONPATH=src uv run --frozen --offline python -m unittest discover -s tests -v`で**30件pass**。`uv lock --check --offline`も成功した。主要な反例は、EOFだけを残した中間欠落、別commit混入、未知版・型・重複キー、symlink・パス逸脱、読解範囲外の根拠、必読未完、再開時のcache・コード・入力改変、同時Writer、既存run上書き、HTML成果物の改変、歴史リンクをmainで評価する誤り。

これらは合成入力による機械検査。意味的な理解、独立した別AI、Humanの利用効果の実証ではない。evalsの六つの合成事例も、保存しただけで評価成功とは扱わない。

## 段階切替と観測記録

1. 初版17ファイル・この記録・生成物の限定ignoreを保存する。入口掲載はまだ行わない。
2. 全保存ファイルをRemoteから再取得し、意図したbyteと照合する。
3. 公開した固定コードを使い、Root・入口・文書役割、Main／Support／29／30との責務、Report／Feedback、Harnessの原本と成果の境界を重点として、一件の読み取り専用レビューを行う。
4. Reportと最小証跡を保存・確認した結果に応じ、Root README・Repository Review入口・変更記録索引を限定更新する。改善提案は記録に留める。

この初回commit時点では、2–4は未確認。実際のrun、対象commit、保存確認、入口掲載の成立は後続の本記録で追記し、予定を成功として先取りしない。

## 能力の境界と復元

初版のread-onlyはReview操作の契約であり、Hostから書込Toolを除去する強制sandboxではない。PythonにはGitHub書込APIも対象コード実行もないが、Host全体の権限分離、Windows、外部URL・anchorの自動網羅、別AIによるcold start、反復利用効果は未確認。

原本取得と読解申告、機械合格と意味判断、ローカルZIPと永続保存、ReportとHuman Feedbackを別に扱う。証跡ZIPは原本cacheを含まないため、完全なRepository backupや単独で再開できるrun backupとは呼ばない。

復元は、利用案内の限定差分を外して従来のReview Prompt直接利用へ戻せる。コードとrunは固定版の証拠として保持できる。既存ファイルの移動・削除がないため転送Stubや原本移設の逆操作は不要。後続mainに他担当変更がある場合は本件の差分だけを戻し、main全体を過去へresetしない。固定履歴リンクは書き換えない。
