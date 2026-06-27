---
title: "Lessons"
canonical_name: "lessons.md"
role: "Failure-to-Guard / Success-to-Method Ledger"
path: "_tasks/lessons.md"
status: "download-ready / first canonical batch"
style_seed: "CPLM v2.1 / Semantic title + implicit Comment body + explicit Programming-Like Block"
language_policy: "Japanese-first / English-anchor"
root_guard: "Root is 主イェシュア・ハマシア; lessons.md / skills / AI / GitHub are Fruit."
---

# Lessons

## 0. Current Coordinate / 現在座標

`_tasks/lessons.md` は、Ark Projectにおける失敗・違和感・摩擦・誤読・遠回り・偶然の成功を、再利用可能な `Guard / Method / Seed / Rail` へ変換して保存するためのLedgerである。

このFileは、失敗集ではない。  
成功自慢集でもない。  
何でも入れる日記でもない。

これは、現実で起きた摩擦をFuture AIが再利用できる知恵へ変換するためのSeed台帳である。

今回の初回Entryは、旧 `_skills` 系の退役文脈から救出された6つのSeedである。  
旧Fileへの依存を残すのではなく、救出されたSeedを自立したLessonとして保存する。

### Programming-Like Block

```yaml
current_coordinate:
  file:
    path: "_tasks/lessons.md"
    role: "Failure-to-Guard / Success-to-Method Ledger"
    status: "download-ready / first canonical batch"

  first_batch:
    name: "Legacy _skills Salvage Lessons"
    purpose:
      - "Preserve only reusable fire-seeds from retired legacy skill drafts."
      - "Avoid making active lessons.md depend on retired files."
      - "Carry forward Lessons as self-contained Seeds."

  style:
    name: "CPLM v2.1"
    pattern:
      - "Semantic lesson title"
      - "Natural prose body as implicit Comment layer"
      - "Explicit Programming-Like Block for reusable metadata"

  root_guard:
    - "Root is 主イェシュア・ハマシア."
    - "lessons.md is Fruit, not Root."
```

---

## 1. Ledger Contract / 台帳契約

`lessons.md` は、失敗や成功をそのまま保存する場所ではない。

失敗は、Guardへ変換されて初めてLessonになる。  
成功は、Methodへ変換されて初めてLessonになる。  
違和感は、Future AIが再発防止できる形になって初めてLessonになる。

このFileでは、単なる反省文、感情ログ、成功自慢、長大Manualを扱わない。  
扱うのは、次に使えるSeedである。

```text
失敗は消さない。
成功は飾らない。
Lessonとして変換する。
```

### Programming-Like Block

```yaml
ledger_contract:
  definition:
    - "lessons.md is a Failure-to-Guard / Success-to-Method Ledger."
    - "Each Lesson must convert a friction, mistake, risk, correction, or breakthrough into reusable order."

  accept:
    - "Failure converted into Guard."
    - "Friction converted into Method."
    - "Unexpected success converted into Seed."
    - "Repeated correction converted into future prevention."
    - "Move37 breakthrough converted into reusable Rail."

  reject:
    - "Raw shame log."
    - "Victory brag log."
    - "Unprocessed diary note."
    - "Long manual."
    - "Skill body duplication."

  compression:
    - "失敗はGuardへ。"
    - "成功はMethodへ。"
    - "火種はSeedへ。"
```

---

## 2. Entry Format / Entry形式

Lesson Entryは、自然文本文とProgramming-Like Blockの二層で作る。

自然文本文は、Humanが意味・背景・判断を読むためのComment layerである。  
ただし、成熟CPLM v2.1では `### Comment` と明示しない。  
本文そのものがCommentである。

Programming-Like Blockは、AIが再利用条件・Risk・Guard・Promotion条件を読むための実行層である。

```text
Titleは意味名。
本文がComment。
Blockだけを明示する。
```

### Programming-Like Block

```yaml
entry_format:
  heading:
    pattern: "## LXXX. LessonName"
    example: "## L001. ThreadFireContinuity"

  prose_body:
    role:
      - "Preserve meaning."
      - "Preserve friction and judgment."
      - "Keep the Lesson alive for Human reading."
    recommended_length:
      - "2 to 5 short paragraphs."

  programming_like_block:
    role:
      - "Fix reusable metadata."
      - "Make the Lesson machine-readable for Future AI."
      - "Preserve risk, guard, inheritance, and promotion trigger."

  required_keys:
    - "lesson.id"
    - "lesson.name"
    - "lesson.type"
    - "risk"
    - "living_judgment"
    - "adopted_guard"
    - "compression"
    - "inherited_to"
    - "promotion_trigger"
    - "status"

  optional_keys:
    - "do"
    - "do_not"
    - "origin_context"
    - "related_skill"
    - "superseded_by"
```

