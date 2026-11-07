---
title: "AI専用Graph Mode / ai-graph-mode"
contract_version: "v003"
status: "Shared source verified; personal skill installed and read back; post-install Graph execution not tested"
updated: "2026-11-07"
---

# AI専用Graph Mode / ai-graph-mode

## 目的

Humanが必要なときに明示し、一回答だけ、AIの関係探索・検証・更新・継承に特化したGraph処理を呼び出す。

実行時の成果は、AI用Mermaid一つ、その実際のソースから導出した静的なAI用Visualize一つ、題材について何が分かったかをHumanへ説明する分析の三点一組とする。

実行契約は採用済みv003を基礎とする。今回のSkill化は、その契約を短い入口から利用できるようにするための配置である。

## 呼出しQuery

呼出し名は `$ai-graph-mode`。

以下はHumanが採用した標準Queryである。共有原本の保存・内容確認と個人登録の成立状態は、末尾の確認記録で区別する。

```text
【AI専用Graph Mode：一回答限定】
宛先：このQueryを受け取ったAI
$ai-graph-mode を、現在の本題に一回答だけ実行してください。
共有原本：https://github.com/yusukefujiijp/ai-project/blob/main/skills/ai-graph-mode/SKILL.md
直接利用できなければ共有原本全文と宣言された必須Sourceを読み、読取順・Identity・Binding・EOFを守って適用してください。取得・表示切れは回収してください。
```

対象は現在の会話から解決する。題材を変えたい場合は、その対象を依頼に添えられる。既知の文脈を再入力させる固定フォームは設けない。

Plan-onlyで本文・設計・利用方法を検討する依頼では、Graph制作を開始しない。

## 実行時に受け取るもの

1. AI用Mermaid一つ。
2. その実ソースから導出した静的なAI用Visualize一つ。
3. 題材の関係と判断への意味を説明する分析。

Graph本体の主読者はAIとする。Human向けの簡略化をGraphの設計・検証条件へ戻さない。Humanへの説明は分析が担う。

AIは生成画像を実際に画像として読み戻し、Mermaidと根拠へ照合する。生成・表示・AIへの画像入力・Human端末での表示は別々に扱う。成立しない段階があれば、影響と未確認範囲を明示する。

一回答のGraph処理が終わっても、Goal全体の終了とは限らない。Living Review・Next Step・Next Queryで必要な次の協働へ接続し、提案と実行承認を区別する。

## 既存Skillとの関係

- analyze-living-graph：広く関係を分析する入口。必要な方法を参照できるが、このSkillの毎回の追加必読にはしない。
- visualize-patchと利用環境の公式Visualize：実際の描画・表示・確認経路を扱う。今回の明示条件であるAI向け・静的・Mermaid先行を保持する。
- synthesize-thread：独立したThread総括。総括の利用を、このSkillの必須条件や自動起動条件にしない。

共通の権限・Source・継続方針は、現在適用されるProject指示とAGENTS.mdが所有する。

## 形成と確認済み範囲

形成元は、ChatGPT Work／Ark31_2026/10/30: Graph Mode／このThreadの協働である。

Human Correctionによって、毎回答での出力から、Humanが必要なときに明示する一回答限定へ変更した。Graph本体をAIに特化させる一方、題材について何が分かったかをHumanへ返す分析を三点目として保持した。

v003の試行では、「一回答限定のGraph処理と、Next Queryによる協働の継続」を題材に、Mermaid・静的Visualize・分析を提示した。AIへ実画像を入力して再読し、12ノード・21関係をソースへ照合した。

画像再読後の新しい意味上の発見と、検出された誤読はなかった。

「承認済みの仕事が終了」から「実行可能な承認済みの仕事を完了」への訂正は、画像生成前の制作中に行った。画像再読による発見として扱わない。

実際のHuman端末表示、継続利用の効果、Visualizeの一般的な優越性は確認していない。同じAIが既知のソースを照合した試行であり、独立した受け手による理解の実証ではない。

