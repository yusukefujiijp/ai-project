---
title: "Reports — 根拠から意味を読み、次の理解へ渡す"
canonical_path: "artifacts/reports/README.md"
version: "v003"
created: "2026-10-25"
updated: "2026-10-25"
updated_reason: "Separate collection-wide guidance from dated reading routes; relocate the initial thirteen reports and coverage appendix under 2026-10-25 with Human approval."
role: "Report collection entry, reading routes and revision guidance; not a second Current state"
primary_reader: "Human / Current AI / Future AI"
initial_collection_source_commit: "ba47216debeb2163a5dbf880c6b37d73edbb7e41"
expected_eof: "EOF::ARTIFACTS_REPORTS_HOME::v003"
---

# Reports

**何について、何が分かり、それがどんな意味を持つかを、根拠とともに伝えるReportの入口。** Humanが理解・比較・判断する用途と、AIが後から根拠を確かめ、別の問いへ発展させる用途の両方を扱う。

調査、比較、考察、活動、検証、進捗、結果など、内容に合う形で育てる。残作業は重要な題材の一つであり、このCollection全体をTask管理専用にはしない。全Reportへ同じ章立てや提言を強制せず、理解を深めて完結する作品も置く。

## 日付別の入口

- [2026-10-25 — 初回の13本と読取付録](2026-10-25/README.md)：協働の入口、完成と証拠、AIへのReport、想起、Currentと歴史、経験からの学習、成果物の到達、研究と編集など。問い別の一覧と読み方は日付側にある。

日付は収納の軸、問いや目的は読む先を選ぶ軸である。日付を覚えていることや全Reportを読むことを利用条件にしない。AIは現在の問いから必要な作品と原本へ接続する。親の一覧は各まとまりの所在と概要を示し、個々の作品の案内は日付側READMEが所有する。日付をまたぐ読み方は実際の利用に応じて育て、本文の複製や全分野の先回りした分類を増やさない。

## 原本とReportの分担

事実・現在状態・経験・方法は、各DomainやSkill等の所有原本に戻る。Reportはそれらを編集・比較し、意味や候補を示せるが、第二の可変Stateや指示原本を作らない。現在の仕事へ利用するAIは、Reportの観測時点と現在のHuman指定、必要なCurrent原本を照合する。明示Bindingや必須読解を、Reportの要約で代替しない。

Reportの存在や提案は、採用・送信・実行・予定変更の権限ではない。現在の有効な委任があれば、その範囲は必要な検証まで進める。読むだけで新しいTaskを発生させず、未採用の分析や通常のUnknownを宿題へ変えない。

既存の[Repository Living Review](https://github.com/yusukefujiijp/ai-project/blob/main/repository-reviews/README.md)は時点間のRepository比較とその方法を、[AI-MammothのReport入口](https://github.com/yusukefujiijp/ai-project/blob/main/agents/muse/artifacts/report/README.md)はそのActor側のReportを所有する。この入口を、それらの自動移設・統合の指示にしない。

Root・Teshuvah・Human Foreground One・Correction・STOPとGuardは[ARK](https://github.com/yusukefujiijp/ai-project/blob/main/ARK.md)と[AGENTS](https://github.com/yusukefujiijp/ai-project/blob/main/AGENTS.md)を保持する。ReportやAIはKeliである。

## 保存と育て方

新しいReportは、原則として初回公開日の日本時間に対応する`YYYY-MM-DD/`へ保存する。既存作品の訂正・改訂は同じ住所で行い、更新日・版・Git履歴で変化を辿る。日付が変わるたびに既存作品を移し直さない。観測日・参照commit・対象読者はそれぞれの意味で保持し、同じ日付に入ることを同じ根拠や読者方針の証明にしない。

新しい問い・観測・比較として独立した価値がある場合は、新しいReportにできる。同じ作品の訂正・説明改善は既存ファイルを改訂し、既存作品への接続で目的を満たせる場合は、その入口を案内する。依頼の件数を新規ファイル数へ機械的に変換せず、全Reportに固定の命名・章数・長さを課さない。

誤りの訂正は理由と根拠を残して行い、当時の観測を後のCurrentで黙って塗り替えない。作品固有のFeedbackと、共通の執筆方法へ戻す学びを分ける。保存・登録・読者の理解・実利用効果も別々に扱う。

新しい作品の保存では、AIが日付側の収録案内と親の入口を必要な範囲で整える。日付側READMEは目的・収録作品・読み方・必要な根拠への接続を持ち、共通規則を全文複製しない。一つの作品の本文は一つの住所で育て、必要な複数の入口からそこへ接続する。年・月などの追加階層や索引は、実際の探索・更新の負担に応じて検討する。

必要なREADMEとRemote再取得は[Artifacts](https://github.com/yusukefujiijp/ai-project/blob/main/artifacts/README.md)および[保存契約](https://github.com/yusukefujiijp/ai-project/blob/main/prompts/artifact-to-github.md)へ接続する。全操作ログや私的会話を複製せず、公開可能な素材と現在の承認範囲を保つ。

## 初回作品の配置変更

2026-10-25、継続生成による直下のファイル増加についてのHuman Feedbackと実行承認に基づき、初回13本と読取付録を[2026-10-25/](2026-10-25/README.md)へまとめた。既存のファイル名・本文の分析・根拠・対象読者を保持し、各作品の住所情報と版を整合した。

旧`artifacts/reports/2026-10-25-*.md`の作品は、同じファイル名で`artifacts/reports/2026-10-25/`にある。移動前の一覧と本文は[固定版のREADME](https://github.com/yusukefujiijp/ai-project/blob/cb9c3a80cd73378fa97e4293fca4013e0d52a84e/artifacts/reports/README.md)から辿れる。この履歴への接続を旧main URLの自動転送とは扱わない。配置変更は、分析の再実施や実利用効果の確認を意味しない。

EOF::ARTIFACTS_REPORTS_HOME::v003
