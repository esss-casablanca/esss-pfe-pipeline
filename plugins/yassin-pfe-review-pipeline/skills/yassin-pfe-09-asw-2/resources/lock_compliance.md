# Lock Compliance

This audit operates on the **locked V3**. `content_lock.json` enumerates what is frozen and what is
editable. Every recommendation this skill makes — and every action it hands to `Yassin_PFE_07_ASW_1` —
must respect that boundary.

## May be recommended (editable scope)
- Surface wording and word choice.
- Sentence structure and length variation.
- Clarity, cohesion, and flow.
- Paragraph organisation.
- Register and academic style.
- Strengthening *how* an existing claim is expressed and connected to the student's own reasoning.

## Must NOT be recommended (frozen scope)
- Adding, removing, or altering any scientific claim or conclusion.
- Changing any number, statistic, effect estimate, confidence interval, or PRISMA count.
- Adding, removing, or changing any citation or reference.
- Altering table data (A–I), risk-of-bias judgments, certainty ratings, or synthesis findings.

## Practical rule
When a paragraph reads as weak authorship *because* a claim is generic or unsupported, the fix is
**not** to change the claim — the science is locked. The fix is to coach the student to express the
*existing* locked claim with their own specificity: linking it to their actual extracted findings,
their methodological reasoning, or their local context already present in the review. If a paragraph
genuinely cannot be strengthened without changing locked science, say so explicitly and flag it as
an author-verification item rather than recommending a frozen-scope change.

---

## Additional duty for the reviser (Yassin_PFE_07_ASW_1 / Yassin_PFE_09_ASW_2)

The reviser does not merely *avoid recommending* frozen changes — it must **not make them** and
must **attest** that it did not. After producing the revised version:

1. Confirm the reference list is unchanged: same count, same entries, same identifiers as
   `content_lock.json`'s `frozen_reference_list`.
2. Confirm every frozen claim still appears with the same meaning and the same numbers.
3. Confirm no statistic, PRISMA count, or table value changed.
4. Record the result in the **lock-compliance attestation** (`lock_attestation_schema.json`).

If any frozen element would have to change to fix a writing problem, **do not change it**. Leave the
text as locked, mark the spot, and explain to the student that this can only be revisited by
re-opening the science (a return to the review-version steps), not in the authorship loop.
