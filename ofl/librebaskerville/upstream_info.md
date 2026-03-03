# Investigation Report: Libre Baskerville

**Family Name**: Libre Baskerville
**Directory**: `ofl/librebaskerville`
**Designer**: Impallari Type
**License**: OFL
**Date Added**: 2012-11-30
**Model**: Claude Opus 4.6

## Source Block Status

The METADATA.pb already contained a complete source block at the time of this investigation.

## Repository URL

**URL**: https://github.com/impallari/Libre-Baskerville
**Status**: Valid repository, cloned at `upstream_repos/fontc_crater_cache/impallari/Libre-Baskerville`

The repository is owned by Pablo Impallari (impallari), the original designer. The copyright string in METADATA.pb also references this repository.

## Commit Hash

**Commit**: `d20160cfa0ac4c532327f85b3ca4054acf92ed38`
**Author**: Emma Marichal <bonjour@emmamarichal.fr>
**Date**: 2025-10-15
**Message**: "fix feature issue"

### Verification

The commit was verified by binary comparison of the variable font files:

- `fonts/variable/LibreBaskerville[wght].ttf` (171,900 bytes) -- identical to google/fonts
- `fonts/variable/LibreBaskerville-Italic[wght].ttf` (167,456 bytes) -- identical to google/fonts

Both files were binary-identical between the upstream commit and the files in google/fonts.

### Commit Context

This commit is the second-to-last commit on the `master` branch. The latest commit on master is `9852edf` ("Merge pull request #14 from emmamarichal/master"), which is the merge commit that incorporated `d20160c`. The tree contents are identical between both commits (no diff).

The first commit in google/fonts PR #9909 originally referenced the merge commit `9852edf75ece3af500a5ec61245f94788c3d4633`, but the source block was later updated (by Felipe Sanches in commit `3b6cb0462`) to reference `d20160c` instead, which is the actual work commit containing the feature fix. Both commits produce the same files.

## Config YAML

**Path**: `sources/config.yaml`
**Location**: In the upstream repository (not an override)

The config.yaml existed at the referenced commit and contained a valid gftools-builder configuration:

```yaml
sources:
  - LibreBaskerville.glyphs
  - LibreBaskerville-Italic.glyphs
familyName: Libre Baskerville
axisOrder:
  - wght
  - ital
cleanUp: true
stat:
  LibreBaskerville[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: Regular
      value: 400
      linkedValue: 700
      flags: 2
    - name: Medium
      value: 500
    - name: SemiBold
      value: 600
    - name: Bold
      value: 700
  - name: Italic
    tag: ital
    values:
    - name: Roman
      value: 0
      linkedValue: 1
      flags: 2
  LibreBaskerville-Italic[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: Regular
      value: 400
      linkedValue: 700
      flags: 2
    - name: Medium
      value: 500
    - name: SemiBold
      value: 600
    - name: Bold
      value: 700
  - name: Italic
    tag: ital
    values:
    - name: Italic
      value: 1
```

Source files referenced by the config:
- `sources/LibreBaskerville.glyphs` -- present at the referenced commit
- `sources/LibreBaskerville-Italic.glyphs` -- present at the referenced commit

## Google Fonts PR History

### PR #9909 (Merged 2025-10-22)
- **Title**: "Libre Baskerville: Version 2.005; added"
- **Author**: emmamarichal (Emma Marichal)
- **Merged by**: emmamarichal

This PR upgraded Libre Baskerville from static fonts (Version 1.051) to variable fonts (Version 2.005). The PR contained four commits:

1. `93b0f9ed1` (2025-10-17) -- "Libre Baskerville: Version 1.051; ttfautohint (v1.8.4.7-5d5b) added" -- referenced upstream commit `9852edf`
2. `9e63336c5` (2025-10-17) -- "VF replacement" -- replaced static TTFs with variable font files
3. `4f90d359c` (2025-10-17) -- "update metadata.pb" -- updated METADATA.pb for variable font filenames
4. `ccec48b33` (2025-10-22) -- "Update OFL.txt with corrected formatting"

After this PR was merged, Felipe Sanches added source metadata in commits `f84930e03` and `3b6cb0462`, updating the commit hash from `a658d05` (the earlier merge commit of PR #13) to `d20160c` (the actual fix in PR #14), and adding the `config_yaml` field.

### Earlier History

Before PR #9909, the family had only static fonts (Regular, Italic, Bold) dating back to the original onboarding in 2012. The font went through several metadata-only updates over the years.

## Font Files in google/fonts

| File | Size |
|------|------|
| `LibreBaskerville[wght].ttf` | 171,900 bytes |
| `LibreBaskerville-Italic[wght].ttf` | 167,456 bytes |

Both are variable fonts with a `wght` axis ranging from 400 to 700.

## Upstream Repository Structure

The upstream repo contained the following relevant structure at commit `d20160c`:

- `sources/LibreBaskerville.glyphs` -- upright source
- `sources/LibreBaskerville-Italic.glyphs` -- italic source
- `sources/config.yaml` -- gftools-builder configuration
- `fonts/variable/LibreBaskerville[wght].ttf` -- pre-built variable font (upright)
- `fonts/variable/LibreBaskerville-Italic[wght].ttf` -- pre-built variable font (italic)
- `fonts/ttf/` -- static TTF instances
- `fonts/otf/` -- static OTF instances
- `fonts/webfonts/` -- WOFF2 files

## Conclusion

**Status**: Complete
**Confidence**: HIGH

All source metadata fields were already correctly populated in METADATA.pb:
- `repository_url` points to a valid, accessible GitHub repository
- `commit` hash `d20160c` was verified by binary comparison of both variable font files
- `config_yaml` correctly references `sources/config.yaml` in the upstream repo
- `branch` is set to `master`, matching the upstream default branch
- File mappings correctly reference the variable font paths in the upstream repo

No corrections are needed. The source block is complete and verified.
