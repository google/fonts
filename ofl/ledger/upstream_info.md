# Investigation: Ledger

## Summary

| Field | Value |
|-------|-------|
| Family Name | Ledger |
| Slug | ledger |
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

The METADATA.pb for Ledger contains no `source { }` block at all — no `repository_url`, no commit hash, no config path.

The google/fonts git history for `ofl/ledger/Ledger-Regular.ttf` shows:
- `f8265bddf` — "ledger: v1.003 added (#2514)"
- `0436d99c0` — "ledger: fixed nbsp width (#2353)"
- `90abd17b4` — "Initial commit" (original onboarding)

The commit body for `f8265bddf` was checked but contains no upstream repository reference.

The OFL copyright states: `Copyright (c) 2011, Denis Masharov <denis.masharov@gmail.com>`. The designer is Denis Masharov. No GitHub repository URL is referenced in the font files.

No upstream repository for this font was found in `upstream_repos/fontc_crater_cache/`.

## Conclusion

No source block exists and no upstream repository was found. The font has been updated multiple times in google/fonts but the source repository was never documented. Denis Masharov would need to be contacted or searched for to find if sources were published. Status is `missing_url`.
