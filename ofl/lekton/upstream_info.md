# Investigation: Lekton

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lekton |
| Slug | lekton |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Lekton contains no `source { }` block at all — no `repository_url`, no commit hash, no config path.

The google/fonts git history for `ofl/lekton/Lekton-Regular.ttf` shows only:
- `90abd17b4` — "Initial commit" (original onboarding, pre-dating gftools-packager)

The designer is listed as "ISIA Urbino" (Istituto Superiore per le Industrie Artistiche, Urbino — an Italian design school). The OFL copyright states: `Copyright (c) 2008, 2009, 2010, Accademia di Belle Arti di Urbino (luciano.perondi@isiaurbino.net)`. The font is attributed to the academic institution rather than an individual designer.

No upstream repository for this font was found in `upstream_repos/fontc_crater_cache/`.

## Conclusion

No source block exists and no upstream repository was found. Lekton was created by ISIA Urbino (an Italian design institution) and was part of the initial google/fonts batch before source tracking was in place. Finding an upstream repository would require contacting the institution or searching for any archival hosting. Status is `missing_url`.
