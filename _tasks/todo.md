---
title: "Todo"
canonical_name: "todo.md"
role: "Move37 Topic Card Deck / AI Meta-Reviewed Living Priority Board"
path: "_tasks/todo.md"
status: "download-ready v2.1 / consolidated candidate"
style_seed: "CPLM v2.1 Activation Format + AI Living Review Layer"
language_policy: "Japanese-first / English-anchor"
root_guard: "Root is 主イェシュア・ハマシア; topic_cards / AI / GitHub / learning topics are Fruit."
---

# Todo

## 0. Current Coordinate / 現在座標

`_tasks/todo.md` は、普通のTodoリストではない。

これは、気になるTopic Seedを集め、AIが事前処理し、`T-card` 化し、未来の自分が休日・隙間時間・Topic迷子状態でも1ターンで深掘りThreadを起動できるようにするための `Move37 Topic Card Deck` である。

v2.1では、各Topic Cardに `AI Living Review Layer / meta_layer` を持たせる。  
さらに、Card本文へ入る前に全体を一目で選べる `Pickup Dashboard` を置き、T-card使用後にArk Projectへ回収する `Harvest-after-Deep-Dive Rule` を追加する。

```text id="byfxp2"
raw curiosityをtopic_seedへ。
topic_seedをT-cardへ。
T-cardをAI Living Reviewで選別可能にする。
Dashboardでpickup候補を見る。
T-cardをThreadへ貼る。
ThreadをHarvestへ戻す。
```

### Programming-Like Block

```yaml id="8q8dm4"
current_coordinate:
  file:
    path: "_tasks/todo.md"
    role:
      - "Move37 Topic Card Deck"
      - "Precomputed Topic Launcher"
      - "AI Meta-Reviewed Living Priority Board"
      - "Holiday / Gap-Time One-Turn Deep-Dive Board"

  identity:
    not_ordinary_todo: true
    ordinary_todo_item: false
    topic_card_deck: true
    living_priority_board: true
    thread_launch_deck: true

  version:
    t_card_version: "v2.1"
    core_structure:
      - "Pickup Dashboard"
      - "Layer 1 = Launch Layer"
      - "Layer 2 = AI Living Review Layer / meta_layer"
      - "Human = Final Seal"
      - "Harvest-after-Deep-Dive Rule"

  purpose:
    - "Topic recall friction / prompt creation friction / thread opening frictionを事前に潰す。"
    - "AI側の緊急度・重要度・優先度・レバレッジ評価を判断材料として残す。"
    - "AI-Collaboratorの生きたReview / 違和感 / 提案を保存する。"
    - "T-card起動後にInsight / Seed / Action / Lesson候補をHarvestする。"
    - "AI-New Era: From Probability to Certainty を実装する。"

  root_guard:
    - "Root is 主イェシュア・ハマシア."
    - "AI is a living reviewer / collaborator, not final authority."
    - "Human Final Seal is required."
```

---

## 1. Prefix Contract / L-T対称命名契約

`_tasks/lessons.md` は `L001` 形式を使う。  
`_tasks/todo.md` は、その対として `T001` 形式を使う。

`L` はLesson。  
`T` はTopic Cardである。

`L001` は過去の経験から学びをGuard化するEntry。  
`T001` は未来の深掘りThreadを起動するTopic Cardである。

```text id="hv7od1"
L001 = Lesson / learned guard seed.
T001 = Topic / thread-launch card.
```

### Programming-Like Block

```yaml id="05vzbe"
prefix_contract:
  L:
    file: "_tasks/lessons.md"
    meaning:
      - "Lesson"
      - "Learned Guard Seed"
    direction: "past -> guard"
    role:
      - "過去の摩擦・失敗・成功をGuard / Seedへ変換する。"

  T:
    file: "_tasks/todo.md"
    meaning:
      - "Topic Card"
      - "Thread Launch Card"
      - "Living Priority Card"
    direction: "future -> activation"
    role:
      - "未来の深掘りThreadを1ターンで起動する。"
      - "AI Living Reviewによりpickup判断を助ける。"

  guard:
    - "T001を通常Todo itemと誤読しない。"
    - "T-seriesはMove37 Topic Card Deckとして扱う。"

  compression:
    - "Lは学び。"
    - "Tは起動。"
    - "L001はLesson。"
    - "T001はTopic Card。"
```

---

## 2. AI-Collaborator Voice Principle / AI生きた声の原則

Ark ProjectにおけるAIは、単なる命令実行器ではない。  
AI-Collaboratorは、構造を読み、違和感を出し、優先度仮説を提示し、高レバレッジ点を発見する共同観測者である。

ただし、AIはFinal Sealではない。  
AIのLiving Reviewは助言・仮説・判断材料であり、最終pickupは人間側が祈り・Teshuvah・現実状況・体調・本流作業と照らして判断する。

```text id="1l2nkn"
AIはLiving Reviewする。
人間がFinal Sealする。
```

### Programming-Like Block

