# Investigation: Junge

## Summary

| Field | Value |
|-------|-------|
| Family Name | Junge |
| Slug | junge |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/junge |
| Commit Hash | 1753e7a229f48ac314ad3c54da9fcfb2d7946f75 |
| Config YAML | none (OTF-only sources in librefonts mirror) |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Junge has no source block. The font was designed by Alexei Vanyashin for Cyreal, as noted in the copyright string: "Copyright (c) 2011, Cyreal (www.cyreal.org a@cyreal.org) with Reserved Font Name 'Junge'."

The git history in google/fonts shows the font has been present since the initial commit (`90abd17b4`), with only metadata-level changes (language fields, stroke/classifications) since then. No font binary update has occurred since initial onboarding.

The DESCRIPTION.en_us.html credits Alexei Vanyashin (`@avanyashin` on Twitter) as the designer. No GitHub repository is mentioned. No override `config.yaml` exists in the google/fonts `ofl/junge/` directory.

Searching the upstream cache at `upstream_repos/fontc_crater_cache/cyrealtype/` shows many Cyreal-maintained fonts (Adamina, Alice, Alike, Lora, etc.) but no Junge repository.

A `librefonts` mirror of Junge exists in the cache at `upstream_repos/fontc_crater_cache/librefonts/junge/`. This contains TTX-decompiled OTF files and a `src/` directory with more TTX files. No Glyphs, UFO, or other gftools-builder compatible sources are present. The commit `1753e7a229f48ac314ad3c54da9fcfb2d7946f75` is the recorded commit in the tracking JSON.

The font directory in google/fonts contains only:
- `Junge-Regular.ttf`
- `METADATA.pb`
- `OFL.txt`
- `DESCRIPTION.en_us.html`
- `FONTLOG.txt`

No override `config.yaml` exists in the google/fonts directory.

## Conclusion

Junge has a librefonts mirror at `https://github.com/librefonts/junge` with commit `1753e7a229f48ac314ad3c54da9fcfb2d7946f75`. The librefonts mirror contains only TTX-decompiled OTF files — no gftools-builder compatible sources. No `config.yaml` can be created without first identifying original editable source files from Cyreal. Status: no_config_possible.