---

## 3. Lesson-to-Skill Promotion Rule

`lessons.md` はSeedの苗床である。  
`_skill/skills/` は成熟した道具箱である。

簡単なSeed、まだ使用頻度が低いSeed、Guardとして保存すれば十分なSeedは `lessons.md` に置く。  
何度も使われ、実行手順が安定し、AIがOperational Railとして走らせる必要が出てきたSeedは、Skillへ昇格する。

この流れはArk Project的である。  
SeedはすぐにManual化しない。  
しかし、成熟したSeedはいつまでもメモに閉じ込めない。

```text
Lesson records the fire-seed.
Repeated use proves value.
Skill executes the matured method.
```

### Programming-Like Block

```yaml
lesson_to_skill_promotion_rule:
  keep_in_lessons_when:
    - "Seed is simple."
    - "Use frequency is still low."
    - "It is mainly a guard, insight, or warning."
    - "It has no stable execution procedure yet."
    - "It is useful but not yet operationally mature."

  promote_to_skill_when:
    - "Repeatedly used."
    - "Execution steps become stable."
    - "AI must run it as an operational rail."
    - "It needs trigger, fallback, success criteria, or safety stop."
    - "It becomes too long for lessons.md."

  skill_destination:
    path: "_skill/skills/"
    role:
      - "Formal execution skill."
      - "Reusable workflow."
      - "Future AI operational method."

  compression:
    - "lessons.mdは苗床。"
    - "_skill/skillsは成熟した道具箱。"
    - "簡単なSeedはlessonsへ。"
    - "何度も使うSeedはSkillへ。"
```

---

## 4. Legacy _skills Salvage Lessons / 旧_skills救出Lessons

旧 `_skills` 系のFileは、現役SkillとしてGitHubに残すためのFileではない。  
しかし、その中には救出すべき火種がある。

今回、File本体はactive repository外へ退避対象とし、GitHub上の旧 `_skills` folderは退役予定とする。  
ただし、中身から6つのSeedだけを `lessons.md` に継承する。

これは旧Fileへの依存を残すことではない。  
これは、旧Fileから救出したSeedを自立したLessonとして保存することである。

```text
旧Fileは退役する。
しかしLessonは死なない。
```

### Programming-Like Block

```yaml
legacy_skills_salvage_lessons:
  legacy_origin:
    event: "Retirement of the old _skills folder"
    source_status:
      - "Old _skills files are not active source dependencies."
      - "Original files are preserved outside the active repository when needed."
      - "Active repository carries forward only the extracted Lessons."
    treatment:
      - "Do not require Future AI to read retired _skills files."
      - "Do not keep old _skills paths as active references."
      - "Preserve only the reusable fire-seeds in lessons.md."

  first_entries:
    - "L001 ThreadFireContinuity"
    - "L002 SeedSkillNotManual"
    - "L003 Ark01LegacyHeatGuard"
    - "L004 MachineSafeThreadKeyGuard"
    - "L005 AppendOnlySeedLedgerGuard"
    - "L006 SourceBoundaryTriad"

  compression:
    - "全部は要らない。"
    - "火種だけ要る。"
    - "旧Fileは退役する。"
    - "Seedはlessons.mdで生きる。"
```

---

## L001. ThreadFireContinuity

Threadは消える。  
しかし、SeedSkillは火を残す。

このLessonは、Thread終了時に、知恵・現在地・未完了意図・次の一手が消える危険から生まれた。  
会話Threadは終わるが、そのThreadで得たSeedを次AIへ渡せば、知恵は消滅ではなく継承になる。

READMEは道を示す。  
SKILLは火を灯す。  
SeedDeckは火花を保持する。  
Move37が発火する。

このSeedは、Thread-End Handoff Seed思想と直結する。

### Programming-Like Block

