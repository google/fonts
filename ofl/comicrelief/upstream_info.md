# Comic Relief - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Comic Relief |
| Designer | Jeff Davis |
| Repository URL | https://github.com/loudifier/Comic-Relief |
| Commit | `856315f5a45dfdad75090e4454f1ebfd019296b9` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| Override Config | No |
| Date Added | 2025-02-13 |
| License | OFL |

## How URL Found

The repository URL `https://github.com/loudifier/Comic-Relief` was included in the METADATA.pb from the initial onboarding. The font was added via issue #6529, opened by `loudifier` (Jeff Davis), the author of the font. The onboarding commit (`0ed65319a`) already had the complete source block with repository URL.

## How Commit Determined

The commit hash `856315f5a45dfdad75090e4454f1ebfd019296b9` is explicitly stated in the onboarding commit message:

> "Taken from the upstream repo https://github.com/loudifier/Comic-Relief at commit https://github.com/loudifier/Comic-Relief/commit/856315f5a45dfdad75090e4454f1ebfd019296b9."

This was part of the initial onboarding by Yanone (post@yanone.de), committed on 2025-02-13. The METADATA.pb also includes an `archive_url` for the v1.2 release: `https://github.com/loudifier/Comic-Relief/releases/download/v1.2/Comic-Relief-v1.2.zip`.

In the upstream repository, commit `856315f` is "update FONTLOG" and corresponds to the state of the repo at version 1.2 (the version that was onboarded as "Version 1.200" in google/fonts).

## Config YAML Status

The upstream repository has `sources/config.yaml` at commit `856315f`:

```yaml
sources:
  - ComicRelief-Regular.ufo
  - ComicRelief-Bold.ufo
familyName: "Comic Relief"
outputDir: "../fonts"
buildOTF: false
googleFonts: true
removeOutlineOverlaps: false
buildVariable: false
```

**Note**: The config references `.ufo` source files, but the repository at this commit only contains `.sfd` (FontForge) source files. The `.ufo` files would be generated from the `.sfd` files as part of the build process (the repo has conversion scripts for this at later commits). The fonts in google/fonts were likely taken from the v1.2 release archive rather than built directly from this commit.

## Verification

- **Commit exists in upstream**: Yes - verified in the repository
- **Branch matches**: Yes - `main` branch
- **Config YAML exists at commit**: Yes - `sources/config.yaml` exists at `856315f`
- **Font files**: The METADATA.pb references `fonts/ttf/ComicRelief-Regular.ttf` and `fonts/ttf/ComicRelief-Bold.ttf` which were from the release archive
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/loudifier/Comic-Relief/`
- **Significant work after this commit**: Yes - there are many commits after `856315f` (hinting improvements, build system changes, version 1.210 update). These have not been onboarded to Google Fonts

## Confidence Level

**HIGH** - The commit hash is explicitly confirmed by the onboarding commit message. The repository URL matches the issue author. The font was recently onboarded (February 2025) with full source documentation.

## Open Questions

- The upstream repo has significant development after the onboarded commit (v1.210 update, hinting improvements). A future update to Google Fonts may be warranted.
- The config.yaml references `.ufo` files but only `.sfd` files exist at the referenced commit. The build process may require a conversion step or the fonts were taken from the release archive.
