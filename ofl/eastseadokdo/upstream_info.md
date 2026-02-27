# East Sea Dokdo

## Summary

East Sea Dokdo is a Korean and Latin handwriting/display font designed by YoonDesign Inc. The upstream repository (`yoondesign/Yoonfont-KoreaDokdo`) contains only binary font files (.ttf, .otf) -- no editable source files. The font was originally named "KoreaDokdo" and was renamed to "East Sea Dokdo" during the Google Fonts onboarding process. A config.yaml cannot be created because there are no buildable source files.

## Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | East Sea Dokdo |
| **Designer** | YoonDesign Inc |
| **License** | OFL |
| **Date Added** | 2018-03-12 |
| **Repository URL** | https://github.com/yoondesign/Yoonfont-KoreaDokdo |
| **Commit Hash** | `41594a5` (latest commit before google/fonts merge) |
| **Config YAML** | N/A (binary-only repo, no buildable sources) |
| **Status** | no_config_possible |

## Investigation Details

### Onboarding History

East Sea Dokdo was added to Google Fonts in PR [#1459](https://github.com/google/fonts/pull/1459) ("korean families r01: added") by Marc Foley (@m4rc1e) on 2018-03-13 (commit `16680f868`). The PR body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com". This was a batch addition of approximately 20 Korean font families.

The font was originally named "KoreaDokdo" in the upstream repo. During the onboarding process, it was renamed to "East Sea Dokdo" (the name table in the google/fonts binary still contains traces of both names: `EastSeaDokdo-Regular` and `KoreaDokdo-Regular` / `DaehanMingukDokdo-Regular`).

The font binary has not been updated since onboarding.

### Upstream Repository

The upstream repository is [yoondesign/Yoonfont-KoreaDokdo](https://github.com/yoondesign/Yoonfont-KoreaDokdo), created on 2017-12-13. YoonDesign Inc is a Korean professional design group.

**Repository contents** (binary-only, no source files):
- `KoreaDokdo.ttf` (3,834,712 bytes) -- added in commit `50394d2` (2017-12-13), never modified
- `OFL_Yoondesign KoreaDokdo.txt` -- license file
- `README.md` -- brief description
- `Readme_Yoondesign_KoreaDokdo.txt` -- brief description
- `KoreaDokdo.otf` was present but deleted in commit `4daa805` (2018-03-18, after google/fonts merge)

**Commit timeline:**
| Hash | Date | Description |
|------|------|-------------|
| `05b13e8` | 2017-12-13 | Create README.md |
| `50394d2` | 2017-12-13 | Add files via upload (TTF, OTF, OFL.docx) |
| `71a3f66` | 2017-12-19 | Delete KoreaDokdo OFL.docx |
| `c51db01` | 2017-12-19 | Delete README.md |
| `db6fa92` | 2017-12-19 | Add files via upload (OFL.txt, Readme) |
| `8392394` | 2017-12-19 | Create README.md |
| `bd0e074` | 2017-12-19 | Delete README.md |
| **`41594a5`** | **2017-12-19** | **Create README.md** (latest before google/fonts merge) |
| `1bc4d9e` | 2017-12-19 | Update Readme_Yoondesign_KoreaDokdo.txt |
| `4daa805` | 2018-03-18 | Delete KoreaDokdo.otf (AFTER google/fonts merge) |

**Note on commit ordering**: Commits `41594a5` and `1bc4d9e` both have the date 2017-12-19 but `1bc4d9e` is a child of `41594a5`. Both predate the google/fonts merge on 2018-03-13. The most accurate reference commit is `1bc4d9e` as the last commit before the google/fonts merge.

**Corrected reference commit**: `1bc4d9e` (2017-12-19, "Update Readme_Yoondesign_KoreaDokdo.txt") -- this was the latest commit in the upstream repo before the google/fonts PR #1459 was merged.

### Binary Comparison

The upstream TTF (`KoreaDokdo.ttf`, 3,834,712 bytes) differs from the google/fonts binary (`EastSeaDokdo-Regular.ttf`, 3,178,684 bytes). This is expected because Aaron Bell re-mastered the font for Google Fonts, which included:
- Renaming from "KoreaDokdo" to "East Sea Dokdo"
- Modifying the name table (vendor code `UKWN`)
- Likely subsetting or optimizing the font (file is ~656KB smaller)

### Other YoonDesign Repos

YoonDesign has several font repos on GitHub, all following the same binary-only pattern:
- `yoondesign/yoonfont-Gamjaflower` -- binary only
- `yoondesign/Yoonfont-HiMelody` -- binary only
- `yoondesign/Yoonfont-Poorstory` -- binary only
- `yoondesign/Yoonfont` -- empty repo

None contain editable source files.

### Source Availability

No source files (`.glyphs`, `.ufo`, `.designspace`, `.sfd`) exist in the upstream repository or anywhere publicly accessible. The repository only contains compiled binary fonts (.ttf, .otf). A config.yaml cannot be created because there are no buildable source files for gftools-builder.

### Copyright and License

- Upstream OFL: "Copyright [1989-2017] Yoondesign Inc., with Reserved Font Name 'KoreaDokdo'"
- google/fonts OFL: "Copyright (c) YoonDesign Inc. All Rights Reserved."
- Designer website: http://www.yoonfont.co.kr

## Conclusion

East Sea Dokdo has an identified upstream repository (`yoondesign/Yoonfont-KoreaDokdo`), but it is a binary-only repo with no editable source files. The source block can reference the repository URL and commit hash, but no config.yaml can be provided since there are no buildable sources. The font was re-mastered by Aaron Bell during onboarding, so the google/fonts binary is a derivative of the upstream binary rather than a direct copy.

**Recommended METADATA.pb source block:**
```
source {
  repository_url: "https://github.com/yoondesign/Yoonfont-KoreaDokdo"
  commit: "1bc4d9ec41e5159a839e58a349fa2e88799e93bc"
}
```

**Status**: `missing_config` -- upstream repo exists but contains only binaries, no buildable source files, so no config.yaml is possible.
