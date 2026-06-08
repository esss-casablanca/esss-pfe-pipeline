# Verification Protocol — checking V2 closures against the actual text

The closure map states what V2 *claims* to have done. This protocol checks each claim against the
**real V2 text**. Never accept a status on assertion alone.

## Per-issue verification steps

For each issue in the CA_1 register:

1. **Read the claim.** Note the closure map's `status`, `action_taken`, and `v2_location`.
2. **Go to the cited location** in V2 (`S0x` / `P00x` / `P00x-S0y` / table letter).
3. **Confirm the fix is actually there** and meets the closure criterion for that concern code
   (see `concern_codes_and_severity.md` and the V2 closure rubric). Ask: does the text at this
   location genuinely perform the required action, or only gesture at it?
4. **Check for fabrication.** If the "closure" rests on a value, count, or source that looks
   invented or unverifiable, treat it as **not_closed** and flag it as a serious concern.
5. **Assign a verdict:**

| Verdict | When |
|---|---|
| `verified_closed` | The location contains the required fix; criterion met; no fabrication. |
| `partially_verified` | Real improvement, but the action is incomplete. |
| `not_closed` | Fix absent, superficial, fabricated, or location does not support the claim. |
| `blocked_author_input` | Honestly `cannot_close_yet`; depends on student/supervisor input, properly marked. |
| `unable_to_verify` | Location uncitable or required inputs missing; state precisely why. |

6. **Record** the checked location and a one-line finding.

## Turning verdicts into V3 issues

- `verified_closed` → no action; logged only.
- `blocked_author_input` → no new issue, **but** add to the lock-readiness blocking set if the
  underlying issue is Critical or Major, and remind the student of the exact input needed.
- `partially_verified`, `not_closed`, `unable_to_verify` → create a **reopened** issue for V3 with
  provenance `reopened` and `reopened_from` = the CA_1 issue id, carrying forward (or raising) the
  original severity and a sharpened required action.

## Caution on severity drift

A defect that was Critical in V1 and remains unfixed in V2 is still Critical — do not downgrade it
because effort was visible. Conversely, if V2 genuinely resolved part of a Major issue and only a
Minor remainder persists, the reopened issue may be Minor; say why.
