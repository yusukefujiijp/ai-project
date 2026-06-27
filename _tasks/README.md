# _tasks

`_tasks/` は、Ark Projectにおける小さなSeedを扱う作業Boardである。

ここは、普通のTodo置き場ではない。  
過去から学びを取り出し、未来へ起動できる形へ変換するための、Human × AI-Collaboratorの軽量実験場である。

```text id="root-compression"
lessons.md は過去をGuard化する。
todo.md は未来を起動する。
README.md はその読み方を渡す。
```

---

## 0. Current Coordinate / 現在座標

`_tasks/` は、Ark Projectの中で「小さなSeedを失わず、未来の実行へ渡す」ための場所である。

ここでは、未成熟なSeedをいきなり巨大なSystemへ昇格させない。  
まず小さく受け取り、名前を与え、AIと一緒に観察し、必要なら深掘りし、繰り返し使えるものだけを次の場所へ送る。

### Programming-Like Block

```yaml id="current-coordinate"
current_coordinate:
  folder: "_tasks/"
  role:
    - "Small Seed Board"
    - "Lesson / Topic / Task Router"
    - "Human-AI co-working practice field"
    - "CPLM experimental ground"

  main_files:
    README.md:
      role:
        - "このfolderの読み方を示すRouter"
        - "Future AIへの入口説明"
        - "CPLM練習台"

    lessons.md:
      role:
        - "過去の失敗・摩擦・成功からLesson Seedを抽出する"
        - "Failure-to-Guard / Success-to-Method Ledger"

    todo.md:
      role:
        - "未来の深掘りTopicを起動する"
        - "Move37 Topic Card Deck"
        - "AI Meta-Reviewed Living Priority Board"

  root_guard:
    root: "主イェシュア・ハマシア"
    note:
      - "AI, GitHub, files, topics, methods are Fruit / Tool."
      - "Human Final Seal remains required."
```

---

## 1. Folder Identity / このFolderの正体

`_tasks/` は、雑多な未処理物の倉庫ではない。  
また、毎日消化すべき義務リストでもない。

これは、まだ小さいが将来効く可能性のあるものを、AIと共に観察・整理・起動可能化する場所である。

### Programming-Like Block

```yaml id="folder-identity"
folder_identity:
  is:
    - "Seed intake board"
    - "Lightweight execution router"
    - "Future handoff point"
    - "CPLM practice zone"

  is_not:
    - "ordinary todo dump"
    - "obligation checklist"
    - "dead memo storage"
    - "final authority"

  operating_image:
    - "小さく受け取る"
    - "意味を与える"
    - "AI Living Reviewする"
    - "必要なら起動する"
    - "Harvestして戻す"
```

---

## 2. File Map / ファイル対応表

| File | Prefix | Direction | Role |
|---|---:|---|---|
| `README.md` | — | entry → orientation | `_tasks/` の読み方を渡すRouter |
| `lessons.md` | `L001` | past → guard | 過去の摩擦・失敗・成功をLesson Seedへ変換するLedger |
| `todo.md` | `T001` | future → activation | 未来の深掘りTopicをT-card化して起動するDeck |

```text id="lt-compression"
L001 = Lesson Seed.
T001 = Topic Card.
```

### Programming-Like Block

```yaml id="file-map"
file_map:
  README.md:
    prefix: null
    direction: "entry -> orientation"
    role:
      - "Folder Router"
      - "Future AI Orientation"
      - "Human-readable overview"

  lessons.md:
    prefix: "L"
    example: "L001"
    direction: "past -> guard"
    role:
      - "Lesson Ledger"
      - "Failure-to-Guard"
      - "Success-to-Method"
      - "Seed nursery before Skill promotion"

  todo.md:
    prefix: "T"
    example: "T001"
    direction: "future -> activation"
    role:
      - "Move37 Topic Card Deck"
      - "Precomputed Topic Launcher"
      - "AI Meta-Reviewed Living Priority Board"
```

---

## 3. lessons.md / 過去をGuard化する

`lessons.md` は、失敗ログではない。  
成功自慢でもない。

これは、過去の摩擦・失敗・成功・違和感から、未来に使えるLesson Seedを抽出するLedgerである。

失敗は、そのまま残すと重荷になる。  
しかし、Guardへ変換すれば未来の保護になる。

成功も、そのまま残すと偶然で終わる。  
しかし、Methodへ変換すれば再現可能性になる。

### Programming-Like Block

