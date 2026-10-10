---
title: "Artifact → GitHub / Programming-like — 保存手順の構造を理解する"
version: "v001-human-authorized"
edition: "First explicit version in the modernized companion series"
canonical_path: "prompts/artifact-to-github-programming-like.md"
role: "AI-native learning and review companion; non-executable pseudocode"
status: "active companion / Human-authorized modernization / field effects unverified"
created: "2026-10-10"
updated: "2026-10-10"
semantic_owner: "artifact-to-github.md"
reviewed_owner_version: "v001-human-authorized"
replacement_for_main_card: false
source_path: "ss_super-special/artifact-to-github_programming-like.md"
source_commit: "0d21990a126948703eca517c65017f2038d4393c"
source_blob: "6643dad308fcf862d5d4670ce80b3d36fc37ca3e"
change_record: "../control-center/changes/STR-014-super-special-prompt-modernization.md"
expected_eof: "EOF::ARTIFACT_TO_GITHUB_PROGRAMMING_LIKE::v001-human-authorized"
---

# Artifact → GitHub / Programming-like

**保存手順を、入力・状態・条件分岐・不変条件から理解し、抜けや矛盾を発見するためのPrompt。**

## 1. 起動と主カードの関係

使う場面は、GitHub保存の手順を構造的に学びたい時、複数の条件が混ざって判断を誤りそうな時、主カードの改善点を検討する時。通常の保存では[主カード](artifact-to-github.md)だけを選べる。

起動例：

> Artifact → GitHubの主カードとこの補助版を読み、今回の状況を入力・状態・分岐・不変条件で説明してください。観測した事実と仮定を分け、判断が変わる条件を示してください。実行範囲は現在の依頼に従ってください。

この本文と主カードをmetadataから各Exact EOFまで読む。同一会話で同一blobの全文読解を確認済みなら再利用できる。読んだ主カードの版を区別し、reviewed_owner_versionを将来のCurrentを固定するBindingと解釈しない。主カードが変われば関係する分岐を再確認する。未取得なら準拠した保存判断をしたとは言わず、不足と回復先を示す。

主カードが保存手順の意味を所有する。本書はその理解を助け、別の権限契約・第二の実行エンジンを作らない。疑似コードのIMPORTや関数名は説明記法であり、実際の読込・同期・API・自動検証を実行しない。齟齬を見つけたら、版と根拠を示して主カードに照らす。主カード自体と上位契約が衝突する時は適用契約に従う。

Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah、Human Foreground Oneは主の完全勝利。HumanはMeaning・Correction・STOP・Final Sealを保持し、AI・このモデル・GitHubはKeliである。Guard・Source契約・アクセス制御を保持する。分析の依頼から保存実行を推定しない。

## 2. 状況を型として読む

下記は固定入力Schemaではない。今回の判断に必要な項目を現在の文脈から解決し、未確認はUnknownのまま残す。

```text
Context
  purpose            : 今回の成果と完了条件
  authority          : PLAN_ONLY | AUTHORIZED_SCOPE | STOPPED | UNCLEAR
  source             : 本文またはバイト / 完成度 / 版と根拠
  target             : repository / ref / path / owner
  current_snapshot   : 内容 / blob / commit / 観測時点
  intended_change    : CREATE | UPDATE | MOVE | DELETE | NO_CHANGE
  dependencies       : 一緒に整合させる本文・案内・契約
  operation_result   : SUCCESS_REPORTED | FAILURE_CONFIRMED | UNKNOWN | NOT_ATTEMPTED
  remote_evidence    : 実取得内容と意図の比較 / 不足
```

Authorityは「Toolがあるか」と別、sourceの完成度は「保存されたか」と別、operation_resultは「内容を検証したか」と別である。同じ成功という語へ圧縮しない。

## 3. 不変条件から見る

INVARIANTは、ある経路だけでなく全経路で守る意味を表す。

1. 主カードと現在の依頼が定める権限を、説明用モデルが増やさない。
2. 同一結果の有無が不明なら、再実行より先にCurrentを確認する。
3. 並行変更・未知のデータを保持し、衝突を黙って上書きしない。
4. 複数ファイルの整合が必要なら、その関係を一組として検討できる。
5. 保存の応答、Remote検証、Manual Pack準備、実利用の効果を区別する。
6. 拒否・STOPを技術的失敗として扱い、手動経路へ逃がさない。

この一覧は主カード§2–7の構造化された読み方である。実際の手順や境界が変わったら主カードへ戻る。

## 4. 状態と遷移

| 状態 | 何を観測したか | 次の有効な接続 |
|---|---|---|
| REVIEWING | 目的・Source・Target・権限を確認中 | 不足の解決、またはPlan提示 |
| READY | 今回の書込と必要な検証を行える | 最新基点を照合し保存 |
| OUTCOME_UNKNOWN | 応答欠落等で反映結果が不明 | Remoteの状態回復。再送は先にしない |
| PUBLISHED_UNVERIFIED | 保存応答または反映はあるが照合不足 | 実体を取得して確認 |
| VERIFIED | 意図した内容・必要条件と実体が一致 | 依頼の残点を確認し完了 |
| NO_CHANGE | Currentが目的を満たし変更不要 | 確認した根拠を返す |
| MANUAL_READY | 許可された手動用Packを用意した | 手動実施と保存確認はまだ別 |
| BLOCKED | 必須条件・権限・安全な回復が不足 | 影響範囲と回復条件を示す |
| STOPPED | Humanの停止・取消し等を受領 | 対象行為を停止。別Routeへ遷移しない |

状態名は理解と説明のための候補であり、Repositoryへ新しいStateファイルを作る指示ではない。中断後は、記憶した状態名より実体と最新Correctionを優先する。

