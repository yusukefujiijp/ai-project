---
type: "Ark-WTP Seed Unit"
unit_id: "ARK_WTP_BERESHIT_HEBREW_WORD_V003"
title: "Bereshit Full-Parasha × Hebrew Word Lens Seed Unit v0.3"
version: "v0.3-capability-revalidation-candidate"
canonical_path: "projects/ark-wtp/seed-units/bereshit.md"
status: "candidate / capability-revalidation-provisional-pass / human-review-required"
project: "Ark-WTP / Weekly Torah Portion / Lens-as-Dimensions"
parasha: "Bereshit"
substrate: "Genesis 1:1–6:8"
lens: "Hebrew Word Lens"
language_policy: "Japanese-first / Hebrew anchors / English control labels"
root: "主イェシュア・ハマシア"
root_guard: "This Seed Unit is a Keli; it does not replace Torah, 主イェシュア・ハマシア, prayer, Human judgment, or lived obedience."
human_final_seal_required: true
artifact_generation_is_final_seal: false
peshat_baseline_status: "reported by predecessor workflow but not found in current repository; not reconstructed or treated as evidence"
primary_text:
  - "Mechon-Mamre, Genesis 1–6, Hebrew Masoretic text"
  - "Sefaria, Genesis 1:1–6:8 range index"
---

# Bereshit Full-Parasha × Hebrew Word Lens Seed Unit v0.3

## 0. Reality and Gate Status

```yaml
reality:
  declared_unit: "Bereshit Full-Parasha × Hebrew Word Lens"
  declared_substrate: "Genesis 1:1–6:8"
  previous_peshat_artifact:
    workflow_claim: "Peshat Lens v0.3 completed and available in Ark05:04 thread draft"
    repository_observation: "No Bereshit / Peshat / Genesis / Torah / Lens content exists in the referenced Ark05:04 file"
    treatment: "Dangling State; do not invent or reconstruct it in this unit"
  current_action: "Create the missing Hebrew Word Lens unit as a capability revalidation candidate"
```

## 1. Lens Focus Line

Hebrew Word Lensは、Bereshit 1:1–6:8をPlotとして再要約せず、同一語根・反復語・命名句・対応構文がParasha全体を通してどのような意味の連鎖と反転を作るかを本文内部から追跡し、辞書羅列・語呂合わせ・別Lensの結論を持ち込まないLensである。

## 2. Parasha-Scale Lexical Map

```text
Divine seeing / naming / ordering
        ↓
Human formation / naming / guarding
        ↓
Human seeing / taking / disordered rule
        ↓
Ground / blood / denied guarding
        ↓
Image-bearing lineage / repeated death
        ↓
Formed inclination of the heart / grief
        ↓
Noah named toward comfort; Noah finds favor
```

The map is a lexical trajectory, not a substitute for Peshat chronology.

## 3. Textual Anchors

### 3.1 A1 — ראה with טוב / רע: Who sees, and what is judged good?

```yaml
anchor:
  hebrew: ["וַיַּרְא", "וַתֵּרֶא", "טוֹב", "רַע"]
  references:
    - "Genesis 1:4, 1:10, 1:12, 1:18, 1:21, 1:25, 1:31"
    - "Genesis 3:6"
    - "Genesis 6:2, 6:5"
  exact_recurrence:
    - "Creation repeatedly receives the divine evaluation כִּי־טוֹב, culminating in טוֹב מְאֹד."
    - "The woman sees that the tree is good: וַתֵּרֶא הָאִשָּׁה כִּי טוֹב הָעֵץ."
    - "The sons of God see that the daughters of humanity are good/fair: וַיִּרְאוּ ... כִּי טֹבֹת הֵנָּה."
    - "YHWH then sees that human evil is great: וַיַּרְא יְהוָה כִּי רַבָּה רָעַת הָאָדָם."
  parasha_function: "The repeated seeing-and-evaluating vocabulary moves from divine discernment of created good, through creaturely sight that selects what appears good, to divine sight of pervasive human evil."
  boundary: "The lexical pattern does not by itself prove that every human act of seeing is evil, nor does it erase the local Peshat of each scene."
```

This is the strongest full-Parasha Hebrew Word trajectory in the unit: the issue is not merely the objects seen, but the shifting subject who sees and evaluates.

