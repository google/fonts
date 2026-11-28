# Investigation Report: Henny Penny

## Summary

Henny Penny is a static display typeface designed by Olga Umpeleva for Brownfox. It was part of the initial google/fonts repository commit in 2015. The upstream repository at `librefonts/hennypenny` contains only VFB (FontLab) source files and TTX decompositions -- no gftools-builder-compatible sources (.glyphs, .ufo, .designspace). A config.yaml cannot be created because the sources are not in a format that gftools-builder can process.

## Key Findings

| Field               | Value |
|---------------------|-------|
| **Family Name**     | Henny Penny |
| **Designer**        | Brownfox (Olga Umpeleva) |
| **Repository URL**  | https://github.com/librefonts/hennypenny |
| **Commit Hash**     | `4847dd1836a19c92e496eac373770f0d09743c49` |
| **Config YAML**     | none (VFB-only sources) |
| **Branch**          | `master` |
| **Status**          | **no_config_possible** |
| **Confidence**      | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/hennypenny/METADATA.pb` contains a minimal source block (added in commit `9a14639f3` on 2026-02-25):
```
source {
  repository_url: "https://github.com/librefonts/hennypenny"
  commit: "4847dd1836a19c92e496eac373770f0d09743c49"
}
```

No config_yaml, no file mappings, no branch field. The font has no axes (static, single weight).

### Git History in google/fonts

The font binary (`HennyPenny-Regular.ttf`) has only been touched twice:
1. `90abd17b4` (2015-03-07): Initial commit -- bulk import of all fonts into the repository
2. `76adaf1d2` (2021-11-01): A deploy commit that actually deleted some files (DESCRIPTION, FONTLOG) and restructured the repository

The font has never been updated via gftools-packager. It was part of the original Google Fonts collection.

### Upstream Repository Verification

The cached repository at `fontc_crater_cache/librefonts/hennypenny/` has been verified:
- Remote: `https://github.com/librefonts/hennypenny`
- Current branch: `master`
- The repository has exactly one commit: `4847dd1836a19c92e496eac373770f0d09743c49` ("update .travis.yml", dated 2014-10-17)
- Author: hash3g (hash.3g@gmail.com)

This is a `librefonts` mirror repository -- a common pattern for early Google Fonts families where the original sources were archived in the librefonts GitHub organization. The single commit contains the entire project.

### Source Files

The repository contains only legacy source formats:
- `src/HennyPenny-Regular-TTF.vfb` -- FontLab VFB source (TrueType outlines)
- `src/HennyPenny-Regular-OTF.vfb` -- FontLab VFB source (CFF outlines)
- Various `.ttx` decompositions of the compiled TTF and OTF fonts
- `METADATA.json`, `OFL.txt`, `FONTLOG.txt`

There are **no** gftools-builder-compatible source files:
- No `.glyphs` files
- No `.ufo` directories
- No `.designspace` files
- No `config.yaml`

VFB is a proprietary FontLab format that cannot be processed by gftools-builder. Creating an override config.yaml is not possible without first converting the sources to a supported format.

### Onboarding Timeline

- 2012-02-22: Date added to Google Fonts catalog (per METADATA.pb)
- 2014-10-17: Source repo created/archived at librefonts/hennypenny
- 2015-03-07: Font included in initial commit of google/fonts repository
- 2021-11-01: Repository restructuring (deploy commit)
- 2026-02-25: Source block added to METADATA.pb with repo URL and commit hash

### Font Copyright

From the font binary:
```
Copyright (c) 2012, Brownfox (gayaneh.b@gmail.com), with Reserved Font Name "Henny Penny"
```

The FONTLOG credits:
- Olga Umpeleva -- Designer
- Gayaneh Bagdasaryan -- Type consultant (Brownfox)
- Igino Marini -- Spacing and Kerning

## Conclusion

The source block in METADATA.pb correctly identifies the upstream repository and commit. However, no config.yaml can be created because the upstream repository only contains VFB (FontLab) source files, which are not compatible with gftools-builder. The font would need source conversion (VFB to .glyphs or .ufo) before a build configuration could be established. The status is `no_config_possible`.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/hennypenny"
  commit: "4847dd1836a19c92e496eac373770f0d09743c49"
}
```

No additional fields are recommended -- the VFB-only sources prevent config_yaml specification and meaningful file mappings.
