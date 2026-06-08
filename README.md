# Yassin ESSS PFE Review-Article Pipeline — installable plugin

One bundle, ten skills, for ALL ESSS students (any filière, any project). It carries a student from
their note de cadrage to a publication-ready **systematic review** and three journal-submission packs.

## What's inside (the ten steps)
1. yassin-pfe-01-review-v1 — build V1 + create the student profile
2. yassin-pfe-02-ca-1 — first critical appraisal of V1
3. yassin-pfe-03-review-v2 — V2 closing every appraisal issue
4. yassin-pfe-04-ca-2 — deep second appraisal + lock-readiness
5. yassin-pfe-05-review-v3 — V3 and the content lock (science frozen)
6. yassin-pfe-06-ai-ara-1 — AI-authorship audit of the locked V3
7. yassin-pfe-07-asw-1 — authorship revision to V4 (lock-safe)
8. yassin-pfe-08-ai-ara-2 — second authorship audit of V4
9. yassin-pfe-09-asw-2 — final authorship revision to V5
10. yassin-pfe-10-publishing-assistance — journal selection + submission packs

## Install (Claude Cowork / Claude Code)
1. Unzip this file to a folder.
2. In Cowork/Claude Code, add the local marketplace and install:
   ```
   /plugin marketplace add /path/to/yassin-esss-pfe-marketplace
   /plugin install yassin-pfe-review-pipeline@yassin-esss-pfe
   /reload-plugins
   ```
   (You can also point `/plugin marketplace add` at a Git repo if you host this folder on GitHub.)
3. Each step is then available as `/yassin-pfe-review-pipeline:<skill>` and via Cowork routing.

The student fills in their own identity, department, supervisors and note de cadrage at Step 1;
nothing here is tied to a specific project or filière.
