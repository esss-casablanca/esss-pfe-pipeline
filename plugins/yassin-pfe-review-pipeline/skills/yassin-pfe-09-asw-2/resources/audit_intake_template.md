# Skill 1 Audit Intake Template

Use this file when the user provides output from `yassin-ai-authorship-risk-audit`.

## Required fields from Skill 1

Extract or reconstruct the following:

| Skill 1 field | How Skill 2 uses it |
|---|---|
| Document language | Choose French/English revision style |
| Document type | Select section logic and reporting expectations |
| Section name/type | Interpret formulaic vs authorial-risk sections |
| Paragraph ID | Preserve traceability in revision log |
| Sentence ID | Revise only when sentence-level comments are meaningful |
| Risk score | Select revision priority, not detector optimization |
| Concern codes | Determine legitimate revision action |
| False-positive caution | Avoid over-revising formulaic methods/ethics/statistics |
| Recommended legitimate revision | Use as starting point |
| External detector mode | Distinguish internal audit from real uploaded reports |

## Concern-code to revision-action map

| Skill 1 concern | Legitimate Skill 2 response |
|---|---|
| Generic paragraph | Add study-specific population, setting, method, variable, or result if supplied; otherwise mark missing detail |
| Unsupported claim | Add `[REFERENCE REQUIRED]`, `[DATA REQUIRED]`, or remove overclaim |
| Formulaic transition | Replace with logical disciplinary transition tied to section content |
| Weak method detail | Insert `[METHOD DETAIL REQUIRED]` and clarify what is missing |
| Weak literature synthesis | Compare studies, methods, populations, findings, and gaps using supplied references |
| Discussion not linked to results | Tie interpretation to actual findings or mark `[DATA REQUIRED]` |
| Overgeneralized conclusion | Narrow conclusion to study scope |
| Translation-like phrasing | Correct idiomatic academic French/English without changing meaning |
| Possible false positive | Keep conventional wording if scientifically appropriate |

## Output traceability

When Skill 1 IDs are available, the revision log must include:

- `source_paragraph_id`;
- `source_sentence_id` if applicable;
- `skill1_risk_score`;
- `skill1_concern_codes`;
- `revision_action`;
- `meaning_drift_risk`;
- `author_verification_required`.

## Rule

Do not use Skill 1 scores as detector-clearance targets. Use them only to prioritize scholarly review.
