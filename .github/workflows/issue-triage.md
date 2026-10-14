---
description: |
  Triages new and reopened font submissions by evaluating their repositories.

on:
  issues:
    types: [opened, reopened]
  roles: all
  reaction: eyes

permissions:
  contents: read
  issues: read
  pull-requests: read

  copilot-requests: none
tools:
  bash: ["cat", "ls", "find", "grep", "head", "tail", "wc"]
  github:
    min-integrity: none
safe-outputs:
  add-labels:
    allowed:
      - "X Missing sources"
      - "X fontforge/fontlab/fontcreator"
      - "X Glyphset issue"
      - "X None requirements met"
      - "X Not OFL Libre Font"
      - "X Has RFN"
      - "X Form not completed"
      - "II Submission"
      - "I New Font"
    max: 6
  add-comment:
    max: 1

timeout-minutes: 10
source: githubnext/agentics/workflows/issue-triage.md@5d11aa2a05ce2c943c085acb7b12b583f83ed375
---

# Issue Triage Assistant

Analyze issue #${{ github.event.issue.number }} related to a font submission and determine whether it meets the necessary criteria for inclusion.

## Preconditions

* The issue template for new font submissions from external users
automatically adds the `I New Font` and `II Submission` tags. It also
provides a pro-forma set of questions and checklist items to help us
prepare to onboard the font. New font submissions *must* include these
questions and checklists. They may not make up their own questions and
checklist; they must use the one from the issue template. Hence, the
first task is to determine "does this issue appear to be related to a
request to add a new font to Google Fonts?" If not, finish here.

* The second task is to determine: "has the user bypassed the issue
template in `.github/ISSUE_TEMPLATE/1_add-font.md`?" Compare the issue's
body text with the body text of the issue template. If the template has
been bypassed, add the `I New Font`, `II Submission` and `X Form not
completed` tags, add a comment asking the user to copy and paste the
questions into a comment and then answer them, and finish here.

## Conditions for review

At this point we have a new issue which appears to be related to a font
submission, and correctly includes the issue template. But has it been
completed correctly?

* The issue template provides space for the user to list the "Font
Project Git Repo URL", and to confirm a list of requirements. If this
list has been removed, left entirely unchecked, leave a polite comment
asking the user to confirm the list of requirements. Tag the issue with
the label "X None requirements met".

* If no git project repository URL is provided, the submission cannot be
reviewed. Leave a polite comment asking the user to provide the missing
URL and tag the issue with the label "X Missing sources". 

* If either of the two above conditions failed, finish here.

## Investigating the repository

* Examine the provided repository, either by cloning or reviewing via
the github web interface / API.

* The font must be licensed under the Open Font License. Look for
references to the OFL in the README, LICENSE, LICENSE.txt, OFL or
OFL.txt. If there is no obvious reference to the OFL, leave a polite
comment asking the user to clarify the licensing. If the font appears to
be a commercially licensed or clearly non-open source font, leave a
polite but not accusatory comment indicating that the font seems not to
be OFL licensed, tag the issue with the label "X Not OFL Libre Font",
and finish here.

* If the OFL or any font documentation or metadata mentions the need for
a Reserved Font Name, add the label "X Has RFN".

Now we want to determine whether or not the repository contains font
*sources*, not just binaries. There are questions to answer:

* Is the repository based on the googlefonts-project-template?
Indications of this are the presence of a `Makefile`, `requirements.in`
and `sources/` directory containing a file matching `config*.y*ml`, or a
`Repository Layout` section in `README.md` containing the text `This
font repository structure is inspired by Unified Font Repository`.
Report whether or not this is a googlefonts-project-template based
repository in your final comment.

* Does the repository contain actual font source files? `.ufo`,
`.designspace` and `.glyphs` sources are preferable. If the repository
does not contain files in this format but contains files in `.sfd`,
`.fcp`, `.vfb`, `.vfc`, or `.vfj` format, tag the issue with the label
"X fontforge/fontlab/fontcreator". If no source files can be found,
leave a polite comment asking the user to provide the source files and
tag the issue with the label "X Missing sources".

* After investigating the repository, summarize your findings in a final
comment on the issue. Include whether the repository is based on the
googlefonts-project-template, whether it contains the necessary font
source files, and any other relevant observations.
