# Investigation: Fleur De Leah

## Family Details
- **Family name**: Fleur De Leah
- **Designer**: Robert Leuschke
- **License**: OFL
- **Category**: HANDWRITING, DISPLAY
- **Date added**: 2021-09-02
- **Path in google/fonts**: `ofl/fleurdeleah/`

## Source Block (from METADATA.pb)
```
source {
  repository_url: "https://github.com/googlefonts/fleurdeleah"
  commit: "69626faaf6a596ea822d4b0fd9521a506b9ffcc0"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/FleurDeLeah-Regular.ttf"
    dest_file: "FleurDeLeah-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Upstream Repository
- **URL**: https://github.com/googlefonts/fleurdeleah
- **Branch**: master
- **Status**: Repository exists and is accessible

## Commit Verification

### Commit referenced in METADATA.pb: `69626faaf6a596ea822d4b0fd9521a506b9ffcc0`

This is the only commit in the upstream repository. The commit message is "legacy ttf deleted", dated 2021-09-02 19:09:33 -0500 (authored by Viviana Monsalve).

### How was this commit identified?

The google/fonts onboarding commit `90b4ee651` (PR #3794) explicitly references the upstream commit in its body:

> "Fleur De Leah Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/fleurdeleah at commit https://github.com/googlefonts/fleurdeleah/commit/69626faaf6a596ea822d4b0fd9521a506b9ffcc0."

Since there is only one commit in the upstream repository, the hash is trivially verified -- there are no other candidates.

### Binary file verification

The TTF file in google/fonts matches the upstream repo exactly:
- **SHA-256**: `11f6c19bd52835c66cf6cf78f060a467a92a85f1d667447ea8feefdd9bccba7d`
- **File size**: 231,608 bytes
- Both `ofl/fleurdeleah/FleurDeLeah-Regular.ttf` and `fonts/ttf/FleurDeLeah-Regular.ttf` in upstream match.

## Build Configuration

### config.yml in upstream repo

Located at `sources/config.yml`:
```yaml
sources:
  - FleurDeLeah.glyphs
familyName: "Fleur De Leah"
buildVariable: false
#autohintTTF: false
```

This is a valid gftools-builder configuration. The source file `sources/FleurDeLeah.glyphs` exists in the repo.

### config_yaml in METADATA.pb
Set to `sources/config.yml` -- correctly pointing to the config file in the upstream repo.

### Override config in google/fonts
No override config.yaml exists in `ofl/fleurdeleah/`.

## Onboarding History

- **PR**: [google/fonts#3794](https://github.com/google/fonts/pull/3794) -- "Fleur De Leah: Version 1.010; ttfautohint (v1.8.3) added"
- **Author**: Viviana Monsalve (vv-monsalve)
- **Co-authored by**: Rosalie Wagner
- **Merged**: 2021-09-08
- **Tool used**: gftools-packager
- **PR comment**: "Fleur De Leah is part of Batch 2 of TypeSetIt projects"

The onboarding was straightforward -- a single font added via gftools-packager, with the binary taken directly from the upstream repo at its only commit.

## Summary

| Field | Value | Status |
|---|---|---|
| repository_url | `https://github.com/googlefonts/fleurdeleah` | Correct |
| commit | `69626faaf6a596ea822d4b0fd9521a506b9ffcc0` | Verified (only commit in repo, binary matches) |
| branch | `master` | Correct |
| config_yaml | `sources/config.yml` | Correct (file exists at that path) |

## Conclusion

- **Status**: complete
- **Confidence**: HIGH

All source metadata fields in METADATA.pb are correct and verified. The repository URL is valid, the commit hash is the only commit in the repository, the binary file checksums match exactly, and the config.yml exists at the referenced path with valid gftools-builder configuration. No corrections needed.