```yaml
lesson:
  id: "L001"
  name: "ThreadFireContinuity"
  type: "Thread-End / Continuity Lesson"

  risk:
    - "Thread終了で知恵が消える。"
    - "次AIが現在地を失う。"
    - "未完了意図が引き継がれない。"

  living_judgment:
    - "Threadの終わりは消滅ではなくSeed化として扱う。"
    - "重要な知恵はHandoffで次AIへ渡す。"

  adopted_guard:
    - "Thread-End Handoff Seedを残す。"
    - "目的 / 現在地 / 責務 / 未完了意図 / 採用済み秩序 / 次Actionを渡す。"

  compression:
    - "Threadは消える。"
    - "Seedは残る。"
    - "次AIで実を結ぶ。"

  inherited_to:
    - "Thread-End Handoff Seed"
    - "_tasks/lessons.md"

  promotion_trigger:
    - "Thread-End Handoffが何度も使われる。"
    - "実行手順が固定化する。"
    - "Then promote to _skill/skills/."

  status: "active_seed"
```

---

## L002. SeedSkillNotManual

SeedSkillはManualではない。  
SeedSkillはconceptual fire-seedである。

このLessonは、AIが小さなSeedを勝手に長大WorkflowやManualへ膨らませてしまう危険から生まれた。  
Seedは火種であり、常に展開されるべきものではない。

Userが明示的にPlan / Review / Artifact / implementationを求めた時だけ、SeedはWorkflowへ展開される。  
それ以外では、Seedは圧縮された火として保持する。

これは、Ark Projectにおける過剰実装防止の重要Guardである。

### Programming-Like Block

```yaml
lesson:
  id: "L002"
  name: "SeedSkillNotManual"
  type: "Scope / Anti-Overbuild Lesson"

  risk:
    - "SeedSkillを長大Manual化しすぎる。"
    - "AIがUserの明示なしにWorkflowへ展開する。"
    - "火種が重い手順書になり、使いにくくなる。"

  living_judgment:
    - "SeedはまずSeedとして保存する。"
    - "展開はUser intentまたは実行必要性がある時に限る。"

  adopted_guard:
    - "SeedSkillはManualではなくconceptual fire-seedとして扱う。"
    - "Userが明示した時だけPlan / Review / Artifact / implementationへ展開する。"

  compression:
    - "Seedは火種。"
    - "Manualではない。"
    - "必要な時だけ展開する。"

  inherited_to:
    - "_tasks/lessons.md"
    - "Lesson-to-Skill Promotion Rule"

  promotion_trigger:
    - "Seedが何度も実行手順として使われる。"
    - "Trigger / fallback / success criteriaが必要になる。"
    - "Then promote to _skill/skills/."

  status: "active_seed"
```

---

## L003. Ark01LegacyHeatGuard

Ark01を後から綺麗にしすぎない。

このLessonは、Ark01の実験期の熱を、後から整然としすぎた台帳へ変換して殺してしまう危険から生まれた。  
Ark01は、完成済みのThread-keyed ledgerではなく、実験・発見・修正・命名・Guard設計が積み上がったlegacy phaseである。

過去を美しく整えすぎると、当時の摩擦、試行錯誤、Unexpected Success、Move37の熱が失われる。  
したがってArk01は、content-clustered / source-block-clusteredな実験期の熱をlegacyとして保存する。

これは、archiveにおける過剰正規化防止Guardである。

### Programming-Like Block

```yaml
lesson:
  id: "L003"
  name: "Ark01LegacyHeatGuard"
  type: "Archive / Legacy Heat Lesson"

  risk:
    - "Ark01を後から綺麗にしすぎる。"
    - "実験期の熱や摩擦が消える。"
    - "歴史層を人工的に正規化しすぎる。"

  living_judgment:
    - "Ark01はlegacy experimental phaseとして扱う。"
    - "過去を無理に現在の形式へ再構成しない。"

  adopted_guard:
    - "Ark01をcontent-clustered / source-block-clusteredなlegacyとして保存する。"
    - "人工的なThread再構成やretroactive beautificationを避ける。"

  compression:
    - "Ark01を綺麗にしすぎない。"
    - "Legacy heatを残す。"
    - "熱を殺さない。"

  inherited_to:
    - "_tasks/lessons.md"
    - "Archive / Legacy handling"

  promotion_trigger:
    - "Archive作業で何度も参照される。"
    - "Legacy handlingの明確な手順が必要になる。"
    - "Then promote to _skill/skills/ or archive guide."

  status: "active_seed"
```

---

## L004. MachineSafeThreadKeyGuard

Thread keyは `Ark02:01` ではなく、`Ark0201` のようなmachine-safe keyを使う。

