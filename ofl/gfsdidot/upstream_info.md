# GFS Didot - Investigation Report

## Summary

GFS Didot is a serif typeface designed by Takis Katsoulidis and digitized by George Matthiopoulos of the Greek Font Society, based on Firmin Didot's famous 1805 Greek typeface. It was added to Google Fonts on 2010-09-21 in the initial bulk commit. The only known upstream repository is `librefonts/gfsdidot`, which is an automated archive containing TTX decompositions of the font binaries -- not editable source files. No gftools-builder-compatible sources (.glyphs, .ufo, .designspace) exist in the upstream repo, making a config.yaml impossible.

## Key Findings

| Field              | Value                                          |
|--------------------|------------------------------------------------|
| Family Name        | GFS Didot                                      |
| Designer           | Greek Font Society (Takis Katsoulidis, George D. Matthiopoulos) |
| Repository URL     | https://github.com/librefonts/gfsdidot         |
| Commit Hash        | ce7a216e8765803eee73b284275975d323e2396c        |
| Config YAML        | None (no gftools-builder-compatible sources)    |
| Status             | no_config_possible                              |
| Confidence         | HIGH                                           |
| Date Added         | 2010-09-21                                     |
| License            | OFL                                            |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/gfsdidot/METADATA.pb` has no `source { }` block. It contains:
- Family name: "GFS Didot"
- Designer: "Greek Font Society"
- One font style: Regular (400)
- Subsets: menu, greek, greek-ext, latin, vietnamese

### Google Fonts Repository History

The font was introduced in commit `90abd17b4` ("Initial commit") on 2015-03-07 by Dave Crossland. The TTF file `GFSDidot-Regular.ttf` has never been modified since that initial commit. Only metadata files have been updated:
- `480630de3`: Tentative update to METADATA.pb textprotos
- `27f377ab0`: Update copyright field in METADATA.pb
- `883939708`: Remove METADATA.json files
- `633ebadbf`: Add language support metadata (#4160)
- `25eb9a634`: Update DESCRIPTION.en_us.html (corrected the name "Korais")
- `84f7346a7`: Found some more subsets (added greek-ext, latin, vietnamese)

### Upstream Repository Analysis

The repository at `https://github.com/librefonts/gfsdidot` is part of the `librefonts` organization, an automated archive of Google Fonts families maintained by hash3g (Dave Crossland's automated tooling). The repo has exactly **one commit**:

- **Commit**: `ce7a216` (2014-10-17, by hash3g)
- **Message**: "update .travis.yml"

The repository contents:
- **Root level**: TTX decomposition of `GFSDidot-Regular.ttf` (split into per-table XML files), plus `METADATA.json`, `OFL.txt`, `DESCRIPTION.en_us.html`, `.travis.yml`
- **`src/` directory**: TTX decompositions of additional font variants (Regular, Italic, Bold, Bold Italic) in both OTF and TTF formats, plus a PDF specimen and `VERSIONS.txt` / `METADATA_comments.txt`

The `.travis.yml` uses an old fontbakery-cli build pipeline from 2014 that compiles TTX files back into binaries. This is not a gftools-builder configuration.

### Source File Assessment

No gftools-builder-compatible sources exist anywhere in the repository:
- No `.glyphs` files
- No `.ufo` directories
- No `.designspace` files
- No `.sfd` (FontForge) files
- No `config.yaml`

The only "sources" are TTX (XML) decompositions of the compiled font binaries. These are essentially a round-trippable serialization of the binary font data, not editable design sources. The original design sources (likely created in a proprietary tool by the Greek Font Society) are not publicly available.

### Greek Font Society Context

The Greek Font Society (GFS) distributes their fonts through their website at `https://www.greekfontsociety-gfs.gr`. The fonts were designed in the 1990s-2000s and the original design sources predate modern open-source font development workflows. The `librefonts` repos are third-party archives, not official GFS repositories.

## Conclusion

The `librefonts/gfsdidot` repository is a valid upstream reference as it is the only known GitHub repository for this font, but it contains only TTX decompositions, not editable design sources. A config.yaml is not possible because there are no gftools-builder-compatible source files. The repository has a single commit from 2014, which is the only possible commit hash to reference.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/gfsdidot"
  commit: "ce7a216e8765803eee73b284275975d323e2396c"
}
```

Note: `config_yaml` is omitted because no gftools-builder-compatible sources exist. The upstream repository contains only TTX decompositions of the font binaries.