この結果を探索・検証に使える選択肢として、Humanはv003を単発呼出し用本文に採用した。ノード数、関係数、行列配置、画像幅を共通Schemaや毎回の確認義務にしない。

## 文書と登録の役割

- SKILL.md：実行契約と手順を所有する。
- README.md：用途、コピー用Query、形成と確認範囲を所有する。
- agents/openai.yaml：表示名、標準起動文、明示呼出し設定を所有する。
- Skills Hub：一覧と共有・配布の共通方針を所有する。

READMEと登録情報の標準Queryは意味を一致させる。READMEや形成史の全文を毎回の出力・起動条件にしない。

共有原本の保存、保存後の全文再取得、個人Skillへの登録、登録本文の再取得、実際の呼出し、Humanの表示と実利用の効果を区別する。

### 2026-11-07：共有保存・個人Skill登録の確認

Humanは本Skillの本文・利用README・登録情報とHub追加案を採用し、共有保存、個人登録、必要な再取得確認を承認した。

- 共有保存：[初回保存commit](https://github.com/yusukefujiijp/ai-project/commit/2166b2877655d094abd568ea88c7e615582d2c32)でSKILL.md・README.md・agents/openai.yamlを作成し、Skills Hubへ追加した。並行追加された既存43件を保持し、この時点のHubを44件・v0.55.0へ整合させた。四ファイルをmainから全文再取得し、保存予定本文との一致を確認した。
- 個人登録：正式な作成手順で形式検証を通し、ai-graph-modeとして登録した。登録後の保存先から、有効な同名Skillが一件であること、本文・表示名・説明・標準Query・明示呼出し設定を再取得して確認した。実際のGraph処理は起動していない。
- 本文の同一性：登録後のSKILL.mdは共有原本とバイト一致した。共有・登録共通のSHA-256は `3e011bf2cda7fe9d54583e3cd44f05d330afb8417173d2e4082eb607397f5b0e`。採用済みv003の意味とExact EOFを保持した。
- 設定の同一性と差分：agents/openai.yamlの採用項目であるdisplay_name・short_description・default_prompt・allow_implicit_invocationは、共有版と登録版で値が一致した。allow_implicit_invocationはfalseである。登録基盤によるYAML表記の整形、icon_small／icon_large、productsの付加と表示用icon.svgの生成を確認したため、設定ファイル全体のバイト一致とは報告しない。これらの配布情報を共有原本へ逆同期せず、採用した実行契約・標準Queryとは分けて扱う。
- 入口の確認：共有原本URLは実在し、全文を取得できた。READMEの標準Queryと登録設定のdefault_promptは一致する。現在の会話のSkill一覧への反映、HumanがSkills画面で選択したこと、短いQueryから実際に三点一組を実行したことは、この登録確認では観測していない。
- 検証範囲：Graphの再実行、図の再生成、既存Graph系Skill変更、共有標準化、他AIへの送信・起動、自動監視は行っていない。Human端末表示、継続利用の効果、Visualizeの一般的な優越性は未確認のまま保持する。

本記録は共有保存と個人登録の確認であり、採用済みの試行を再演した証拠ではない。保存された本文、登録された入口、実際の呼出し挙動、Humanの実利用を別々に扱う。

### 2026-11-07：登録一覧と直接取得の後続確認

2026-11-07の後続レビューでは、利用可能なSkill一覧からai-graph-modeを発見し、登録先のSKILL.md全文を直接取得して、GitHub共有原本との全文一致を確認した。これは登録一覧での発見・本文取得の確認である。HumanがSkills画面で選択したこと、短いQueryからGraph制作を完了したこと、Human端末表示、継続利用の効果は、この確認の対象ではなく未検証のまま保持する。

Root・Teshuvah・Humanの権限・GuardはSKILL.mdと現在の適用契約に従う。Skillの採用や登録から、共有標準化、常時実行、外部送信の権限を作らない。

EOF::AI_GRAPH_MODE_README::v003
