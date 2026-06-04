# Bhavuka - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Bhavuka |
| Repository URL | https://github.com/10four/Bhavuka |
| Commit Hash | e4819c2a22da01f0bb124b26e3d1ab86d1e05587 |
| Config YAML | (none) |
| Status | missing_config |
| Category | DISPLAY |

## How the Repository URL Was Found

The repository URL `https://github.com/10four/Bhavuka` is documented in the METADATA.pb `source{}` block. It was added by commit `46a7c0576` ("Add more upstreams (a,b)"). The copyright field in the font metadata references "Matt Heximer (www.10fourdesign.com)", which corresponds to the GitHub organization `10four`.

## How the Commit Hash Was Determined

The commit hash `e4819c2a22da01f0bb124b26e3d1ab86d1e05587` is the latest (HEAD) commit in the upstream repository. It was added to the METADATA.pb in the batch commit `9a14639f3` (2026-02-25): "Add source blocks to 602 more METADATA.pb files".

The upstream repository has a total of 21 commits, with `e4819c2` (2016-03-07) being the most recent. The font was added to google/fonts in the initial commit `90abd17b4` (2015-03-07).

**Key finding**: The font file (`Bhavuka-Regular.ttf`) did NOT change between commit `cd83228` (2014-10-06, which includes the vertical metrics fix from PR #1) and commit `e4819c2` (2016-03-07). Between these two commits, only `README.md` was modified (+8 lines, -2 lines). Since the font was onboarded from the initial google/fonts commit in March 2015, the correct source commit would technically be `cd83228` (the merge of the vertical metrics fix, dated 2014-10-06, before the google/fonts addition). However, since `e4819c2` contains the identical TTF file and is the repo HEAD, using it as the reference commit is also valid.

### Upstream repository timeline:
- `9dfc0fb` (2014-10-05) - Fixing vertical metrics
- `cd83228` (2014-10-06) - Merge pull request #1 from fontdirectory/master (last TTF change)
- `e4819c2` (2016-03-07) - Update README.md (HEAD, only README change, TTF unchanged)

### google/fonts timeline:
- `90abd17b4` (2015-03-07) - Initial commit (added Bhavuka along with many other fonts)

## Config YAML Status

**No config.yaml exists** in the upstream repository, either at the recorded commit or at HEAD.

The repository structure at the recorded commit is:
- `Bhavuka-Regular.sfd` (FontForge source)
- `Bhavuka-Regular.ttf` (pre-built binary)
- `Bhavuka-Regular.pdf`
- `OFL.txt`
- `README.md`

The font source is in SFD (FontForge) format, which is not compatible with gftools-builder. No override config.yaml exists in the google/fonts family directory either.

## Verification

- **Repository exists**: Yes, confirmed locally at `upstream_repos/fontc_crater_cache/10four/Bhavuka`
- **Commit hash exists**: Yes, verified: `e4819c2 Update README.md`
- **Config.yaml exists**: No, neither in upstream repo nor as override
- **Source format**: SFD (FontForge) - not gftools-builder compatible
- **TTF unchanged since pre-onboarding**: The font binary is identical between `cd83228` and `e4819c2`

## Confidence Level

**Medium-High** - The repository URL is correct and the commit hash points to a valid commit where the TTF is identical to what was onboarded. However, the commit hash `e4819c2` represents a README update from 2016, not the actual commit that produced the font binary. The more precise onboarding-relevant commit would be `cd83228` (2014-10-06), which is the last commit that modified the TTF file. Since both commits contain the same TTF, the practical impact is negligible, but the provenance is slightly imprecise.

## Open Questions

- Should the commit hash be updated to `cd83228` (the last commit that actually modified the TTF) instead of `e4819c2` (the repo HEAD which only updated README)?
- The font uses Devanagari script support. The SFD source format means it cannot be rebuilt with gftools-builder. This family will likely remain in `missing_config` status permanently unless the source is converted to a modern format.
