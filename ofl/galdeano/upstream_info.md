# Investigation Report: Galdeano

## Summary

Galdeano is a humanist sans-serif typeface designed by Dario Manuel Muhafara. It was part of the initial commit to the google/fonts repository on 2015-03-07. The upstream repository is `librefonts/galdeano`, a single-commit archive repo created by Alexei Vanyashin (hash3g) on 2014-10-17. The repo contains only legacy source formats (VFB and SFD) with no gftools-builder compatible sources.

## Key Findings

| Field             | Value                                                    |
|-------------------|----------------------------------------------------------|
| Family Name       | Galdeano                                                 |
| Repository URL    | https://github.com/librefonts/galdeano                   |
| Commit Hash       | 0325c647c669479930cc9126131a78ca5b942db9                 |
| Config YAML       | None (SFD/VFB sources only)                              |
| Source Type        | SFD + VFB (legacy formats)                               |
| Status            | no_config_possible                                       |
| Confidence        | HIGH                                                     |
| Date Added        | 2011-12-07                                               |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb has no `source { }` block. The font is listed under the OFL license with designer "Dario Manuel Muhafara". Copyright references http://www.tipo.net.ar.

### Git History in google/fonts

- **90abd17b4** (2015-03-07): "Initial commit" by Dave Crossland - The font was included in the massive initial commit that added all fonts to the google/fonts repository.
- **76adaf1d2**: Deploy commit (no font changes).

The font binary (Galdeano-Regular.ttf) has never been modified since the initial commit. All subsequent commits touching the directory were metadata-only changes (METADATA.pb updates, language support, etc.).

### Upstream Repository

The repo `librefonts/galdeano` was created on 2014-07-16 and last pushed on 2014-10-17. It contains a single commit:

- **0325c64** (2014-10-17): "update .travis.yml" by hash3g (Alexei Vanyashin) - This is a squashed initial commit that includes all files: TTX decompositions, source files, metadata, and Travis CI configuration.

The `librefonts` organization is a collection of archived font repos, typically migrated from the old Google Font Directory.

### Source Files

The repo contains legacy source formats only:
- `src/Galdeano-Regular.vfb` - Original FontLab source
- `src/Galdeano-Regular-OTF.vfb` - OTF-specific FontLab source
- `src/Galdeano-Regular-TTF.sfd` - FontForge SFD source (TrueType outlines)

Additionally, the repo has extensive TTX decompositions of both the TTF and OTF files at the root level and in `src/`.

The `src/VERSIONS.txt` confirms: "Galdeano-Regular.ttf: Version 1.001"

The `src/METADATA_comments.txt` contains the original subsetting/processing commands from the Google Font Directory workflow.

### Config YAML Assessment

No `config.yaml` exists. The only source formats are VFB (proprietary FontLab) and SFD (FontForge). Neither is compatible with gftools-builder. Creating an override config.yaml is not possible without converting the sources to a modern format first.

## Conclusion

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/galdeano"
  commit: "0325c647c669479930cc9126131a78ca5b942db9"
}
```

**Status**: no_config_possible

**Notes**: This is a legacy font from the original Google Font Directory era. The `librefonts/galdeano` repo is an archive containing VFB and SFD sources that are not compatible with gftools-builder. The single commit in the repo predates the google/fonts initial commit. No config.yaml can be created without first converting the sources to a modern format (UFO, .glyphs, or .designspace).
