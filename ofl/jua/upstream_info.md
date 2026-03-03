# Investigation: Jua

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jua |
| Slug | jua |
| License Dir | ofl |
| Repository URL | https://github.com/baemin/Jua (unverified) |
| Commit Hash | eee0159e73c39bd804c275ca49376994d27e4e62 (unverified) |
| Config YAML | unknown |
| Status | missing_config |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Jua has no source block at all. The font was added to google/fonts as part of commit `16680f868` ("korean families r01: added (#1459)") on 2018-03-13, authored by Marc Foley. A subsequent hotfix was applied on 2024-01-19 in commit `c6f978399` ("Hotfixed space & nbspace chars") by Yanone, which updated the TTF binary.

The copyright string in the font reads: "Copyright 2018 The BM JUA Project Authors". "BM JUA" refers to Baemin Jua (배민 주아), a typeface produced by Woowahan Brothers (우아한형제들), the company behind the Baemin food delivery app in South Korea. No GitHub URL or upstream repository reference appears in the OFL.txt, DESCRIPTION.en_us.html, or any commit message.

The Jua family directory in google/fonts contains only:
- `Jua-Regular.ttf`
- `METADATA.pb`
- `OFL.txt`
- `DESCRIPTION.en_us.html`

No override `config.yaml` is present in the google/fonts directory.

The tracking file `data/gfonts_library_sources.json` records `https://github.com/baemin/Jua` as the repository URL with commit `eee0159e73c39bd804c275ca49376994d27e4e62`, and notes "No buildable source files at recorded commit". However, this repository was not found in the local cache at `upstream_repos/fontc_crater_cache/` — no "baemin" organization or "Jua" repository is cached, so the URL could not be independently verified.

No override `config.yaml` is present in the google/fonts directory. The METADATA.pb has no source block.

## Conclusion

The tracking JSON records an upstream repository at `https://github.com/baemin/Jua` with commit `eee0159e73c39bd804c275ca49376994d27e4e62`, but this could not be verified as the repo is not in the local cache. The status is `missing_config` because even if the repository URL and commit are correct, the source format is reportedly not gftools-builder compatible (no buildable source files). An override `config.yaml` may be needed if compatible sources can be identified. Further investigation is required to verify the repository URL and determine if buildable sources exist.