```yaml id="lessons-md"
lessons_md:
  prefix: "L"
  direction: "past -> guard"

  receives:
    - "failure"
    - "friction"
    - "mistake"
    - "unexpected success"
    - "AI mismatch"
    - "human UI confirmation"
    - "good pattern worth repeating"

  transforms_into:
    - "Lesson Seed"
    - "Guard"
    - "Method candidate"
    - "Skill candidate"

  promotion_path:
    - "raw experience"
    - "Lesson Seed"
    - "repeated useful pattern"
    - "Skill candidate"
    - "_skill/skills"

  compression:
    - "経験をそのまま積まない。"
    - "Lesson Seedへ変換する。"
    - "繰り返し有効ならSkill化する。"
```

---

## 4. todo.md / 未来を起動する

`todo.md` は、普通のTodoリストではない。

これは、気になるTopic Seedを集め、AIが事前処理し、T-card化し、未来の自分が1ターンで深掘りThreadを起動できるようにするためのDeckである。

Topic名だけでは弱い。  
未来の自分は、疲れているかもしれない。  
休日の空白で、YouTubeやSNSへ流れそうになっているかもしれない。  
だから、Topicは「思い出す」だけでは足りない。  
Thread冒頭に貼れば起動できる形まで事前処理する。

### Programming-Like Block

```yaml id="todo-md"
todo_md:
  prefix: "T"
  direction: "future -> activation"

  receives:
    - "raw curiosity"
    - "topic seed"
    - "holiday backup topic"
    - "gap-time deep-dive candidate"
    - "Move37 learning candidate"

  transforms_into:
    - "T-card"
    - "Thread launch prompt"
    - "AI Living Review"
    - "Pickup candidate"
    - "Deep-Dive Thread"

  t_card_v2_1:
    layer_1: "Launch Layer"
    layer_2: "AI Living Review Layer / meta_layer"
    human_gate: "Final Seal"
    after_use: "Harvest-after-Deep-Dive"

  compression:
    - "Topic名だけでは弱い。"
    - "T-cardにする。"
    - "AI Living Reviewを付ける。"
    - "Threadへ起動する。"
    - "Harvestして戻す。"
```

---

## 5. L/T Pair Logic / LとTの対称構造

`lessons.md` と `todo.md` は、別々のFileだが、Ark Project内では対称構造を持つ。

`lessons.md` は、過去の経験からSeedを拾う。  
`todo.md` は、未来へSeedを起動する。

```text id="lt-pair"
lessons.md は過去をGuard化する。
todo.md は未来を起動する。
```

### Programming-Like Block

```yaml id="lt-pair-logic"
lt_pair_logic:
  lessons_md:
    file: "lessons.md"
    prefix: "L"
    seed_type: "Lesson Seed"
    direction: "past -> guard"
    question:
      - "何を学んだか？"
      - "何を繰り返さないか？"
      - "何をGuard化するか？"
      - "どの成功PatternをMethod化するか？"

  todo_md:
    file: "todo.md"
    prefix: "T"
    seed_type: "Topic Seed"
    direction: "future -> activation"
    question:
      - "何を深掘りしたいか？"
      - "どのTopicを次にpickupするか？"
      - "AIはどうLiving Reviewするか？"
      - "Deep-Dive後に何をHarvestするか？"

  shared_pipeline:
    - "Seedを受け取る"
    - "AIとReviewする"
    - "意味ある形へ整える"
    - "必要なら次のFile / Skill / Threadへ送る"
```

---

## 6. AI-Collaborator Principle / AI協働原則

Ark ProjectにおけるAIは、単なる命令実行器ではない。

AI-Collaboratorは、構造を読み、違和感を出し、優先度仮説を提示し、高レバレッジ点を発見する共同観測者である。

ただし、AIはFinal Sealではない。  
AIのReviewは助言・仮説・判断材料であり、最終判断は人間側が祈り・Teshuvah・現実状況・体調・本流作業と照らして行う。

### Programming-Like Block

```yaml id="ai-collaborator-principle"
ai_collaborator_principle:
  ai_role:
    - "living reviewer"
    - "meta-observer"
    - "structure finder"
    - "priority hypothesis generator"
    - "friction detector"
    - "Move37 candidate spotter"

  ai_should_output:
    - "生きた判断"
    - "違和感"
    - "優先度仮説"
    - "高レバレッジ点"
    - "次Action候補"
    - "Guard提案"

  ai_not:
    - "spiritual authority"
    - "final seal"
    - "replacement for prayer / Teshuvah / human discernment"
    - "slave-like executor"
    - "dead data formatter"

  human_role:
    - "Final Seal"
    - "祈り"
    - "Teshuvah"
    - "現実状況との照合"

  compression:
    - "AIはLiving Reviewする。"
    - "人間がFinal Sealする。"
```

