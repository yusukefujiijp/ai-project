---
type: "Ark-WTP Seed Unit Template"
template_version: "v001-candidate"
canonical_path: "projects/ark-wtp/seed-units/_template.md"
status: "candidate / human-review-required / AI-reusable"
project: "Ark-WTP / Weekly Torah Portion / Lens-as-Dimensions"
root: "主イェシュア・ハマシア"
root_guard: "The Seed Unit is a Keli; it must not replace Torah, 主イェシュア・ハマシア, Human judgment, prayer, or lived obedience."
---

# Ark-WTP Seed Unit Template

## 0. Unit Contract

```yaml
unit_contract:
  declared_unit: "one full Parasha × one Lens"
  required_substrate: "full declared Parasha range"
  style: ["compact", "anchor-based", "evidence-first"]
  forbidden: ["verse-by-verse paraphrase", "dictionary list", "forced thematic filling", "unsupported wordplay"]
  allowed_absence: true
  human_final_seal_required: true
```

## 1. Unit Identity

```yaml
unit_identity:
  unit_id: "<stable-id>"
  parasha: "<name>"
  substrate: "<Torah range>"
  lens: "<one active Lens>"
  version: "<version>"
  status: "candidate / human-review-required"
  source_basis: "<primary text and supporting references>"
```

## 2. Lens Focus Line

State in one sentence what this Lens is permitted to observe in this Parasha and what it must not import.

## 3. Textual Anchors

For each selected anchor record:

```yaml
anchor:
  id: "A<n>"
  hebrew: "<word / phrase / repeated construction>"
  references: ["<reference>"]
  observation: "<what the text itself shows>"
  parasha_function: "<how the anchor changes or connects across the full substrate>"
  boundary: "<what is not established>"
```

Use only anchors that materially open the selected Lens. Do not fill a quota.

## 4. Parasha-Scale Synthesis

Connect the selected anchors across the full substrate without turning the Seed Unit into a plot summary or another Lens.

## 5. Allowed Absence

List expected themes or fields intentionally left empty because the selected Lens or textual evidence does not support them.

## 6. Evidence and Uncertainty Ledger

Separate:

- exact textual recurrence;
- morphology or syntax requiring review;
- literary inference;
- claims deliberately rejected.

## 7. Capability Gate

```yaml
capability_gate:
  full_parasha_substrate_used: false
  selected_lens_remained_distinct: false
  allowed_absence_respected: false
  unsupported_wordplay_rejected: false
  evidence_locations_named: false
  artifact_boundary_respected: false
  human_review_required: true
  result: "PASS / PROVISIONAL_PASS / FAIL"
```

## 8. Next Gate

Name one next action only. Do not scale from one successful Seed Unit to the full Matrix automatically.

<!-- ARK_WTP_SEED_UNIT_TEMPLATE_EOF_v001-candidate -->
