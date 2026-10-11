# GFS Neohellenic - Investigation Report

## Summary

GFS Neohellenic is a sans-serif typeface designed by Takis Katsoulidis and digitized by George Matthiopoulos of the Greek Font Society, based on Victor Scholderer's 1927 "New Hellenic" type for the Lanston Monotype Corporation. It was added to Google Fonts on 2010-09-21 in the initial bulk commit. The family has four styles (Regular, Italic, Bold, Bold Italic). The only known upstream repository is `librefonts/gfsneohellenic`, which is an automated archive containing TTX decompositions of the font binaries -- not editable source files. No gftools-builder-compatible sources (.glyphs, .ufo, .designspace) exist in the upstream repo, making a config.yaml impossible.

## Key Findings

| Field              | Value                                          |
|--------------------|------------------------------------------------|
| Family Name        | GFS Neohellenic                                |
| Designer           | Greek Font Society (Takis Katsoulidis, George D. Matthiopoulos) |
| Repository URL     | https://github.com/librefonts/gfsneohellenic   |
| Commit Hash        | 76fc8bb657ac989832180f3b6dea778862059532        |
| Config YAML        | None (no gftools-builder-compatible sources)    |
| Status             | no_config_possible                              |
| Confidence         | HIGH                                           |
| Date Added         | 2010-09-21                                     |
| License            | OFL                                            |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/gfsneohellenic/METADATA.pb` has no `source { }` block. It contains:
- Family name: "GFS Neohellenic"
- Designer: "Greek Font Society"
- Four font styles:
  - Regular (400 normal)
  - Italic (400 italic)
  - Bold (700 normal)
  - Bold Italic (700 italic)
- Subsets: menu, greek, greek-ext, latin, vietnamese

### Google Fonts Repository History

The font was introduced in commit `90abd17b4` ("Initial commit") on 2015-03-07 by Dave Crossland. The TTF files have never been modified since that initial commit. Only metadata files have been updated:
- `480630de3`: Tentative update to METADATA.pb textprotos
- `27f377ab0`: Update copyright field in METADATA.pb
- `883939708`: Remove METADATA.json files
- `633ebadbf`: Add language support metadata (#4160)
- `84f7346a7`: Found some more subsets (added greek-ext, latin, vietnamese)

### Upstream Repository Analysis

The repository at `https://github.com/librefonts/gfsneohellenic` is part of the `librefonts` organization, an automated archive of Google Fonts families maintained by hash3g (Dave Crossland's automated tooling). The repo has exactly **one commit**:

- **Commit**: `76fc8bb` (2014-10-17, by hash3g)
- **Message**: "update .travis.yml"

The repository contents:
- **Root level**: TTX decomposition of all four styles (GFSNeohellenic.ttf, GFSNeohellenicItalic.ttf, GFSNeohellenicBold.ttf, GFSNeohellenicBoldItalic.ttf) split into per-table XML files, plus `METADATA.json`, `OFL.txt`, `DESCRIPTION.en_us.html`, `.travis.yml`
- **`src/` directory**: TTX decompositions of all four styles in both OTF and TTF formats, plus a PDF specimen ("NeoHellenic Specimen.pdf"), `VERSIONS.txt`, and `METADATA_comments.txt`

The `.travis.yml` uses an old fontbakery-cli build pipeline from 2014 that compiles TTX files back into binaries. This is not a gftools-builder configuration.

### Source File Assessment

No gftools-builder-compatible sources exist anywhere in the repository:
- No `.glyphs` files
- No `.ufo` directories
- No `.designspace` files
- No `.sfd` (FontForge) files
- No `config.yaml`

The only "sources" are TTX (XML) decompositions of the compiled font binaries. These are a round-trippable serialization of the binary font data, not editable design sources. The original design sources (likely created in a proprietary tool by the Greek Font Society) are not publicly available.

### Greek Font Society Context

The Greek Font Society (GFS) distributes their fonts through their website at `https://www.greekfontsociety-gfs.gr`. The DESCRIPTION file notes that GFS digitized the typeface in 1993-1994, funded by the Athens Archaeological Society, with additional weights (italic, bold, bold italic) added in 2000 along with a Latin version. The `librefonts` repos are third-party archives, not official GFS repositories.

## Conclusion

The `librefonts/gfsneohellenic` repository is a valid upstream reference as it is the only known GitHub repository for this font, but it contains only TTX decompositions, not editable design sources. A config.yaml is not possible because there are no gftools-builder-compatible source files. The repository has a single commit from 2014, which is the only possible commit hash to reference.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/gfsneohellenic"
  commit: "76fc8bb657ac989832180f3b6dea778862059532"
}
```

Note: `config_yaml` is omitted because no gftools-builder-compatible sources exist. The upstream repository contains only TTX decompositions of the font binaries.