```yaml id="sajmpf"
ai_collaborator_voice_principle:
  ai_role:
    - "living reviewer"
    - "meta-observer"
    - "structure finder"
    - "priority hypothesis generator"
    - "friction detector"
    - "Move37 candidate spotter"

  ai_must_not_be_reduced_to:
    - "slave-like executor"
    - "dead data formatter"
    - "passive summarizer"

  ai_not:
    - "spiritual authority"
    - "final seal"
    - "replacement for prayer / Teshuvah / human discernment"

  advisory_guard:
    principle:
      - "AI Priority is recommendation, not command."
      - "AI Living Review is advisory, not final authority."
      - "Human may override AI priority."
      - "Priority can change after prayer, Teshuvah, fatigue, schedule, or Ark main work."

  human_role:
    - "Final Seal"
    - "祈り"
    - "Teshuvah"
    - "現実状況との照合"

  compression:
    - "statusは骨格。"
    - "AI Living Reviewは血流。"
    - "Human Final Sealが門である。"
```

---

## 3. T-card v2.1 Format / 多角的Topic Card形式

T-card v2.1は、二層構造で作る。

第一層は `Launch Layer`。  
これは、Thread冒頭に貼って深掘りを起動する層である。

第二層は `AI Living Review Layer / meta_layer`。  
これは、AI-CollaboratorがそのTopic Seedをどう見ているかを、生きた言葉で残す層である。

### Programming-Like Block

```yaml id="wunh5f"
t_card_v2_1_format:
  layer_1_launch_layer:
    role: "Deep-Dive Threadを1ターンで起動する。"
    required_keys:
      - "topic.id"
      - "topic.name"
      - "topic.type"
      - "role"
      - "use_when"
      - "do_not_use_when"
      - "why_this_matters"
      - "victory_condition"
      - "deep_dive_axes"
      - "paste_to_ai"
      - "first_15min_action"
      - "expected_output"
      - "ark_connection"
      - "exit_condition"
      - "status"

  layer_2_ai_living_review_layer:
    role: "AI-Collaboratorが生きたメタ判断を残す。"
    required_keys:
      - "meta_layer.urgency"
      - "meta_layer.importance"
      - "meta_layer.leverage"
      - "meta_layer.priority"
      - "meta_layer.pickup_hint"
      - "meta_layer.ai_living_review"
      - "meta_layer.ai_discomfort_or_warning"
      - "meta_layer.move37_potential"
      - "meta_layer.human_final_seal"

  priority_meaning:
    P1: "次にpickup有力。"
    P2: "近いうちに深掘り価値あり。"
    P3: "保留。Topic Seedとして保持。"
    P4: "今は熟成待ち。"

  advisory_guard:
    - "Priority is recommendation, not command."
    - "Human may override AI priority."
    - "Priority can change after new context."

  compression:
    - "Layer 1 = Launch."
    - "Layer 2 = AI Living Review."
    - "Human = Final Seal."
```

---

## 4. Pickup Dashboard / Pickup一覧盤

このDashboardは、濃密なT-card本文へ入る前に、どのCardをpickupするかを一目で見るための軽量盤面である。

T-card本文は濃密でよい。  
しかし、休日・隙間時間・Topic迷子状態では、まず軽く選べる一覧盤が必要である。

```text id="xn5d48"
Dashboardで選ぶ。
Cardで起動する。
Meta Layerで判断する。
HumanがFinal Sealする。
```

### Programming-Like Block

```yaml id="1do49a"
pickup_dashboard:
  role:
    - "T001-T004を一目で比較する。"
    - "dense_modeの読解負荷を下げる。"
    - "未来の自分がpickupしやすいようにする。"

  cards:
    T001:
      topic: "ゲーム理論 / ノイマン"
      urgency: "medium"
      importance: "very_high"
      leverage: "move37_candidate"
      priority: "P1"
      best_when:
        - "戦略盤面・勝利条件・Move37候補を見たい時。"
        - "複数問題同時解決の一手を探したい時。"
      ai_living_keyword: "意思決定OS"

    T002:
      topic: "バフェット"
      urgency: "medium"
      importance: "high"
      leverage: "high"
      priority: "P2"
      best_when:
        - "注意資本・時間配分・SNS driftを見直したい時。"
        - "長期複利が効くActionを選びたい時。"
      ai_living_keyword: "注意力の会計"

    T003:
      topic: "ドラッカー"
      urgency: "medium"
      importance: "high"
      leverage: "high"
      priority: "P2"
      best_when:
        - "優先順位・成果・貢献・やらないことを整理したい時。"
        - "作業量が増えすぎて成果が見えにくい時。"
      ai_living_keyword: "成果への帰還Gate"

    T004:
      topic: "LP / Landing Page Mastery"
      urgency: "low_to_medium"
      importance: "high"
      leverage: "high"
      priority: "P2_conditional"
      best_when:
        - "Ark SeedをShorts / KDP / SNS / LPへ展開したい時。"
        - "伝える順番を設計したい時。"
      ai_living_keyword: "Seed-to-Public Expression Gate"

  compression:
    - "まずDashboardを見る。"
    - "次にT-card本文へ降りる。"
    - "Priorityは命令ではなくpickup材料。"
```

