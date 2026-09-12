# Living Update Reference

Use this reference only when observed Reality can correct a prediction, relation hypothesis, or next path.

## 1. Minimum Living State

```yaml
living_graph_state:
  current_reality: ""
  active_nodes: []
  active_relations: []
  selected_path: ""
  predicted_result: ""
  actual_action: ""
  actual_result: ""
  prediction_error: ""
  human_correction: ""
  relation_updates: []
  newly_active: []
  newly_dormant: []
  pruned_or_deferred: []
  next_priority_path: ""
  confidence_change: "increase | hold | decrease"
  human_review: "required"
```

Do not require every field. Capture the minimum state needed to show what changed and why.

## 2. Update Rules

- Prediction approximately matches Actual: conditionally strengthen the relevant relation, not the whole theory.
- Prediction differs from Actual: weaken the relation, add a condition, split the path, or return it to unknown.
- Evidence is insufficient: hold confidence and keep the relation dormant or provisional.
- A guard was violated: do not promote the path even if the outcome appears favorable.
- Only one sample exists: do not universalize.
- Human materially corrects the account: reconstruct from the correction rather than defending polished prose.

Use ordinal updates such as `increase`, `hold`, or `decrease` unless real measurement justifies numbers.

## 3. No Fake Living

Do not call a graph living merely because:

- a control is interactive;
- an animation runs;
- a displayed weight changes;
- a hypothetical result was supplied by the AI;
- no Actual Reality has been observed.

Livingness requires a correctable state change grounded in Reality or Human correction.

## 4. Double-Spiral Operation

Keep one surface for the Human and one learning loop in the AI background:

```text
Spiral A: purpose -> candidate -> guard -> one move -> Actual Reality
Spiral B: relation hypothesis -> prediction -> Actual Reality -> error -> update -> next prose
```

The spirals cross at Actual Reality. Do not make the Human manage both surfaces.

## 5. Bounded Field Test

For one low-risk, reversible, short case, capture:

```yaml
field_test:
  current_reality: ""
  human_foreground_handle: ""
  initial_candidates: []
  relation_hypothesis: ""
  bridge_or_cut_edge: ""
  predicted_result: ""
  guard_result: "ACT | PAUSE | REJECT"
  one_move: ""
  actual_result: ""
  prediction_error: ""
  graph_native_fruit: ""
  relation_update: ""
  next_priority_path: ""
  human_correction: ""
```

Stop after one case. Do not create an artifact, fix numeric weights, or expand theory before the Actual Result. Return the result for Human review.

## 6. Prose Return for a Living Update

State:

1. The prior prediction or active path.
2. The actual observation.
3. The material difference.
4. Which relation changed.
5. What remains unknown.
6. The revised next path.
7. What future observation would reverse or refine this update.
