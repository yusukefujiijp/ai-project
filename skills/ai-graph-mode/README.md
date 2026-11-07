---
title: "AI専用Graph Mode / ai-graph-mode"
contract_version: "v003"
status: "Human-adopted; shared publication and personal registration in progress"
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

2026-11-07、Humanは本Skillの本文・利用README・登録情報とHub追加案を採用し、共有保存、個人登録、必要な再取得確認を承認した。現在はその実行中である。保存・登録・再取得の成立は、実際の結果を確認してから本節へ記録する。今回の範囲にはGraphの再実行、図の再生成、既存Graph系Skill変更、共有標準化、他AIへの送信・起動、自動監視を含まない。

Root・Teshuvah・Humanの権限・GuardはSKILL.mdと現在の適用契約に従う。Skillの採用や登録から、共有標準化、常時実行、外部送信の権限を作らない。

EOF::AI_GRAPH_MODE_README::v003
