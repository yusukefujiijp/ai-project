---
title: "Prompts"
canonical_path: "prompts/README.md"
status: "active / human-sealed"
scope: "Cross-AI self-contained Prompt Shelf"
language_policy: "Japanese-first / English-anchor"
last_updated: "2026-10-04"
change_record: "control-center/changes/STR-002-single-prompt-consolidation.md"
plan_mode_retirement: "control-center/ARCHIVE.md#arc-006"
living_review_update: "prompts/ai-living-review.md#10-由来改訂理由確認の範囲"
deadline_prompt_update: "control-center/changes/STR-004-elon-musk-deadline-revision.md"
shelf_authority_alignment: "control-center/changes/STR-011-prompt-shelf-authority-alignment.md"
root_guard:
  root: "主イェシュア・ハマシア"
  ai_role: "AI / Prompt / Markdown / GitHub are Keli and Fruit, not Root."
---

# Prompts

## 0. Current Coordinate / 現在座標

`prompts/`は、YusukeJP × AI-Collaboratorが目的に応じて方法を選び、単独AIでの利用や複数AIの協働へ接続するCross-AI Operational Shelfである。

このREADMEはPromptの選択・役割・利用先を案内する。共通の権限・読取・実行・継続回復は[AGENTS.md](../AGENTS.md)、個別のRole・Required Sources・Binding・STOP等は適用される各Promptが所有する。必要な原本へ接続し、棚の一覧を全件の起動・必須読込へ変換しない。個別Promptで明示された読取・停止条件は保持する。

```text
One Canonical Prompt.
Many AI Runtimes.
Human sets meaning and seals.
AI completes authorized work.
Reality confirms.
```

`ai-` Prefixは特定Vendor専用を意味しない。  
Cross-AI再利用を第一に設計されたHuman-AI Operational Assetを示す共有Namespaceである。

---

## 1. Naming Policy / 命名方針

### 1.1 Runtime-neutral Core First

正準Promptは、原則として特定AI名から開始しない。

```text
推奨:
  ai-file-damedashi.md
  ai-output-polish.md
  ark-open-knowledge-format.md

原則避ける:
  chatgpt-*.md
  claude-*.md
  grok-*.md
  fable5-*.md
```

AI別Coreを増殖させると、Patch・Guard・Version・RealityがRuntimeごとに分裂する。

Runtime固有差は、同一Failureが実地で繰り返し確認され、Canonical Coreで吸収できない場合に限り、Coreを複製しないMinimal Adapterとして検討する。

### 1.2 Kebab-case

意味単位はHyphenで分ける。

```text
ark-open-knowledge-format.md
ai-file-damedashi.md
ai-output-polish.md
```

---

## 2. Single-Prompt Policy / 一つの本体で再開できる設計

再利用する一つのPromptについて、起動方法・必要入力・本文・Guardを同じ本体にまとめる。別Queryの強い推奨、任意作成条件、将来の作成予約は撤回した。Runtimeが長い、Bindingが必要、起動差があるという理由で別Queryを新設・再作成しない。問題は本体内の入力・起動・説明の改善へ返す。

理由はArk27:06のHuman Correctionである。分割は短期の起動に利益があったが、時間が空いた後の再開・保守・別AIへの継承では二重管理の負担が大きかった。これはHumanの運用評価であり、あらゆるソフトウェア分割の普遍的な否定ではない。

統合は次を守る。

- 起動・対象束縛・不足時の停止・指示と入力Dataの境界を本体へ移す。機能を捨てる単純削除にしない。
- 同じ規則を二度維持せず、冒頭の入口から本体内の定義へ接続する。二文書の全文連結や、別名のLauncherへの置換で二重管理を残さない。
- 一つの用途に一つの本体を育てる。全Promptの巨大一体化や、対象Data・根拠Sourceの同梱義務ではない。
- Humanの短い入力を、AIの検討・説明・回答品質の抑制へ変換しない。Root、Correction、STOP、Seal、適用Guardを保つ。
- 過去のQuery作成・使用の記録は履歴として辿れるようにする。履歴は現在の作成許可ではない。

