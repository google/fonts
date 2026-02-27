# Investigation: Just Another Hand

## Summary

| Field | Value |
|-------|-------|
| Family Name | Just Another Hand |
| Slug | just-another-hand |
| License Dir | apache |
| Repository URL | https://github.com/librefonts/justanotherhand |
| Commit Hash | unknown |
| Config YAML | none (VFB-only sources in librefonts mirror) |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Just Another Hand has no source block. The font is under an Apache 2.0 license (not OFL) and is located at `apache/justanotherhand/`. It was designed by Brian J. Bonislawsky DBA Astigmatic (AOETI).

The git history in google/fonts shows:
- Initial commit `90abd17b4` (earliest record)
- Hotfix `a7995c748` ("hotfix-justanotherhand: v1.001 added (#778)") on 2017-08-07 by Marc Foley, which renamed the TTF file from `JustAnotherHand.ttf` to `JustAnotherHand-Regular.ttf` and fixed copyright strings

The copyright in the font reads: "Copyright (c) 2010 by Brian J. Bonislawsky DBA Astigmatic (AOETI). All rights reserved. Available under the Apache 2.0 licence."

The DESCRIPTION.en_us.html describes the font as a narrow brush-drawn handwriting font but contains no URL to an upstream repository. No override `config.yaml` exists in the google/fonts `apache/justanotherhand/` directory.

A `librefonts` mirror of Just Another Hand exists in the cache at `upstream_repos/fontc_crater_cache/librefonts/justanotherhand/`. The latest commit is `151e64a` ("update .travis.yml"). The `src/` directory contains:
- `JustAnotherHand.vfb` — a FontLab VFB source file
- `METADATA_comments.txt`
- `VERSIONS.txt`

The VFB format (FontLab) is not compatible with gftools-builder. The librefonts mirror also contains TTX-decompiled TTF files of the font.

Note: This family is under Apache 2.0 license, located in the `apache/justanotherhand/` directory (not `ofl/`). The `data/gfonts_library_sources.json` tracking file does not include Apache-licensed families, so Just Another Hand is not tracked there.

The font file structure in google/fonts contains only:
- `JustAnotherHand-Regular.ttf`
- `METADATA.pb`
- `LICENSE.txt`
- `DESCRIPTION.en_us.html`

No override `config.yaml` exists in the google/fonts directory.

## Conclusion

Just Another Hand has a librefonts mirror at `https://github.com/librefonts/justanotherhand`. The only available source format is FontLab VFB, which is not compatible with gftools-builder. No `config.yaml` can be created without first converting sources. The family is Apache-licensed and not currently tracked in the gfonts_library_sources.json file. Status: no_config_possible.
