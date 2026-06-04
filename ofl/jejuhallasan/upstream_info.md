# Investigation: Jeju Hallasan

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jeju Hallasan |
| Slug | jeju-hallasan |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `ofl/jejuhallasan/` directory in google/fonts contains only `DESCRIPTION.en_us.html`, `EARLY_ACCESS.category`, `JejuHallasan-Regular.ttf`, and `OFL.txt`. There is no `METADATA.pb` file.

The font was added in the initial commit to google/fonts (`90abd17b4`, "Initial commit", 2015-03-07 by Dave Crossland). No subsequent updates have been made.

The OFL copyright reads: "Copyright 2014 Jeju Special Self-Governing Province (jmg0987@korea.kr), with Reserved Font Name 'Jeju Hallasan, 'Jeju Gothic, 'Jeju Myeongjo'." All three Jeju fonts (Gothic, Hallasan, Myeongjo) share the same copyright holder: Jeju Special Self-Governing Province, a Korean government body.

The `EARLY_ACCESS.category` file marks this as an early access font. The font name refers to Mt. Hallasan, a volcano on Jeju Island (UNESCO World Natural Heritage Site). No upstream repository URL is referenced anywhere in the directory.

No upstream repository for this family was found in the cache at `upstream_repos/fontc_crater_cache/`.

## Conclusion

No METADATA.pb exists and no upstream repository URL is known. The font is from a Korean government body (Jeju Special Self-Governing Province). It shares the same copyright and source context as Jeju Gothic and Jeju Myeongjo. An upstream repository may not be publicly accessible. Further investigation is needed to identify an upstream source.