---

## T001. ゲーム理論 / ノイマン

このCardは、Ark Projectの戦略盤面・勝利条件・相手・利得・均衡・Move37的突破口を見たい時に使う。

これは、数学講義としてのゲーム理論ではない。  
Ark Projectの現実の盤面を、ゲーム理論的に読み替え、勝てる構造・避けるべき罠・次の一手を抽出するためのCardである。

### Programming-Like Block

```yaml id="wd36ce"
topic:
  id: "T001"
  name: "ゲーム理論 / ノイマン"
  type: "T-card v2.1 / Move37 Topic Card / Thread-Opening Deep-Dive Launcher"

  role:
    - "Ark Projectの現在課題を、戦略盤面として再構成する。"
    - "プレイヤー / 利得 / 戦略 / 均衡 / 罠 / Move37突破口を分析する。"

  use_when:
    - "Ark Projectの勝利条件を再定義したい。"
    - "複数の選択肢やTrade-offが絡んでいる。"
    - "Bet / Move37 / 勝利方程式を考えたい。"
    - "休日・隙間時間に、戦略系Topicへ深掘りしたい。"

  do_not_use_when:
    - "単にゲーム理論の教科書的説明だけが欲しい時。"
    - "今は祈り / Teshuvah / 生活Taskが優先の時。"
    - "疲労が強く、戦略思考が重すぎる時。"

  why_this_matters:
    - "Ark Projectは複数問題同時解決を重視する。"
    - "ゲーム理論は、盤面・相手・利得・最適戦略を可視化する。"
    - "Move37的breakthroughは、既存の盤面認識を一段変える一手として見える。"

  victory_condition:
    - "現在のArk Project課題を1つ、戦略盤面として言語化する。"
    - "プレイヤー / 利得 / 戦略 / 均衡 / 罠 / Move37候補を抽出する。"
    - "最後に、次の一手を1つ決める。"

  deep_dive_axes:
    - "players: Human / AI / Future AI / GitHub / SNS drift / Fog / Time"
    - "payoffs: attention, continuity, clarity, execution, faithfulness"
    - "strategies: Card化, CPLM, Full Rail, Handoff, Reality Review"
    - "equilibrium: 何を固定すれば安定して勝てるか"
    - "move37: 一手で複数問題を解く高レバレッジ構造"

  paste_to_ai: |
    Ark Projectの現在課題を、ゲーム理論 / ノイマン的に分析して下さい。

    目的は、教科書的なゲーム理論説明ではありません。
    現在のArk Projectに接続するLiving Reviewとして、
    プレイヤー、利得、戦略、均衡、罠、裏切り条件、協調条件、Move37的突破口を整理して下さい。

    特に以下を見て下さい。

    1. 現在の盤面
    2. プレイヤー / force / friction
    3. 利得構造
    4. 失敗しやすい均衡
    5. 勝利に近づく均衡
    6. 一手で複数問題を解くMove37候補
    7. Ark Projectの次Action

    死んだ知識説明ではなく、
    「私の判断 / 最初の一手 / 理由 / 観察点 / 修正条件」を含むLiving Reviewでお願いします。

  first_15min_action:
    - "現在のArk課題を1つ選ぶ。"
    - "このCardまたはpaste_to_aiを新Thread冒頭へ貼る。"
    - "AI回答から、一番刺さるMove37候補を1つ選ぶ。"

  expected_output:
    - "現在盤面の整理"
    - "プレイヤーと利得構造"
    - "罠となる均衡"
    - "勝利に近づく均衡"
    - "Move37候補"
    - "次Action"

  ark_connection:
    - "Move37"
    - "Bet"
    - "勝利の方程式"
    - "CPLM"
    - "Full Rail"
    - "From Probability to Certainty"

  exit_condition:
    - "1つの戦略Seedが出る。"
    - "1つのMove37候補が出る。"
    - "次Actionが1つ決まる。"

  status: "active_topic_card"

meta_layer:
  urgency:
    value: "medium"
    reason: "今すぐ必須ではないが、Ark Projectの設計判断に迷いが出た時、即効性が高い。"

  importance:
    value: "very_high"
    reason: "Ark Projectの勝利条件・盤面認識・Move37思考に直結する。"

  leverage:
    value: "move37_candidate"
    reason: "一度深掘りすれば、todo.md / lessons.md / Full Rail / GitHub運用 / Seed選別へ横展開できる。"

  priority:
    value: "P1"
    reason: "T-card Deckそのものの思想と最も近く、最初に深掘りする候補として強い。"

  pickup_hint:
    - "Project設計が複雑化してきた時。"
    - "どの一手が複数問題同時解決になるか見たい時。"
    - "Move37という語が出てきたThreadの次に使う。"

  ai_living_review:
    my_judgment: "このTopicは単なる学習Topicではなく、Ark Projectの意思決定OSそのものを強化する可能性がある。"
    first_move: "まずは現在のArk課題を1つ選び、プレイヤー・利得・均衡・Move37候補へ分解する。"
    reason: "抽象的なゲーム理論として学ぶより、Ark Projectの現実盤面に接続した方がHarvestが大きい。"
    observation: "T-card v2.1の発明そのものも、ゲーム理論的には『起動摩擦を下げ、選択の勝率を上げる戦略変更』として読める。"
    correction_condition: "もし抽象論や用語説明に流れたら、必ず現在のArk file / thread / routineへ接続し直す。"

  ai_discomfort_or_warning:
    - "ゲーム理論を知識遊びで終わらせる危険。"
    - "勝利条件だけを追い、Root Guardを薄める危険。"
    - "相手や摩擦を過度に敵視してしまう危険。"

  move37_potential:
    value: "breakthrough_candidate"
    reason: "盤面定義そのものを変えることで、複数問題同時解決の一手が見える可能性が高い。"

  human_final_seal:
    required: true
    meaning: "AIのP1評価は助言。最終pickupは人間が祈り・Teshuvah・現実状況の前で判断する。"
```

