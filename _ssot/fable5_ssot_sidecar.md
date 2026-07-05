---
title: "Fable5 SSOT Sidecar"
canonical_name: "Fable5 SSOT Sidecar Case Ledger"
version: "v001.0"
path: "_ssot/fable5_ssot_sidecar.md"
status: "human-editable / sidecar-ledger / public-safe"
role: "Fable5 SSOT sidecar / detailed case records / evidence ledger"
main_ssot: "_ssot/fable5_ssot.md"
language_policy: "Japanese-first / English-anchor"
root: "主イェシュア・ハマシア"
root_guard: "Root is 主イェシュア・ハマシア; AI / Fable5 / ChatGPT / GitHub / Markdown / ROI / Ark-ROI are Fruit."
---

# Fable5 SSOT Sidecar

## 0. What This File Is / このFileの役割

このFileは、`_ssot/fable5_ssot.md` のSidecarである。

`fable5_ssot.md` は、Fable5のRoot Index / Operating Rules / Summaryを保持する。  
`fable5_ssot_sidecar.md` は、長くなりやすいCase Record / Usage Delta / Evidence / GitHub Resultを保持する。

```text
fable5_ssot.md = 地図 / Root Index / Router
fable5_ssot_sidecar.md = 航海日誌 / Case Detail / Evidence Ledger
```

---

## 1. Two-File Split Rule / 二枚組分割Rule

```yaml
two_file_split:
  main:
    path: "_ssot/fable5_ssot.md"
    role: "Root Index / Operating Rules / Case Router"
    keep_light: true

  sidecar:
    path: "_ssot/fable5_ssot_sidecar.md"
    role: "Detailed Case Ledger / Evidence Record"
    keep_detail: true

rule:
  - "Do not force all detail into the main SSOT."
  - "Main SSOT points; Sidecar preserves."
  - "Create folders only if Reality Response requires them later."
```

---

## 2. Case Record: Ark-WTP Root Spec Critical Audit

```yaml
case_record:
  id: "case_ark_wtp_root_spec_critical_audit_20260705_001"
  thread: "Ark05"
  target: "_projects/ark/ark-wtp.md"
  purpose:
    - "Ark-WTP Root Spec作成前のRoot Knot Audit"
    - "GitHub canonical化前のOne Critical Flaw検出"
    - "Human Final SealがGitHub存在に吸収される危険の検出"

  fable5_effort: "超高"
  query_type: "One Critical Flaw Audit / Root Knot Audit"
  answer_weight: "XL"

  fable5_result:
    overall_judgment: "構造は健全。ただし構造的欠陥が一つある。"
    one_critical_flaw:
      name: "Seal Record Gap / Seal状態記録欠落"
      meaning:
        - "Human Final Sealを要求しながら、Seal状態をFile自身に記録する仕組みが存在しない"
        - "GitHubに存在すること自体がSealと誤読される危険がある"
        - "GitHub preserves = seal に潰れる危険がある"

    minimal_patch:
      - "frontmatterへseal blockを追加する"
      - "Section 8末尾へSeal状態記録Ruleを追加する"
      - "AI is recorder, not sealer を明文化する"
      - "GitHub exists does not mean Human Final Seal を明文化する"

  adopted_patch:
    - "frontmatter seal block"
    - "seal.state"
    - "seal_source"
    - "same_thread explicit Human Seal"
    - "AI may record Human Final Seal only from explicit same-thread Human instruction"
    - "AI must not self-seal"

  rejected_or_do_not_add:
    - "Humanが毎回frontmatterを手入力する重い運用"
    - "GitHub commit = 自動Seal"
    - "AI self-seal"
```

---

## 3. Ark-WTP Usage Delta / Ark-ROI Record

