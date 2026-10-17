# Maven Pro — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The source block in `ofl/mavenpro/METADATA.pb` currently reads:

```
source {
  repository_url: "https://www.github.com/m4rc1e/mavenproFont"
  commit: "a694ee80d067e6f8cad700930e78ce395d4949e6"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/variable/MavenPro[wght].ttf"
    dest_file: "MavenPro[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
```

## Repository Analysis

### Repository History

Maven Pro has a complex upstream repository history:

1. **`googlefonts/mavenproFont`** (https://github.com/googlefonts/mavenproFont) — The original upstream repo, created 2017-03-13 under the googlefonts organization. Last pushed 2023-06-19. This was the repository initially referenced in METADATA.pb when the source block was first added in the "Update upstreams" commit (c891a9b8, 2024-03-04).

2. **`m4rc1e/mavenproFont`** (https://github.com/m4rc1e/mavenproFont) — A fork of the googlefonts repo, created 2018-04-04 by Marc Foley. Marc used this fork to prepare the Version 2.103 update in February 2025. The METADATA.pb now points to this fork.

### Current Upstream Repo (m4rc1e/mavenproFont)

- **Default branch**: main
- **Total commits (on main)**: ~30 (history stretching back to the original repo)
- **Key recent commits** (Feb 6-7, 2025, by Marc Foley):
  - `a694ee8` — "regenned fonts" (2025-02-07, the referenced commit)
  - `86a23da` — "fix Lslash" (2025-02-07)
  - `144085d` — "regen fonts" (2025-02-07)
  - `a43a9e5` — "update copyright string, sigh" (2025-02-07)
  - `fee7a8a` — "bump requirements" (2025-02-07)
  - `0c55e03` — "upgrade upload-artifact" (2025-02-06)
  - `e872218` — "bump version" (2025-02-06)
  - `9a6093e` — "update license" (2025-02-06)
  - Multiple other prep commits from the same two days

### Source Files

Located at `sources/` in the repo:
- `sources/MavenPro.glyphs` — Glyphs source file (534,604 bytes)
- `sources/config.yaml` — gftools-builder configuration

### Build Configuration

The `sources/config.yaml` contains:

```yaml
sources:
  - MavenPro.glyphs
axisOrder:
  - wght
familyName: Maven Pro
stat:
  MavenPro[wght].ttf:
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
    - name: ExtraBold
      value: 800
    - name: Black
      value: 900
```

### Output Verification

The variable font `fonts/variable/MavenPro[wght].ttf` from the upstream repo at commit `a694ee8` has SHA-256 hash `bc994ed80baaec6ea61d7cb631f49466a1deb29d4363138021a96931f9faae9a`, which is **identical** to the file in `ofl/mavenpro/MavenPro[wght].ttf` in google/fonts. This confirms the binary was taken directly from the upstream repo's pre-built output.

## Onboarding History

### Timeline

1. **Initial addition** (2011-05-25): Maven Pro was added to Google Fonts (`date_added` in METADATA.pb).

2. **Multiple updates** over the years: v2.000 (2016), v2.002 (2017), v2.003 VF (2018), v2.100 (2019), v2.101 STAT fix (2021), v2.102 hotfix (2022).

3. **Source block first added** (2024-03-04, commit c891a9b8): The "Update upstreams" commit added a bare source block pointing to `https://github.com/googlefonts/mavenproFont` (no commit hash, no config_yaml, no files).

4. **Version 2.103 update** (2025-02-07, commit ec6798de, by Marc Foley): This commit updated the font binary and enriched the source block with the commit hash, files mapping, and branch. It changed the repository URL from `googlefonts/mavenproFont` to `m4rc1e/mavenproFont`. The commit message explicitly states: "Taken from the upstream repo https://www.github.com/m4rc1e/mavenproFont at commit a694ee80d067e6f8cad700930e78ce395d4949e6."

5. **config_yaml field added** (2025-04-03, commit be712aef, PR #9051, by Felipe Sanches): Added the `config_yaml: "sources/config.yaml"` field to complete the source block.

### Relevant PRs

- **PR #9051** (merged 2025-02-07): "Maven Pro: Version 2.103 added" — Marc Foley's update that refreshed the font and set up the source block pointing to his fork.

## Build Configuration

- **config.yaml exists**: Yes, at `sources/config.yaml` in the upstream repo
- **gftools-builder compatible**: Yes, uses standard gftools-builder format with Glyphs source
- **Override needed**: No, the upstream repo has a proper config.yaml
- **METADATA.pb config_yaml field**: Correctly set to `sources/config.yaml`

## Findings

### URL Issue (Minor)

The `repository_url` in METADATA.pb uses `https://www.github.com/m4rc1e/mavenproFont` (with `www.` prefix). This returns HTTP 301 redirecting to `https://github.com/m4rc1e/mavenproFont`. While functional, the canonical form without `www.` would be more standard. This was set by Marc Foley in the Version 2.103 commit and is the URL he used consistently in both the METADATA.pb and commit message.

### Fork vs. Original Repo

The METADATA.pb points to Marc Foley's personal fork (`m4rc1e/mavenproFont`) rather than the organization repo (`googlefonts/mavenproFont`). This is intentional: Marc prepared the v2.103 update in his fork, and the specific commit `a694ee8` exists only in his fork (the googlefonts repo was last pushed in 2023). The fork relationship is confirmed via GitHub API.

### Source Block Completeness

The current source block is **complete**:
- `repository_url`: Set (points to m4rc1e fork)
- `commit`: Set and verified (`a694ee8`)
- `config_yaml`: Set and verified (`sources/config.yaml`)
- `files`: Correctly mapped (variable font + OFL.txt)
- `branch`: Set to `main`
- Binary file hash match: Confirmed

### Commit Hash Verification

The commit `a694ee80d067e6f8cad700930e78ce395d4949e6` was made on 2025-02-07 at 10:44:35 UTC by Marc Foley, with message "regenned fonts." The google/fonts commit adding Version 2.103 was made 45 seconds later at 10:45:20 UTC. The binary files are byte-identical. The commit is the latest (HEAD) on the main branch of `m4rc1e/mavenproFont`. This is definitively the correct commit.

## Recommended Source Block

The current source block is already complete and correct. The only minor improvement would be normalizing the URL to remove the `www.` prefix:

```
source {
  repository_url: "https://github.com/m4rc1e/mavenproFont"
  commit: "a694ee80d067e6f8cad700930e78ce395d4949e6"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/variable/MavenPro[wght].ttf"
    dest_file: "MavenPro[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
```

**Note**: The only change from current is `www.github.com` to `github.com`. This is a cosmetic normalization; the `www.` URL works via redirect.