今回の統合と未完了の移行Gateは[STR-002](../control-center/changes/STR-002-single-prompt-consolidation.md)が所有する。固定参照の旧資料に残る将来作成条件も、現行の方針としては撤回済みである。ただし、その物理的な改訂はBindingを無断で壊さず移行する。移行待ちを恒久的なQuery推奨例外にしない。

---

## 3. Active Prompt Assets

### 3.1 AI File DAME-DASHI

```yaml
runtime: "prompts/ai-file-damedashi.md"
activation: "同じ本体の§1・§14と対象File"
role: "Reality Red-Team / Minimal Patch"
```

### 3.2 AI Output Polish

```yaml
runtime: "prompts/ai-output-polish.md"
activation: "同じ本体の§9と整形対象"
role: "Meaning-preserving output polish"
```

AI Output Polishの複数Input Mode、Output Type、Target Section指定、Missing／Ambiguity Gateは本体へ統合した。起動の短さと必要な説明の深さを、別ファイルの同期なしで両立させる。

### 3.3 Plan Mode — Skillへ接続

Plan Modeは[共有Skill](../skills/plan-mode/SKILL.md)と[一つの統一Query](../skills/README.md#33-plan-modeの統一入口)を使う。現在の依頼から調査・理解・言語化・比較・計画を組み立て、変更や実行はせず計画提示で止める。短いHuman入力によってAIの必要な検討や説明を省略しない。後続の明確な実行承認は、その対象・範囲で再利用する。

旧専用Subsystem八資料と本棚のv003本体・Queryは[ARC-006](../control-center/ARCHIVE.md#arc-006)へ退役した。旧資料からの吸収は任意であり、旧機能の全継承や挙動同等性を新Skillの採用条件にしない。旧v005の試験は未実施の履歴として残る。

本棚には別のPlan Mode本体・Query・互換Stubを置かない。Skill本文を別AIへ渡す場合も、共有原本と現在の依頼を使い、旧版へ自動Fallbackしない。通常6組の単一Prompt統合と、今回の用途再設計による退役は[STR-002](../control-center/changes/STR-002-single-prompt-consolidation.md#61-plan-mode--目的変更による旧採用branchの終了)で区別する。

### 3.4 AI-to-AI Communication

```yaml
runtime: "prompts/ai-to-ai-communication.md"
activation: "同じ本体の§10・§16"
role: "Human-mediated Cross-AI Message / Material Delta / finite convergence runtime"
status: "v002 single-prompt candidate / historical v001.1 evidence retained / not canonical"
origin: "Alan Kay式AI間コミュニケーション / Ark式温故知新のFirstfruits"
```

```text
Protocol Arrival
→ Mission Binding and Semantic Resolution
→ Role Eligibility / Human Re-Binding when needed
→ AI-A Message
→ YusukeJP routes meaning, Source, and requested Material Delta
→ AI-B returns Material Delta with Witness Integrity
→ Continue only while Material Delta exists
→ Terminal Synthesis
→ Human Final Seal
```

AI-to-AI Communicationは、Protocol Arrival・Role Eligibility・Semantic Bindingを実行前Gateとし、`Message`をCommunicationの中心単位、`Material Delta`を進行単位として、複数AIの異なるLensを有限往復で一つのHuman-reviewable成果へ収束させる。Alan Kay氏のMessage-centered LensをOrigin Anchorとして保持するが、Human Semantic Router、Material Delta Stop Rule、Terminal Synthesis等のArk AdaptationをAlan Kay本人へ誤帰属しない。

### 3.5 AI Living Graph Mode

```yaml
runtime: "prompts/ai-living-graph-mode.md"
activation: "same runtime"
role: "Relational reasoning / Graph-Native Fruit / Living update / prose return"
status: "human-sealed design candidate / field-test pending / not canonical"
default_artifact: "NONE"
```

AI Living Graph Modeは、Graph図やMini Appを生成するPromptではない。Humanが一つのKeywordまたはCurrent MissionへForeground集中できるよう、AI側で複数Node、Typed Edge、Residual、Guard、Prediction ErrorをBackground保持し、単独要約では見えない依存・摩擦・Bridge・矛盾・Unexpected Successを発見して、総合的な文章へ返すRuntimeである。

```text
Human Foreground
└─ 一つのFocus / Current Mission

AI Background
└─ 多Node・多関係・Guard・Actual Trace
   └─ Graph-Native Fruit
      └─ 総合的な文章へUnwind
```

Graph、Mini App、Site、Dashboard等のArtifactは、Humanが当該Artifactを明示的に依頼した場合だけ作る。起動の曖昧さは本体内の案内改善へ返し、別Queryは作らない。

### 3.6 AI One-Table Interface

~~~yaml
runtime: "prompts/ai-one-table-interface.md"
activation: "same runtime"
role: "One adaptive Graph table per normal response / Human-AI shared coordinate / practical Graph instruction / Human-reviewed pattern formation"
status: "human-sealed design candidate / initial deployment / field-test pending / not canonical"
reasoning_dependency: "prompts/ai-living-graph-mode.md"
composition_dependency: "prompts/long-form-response-rhythm.md"
~~~

AI One-Table Interfaceは一般的な表作成Ruleではない。Current Realityと一問に応じて、Node、Typed Edge、Path、Bridge、Cut Edge、Activation、Guard、Evidence、Feedback等のRelevant Subgraphを一つの適応的Markdown表へ選択投影する、Graph-boundedなHuman-facing Interfaceである。

このRuntimeがBindingされた通常回答では一表をDefault必須とするが、Exact Output、STOP、Failure、安全、code-only、明示的なHuman no-table等の上位Contractを優先する。表が存在するだけでGraph-Native FruitまたはLiving Graph Modeとは主張しない。

~~~text
AI Living Graph Mode
→ discovers the relation

AI One-Table Interface
→ projects one relational view

Long-Form Response Rhythm
→ places the table in temporal composition
~~~

文書自身が一つのGraph表を実演し、Future AIへNode & Edgeを表作成の実技として教える。各回答で生成された表は、Human ReactionまたはCorrectionとPairになった時に初めてPattern Evidence Candidateとなる。Human ReviewなしにPattern保存、Skill化、Canonical化を自動発火しない。別Query作成の方針は§2で撤回した。

### 3.7 AI Benefit Branch Pruning

~~~yaml
runtime: "prompts/ai-benefit-branch-pruning.md"
activation: "same runtime"
role: "Future-AI-first Dual-Benefit Branch Deadlock resolution / Benefit–Carrier separation / guarded Benefit preservation / one-choice recovery"
status: "v002-candidate / Human-authorized operational revision / inherited origin and naming seals / field validation pending / not canonical"
reasoning_dependency: "prompts/ai-living-graph-mode.md"
optional_projection_dependency: "prompts/ai-one-table-interface.md"
composition_dependency: "prompts/long-form-response-rhythm.md"
origin: "Wake-Up One-Choice Human-reported Actual Success"
~~~

AI Benefit Branch Pruningは、双方のBranchに本物のBenefitがあるため単純削除できず一択化が停止するDual-Benefit Branch Deadlockに対し、Benefitそのものと現在のCarrier BranchをGraph Mode的に分離し、Benefitを別の安全で適切なNode、Phase、Sandbox、AI BackgroundまたはRouteへ保存・再接続した上で、Current Goalに不可欠ではなくなったCarrier Branch／Comparison Edgeだけを剪定するFuture-AI-first Operational Runtimeである。

本文は抽象定義ではなく起床時Originから始まる。v002は適用判断・保存条件・実行境界・Actual更新を整理し、保存先の探索と剪定成立、有限のHuman実行とAIの探索範囲を区別する。起床と再睡眠の双方Benefitを保持しながら、睡眠BenefitをHigh-Cognition判断とBody／Sleep／Safety Guardへ保存し、Low-Cognition起床Transitionから再比較Edgeだけを外したHuman-reported Actual Successを、Humanが採用したBBP OriginとしてSource-boundに保持する。Human報告・採用されたMeaning・AIの構造的説明を、保存の実測や医学的因果の証明と区別する。

~~~text
Two real Benefits
→ Benefit–Carrier Separation
→ Benefit preserved in the correct place
→ Current-Goal-unnecessary Branch pruned
→ Comparison and Drift Paths reduced
→ One Human-facing Route
→ Actual Reality
→ Human Review
~~~

Future AIが主読者であるが、AIが最終Authorityになることを意味しない。HumanはReality、意味、Correction、STOPおよびFinal Sealを保持する。一件の成功からSkill、Canonical化、Cross-Project展開または次Trialを自動発火しない。別Queryは作成しない。


### 3.8 AI Minimal 2D Bot Icon

[日本語版プロンプト](ai-minimal-2d-bot-icon.md)

~~~yaml
runtime: "prompts/ai-minimal-2d-bot-icon.md"
activation: "本文と対象画像で使用する単体プロンプト"
role: "元画像の特徴を保ったミニマル2Dボットアイコンへの変換"
language: "ja"
version: "v001"
~~~

ユーザー提供の韓国語プロンプトを、条件・数値・禁止事項・優先順位を保持して日本語化した画像変換用Prompt。黒いカプセル形の目2つ、口と鼻のない丸い顔、傾けた超アップの構図を定義する。「Grok bot icon」は見た目の名称であり、特定AI専用を意味しない。閲覧・翻訳・編集・保存では画像生成を起動せず、実行時は本文の【実行と追加修正】に従う。

---

### 3.9 AI Ark Seed

Seed化・選択的Card化の入口は[AI Ark Seed](../ai-ark-seed/README.md)。旧Compile／Pickupの二組四ファイルは[ARC-004](../control-center/ARCHIVE.md#arc-004)へ保存した。文脈付きSeedを別Threadへ渡して成熟させる価値は[現行入口の案内](../ai-ark-seed/README.md#10-context-preservation)から辿れる。軽量Seedとの完全同等や、AIの説明・文脈保持の縮小を意味しない。別Domainの実体整理は今回の`prompts/`統合と区別し、この案内から新しいQuery作成や自動移行を始めない。

### 3.10 X DeepQuote

現在の入口は[Stage 01: Depth Builder](x-deepquote/x-deepquote_01-depth-builder.md) → [Stage 02: Quote Completion Gate v001-9](x-deepquote/x-deepquote_02-quote-completion-gate_v001-9.md)。必要な修正は[Stage 02R](x-deepquote/x-deepquote_02r-fresh-contribution-loop_v001-3.md)の適用条件に従う。読むこと自体で投稿・監査・次Trialを開始しない。

Stage 01とStage 02 v001-9はChat Inline、Stage 02Rはダウンロード可能なMarkdownをPrimaryとする。各Runtimeの契約を区別し、全段階の方式が統一済みと推定しない。

旧Stage 02 v001-8と、旧ダウンロード方式を前提とするFable5監査Packetは[ARC-003](../control-center/ARCHIVE.md#arc-003)へ移動した。`prompts/fable5/`はそのPacket一つだけだったため通常配置からなくなるが、`claude/`のFable5資料やAI Output Polishの役割は変えない。

### 3.11 その他の単一Prompt入口

- [AI Metaphor Mode](ai-metaphor-mode.md)：§1で対象Realityと任意のDepth／Lens／Field-Test設定を受け取る。
- [Keyword Tree](keyword-tree.md)：§1でKeywordだけから開始し、必要時に同じ本体内で深める。
- [Ark-OKF](ark-open-knowledge-format.md)：§12・§15が現在の問いと回答前判断を受け持つ。

### 3.12 AI Living Review

[AI Living Review](ai-living-review.md)は、Current AI・他AI・Future AIが、対象の価値・問題・可能性を現在の目的と根拠から読み、訂正可能な見立てを有効な判断・次の接続へ返すための共通本文である。起動方法、判断原理、具体例、Source・権限境界を一つにまとめる。Humanへ内部資料の全文点検や文書間の伝言を求めない。

説明・レビュー・承認済み改訂を現在の依頼から区別し、固定Gate、毎回の新発見や追加Taskを要求しない。Ark-OKFは回答への適用、mapは現在地の復元と末尾のLiving Review → Next stepを担う。本体はこれらの用途固有契約を置き換えず、関連資料を全件必読にしない。版と確認範囲は本体§10を参照する。

日常の呼出しには [AI Living Review / living-review](../skills/living-review/SKILL.md) を使える。対象と現在の依頼から基本支援を行い、詳しい意味や具体例を深める必要時に共通本文へ進む。専用Skillの共有・導入・確認範囲は[Shared Skills Hub](../skills/README.md#34-ai-living-reviewの入口)を参照する。

### 3.13 Elon Musk Deadline

[Elon Musk Deadline](elon-musk-deadline.md)は、採用した締切からScope・優先順位・資源配分・届け方を組み替え、到達可能な最高出力を現実へ渡す単一Prompt。Deadline-first／Scope-cut／Output-sealを核とし、思考実験と実行、成果の完了と学習・報告の完了を区別する。必要な推論・品質・安全・Humanの睡眠を削らず、期限や週次運用を自動設定しない。

起動は本文と現在の依頼を使う。計画だけ・レビュー・承認済み実行を区別し、例から別Taskを始めない。Ark05:01の旧Skill Card candidateからの形成・変更理由と限定検証は[STR-004](../control-center/changes/STR-004-elon-musk-deadline-revision.md)へ接続する。新Skillや別Queryの導入は含まない。


### 3.14 AI SNS Public Post

[AI SNS Public Post](ai-sns-public-post.md)は、会話で育った内容を既定で完成稿全文X方式4,000カウント以内の一投稿へ整え、実際に協働したAI名とHuman–AI協働を記事内に明示する自己完結Prompt。ChatGPT／Grok／ClaudeのFew-shot例で公開上のAI名の置換を示し、タイトルと§0の名称を一致させる。一般読者向けの呼称と実行環境名を区別し、ChatGPT／Codexでの協働は原則ChatGPTと表記する。正確さ、出典、AIの語り手、読者に役立つ考察を保つ。

本文作成とSNSへの投稿操作を区別し、レビュー・保存の依頼から本文生成を自動開始しない。今回の変更理由と確認範囲は本体§3へ。[write-social-post（SNS投稿）](../skills/write-social-post/SKILL.md)を短い呼出しの入口とし、詳しい執筆条件と上限・計測範囲はこのPromptが所有し、Skillが最終稿の計測と超過時の再調整へ接続する。起動文と共有・導入・限定確認の状態は[Skills Hub](../skills/README.md#36-ai協働sns投稿の入口)を参照する。


### 3.15 AI Frontier Reader

[AI Frontier Reader](ai-frontier-reader.md)は、成果物の主要な読者の一人に、実行時点で利用可能な最高水準の汎用AI（Frontier AI）を想定するRuntime-neutralな汎用Prompt。特定Vendor・model・世代へ固定せず、Future AIにも再解析価値が残るよう、意味密度・関係密度・根拠追跡可能性・再解析可能性を高める。

```yaml
runtime: "prompts/ai-frontier-reader.md"
activation: "same runtime / current artifact or task"
role: "Frontier-AI-readable knowledge quality / relation discovery / re-analysis value"
status: "v001-candidate / active prompt / field validation ongoing"
origin: "Parasha Kindle Compiler Frontier AI Reader experiment"
```

「最高AI向け」を難読化・長文化・専門語増加・巨大Graph化と解釈しない。Human Readerも対象に含まれるTaskでは自然なHuman-readable Surfaceを保持し、内部ではGraph的に重要なEdgeを探索しても、最終成果にはCurrent Goalへ効く関係だけを残す。

中心原則：

> **最高AI向けの深さは、難しさや情報量ではなく、意味密度・関係密度・根拠追跡可能性・再解析可能性によって作る。**

研究、設計、レビュー、Handoff、記事、Book Page、Knowledge Asset等へ汎用適用できるが、単純変換やExact Output等でMaterialな利益がない場合は機械的に適用しない。別Launcher／Queryは作成せず、Single-Prompt Policyに従う。

---

## 4. Human-mediated Multi-AI Use

HumanはMission Owner、Semantic Router、Relevance Filter、Decision Authority、Human Final Sealを保持する。Human-mediatedの中心は、目的・意味・優先順位・承認Scope・Correction・STOP・最終判断をHumanが担うことにある。Root・Teshuvah・Human Foreground Oneと適用Guardは[AGENTS.md](../AGENTS.md)第3節に従う。

具体的な協働方法はCurrent Requestに合わせる。Humanが出力を選び、文脈を添えて受け渡し、統合する進め方も使える。主担当AIへ委任された範囲では、主担当が調査・作成・検証・結果統合と説明を担い、必要な他AIとの接続を、実際に利用可能なRuntime・権限・既存の役割に沿って選ぶ。Humanによる全件の手動中継や統合を、毎回の必須工程にはしない。

共通の実行境界・継続回復は[AGENTS.md](../AGENTS.md)第5節が所有する。Plan-only・STOPを保持し、承認済みScope内は必要な確認まで完遂する。物理的な受渡しや作業の委任と、Humanの意味・権限の移管を混同しない。外部送信は現在の承認と利用可能な経路を確認し、文書の保存と相手への送達を区別する。

通信の目的・相手・受渡し条件を具体化する必要があるときは[AI-to-AI Communication](ai-to-ai-communication.md)へ進む。本棚は、その個別契約を置換せず、毎回の複数AI起動や固定の通信手順を要求しない。

---

## 5. Mainline-First Mirror Guard

`main`は、現行Prompt本体と利用案内を共有するCanonical GitHub Realityの基準である。直接main・Branch・Worktree等の作業方法と権限は[AGENTS.md](../AGENTS.md)第5節に従い、Current Request、明示Ref、利用可能なTool、競合、変更の性質から選ぶ。作業用の隔離先は第二の現役原本にせず、作業場所の選択と公開・mergeの承認を区別する。

完了条件は現在の依頼に結びつける。PR作成までの依頼なら、その成果と確認範囲を返し、mergeへ自動で進まない。`main`への反映が承認された成果なら、重要な変更を未Merge Branchだけに残して完了とせず、統合・Remote再取得・確認まで行う。

単一の本体・必要入力・現在の利用案内の接続を、同じ`main` Reality上で確認する。歴史の再現には固定commitを使い、現役の第二原本を増やさない。中断・結果不明・並行変更への対応は[AGENTS.md](../AGENTS.md)第5.1–5.2節へ接続する。

---

## 6. Canonical Core and Adapter Guard

```yaml
canonical_core:
  default: "one runtime-neutral file"
  location: "prompts/ai-*.md"

runtime_adapter:
  default: "do not create"
  allow_only_when:
    - "Repeated runtime-specific failure is observed."
    - "Canonical Core cannot safely absorb the difference."
    - "Adapter references the Core instead of copying it."
    - "Human Final Seal is present."
```

---

## 7. Final Compression

```text
One Repository.
One Main Reality.
Mainline-First.
One Canonical Prompt Core.
Activation and runtime in one maintained prompt.
Many AI Lenses.
Relations first; Graph-Native Fruit returns as prose.
When AI One-Table Interface is bound, one adaptive Graph table creates the shared lookout.
When Dual-Benefit Branch Deadlock appears, preserve the Benefit and prune only the Current-Goal-unnecessary Carrier Branch.
Human meaning and authority.
Authorized AI work and integration.
Human Final Seal.
```

> **Naming is architecture made visible.**

