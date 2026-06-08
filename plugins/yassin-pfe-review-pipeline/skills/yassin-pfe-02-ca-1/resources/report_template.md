# Appraisal Report Template (.docx)

Produce the report as a real `.docx` (see `/mnt/skills/public/docx/SKILL.md`). Use this exact section order.

---

# Initial Critical Appraisal — Review Article V1
### ESSS PFE Review Pipeline · Step 2 (Yassin_PFE_02_CA_1)

## 1. Executive summary
Three to six sentences: the global verdict, the count of issues by severity, and the single most important thing V2 must fix. No padding.

## 2. Scope and inputs
- Review type and assigned framework (from the note de cadrage, if available).
- Inputs available vs. missing (V1 text, note de cadrage, Consensus log Table A, citation matrix Table I, target journal).
- Dimensions whose appraisal is limited by missing inputs, stated plainly.
- Language of this report; note that a French companion version is available on request.

## 3. Global verdict
One of: *Sound, minor revision only* · *Revisable — Major revision required* · *Not yet a valid review — Critical revision required* · *Provisional — appraisal limited by missing inputs*. One paragraph justifying it.

## 4. Dimension-by-dimension assessment
For each dimension in `appraisal_dimensions.md`: state **met / partially met / not met**, with brief evidence. Keep dimensions that are fully met to one line each; spend the words on the defects.

## 5. Issue register (human-readable)
A table, one row per issue, sorted Critical → Observation:

| ID | Code | Severity | Location | Finding (with evidence) | Required action for V2 | New search? |
|----|------|----------|----------|--------------------------|------------------------|-------------|

This table is the readable mirror of the JSON register; the two must match exactly.

## 6. Prohibited-shortcut check
Explicitly confirm, for each of V1's prohibited shortcuts, whether it is present. Any present item must also appear as a Critical issue in Section 5.

## 7. Fresh-research plan for V2
List the issues flagged `needs_new_search`, grouped by the V1 deep-cycle query type(s) they require, so V2 has a ready search agenda.

## 8. Handoff contract to Yassin_PFE_03_Review_V2
State V2's obligations: close every Critical and Major issue, run the Section 7 searches, and return a closure map keyed to the issue IDs (this is what Yassin_PFE_04_CA_2 will verify).

## 9. Limitations of this appraisal
Be honest about what could not be judged and why (e.g. search depth could not be fully verified without Table A).

---

*This appraisal evaluates scientific rigour and reporting quality only. It does not assess AI-likeness or authorial style, which are handled separately later in the pipeline. It raises issues for revision; it does not rewrite the review.*
