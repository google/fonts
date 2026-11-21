# Iosevka Charon Mono: source metadata review

**Date**: 2026-09-27
**Model**: Claude Opus 5.5
**Family**: ofl/iosevkacharonmono
**Status**: missing_config (no gftools-builder config possible: Iosevka parametric sources)
**Confidence**: HIGH

## Initial state

- METADATA.pb had a source block with repository_url https://github.com/jul-sh/iosevka-charon, commit 727f1343e957cadd354f9ec4ee98eba9b645143d, archive_url https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip, branch main and 9 files entries (OFL.txt and 8 TTFs from iosevkacharonmono/ in the zip).
- It had no config_yaml, and the family directory had no override config.yaml. The 2026-09-27 source-metadata audit flagged this as "no config_yaml and no override config.yaml".
- The family was onboarded by gftools-packager in PR #10247 (commit 691932a, merged 2026-02-27), whose message named upstream commit 727f134.

## Actions taken

- Verified the recorded commit in the upstream mirror (fetched 2026-09-27):
  - 727f134 ("Merge pull request #16 from jul-sh/v34.1.0-w-almost-flat-top", 2026-02-13 16:09 UTC) is the target of the lightweight tags v34.100 and pre-727f1343e957cadd354f9ec4ee98eba9b645143d. Its sources/version.json gives gf_version 34.100; its first parent (tag v33.305) gives 33.305.
  - Downloaded the v34.100 release asset iosevka-charon.zip (SHA-256 b2e7a2a1b9e1abea5426c7510b15e466b31b5b43d96653ca43b9605a2f8ab9e9). All 8 shipped TTFs were byte-identical (SHA-256) to iosevkacharonmono/*.ttf in the zip and report "Version 34.100". The OFL.txt added at onboarding was identical to the zip's copy; google/fonts edited it afterwards. The upstream CI workflow at 727f134 builds the fonts and uploads iosevka-charon.zip when a release is published.
  - Found no upstream commit, on any ref, touching sources/, scripts/ or Makefile between 727f134 and the google/fonts merge. The two commits of 2026-02-20 (5501bc4, 343fcf7) edited README.md only.
  - Found that upstream replaced the history of main on 2026-03-18/19. The CI prerelease tags, created on every push to main, follow the old lineage up to daa738d (2026-03-18 22:51 -0400) and the new one from 6b0a474 (tag v34.201, 2026-03-18 23:32 -0400). The new main (70 commits, rooted at b8a1155 of 2026-01-03 and at 75f4305, the squashed Iosevka subtree import of 2026-03-13) shares no commit with 727f134. It holds 48155e078af9f81a4360500f52c9a95180b36b6b, which has the same tree and message as 727f134.
  - Confirmed that 727f134 is still fetchable. It is reachable from tag v34.100, several pre- tags and five side branches, and https://github.com/jul-sh/iosevka-charon/archive/727f1343e957cadd354f9ec4ee98eba9b645143d.tar.gz returned HTTP 200. That tarball URL is what google-fonts-sources downloads. The commit field was kept at 727f134, the commit the release was built from.
- Searched the tree at 727f134 for a gftools-builder config and for builder-compatible sources and found none. Its 4274 files include the Iosevka parametric sources under sources/iosevka/ (348 .ptl, 95 .mjs, 3464 .svg), the TOML build plan sources/private-build-plans.toml (plans IosevkaCharon and IosevkaCharonMono; the Makefile default), a fast debug plan sources/test-build-plans.toml, and Python post-processing scripts driven by a Nix-wrapped Makefile. The only YAML files are CI workflows and a Prettier config. A sources/config.yaml existed earlier in the history, but it belonged to the googlefonts-project-template example font (Radio Canada Display). Commit 6dc1652 "Migrate to Iosevka Charon" (2025-11-27), an ancestor of 727f134, deleted it. Current main (532af98, 2026-09-14) has no config either.
- Build-tested the decision in scratch clones at 727f134 with two throwaway probe configs: sources/config.yaml listing private-build-plans.toml, and a repo-root config listing sources/private-build-plans.toml. gftools-builder3 (e851b8b) rejected the plan in both cases with "Recipe is not valid: Failed to load source <plan>: Unknown file type for file <plan>". The Python builder (gftools 0.9.100.dev6+g2db1fe32f.d20260315) failed on both in its recipe provider ("Instance private-build-plans.toml must have a name, or familyName and styleName"). The probes were then discarded.
- Left METADATA.pb unchanged and created no override config.yaml.

## Final state

- METADATA.pb is unchanged. Its source block (repository_url, commit 727f134, archive_url, files, branch) is complete for an archive-based onboarding, and the commit is verified against the shipped binaries.
- There is no config_yaml and no override config.yaml, because gftools-builder and fontc cannot build Iosevka sources. The upstream builds the fonts with its own pipeline: scripts/iosevka_build.py drives Iosevka's Node.js build, then scripts/fix_fonts.py post-processes the output.
- The sibling family Iosevka Charon (ofl/iosevkacharon, PR #10245) shares the repository, commit and release zip.
- Upstream has published two later releases: v34.300 (2026-03-26) and v34.801 (Iosevka 34.8.1, published 2026-09-15 and marked Latest on GitHub; its tag is on 532af98, the current head of main). Google Fonts has not onboarded either.

## Earlier upstream_info.md (2026-03-03)

The previous report is kept below. Its headings were demoted by two levels and its em dashes were replaced with "--"; the text is otherwise unchanged.

### Iosevka Charon Mono -- Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `iosevkacharonmono`
**Status**: complete (archive-based onboarding, no gftools-builder config applicable)

#### Initial State

The METADATA.pb at `ofl/iosevkacharonmono/METADATA.pb` already contained a complete `source { }` block:

```
source {
  repository_url: "https://github.com/jul-sh/iosevka-charon"
  commit: "727f1343e957cadd354f9ec4ee98eba9b645143d"
  archive_url: "https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip"
  files { source_file: "OFL.txt" dest_file: "OFL.txt" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Light.ttf" dest_file: "IosevkaCharonMono-Light.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-LightItalic.ttf" dest_file: "IosevkaCharonMono-LightItalic.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Regular.ttf" dest_file: "IosevkaCharonMono-Regular.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Italic.ttf" dest_file: "IosevkaCharonMono-Italic.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Medium.ttf" dest_file: "IosevkaCharonMono-Medium.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-MediumItalic.ttf" dest_file: "IosevkaCharonMono-MediumItalic.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-Bold.ttf" dest_file: "IosevkaCharonMono-Bold.ttf" }
  files { source_file: "iosevkacharonmono/IosevkaCharonMono-BoldItalic.ttf" dest_file: "IosevkaCharonMono-BoldItalic.ttf" }
  branch: "main"
}
```

The family directory contained 8 TTF files (Light, LightItalic, Regular, Italic, Medium, MediumItalic, Bold, BoldItalic), METADATA.pb, OFL.txt, and an article directory with ARTICLE.en_us.html. No DESCRIPTION.en_us.html and no override config.yaml were present.

#### Investigation

##### Upstream Repository

The upstream repository is https://github.com/jul-sh/iosevka-charon, maintained by Juliette Pluto (jul-sh). The repository was created on 2021-10-31 and describes both "Iosevka Charon" (quasi-proportional) and "Iosevka Charon Mono" (true monospace) as derivatives of the Iosevka open source font project by be5invis.

##### Build System

This font does NOT use gftools-builder and has no `.glyphs`, `.ufo`, or `.designspace` source files. Instead, it uses Iosevka's own parametric build system:

1. **Source**: The Iosevka source code is embedded as a git subtree under `sources/iosevka/`
2. **Build plans**: Font variants are defined in `sources/private-build-plans.toml` -- a TOML configuration that specifies character variants, weights (Light/300, Regular/400, Medium/500, Bold/700), slopes (Upright, Italic), and spacing (quasi-proportional for Charon, normal monospace for Charon Mono)
3. **Build pipeline**: A `Makefile` orchestrates a multi-stage build:
   - Stage 1: `scripts/iosevka_build.py` compiles raw fonts from Iosevka sources using the build plan
   - Stage 2: `scripts/fix_fonts.py` post-processes fonts for Google Fonts compliance (vertical metrics, component flattening, copyright notices, etc.)
4. **Environment**: The build uses Nix (flake.nix) for reproducible dependency management
5. **Distribution**: Pre-built TTFs are published as GitHub Release assets

Since gftools-builder cannot build Iosevka-based fonts (they require Node.js and the Iosevka build toolchain), no `config.yaml` is applicable. The fonts are onboarded via the `archive_url` and `files` mapping mechanism in METADATA.pb.

##### Commit Hash Verification

The commit `727f1343e957cadd354f9ec4ee98eba9b645143d` was verified against the upstream repository:

- **Commit message**: "Merge pull request #16 from jul-sh/v34.1.0-w-almost-flat-top -- v34.1.0: w = curly-almost-flat-top-serifless"
- **Commit date**: 2026-02-13T16:09:26Z
- **Author**: jul-sh
- **Release**: This commit corresponds exactly to the `v34.100` release tag, created at the same timestamp (2026-02-13T16:09:26Z)

The archive_url `https://github.com/jul-sh/iosevka-charon/releases/download/v34.100/iosevka-charon.zip` correctly points to the v34.100 release asset.

Two subsequent commits were found between the referenced commit and the PR merge date (2026-02-27):
- `5501bc426a3f` (2026-02-20): "Update README description"
- `343fcf7a5004` (2026-02-20): "Fix stray conflict marker text in README"

These are documentation-only changes and do not affect font files or build configuration, confirming the referenced commit is correct for the font binaries.

##### Google Fonts PR History

The font was onboarded via PR [#10247](https://github.com/google/fonts/pull/10247):
- **Title**: "Iosevka Charon Mono: Version 34.100 added"
- **Author**: Emma Marichal (@emmamarichal)
- **Created**: 2026-02-19
- **Merged**: 2026-02-27 by Marc Foley (@m4rc1e)
- **Body**: "Taken from the upstream repo https://github.com/jul-sh/iosevka-charon at commit https://github.com/jul-sh/iosevka-charon/commit/727f1343e957cadd354f9ec4ee98eba9b645143d."

The google/fonts commit history for this directory shows 4 commits:
1. `691932aca` (2026-02-19): "Iosevka Charon Mono: Version 34.100 added" -- initial onboarding with font files, METADATA.pb, and OFL.txt
2. `34457f077` (2026-02-19): "article" -- added ARTICLE.en_us.html
3. `7a0413213` (2026-02-19): "OFL update"
4. `c7f2c84d2` (2026-02-20): "Refine description of Iosevka Charon font"

##### Sibling Family

The repository also produces "Iosevka Charon" (quasi-proportional variant), onboarded in the sibling directory `ofl/iosevkacharon/` via PR [#10245](https://github.com/google/fonts/pull/10245).

##### Copyright

The font copyright reads: "Copyright 2015-2025 The Iosevka Project Authors (https://github.com/be5invis/Iosevka)" -- referring to the upstream Iosevka project from which Iosevka Charon derives.

#### Actions Taken

No changes were needed. The METADATA.pb already contained a complete and accurate source block. The investigation verified all existing metadata:
- Repository URL is valid and accessible
- Commit hash matches the v34.100 release and is the correct onboarding commit
- Archive URL points to the correct release asset
- File mappings correctly reference paths within the release ZIP
- Branch field is set to "main"

#### Final State

The source block in METADATA.pb is complete and correct. No `config_yaml` field is needed because the font uses Iosevka's custom build system, not gftools-builder. The fonts are distributed as pre-built binaries via GitHub Releases, and the `archive_url` + `files` mechanism properly handles this onboarding pattern.

The upstream repo is not yet cloned in the local cache at `upstream_repos/fontc_crater_cache/`. If needed, it can be cloned to `upstream_repos/fontc_crater_cache/jul-sh/iosevka-charon/`.

#### Source Block

The existing source block is complete and verified:

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
    source_file: "iosevkacharonmono/IosevkaCharonMono-Light.ttf"
    dest_file: "IosevkaCharonMono-Light.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-LightItalic.ttf"
    dest_file: "IosevkaCharonMono-LightItalic.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Regular.ttf"
    dest_file: "IosevkaCharonMono-Regular.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Italic.ttf"
    dest_file: "IosevkaCharonMono-Italic.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Medium.ttf"
    dest_file: "IosevkaCharonMono-Medium.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-MediumItalic.ttf"
    dest_file: "IosevkaCharonMono-MediumItalic.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-Bold.ttf"
    dest_file: "IosevkaCharonMono-Bold.ttf"
  }
  files {
    source_file: "iosevkacharonmono/IosevkaCharonMono-BoldItalic.ttf"
    dest_file: "IosevkaCharonMono-BoldItalic.ttf"
  }
  branch: "main"
}
```
