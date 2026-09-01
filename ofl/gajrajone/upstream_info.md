# Investigation Report: Gajraj One

## Summary

Gajraj One is a Devanagari and Latin display font designed by Saurabh Sharma, added to Google Fonts on 2023-01-23 via gftools-packager. The upstream repository is `https://github.com/xconsau/GajrajOne`, which contains a single commit with UFO sources and a valid `config.yaml`. The METADATA.pb source block is complete and verified: the commit hash `5768aa3d4522b402ead302e5bb8697e965da694f` correctly identifies the onboarding commit, and the binary font in google/fonts is identical to the one in the upstream repository.

## Key Findings

| Field              | Value                                                      |
|--------------------|------------------------------------------------------------|
| Family Name        | Gajraj One                                                 |
| Designer           | Saurabh Sharma                                             |
| License            | OFL                                                        |
| Date Added         | 2023-01-23                                                 |
| Repository URL     | https://github.com/xconsau/GajrajOne                       |
| Commit Hash        | 5768aa3d4522b402ead302e5bb8697e965da694f                   |
| Config YAML        | sources/config.yaml                                        |
| Source Type         | UFO                                                       |
| Status             | complete                                                   |
| Confidence         | HIGH                                                       |

## Investigation Details

### Onboarding History

Gajraj One was added to google/fonts in commit `e4ae4df6f` (2023-01-23) by Yanone (post@yanone.de) via gftools-packager. The commit message reads:

> [gftools-packager] Gajraj One: Version 1.000 added
> Gajraj One Version 1.000 taken from the upstream repo https://github.com/xconsau/GajrajOne at commit https://github.com/xconsau/GajrajOne/commit/5768aa3d4522b402ead302e5bb8697e965da694f.

The original onboarding commit created the METADATA.pb with a source block containing the repository URL and commit hash. Later commits enriched the metadata:
- `66f91f10f` (2024-04-03) by Simon Cozens: Merged upstream.yaml into METADATA.pb, adding file mappings and branch information
- `19cdcec59` (2025-03-31) by Felipe Sanches: Added `config_yaml: "sources/config.yaml"` from fontc_crater targets list
- `ea42b7c32`: Added stroke/classification metadata
- `292f049d5`: Added primary_script for Devanagari

### Upstream Repository

The upstream repository at `https://github.com/xconsau/GajrajOne` is accessible and verified. It is cached locally at `fontc_crater_cache/xconsau/GajrajOne/`.

The repository contains a single commit:
- `5768aa3` (2023-01-19) by Saurabh Sharma: "Add files via upload"

This single commit added the entire project, based on the Google Fonts project template.

### Repository Contents

```
sources/
  config.yaml
  GajrajOne-Regular.ufo/
  features_backup/
fonts/
  ttf/GajrajOne-Regular.ttf
  otf/GajrajOne-Regular.otf
  webfonts/GajrajOne-Regular.woff2
documentation/
  gajraj-specimen.jpg
scripts/
.github/workflows/build.yaml
AUTHORS.txt
CONTRIBUTORS.txt
DESCRIPTION.en_us.html
Makefile
OFL.txt
README.md
requirements.txt
```

### Config.yaml

The `sources/config.yaml` file exists in the upstream repository with the following content:

```yaml
sources:
  - GajrajOne-Regular.ufo

familyName: Gajraj One

autohintTTF: false
```

This is a valid gftools-builder configuration referencing the UFO source relative to the `sources/` directory.

### Binary Verification

The font binary in google/fonts (`GajrajOne-Regular.ttf`, 149,784 bytes) was compared with the binary from the upstream repository at commit `5768aa3`:
- **MD5 match**: Both files have the same hash (`3e9aeacf42fc435dc9350670b7e51591`)
- **Size match**: Both files are 149,784 bytes

This confirms that the binary in google/fonts was taken directly from the upstream repository's pre-built `fonts/ttf/` directory at the referenced commit, without recompilation.

### Source File Assessment

The repository contains `sources/GajrajOne-Regular.ufo/` which is a UFO (Unified Font Object) source, fully compatible with gftools-builder. The config.yaml correctly references this source.

### Branch Information

The repository has one branch: `main` (default), matching the `branch: "main"` field in METADATA.pb.

## Conclusion

Gajraj One's METADATA.pb source block is complete and fully verified. The repository URL, commit hash, file mappings, branch, and config_yaml are all correct. The binary font in google/fonts is an exact copy of the pre-built font from the upstream repo. No changes are needed.

### Current METADATA.pb Source Block (verified correct)

```
source {
  repository_url: "https://github.com/xconsau/GajrajOne"
  commit: "5768aa3d4522b402ead302e5bb8697e965da694f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/GajrajOne-Regular.ttf"
    dest_file: "GajrajOne-Regular.ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
