# Investigation Report: Finlandica

## Family Information
- **Family Name**: Finlandica
- **Designer**: Helsinki Type Studio, Niklas Ekholm, Juho Hiilivirta, Jaakko Suomalainen
- **License**: OFL
- **Category**: Sans Serif
- **Date Added to Google Fonts**: 2022-05-13
- **Google Fonts Path**: `ofl/finlandica/`

## Upstream Repository
- **Repository URL**: https://github.com/HelsinkiTypeStudio/Finlandica
- **Branch**: master
- **Repository Status**: Active, single commit (force-pushed history)

## Source Files in Upstream
- `sources/Finlandica.glyphs` (Roman)
- `sources/Finlandica-Italic.glyphs` (Italic)
- `sources/config.yaml` (gftools-builder configuration)
- `sources/CustomFilterFilandicaSet.plist`

## Build Configuration
- **config.yaml location**: `sources/config.yaml` (in upstream repo)
- **Override config.yaml in google/fonts**: Not present, not needed
- **Source format**: Glyphs (.glyphs)
- **Variable font output**: `Finlandica[wght].ttf`, `Finlandica-Italic[wght].ttf`
- **Axes**: wght (400-700)

## Commit Analysis

### Current METADATA.pb Commit
- **Commit**: `959e075ccc9652de57c72ecf56f887e13a537c85`
- **Date**: 2023-10-19
- **Message**: "Update README.md" (gender neutral "Jokaisenoikeus" instead of the old "Jokamiehenoikeus")
- **Author**: Niklas Ekholm

### History of Commit References in google/fonts

| Date | PR | Version | Commit Referenced |
|------|-----|---------|-------------------|
| 2022-05-13 | #4666 | 1.062 (initial) | `24c1334e9c4559efc297dee980cb4c365ab05f85` |
| 2022-06-02 | #4733 | 1.063 | `9da70dc1ce8cda37cbe3fd488b239156b097ef40` |
| 2022-09-29 | #5334 | 1.064 (latest) | `f18a892e62bdcd80839549c04e3572e2bdca435e` |
| 2024-04-03 | upstream.yaml merge | -- | (added files/branch metadata, kept `f18a892e`) |
| 2025-03-31 | Batch 1/4 | -- | Changed commit to `959e075c`, added `config_yaml` |

### Key Finding: Force-Pushed Repository

The upstream repository at https://github.com/HelsinkiTypeStudio/Finlandica currently contains only a **single commit** (`959e075`, dated 2023-10-19). All three commits previously referenced by gftools-packager (`24c1334e`, `9da70dc1`, `f18a892e`) no longer exist, indicating the repository was force-pushed or recreated after the last google/fonts update (2022-09-29).

The original onboarding commit for the Version 1.064 update was `f18a892e62bdcd80839549c04e3572e2bdca435e`, as documented in PR #5334. This commit no longer exists in the repository.

### Binary File Verification

The binary font files at the current single commit `959e075` are **byte-identical** to those in google/fonts:

| File | SHA-256 | Size |
|------|---------|------|
| `Finlandica[wght].ttf` | `8192c7f916ad92...` | 143,908 bytes |
| `Finlandica-Italic[wght].ttf` | `70b7bddb5b5d01...` | 151,992 bytes |

Both upstream and google/fonts copies match exactly. The OFL.txt files also match.

### How `959e075` Entered METADATA.pb

The "Batch 1/4" commit (2025-03-31) ported data from fontc_crater's `targets.json`, which uses the latest commit of each upstream repo. Since the repo had been force-pushed to a single commit by that time, fontc_crater recorded `959e075`. This replaced the original `f18a892e` that was correctly set by gftools-packager.

## PR History

All three PRs were authored by Emma Marichal (@emmamarichal) and merged by Rosalie Wagner (@RosaWagner):

1. **PR #4666** (2022-05-13): Initial onboarding, Version 1.062
2. **PR #4733** (2022-06-02): Update to Version 1.063 (closes #4241, unblocks #4666)
3. **PR #5334** (2022-09-29): Update to Version 1.064 (latest)

## Assessment

### Commit Hash Status

The commit `959e075` currently in METADATA.pb is **acceptable but not ideal**:

- **Acceptable**: The binary files at this commit are identical to those in google/fonts, and it is the only commit that exists in the repository. The `sources/config.yaml` path is valid at this commit.
- **Not ideal**: The original onboarding commit was `f18a892e` (from PR #5334), but it no longer exists due to the repository being force-pushed. Since the repo only has one commit, `959e075` is effectively the only option.

### Current METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/HelsinkiTypeStudio/Finlandica"
  commit: "959e075ccc9652de57c72ecf56f887e13a537c85"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Finlandica[wght].ttf"
    dest_file: "Finlandica[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Finlandica-Italic[wght].ttf"
    dest_file: "Finlandica-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Conclusion

- **Status**: complete
- **Confidence**: HIGH
- **Repository URL**: Correct (https://github.com/HelsinkiTypeStudio/Finlandica)
- **Commit**: `959e075ccc9652de57c72ecf56f887e13a537c85` -- the only existing commit; binary files verified identical to google/fonts
- **Config**: `sources/config.yaml` (present in upstream repo, valid gftools-builder config)
- **Action needed**: None. The METADATA.pb source block is complete and correct. While the original onboarding commit (`f18a892e`) was lost to a force-push, the current commit contains identical binary output and valid source files.
