# Investigation Report: Galindo

## Summary

Galindo is a display typeface designed by Brian J. Bonislawsky (Astigmatic/AOETI). It was part of the initial commit to the google/fonts repository on 2015-03-07. The upstream repository is `librefonts/galindo`, a single-commit archive repo created by Alexei Vanyashin (hash3g) on 2014-10-17. The repo contains only legacy VFB sources with no gftools-builder compatible formats.

## Key Findings

| Field             | Value                                                    |
|-------------------|----------------------------------------------------------|
| Family Name       | Galindo                                                  |
| Repository URL    | https://github.com/librefonts/galindo                    |
| Commit Hash       | dc5fea52318d56672b1e3f000851806c8b5bd2cc                 |
| Config YAML       | None (VFB sources only)                                  |
| Source Type        | VFB (legacy FontLab format)                              |
| Status            | no_config_possible                                       |
| Confidence        | HIGH                                                     |
| Date Added        | 2012-08-13                                               |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb has no `source { }` block. The font is listed under the OFL license with designer "Astigmatic". Copyright references Brian J. Bonislawsky DBA Astigmatic (AOETI).

### Git History in google/fonts

- **90abd17b4** (2015-03-07): "Initial commit" by Dave Crossland - The font was included in the massive initial commit that added all fonts to the google/fonts repository.
- **76adaf1d2**: Deploy commit (no font changes).

The font binary (Galindo-Regular.ttf) has never been modified since the initial commit. All subsequent commits touching the directory were metadata-only changes (METADATA.pb updates, language support, classifications, etc.).

### FONTLOG.txt

The FONTLOG.txt in the google/fonts directory documents:
- Version 1.001, released 2012-05-24
- Three source files mentioned: Galindo-Regular.vfb (original), Galindo-Regular-OTF.vfb (merged contours for OTF), Galindo-Regular-TTF.vfb (TrueType outlines with hinting)

### Upstream Repository

The repo `librefonts/galindo` was created on 2014-07-16 and last pushed on 2014-10-17. It contains a single commit:

- **dc5fea5** (2014-10-17): "update .travis.yml" by hash3g (Alexei Vanyashin) - This is a squashed initial commit that includes all files: TTX decompositions, source files, metadata, and Travis CI configuration.

The `librefonts` organization is a collection of archived font repos, typically migrated from the old Google Font Directory.

### Source Files

The repo contains legacy VFB source files only:
- `src/Galindo-Regular.vfb` - Original FontLab source with contour overlaps
- `src/Galindo-Regular-OTF.vfb` - OTF-specific FontLab source (merged contours)
- `src/Galindo-Regular-TTF.vfb` - TrueType outlines with hinting adjustments

All three are binary VFB files (FontLab Studio format). Additionally, the repo has extensive TTX decompositions of both the TTF and OTF at the root level and in `src/`.

The `src/VERSIONS.txt` confirms: "Galindo-Regular.ttf: Version 1.000"

The `src/METADATA_comments.txt` contains the original subsetting/processing commands from the Google Font Directory workflow.

### Config YAML Assessment

No `config.yaml` exists. The only source format is VFB (proprietary FontLab Studio), which is not compatible with gftools-builder. Creating an override config.yaml is not possible without converting the sources to a modern format first.

## Conclusion

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/galindo"
  commit: "dc5fea52318d56672b1e3f000851806c8b5bd2cc"
}
```

**Status**: no_config_possible

**Notes**: This is a legacy font from the original Google Font Directory era. The `librefonts/galindo` repo is an archive containing VFB sources that are not compatible with gftools-builder. The single commit in the repo predates the google/fonts initial commit. No config.yaml can be created without first converting the sources to a modern format (UFO, .glyphs, or .designspace).
