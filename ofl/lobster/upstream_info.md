# Lobster — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

The current source block in `ofl/lobster/METADATA.pb` contains only the repository URL, with no commit hash or config_yaml reference:

```
source {
  repository_url: "https://github.com/impallari/The-Lobster-Font"
}
```

An override `config.yaml` file already exists in the google/fonts family directory (`ofl/lobster/config.yaml`), added in commit `5ddf312` ("Add config_yaml enrichment for 82 font families", 2026-02-20).

## Repository Analysis

**Upstream repo**: https://github.com/impallari/The-Lobster-Font (verified accessible, HTTP 200)
**License**: OFL
**Designer**: Pablo Impallari (Impallari Type)

The upstream repository at `impallari/The-Lobster-Font` is the original source. It has a complex fork chain:

1. **impallari/The-Lobster-Font** — original upstream by Pablo Impallari
2. **ThomasJockin/The-Lobster-Font** — fork of impallari
3. **cyrealtype/The-Lobster-Font** — fork of ThomasJockin (Alexei Vanyashin's work)
4. **googlefonts/lobster** — fork of impallari (renamed from "The-Lobster-Font" to "lobster")

The v2.100 update was developed by Alexei Vanyashin (alexeiva) on the cyrealtype fork and merged to the googlefonts fork on 2017-10-31. The same changes were later merged into the impallari/The-Lobster-Font master branch via PR #11 on 2023-05-03 (a no-diff fast-forward merge, since both branches contained identical content).

**Repository structure** (at commit `0796aa8`):
```
sources/
  Lobster.glyphs          (Glyphs format source)
fonts/
  ttf/Lobster-Regular.ttf (precompiled binary)
  otf/Lobster-Regular.otf (precompiled binary)
AUTHORS.txt
CONTRIBUTING.md
CONTRIBUTORS.txt
DESCRIPTION.en_us.html
OFL.txt
README.md
```

No `config.yaml` exists in the upstream repository. The source file is a `.glyphs` format file, compatible with gftools-builder.

**Contributors** (from git history): Pablo Impallari, Alexei Vanyashin (alexeiva), Marc Foley, ThomasJockin.

## Onboarding History

Lobster has a long history in Google Fonts, dating back to the initial commit (`90abd17`, the very first commit in the google/fonts repository). Key milestones for the binary:

| Commit | Date | Description |
|--------|------|-------------|
| `90abd17` | (initial) | Initial commit (original Lobster) |
| `037ee7b` | (early) | Added V1.007 |
| `98f26cd` | (early) | .null width set to 0 |
| `9053cf2` | (early) | v2.000 kerning improvements by Alexei |
| `8d69f43` | (early) | Fixed fractions |
| `c32a2f3` | (early) | Fixed percent and thousandth glyphs |
| `c08bc94` | (early) | Updated copyright string, RFN |
| `ae26195` | 2016-12-13 | v2.001 added (PR #532) |
| `98f1d55` | 2017-11-03 | **v2.100 added (PR #1296)** — current version |

**PR #1296** (the last font binary update) was authored by Marc Foley (@m4rc1e) and merged by Dave Crossland (@davelab6) on 2017-11-03. The PR body stated: "Taken from the GF Repo, https://github.com/googlefonts/The-Lobster-Font". The update added extensive Cyrillic Extended glyphs and Latin-B characters.

**PR #532** (v2.001) was also by Marc Foley, merged 2016-12-13, fixing issue #525 (Cyrillic ligature issue) and RFN.

## Build Configuration

The upstream repository has no `config.yaml` file. The source file `sources/Lobster.glyphs` is a Glyphs-format file compatible with gftools-builder.

An override `config.yaml` already exists in the google/fonts family directory:
```yaml
sources:
  - sources/Lobster.glyphs
```

This was added in commit `5ddf312` on 2026-02-20.

**Note on binary differences**: The font binary in google/fonts (406,076 bytes) does not match the pre-built binary in the upstream repository at commit `0796aa8` (405,892 bytes). This is expected for a 2017 onboarding — Marc Foley likely rebuilt the font from the Glyphs sources using the tooling available at the time (not gftools-builder, which did not exist yet). The source files at `0796aa8` represent the correct source state used for the v2.100 onboarding.

## Findings

1. **Repository URL is correct**: `https://github.com/impallari/The-Lobster-Font` is the original upstream and is accessible. The googlefonts/lobster fork shares the same commit hashes.

2. **Commit hash identified**: `0796aa8` ("regenerated fonts", 2017-10-27) by Alexei Vanyashin is the last content commit before the googlefonts fork merge (`2cb4569`, 2017-10-31) and before the google/fonts PR #1296 was merged (2017-11-03). This is the correct source commit for the v2.100 update.

3. **Override config.yaml already in place**: The google/fonts directory already has an override `config.yaml` pointing to `sources/Lobster.glyphs`, so no `config_yaml` field is needed in METADATA.pb.

4. **Missing commit hash in METADATA.pb**: The source block lacks a `commit` field. Adding `commit: "0796aa8aa42f6cbc89fa61be4a2a12fdcd2b8998"` would complete the source metadata.

5. **No newer upstream changes**: The impallari repo's last merge commit (`ee431d4`, 2023-05-03) was a no-diff merge of the cyrealtype PR — it introduced no new content beyond what was already at `0796aa8`. The source files are identical between `0796aa8` and the current HEAD (`ee431d4`).

## Recommended Source Block

```
source {
  repository_url: "https://github.com/impallari/The-Lobster-Font"
  commit: "0796aa8aa42f6cbc89fa61be4a2a12fdcd2b8998"
}
```

The `config_yaml` field is intentionally omitted because an override `config.yaml` already exists in the google/fonts family directory and is auto-detected by google-fonts-sources.