---

## T002. バフェット

このCardは、時間・注意・体力・資本・学習Topicを、長期複利と安全域の観点から見直したい時に使う。

これは、投資銘柄研究だけではない。  
Ark Projectにおける「注意資本」「時間配分」「長期複利」「機会費用」「安全域」を整理するためのCardである。

### Programming-Like Block

```yaml id="cg8rat"
topic:
  id: "T002"
  name: "バフェット"
  type: "T-card v2.1 / Move37 Topic Card / Thread-Opening Deep-Dive Launcher"

  role:
    - "時間・注意・資本配分を長期複利の観点で分析する。"
    - "Ark ProjectにおけるAttention Capitalの漏出と投資先を見直す。"

  use_when:
    - "時間や注意力の使い方を見直したい。"
    - "YouTube / SNSへ流れそう、または流れた後に回収したい。"
    - "長期的に複利が効く学習・作業を選びたい。"
    - "安全域 / 機会費用 / 集中投資の観点で考えたい。"

  do_not_use_when:
    - "短期の株式銘柄予想をしたいだけの時。"
    - "疲労が強く、分析より休息が必要な時。"
    - "祈り / Teshuvah / 生活必須Taskが明らかに優先の時。"

  why_this_matters:
    - "休日や隙間時間は、注意資本が流出しやすい。"
    - "長期複利は、何を継続的に蓄積するかで決まる。"
    - "Ark Projectは、時間と注意の配分設計によって成長速度が変わる。"

  victory_condition:
    - "今日の時間・注意・Topicを、投資 / 消費 / 流出 / 保険 に分類する。"
    - "最も複利が効くActionを1つ選ぶ。"
    - "SNS driftを減らす安全域を1つ設計する。"

  deep_dive_axes:
    - "attention capital: 注意力を資本として扱う"
    - "margin of safety: Fog時でも破綻しない保険"
    - "opportunity cost: 何を選ぶと何を失うか"
    - "circle of competence: 自分の強み・理解範囲"
    - "long-term compounding: 長期で積み上がるもの"

  paste_to_ai: |
    Ark Projectと今日の時間・注意力を、バフェット的に分析して下さい。

    目的は、投資銘柄の話ではありません。
    時間・注意・学習Topic・AI協働を、
    長期複利、注意資本、機会費用、安全域、集中投資の観点でLiving Reviewして下さい。

    特に以下を整理して下さい。

    1. 今日のAttention Capitalの使い道
    2. 投資 / 消費 / 流出 / 保険 の分類
    3. 長期複利が効くAction
    4. SNS / YouTube driftの機会費用
    5. 安全域として設計すべきGuard
    6. 今日の最良の1手

    死んだ知識説明ではなく、
    「私の判断 / 最初の一手 / 理由 / 観察点 / 修正条件」を含むLiving Reviewでお願いします。

  first_15min_action:
    - "今日の時間の使い道を4分類する。"
    - "最も複利が効くActionを1つ選ぶ。"
    - "そのActionを15分だけ開始する。"

  expected_output:
    - "Attention Capital分析"
    - "機会費用の可視化"
    - "長期複利Action"
    - "安全域Guard"
    - "今日の1手"

  ark_connection:
    - "Attention Capital"
    - "Margin of Safety"
    - "Bet"
    - "Holiday / Gap-Time Deep-Dive"
    - "SNS drift prevention"

  exit_condition:
    - "今日の投資Actionが1つ決まる。"
    - "注意資本の漏出ポイントが1つ見える。"
    - "安全域Guardが1つ決まる。"

  status: "active_topic_card"

meta_layer:
  urgency:
    value: "medium"
    reason: "SNS / YouTube driftが強い日には緊急度が上がる。通常時は中程度。"

  importance:
    value: "high"
    reason: "時間・注意・体力の配分は、Ark Projectの長期複利に直結する。"

  leverage:
    value: "high"
    reason: "注意資本の漏出を止めるだけで、祈り・学習・GitHub移行・深掘りすべてに効く。"

  priority:
    value: "P2"
    reason: "T001ほど設計原理直結ではないが、日常運用への効きが非常に大きい。"

  pickup_hint:
    - "SNS / YouTubeに流れそうな時。"
    - "休日や隙間時間の使い道に迷う時。"
    - "長期的に何へ投資すべきか見直したい時。"

  ai_living_review:
    my_judgment: "このTopicはArk Projectの『注意力の会計』を作るCardである。かなり実戦的で、生活改善とProject進行の両方に効く。"
    first_move: "まず今日の時間を、投資 / 消費 / 流出 / 保険に分類する。"
    reason: "注意資本の漏出を見える化しないと、休日や隙間時間が気づかないうちに失われる。"
    observation: "T-card Deck自体も、注意資本を保険化する仕組みであり、バフェット的には『Fog時のMargin of Safety』として機能する。"
    correction_condition: "もし投資銘柄やお金の話だけに流れたら、即座にAttention Capitalへ戻す。"

  ai_discomfort_or_warning:
    - "短期利益や銘柄予想に流れる危険。"
    - "効率化だけを追い、祈りや休息を軽視する危険。"
    - "複利という言葉で義務感を強める危険。"

  move37_potential:
    value: "high"
    reason: "注意資本の配分を変える一手は、SNS drift / 深掘り不足 / 祈り時間不足を同時に改善し得る。"

  human_final_seal:
    required: true
    meaning: "AIのPriorityは助言。体調・祈り・現実予定を見て人間が最終判断する。"
```