## 5. 判断分岐の疑似コード

以下は主カードを読むためのモデルである。関数の実装・Tool呼出し・隠れた自動承認は存在しない。

```text
REVIEW(context, current_main_card):
    IF latest_instruction_stops_this_operation:
        RETURN STOPPED

    IF context.is_plan_only:
        RETURN plan_without_mutation

    IF mandatory_source_missing OR applicable_access_denied:
        RETURN BLOCKED(with_affected_scope_and_recovery)

    resolve_source_target_authority_and_dependencies()

    IF material_authority_gap:
        RETURN BLOCKED(with_specific_missing_decision)

    inspect_current_remote()

    IF earlier_operation_outcome_is_unknown:
        IF intended_result_is_present AND completion_conditions_match:
            RETURN NO_CHANGE(with_evidence)
        IF result_cannot_be_safely_determined:
            RETURN OUTCOME_UNKNOWN
        # 未反映を確認できた場合だけ、最新権限と基点で準備へ戻る

    IF current_remote_already_satisfies_request:
        RETURN NO_CHANGE(with_evidence)

    IF conflicting_changes_cannot_be_resolved_within_scope:
        RETURN BLOCKED(with_conflict_and_preserved_state)

    prepare_coherent_change_preserving_parallel_work()

    IF a_legal_direct_route_is_available:
        result = apply_authorized_change()
        IF result.is_unknown:
            RETURN OUTCOME_UNKNOWN -> inspect_remote_before_retry
        IF result.is_success_reported:
            RETURN PUBLISHED_UNVERIFIED -> verify_remote
        IF result.is_permission_denied:
            RETURN BLOCKED  # Manualへ迂回しない
        RETURN diagnose_confirmed_failure_using_main_card_section_6

    IF manual_route_is_authorized_and_not_a_bypass:
        RETURN MANUAL_READY(using_current_baseline)

    RETURN BLOCKED(with_available_recovery)
```

`verify_remote`は、Path／Ref／内容／必要なMetadata・Links・EOFを実際に照合して初めてVERIFIEDへ進むことを表す。照合できない、または不一致ならそのまま未完了を保持する。Tool failure後は毎回Manualへ進む、という省略をしない。

## 6. 机上で分岐を点検する例

下記は構成した説明例と期待判断であり、実行済みTest Suiteではない。現実の確認やGitHub書込を開始する命令でもない。

| 構成した状況 | 主カードに沿う判断 | 誤読すると起こること |
|---|---|---|
| Artifact完成、依頼は配置計画のみ | 変更せず配置案を返す | 完成物の存在を公開承認にする |
| 保存応答が消失、Remoteには目的の内容がある | 実体を照合し、同じWriteをしない | Timeoutを失敗として二重更新する |
| APIが承認・アクセス拒否を返す | 拒否対象を停止し、回復条件を示す | Manual Packで拒否を迂回する |
| 技術的な直接経路が使えず、手動保存は承認範囲内 | 最新基点を含むPackを準備できる | Pack準備を公開済みと報告する |
| Source準備後にHumanが同じ項目を訂正 | Currentへ統合し直す。未解決衝突は保留 | 古い全文で訂正を消す |
| 本文移動と入口修正が一体 | 整合した変更単位で確認・反映する | 1ファイル規則で壊れた中間状態を公開する |
| 保存後にHumanが内容を取消した | 取消しを保持し、古い成功目標を再適用しない | 回復として削除済み内容を復活させる |
| 保存成功応答はあるがRemote未取得 | PUBLISHED_UNVERIFIED | successを照合済みにする |

点検で矛盾を見つけたら、どの版・状態・条件で判断が分かれたかを示す。説明用ケースが通ったことを、全Tool・全AI・実生活での再現性へ一般化しない。

## 7. HumanのProgramming再学習にも使う

旧版のProgramming Re-learningという目的を保つ。

- **IF／THEN／ELSE**：何が変われば次の判断が変わるかを読む。
- **GUARD CLAUSE**：成立しない条件を先に見分け、その操作を止める。
- **INVARIANT**：どの経路でも失ってはいけない性質を読む。
- **STATE MACHINE**：現在状態と、根拠のある次の状態を区別する。
- **TEST CASE**：仮定と期待判断を具体化し、抜けを探す。

たとえば「失敗したら手動にする」を分解すると、結果不明、技術的失敗、権限拒否で遷移が異なることが分かる。この違いが、疑似コード化の利益である。書式を増やすだけで意味が明確になったとはしない。

## 8. Feedbackと由来

今回得た理解、発見した分岐の不足、確かめたい条件を必要な範囲で返す。実施した観測と期待判断を分け、主カード改善案はCandidateとして示す。改訂権限があれば担当原本へ反映し、なければ提案として止める。補助版だけで別の規則を発展させない。

[旧補助版](https://github.com/yusukefujiijp/ai-project/blob/0d21990a126948703eca517c65017f2038d4393c/ss_super-special/artifact-to-github_programming-like.md)はdraft_candidateのResearch Companionとして、主カード優先とHumanのProgramming再学習を明示していた。新版もこの二つの価値を保持する。旧§9と§17にあった非success時の書き分けは、単一のManual fallbackへ圧縮しない形に改めた。これは本文の整合修正であり、旧版が実行されて事故を起こしたという観測ではない。

旧本文に明示versionはなく、本v001は現代化した補助版系列の最初の明示版。旧版の掲載テストも本書の机上ケースも、実施記録とは区別する。今回の改訂・保存・確認範囲は[STR-014](../control-center/changes/STR-014-super-special-prompt-modernization.md)へ。

EOF::ARTIFACT_TO_GITHUB_PROGRAMMING_LIKE::v001-human-authorized
