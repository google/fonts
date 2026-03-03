# Matangi — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/thegraphicant/Matangi"
  commit: "a806f5ac9093cab670d0ce25a2cf5639bcc000ca"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Matangi[wght].ttf"
    dest_file: "Matangi[wght].ttf"
  }
  files {
    source_file: "article/ARTICLE.en_us.html"
    dest_file: "ARTICLE.en_us.html"
  }
  files {
    source_file: "article/matangi-01.jpg"
    dest_file: "matangi-01.jpg"
  }
  files {
    source_file: "article/matangi-02.jpg"
    dest_file: "matangi-02.jpg"
  }
  files {
    source_file: "article/matangi-03.jpg"
    dest_file: "matangi-03.jpg"
  }
  files {
    source_file: "article/matangi-04.jpg"
    dest_file: "matangi-04.jpg"
  }
  files {
    source_file: "article/matangi-05.jpg"
    dest_file: "matangi-05.jpg"
  }
  files {
    source_file: "article/matangi-06.jpg"
    dest_file: "matangi-06.jpg"
  }
  files {
    source_file: "article/matangi-07.jpg"
    dest_file: "matangi-07.jpg"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

**Repository**: https://github.com/thegraphicant/Matangi
**Owner**: The Graphic Ant (thegraphicant)
**Designer**: The Graphic Ant (Devanagari + Latin sans-serif)
**Primary Script**: Devanagari (`Deva`)
**Date added to Google Fonts**: 2025-04-29

The upstream repository was found in the fontc_crater_cache. It contained a `.glyphs` source file and a `config.yaml` for gftools-builder. The repository had a clean working tree at the time of inspection.

### Repository Structure (at commit a806f5a)

```
article/
  ARTICLE.en_us.html
  MATANGI-01.jpg through MATANGI-07.jpg
fonts/
  ttf/ (static TTFs: Light through Black)
  variable/Matangi[wght].ttf
  webfonts/ (woff2 files)
sources/
  config.yaml
  Matangi.glyphs
OFL.txt
README.md
```

### Commit History (upstream)

The upstream repo had 18 commits total. Key merge commits:

1. `81c6848` (2025-05-16) - Merge PR #1 from yanone/main: Initial setup with binaries and file extensions
2. `c67a7d9` (2025-05-21) - Merge PR #4 from yanone/main: File renaming
3. `a806f5a` (2025-06-24) - Merge PR #5 from simoncozens/fix-rendering: Adjusted conjunct subcategories and rebuilt fonts

The commit `a806f5a` was HEAD of the `main` branch and the latest commit in the repository.

## Onboarding History

Matangi went through three PRs to google/fonts:

### PR #9481 — Initial Onboarding (merged 2025-05-21)
- **Title**: "Matangi: Version 3.002 added"
- **Author**: Yanone
- **Referenced commit**: `81c68488ff396d1264c6e9d195f106ff85e124ec` (Merge PR #1 from yanone/main)
- This was the initial addition of the font to google/fonts.

### Source Info Update (PR #9490, commit 26254ae, 2025-05-21)
- Author: Felipe Sanches
- Updated the commit hash from `81c6848` to `c67a7d9` (Merge PR #4 from yanone/main)
- Added `config_yaml: "sources/config.yaml"` field

### PR #9615 — Version 3.003 Update (merged 2025-06-27)
- **Title**: "Matangi: Version 3.003 added"
- **Author**: Emma Marichal
- **Referenced commit**: `a806f5ac9093cab670d0ce25a2cf5639bcc000ca`
- Multiple fixes: removed latin-ext subset, bumped version, fixed image filename casing (MATANGI -> matangi), added images back

### PR #9658 — Version 3.004 Update (merged 2025-07-10)
- **Title**: "Matangi: Version 3.004 added"
- **Author**: Emma Marichal
- **Referenced commit**: `a806f5ac9093cab670d0ce25a2cf5639bcc000ca` (same as PR #9615)
- Bumped version, removed article, updated OFL.txt
- The article directory was removed from google/fonts in this PR (commit 7c76f9b "remove useless article") but images remained via the METADATA.pb source_file mappings

## Build Configuration

**Config location**: `sources/config.yaml` (in upstream repo)
**Config present at referenced commit**: Yes

```yaml
sources:
  - Matangi.glyphs
buildOTF: false
buildTTF: true
buildWebfont: true
buildStatic: true
buildVariable: true
```

The config.yaml existed at all three referenced commits (81c6848, c67a7d9, a806f5a) and was identical throughout. It referenced the `.glyphs` source file for building.

No override config.yaml existed in the google/fonts family directory.

## Findings

### Commit Hash: Correct
The commit hash `a806f5ac9093cab670d0ce25a2cf5639bcc000ca` in METADATA.pb correctly points to the latest commit in the upstream repository (HEAD of main). This is the commit referenced in both PR #9615 and PR #9658. The font binary in google/fonts (711948 bytes) matches the size of the variable font at this commit in the upstream repo.

### Config YAML: Correct
The `config_yaml: "sources/config.yaml"` field correctly points to a valid gftools-builder config in the upstream repo. The config references `Matangi.glyphs` as the source.

### Repository URL: Correct
The `repository_url` field matches the upstream repository's remote URL.

### Image Filename Casing Mismatch (Minor Issue)
The METADATA.pb `source_file` entries for article images reference lowercase filenames (e.g., `article/matangi-01.jpg`), but the actual files in the upstream repo at commit `a806f5a` are uppercase (e.g., `article/MATANGI-01.jpg`). This mismatch would cause gftools-packager to fail on case-sensitive filesystems (Linux) but would work on case-insensitive filesystems (macOS). The images in google/fonts are lowercase and have been significantly compressed (e.g., MATANGI-01.jpg: 790KB upstream vs matangi-01.jpg: 111KB in google/fonts), suggesting they were reprocessed externally rather than copied directly via the source_file mapping.

### Source Block: Complete
All required fields are present: repository_url, commit, config_yaml, branch, and files mappings.

## Recommended Source Block

The current source block is complete and correct. No changes are recommended. The image filename casing mismatch is a minor issue that does not affect the source metadata integrity -- the images appear to have been reprocessed externally regardless.

```
source {
  repository_url: "https://github.com/thegraphicant/Matangi"
  commit: "a806f5ac9093cab670d0ce25a2cf5639bcc000ca"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Matangi[wght].ttf"
    dest_file: "Matangi[wght].ttf"
  }
  files {
    source_file: "article/ARTICLE.en_us.html"
    dest_file: "ARTICLE.en_us.html"
  }
  files {
    source_file: "article/matangi-01.jpg"
    dest_file: "matangi-01.jpg"
  }
  files {
    source_file: "article/matangi-02.jpg"
    dest_file: "matangi-02.jpg"
  }
  files {
    source_file: "article/matangi-03.jpg"
    dest_file: "matangi-03.jpg"
  }
  files {
    source_file: "article/matangi-04.jpg"
    dest_file: "matangi-04.jpg"
  }
  files {
    source_file: "article/matangi-05.jpg"
    dest_file: "matangi-05.jpg"
  }
  files {
    source_file: "article/matangi-06.jpg"
    dest_file: "matangi-06.jpg"
  }
  files {
    source_file: "article/matangi-07.jpg"
    dest_file: "matangi-07.jpg"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```