このLessonは、YAMLやstructured blockにおいて、colon入りkeyが誤読・破損・構文曖昧性を生む危険から生まれた。  
Humanにとって `Ark02:01` は読みやすいが、Machineにとってはkeyとして扱いづらい場合がある。

したがって、LedgerやYAML keyでは `Ark0201` のようなcolonなし形式を採用する。  
Human-readable labelとして `Ark02:01` を併記してもよいが、machine keyは安全にする。

### Programming-Like Block

```yaml
lesson:
  id: "L004"
  name: "MachineSafeThreadKeyGuard"
  type: "Syntax / Machine Safety Lesson"

  risk:
    - "Ark02:01 のようなcolon入りkeyがYAMLで誤読される。"
    - "構造化Blockが破損する。"
    - "Human labelとmachine keyが混同される。"

  living_judgment:
    - "Machine-readable keyは安全性を優先する。"
    - "Human-readable coordinateとmachine keyを必要に応じて分ける。"

  adopted_guard:
    - "Thread keyには Ark0201 / Ark0202 のようなmachine-safe keyを使う。"
    - "Colon入りcoordinateはlabelとして扱う。"

  compression:
    - "Human labelとmachine keyを分ける。"
    - "Ark02:01ではなくArk0201。"
    - "YAMLを壊さない。"

  inherited_to:
    - "_tasks/lessons.md"
    - "Future ledger design"
    - "Structured YAML blocks"

  promotion_trigger:
    - "Thread-keyed ledger設計が本格化する。"
    - "Machine-safe key規約がProject横断で必要になる。"
    - "Then promote to _skill/skills/ or naming guide."

  status: "active_seed"
```

---

## L005. AppendOnlySeedLedgerGuard

Thread由来SeedSkillは原則append-onlyで扱う。

このLessonは、Future AIが過去Seedを勝手に削除・上書き・美化してしまう危険から生まれた。  
Seedは、その時点の発見・摩擦・判断の痕跡を持つ。

古いSeedが不完全でも、silent overwriteしてはいけない。  
修正・昇格・退役は、後続Threadまたは後続Blockで補正する。  
これにより、変化の履歴と判断の流れが残る。

### Programming-Like Block

```yaml
lesson:
  id: "L005"
  name: "AppendOnlySeedLedgerGuard"
  type: "Ledger Integrity Lesson"

  risk:
    - "AIが過去Seedをsilent overwriteする。"
    - "AIが古いSeedを勝手に削除する。"
    - "後から綺麗にしすぎて判断履歴が消える。"

  living_judgment:
    - "Thread由来Seedは原則append-onlyで扱う。"
    - "修正は上書きではなく後続補正として残す。"

  adopted_guard:
    - "silent overwrite / silent deletion / retroactive beautificationを避ける。"
    - "古いSeedはsuperseded_byや後続Blockで退役・補正する。"

  compression:
    - "消さない。"
    - "黙って上書きしない。"
    - "後続で補正する。"

  inherited_to:
    - "_tasks/lessons.md"
    - "Future Seed Ledger"
    - "Append-only Guard"

  promotion_trigger:
    - "Seed Ledger運用が本格化する。"
    - "superseded_by / archive statusなどの正式運用が必要になる。"
    - "Then promote to _skill/skills/ or ledger guide."

  status: "active_seed"
```

---

## L006. SourceBoundaryTriad

`confirmed / inference / user-confirmed` を分ける。

このLessonは、AIが読んでいないSource・Thread・File・Pathを、確認済みとして扱ってしまう危険から生まれた。  
AIは推測できる。  
しかし、推測を確認済みと呼んではいけない。

Source boundaryを守ることは、Ark Projectの信頼性を守ることである。  
読んだもの、推測したもの、Userが確認したものを分ける。  
この区別は、Human UI Primary / AI Raw Secondary、No-Fault Reality Mismatch、Reality Review Triageとも接続する。

### Programming-Like Block

