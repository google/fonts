# Investigation Report: Gorditas

## Summary

Gorditas is a display slab-serif family designed by Gustavo Dipre, first added to Google Fonts on 2012-03-14. The upstream repository is at `https://github.com/librefonts/gorditas`. The repo contains only VFB (FontLab) and TTX source files -- no gftools-buildable sources (.glyphs, .ufo, .designspace) and no config.yaml. There is only a single commit in the upstream repo. Building with gftools-builder is not possible without a source format conversion.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Gorditas |
| Repository URL    | https://github.com/librefonts/gorditas |
| Commit Hash       | `2212c0647e87c13121e408ee446dffe924792ac1` |
| Config YAML       | None (VFB-only sources, not gftools-buildable) |
| Source Files      | `src/Gorditas-Regular-TTF.vfb`, `src/Gorditas-Bold-TTF.vfb`, plus TTX decompositions |
| Status            | **no_config_possible** |
| Confidence        | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb on main has NO source block. A source block with `repository_url` and `commit` was added on the `sources_info_2026-02-25` branch (commit `9a14639f3c6d`) but has not been merged to main yet.

### Git History in google/fonts

- `90abd17b4` (2015-03-07): Initial commit (repository creation, Gorditas included from the start).
- `76adaf1d2` (2021-11-01): Deploy commit that included Gorditas file changes (deletion/restructuring). This is the only commit that modified the TTF files after the initial import.
- No gftools-packager or onboarding-style commit message exists; this font predates the modern onboarding workflow.

### Upstream Repository Verification

The upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/gorditas/`. Findings:
- Remote URL confirmed: `https://github.com/librefonts/gorditas`
- The repo has exactly ONE commit: `2212c06` ("update .travis.yml", 2014-10-17).
- Source files in `src/` directory:
  - `Gorditas-Regular-OTF.vfb` and `Gorditas-Bold-OTF.vfb` (OTF FontLab sources)
  - `Gorditas-Regular-TTF.vfb` and `Gorditas-Bold-TTF.vfb` (TTF FontLab sources)
  - TTX decompositions of OTF files
  - `VERSIONS.txt` and `METADATA_comments.txt`
- Root directory contains TTX decompositions of TTF files.
- NO `.glyphs`, `.ufo`, `.designspace`, or `config.yaml` / `config.yml` files anywhere.
- No SFD files either.

### Source Format Assessment

VFB (FontLab 5) is a proprietary binary format that is NOT supported by gftools-builder or fontc. To build this font from source, the VFB files would need to be converted to a modern format (e.g., .glyphs or .ufo), which is outside the scope of metadata enrichment.

### Commit Hash Verification

With only a single commit (`2212c06`) in the upstream repo, dated 2014-10-17, this must be the commit that corresponds to the font files in google/fonts. The font was part of google/fonts from the initial commit (2015-03-07), consistent with the upstream repo predating the google/fonts repository.

## Conclusion

Gorditas has a valid upstream repository at `https://github.com/librefonts/gorditas` with a single commit. The sources are in VFB format (FontLab 5 proprietary), which is not buildable by gftools-builder. No config.yaml exists and none can be created without first converting the sources to a modern format.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/gorditas"
  commit: "2212c0647e87c13121e408ee446dffe924792ac1"
}
```

**Status**: no_config_possible
**Confidence**: HIGH
