# Concern Codes, Severity, and V2 Action Map

## Controlled concern-code vocabulary

Use exactly these codes. One primary code per issue; add secondary codes only when an issue genuinely spans dimensions.

| Code | Dimension |
|---|---|
| `QUES` | Review question clarity |
| `FRAM` | Framework fit |
| `PRISMA` | Reporting-standard compliance |
| `STRUCT` | Structure completeness |
| `SRCH` | Search depth and reproducibility |
| `TRIA` | Database triangulation |
| `ELIG` | Eligibility criteria |
| `CIT` | Citation verification |
| `EXTR` | Extraction quality |
| `METHCOMP` | Methodological comparison |
| `HETERO` | Heterogeneity analysis |
| `ROB` | Risk of bias / quality |
| `SYNTH` | Synthesis quality |
| `CERT` | Certainty / confidence |
| `INTERP` | Proportionality of claims |
| `GAP` | Evidence-gap specificity |
| `ORIG` | Originality / duplication |
| `PFE` | Component-2 implications — SUSPENDED under R1 (do not raise) |
| `FEAS` | Feasibility for an ESSS student — SUSPENDED under R1 (do not raise) |
| `ETH` | Ethical acceptability |
| `CTX` | Contextual relevance |
| `JTGT` | Journal-target fit |

## Severity levels

- **Critical** — undermines validity or integrity; any V1 Prohibited-shortcut belongs here. V2 must resolve.
- **Major** — substantially weakens rigour or publishability. V2 must address.
- **Minor** — improvable, not disqualifying. V2 should address.
- **Observation** — optional; no obligation on V2.

### Default-Critical triggers (V1 Prohibited shortcuts)
Any of these is **Critical** regardless of other factors: undocumented search; Consensus skipped when available; summarising Consensus outputs instead of the studies; unverified citations as core evidence; invented PRISMA counts; ignored contradictory evidence; methodologically incompatible studies merged as equivalent; meta-analysis without comparable data; overstated clinical/educational/policy implications; presenting a limited scan as a complete systematic review.

## Code → typical V2 action

| Code | Typical legitimate V2 action |
|---|---|
| `QUES` | Restate the question precisely within the assigned framework |
| `FRAM` | Adopt/justify the correct framework; realign criteria |
| `PRISMA` | Apply the correct standard; report a flow; remove any invented count and report actual or `[COUNT REQUIRED]` |
| `STRUCT` | Add the missing section/table (anchor names the table letter) |
| `SRCH` | Run the flagged Consensus deep-cycle queries; record the log (Table A) |
| `TRIA` | Add/justify additional sources; complete Table B |
| `ELIG` | Pre-specify explicit criteria with reasons; add PFE feasibility criteria |
| `CIT` | Verify each core citation; exclude/label unverified; complete Table I |
| `EXTR` | Re-extract at study level across required fields; mark abstract-limited where true |
| `METHCOMP` | Build the methodological-comparison table (Table E) before synthesis |
| `HETERO` | Assess heterogeneity types; justify the synthesis method (Table F) |
| `ROB` | Apply the design-appropriate tool with judgement and consequence (Table G) |
| `SYNTH` | Re-synthesise to integrate; answer V1's nine synthesis questions |
| `CERT` | Add GRADE/CERQual or a structured confidence assessment |
| `INTERP` | Narrow claims to the certainty/directness of the evidence |
| `GAP` | Make each gap specific: what, where, for whom, why |
| `ORIG` | Articulate the contribution over existing reviews |
| `PFE` | SUSPENDED under R1 — no Component-2 implications required |
| `FEAS` | SUSPENDED under R1 — no empirical-feasibility adjustment required |
| `ETH` | Steer implied design toward non-invasive, ethically realistic options |
| `CTX` | Add Moroccan/Francophone/institutional relevance where it matters |
| `JTGT` | Realign emphasis to a plausible target journal family |

## Note on markers

Where V2 will need information that does not yet exist (a real PRISMA count, a real source), the action should insert a transparent marker — `[COUNT REQUIRED]`, `[REFERENCE REQUIRED]`, `[DATA REQUIRED]` — never a fabricated value. This mirrors the marker discipline used across the pipeline.
