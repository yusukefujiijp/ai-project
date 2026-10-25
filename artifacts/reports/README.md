---
title: "Reports — 根拠から意味を読み、次の理解へ渡す"
canonical_path: "artifacts/reports/README.md"
version: "v001"
created: "2026-10-25"
role: "Report collection entry, reading routes and revision guidance; not a second Current state"
primary_reader: "Human / Current AI / Future AI"
initial_collection_source_commit: "ba47216debeb2163a5dbf880c6b37d73edbb7e41"
expected_eof: "EOF::ARTIFACTS_REPORTS_HOME::v001"
---

# Reports

**何について、何が分かり、それがどんな意味を持つかを、根拠とともに伝えるReportの入口。** Humanが理解・比較・判断する用途と、AIが後から根拠を確かめ、別の問いへ発展させる用途の両方を扱う。

調査、比較、考察、活動、検証、進捗、結果など、内容に合う形で育てる。残作業は重要な題材の一つであり、このCollection全体をTask管理専用にはしない。全Reportへ同じ章立てや提言を強制せず、理解を深めて完結する作品も置く。

## 今の問いから読む

2026-10-25の初回Collectionは、Repository全体の構成確認と主要原本の横断読解から生まれた10本。各Reportは単独でも読める。番号は読書順の目安であり、実行順序やTask番号ではない。

| Node | Edge — この問いから読む | Report |
|---|---|---|
| 1. 入口と責任 | 短い依頼 → AIが担う深い整理 | [一つの入口の背後に、複数の責任を残す](2026-10-25-one-entry-many-responsibilities.md) |
| 2. 完成と証拠 | 保存・接続・理解・効果 → 正しい次の判断 | [完成状態を平らにしない](2026-10-25-completion-and-evidence.md) |
| 3. AIへのReport | 観測と解釈 → 受け手の独立した判断 | [AIからAIへのReport](2026-10-25-ai-to-ai-report.md) |
| 4. 戻る支援 | 想起・開始・移行・文脈欠損 → 適した支援 | [戻る支援には、異なる切れ目がある](2026-10-25-four-kinds-of-reconnection.md) |
| 5. Currentと歴史 | 当時の記録と現在の原本 → 巻き戻さない理解 | [Currentと歴史を同時に読む](2026-10-25-current-and-history.md) |
| 6. 経験から学ぶ | 成功と訂正 → 条件を保つ再利用 | [成功は何を再現し、訂正は何を守るのか](2026-10-25-learning-from-success-and-correction.md) |
| 7. 成果物の到達 | 内容・媒体・入口 → 読む／見る／聴く場面 | [成果物が届くとは何か](2026-10-25-artifacts-that-reach-the-reader.md) |
| 8. Reportの核 | 目的・素材・読者 → 汎用的な執筆判断 | [汎用Reportを小さな核から育てる](2026-10-25-small-core-for-general-reports.md) |
| 9. 別領域への横展開 | GitHub整理の知見 → 居室固有の条件 | [GitHub整理から居室整理へ](2026-10-25-transferring-methods-to-room-care.md) |
| 10. 自由度と継続 | 創発・Root・現在の権限 → 戻れる協働 | [自由度を、戻れる協働へ結ぶ](2026-10-25-freedom-and-recoverable-continuity.md) |

全体像からなら1→2→10、AI→AI Reportを深めるなら3→5→8、生活への接続を考えるなら4→9→7が読み方の一例になる。すべてを読むことを利用条件にしない。

## このCollectionから見えてきたこと

今回の横断分析では、蓄積した判断を、現在の条件で再び使えるようにする構造が複数領域に現れた。入口を短くする、原本の責任を分ける、過去とCurrentを区別する、受け手への到達を確かめるという工夫は、別々のGoalを支えながら関係している。

この共通点は、全Skillや全領域を一つのSystemへ統合する結論ではない。似た構造の中にある違いを読み、使う場面を選ぶための分析である。各Reportは重要な反例・限界を残し、推論や候補を実装済み・実証済みへ変えていない。

## 根拠と読取範囲

分析基点は[commit ba47216debeb](https://github.com/yusukefujiijp/ai-project/tree/ba47216debeb2163a5dbf880c6b37d73edbb7e41)。全体Treeの1,001項目・689ファイルを確認し、48資料について全文または明示した範囲を実際に読んだ。46本文の全文読解・同一性を確認した既読再利用、空Seed一つの確認、PLAN一つの部分読解を区別する。

**全Repositoryの全文読了や、全案件の現在状態の監査を完了したという意味ではない。** 読んだ原本・Git blob・未読範囲・確認境界は[読取付録](2026-10-25-reading-scope.md)へ。各Reportの引用は固定版へ戻れる。

既存の[Repository Living Review](../../repository-reviews/README.md)は時点間のRepository比較とその方法を、[AI-MammothのReport入口](../../agents/muse/artifacts/report/README.md)はそのActor側のReportを所有する。今回それらを移設・統合せず、Humanが指定した共通のReports領域へ主題別の作品を置いた。過去の全Reportに対する新規性比較は行っていない。

専用のwrite-report共有原本・同名の登録実体は、今回確認した範囲では見つからなかった。既存のwrite-text・save・自己改善Loopの方法で制作を進めており、専用Skillの作成・登録まで完了したとは扱わない。

## 原本とReportの分担

事実・現在状態・経験・方法は、各DomainやSkill等の所有原本に戻る。Reportはそれらを編集・比較し、意味や候補を示せるが、第二の可変Stateや指示原本を作らない。現在の仕事へ利用するAIは、Reportの観測時点と現在のHuman指定、必要なCurrent原本を照合する。明示Bindingや必須読解を、Reportの要約で代替しない。

Reportの存在や提案は、採用・送信・実行・予定変更の権限ではない。現在の有効な委任があれば、その範囲は必要な検証まで進める。読むだけで新しいTaskを発生させず、未採用の分析や通常のUnknownを宿題へ変えない。

Root・Teshuvah・Human Foreground One・Correction・STOPとGuardは[ARK](../../ARK.md)と[AGENTS](../../AGENTS.md)を保持する。ReportやAIはKeliである。

## 保存と育て方

作品の安定した住所を使い、改訂は同じファイルとGit commitで辿る。今回の作品は日付と題材で識別したが、全Reportに固定の命名・章数・長さを課すものではない。別の観測として残す価値がある時は、その違いを説明して新しいReportにできる。

誤りの訂正は理由と根拠を残して行い、当時の観測を後のCurrentで黙って塗り替えない。作品固有のFeedbackと、共通の執筆方法へ戻す学びを分ける。保存・登録・読者の理解・実利用効果も別々に扱う。

新しい作品を保存する時は、この入口から目的に応じて辿れるようにする。必要なREADMEとRemote再取得は[Artifacts](../README.md)および[保存契約](../../prompts/artifact-to-github.md)へ接続する。全操作ログや私的会話を複製せず、公開可能な素材と現在の承認範囲を保つ。

EOF::ARTIFACTS_REPORTS_HOME::v001
