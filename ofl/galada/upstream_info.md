# Investigation Report: Galada

## Summary

Galada is a Bengali and Latin display font derived from the Lobster typeface, developed by Black Foundry (Jeremie Hornus, Yoann Minet, Juan Bruce). It was onboarded to Google Fonts on 2017-08-07 via PR #996 by Marc Foley. The upstream repository is `BlackFoundryCom/Galada` (previously referenced as `TypefactoryNet/Galada` in the DESCRIPTION). The repo has UFO sources and a custom `build.py` script but no `config.yaml` for gftools-builder. An override config.yaml can be created.

## Key Findings

| Field             | Value                                                    |
|-------------------|----------------------------------------------------------|
| Family Name       | Galada                                                   |
| Repository URL    | https://github.com/BlackFoundryCom/Galada                |
| Commit Hash       | ee2fe5b461b2af0ade8952a7d4150958689433b4                 |
| Config YAML       | None (needs override)                                    |
| Source Type        | UFO (master/Galada.ufo)                                  |
| Status            | missing_config                                           |
| Confidence        | MEDIUM                                                   |
| Date Added        | 2016-06-20 (metadata), 2017-08-07 (actual onboarding)   |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb has no `source { }` block. The font is listed with designer "Black Foundry" and copyright attributing Pablo Impallari and Black Foundry. No `repository_url` is set.

### Git History in google/fonts

- **a98b83a29** (2017-08-07): "hotfix-galada: v1.261 added (#996)" by Marc Foley - Initial onboarding of the font. Added DESCRIPTION.en_us.html, Galada-Regular.ttf (187,776 bytes), METADATA.pb, and OFL.txt.
- **88ec41468** (2021-03-22): "Galada: Multiple designers fixed (#3229)" by Rosalie Wagner - Only updated METADATA.pb designer field.
- **76adaf1d2**: Deploy commit (no font changes).

The font binary has never been updated since the initial onboarding.

### PR #996 Analysis

PR #996 was created by Marc Foley (m4rc1e) and merged by Dave Crossland on 2017-08-07. The PR body was empty, with no comments or reviews. The title indicates "v1.261 added" as a hotfix.

### Upstream Repository

The DESCRIPTION.en_us.html references `https://github.com/TypefactoryNet/Galada`, which now resolves to `https://github.com/BlackFoundryCom/Galada` (GitHub organization rename/transfer).

The repo was created on 2015-06-30 and last pushed on 2018-05-18. It contains a single squashed commit:

- **ee2fe5b** (2018-04-10): "fix inversion of conjuncts bn_h_na and bn_h_nna" by Jeremie Hornus - This is the only commit and appears to be a squashed initial push that includes all project files.

**Timeline anomaly**: The repo's only commit (2018-04-10) postdates the Google Fonts onboarding (2017-08-07). This means either: (1) the repo history was squashed after onboarding, or (2) the font was built from a private version of the repo before it was made public. Since there is only one commit, `ee2fe5b` is the only available hash.

### Source Files

The repo contains UFO sources in multiple locations:
- `master/Galada.ufo` - Main mastering source
- `UFO/Design/Galada.ufo` - Design source
- `UFO/Original/Lobster.ufo` - Original Lobster reference
- `UFO/Mastering/PS/Galada.ufo` - PostScript mastering
- `UFO/Mastering/TT/Galada.ufo` - TrueType mastering

A custom `master/build.py` exists that generates OTF using `makeotf`. The `build/` directory contains both `Galada.otf` and `Galada.ttf`, but the TTF in the repo (229,000 bytes) does not match the one on Google Fonts (187,776 bytes).

### Binary Comparison

- Google Fonts TTF: 187,776 bytes (SHA256 prefix: acc22b41ee470dc5)
- Upstream repo build/Galada.ttf: 229,000 bytes (SHA256 prefix: a1d2104e874c1011)

The files do not match. The Google Fonts version was likely compiled through a different process or from a different state of the sources.

### Config YAML Assessment

No `config.yaml` exists in the repo. The repo uses a custom `build.py` script with `makeotf`. A gftools-builder override config.yaml could be created referencing the `master/Galada.ufo` source.

## Conclusion

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/BlackFoundryCom/Galada"
  commit: "ee2fe5b461b2af0ade8952a7d4150958689433b4"
}
```

**Status**: missing_config

**Notes**: The repo has only a single commit which postdates the Google Fonts onboarding. The binary in the repo does not match the one on Google Fonts, suggesting the font was compiled through a separate process. An override config.yaml could be created for gftools-builder using the `master/Galada.ufo` source, but the build may not reproduce the exact binary currently on Google Fonts. The DESCRIPTION.en_us.html references the old TypefactoryNet/Galada URL which now redirects to BlackFoundryCom/Galada.
