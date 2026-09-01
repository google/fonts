# Investigation Report: Hi Melody

## Summary

Hi Melody is a Korean handwriting font designed by YoonDesign Inc, added to Google Fonts on 2018-02-23 as part of a bulk Korean font onboarding (PR #1459) by Marc Foley. The upstream repository at `https://github.com/yoondesign/Yoonfont-HiMelody` contains only compiled binary fonts (.otf and .ttf) with no source files. The repo has a single meaningful commit (4feb231) from 2017-12-19. No config.yaml is possible since no buildable sources exist.

## Key Findings

| Field             | Value                                                                 |
|-------------------|-----------------------------------------------------------------------|
| Family Name       | Hi Melody                                                             |
| Designer          | YoonDesign Inc                                                        |
| Repository URL    | https://github.com/yoondesign/Yoonfont-HiMelody                      |
| Commit Hash       | 4feb2315457c615527775b455d119e9f3b8c8863                              |
| Config YAML       | N/A (no buildable sources)                                            |
| Status            | no_config_possible                                                    |
| Confidence        | HIGH                                                                  |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has no source block in the upstream google/fonts main branch. A source block with `repository_url` and `commit` was added in a local commit (9a14639f3) as part of a batch of 602 families but may not yet be merged upstream.

Key METADATA.pb fields:
- Designer: YoonDesign Inc
- License: OFL
- Category: HANDWRITING
- Date added: 2018-02-23
- Primary script: Kore

### Git History in google/fonts

The font was onboarded in commit `16680f868` (PR #1459, "korean families r01: added", 2018-03-13) by Marc Foley. This was a large batch commit adding ~25 Korean font families simultaneously. The PR body states: "Korean Font binaries have been mastered by Aaron Bell."

A subsequent commit `1ef157d39` ("Add back case corrected files", 2018-03-13) by Dave Crossland re-added the font file `HiMelody-Regular.ttf` with corrected filename casing (from `Himelody-Regular.ttf` to `HiMelody-Regular.ttf`). The font binary has not been modified since.

### Upstream Repository Analysis

The upstream repo `yoondesign/Yoonfont-HiMelody` was verified via the GitHub API:
- Owner: yoondesign
- Default branch: master
- Last pushed: 2017-12-19
- Total files at HEAD: `Himelody.otf`, `Himelody.ttf`, `OFL_Yoondesign HiMelody.txt`, `README.md`, `Readme_Yoondesign_HiMelody.txt`

The repository contains **only compiled font binaries** (OTF and TTF). There are no source files (.glyphs, .ufo, .designspace, .sfd) whatsoever. The commit 4feb231 is the most recent commit and is dated 2017-12-19, which predates the google/fonts onboarding (2018-03-13).

The repo is NOT cached in the local upstream repos cache. Only two other yoondesign repos are cached (yoonfont-Gamjaflower and Yoonfont-KoreaDokdo).

### Commit Verification

The commit `4feb2315457c615527775b455d119e9f3b8c8863` was verified on GitHub:
- Message: "Create README.md"
- Date: 2017-12-19
- This is the HEAD/latest commit of the repository

Since this is the only meaningful commit and the entire repo has only binaries, this is the correct reference commit. The font binary in google/fonts was likely provided directly by Aaron Bell who "mastered" the Korean fonts per the PR description, and the compiled binaries were placed in this upstream repo.

### Source Files Assessment

No buildable source files exist anywhere in the repository at any commit:
- No .glyphs, .glyphx, .ufo, .designspace, or .sfd files
- No config.yaml or build.py
- Only compiled .otf and .ttf binaries

This is typical of several YoonDesign fonts where the company released only compiled binaries under OFL.

## Conclusion

**Status: no_config_possible**

Hi Melody's upstream repository contains only compiled font binaries with no source files. The repository URL and commit hash are verified and correct. No config.yaml can be created because there are no buildable sources. The source block should include `repository_url` and `commit` but cannot include `config_yaml`.
