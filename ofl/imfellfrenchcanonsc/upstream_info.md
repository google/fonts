# Investigation: IM Fell French Canon SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | IM Fell French Canon SC |
| Slug | im-fell-french-canon-sc |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/imfellfrenchcanonsc |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for IM Fell French Canon SC (at `google/fonts/ofl/imfellfrenchcanonsc/METADATA.pb`) contains no source block. The family was added in the initial commit to google/fonts (commit `90abd17b4`, dated 2015-03-07 by Dave Crossland).

The upstream repository was identified as `https://github.com/librefonts/imfellfrenchcanonsc` (confirmed by examining the cached repo at `upstream_repos/fontc_crater_cache/librefonts/imfellfrenchcanonsc/`).

The librefonts/imfellfrenchcanonsc repository contains only TTX-decompiled font files:
- `IMFeFCsc28P.ttf.ttx` (and split per-table `.ttx` files)

There are no gftools-builder-compatible sources (no `.glyphs`, `.ufo`, or `.designspace` files). The `src/` directory contains only `METADATA_comments.txt` and `VERSIONS.txt`. The SC (Small Caps) variant is a companion to IM Fell French Canon, designed by Igino Marini.

The HEAD commit of the upstream repo is `e7117aa9c7faa9e456fea0ec4806c284a21b54fd` (message: "update .travis.yml").

Because the upstream repository only contains TTX decompiled sources and no gftools-builder-compatible source files, it is not possible to add a meaningful `config_yaml` for automated rebuilds.

## Conclusion

No source block can be completed for IM Fell French Canon SC. The upstream repository (`librefonts/imfellfrenchcanonsc`) only contains TTX-decompiled sources. Status: `no_config_possible`. A source block with `repository_url` only could be added to document the upstream location, but no `config_yaml` is available.