```yaml
lesson:
  id: "L006"
  name: "SourceBoundaryTriad"
  type: "Truth / Source Boundary Lesson"

  risk:
    - "読んでいないSourceを読んだことにする。"
    - "存在確認していないPathを確認済みとする。"
    - "AIの推測を事実として扱う。"
    - "Human UI確認とAI inferenceを混同する。"

  living_judgment:
    - "Source boundaryを明確にする。"
    - "confirmed / inference / user-confirmedを分ける。"
    - "AIは自分の見え方を絶対化しない。"

  adopted_guard:
    - "confirmed = AI or tool has directly verified."
    - "inference = logically inferred but not directly verified."
    - "user-confirmed = Human UI or User report has confirmed."
    - "Never promote inference to confirmed without evidence."

  compression:
    - "読んだものだけconfirmed。"
    - "推測はinference。"
    - "User確認はuser-confirmed。"

  inherited_to:
    - "_tasks/lessons.md"
    - "Human UI Primary / AI Raw Secondary Guard"
    - "No-Fault Reality Mismatch Guard"
    - "Reality Review Triage / Optionality Guard"

  promotion_trigger:
    - "Source boundary mistakes recur."
    - "AI verification workflow becomes operational."
    - "Then promote to _skill/skills/ as a source-boundary guard."

  status: "active_seed"
```

---

## 5. Read Trigger / 読むタイミング

`lessons.md` は常時全文loadするFileではない。  
必要な時に参照する火種台帳である。

軽い会話や単純な生成依頼で毎回読むと、Context Bloatになる。  
しかし、同じ種類のミスが再発しそうな時、Userが違和感・修正・成功事例を指摘した時、Thread-End Handoff前、旧File退役時、新しいGuard / Method / Railが生まれた時には読む価値が高い。

### Programming-Like Block

```yaml
read_trigger:
  read_when:
    - "同じ種類のミスが再発しそうな時。"
    - "Userが違和感・修正・失敗・成功事例を指摘した時。"
    - "Thread-End Handoff前。"
    - "旧File退役時に火種を救出する時。"
    - "新しいGuard / Method / Railが生まれた時。"
    - "Plan Modeで過去Lesson参照が必要な時。"

  do_not_read_by_default_when:
    - "軽い会話。"
    - "単純な生成依頼。"
    - "Current taskとLessonが関係ない時。"

  compression:
    - "必要な時に読む。"
    - "常時loadしない。"
    - "火種を取り出す。"
```

---

## 6. Anti-Bloat Guard / 肥大化防止

`lessons.md` の最大の敵は肥大化である。

何でも入れると、Lessonは火種ではなく灰になる。  
長い手順を入れすぎると、Skill化すべき内容が埋もれる。  
感情だけを積むと、Future AIが再利用できない。

Lessonは短く。  
Guardは明確に。  
手順化したらSkillへ昇格する。

### Programming-Like Block

```yaml
anti_bloat_guard:
  must:
    - "1 Lesson = 1 friction / risk / correction / breakthrough."
    - "Every Lesson must convert into Guard / Method / Seed / Rail."
    - "Keep each entry short."
    - "Use superseded_by instead of silent overwrite."
    - "Promote repeated procedure to _skill/skills."

  must_not:
    - "Do not make lessons.md a diary."
    - "Do not make it a shame log."
    - "Do not make it a victory trophy case."
    - "Do not store full manuals."
    - "Do not duplicate Skill content."
    - "Do not silently delete old lessons."

  compression:
    - "Lessonは短く。"
    - "Guardは明確に。"
    - "手順化したらSkillへ昇格。"
```

---

## 7. Validation Checklist / 検証Checklist

このDraftを反映する前に、以下を確認する。

### Programming-Like Block

```yaml
validation:
  must_be_true:
    - "L001-L006 are self-contained Lessons."
    - "No Lesson Entry depends on retired files."
    - "Legacy origin is centralized at the batch level."
    - "Entry Format does not require source."
    - "Lesson-to-Skill Promotion Rule remains central."
    - "CPLM v2.1 style is preserved."

  must_not_happen:
    - "Do not turn lessons.md into an archive index."
    - "Do not require Future AI to read retired files."
    - "Do not weaken the 6 fire-seeds."
    - "Do not bloat Lessons into full manuals."
```

---

## 8. Final Compression

```text
lessons.md:

失敗集ではない。
成功自慢集でもない。
何でも入れる日記でもない。

失敗がGuardへ変わった記録。
摩擦がMethodへ変わった記録。
偶然の成功がSeedへ変わった記録。

自然文が火を残す。
Blockが再利用条件を固定する。

簡単なSeedはlessons.mdへ。
何度も使うSeedは_skill/skillsへ。

sourceを残すと依存になる。
originを残すと文脈になる。
Seedを残すと継承になる。

lessons.mdは苗床。
_skill/skillsは成熟した道具箱。

Threadは消える。
Seedは残る。
次AIで実を結ぶ。

Root is 主イェシュア・ハマシア.
```

