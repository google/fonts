# Investigation Report: Headland One

## Summary

Headland One is a serif typeface designed by Gary Lonergan and mastered by Eben Sorkin (Sorkin Type Co), added to Google Fonts on 2012-05-09 via the initial commit of the repository. It has no source block in METADATA.pb. An upstream repository exists at `https://github.com/librefonts/headlandone`, but it contains only SFD source files (FontForge format) and TTX dumps -- no gftools-builder compatible sources (.glyphs, .ufo, or .designspace). No config.yaml is possible for this family.

## Key Findings

| Field              | Value                                                                 |
|--------------------|-----------------------------------------------------------------------|
| Family Name        | Headland One                                                          |
| Designer           | Gary Lonergan                                                         |
| Repository URL     | https://github.com/librefonts/headlandone                             |
| Commit Hash        | c5193604253d9cf325e43b44e88045a503b53cbf                              |
| Config YAML        | None (SFD-only sources)                                               |
| Status             | no_config_possible                                                    |
| Confidence         | HIGH                                                                  |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has no source block at all. It contains only:
- Family name, designer ("Gary Lonergan"), license (OFL)
- Category: SERIF
- Date added: 2012-05-09
- One font weight: HeadlandOne-Regular.ttf (400 normal)
- Subsets: menu, latin, latin-ext

No `repository_url`, `commit`, or `config_yaml` fields.

### Google Fonts Git History

The font was part of the massive initial commit of the google/fonts repository:

1. **90abd17b4** - `Initial commit` -- Mar 7, 2015 (by Dave Crossland) -- this is when the git repo was created; the font was already in the Google Fonts catalog since 2012-05-09.
2. **76adaf1d2** - `deploy: c7e274018...` -- this commit DELETED the Headland One files (likely a transient state in repo reorganization).

The binary TTF file has only been touched by these two commits. There are no PR references or update commits.

### Upstream Repository

The upstream repo at `https://github.com/librefonts/headlandone` is cached at `fontc_crater_cache/librefonts/headlandone`.

The repo has a single commit:
- **c519360** - `update .travis.yml` -- Oct 17, 2014

This is a typical `librefonts` mirror repo that contains:
- TTX table dumps of the font files
- SFD source files (`src/HeadlandOne-Regular-TTF.sfd` and `src/HeadlandOne-Regular-OTF.sfd`)
- FONTLOG.txt, DESCRIPTION.en_us.html, OFL.txt, METADATA.json

### Source Files

The only source files in the repo are:
- `src/HeadlandOne-Regular-TTF.sfd` -- FontForge SFD for TrueType version
- `src/HeadlandOne-Regular-OTF.sfd` -- FontForge SFD for OpenType/CFF version

These are SFD (FontForge) format files. The FONTLOG.txt mentions the original source was created in FontLab VBF format. No `.glyphs`, `.ufo`, or `.designspace` files exist. These SFD sources are not compatible with gftools-builder, so no config.yaml can be created.

### Font Copyright and Origin

From the FONTLOG.txt and binary metadata:
- Designed by Gary Lonergan (garylonergan@hotmail.com)
- Mastered by Eben Sorkin (sorkineben@gmail.com, Sorkin Type Co)
- Copyright: "Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com)"
- Version 1.002 (April 2011)
- The DESCRIPTION.en_us.html references Google Code as the source repository (historical -- Google Code was shut down)

No override config.yaml exists in the google/fonts directory.

## Conclusion

The family has an identifiable upstream repo at `librefonts/headlandone` with only one commit. The sources are SFD-only (FontForge format), which are not compatible with gftools-builder. A source block can be added with the repository URL and commit hash, but no config.yaml is possible.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/headlandone"
  commit: "c5193604253d9cf325e43b44e88045a503b53cbf"
}
```
