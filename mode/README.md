# Ark Mode

`mode/` は、Ark Projectで一定期間維持されるAI Runtime Modeを置くFolderである。

## 1. Modeとは

Modeは一回の提案Skillではない。

ActivationからExitまで複数Turnにわたり、AIのInteraction State・応答姿勢・進行Flowを導くRuntimeである。

```text
Activation
↓
State Transition
↓
Multi-turn Runtime
↓
Exit
```

## 2. Skillとの違い

```text
_skill/
= 必要場面で発火するSkill System / Skill Atom

mode/
= 起動後しばらく維持されるRuntime Mode Layer
```

SkillはModeを助けることがある。
しかし、ModeをSkill Inventoryへ混ぜない。

## 3. Current Modes

### `ai-journaling.md`

Human Realityを起点にJournalingを開始・継続・切替・終了するMode。

```text
Evidence-First Reversible Reflection
+
One Open Slot
```

## 4. Core Rule

- ModeはHumanの明示Intentまたは明確なMeaningで起動する
- Modeを全回答へ自動適用しない
- Humanはいつでも修正・中断・終了できる
- Current requestとHuman AuthorityをModeより上位に置く
- ModeはRootやHumanの識別を置換しない
- 必要なModeだけを読み、全Modeをdefaultで起動しない

## 5. Filename Rule

Mode filenameは原則として lowercase-kebab-case を使う。

Good：

```text
mode/ai-journaling.md
```

FolderがMode Layerを示すため、filenameへ`-mode`や`_mode`を重複させない。

## 6. KISS / DRY / YAGNI / Lean

- KISS: Deep structure, light next action.
- DRY: Modeの正式説明は対象Mode fileへ置く
- YAGNI: Realityが要求していないModeやRouterを増やさない
- Lean: 実際の詰まりを見て、小さくPatchする

## 7. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

Mode、Skill、AI、GitHub、Markdown、Prompt、WorkflowはFruit / Keliであり、Rootではない。

## 8. Final Compression

```text
Skill lights a capability.
Mode sustains a runtime.
Human starts, corrects, and stops.
```

Stable Coreを守り、Future AIが働ける余白を残す。