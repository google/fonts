# Investigation: Lato

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lato |
| Slug | lato |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/LatoGFVersion |
| Commit Hash | unknown |
| Config YAML | none |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/LatoGFVersion"
}
```

## Investigation

The METADATA.pb has a `repository_url` pointing to `https://github.com/googlefonts/LatoGFVersion` but no commit hash.

The google/fonts git history for `ofl/lato/Lato-Regular.ttf` shows:
- `f3b885d55` — "lato: v2.015 added (#479)" — 2016-12-02

The commit body for `f3b885d55` references: "Version 2.015 release for Google Fonts. These fonts have been hot fixed from the original sources. The hot fix source repository is here https://github.com/googlefonts/LatoGFVersion"

The upstream repo at `upstream_repos/fontc_crater_cache/googlefonts/LatoGFVersion/` was last updated on 2016-11-28 with commit `080cb69` ("fonts: regenerated"). This is almost certainly the commit used for the onboarding (matching the timing).

The LatoGFVersion repo structure:
- `build/` — build scripts (shell, Python)
- `fonts/` — output fonts directory
- `src/` — prebuilt TTF source files

This repo contains prebuilt TTF files in `src/` rather than design-time sources. There is no `config.yaml` for gftools-builder.

## Conclusion

The repository URL is present but the commit hash is missing. The most likely onboarding commit is `080cb69` ("fonts: regenerated", 2016-11-28), which is the HEAD of the LatoGFVersion repo at the time of the google/fonts addition. However, the source contains only prebuilt TTF files and custom shell/Python build scripts — no gftools-builder compatible sources. No `config.yaml` is possible without proper design sources.

## Commit Added (MEDIUM confidence)

Commit `080cb69711ca050d91e9c866e58df7a73095c69a` was determined by **date_correlation**. Found the latest upstream commit before the binary modification date in google/fonts (2016-12-02). This assumes the upstream HEAD at onboarding time was the commit used.