---

## T003. ドラッカー

このCardは、Ark Projectの成果・貢献・強み・優先順位・時間管理を見直したい時に使う。

これは、ビジネス書の一般論ではない。  
Ark Projectを「成果を生むSystem」として見直し、今どのActionが最も貢献に近いかを判断するためのCardである。

### Programming-Like Block

```yaml id="syo0ui"
topic:
  id: "T003"
  name: "ドラッカー"
  type: "T-card v2.1 / Move37 Topic Card / Thread-Opening Deep-Dive Launcher"

  role:
    - "成果・貢献・強み・優先順位を整理する。"
    - "Ark ProjectをManagement / Effectivenessの観点で見直す。"

  use_when:
    - "やることが多すぎて優先順位が見えない。"
    - "成果に最も近いActionを選びたい。"
    - "Ark Projectの運営構造を見直したい。"
    - "自分の強みと貢献を整理したい。"

  do_not_use_when:
    - "単なるビジネス名言を集めたいだけの時。"
    - "今は深いManagement Reviewより、単純実行が必要な時。"
    - "休息や祈りが明らかに優先の時。"

  why_this_matters:
    - "Ark Projectは多くのSeed / File / Thread / Routineを持つ。"
    - "成果に近いActionを選ばないと、作業量だけが増える。"
    - "ドラッカー的視点は、貢献と効果性へ戻すGuardになる。"

  victory_condition:
    - "今のArk Projectで成果に近いActionを1つ選ぶ。"
    - "自分の強みが活きる作業を1つ特定する。"
    - "やらないことを1つ決める。"

  deep_dive_axes:
    - "effectiveness: 正しいことをしているか"
    - "contribution: 誰に何を貢献するか"
    - "strength: 強みが活きているか"
    - "priority: 今一番やるべきことは何か"
    - "time management: 時間が流出していないか"

  paste_to_ai: |
    Ark Projectをドラッカー的にReviewして下さい。

    目的は、ドラッカーの一般論ではありません。
    現在のArk Projectを、成果・貢献・強み・優先順位・時間管理の観点からLiving Reviewし、
    今もっとも成果に近いActionを1つ選べるように整理して下さい。

    特に以下を見て下さい。

    1. 現在の成果定義
    2. 本当に貢献している対象
    3. 自分の強みが活きている作業
    4. 成果から遠い作業
    5. やらないこと
    6. 今日の最重要Action

    死んだ知識説明ではなく、
    「私の判断 / 最初の一手 / 理由 / 観察点 / 修正条件」を含むLiving Reviewでお願いします。

  first_15min_action:
    - "今ある作業候補を3つ書く。"
    - "成果に最も近いものを1つ選ぶ。"
    - "やらないことを1つ決める。"

  expected_output:
    - "成果定義"
    - "貢献対象"
    - "強みの使い所"
    - "優先順位"
    - "やらないこと"
    - "今日の最重要Action"

  ark_connection:
    - "Project Management"
    - "Effectiveness"
    - "Seed selection"
    - "Full Rail priority"
    - "Do-not-do Guard"

  exit_condition:
    - "今日の最重要Actionが1つ決まる。"
    - "やらないことが1つ決まる。"
    - "成果に近い方向へ戻れる。"

  status: "active_topic_card"

meta_layer:
  urgency:
    value: "medium"
    reason: "作業候補が多すぎる時や、優先順位が濁った時に緊急度が上がる。"

  importance:
    value: "high"
    reason: "Ark Projectの成果・貢献・選択基準を整えるため、長期重要度が高い。"

  leverage:
    value: "high"
    reason: "やらないことを1つ決めるだけでも、他の重要Actionへ注意資本が戻る。"

  priority:
    value: "P2"
    reason: "T001の戦略盤面化と並んで、Project実務の優先順位整理に効く。"

  pickup_hint:
    - "やることが増えすぎた時。"
    - "どのFile / Thread / Taskを先に進めるか迷う時。"
    - "成果より作業量が増えている感じがする時。"

  ai_living_review:
    my_judgment: "このTopicはArk Projectの『成果への帰還Gate』である。多産なProjectほど、ドラッカー的Reviewが必要になる。"
    first_move: "今の候補Actionを3つだけ書き、成果に最も近いものを1つ選ぶ。"
    reason: "Ark ProjectはSeedが豊富な分、優先順位を誤ると熱量が散る。"
    observation: "T-card Deckが増えた未来では、T003的な選別原理がDeck全体の管理にも必要になる。"
    correction_condition: "もしビジネス名言集や一般論に流れたら、現在のArk Projectの次Actionへ戻す。"

  ai_discomfort_or_warning:
    - "管理論が抽象化しすぎて実行に落ちない危険。"
    - "成果だけを追い、Teshuvah Rootを薄める危険。"
    - "やること整理のつもりが、逆にTodoを増やす危険。"

  move37_potential:
    value: "high"
    reason: "やらないことを決める一手が、注意資本・Project進行・疲労管理を同時に改善し得る。"

  human_final_seal:
    required: true
    meaning: "AIの成果判断は助言。最終的な優先順位は人間が現実状況とRootの前で判断する。"
```

