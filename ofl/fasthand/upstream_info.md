# Fasthand - Investigation Report

## Family Details

- **Family name**: Fasthand
- **Designer**: Danh Hong, Neapolitan
- **License**: OFL
- **Category**: Display, Handwriting
- **Primary script**: Khmer (Khmr)
- **Date added to Google Fonts**: 2012-05-24
- **Google Fonts path**: `ofl/fasthand/`

## Upstream Repository

- **URL**: https://github.com/danhhong/Fasthand (verified accessible, HTTP 200)
- **Owner**: danhhong (Danh Hong)
- **Branch**: master
- **Contributors**: Danh Hong (author), Yanone (contributor - Khmer font engineer)

## Source Files

The upstream repository contains:
- `Source/Fasthand.glyphs` - Glyphs source file
- `Source/builder.yaml` - gftools-builder configuration
- `Release/ttf/Fasthand-Regular.ttf` - Pre-built binary

### builder.yaml Contents

```yaml
sources:
  - Fasthand.glyphs
outputDir: "../Release"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/danhhong/Fasthand"
  commit: "048b6cfd785212af6470687da43969cc9bf462d9"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/ttf/Fasthand-Regular.ttf"
    dest_file: "Fasthand-Regular.ttf"
  }
  branch: "master"
}
```

## Commit History Analysis

### Upstream Repository Commits (complete history)

| Commit | Date | Message |
|--------|------|---------|
| `048b6cf` | 2021-11-01 | Merge pull request #2 from yanone/master (HEAD) |
| `92bb93f` | 2021-10-28 | New binary |
| `ad31ca7` | 2021-10-28 | Bumped version |
| `71122fa` | 2021-10-28 | Updated sidebearings |
| `7f3bd99` | 2021-06-07 | Merge pull request #1 from yanone/master |
| `ec39a0a` | 2021-04-15 | Ligature definition to Letter |
| `bf1fae7` | 2021-04-15 | Vertical metrics, new font |
| `2e032de` | 2021-04-15 | Added uni00A0, uni25CC |
| `81b4159` | 2021-04-15 | Cubic outlines |
| `1193bb9` | 2021-04-15 | Metadata |
| `60cd75f` | 2021-04-15 | Create Fasthand.glyphs |
| `aedc50d` | 2020-08-24 | update |

### Google Fonts Update History

1. **Initial commit** (2015-03-07, `90abd17`): Original onboarding.
2. **PR #3512** (merged 2021-09-08, `6df6c98`): Version 8.000 added. Used upstream commit `7f3bd99` (Merge PR #1 from yanone). This was the major redesign by Yanone working with Danh Hong.
3. **PR #4020** (merged 2021-11-10, `8855534`): Version 8.001 added. Used upstream commit `048b6cf` (Merge PR #2 from yanone). Updated sidebearings fix.
4. **PR #4152** (merged 2021-12-07, `4f5dbdb`): Bumped to Version 8.002. Batch update by Yanone across 14 Khmer fonts to fix urgent glyph definition issues (glyphs in GSUB not being recognized as letters by Microsoft Edge). This change was NOT pushed to the upstream repository.

## Commit Hash Verification

- **METADATA.pb references**: `048b6cfd785212af6470687da43969cc9bf462d9`
- **This is HEAD of upstream master**: Yes, this is the latest commit in the upstream repo.
- **PR #4020 confirms this hash**: The gftools-packager message explicitly states this commit was used.

### Binary Mismatch Issue

The current binary in google/fonts does NOT match the binary at commit `048b6cf`:
- **Upstream binary at `048b6cf`**: 213,872 bytes, Version 8.001
- **Current google/fonts binary**: 213,852 bytes, Version 8.002

The discrepancy is due to PR #4152 (merged 2021-12-07), where Yanone rebuilt the font with glyph categorization fixes (marking GSUB-substituted glyphs as letters for Microsoft Edge compatibility). This fix was applied directly to the binary submitted in google/fonts but was never pushed back to the upstream repository.

The METADATA.pb commit hash `048b6cf` is correct for the source block that was added with PR #4020, but the actual binary currently served was rebuilt by Yanone in PR #4152 from a locally modified version of those same sources.

## Configuration

- **config_yaml**: `Source/builder.yaml` (exists in upstream repo at all commits since it was added)
- **Override config needed**: No, the upstream repo has a proper builder.yaml
- **Source type**: `.glyphs` (Glyphs app format)
- **Build type**: Static only (no variable font)

## Status

- **Repository URL**: Correct and verified
- **Commit hash**: `048b6cf` -- correct for the PR #4020 onboarding, but the binary was subsequently modified by PR #4152 without a corresponding upstream push
- **Config path**: `Source/builder.yaml` -- correct and present in the upstream repo
- **Source block**: Complete and accurate (modulo the binary mismatch from PR #4152)
- **Overall status**: Complete (with caveat about binary version mismatch)

## Notes

- Fasthand is a Khmer handwriting-style font. The Latin component is based on Seaweed Script by Neapolitan.
- The upstream repo was created in 2020 by Danh Hong, with significant work by Yanone (font engineer) who submitted the redesigned versions to Google Fonts via PRs #1 and #2 in the upstream repo, and PRs #3512, #4020, and #4152 in google/fonts.
- The binary version mismatch (8.001 in upstream vs 8.002 in google/fonts) is a known pattern: Yanone applied batch fixes to multiple Khmer fonts in PR #4152 without pushing changes upstream. The source changes were glyph category definitions, not design changes.
- No additional commits have been made to the upstream repo since `048b6cf` (2021-11-01).

## Confidence: HIGH

The source block is complete and well-documented. The commit hash `048b6cf` matches what gftools-packager recorded in PR #4020. The only caveat is the subsequent binary modification in PR #4152, which is a separate issue that does not affect the correctness of the source metadata.
