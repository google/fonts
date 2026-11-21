# Nevermind: upstream source metadata

## Initial state

- METADATA.pb had a source block with repository_url https://github.com/lamzhonghang/nevermind, commit 8b5dbcc2f615b14443e32121a7f369360c36d222, branch main and three file mappings (OFL.txt and the two variable fonts), but no config_yaml.
- The family directory had no override config.yaml and no upstream_info.md.
- gftools-packager onboarded the family at Version 1.000 in commit 97c873a (2026-07-24). It arrived through PR #10736, merged 2026-07-31, and the commit message names upstream commit 8b5dbcc.

## Actions taken

- Verified the recorded commit. At 8b5dbcc, fonts/variable/Nevermind[wght].ttf, fonts/variable/Nevermind-Italic[wght].ttf and OFL.txt are byte-identical to the shipped files (same git blobs). The variable fonts were last rebuilt upstream in 7cb2531 (2025-12-11, "Build fonts"), which matches their head.modified (2025-12-11 15:35 UTC). After that, only OFL.txt changed (9822f7a, merged into main as 8b5dbcc on 2026-07-24), and Google Fonts ships that OFL.txt. No upstream commit landed between 8b5dbcc and the Google Fonts merge.
- Found a gftools-builder config at sources/config.yaml at that commit. It lists Nevermind.glyphs, sets splitItalic: true and gives STAT definitions for both variable fonts.
- Build-tested the config at 8b5dbcc:
  - gftools builder (Python, fontmake 3.11.1) reproduced both variable fonts. Only head.modified and head.checkSumAdjustment differ, and the functional gate passed for both styles.
  - gftools-builder3 (fontc) stopped on the vendorID custom parameter "XMIND" in the .glyphs file. fontc rejects a 5-character vendor ID, while fontmake truncates it to the 4-byte "XMIN" found in the shipped fonts. With the vendorID patched in a scratch copy only, builder3 wrote the same combined wght+ital font under both file names, because it does not yet split the ital axis. Neither failure is caused by the config.
- Added config_yaml: "sources/config.yaml" to the source block of METADATA.pb. No other field was changed.

## Final state

- The source block points to https://github.com/lamzhonghang/nevermind at 8b5dbcc2f615b14443e32121a7f369360c36d222, with config_yaml sources/config.yaml.
- The shipped fonts rebuild from that commit and config with the Python gftools builder. They do not yet build with gftools-builder3/fontc, for the two reasons above.

## Related repositories

- https://github.com/lamzhonghang/nevermind now redirects to https://github.com/lamzhonghang/Xmind. The upstream renamed the family to Xmind (Version 1.001) on 2026-09-02, after this family was merged. The renamed family was onboarded separately as ofl/xmind (PR #10956). Commit 8b5dbcc is still reachable from main in the renamed repository.
- https://github.com/xmindltd/nevermind is named in the copyright string. It is an earlier Xmind distribution repository (master at 95cf077, commits 2020-01-03 to 2023-07-21) that holds only binaries (static NeverMind TTFs, width families) and PNG specimens, with no font sources. It was never the source of this family.