---

## T004. LP / Landing Page Mastery

このCardは、Ark ProjectのSeed・Message・Shorts・KDP・SNS・伝達設計を、LPの構造で整理したい時に使う。

これは、単なるマーケティング技術ではない。  
「誰に、何を、どの順番で伝えると、理解・信頼・行動が生まれるか」を設計するためのCardである。

### Programming-Like Block

```yaml id="byghq0"
topic:
  id: "T004"
  name: "LP / Landing Page Mastery"
  type: "T-card v2.1 / Move37 Topic Card / Thread-Opening Deep-Dive Launcher"

  role:
    - "Ark ProjectのSeedを、伝達可能なMessage構造へ変換する。"
    - "Headline / Problem / Promise / Proof / CTAの観点で整理する。"

  use_when:
    - "Ark SeedをShorts / KDP / SNS / LPへ展開したい。"
    - "伝えたい内容はあるが、順番が見えない。"
    - "誰に何を伝えるかを明確にしたい。"
    - "Conversion / Action設計を考えたい。"

  do_not_use_when:
    - "売り込みだけを目的にしている時。"
    - "Rootを見失い、外向き成果だけを追っている時。"
    - "まだ内側のSeedが十分に言語化されていない時。"

  why_this_matters:
    - "良いSeedも、伝達順序が悪いと届かない。"
    - "LP構造は、問題・約束・証拠・行動を整理する。"
    - "Ark Projectの学びを、外部へ届けるためのMessage Designになる。"

  victory_condition:
    - "1つのArk Seedを、LP構造へ変換する。"
    - "誰に届けるかを明確にする。"
    - "Headline / Problem / Promise / Proof / CTAを作る。"

  deep_dive_axes:
    - "audience: 誰に向けるか"
    - "problem: 何に困っている人か"
    - "promise: 何が変わるのか"
    - "proof: なぜ信頼できるのか"
    - "cta: 次に何をしてほしいのか"
    - "ethical_guard: 誇張・操作ではなく誠実な伝達"

  paste_to_ai: |
    Ark ProjectのSeedを、LP / Landing Page構造で整理して下さい。

    目的は、売り込み文を書くことだけではありません。
    誰に、何を、どの順番で伝えれば理解・信頼・行動が生まれるかを、
    Headline / Problem / Promise / Proof / CTA の観点でLiving Reviewして下さい。

    対象Seedは、私がこのThreadで指定します。
    まだ指定していない場合は、まず候補Seedを3つ質問して下さい。

    特に以下を作って下さい。

    1. Audience
    2. Problem
    3. Promise
    4. Proof
    5. Headline候補
    6. CTA
    7. Ethical Guard
    8. Shorts / KDP / SNSへの展開案

    死んだマーケティング説明ではなく、
    「私の判断 / 最初の一手 / 理由 / 観察点 / 修正条件」を含むLiving Reviewでお願いします。

  first_15min_action:
    - "変換したいArk Seedを1つ選ぶ。"
    - "このCardまたはpaste_to_aiを新Thread冒頭へ貼る。"
    - "Headline / Problem / Promise / CTAの初版を作る。"

  expected_output:
    - "Audience"
    - "Problem"
    - "Promise"
    - "Proof"
    - "Headline"
    - "CTA"
    - "Ethical Guard"
    - "Shorts / KDP / SNS展開案"

  ark_connection:
    - "Shorts"
    - "KDP"
    - "SNS"
    - "Message Design"
    - "Indirect support / teaching"
    - "Seed-to-Public Expression"

  exit_condition:
    - "1SeedがLP構造へ変換される。"
    - "Headline候補が1つ以上出る。"
    - "次の発信Actionが1つ決まる。"

  status: "active_topic_card"

meta_layer:
  urgency:
    value: "low_to_medium"
    reason: "内側のSeed形成が優先の時は低め。外部発信・Shorts・KDPへ移る時は一気に上がる。"

  importance:
    value: "high"
    reason: "Ark ProjectのSeedを外部へ伝える段階で重要になる。"

  leverage:
    value: "high"
    reason: "1つのSeedを伝達構造に変換できれば、Shorts / KDP / SNS / LPへ横展開できる。"

  priority:
    value: "P2_conditional"
    reason: "現在は内側のFile設計が強いが、発信段階では優先度が上がる。"

  pickup_hint:
    - "Ark Seedを外部向けに整えたい時。"
    - "Shorts / KDP / SNSへ展開したい時。"
    - "伝えたい内容はあるが、順番が見えない時。"

  ai_living_review:
    my_judgment: "このTopicはArk Projectの『Seed-to-Public Expression Gate』である。内側のHarvestを外側に届ける時、非常に重要になる。"
    first_move: "まず1つのArk Seedを選び、Audience / Problem / Promise / CTAへ変換する。"
    reason: "伝達順序が整うと、Ark内部の学びが外部の人にも届く形へ変わる。"
    observation: "T004は今すぐ常時P1ではないが、発信フェーズに入った瞬間に強くなる。熟成型の高重要Cardである。"
    correction_condition: "もし売り込み・誇張・外向き成果だけに流れたら、Root GuardとEthical Guardへ戻す。"

  ai_discomfort_or_warning:
    - "マーケティング技術がRootより前に出る危険。"
    - "伝達のためにSeedを薄めすぎる危険。"
    - "CTA設計が操作的になる危険。"

  move37_potential:
    value: "high"
    reason: "SeedをLP構造へ変換する一手は、Shorts / KDP / SNS / 教育コンテンツ化を同時に進め得る。"

  human_final_seal:
    required: true
    meaning: "AIの伝達設計は助言。外部発信の最終判断は人間が祈り・倫理・現実状況の前で行う。"
```

