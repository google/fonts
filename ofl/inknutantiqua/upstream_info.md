# Investigation: Inknut Antiqua

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inknut Antiqua |
| Slug | inknut-antiqua |
| License Dir | ofl |
| Repository URL | https://github.com/clauseggers/Inknut-Antiqua |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/clauseggers/Inknut-Antiqua"
}
```

## Investigation

The METADATA.pb for Inknut Antiqua (at `google/fonts/ofl/inknutantiqua/METADATA.pb`) contains a partial source block with only `repository_url` — no `commit` and no `config_yaml`.

The `repository_url` field was added to METADATA.pb by Simon Cozens in commit `21e98aac8` on 2024-01-14 ("More upstreams (i,j,k)"), alongside several other families.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/clauseggers/Inknut-Antiqua/`. The repository structure is:
- `Inknut Antiqua uprights.glyphs` — a `.glyphs` source file at the repo root
- `UFOs/` — contains `Inknut Antiqua-Regular.ufo` and `Inknut Antiqua-Bold.ufo`
- `Inknut Antiqua LATIN ONLY/Inknut Antiqua uprights 124 LATIN ONLY.glyphs`
- `TTF-OTF/` — compiled TTF/OTF files
- `OFL.txt`, `README.md`, and other assets

The repository has a `.glyphs` source file, which is gftools-builder-compatible, but no `config.yaml` exists anywhere in the repository.

**Google/fonts history for Inknut Antiqua:**
- Initial commit `90abd17b4` (2015-03-07): Initial add
- `a1eda398f` (2015-05-20): "Updating Inknut Antiqua" — updated all TTF files
- `afd76e905` (2017-05-08): "hotfix-inknutantiqua: v1.003 added" — TTF files updated (PR #895)
- `fab83f4be` (2020-10-08): "HindGuntur, InknutAntiqua, Khula, Padauk Hinting (#2378)" — re-hinted TTFs

The upstream repo commit history shows the most recent activity is `91d14bf032cc0b44360a5adf56f3af16639786c7` (2026-01-02, "Fix image link for Inknut Antiqua specimen"), with most font development activity clustered in 2014-2015.

Given the last substantive font file update in google/fonts was the hinting PR in October 2020, and that PR operated on the TTF files directly (not from upstream source), the correct onboarding commit is unclear. The fonts in google/fonts were likely derived from an early upstream commit (2014-2015), but cross-referencing the exact commit requires comparing binary file properties. The HEAD commit of the upstream is `91d14bf032cc0b44360a5adf56f3af16639786c7` (January 2026).

An override `config.yaml` in the google/fonts family directory could reference the `.glyphs` source for potential rebuilds, but the correct commit hash needs to be identified first.

## Conclusion

The source block for Inknut Antiqua is incomplete: it has `repository_url` but is missing both `commit` and `config_yaml`. The upstream repository has `.glyphs` source files but no `config.yaml`. Status: `missing_commit`. Actions needed: (1) identify the correct upstream commit corresponding to the current binary files in google/fonts; (2) create an override `config.yaml` in the google/fonts directory referencing `Inknut Antiqua uprights.glyphs`.

## Commit Added (HIGH confidence)

Commit `9db4a5c235ef042adbc0da37fcf3dda3ffe59201` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2020-10-08). This is the most reliable method.
