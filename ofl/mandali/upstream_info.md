# Mandali — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/appajid/mandali"
}
```

The source block contains only the `repository_url`. There is no `commit` hash and no `config_yaml` field.

## Repository Analysis

The upstream repository at `https://github.com/appajid/mandali` exists and is accessible. It was created on 2014-11-15 and last pushed to on 2014-11-26. The repository is not archived and is not a fork. The default branch is `master`.

The repository contains only two commits:

1. **77ee092** (2014-11-15) — "Updating TTF SFD Copyright and version" — Initial commit by appajid (ambarisha@gmail.com) containing `Mandali.sfd`, `Mandali.ufo/`, and `OFL.txt`
2. **b5d0982** (2014-11-26) — "Latin Characters removed" — Removed Latin character glyphs from the SFD and UFO sources (373 files changed, 313 insertions, 10045 deletions)

### Source Files

The repository contains:
- `Mandali.sfd` — FontForge SFD source file (2.9 MB)
- `Mandali.ufo/` — UFO2 source directory (created by FontLab, per `metainfo.plist`), containing approximately 1,252 glyph files
- `OFL.txt` — SIL Open Font License

There are no `.glyphs`, `.glyphx`, or `.designspace` files. The UFO source is in UFO format version 2. There is no `config.yaml` or any build configuration file.

### Repository Cleanliness

The cached clone was clean with no local modifications, up to date with `origin/master`.

## Onboarding History

Mandali was added to Google Fonts with `date_added: 2014-12-10` in METADATA.pb. The font binary (`Mandali-Regular.ttf`, 619,212 bytes) was included in the initial commit of the google/fonts repository on 2015-03-07 by Dave Crossland. The binary has never been modified since — its SHA256 hash (`8ba4663d114aff639e4974b65795353c193272026308608d95770aaaa6afd806`) has remained identical from the initial commit to the present.

The font binary was version 1.0.5 and was processed with `ttfautohint (v1.2.25-373a) -l 7 -r 28 -G 50 -x 13 -D telu -f latn -w G -X ""`. The binary contains Latin characters derived from Vernon Adams' Nunito, as documented in the copyright string: "Copyright (c) 2012 Silicon Andhra (fonts.siliconandhra.org). Copyright (c) 2011, Vernon Adams (vern@newtypography.co.uk), with Reserved Font Name Nunito".

### Key Observation: Commit Hash Determination

The second upstream commit (b5d0982, 2014-11-26) removed Latin characters from the SFD and UFO source files. However, the binary in google/fonts still contains Latin characters. This means the binary was NOT compiled from the latest upstream commit. It was more likely compiled from or around commit **77ee092** (2014-11-15), which still contained Latin sources, or from an even earlier pre-repository state.

However, since the font binary was version 1.0.5 and the UFO fontinfo.plist references "Version 1.00", there may have been intermediate compilation steps not reflected in the upstream repo. The binary was likely compiled separately and placed in google/fonts.

### Source Block Addition

The source block was added to METADATA.pb in commit c891a9b8 ("Update upstreams") on 2024-03-04 by Simon Cozens, merged via PR #7344 ("Update upstreams (2/2)") on 2024-03-06.

## Build Configuration

There is no `config.yaml` in the upstream repository. The source files are:
- **SFD** (FontForge native format) — Not directly supported by gftools-builder
- **UFO2** (FontLab export) — Could potentially be used with gftools-builder, but requires a `config.yaml`

The UFO source is version 2 (created by `com.fontlab.ufoLib`). Modern gftools-builder typically works with UFO3 or `.glyphs`/`.designspace` files. Building from these legacy sources would likely require conversion or special handling.

Additionally, the latest upstream commit removed Latin characters from the sources, meaning the current source state does not match the binary in google/fonts (which includes Latin). Any rebuild from the current upstream sources would produce a different font.

### Override config.yaml Feasibility

Creating an override `config.yaml` for this font is problematic because:
1. The UFO source is version 2, which may not be fully compatible with modern gftools-builder
2. The current source state (after Latin removal) does not match the binary in google/fonts
3. The SFD format is not supported by gftools-builder
4. The font was originally compiled with ttfautohint, which would need to be replicated

## Findings

1. **Repository URL is correct**: The `repository_url` field correctly points to `https://github.com/appajid/mandali`.

2. **Missing commit hash**: There is no commit hash in the source block. The most likely candidate for the onboarding commit is **77ee092** (2014-11-15), the first commit, since the binary contains Latin characters that were removed in the second commit. However, the exact provenance of the binary (version 1.0.5 vs. version 1.00 in the sources) suggests the binary may have been compiled from a different state.

3. **No config.yaml**: The upstream repo lacks a `config.yaml`. The sources are SFD + UFO2 format, which are legacy formats for gftools-builder. Creating a working override config would be difficult given the source/binary mismatch.

4. **Source/binary mismatch**: The current state of the upstream sources (latest commit b5d0982) does not match the binary in google/fonts. The sources had Latin characters removed, but the binary retains them.

5. **Dormant upstream**: The repository has not been updated since November 2014. It is unlikely to receive updates.

6. **Font heritage**: Mandali is a Telugu font designed by Purushoth Kumar Guttula, with Latin characters derived from Vernon Adams' Nunito. It was made available by Silicon Andhra / AP Society for Knowledge Networks.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/appajid/mandali"
  commit: "77ee092273d1941fac6021e200d38e8f39dd0943"
}
```

The commit hash **77ee092** is recommended because it is the only commit where the sources still contained Latin characters matching the binary. No `config_yaml` field is included because there is no config.yaml in the upstream repo and the SFD/UFO2 sources are not readily compatible with gftools-builder. An override config.yaml is not recommended at this time due to the source format limitations and the source/binary mismatch at the latest commit.

**Status justification**: Marked as `incomplete` because while the repository URL is verified and a plausible commit hash was identified, there is no build configuration and the source/binary relationship is uncertain. The font's legacy source format (SFD + UFO2) and dormant upstream make full metadata enrichment difficult.
