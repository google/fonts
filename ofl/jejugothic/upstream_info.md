# Investigation: Jeju Gothic

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jeju Gothic |
| Slug | jeju-gothic |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `ofl/jejugothic/` directory in google/fonts contains only `DESCRIPTION.en_us.html`, `EARLY_ACCESS.category`, `JejuGothic-Regular.ttf`, and `OFL.txt`. There is no `METADATA.pb` file.

The font was added in the initial commit to google/fonts (`90abd17b4`, "Initial commit", 2015-03-07 by Dave Crossland). No subsequent updates have been made.

The OFL copyright reads: "Copyright 2014 Jeju Special Self-Governing Province (jmg0987@korea.kr), with Reserved Font Name 'Jeju Hallasan, 'Jeju Gothic, 'Jeju Myeongjo'." The font is published by a Korean government entity (Jeju Province).

The `EARLY_ACCESS.category` file contains "Sans Serif", marking it as an early access font. No upstream repository URL is referenced anywhere in the directory.

No upstream repository for this family was found in the cache at `upstream_repos/fontc_crater_cache/`.

## Conclusion

No METADATA.pb exists and no upstream repository URL is known. The font is from a Korean government body (Jeju Special Self-Governing Province). An upstream repository may exist on a Korean government server or the fonts may have been delivered directly without a publicly accessible git repository. Further investigation is needed to identify an upstream source.
