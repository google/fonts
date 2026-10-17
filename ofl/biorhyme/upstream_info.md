# Investigation Report: BioRhyme

## Source Data

| Field | Value |
|-------|-------|
| Family Name | BioRhyme |
| Designer | Aoife Mooney |
| License | OFL |
| Repository URL | https://github.com/aoifemooney/makingbiorhyme |
| Commit | `b3c0488559ad7c42e11b71e65d255344faff63b9` |
| Branch | gh-pages |
| Config YAML | `sources/config.yaml` |
| Date Added | 2016-06-20 |
| Status | Complete |

## How URL Found

The repository URL `https://github.com/aoifemooney/makingbiorhyme` was established via the gftools-packager commit `1c997e944` in google/fonts, which explicitly states: "BioRhyme Version 1.600;gftools[0.9.33] taken from the upstream repo https://github.com/aoifemooney/makingbiorhyme". The copyright field in METADATA.pb also references this URL.

## How Commit Determined

The commit hash `b3c0488559ad7c42e11b71e65d255344faff63b9` was recorded by gftools-packager in commit `1c997e944` (September 2023, by Emma Marichal). The commit message explicitly states it was taken from the upstream repo at this commit. This was later incorporated into METADATA.pb via the "Merge upstream.yaml into METADATA.pb" process (`66f91f10f`) and confirmed in the fontc_crater targets list batch port (`19cdcec59`).

### Cross-verification

- The commit `b3c0488` exists in the upstream repo on the `gh-pages` branch
- It is the HEAD (and only visible commit due to squashed history) of the `gh-pages` branch
- The commit message is "Merge pull request #25 from emmamarichal/gh-pages", which corresponds to Emma Marichal's work
- The upstream.yaml created by gftools-packager in `1c997e944` references branch `gh-pages` and maps `fonts/variable/BioRhyme[wdth,wght].ttf`

## Config YAML Status

**Found in upstream at `sources/config.yaml`**

The config.yaml exists at commit `b3c0488` and configures a variable font build:
- Source: `BioRhyme.glyphs`
- Axes: wdth (100-125), wght (200-800)
- familyName: BioRhyme
- buildStatic: false
- Includes STAT table configuration

## History

1. **2016-06-20**: BioRhyme originally added to google/fonts (date_added)
2. **2017-05-23**: Static fonts added via hotfix (commit `81ab217e2`, PR #976)
3. **2023-09-20**: Variable font update via gftools-packager (commit `1c997e944`), replacing 5 static TTFs with `BioRhyme[wdth,wght].ttf`. Font upgraded to Version 1.600 with wdth and wght axes.

## Verification

- [x] Repository URL is valid and accessible
- [x] Commit hash exists in upstream repo
- [x] Commit is on the `gh-pages` branch (HEAD)
- [x] Config.yaml exists at the recorded path at the recorded commit
- [x] Source block in METADATA.pb is complete with files mapping
- [x] Variable font `BioRhyme[wdth,wght].ttf` matches the build configuration

## Confidence Level

**High** -- All data is fully verified. The gftools-packager commit provides a clear and direct link between the upstream commit and the font files in google/fonts.

## Open Questions

None.
