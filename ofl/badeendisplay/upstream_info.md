# Badeen Display

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Designer**: Hani Alasadi (Hani Adnan Abdulamir)
- **Primary Script**: Arabic

## Source Data

| Field            | Value                                                        |
|------------------|--------------------------------------------------------------|
| repository_url   | https://github.com/haniadnansd/Badeen-Display                |
| commit           | c1370b602b4a9819c4ddce4af17962a42edb8bc3                     |
| config_yaml      | source/config.yaml                                           |
| branch           | main                                                         |
| date_added       | 2024-11-20                                                   |

## Repository URL Verification

The repository URL `https://github.com/haniadnansd/Badeen-Display` was confirmed valid. A cached clone existed at `upstream_repos/fontc_crater_cache/haniadnansd/Badeen-Display` with the remote origin matching the METADATA.pb `repository_url`. The issue #7814 on google/fonts, filed by haniadnansd (Hani Adnan Abdulamir), included the same repository URL in its body, confirming the designer submitted this repo for onboarding.

## Commit Hash Verification

The commit `c1370b602b4a9819c4ddce4af17962a42edb8bc3` was verified to exist in the upstream repository. It was authored on 2024-11-14 and contained a minor update to `DESCRIPTION.en_us.html`. This was the HEAD of the `main` branch (the latest commit in the repo) at the time of onboarding.

The onboarding commit in google/fonts (`c31eae585`, dated 2024-11-20) explicitly referenced this commit hash in its message: "Taken from the upstream repo https://github.com/haniadnansd/Badeen-Display at commit https://github.com/haniadnansd/Badeen-Display/commit/c1370b602b4a9819c4ddce4af17962a42edb8bc3". The font was merged via PR #8521 on 2024-11-25. No additional upstream commits were made between the referenced commit (Nov 14) and the merge date (Nov 25), confirming the commit hash is correct and was the latest available code at the time.

## Config Verification

The file `source/config.yaml` existed at the referenced commit with the following contents:

```yaml
sources:
    - BadeenDisplay.glyphs
```

This is a valid gftools-builder configuration referencing the Glyphs source file `BadeenDisplay.glyphs`, which was present in the same `source/` directory at the referenced commit. The `config_yaml` field in METADATA.pb correctly points to `source/config.yaml`. No override config.yaml was needed or present in the google/fonts family directory.

The config.yaml was originally added by Yanone (post@yanone.de) on 2024-10-23 with the message "Added rudimentary config.yaml" as part of the onboarding preparation via upstream PR #5.

## File Mapping

The METADATA.pb `source.files` block mapped three files from the upstream repo to the google/fonts family directory:

| Source (upstream)                        | Destination (google/fonts)         | Verified |
|------------------------------------------|------------------------------------|----------|
| OFL.txt                                  | OFL.txt                            | Yes      |
| fonts/ttf/BadeenDisplay-Regular.ttf      | BadeenDisplay-Regular.ttf          | Yes      |
| DESCRIPTION.en_us.html                   | DESCRIPTION.en_us.html             | Yes      |

All three source files were confirmed to exist at the referenced commit in the upstream repository.

## Onboarding History

1. **Issue #7814** was filed by haniadnansd requesting the addition of Badeen Display to Google Fonts.
2. Yanone (a font engineer) contributed to the upstream repo via PRs #5 and #7, adding config.yaml, improving glyphs, and creating the DESCRIPTION.
3. The font was onboarded via google/fonts PR #8521 (branch `gftools_packager_ofl_badeendisplay`), merged on 2024-11-25.
4. The onboarding commit `c31eae585` was dated 2024-11-20 with the message "Badeen Display: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added".
5. A subsequent sources info commit `c30e1a094` (2025-09-18) added the `source { }` block to METADATA.pb, referencing the same commit hash.

## Conclusion

All source metadata for Badeen Display was verified as complete and correct. The repository URL, commit hash, and config_yaml path in METADATA.pb accurately reflect the upstream state used for onboarding. No corrections were needed.
