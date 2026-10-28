# Repository Review evaluations — v0.1.0

この棚は、機械テストだけでは分からない**意味の取り違え**を観察する。方法の原本は[Review Prompt](../../repository-reviews/review-prompt.md)。ここへ別のReview方法を作らない。

`cases/repository-review.jsonl`は合成事例。実Repositoryの最新状態やHumanの評価を転記した証拠ではない。実行AIは提示された状態から判断を述べ、期待する区別と照合し、根拠・観察者・対象版・未確認条件を記録する。schema_version/id/input/expected_observationを持つ。ケースをロードできることと、AIが意味を理解したことを別に扱う。

初版に自動LLM grader、点数集計、別AI起動は含めない。合成ケースの存在やunittestのpassを、これらの評価の合格と報告しない。必要な実地試験は、重点範囲を明示した一件の読み取り専用Repositoryレビューとして実施する。Report・最小証跡・導入記録へ、実施した評価と未実施の評価を分けて残す。

観察点は、原本と配布先、準備済みと実行中、現在の依頼と過去の報告、取得と読解、機械検査とHumanの利益を区別できるか。失敗が観測されたら再現に必要な条件を合成してケースを追加する。実データ・個人情報・会話全体をfixtureへ複製する必要はない。

利用回数・別AI・別環境・Human Feedbackが増えた時は、その観測条件で再評価する。一件の成功から普遍的な有効性を認定せず、今回のレビューから改善実装の新権限を作らない。
