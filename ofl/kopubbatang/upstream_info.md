# Investigation: KoPub Batang

## Summary

| Field | Value |
|-------|-------|
| Family Name | KoPub Batang |
| Slug | ko-pub-batang |
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

The `google/fonts/ofl/kopubbatang/` directory exists but contains no `METADATA.pb` file. The directory contains:
- `DESCRIPTION.en_us.html`
- `EARLY_ACCESS.category` (contains "Serif")
- `KoPubBatang-Bold.ttf`
- `KoPubBatang-Light.ttf`
- `KoPubBatang-Regular.ttf`
- `OFL.txt`

The presence of `EARLY_ACCESS.category` indicates this font is in an early access/sandboxed state, not yet fully part of the public Google Fonts catalog with full metadata tracking.

According to the DESCRIPTION.en_us.html, the font was designed by Fontrix, sponsored by Korea's Ministry of Culture, Sports and Tourism, and published by the Korea Publishers Society. It supports 11,172 Hangul glyphs plus Chinese, English and KS symbols.

No upstream GitHub repository was found in the cache.

## Conclusion

This font is in early access status with no METADATA.pb and no known upstream repository. It is a government-sponsored Korean font and the source files may not be publicly available on GitHub. No further investigation is possible without locating the upstream source repository or making contact with the Korea Publishers Society or Fontrix.
