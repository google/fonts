# Investigation Report: Gaegu

## Summary

Gaegu is a Korean handwriting-style font family designed by JIKJI SOFT, added to Google Fonts on 2018-02-28 via PR #1459. The font was part of a batch of Korean font families onboarded by Marc Foley, with binaries mastered by Aaron Bell. No public upstream source repository has been found. The designer's GitHub account (jikjisoft) has one repository (jikjisoft/jikjifont) which is completely empty. The font was onboarded from pre-compiled binaries without any known public source.

## Key Findings

| Field              | Value                                                      |
|--------------------|------------------------------------------------------------|
| Family Name        | Gaegu                                                      |
| Designer           | JIKJI SOFT                                                 |
| License            | OFL                                                        |
| Date Added         | 2018-02-28                                                 |
| Repository URL     | None found                                                 |
| Commit Hash        | N/A                                                        |
| Config YAML        | N/A                                                        |
| Source Type         | Pre-compiled TTF binaries (no public sources)              |
| Status             | no_upstream_repo                                           |
| Confidence         | HIGH                                                       |

## Investigation Details

### Onboarding History

Gaegu was added to google/fonts in commit `16680f868` (2018-03-13) as part of PR #1459 titled "korean families r01: added", authored by Marc Foley. This PR onboarded 23 Korean font families in a single commit:

- Black And White Picture, Black Han Sans, Cute Font, Do Hyeon, Dokdo, East Sea Dokdo, **Gaegu**, Gamja Flower, Gothica 1, Gugi, Hi Melody, Jua, Kirang Haerang, Nanum Brush Script, Nanum Gothic, Nanum Myeongjo, Nanum Pen Script, Poor Story, Single Day, Song Myung, Stylish, Sunflower, Yeon Sung

The PR body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com"

### PR Discussion (PR #1459)

Key points from the PR discussion:
- Marc Foley noted that Gaegu (originally "Gaeugu") didn't have a Regular weight, only a Medium weight
- Dave Crossland approved renaming the Medium weight to Regular
- Aaron Bell confirmed there would be no issues with the switch
- Marc Foley pushed an update on 2018-02-28 renaming the font weights
- The fonts were tested on Win7 IE9 through OSX Safari via diffbrowsers

### Search for Upstream Repository

1. **jikjisoft/jikjifont**: The designer's GitHub account (jikjisoft) has one repository at `https://github.com/jikjisoft/jikjifont`. This repository is completely empty (created 2017-11-09, never received any commits). The account was created before the font was onboarded but the repo was never populated.

2. **GitHub search**: No repositories matching "gaegu font" were found under the googlefonts, jikjisoft, or aaronbell organizations.

3. **Web search**: No upstream source repository was found. The font is widely distributed by third-party font sites but none reference a source repository.

4. **Cached repos**: No Gaegu repository exists in the fontc_crater_cache.

### Font Binary Analysis

The font files in google/fonts have not changed since the original onboarding:
- `Gaegu-Light.ttf`
- `Gaegu-Regular.ttf`
- `Gaegu-Bold.ttf`

The copyright string is "Copyright 2018 The Gaegu Project Authors" with no repository URL referenced.

### Source File Assessment

No public source files (.glyphs, .ufo, .designspace, .sfd, .vfb) have been found for this font family. The binaries appear to have been prepared by Aaron Bell from sources not available publicly.

## Conclusion

Gaegu has no known public upstream repository. The designer (JIKJI SOFT) created a GitHub account and empty repository but never published sources. The fonts were onboarded as pre-compiled binaries mastered by Aaron Bell. No source block can be added to METADATA.pb.

### Recommended METADATA.pb Source Block

No source block can be added. The status remains `no_upstream_repo`.

### Pending Questions

- **Aaron Bell / Marc Foley**: Were original source files (before mastering) received from JIKJI SOFT? Are they available anywhere? Could they be published to jikjisoft/jikjifont or a googlefonts repository?
