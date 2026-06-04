# Investigation: Hannari

## Summary

| Field | Value |
|-------|-------|
| Family Name | Hannari |
| Slug | hannari |
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

(No METADATA.pb exists for this family. It is an Early Access font.)

## Investigation

The family directory is at `ofl/hannari/` and contains:
- `Hannari-Regular.ttf`
- `DESCRIPTION.en_us.html`
- `OFL.txt`

(No `EARLY_ACCESS.category` file is present, unlike most other Early Access fonts.)

**No METADATA.pb exists.** This is an Early Access font that predates the modern METADATA.pb onboarding process.

### Git History

```
bf19077ad  2016-09-30  Add 8 Japanese fonts under OFL for Early Access
6bda16478             Format HTML with new html formatter
```

- **commit `bf19077ad`** (2016-09-30, Dave Crossland): Added as part of a batch of 8 Japanese fonts under OFL for Early Access. The commit included `Hannari-Regular.ttf`, `DESCRIPTION.en_us.html`, and `OFL.txt` for `ofl/hannari/`. Other fonts added in this same commit include Kokoro, M+ 1p, Nico Moji, Nikukyu, Rounded M+ 1c, Sawarabi Gothic, and Sawarabi Mincho.

### Creator Information

The `DESCRIPTION.en_us.html` states:
> "Hannari, from [typingart](https://twitter.com/typingart), is an original Kana design inspired by a historical design, Tsukiji."

It also notes:
> "The upstream project includes Kanji, Latin and other glyphs from the IPA fonts, which are removed from this font. Now released under the SIL Open Font License."

The designer is known by the Twitter handle **@typingart**. The font is a Japanese kana typeface inspired by Tsukiji-style typography.

The `OFL.txt` copyright line reads:
> "Copyright 2016 The Hannari Project Authors."

### Upstream Repository Search

No GitHub repository URL appears in any file within `ofl/hannari/`. The description links only to a Twitter profile (https://twitter.com/typingart), not a GitHub repository.

The note about the "upstream project" including IPA font glyphs (which were removed for the Google Fonts version) suggests there is a source repository, but it is not referenced in any google/fonts file.

The designer @typingart is **not** found in `upstream_repos/fontc_crater_cache/`.

### No config.yaml Known

The source format of the upstream project is unknown. Given that this is a Japanese kana font from 2016 with 230 glyphs (as stated in the description), it may have been created with a tool like Glyphs or FontForge.

## Conclusion

This Early Access Japanese kana font by designer @typingart has no documented upstream repository in google/fonts. The font was added in a batch of 8 Japanese fonts on 2016-09-30 with no reference to a source repository.

**Action needed**: Investigate whether @typingart has published a GitHub repository (search for "typingart" on GitHub). Alternatively, check if there is a sourceforge or other hosting for the original Hannari project. The description mentions the original project included additional glyphs from IPA fonts, suggesting a source file somewhere.

**Person to ask**: @typingart on Twitter/X, or Dave Crossland who performed the onboarding.
