# Graph Operations Reference

Use this reference to construct the smallest sufficient relational model and extract relation-native fruit. Keep the model internal unless a compact structure improves the answer.

## 1. Reality and Evidence Packet

Capture only relevant fields:

```yaml
reality_packet:
  current_reality: ""
  human_center: ""
  current_question: ""
  foreground_handle: ""
  known_constraints: []
  available_resources: []
  candidate_actions: []
  actual_trace: []
  confirmed: []
  inferred: []
  unknown: []
  prohibited_claims: []
```

Useful evidence classes:

- `SOURCE_FACT`: directly read from the current source.
- `H_OBS`: Human direct observation.
- `H_HYP`: Human hypothesis.
- `H_COR`: Human material correction.
- `AI_SYN`: AI synthesis candidate.
- `AI_DES`: AI design candidate.
- `TOOL_OBS`: tool or interface observation.
- `E1`: field evidence.
- `D1`: correctable design decision.

## 2. Minimal Nodes and Typed Relations

Prefer these node roles when useful:

```text
root | purpose | reality | signal | candidate | guard
action | observation | learning | attribution
```

Mark nodes `active`, `dormant`, `deferred`, or `pruned` only when status affects the decision.

Use the minimum relevant relation types:

| Relation | Meaning |
|---|---|
| `ROOTS` | establishes the meaning root |
| `ORIENTS` | provides direction |
| `MODIFIES` | narrows or changes another node's meaning |
| `ACTIVATES` | makes a node operationally relevant |
| `INHIBITS` | suppresses activation or execution |
| `DEPENDS_ON` | consumes another node's output |
| `BRIDGES` | makes two regions traversable |
| `GATES` | passes, pauses, or rejects a move |
| `EXECUTES` | carries a candidate into Reality |
| `OBSERVES` | captures an actual trace |
| `CORRECTS` | changes a relation hypothesis from evidence |
| `ATTRIBUTES` | assigns ownership or credit |

Do not invent relation types as decoration.

## 3. High-Leverage Operations

### 3.1 Bridge detection

Find the node or relation that connects purpose to action, candidate to Reality, or observation to learning.

### 3.2 Cut-edge detection

Find the one relation whose failure prevents upstream strengths from reaching fruit.

Example:

```text
Candidate generation works.
Guard evaluation works.
Candidate -> finite action is broken.

Fruit: The bottleneck is not idea quality; it is the execution edge.
```

### 3.3 Hub and dual-center detection

Check whether multiple semantically powerful centers are simultaneously occupying Human foreground attention. Distinguish importance from activation frequency.

### 3.4 Activation asymmetry

Ask whether the highest-value node should remain in the foreground continuously. A sacred, strategic, or final-attribution node may be most important while another operational handle should guide the current move.

### 3.5 Phase separation

Split roles across `before action`, `during action`, and `after action`. The same word, criterion, or node may legitimately change function across phases.

### 3.6 Feedback detection

Identify how the actual result changes candidate priority, guard interpretation, or future path selection.

### 3.7 False-dependency detection

Remove ordering edges when a branch does not consume another branch's output. Preserve independent coverage and merge only at a real reducer.

### 3.8 Folded-criteria detection

Keep useful criteria in the AI background without forcing the Human to track each criterion as a competing foreground keyword. Folding preserves a criterion while removing it from the attention surface.

## 4. Graph-Native Fruit Test

Ordinary node list:

```text
Candidate, guard, and action exist.
```

Relation-native fruit:

```text
Candidate generation succeeds, but the candidate-to-action relation is the cut edge that blocks the whole path.
```

Fail the gate when the supposed fruit is merely:

- more nodes;
- a Mermaid diagram;
- arbitrary numeric weights;
- animated edges;
- graph terminology without a changed judgment.

## 5. Branch Reduction and Nonlinear Friction

When branches fall from seven to one, six nodes disappear, but comparison and coordination relations may fall much faster. Seven undirected pairwise comparisons allow up to 21 pairs; directed candidates allow up to 42 directions before considering multi-hop paths.

Use this only as a structural explanation:

```text
Branch reduction
-> coordination-edge reduction
-> path-candidate reduction
-> context-switch reduction
-> attention-density increase
-> possible nonlinear fall in operational hesitation
```

Do not present this as a measured cognitive-cost formula. Label quadratic, exponential, singularity, or certainty language as hypothesis unless direct measurement supports it.

## 6. Membranes

Keep these boundaries distinct:

```text
Root / purpose
-------- frozen boundary
Human and AI interpretation candidates
-------- guard membrane
Finite action
-------- Reality membrane
Actual trace / prediction error
-------- Human review
Relation-update candidate
```

Never use a later update to erode an earlier frozen guard.
