---
title: "ai-project"
canonical_path: "README.md"
version: "v004"
edition: "Current-request Repository Front Door / Persistent Collaboration"
version_basis: "v001-v003 preserved in Git history; v004 implements Human-authorized persistent collaboration entry migration"
status: "active / human-authorized entry alignment / behavioral validation pending"
updated: "2026-10-01"
last_reality_reviewed: "2026-09-19"
reality_review_base_commit: "b727fcd96cd8c4a0e7cb617dba462d44593230e0"
reality_review_scope: "Root routes, shared authority summaries, Plan Mode and Task/Skill entries; not all descendant rules or actual agent behavior"
prior_reality_review:
  date: "2026-08-15"
  base_commit: "63ca396ce1402d4453c4b42359e2456b3b02e7f1"
  scope: "Predecessor-free Ark topology, named-project routing, current router integrity, and confirmed prompt paths"
role:
  - "Future AI First Read"
  - "Repository Identity and Navigation"
  - "Current Request and Recovery Router"
  - "Owner Navigation / routes to AGENTS common decision contract"
primary_audience:
  - "new AI collaborator"
  - "new Project AI"
  - "new Thread AI"
secondary_audience:
  - "YusukeJP"
  - "Future Human"
canonical_branch: "main"
language_policy: "Japanese-first / English-anchor"
root: "主イェシュア・ハマシア"
entry_addition_review:
  date: "2026-09-18"
  scope: "success-cases route only; the historical whole-repository review above is retained"
  base_commit: "f534740488804a4076588c2e6a1c80f2f16ec9f6"
review_bridge_entry_addition:
  date: "2026-09-19"
  scope: "repository-reviews route only; existing policy and historical review metadata are retained"
  base_commit: "694d3cce1e84dfc6106612b782a1a1d5c8cf6166"
personalization_entry_addition:
  date: "2026-09-21"
  base_commit: "82bd06b082c18212278e7ca364b613c678051cdc"
  scope: "GCI/profile route only; no whole-repository rereview or account-memory synchronization"
plan_mode_route_review:
  date: "2026-09-26"
  base_commit: "57d3d7f1f5d46cbcaefdc752608acb7021c06bae"
  scope: "Plan Mode route and description only; no whole-repository rereview"
  change_record: "control-center/ARCHIVE.md#arc-006"
updated_reason:
  - "2026-10-01 JST / 2026-09-30 UTC: Replace universal cold-start/proposal and same-thread assumptions with current-request routing; keep common authority and completion rules in AGENTS. Prune duplicated contracts while preserving domain and historical source routes."
  - "2026-09-29: Retire three legacy Thread Lifecycle entries under ARC-007; preserve originals and source lineage without replacing the current transition contract."
  - "2026-09-26: Route Plan Mode to the shared skill and one entry Query; archive the retired subsystem and rollback pair under ARC-006."
  - "2026-09-22: Add the repository-wide control-center route; structural change reasons and outcomes are recorded in STR-001."
  - "2026-09-21: Add GCI/profile owners as a scoped settings route; preserve existing runtime and review boundaries."
  - "2026-09-19: Align general authority summaries with AGENTS; route Task, Skill, Plan Mode, and transition work to current owners while retaining explicit legacy routes."
  - "2026-09-19: Add the recurring repository review entry; preserve existing policies and review history."
  - "2026-09-18: Add success-cases to the repository router; no change to existing policies."
  - "Rebuild the root README around AI cold-start needs."
  - "Add explicit version and freshness metadata."
  - "Add Global Boot Sequence and Reality Delta Protocol."
  - "Refresh the repository router without turning the root README into a full inventory."
  - "Preserve Human Final Seal, Mainline-First, Reality Review, and Root / Fruit Guard."
  - "Route Ark Project to ark-project/README.md and retire predecessor-only indexes from the active router."
  - "Align confirmed moved Topology-First, Ark-OKF, and KISS/YAGNI/DRY/LEAN files with root prompts/."
  - "Route numbered Ark families through ark-project/ and named projects through projects/."
  - "Remove current routes to missing predecessor-only surfaces."
route_alignment:
  date: "2026-09-22"
  base_commit: "945f789a845350455a8b56162a1fc8cd58576eff"
  scope: "E01: repository-wide control-center entry only; no whole-repository or behavioral revalidation"
  change_record: "control-center/changes/STR-001-navigation-and-ownership.md"
