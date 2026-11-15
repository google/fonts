# Iosevka Charon: source metadata review

**Date**: 2026-09-27
**Model**: Claude Opus 5.5
**Family**: ofl/iosevkacharon
**Status**: missing_config (no gftools-builder config possible: Iosevka parametric sources)
**Confidence**: HIGH

## Initial state

- METADATA.pb had a source block with repository_url https://github.com/jul-sh/iosevka-charon, commit 727f1343e957cadd354f9ec4ee98eba9b645143d, archive_url https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip, branch main and 9 files entries (OFL.txt and 8 TTFs from iosevkacharon/ in the zip).
- It had no config_yaml, and the family directory had no override config.yaml. The 2026-09-27 source-metadata audit flagged this as "no config_yaml and no override config.yaml".
- The family was onboarded by gftools-packager in PR #10245 (commit 3d418cc, merged 2026-02-27), whose message named upstream commit 727f134.

## Actions taken

- Verified the recorded commit in the upstream mirror (fetched 2026-09-27):
  - 727f134 ("Merge pull request #16 from jul-sh/v34.1.0-w-almost-flat-top", 2026-02-13 16:09 UTC) is the target of the lightweight tags v34.100 and pre-727f1343e957cadd354f9ec4ee98eba9b645143d. Its sources/version.json gives gf_version 34.100; its first parent (tag v33.305) gives 33.305.
  - Downloaded the v34.100 release asset iosevka-charon.zip (SHA-256 b2e7a2a1b9e1abea5426c7510b15e466b31b5b43d96653ca43b9605a2f8ab9e9). All 8 shipped TTFs were byte-identical (SHA-256) to iosevkacharon/*.ttf in the zip and report "Version 34.100". The OFL.txt added at onboarding was identical to the zip's copy; google/fonts edited it afterwards. The upstream CI workflow at 727f134 builds the fonts and uploads iosevka-charon.zip when a release is published.
  - Found no upstream commit, on any ref, touching sources/, scripts/ or Makefile between 727f134 and the google/fonts merge. The two commits of 2026-02-20 (5501bc4, 343fcf7) edited README.md only.
  - Found that upstream replaced the history of main on 2026-03-18/19. The CI prerelease tags, created on every push to main, follow the old lineage up to daa738d (2026-03-18 22:51 -0400) and the new one from 6b0a474 (tag v34.201, 2026-03-18 23:32 -0400). The new main (70 commits, rooted at b8a1155 of 2026-01-03 and at 75f4305, the squashed Iosevka subtree import of 2026-03-13) shares no commit with 727f134. It holds 48155e078af9f81a4360500f52c9a95180b36b6b, which has the same tree and message as 727f134.
  - Confirmed that 727f134 is still fetchable. It is reachable from tag v34.100, several pre- tags and five side branches, and https://github.com/jul-sh/iosevka-charon/archive/727f1343e957cadd354f9ec4ee98eba9b645143d.tar.gz returned HTTP 200. That tarball URL is what google-fonts-sources downloads. The commit field was kept at 727f134, the commit the release was built from.
- Searched the tree at 727f134 for a gftools-builder config and for builder-compatible sources and found none. Its 4274 files include the Iosevka parametric sources under sources/iosevka/ (348 .ptl, 95 .mjs, 3464 .svg), the TOML build plan sources/private-build-plans.toml (plans IosevkaCharon and IosevkaCharonMono; the Makefile default), a fast debug plan sources/test-build-plans.toml, and Python post-processing scripts driven by a Nix-wrapped Makefile. The only YAML files are CI workflows and a Prettier config. A sources/config.yaml existed earlier in the history, but it belonged to the googlefonts-project-template example font (Radio Canada Display). Commit 6dc1652 "Migrate to Iosevka Charon" (2025-11-27), an ancestor of 727f134, deleted it. Current main (532af98, 2026-09-14) has no config either.
- Build-tested the decision in scratch clones at 727f134 with two throwaway probe configs: sources/config.yaml listing private-build-plans.toml, and a repo-root config listing sources/private-build-plans.toml. gftools-builder3 (e851b8b) rejected the plan in both cases with "Recipe is not valid: Failed to load source <plan>: Unknown file type for file <plan>". The Python builder (gftools 0.9.100.dev6+g2db1fe32f.d20260315) failed on both in its recipe provider ("Instance private-build-plans.toml must have a name, or familyName and styleName"). The probes were then discarded.
- Left METADATA.pb unchanged and created no override config.yaml.

## Final state

- METADATA.pb is unchanged. Its source block (repository_url, commit 727f134, archive_url, files, branch) is complete for an archive-based onboarding, and the commit is verified against the shipped binaries.
- There is no config_yaml and no override config.yaml, because gftools-builder and fontc cannot build Iosevka sources. The upstream builds the fonts with its own pipeline: scripts/iosevka_build.py drives Iosevka's Node.js build, then scripts/fix_fonts.py post-processes the output.
- The sibling family Iosevka Charon Mono (ofl/iosevkacharonmono, PR #10247) shares the repository, commit and release zip.
- Upstream has published two later releases: v34.300 (2026-03-26) and v34.801 (Iosevka 34.8.1, published 2026-09-15 and marked Latest on GitHub; its tag is on 532af98, the current head of main). Google Fonts has not onboarded either.

## Earlier upstream_info.md (2026-03-03)

The previous report is kept below. Its headings were demoted by two levels and its em dashes were replaced with "--"; the text is otherwise unchanged.

### Iosevka Charon -- Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `iosevkacharon`
**Status**: complete (no config -- Iosevka custom build system)

#### Initial State

METADATA.pb already contained a complete source block with:
- `repository_url`: `https://github.com/jul-sh/iosevka-charon`
- `commit`: `727f1343e957cadd354f9ec4ee98eba9b645143d`
- `archive_url`: `https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip`
- `branch`: `main`
- File mappings for all 8 TTF files (Light, LightItalic, Regular, Italic, Medium, MediumItalic, Bold, BoldItalic) from `iosevkacharon/` subdirectory in the release archive
- No `config_yaml` field (expected -- see below)
- No override `config.yaml` in the google/fonts family directory
- No DESCRIPTION.en_us.html file

#### Investigation

##### Onboarding History

The font was onboarded via **PR #10245** ("Iosevka Charon: Version 34.100 added"), authored by **Emma Marichal** (emmamarichal), created on 2026-02-19 and merged on 2026-02-27.

The initial commit `3d418cc3ab7320c8493efebdb8048d24f3c65e25` explicitly references the upstream repo and commit:
> "Taken from the upstream repo https://github.com/jul-sh/iosevka-charon at commit https://github.com/jul-sh/iosevka-charon/commit/727f1343e957cadd354f9ec4ee98eba9b645143d."

The PR body repeats this same information. The PR contained 5 commits total:
1. `3d418cc` -- Initial onboarding (fonts, METADATA.pb, OFL.txt)
2. `335885b` -- Add article
3. `ac3fea7` -- Update OFL link
4. `a7c1e55` -- Fix formatting and content of OFL.txt
5. `13394c5` -- Refine description of Iosevka Charon font

A sibling PR #10247 ("Iosevka Charon Mono: Version 34.100 added") was also merged on the same date for the monospace variant.

##### Commit Hash Verification

The referenced commit `727f1343e957cadd354f9ec4ee98eba9b645143d` was verified in the upstream repo:
- It is a merge commit dated **2026-02-13**: "Merge pull request #16 from jul-sh/v34.1.0-w-almost-flat-top"
- It is tagged as **v34.100** in the upstream repo
- The `pre-727f1343e957cadd354f9ec4ee98eba9b645143d` tag also exists, pointing to the same commit
- The archive URL (`v34.100` release) corresponds to this exact commit

Timeline is consistent: upstream commit (Feb 13) predates the google/fonts onboarding commit (Feb 19) and PR merge (Feb 27).

Two commits exist after the referenced commit in the upstream repo:
- `5501bc4` (2026-02-20) -- "Update README description" (README.md only)
- `343fcf7` (2026-02-20) -- "Fix stray conflict marker text in README" (README.md only)

Both are documentation-only changes that do not affect font files.

##### Build System Analysis

Iosevka Charon uses a **custom build system** that is fundamentally incompatible with gftools-builder:
- Fonts are built from the [Iosevka](https://github.com/be5invis/Iosevka) source using a Node.js-based build pipeline
- The `sources/iosevka/` directory is a git subtree of the upstream Iosevka project
- Build configuration is in `sources/private-build-plans.toml` (TOML format, Iosevka-specific)
- The build process uses a Makefile with Nix-based dependency management
- Post-processing scripts in `scripts/` handle Google Fonts compliance
- There are **no** `.glyphs`, `.ufo`, or `.designspace` files -- the source format is Iosevka's custom parametric system

Since there are no gftools-builder compatible sources, a `config.yaml` is neither present nor applicable. The fonts are distributed as pre-built TTFs via GitHub releases, and the `archive_url` + `files` mapping in METADATA.pb correctly reflects this distribution method.

##### Repository Details

- **Owner/Repo**: jul-sh/iosevka-charon
- **Designer**: Juliette Pluto (jul-sh)
- **License**: SIL OFL 1.1 (fonts), MIT (code/docs)
- **Copyright**: "Copyright 2015-2025 The Iosevka Project Authors (https://github.com/be5invis/Iosevka)"

#### Actions Taken

No changes were needed. The source block in METADATA.pb is already complete and accurate. The upstream repo was cloned to the cache at `upstream_repos/fontc_crater_cache/jul-sh/iosevka-charon/` for reference.

#### Final State

The METADATA.pb source block is complete with repository URL, commit hash, archive URL, branch, and file mappings. No `config_yaml` is needed because the project uses Iosevka's custom build system (not gftools-builder). The commit hash `727f134` has been verified against the upstream repo and matches the v34.100 tag.

#### Source Block

```
source {
  repository_url: "https://github.com/jul-sh/iosevka-charon"
  commit: "727f1343e957cadd354f9ec4ee98eba9b645143d"
  archive_url: "https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Light.ttf"
    dest_file: "IosevkaCharon-Light.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-LightItalic.ttf"
    dest_file: "IosevkaCharon-LightItalic.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Regular.ttf"
    dest_file: "IosevkaCharon-Regular.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Italic.ttf"
    dest_file: "IosevkaCharon-Italic.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Medium.ttf"
    dest_file: "IosevkaCharon-Medium.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-MediumItalic.ttf"
    dest_file: "IosevkaCharon-MediumItalic.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-Bold.ttf"
    dest_file: "IosevkaCharon-Bold.ttf"
  }
  files {
    source_file: "iosevkacharon/IosevkaCharon-BoldItalic.ttf"
    dest_file: "IosevkaCharon-BoldItalic.ttf"
  }
  branch: "main"
}
```