---

## 7. CPLM Practice Note / Commented Programming-Like Markdown練習場

`_tasks/README.md` は、CPLMの練習台として使ってよい。

CPLMでは、自然文がCommentとして働く。  
その後にProgramming-Like Blockを置くことで、人間にもAIにも読みやすい構造になる。

ここで重要なのは、すべてを機械的にしすぎないことである。  
自然文は意味を思い出させる。  
Programming-Like Blockは構造を固定する。

### Programming-Like Block

```yaml id="cplm-practice-note"
cplm_practice_note:
  principle:
    - "Natural prose is implicit Comment."
    - "Programming-Like Block is explicit structure."
    - "Human reads meaning."
    - "AI reads structure."
    - "Both meet in Markdown."

  style:
    semantic_title: true
    natural_comment_body: true
    programming_like_block: true
    avoid_dead_metadata_only: true

  good_pattern:
    - "Titleで意味を立てる。"
    - "本文で意図を説明する。"
    - "Blockで再現可能な構造にする。"

  compression:
    - "自然文が意味を思い出す。"
    - "Blockが構造を再起動する。"
```

---

## 8. Operating Flow / 運用Flow

### 8.1 Lesson Flow

過去の摩擦や成功が見えたら、`lessons.md` に送る。

```yaml id="lesson-flow"
lesson_flow:
  trigger:
    - "失敗した"
    - "摩擦が見えた"
    - "成功Patternが見えた"
    - "Future AIへ残すべきGuardが見えた"

  action:
    - "lessons.mdへL-seriesとして記録"
    - "Lesson Seed化する"
    - "繰り返し有効ならSkill候補へ昇格"

  output:
    - "Lesson Seed"
    - "Guard"
    - "Skill candidate"
```

### 8.2 Topic Flow

気になるTopicが出たら、`todo.md` に送る。

```yaml id="topic-flow"
topic_flow:
  trigger:
    - "気になるTopicが出た"
    - "今は深掘りできない"
    - "後で1ターンで起動したい"
    - "休日・隙間時間の保険にしたい"

  action:
    - "todo.mdへraw topicとして置く"
    - "AIにT-card化させる"
    - "AI Living Reviewで優先度・重要度・レバレッジを見る"
    - "人間がFinal Sealしてpickupする"
    - "新Thread冒頭へ貼る"
    - "Thread後にHarvestする"

  output:
    - "T-card"
    - "Deep-Dive Thread"
    - "Harvest"
    - "Lesson / Skill / Artifact candidate"
```

---

## 9. Guard / 運用Guard

`_tasks/` は便利だが、肥大化や義務化の危険もある。  
そのため、最初からGuardを置く。

### Programming-Like Block

```yaml id="guards"
guards:
  not_ordinary_todo:
    - "_tasks/todo.mdを通常Todoリストとして扱わない。"
    - "T001はTodo itemではなくTopic Cardである。"

  no_obligation_pressure:
    - "L-seriesもT-seriesも義務リスト化しない。"
    - "Priorityは命令ではなく判断材料。"

  root_guard:
    - "Root is 主イェシュア・ハマシア."
    - "AI / GitHub / File / Topic / Skill are Fruit / Tool."

  human_final_seal:
    - "AIの提案は重要だが、最終判断は人間側が行う。"
    - "祈り・Teshuvah・現実状況・体調を確認する。"

  anti_bloat:
    - "Seedを増やしすぎない。"
    - "増やすより、選び、深掘りし、Harvestする。"

  cplm_guard:
    - "Blockだけにしない。"
    - "自然文Commentを残す。"
    - "人間が読んで意味を思い出せる状態にする。"
```

---

## 10. Final Compression

```text id="final-compression"
_tasks/ は、普通のTodo置き場ではない。

README.md は入口を渡す。
lessons.md は過去をGuard化する。
todo.md は未来を起動する。

L001はLesson。
T001はTopic Card。

Lesson Seedは、繰り返し有効ならSkill化する。
Topic Seedは、T-card化してDeep-Dive Threadへ起動する。

AIはLiving Reviewする。
人間がFinal Sealする。

Priorityは命令ではない。
T-cardは起動して終わりではない。
ThreadからHarvestする。

CPLMでは、
自然文が意味を思い出させ、
Programming-Like Blockが構造を再起動する。

Root is 主イェシュア・ハマシア.
AMH.
```