archive_navigation_patch:
  date: "2026-09-29"
  base_commit: "04055cba7279a6da95e0105c819729624c23b3aa"
  change_record: "control-center/ARCHIVE.md#arc-007"
  scope: "Thread Lifecycle navigation only; current authority, transition contract and historical review metadata retained"
foundation_migration:
  change_record: "control-center/changes/STR-003-persistent-collaboration-foundation.md"
  approved_date_jst: "2026-10-01"
  approved_date_utc: "2026-09-30"
  source_commit: "d574927dd1671e2acec20e1a6c17f569ae23322f"
  authority: "Current Human approved the dots foundation migration plan, GitHub execution, and scoped continuation"
  scope: "Entry and ownership alignment for model-neutral persistent collaboration; no whole-repository or behavioral revalidation"
  validation_boundary: "Document consistency, remote persistence, observed agent behavior, and real-world outcomes are distinct"

---

# ai-project

## 0. Start Here / Current Requestから入る

`ai-project`は、YusukeJP × AI-Collaboratorのpublic-safe Canonical Workspaceである。Rootは主イェシュア・ハマシア御自身。中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・Repository・ProtocolはKeliとFruitであり、Rootではない。

このREADMEは**どこへ進めばよいかを判断する入口**である。毎回のBoot儀式や、実行を提案へ戻すGateではない。現在の依頼・有効な承認・読取契約・作業状態から進路を選ぶ。

