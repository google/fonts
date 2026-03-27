# Investigation: Inria Serif

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inria Serif |
| Slug | inria-serif |
| License Dir | ofl |
| Repository URL | https://github.com/BlackFoundryCom/InriaFonts |
| Commit Hash | unknown |
| Config YAML | none (custom build scripts, no gftools-builder config) |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/BlackFoundryCom/InriaFonts"
}
```

## Investigation

The family was added to google/fonts on 2019-12-05 at 15:55 UTC+1 (commit `a2b3b38b97`), in PR #2272 by Yanone. The commit message is "Added Inria Serif 1.0".

The upstream repository at `https://github.com/BlackFoundryCom/InriaFonts` is cached at `upstream_repos/fontc_crater_cache/BlackFoundryCom/InriaFonts`. The repo contains UFO sources for both Inria Sans and Inria Serif under `masters/INRIA-SANS/` and `masters/INRIA-SERIF/`.

The upstream commit history around the onboarding date shows:
- `d13f0df3` — "Fresh Sans TTFs" — 2019-12-05 15:21 UTC+1 (by Yanone)
- `2bb3549c` — "Fresh Serif TTFs" — 2019-12-05 15:34 UTC+1 (by Yanone)
- `3accdda3` — "Bumped Inria Serif to Google Fonts specs" — 2019-12-05 15:33 UTC+1
- `94732c5a` — "Separate build scripts for each family" — 2019-12-05 15:41 UTC+1
- `8caa79ae` — "Merge pull request #8 from yanone/master" — 2019-12-06 11:19 UTC+1

Since google/fonts was updated at 15:55 and the last upstream commit before that is `94732c5a` at 15:41, the onboarding for Inria Serif was most likely from commit `94732c5a`. The serif-specific commit `2bb3549c` ("Fresh Serif TTFs") at 15:34 is also a candidate.

**Source format**: The repository uses `.ufo` files (UFO format), not `.glyphs` or `.designspace`. There is **no `config.yaml`** in the upstream repository. Build was done using a custom `build-sans.sh` / `build-serif.sh` shell script using `fontmake` directly.

The METADATA.pb currently has `repository_url` but no `commit` field. An override `config.yaml` would be needed since the upstream repo has no gftools-builder configuration.

Note: Inria Sans (PR #2273) and Inria Serif (PR #2272) were both contributed by Yanone at the same time. The upstream repo is shared (both families are in the same repository).

## Conclusion

The `repository_url` is present and correct. The `commit` field is missing. The upstream repository uses UFO sources but has no `config.yaml` — the build was done with custom scripts. An override `config.yaml` would need to be created pointing to the UFO sources under `masters/INRIA-SERIF/`. The most likely onboarding commit is `94732c5a` ("Separate build scripts for each family") or `2bb3549c` ("Fresh Serif TTFs"), both from 2019-12-05.

Action needed: Identify the correct onboarding commit (likely `94732c5a` or `2bb3549c`), create an override `config.yaml`, and update METADATA.pb to add the `commit` field.

## Commit Added (HIGH confidence)

Commit `9b015af5d8ab574b6afeffd324443bfcbf77e300` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2019-12-06). This is the most reliable method.
