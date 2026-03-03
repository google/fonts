# Investigation: Leckerli One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Leckerli One |
| Slug | leckerli-one |
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

The METADATA.pb for Leckerli One contains no `source { }` block at all — no `repository_url`, no commit hash, no config path.

The google/fonts git history for `ofl/leckerlione/LeckerliOne-Regular.ttf` shows only:
- `90abd17b4` — "Initial commit" (original onboarding, pre-dating gftools-packager)

The designer is listed as "Gesine Todt" and the copyright references `www.gesine-todt.de`. The OFL copyright string mentions "hallo@gesine-todt.de" and a reserved font name "Leckerli". No GitHub repository URL is referenced in the font files.

The FONTLOG.txt contains basic font information but no upstream repository reference.

No upstream repository for this font was found in `upstream_repos/fontc_crater_cache/`.

## Conclusion

No source block exists and no upstream repository was found. The font was onboarded in the initial google/fonts commit before gftools-packager was in use. The designer Gesine Todt may need to be contacted or their GitHub profile searched to find if sources were ever published. Status is `missing_url`.