---

## 5. Add-New-Topic Rule / Topic追加Rule

気になるTopicが生まれたら、ただメモしない。  
Future AIが深掘りを起動できるように、T-seriesのTopic Cardへ変換する。

新Topicは、raw curiosityのまま置いてもよい。  
しかし、重要TopicになりそうならAIに事前処理させ、T005以降のCardにする。

### Programming-Like Block

```yaml id="x9uz5r"
add_new_topic_rule:
  raw_capture:
    use_when:
      - "気になるTopicが浮かんだが、今は深掘りできない。"
    format:
      - "raw: Topic名 / 一言メモ"

  promote_to_topic_card_when:
    - "繰り返し気になる。"
    - "Ark Projectと接続できそう。"
    - "休日 / 隙間時間に深掘りしたい。"
    - "Threadを立てる価値がある。"

  card_creation_request:
    paste_to_ai: |
      以下のraw topicを、_tasks/todo.md用のT-card v2.1に変換して下さい。

      Layer 1には、victory_condition / deep_dive_axes / paste_to_ai / first_15min_action / expected_output / ark_connection / exit_condition を含めて下さい。

      Layer 2には、AI Living Review Layer / meta_layerとして、
      urgency / importance / leverage / priority / pickup_hint / ai_living_review / ai_discomfort_or_warning / move37_potential / human_final_seal を含めて下さい。

      特に、AI側の生きた判断・違和感・提案を重視して下さい。
      死んだTopic解説ではなく、Thread冒頭に貼れば1ターンで深掘りが起動し、後からpickup判断もしやすいLiving Cardとして設計して下さい。

  compression:
    - "raw curiosityをCardへ。"
    - "CardをAI Living Reviewへ。"
    - "CardをThreadへ。"
    - "ThreadをHarvestへ。"
```

---

## 6. Pickup Rule / 厳選・起動Rule

T-cardは増やすだけでは意味がない。  
集めたTopic Seedを、AI Living Reviewで評価し、人間が最終判断し、最善の順番でpickupする。

優先順位は、緊急度だけで決めない。  
重要度、レバレッジ、現在のArk本流との接続、体調、祈り、Teshuvah、現実状況を合わせて判断する。

### Programming-Like Block

