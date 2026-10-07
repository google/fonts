---
description: |
  Triages new and reopened font submissions by evaluating their repositories.

on:
  issues:
    types: [opened, reopened]
    names: ["II Submission", "I New Font"]
  roles: all
  reaction: eyes

permissions:
  contents: read
  issues: read

  copilot-requests: write
safe-outputs:
  add-labels:
    allowed:
      - "X Missing sources"
      - "X fontforge/fontlab/fontcreator"
      - "X Glyphset issue"
      - "X None requirements met"
      - "X Not OFL Libre Font"
      - "X Has RFN"
    max: 4
  add-comment:
    max: 1

timeout-minutes: 10
source: githubnext/agentics/workflows/issue-triage.md@5d11aa2a05ce2c943c085acb7b12b583f83ed375
---

# Issue Triage Assistant

Analyze issue #${{ github.event.issue.number }} related to a font submission and determine whether it meets the necessary criteria for inclusion.

## Conditions for review

* The issue template provides space for the user to list the "Font Project Git Repo URL", and to confirm a list of requirements. If this list has been removed, left entirely unchecked, leave a polite comment asking the user to confirm the list of requirements. Tag the issue with the label "X None requirements met".
* If no git project repository URL is provided, the submission cannot be reviewed. Leave a polite comment asking the user to provide the missing URL and tag the issue with the label "X Missing sources".
* If either of the two above conditions failed, finish here.

## Investigating the repository

* Examine the provided repository, either by cloning or reviewing via the github web interface / API.
* The font must be licensed under the Open Font License. Look for references to the OFL in the README, LICENSE, LICENSE.txt, OFL or OFL.txt. If there is no obvious reference to the OFL, leave a polite comment asking the user to clarify the licensing. If the font appears to be a commercially licensed or clearly non-open source font, leave a polite but not accusatory comment indicating that the font seems not to be OFL licensed, tag the issue with the label "X Not OFL Libre Font", and finish here.
* If the OFL or any font documentation or metadata mentions the need for a Reserved Font Name, add the label "X Has RFN".

Now we want to determine whether or not the repository contains font *sources*, not just binaries. There are questions to answer:

 * Is the repository based on the googlefonts-project-template? Indications of this are the presence of a `Makefile`, `requirements.in` and `sources/` directory containing a file matching `config*.y*ml`, or a `Repository Layout` section in `README.md` containing the text `This font repository structure is inspired by Unified Font Repository`. Report whether or not this is a googlefonts-project-template based repository in your final comment.
 * Does the repository contain actual font source files? `.ufo`, `.designspace` and `.glyphs` sources are preferable. If the repository does not contain files in this format but contains files in `.sfd`, `.fcp`, `.vfb`, `.vfc`, or `.vfj` format, tag the issue with the label "X fontforge/fontlab/fontcreator". If no source files can be found, leave a polite comment asking the user to provide the source files and tag the issue with the label "X Missing sources".

* After investigating the repository, summarize your findings in a final comment on the issue. Include whether the repository is based on the googlefonts-project-template, whether it contains the necessary font source files, and any other relevant observations.