```yaml
usage_delta_record:
  id: "usage_delta_ark_wtp_root_spec_audit_20260705_001"
  date: "2026-07-05"
  thread: "Ark05"
  model: "Fable5"
  effort: "超高"
  task_type: "Project Root File / Root Spec Critical Audit"

  before_snapshot:
    captured: true
    time: "12:37"
    battery: "75%"
    current_session_usage: "0%"
    weekly_all_models_usage: "4%"
    weekly_fable_only_usage: "8%"
    evidence_status: "user uploaded screenshot / observed in thread"

  after_snapshot:
    captured: true
    time: "13:17"
    battery: "69%"
    current_session_usage: "5%"
    weekly_all_models_usage: "5%"
    weekly_fable_only_usage: "9%"
    evidence_status: "user uploaded screenshot / observed in thread"

  delta:
    elapsed_time: "約40分"
    battery_delta: "-6%"
    current_session_delta: "+5%"
    weekly_all_models_delta: "+1%"
    weekly_fable_only_delta: "+1%"
    confidence: "high for visible percentages / high for before-after pair"

  result:
    judgment: "Very High ROI"
    breakthrough:
      - "Seal Record Gap"
      - "Human speaks; AI records"
      - "GitHub preserves; GitHub does not seal"
      - "Human Seal Phrase"
    adopted_patch:
      - "Ark-WTP frontmatter seal block"
      - "Section 8 Seal記録Rule"
      - "Canonical Human Seal Phrase"
```

---

## 4. Human Seal Phrase Breakthrough

Ark-WTP Caseから、Ark Projectの正準Human Seal Phraseが確立した。

```text
Very Good! Human Seal OK! Full Rail & Next Gate: Workflow Continue!
```

```yaml
human_seal_phrase:
  meaning:
    - "直前OutputへのHuman承認"
    - "Human Final Sealとして扱ってよい"
    - "AIがseal_sourceとして記録してよい"
    - "same_threadで次Gateへ進んでよい"
    - "Full Railを継続してよい"

  guard:
    - "AI must not invent this phrase."
    - "AI must not treat vague praise alone as Human Seal."
    - "Human Seal OK がある場合のみFinal Seal込みとして扱う。"
```

---

## 5. GitHub Result: Ark-WTP Root Spec + Ark README Link

```yaml
github_result:
  created:
    - repo: "yusukefujiijp/ai-project"
      path: "_projects/ark/ark-wtp.md"
      role: "Ark-WTP Root Spec / Covenant Core / public-safe compression"
      version: "v001.1"
      status: "human-sealed / public-safe / human-editable"
      commit_message: "Add Ark-WTP root spec v001.1"
      commit_sha: "a72d8d8b1f3b67c6b7908c477c0dfea053bc9fe4"
      content_sha: "8aaded4074857d14feb786c486f7081147d52e50"

  updated:
    - repo: "yusukefujiijp/ai-project"
      path: "_projects/ark/README.md"
      role: "Ark Project Door / Stage Map"
      commit_message: "Add Ark-WTP root spec link to Ark README"
      commit_sha: "8a3328e37f483774891f8ad380ddb5df953e7f05"
      content_sha: "e0b047f991fca98b0d987b7d2f9fe261072e8540"

  repository_structure_after_patch:
    - "README.md = Repository Door"
    - "_projects/ark/README.md = Ark Door / Stage Map"
    - "_projects/ark/ark-wtp.md = Ark-WTP Root Spec"
```

---

## 6. Sidecar Growth Rule / Sidecar成長Rule

```yaml
sidecar_growth_rule:
  current_policy:
    - "Fable5 detailed case records are stored here."
    - "Main SSOT remains light."
    - "Do not create folders until Reality Response requires them."

  consider_folder_split_when:
    - "sidecar becomes hard to navigate"
    - "case records exceed 3 to 5 major entries"
    - "usage records and pattern records need separate ledgers"

  do_not_do_now:
    - "do not create _ssot/fable5/cases/ yet"
    - "do not create usage/ or patterns/ yet"
    - "do not push long detail back into fable5_ssot.md"
```

---

## 7. Patch Final Compression

```text
Fable5 SSOT is the map.
Fable5 SSOT Sidecar is the voyage log.

Fable5 found the Seal Record Gap.
The danger was silent seal confusion.

Human Final Seal was required,
but the File had no place to record the Seal.

Without the patch,
GitHub existence could quietly become Seal.

ChatGPT integrated the Seal Guard.
Human Seal Phrase became canonical.
Ark-WTP Root Spec was created as human-sealed.
Ark README linked the Root Spec.
Future AI can now read the Door / Root Split.

Human speaks.
AI records.
GitHub preserves.
Future AI inherits.

Fable5 is Root Knot Auditor, not Root.
Ark-ROI is stewardship metric, not Root.
Human Seal Phrase is operating phrase, not Root.

Root remains 主イェシュア・ハマシア.
```