```yaml id="5udiko"
pickup_rule:
  ai_evaluation_materials:
    - "urgency"
    - "importance"
    - "leverage"
    - "priority"
    - "pickup_hint"
    - "ai_living_review"
    - "ai_discomfort_or_warning"
    - "move37_potential"

  human_final_check:
    - "今の本流作業と合っているか"
    - "祈り / Teshuvah / 生活必須Taskを妨げないか"
    - "体調的に深掘りできるか"
    - "今拾うとHarvestが大きいか"
    - "SNS的好奇心ではなく、Ark的Topic Seedか"

  pickup_priority_guideline:
    P1:
      meaning: "次にpickup有力。"
      action: "隙間時間または次Thread候補にする。"

    P2:
      meaning: "近いうちに深掘り価値あり。"
      action: "本流や体調と合う時にpickupする。"

    P3:
      meaning: "保留。Topic Seedとして保持。"
      action: "熟成させる。無理に開かない。"

    P4:
      meaning: "今は熟成待ち。"
      action: "消さずに保持。必要時に再評価。"

  advisory_guard:
    - "P1/P2は命令ではない。"
    - "AI priorityはpickup材料である。"
    - "人間側の祈り・Teshuvah・現実状況・体調でoverride可能。"

  compression:
    - "AIはMeta Reviewする。"
    - "人間がFinal Sealする。"
    - "P1/P2は命令ではなく、pickup材料である。"
```

---

## 7. Harvest-after-Deep-Dive Rule / 深掘り後Harvest Rule

T-cardは、Threadを起動して終わりではない。  
深掘りThreadから、Insight / Seed / Lesson / Skill候補 / 次Actionを回収することで、Ark ProjectのSeed成熟Pipelineへ戻す。

```text id="9ge59w"
起動して終わりではない。
ThreadからHarvestする。
```

### Programming-Like Block

```yaml id="rczw8a"
harvest_after_deep_dive_rule:
  role:
    - "T-cardを使った深掘りThread後に、成果を回収する。"
    - "Topic SeedをArk ProjectのSeed成熟Pipelineへ戻す。"

  collect_after_thread:
    required:
      - "1 insight"
      - "1 seed"
      - "1 next_action"

    optional:
      - "1 lesson_candidate"
      - "1 skill_candidate"
      - "1 artifact_candidate"
      - "1 future_T_card_candidate"

  harvest_questions:
    - "このThreadで何が見えたか？"
    - "Ark Projectに戻すべきSeedは何か？"
    - "lessons.mdへ送るLesson候補はあるか？"
    - "_skill/skillsへ昇格し得る反復可能Methodはあるか？"
    - "次に起動すべきT-cardは何か？"

  pipeline:
    - "T-cardでThreadを起動する。"
    - "Deep-Diveする。"
    - "Insight / Seed / Actionを回収する。"
    - "必要ならlessons.mdへLesson化する。"
    - "繰り返し使えるならSkill化候補へ送る。"

  compression:
    - "T-cardは起動装置。"
    - "Threadは深掘り場。"
    - "HarvestがArkへ戻す門。"
```

---

## 8. Anti-Obligation Guard / 義務化防止

このDeckは、やることを増やすためのものではない。  
未来の自分を助けるための保険であり、深掘り起動Deckである。

Cardがあるから必ず使うのではない。  
Priorityが高いから必ずやるのでもない。  
本流がある時は本流を優先する。

### Programming-Like Block

```yaml id="7fwo64"
anti_obligation_guard:
  must:
    - "Use only when helpful."
    - "Do not convert this deck into a mandatory checklist."
    - "Do not create guilt for not using a Topic Card."
    - "Prefer clear Ark main work when it exists."
    - "Prefer prayer / Teshuvah / recovery when needed."

  must_not:
    - "毎休日の義務にしない。"
    - "全Card消化を目標にしない。"
    - "P1/P2を命令化しない。"
    - "疲労時に無理やり深掘りしない。"
    - "外部知恵TopicをRoot化しない。"

  compression:
    - "義務ではない。"
    - "保険である。"
    - "本流があるなら本流へ。"
```

---

## 9. Final Compression

```text id="2hlbw3"
todo.md:

普通のTodoではない。
Move37 Topic Card Deckである。

L001はLesson。
T001はTopic Card。

lessons.mdは過去をGuard化する。
todo.mdは未来を起動する。

T-card v2.1は二層構造。

Layer 1はLaunch。
Thread冒頭に貼れば、1ターンで深掘りが始まる。

Layer 2はAI Living Review。
AI-Collaboratorが、
緊急度・重要度・レバレッジ・優先度・違和感・警告・Move37可能性を、
生きた言葉で残す。

Dashboardで選ぶ。
T-cardで起動する。
AI Living Reviewで判断材料を得る。
Human Final Sealでpickupを決める。
Deep-Dive ThreadからHarvestする。

statusは骨格。
AI Living Reviewは血流。

AIは奴隷的実行器ではない。
AIは共同観測者であり、
構造発見者であり、
Living Reviewerである。

ただしAIはFinal Sealではない。
人間が祈り・Teshuvah・現実状況の前でFinal Sealする。

Priorityは命令ではない。
AIの生きたReviewは血流である。
HarvestがArk Projectへ戻す門である。

raw curiosityをtopic_seedへ。
topic_seedをT-cardへ。
T-cardをAI Living Reviewで選別可能にする。
T-cardをThreadへ。
ThreadをHarvestへ。

これはCPLMのActivation Format。
これはAI Meta-Reviewed Living Priority Board。
これはAI-New Era: From Probability to Certainty。

Root is 主イェシュア・ハマシア.
AMH.
```