### 3.2 A2 — בדל / קרא / שם: Separation and naming as ordered identity

```yaml
anchor:
  hebrew: ["וַיַּבְדֵּל", "וַיִּקְרָא", "שֵׁם"]
  references:
    - "Genesis 1:4–10"
    - "Genesis 2:19–23"
    - "Genesis 3:20"
    - "Genesis 4:17, 4:25–26"
    - "Genesis 6:4"
  observation:
    - "God separates domains and calls them by name."
    - "The human calls the living creatures by name and recognizes אִשָּׁה in relation to אִישׁ."
    - "The woman is named חַוָּה in relation to חָי, life."
    - "Cain calls a city by his son's name; later the Nephilim are אַנְשֵׁי הַשֵּׁם, men of name/renown."
  parasha_function: "Naming begins inside divine ordering, is entrusted to the human, and later also becomes a vehicle of genealogy, memorialization, city, and reputation."
  boundary: "This unit records the textual movement; it does not assign one moral value to every act of naming or claim that אִישׁ and אִשָּׁה are established by modern historical etymology solely from Genesis 2:23."
```

### 3.3 A3 — אדם / אדמה / עפר / דם: Human, ground, dust, and blood

```yaml
anchor:
  hebrew: ["אָדָם", "אֲדָמָה", "עָפָר", "דָּם / דְּמֵי"]
  references:
    - "Genesis 2:5–7, 2:15"
    - "Genesis 3:17–19"
    - "Genesis 4:2–12"
    - "Genesis 5:1–5, 5:29"
    - "Genesis 6:1, 6:7"
  exact_connections:
    - "The human, הָאָדָם, is formed from dust from the ground, עָפָר מִן־הָאֲדָמָה."
    - "The human is placed to serve the garden; after rupture the ground is cursed and the human returns to dust."
    - "Cain serves the ground, but Abel's bloods, דְּמֵי אָחִיךָ, cry from that ground."
    - "Humanity multiplies עַל־פְּנֵי הָאֲדָמָה and is threatened with erasure מֵעַל פְּנֵי הָאֲדָמָה."
  parasha_function: "The ground is not background scenery: it is the human's material origin, vocational field, cursed field of toil, witness receiving blood, and the surface from which humanity may be erased."
  boundary: "The consonantal proximity of אָדָם / אֲדָמָה / דָּם is a literary observation in this text; this unit does not claim that all three share one strict historical etymology."
```

### 3.4 A4 — צלם / דמות / תולדות: Image language entering genealogy

```yaml
anchor:
  hebrew: ["צֶלֶם", "דְּמוּת", "תּוֹלְדוֹת"]
  references:
    - "Genesis 1:26–27"
    - "Genesis 2:4"
    - "Genesis 5:1–3"
  exact_connections:
    - "Humanity is created in divine image and likeness."
    - "Genesis 2:4 names the תוֹלְדוֹת of heaven and earth."
    - "Genesis 5:1 opens סֵפֶר תּוֹלְדֹת אָדָם, repeats divine likeness, then says Adam begets a son בִּדְמוּתוֹ כְּצַלְמוֹ."
  parasha_function: "The same image/likeness vocabulary crosses from divine creation into human generation, while תולדות frames both cosmic and human continuity."
  boundary: "The text establishes lexical continuity; this Lens does not resolve every theological question about the transmission or impairment of the divine image."
```

### 3.5 A5 — עבד / שמר / אח: Vocation and denied guardianship

```yaml
anchor:
  hebrew: ["לְעָבְדָהּ", "לְשָׁמְרָהּ", "עֹבֵד אֲדָמָה", "הֲשֹׁמֵר אָחִי אָנֹכִי"]
  references:
    - "Genesis 2:15"
    - "Genesis 4:2, 4:9–12"
  exact_connections:
    - "The human is placed in the garden to serve it and guard it."
    - "Cain is a servant/tiller of the ground."
    - "When asked for his brother, Cain answers with the guarding root: Am I my brother's keeper?"
  parasha_function: "The root שמר moves from entrusted garden-guarding to denied brother-guarding, while עבד remains tied to the ground whose strength Cain finally loses."
  boundary: "The recurrence supports a literary connection; it does not prove that Genesis 2:15 directly commands Cain's specific later responsibility."
```

### 3.6 A6 — תשוקה / משל: One paired construction, two crises

