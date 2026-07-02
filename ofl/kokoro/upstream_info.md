# Investigation: Kokoro

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kokoro |
| Slug | kokoro |
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

The `google/fonts/ofl/kokoro/` directory exists but contains no `METADATA.pb` file. The directory contains:
- `DESCRIPTION.en_us.html`
- `Kokoro-Regular.ttf`
- `OFL.txt`

The absence of an `EARLY_ACCESS.category` file and the minimal directory contents suggest this is an early access font not fully integrated into the catalog.

According to the DESCRIPTION.en_us.html, the font is "Kokoro Mincho (こころ明朝)" from the typingart account (twitter.com/typingart). The description notes it has "231 glyphs" and that the upstream project includes Kanji, Latin and other glyphs from IPA fonts (removed from this version).

No upstream GitHub repository for typingart/kokoro was found in the fontc_crater_cache.

## Conclusion

This font is in early access status with no METADATA.pb and no known upstream repository. The designer uses the Twitter handle @typingart. No further investigation is possible without locating the upstream source repository.
