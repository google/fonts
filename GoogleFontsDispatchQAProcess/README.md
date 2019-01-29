# Google Fonts: Dispatch/QA Process

In a video conference call on December 3rd, 2018 we (@m4rc1e, @graphicore, Irin) documented the current manual processes of
- upgrading existing families
- and on-boarding new families

to [Google Fonts](https://github.com/google/fonts/). We also outlined a proposed process for an automated/supporting tool (the Dispatcher) which is developed as part of the [Font Bakery Dashboard](https://github.com/googlefonts/fontbakery-dashboard/).

#### abbreviations
- *MF: @m4rc1e in the role of the responsible engineer*
- *FB: Font Bakery*
- *QA: Quality Assurance*
- *PR: Pull Request*

## Current approach for new family

- MF: Receives email from family owner that they want to include project on Google Fonts.
- MF: Checks repo is on [spreadsheet](https://docs.google.com/spreadsheets/d/1ampzD9veEdrwUMkOAJkMNkftqtv1jEygiPR0wZ6eNl8/edit#gid=0) and is official
  - If work is a fork, ask DC whether it should be integrated into original repo
- MF: Metadata check:
  - Is font name taken? Check on [namecheck.fontdata.com](http://namecheck.fontdata.com/)
  - Is it trademarked? Check on [uspto.gov](https://www.uspto.gov/trademarks-application-process/search-trademark-database)
- MF: QA upstream using FB and Diffbrowsers. Also inspect every glyph
  - If issues, ask author to fix
  - For high priority families, do fixes; In future, for high priority families, have a way to keep Google Onboarding Manager and author updated daily on what needs to happen next, and have "deadlines" for fixing them
  -  MF: Package into dir on google/fonts
  - Generate new metadata.pb, [https://github.com/googlefonts/gftools/blob/master/bin/gftools-add-font.py](https://github.com/googlefonts/gftools/blob/master/bin/gftools-add-font.py)
    - Add font category and author fields to metadata
- MF: Rerun QA tools. Using wrapper script (MF to upload this week)
- MF: Submit PR



## Current approach for upgrading families

- MF: received an email from user wanting us to upgrade their project
- MF: Checks repo is the official repo
- MF: QA upstream.
- MF: Repackage
  - Regenerate metadata.pb using, [https://github.com/googlefonts/gftools/blob/master/bin/gftools-add-font.py](https://github.com/googlefonts/gftools/blob/master/bin/gftools-add-font.py)
- MF: Submit PR



## Proposed approach new family

- User clicks "add new family radio button"
- User submits family info via expanded form or still via email (github auth + repo write required)
  - Must be github repo
  - Sources must exist
  - License is OFL
- Thank user
- MF: Review form info is good.
- Form then updates spreadsheet
- Generate package
- Run QA tools on package
- Inform user if there are errors
- MF: inspect visual diffs
- MF: if good sign off



## Proposed approach family update

- User clicks on "update family radio button"
- User provides "upstream url"
  - User adds optional authors
- Thank user
- MF: Review form info is good.
- Form then updates spreadsheet
- Generate package
- Run QA tools on package
- MF: Determine if family has passed
- MF: Inform author of necessary changes.
- Once author has responded, repeat packaging and QA
- MF: reinspect
- MF: sign off



## Proposed unified new family and family update approach:

- **(new)** User clicks "add new family radio button"
  - User submits family info via expanded form or still via email (github auth + repo write required)
    - Must be github repo
    - Sources must exist
    - License is OFL
- **(upgrade)** User clicks on "update family radio button"
  - User provides "upstream url" (or just selects family name?)
    - User adds optional authors
- Thank user
- MF: Review form info is good.
- Form then updates spreadsheet (if necessary).
- Generate package (using the spreadsheet info. TODO: DESCRIPTION file?, complete METADATA.pb)
- Run QA tools on package
- MF: Determine if family has passed/inspect visual diffs (depending on whether the family is new or an upgrade, this inspection is a bit different.)
- MF: if bad inform author of necessary changes.
  - Once author has responded, repeat packaging and QA (This repeat will be probably be just a new dispatcher process, like an upgrade at this point. If there were changes to the spreadsheet, they&#39;re already done in following iterations.)
- MF: if good sign off

---

### Add to spreadsheet fields:

Basically all we need to generate complete METADATA.pb:

-Author info
-Category
-Family style



**Reference**

*MD: Material Design, internal tool.*

MD Icons upload site:

 ![MD Icons upload site](assets/MDIconsUploadSite.png 'MD Icons upload site')

MD Icons submit form format:

 ![MD Icons submit form format](assets/MDIconsSubmitFormFormat.png 'MD Icons submit form format')