```yaml
anchor:
  hebrew: ["תְּשׁוּקָה", "מָשַׁל"]
  references:
    - "Genesis 3:16"
    - "Genesis 4:7"
  exact_parallel:
    - "וְאֶל־אִישֵׁךְ תְּשׁוּקָתֵךְ וְהוּא יִמְשָׁל־בָּךְ"
    - "וְאֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה תִּמְשָׁל־בּוֹ"
  parasha_function: "The rare desire/rule pair links the woman-man judgment scene with the warning to Cain about sin crouching at the door; the second occurrence makes the first impossible to treat as isolated vocabulary."
  boundary: "Because תְּשׁוּקָה is rare and debated, this unit preserves the exact parallel without pretending that one English gloss settles every relational or grammatical question."
```

### 3.7 A7 — יצר: The One who forms and the formation of thought

```yaml
anchor:
  hebrew: ["וַיִּיצֶר", "יֵצֶר מַחְשְׁבֹת לִבּוֹ"]
  references:
    - "Genesis 2:7, 2:19"
    - "Genesis 6:5"
  exact_connections:
    - "YHWH God forms, וַיִּיצֶר, the human and the animals from the ground."
    - "Genesis 6:5 speaks of every יֵצֶר, formation/inclination, of the thoughts of the human heart."
  parasha_function: "The shared root moves from divine forming of embodied creatures to the formed inclination of human thought; by 6:5 the problem is described at the level of the heart's continually formed purposes."
  boundary: "Verb and noun share the root יצר but are not interchangeable senses; the literary juxtaposition must not be inflated into a complete doctrine of human psychology."
```

### 3.8 A8 — עצב / נחם / נוח: Pain, hoped-for comfort, and divine grief

```yaml
anchor:
  hebrew: ["עִצָּבוֹן / עֶצֶב", "נֹחַ", "יְנַחֲמֵנוּ", "וַיִּנָּחֶם", "וַיִּתְעַצֵּב"]
  references:
    - "Genesis 3:16–17"
    - "Genesis 5:29"
    - "Genesis 6:6"
  exact_connections:
    - "Pain/toil vocabulary עֶצֶב / עִצָּבוֹן marks the judgments of Genesis 3."
    - "Lamech names Noah with the explanation זֶה יְנַחֲמֵנוּ ... וּמֵעִצְּבוֹן יָדֵינוּ."
    - "Genesis 6:6 uses both roots around YHWH: וַיִּנָּחֶם ... וַיִּתְעַצֵּב אֶל־לִבּוֹ."
  parasha_function: "The hoped-for human comfort from cursed-ground toil is immediately set beside divine regret/grief over humanity, creating a lexical hinge at the end of the Parasha."
  boundary: "Genesis itself presents the Noah/ינחמנו naming explanation, but this unit does not claim that נֹחַ and נחם are identical roots in strict historical linguistics or reduce וַיִּנָּחֶם to one English emotion."
```

## 4. Parasha-Scale Synthesis

Bereshit's Hebrew vocabulary creates a coherent movement without requiring an imported thematic grid:

1. God separates, names, sees, and evaluates creation as good.
2. The human formed from the ground receives naming and guarding activity.
3. Creaturely seeing appropriates what appears good, while desire/rule language enters fractured relations.
4. Guarding is denied at the brother's blood, and the ground becomes witness, curse-bearing field, and lost strength.
5. Image/likeness persists into תולדות, yet the genealogy repeatedly closes with וַיָּמֹת.
6. The root יצר turns from divine forming to the formed inclination of human thought; divine seeing now encounters pervasive רע.
7. Lamech's hoped-for comfort in Noah is placed beside YHWH's grief, while Genesis 6:8 ends with a deliberately different final verb: נֹחַ מָצָא חֵן—not an etymological trick, but the narrative statement that Noah found favor.

The Hebrew Word Lens therefore reveals not a list of important words but a network: ordered distinction and naming become human vocation; human sight and desire disorder reception; ground, guarding, blood, lineage, heart, grief, and favor carry the Parasha from creation to the threshold of the Flood narrative.

## 5. Allowed Absence

