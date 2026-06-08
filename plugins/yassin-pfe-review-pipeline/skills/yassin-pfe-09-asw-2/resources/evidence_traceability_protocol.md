# Evidence Traceability Protocol

## Claim categories

Classify every substantive claim as one of the following:

| Category | Examples | Required support |
|---|---|---|
| Empirical result | prevalence, percentage, mean, p-value, theme, quote | dataset/table/result supplied by user |
| Methodological claim | design, sampling, tool, procedure, analysis | protocol, methods text, author confirmation |
| Literature claim | prior findings, known association, guideline statement | reference supplied or `[REFERENCE REQUIRED]` |
| Contextual claim | Moroccan context, institutional setting, clinical practice context | source, institutional knowledge, or `[LOCAL CONTEXT REQUIRED]` |
| Interpretive claim | meaning of results, implications, explanation | actual findings + literature/context |
| Recommendation | practice, policy, education, research recommendation | findings + scope limitations |

## Source-status labels

Use these labels in the revision log:

- **Supplied-data supported** — directly supported by text/tables/data given by the user.
- **Supplied-reference supported** — supported by references or citations given by the user.
- **Method supplied** — supported by supplied methods/protocol details.
- **Context supplied** — supported by supplied institutional/local context.
- **General academic framing** — no specific factual claim added.
- **Requires verification** — author/supervisor must confirm.
- **Not supportable** — remove or mark; do not present as fact.

## Claim-tracking rules

For every full revision, identify:

- claims added;
- claims modified;
- claims removed;
- claims that became more specific;
- claims requiring author verification.

## Markers

Use:

- `[DATA REQUIRED]`
- `[REFERENCE REQUIRED]`
- `[METHOD DETAIL REQUIRED]`
- `[ETHICS DETAIL REQUIRED]`
- `[LOCAL CONTEXT REQUIRED]`
- `[AUTHOR TO VERIFY]`
- `[REPORTING ITEM REQUIRED]`

Do not remove markers unless the missing information is supplied.
