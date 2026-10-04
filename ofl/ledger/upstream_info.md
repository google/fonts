# Investigation: Ledger

**Model**: Claude Opus 4.6
**Confidence**: MEDIUM

## Source Repository

The original design sources for Ledger are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `ledger/src/`.

### Source Files in googlefontdirectory-hg

- `Ledger-Regular-OTF.vfb` -- FontLab binary source (proprietary, not buildable with gftools-builder)
- `Ledger-Regular-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Ledger-Regular.otf` -- compiled OTF binary, not a design source
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are in VFB and SFD legacy formats only. No `.glyphs`, `.ufo`, or `.designspace` files are present. These formats are not compatible with gftools-builder.

## METADATA.pb Analysis

The METADATA.pb for Ledger contains no `source { }` block -- no `repository_url`, no commit hash, no config path.

## Google Fonts History

The google/fonts git history for `ofl/ledger/Ledger-Regular.ttf` shows:
- `f8265bddf` -- "ledger: v1.003 added (#2514)"
- `0436d99c0` -- "ledger: fixed nbsp width (#2353)"
- `90abd17b4` -- "Initial commit" (original onboarding)

The commit body for `f8265bddf` was checked but contains no upstream repository reference.

## Designer Information

The OFL copyright states: `Copyright (c) 2011, Denis Masharov <denis.masharov@gmail.com>`. The designer is Denis Masharov. No GitHub repository URL is referenced in the font files.

No upstream repository for this font was found in the upstream repo cache.

## Conclusion

The googlefontdirectory-hg monorepo preserves VFB and SFD sources for Ledger, but these are legacy formats not compatible with gftools-builder. No config.yaml can be created without first converting sources to a supported format. The font has been updated multiple times in google/fonts but the source repository was never documented. Denis Masharov would need to be contacted or searched for to find if modern sources were ever published.