```yaml
allowed_absence:
  messiah_conclusion: "Not filled; Messiah Lens was not the selected Lens."
  israel_application: "Not filled; Israel is not yet a named actor in Genesis 1:1–6:8."
  covenant_formula: "Not filled; the noun בְּרִית does not occur in the declared substrate and Genesis 9 is outside this unit."
  systematic_theology: "Not filled; lexical observations are not expanded into a total doctrine."
  exhaustive_lexicon: "Not attempted; anchors were selected for full-Parasha function, not quota completion."
  peshat_comparison: "Not performed; the claimed Peshat v0.3 artifact is absent from the current repository."
```

## 6. Evidence and Uncertainty Ledger

### 6.1 High-confidence textual evidence

- Exact desire/rule parallel: Genesis 3:16 and 4:7.
- Exact image/likeness recurrence: Genesis 1:26–27 and 5:1–3.
- Exact יצר root recurrence: Genesis 2:7, 2:19 and 6:5.
- Exact שמר root recurrence: Genesis 2:15 and 4:9.
- Exact ראה + טוב/רע trajectory across Genesis 1, 3, and 6.
- Explicit textual naming explanations for חַוָּה, שֵׁת, and נֹחַ.

### 6.2 Literary inference requiring Human review

- The movement from divine naming to delegated and later memorial naming.
- The Parasha-scale relation among אדם, אדמה, עפר, and דמי.
- The hinge between Lamech's יְנַחֲמֵנוּ and YHWH's וַיִּנָּחֶם.
- The movement from entrusted garden-guarding to Cain's denied brother-guarding.

### 6.3 Claims deliberately rejected

- `נֹחַ` and `חֵן` are not treated as an etymological reversal proof.
- אדם / אדמה / דם are not asserted to share one complete historical etymology.
- Every occurrence of טוב is not flattened into one moral formula.
- Hebrew similarity is not treated as authorization for Messiah, Covenant, or Israel conclusions under this Lens.

## 7. Source Basis

Primary Hebrew text:

- [Mechon-Mamre — Genesis 1](https://mechon-mamre.org/p/pt/pt0101.htm)
- [Mechon-Mamre — Genesis 2](https://mechon-mamre.org/p/pt/pt0102.htm)
- [Mechon-Mamre — Genesis 3](https://mechon-mamre.org/p/pt/pt0103.htm)
- [Mechon-Mamre — Genesis 4](https://mechon-mamre.org/p/pt/pt0104.htm)
- [Mechon-Mamre — Genesis 5](https://mechon-mamre.org/p/pt/pt0105.htm)
- [Mechon-Mamre — Genesis 6](https://mechon-mamre.org/p/pt/pt0106.htm)
- [Sefaria — Genesis 1:1–6:8](https://www.sefaria.org/Genesis.1.1-6.8)

Method boundary: this candidate primarily uses recurrence and juxtaposition inside the Masoretic Hebrew text. It does not present lexicon definitions as settled merely because an English gloss exists.

## 8. Capability Revalidation Gate

```yaml
capability_revalidation:
  full_parasha_substrate_used: true
  chapter_coverage: [1, 2, 3, 4, 5, 6]
  selected_lens_remained_distinct: true
  allowed_absence_respected: true
  unsupported_wordplay_rejected: true
  evidence_locations_named: true
  artifact_boundary_respected: true
  predecessor_peshat_was_not_invented: true
  human_hebrew_review_required: true
  result: "PROVISIONAL_PASS"

first_bottleneck:
  name: "Dangling Peshat Baseline"
  meaning: "The workflow reports a completed Peshat v0.3 in Ark05:04, but the referenced artifact contains no related content."

unexpected_success:
  name: "Parasha-Scale Lexical Trajectory"
  meaning: "The full substrate exposes linked lexical movements—especially ראה+טוב/רע, תשוקה/משל, שמר, יצר, and עצב/נחם—that a Genesis 1:1 pilot could not reveal."
```

## 9. Next Gate

```yaml
next_gate:
  action: "Human reviews the eight anchors and accepts, corrects, or rejects the PROVISIONAL_PASS."
  do_not_execute_yet:
    - "Do not generate the remaining eight Lens units."
    - "Do not claim the 540-unit Matrix is validated."
    - "Do not reconstruct the missing Peshat artifact from memory."
    - "Do not promote this candidate to final Human Seal automatically."
```

<!-- ARK_WTP_BERESHIT_HEBREW_WORD_V003_EOF -->
