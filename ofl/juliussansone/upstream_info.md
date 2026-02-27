# Investigation: Julius Sans One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Julius Sans One |
| Slug | julius-sans-one |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/juliussansone |
| Commit Hash | 8aadb0e8d6ef7f45aa2844ccd99f7e28f0cd1498 |
| Config YAML | none (OTF-only sources in librefonts mirror) |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Julius Sans One has no source block. The font was designed by Luciano Vergara from the Chilean type foundry LatinoType.

The git history in google/fonts shows the font was present since the initial commit (`90abd17b4`) and was updated in commit `7a00bf8ff` ("Updating Julius Sans One") on 2015-04-20 by Dave Crossland, which applied ttfautohint 1.3 and minor fixes. The copyright notice reads: "Copyright (c) 2012, LatinoType (luciano@latinotype.com), with Reserved Font Names 'Julius'".

The DESCRIPTION.en_us.html mentions LatinoType's website `http://www.latinotype.com` but no GitHub repository URL. No override `config.yaml` exists in the google/fonts `ofl/juliussansone/` directory.

A `librefonts` mirror of Julius Sans One exists in the cache at `upstream_repos/fontc_crater_cache/librefonts/juliussansone/`. This contains TTX-decompiled OTF files and a `src/` directory with more TTX files. No Glyphs, UFO, or other gftools-builder compatible sources are present. The commit `8aadb0e8d6ef7f45aa2844ccd99f7e28f0cd1498` is the recorded commit in the tracking JSON.

This means the `librefonts/juliussansone` mirror is the only known upstream reference, but it contains only decompiled font files (TTX format), not editable source files. No gftools-builder compatible sources are available.

The font file structure in google/fonts contains only:
- `JuliusSansOne-Regular.ttf`
- `METADATA.pb`
- `OFL.txt`
- `DESCRIPTION.en_us.html`

No override `config.yaml` exists in the google/fonts directory.

## Conclusion

Julius Sans One has a librefonts mirror at `https://github.com/librefonts/juliussansone` with commit `8aadb0e8d6ef7f45aa2844ccd99f7e28f0cd1498`. The librefonts mirror contains only TTX-decompiled OTF files — no gftools-builder compatible sources. No `config.yaml` can be created without first identifying and converting original source files. Status: no_config_possible.
