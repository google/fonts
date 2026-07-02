# Investigation Report: Goblin One

## Summary

Goblin One is a display serif font designed by Riccardo De Franceschi and mastered by Eben Sorkin (Sorkin Type Co). It was added to Google Fonts on 2011-06-29 as part of the initial repository commit. The upstream repository is `librefonts/goblinone` on GitHub, which contains only legacy source formats (SFD and VFB). There is no `config.yaml` in the upstream repo and no gftools-builder-compatible sources, so building with gftools-builder/fontc is not possible. The METADATA.pb currently has no source block.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Goblin One                                                         |
| Designer          | Riccardo De Franceschi                                             |
| Date Added        | 2011-06-29                                                         |
| Repository URL    | https://github.com/librefonts/goblinone                            |
| Commit Hash       | 446c2b743e1eda33533ad624c543cfd623eb7c90 (only commit in repo)     |
| Branch            | master                                                             |
| Config Path       | N/A (SFD/VFB sources only)                                        |
| Source Files      | src/GoblinOne-TTF.sfd, src/GoblinOne.vfb                          |
| Status            | **no_config_possible**                                             |
| Confidence        | **HIGH**                                                           |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has no `source { }` block. It contains basic metadata:
- Family name, designer, license, category
- Single static font: `GoblinOne.ttf` (weight 400)
- Subsets: menu, latin
- Classifications: DISPLAY, SERIF

### Onboarding History in google/fonts

Goblin One was part of the initial commit (`90abd17b4`) to the google/fonts repository on 2015-03-07 (the bulk import by Dave Crossland). The font was originally added to Google Fonts on 2011-06-29 per the `date_added` field. The TTF file has never been modified since that initial commit.

No PR or further commit has ever updated the font binary.

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/librefonts/goblinone/` confirms:
- Remote URL: `https://github.com/librefonts/goblinone`
- Single commit: `446c2b7` by hash3g, dated 2014-10-17
- The repo contains TTX decompositions of the font, plus source files

### Source Files

The upstream repo contains only legacy source formats:
- `src/GoblinOne-TTF.sfd` — FontForge SFD file
- `src/GoblinOne.vfb` — FontLab VFB file (binary)

There are no `.glyphs`, `.ufo`, or `.designspace` files. There is no `config.yaml` or `config.yml`. The font is a single-weight static font with no variable font axes.

Since the sources are in legacy formats (SFD/VFB) that are not supported by gftools-builder or fontc, creating a config.yaml would not be useful.

### Font Origin

Per the FONTLOG.txt:
- Designed by Riccardo De Franceschi (2010)
- Spaced and mastered by Eben Sorkin / Sorkin Type Co (2011)
- Mastered from FontLab to TTF

The copyright string references "Sorkin Type Co" as the copyright holder. The `librefonts` GitHub organization appears to be an archive of Google Fonts library fonts with their sources decomposed into TTX format.

## Conclusion

Goblin One has an identifiable upstream repository (`librefonts/goblinone`), but it only contains legacy source formats (SFD/VFB). A `config.yaml` is not possible because gftools-builder does not support these formats. A minimal source block can be added to record the repository URL for documentation purposes.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/goblinone"
  commit: "446c2b743e1eda33533ad624c543cfd623eb7c90"
  branch: "master"
}
```

**Status: no_config_possible**