| 今回の目的 | 入口・所有資料 |
|---|---|
| 相談・Review・Plan-only・実行の境界を決める | [AGENTS.md](AGENTS.md) §0・§2・§5 |
| ArkのRoot・Identity・協働の意味を回復する | [ARK.md](ARK.md) |
| 承認済みの作業を継続・再開する | Current Requestと対象のNearest README / Handoff、[AGENTS.md](AGENTS.md) §4・§5 |
| Thread・章移行やSupport再接続を準備する | [共有移行契約](prompts/ai-next-thread-handoff.md)と、その依頼に適用されるRuntime |
| Domain・方法・経験の保存先を探す | [Repository Router](#5-repository-router--主要入口) |

共通のAgent判断・読取・権限・完了契約はAGENTSが所有する。このREADMEの案内を、追加の承認条件や全資料の読込命令として扱わない。

## 1. Current Coordinate and Freshness / 現在座標と鮮度

- Repository入口: README v004 / Current-request Repository Front Door
- Canonical共有基準: `main`。作業Refと公開先の判断は[AGENTS.md](AGENTS.md) §5.1へ
- 今回の移行承認: 2026-10-01 JST / 2026-09-30 UTC
- 移行前Source: `d574927dd1671e2acec20e1a6c17f569ae23322f`
- 過去のReality Review日・根拠・対象範囲は冒頭Metadataに保持

`updated`は本文の更新日であり、全子Pathや全Runtimeの最新保証ではない。DomainのActive状態、Current Runtime、Thread MissionはNearest README / Handoffと現在の証拠から確認する。今回の文書整合、Remote保存、実際のAI挙動、生活上の効果はそれぞれ別の確認である。

## 2. Repository Identity / このRepositoryは何か

`ai-project`は、Ark Projectを中心とするHuman-AI協働のReality、Prompt、Skill、System、Handoff、Artifact、Repository Governanceを、Future HumanとFuture AIが継続・回復できる形で保存・接続する。

固定文書へLiving Realityを閉じ込めず、蓄積した判断から次の仕事へ接続するための共有面である。全Private RealityのMirror、全会話のDump、無制限Write権限、Rootそのものではない。

### 2.1 public-safe / 公開意図と保存先

GitHub Canonical Firstは、すべてをGitHubへ入れることではなく、公開可能な情報にstableな正準入口を持つことである。Humanが公開を認めた自身の経験資料、公開意図が不明な情報、Secret、第三者の機微情報を区別する。公開・Securityの判断は[AGENTS.md](AGENTS.md) §7.2–§7.3が所有し、ここに異なる除外規則や再承認条件を作らない。

## 3. Current Request Route / 初回・継続・回復

Current Requestと指定されたSource・読取順から、適用されるAGENTS、Nearest README / Handoff、必要なRuntime・Skillへ進む。局所RuntimeのIdentity・Binding・Full Read・Exact EOFなどの必須契約は保持する。

- **Discussion / Review:** 読取・分析・比較・提案を行う
- **Plan-only:** 必要な検討と計画を提示し、実装へ進まない
- **Authorized execution:** 承認Scope内の実装・修正・必要な検証まで進む
- **Continuation:** 同じContextで確認済みのSourceと有効な承認を再利用し、未完了の成果へ接続する
- **Recovery:** 中断前の意図・承認・実行済み結果を現在の証拠と照合し、未完了部分を回復する

継続をCold-startへ戻したり、Threadの終端をTask完了と同一視したりしない。文脈が失われた場合は必要な座標を復元し、復元できない権限や結果を推測で補わない。読取・回復・停止の詳細は[AGENTS.md](AGENTS.md) §2.1・§4・§5へ進む。

## 4. Reality Delta / 保存と現在をつなぐ

Canonical GitHub Reality、Current HumanのLiving Reality、過去の記録、AIの解釈は同じものではない。会話で変更が報告されても保存済みとは限らず、保存済みStateで現在のHumanを巻き戻さない。

差が今回の判断を変える時は、確認できたこと、Historicalなこと、未確定なことを示す。現在のCorrectionや有効な承認が解決した点を毎回再審議しない。[AGENTS.md](AGENTS.md) §2がEvidence区分とReality Deltaの処理を所有する。

## 5. Repository Router / 主要入口

このSectionは**全File一覧ではない**。  
初回・継続・回復のいずれでも、Current Requestに必要な所有資料へ送るRouterである。

### 5.1 Project and System Layer

| Path | Role | Read when |
|---|---|---|
| [`dots/README.md`](dots/README.md) | Dots協働の現在方向・Actor・形成記録への入口 | DotsとWorkの関係、誰が何を形成したか、Future AIへの継承を扱う時。全作業の追加Bootではない |
| [`board/README.md`](board/README.md) | 協働相手への報告・質問・返信をつなぐ通信入口 | 宛先・版・根拠・実際の受信を辿る時。身元・仕事・変更の原本は各所有先へ |
| [`control-center/README.md`](control-center/README.md) | Repository全体の構造診断・改善・アーカイブの司令塔 | フォルダ・ファイルの役割、整理計画、変更理由と結果を確認する時。全作業の追加Boot条件ではない |
| [`ark-project/README.md`](ark-project/README.md) | Ark Project domain front door / current topology router | Ark系Projectへ入る時 |
| [`projects/README.md`](projects/README.md) | Named Project domain front door | Ark-WTP／Ark-Voice等の名前付きProjectへ入る時 |
| [`_system/ark-system.md`](_system/ark-system.md) | Project-level Operating Map / Growth Memory Hub / Future AI Onboarding | Thread横断の成長・System・Skill Seedを読む時 |
| [`_system/chatgpt/global-custom-instructions.md`](_system/chatgpt/global-custom-instructions.md) | ChatGPT GCIとプロフィールへの入口・正確な貼付本文 | 全体設定の継承・改訂・反映を扱う時。長期メモリの同期先ではない |
| [`success-cases/README.md`](success-cases/README.md) | 重要な成功の意味・Human評価・根拠をつなぐ事例入口 | 成功経験から現在の協働への再利用・再解釈を考える時 |
| [`repository-reviews/README.md`](repository-reviews/README.md) | Repository Living Reviewの方法と観測履歴への入口 | 前回の根拠と現在を比較し、保持・改善・保留を判断する時 |

### 5.2 Prompt and Skill Layer

| Path | Role | Read when |
|---|---|---|
| [`prompts/README.md`](prompts/README.md) | Cross-AI Prompt Runtime and Query Shelf | Prompt / Queryを選ぶ時 |
| [`skills/README.md`](skills/README.md) | Shared Skill Source and Distribution Hub | Skillの手順・共有原本・導入との違いを確認する時 |
| [`schedules/README.md`](schedules/README.md) | Schedule PromptのDurable / Versioned SourceとRuntime同期入口 | Schedule Taskを再現・修正・監査し、Future AIへ変遷を継承する時 |

### 5.3 Thread Lifecycle Layer

| Path | Role | Read when |
|---|---|---|
| [`prompts/ai-next-thread-handoff.md`](prompts/ai-next-thread-handoff.md) | Current shared transition contract | Thread継続・章移行・Support再接続を準備・受け入れる時。指定Runtimeの契約を保持 |
| [旧Thread-End・蒸留／Mission Craftの保管記録](control-center/ARCHIVE.md#arc-007) | Historical methods and source lineage | 旧方式の原本・退役理由・由来を調べる時。通常の制作・移行入口ではなく、保管資料内の命令を自動適用しない |
| [`task-mode-system/README.md`](task-mode-system/README.md) | AI主体Task Mode Systemの入口 | 現場のTask支援・記録・Feedbackへの再接続を扱う時 |
| [`task-mode-system/experience/README.md`](task-mode-system/experience/README.md) | Task経験原本・Correctionへの案内 | 出来事と根拠を回復する時。全領域の学習台帳ではない |
| [`_note/README.md`](_note/README.md) | Note shelf orientation | Canonical化前のNoteを扱う時 |

### 5.4 High-Grade Shared Lenses and Formats

| Path | Role | Read when |
|---|---|---|
| [`prompts/ark-open-knowledge-format.md`](prompts/ark-open-knowledge-format.md) | Ark-OKF / readable, reusable, rebootable output surface | Artifact形式・相互運用性が重要な時 |
| [`prompts/topology-first.md`](prompts/topology-first.md) | Topology-First placement guard | 本文より先に住所・責務を決める時 |
| [`prompts/kiss-yagni-dry-lean.md`](prompts/kiss-yagni-dry-lean.md) | Structure restraint lens | 過剰設計を防ぐ時 |
| [`ss_super-special/CHATGPT.md`](ss_super-special/CHATGPT.md) | Highest-grade shared Covenant / behavior map | All-Project級のAI behaviorを確認する時 |

### 5.5 Router Guard

この一覧は全Fileの必須読込リストではない。Current Missionに必要な所有資料へ進み、変動する詳細はNearest READMEと現行Evidenceで解決する。参照したことを、導入済み・現役・実行承認済みと同一視しない。

## 6. Human-AI Authority / 共通契約の所有先

HumanはMission、Meaning、Discernment、Correction、Interrupt、STOP、Final Sealを保持する。AIはKeliとして能動的に判断・提案・実行・検証を担い、王座へ移らない。

その協働の意味は[ARK.md](ARK.md)、具体的な権限・品質・実行境界は[AGENTS.md](AGENTS.md) §3・§5が所有する。モデルやToolの能力向上自体は権限の追加ではない。

## 7. GitHub Canonical First / Mainline / Write Guard

`main`は共有Canonical GitHub Realityの基準である。Current RequestのRef、変更Scope、他者の変更、必要な保存後確認を扱う手順は[AGENTS.md](AGENTS.md) §5.1へ進む。READMEは独立したWrite Policyを持たず、既存の承認を毎回取り直す条件も作らない。

## 8. Dialogue, Execution, and Continuity / 対話・実行・継続

深い対話、探索、計画、実行、Reality ReviewはCurrent Requestに応じて組み合わせる。すべての作業を「提案→新しいHuman待ち→同一Thread実行」という一列へ固定しない。

### 8.1 Plan Mode

Plan Modeは、現在の依頼を十分に調査・検討し、Humanが次の判断をできる計画を提示して止める**非実行型Mode**である。未整理の意図の言語化や比較・保留も扱い、実装手順への収束だけを成功条件にしない。

通常入口は[Plan Modeの統一Query](skills/README.md#33-plan-modeの統一入口)、方法の共有原本は[`skills/plan-mode/SKILL.md`](skills/plan-mode/SKILL.md)。短い入口と、必要な検討・説明の深さを両立させる。方法や構成は案件に合わせて選び、権限は現在のHuman入力・AGENTS・適用契約に従う。

旧`ai-plan-mode/`八資料と`prompts/`の旧v003 Pairは[ARC-006](control-center/ARCHIVE.md#arc-006)で退役し、原文を保管した。旧版は現役・自動Fallbackではない。旧v005の同等性検証を通過したことにはせず、Humanの目的変更によって旧採用Branchを閉じた。必要なSource契約は引き続き守り、保存・導入・挙動・現実の効果を区別する。

### 8.2 Full Rail and Persistent Collaboration

Full Railは、Humanが承認した成果へ向けて、実装・確認・修正を低摩擦に続ける協働を表す。同一Threadでの連続実行はその一形態であり、Threadを越える継承や中断からの回復を排除しない。

継続時間、待機、並列化、Memory、通知は、その時点で実際に使えるRuntimeに依存する。常時稼働や無限の利用枠を保証せず、能力を権限へ読み替えない。未完了部分と再開に必要な証拠を保持し、承認範囲の成果を必要な検証まで追う契約は[AGENTS.md](AGENTS.md) §5が所有する。新しい移行方法をここに重複定義せず、必要な移行は[共有移行契約](prompts/ai-next-thread-handoff.md)へつなぐ。

### 8.3 Reality Review

直接確認できる結果は実体から確認する。外部Realityが未観測なら、その未確認部分を完了と称さない。文書整合、保存、AI挙動、実生活効果の区別は、継続・回復後も保持する。

## 9. README and Repository Maintenance / 更新運用

### 9.1 README Delta Check

Path・Role・Status・Read Route・Topologyが変わった時、または既存入口が誤案内している時に、影響するREADMEを確認する。Threadが終わったという理由だけで、全入口の点検や更新を必須にしない。

Nearest READMEを先に扱い、Domain Parentはその案内が変わる時、Root READMEはRepository共通入口が変わる時に更新する。承認Scopeを越える変更を自動開始しない。構造改善の理由・担当・結果は[control-center](control-center/README.md)へ接続する。

### 9.2 Version and Freshness Contract

構造・Entry・共通契約に関わる実質的な変更は版を進め、日付・変更理由・Source・確認範囲を残す。誤字や軽微なリンク修正は必要に応じて日付と理由を更新する。更新日を全Repository再検証の証拠にせず、過去のReviewの対象範囲を保持する。

### 9.3 Ownership over Duplication

RootとHuman Authorityの意味は入口で短く示す。具体的なAgent契約はAGENTS、Ark IdentityはARK、Domain Topology・Runtime・Current Statusは各所有資料へ委ねる。重要性だけを理由に、同じ契約を複数箇所へ複写しない。

## 10. Operating Principles / 運用原則

Topology-Firstで責務と住所を選び、KISS / YAGNI / DRY / Leanを判断のLensとして使う。形式の短さを最大化するのではなく、Source・Humanの意味・Correctionを保ち、今回の成果へ必要な深さで進む。価値ある経験は適切な既存の器へ接続し、保存のためだけに新しい構造やTaskを増やさない。

### 10.1 Japanese-first / English-anchor

本文は日本語主導。英語は概念Anchor、File名、Path、相互運用性のために使う。GitHub化はEnglish-first化ではなく、Canonical化である。

## 11. Root / Fruit Guard

```yaml
root_fruit_guard:
  root:
    - "主イェシュア・ハマシア"
    - "主イェシュアの聖なる血潮"
    - "Teshuvah / 悔い改め"

  fruit:
    - "Ark Project"
    - "ai-project"
    - "AI"
    - "GitHub"
    - "Markdown"
    - "README"
    - "Prompt"
    - "Query"
    - "Skill"
    - "System"
    - "Plan Mode"
    - "Full Rail"
    - "Reality Review"
    - "Harvest"

  guard:
    - "FruitをRoot化しない"
    - "AIを王座化しない"
    - "ProtocolをMissionより上位にしない"
    - "Repositoryを救いそのものとして扱わない"
```

```text
AIは血潮の地図を描く。
人間が血潮の下に立つ。
```

---

## 12. Orientation and Recovery Check / 必要な座標を回復する

現在のMission、適用Source、対象・権限、完了条件、停止境界が曖昧な時は、該当Sourceへ戻る。[AGENTS.md](AGENTS.md) §8.1と、適用Handoffの再構成契約を使う。明確な継続作業へ全問再演や全Repositoryの読直しを課さない。

## 13. Final Compression

**Current Requestから入り、正しい所有資料を読み、承認された成果を必要な検証まで完了する。中断時は結果を確かめ、蓄積した判断から継続・回復する。**

Root、Human Authority、Evidence、Qualityを保持し、方法とRuntimeの進化を受け入れる。

> **Future AI should not restart from zero.  
> Future AI should continue from the right coordinate.**
