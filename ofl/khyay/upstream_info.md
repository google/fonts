# Investigation: Khyay

## Summary

| Field | Value |
|-------|-------|
| Family Name | Khyay |
| Slug | khyay |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No METADATA.pb file (early access / sandboxed font)
```

## Investigation

The `google/fonts/ofl/khyay/` directory exists but contains no `METADATA.pb` file. The directory contains:
- `DESCRIPTION.en_us.html`
- `EARLY_ACCESS.category`
- `Khyay-Regular.ttf`
- `OFL.txt`

The presence of `EARLY_ACCESS.category` indicates this font is in an early access/sandboxed state.

According to the DESCRIPTION.en_us.html, Khyay is "a display Myanmar typeface and Unicode font" designed by Danh Hong (the same designer as Khmer, KohSantepheap, Koulen and other Khmer/Southeast Asian fonts). The description notes it "is harmonized with the latin typeface Montserrat."

No upstream GitHub repository for Khyay was found in the fontc_crater_cache.

## Conclusion

This font is in early access status with no METADATA.pb and no known upstream repository. While Danh Hong has active GitHub repositories (danhhong), no Khyay repository was found in the cache. This family needs further investigation to locate the upstream source repository.
