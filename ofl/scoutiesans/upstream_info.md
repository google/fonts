# Scoutie Sans: upstream source information

- Repository: https://github.com/sursly/scoutie
- Commit: bac79adfafa587663c134599c2afc31b00c402c0 (tag v1.003, head of main); the checks below were made at v1.001, see the last section
- Config: sources/config.yaml (upstream)
- Status: complete
- Confidence: HIGH

## Initial state

- METADATA.pb had a source block with repository_url, commit 1ad978084a859543cb76fe0de66b31b8fc67db2b, archive_url (the v1.001 release zip), branch "main" and a files map for OFL.txt and the two variable fonts, but no config_yaml.
- The family directory had no override config.yaml and no upstream_info.md, so there was no earlier upstream_info.md content to preserve.
- gftools-packager commit 61ba31f ("Scoutie Sans: Version 1.001 added", 2026-07-02) onboarded version 1.001 and named upstream commit 1ad9780. google/fonts PR #10669, whose body named the same commit, merged it on 2026-07-03.

## Actions taken

- Verified the recorded commit. 1ad9780 ("Fix OFL copyright and finalize v1.001 sources", 2026-07-01 20:34 UTC) is the commit the annotated tag v1.001 points to (tagged 20:41 UTC the same day). It is still the head of main, and the upstream repository had no later commits. The two variable fonts and OFL.txt in the v1.001 release zip named by archive_url were byte-identical (SHA-256) to the files in google/fonts. Both fonts carry version 1.001 and head.modified 2026-07-01 20:46 UTC, minutes after the tag, which matches the upstream CI release job.
- Searched the upstream tree at 1ad9780 for a gftools-builder configuration. sources/config.yaml lists the two Glyphs 3 sources (Scoutie-Sans.glyphs, Scoutie-Sans-Italic.glyphs), sets familyName "Scoutie Sans" and defines per-file STAT tables. It is the only builder config in the tree. The upstream Makefile builds every sources/config*.yaml.
- Added config_yaml: "sources/config.yaml" to the source block. Nothing else in METADATA.pb changed.
- Built sources/config.yaml at 1ad9780 with gftools-builder3 3.0.0 (simoncozens/gftools-builder3 e851b8b, fontc 1.0.0). The build succeeded and produced Scoutie-Sans[wght].ttf and Scoutie-Sans-Italic[wght].ttf. The upstream Makefile renames these to ScoutieSans[wght].ttf and ScoutieSans-Italic[wght].ttf.
- Compared the builds with the shipped fonts. They matched in glyph set (960 glyphs), cmap (759 codepoints mapped to the same glyph names), wght axis (200-800, default 200), the 7 named instances, STAT axes, vertical metrics and name IDs 1, 2, 4, 6, 16 and 17. A functional comparison (cmap, HarfBuzz shaping, unhinted rendering, names, line spacing, advances, GDEF) found one difference per font: the uni00A0 advance (403 built, 420 shipped).
- Traced that difference to scripts/fix_fonts.py, which the upstream Makefile runs after gftools builder. The script copies the space's default advance (hmtx) to the no-break space, adds an identity avar table and cleans the copyright string. After this script ran on the builds, the functional comparison passed for both fonts, and all advance widths also matched at wght 400 and 800.
- Three name records outside that comparison still differed. They come from the toolchain rather than the sources:
  - Name ID 5: fontc appends ";fontc 1.0.0".
  - Name ID 14: the build kept the source's "https://openfontlicense.org/". The shipped fonts have "https://openfontlicense.org", which is the URL the Python gftools fix step writes.
  - Name ID 25: absent from the fontc build.

## Final state

- METADATA.pb records repository_url, the verified commit 1ad978084a859543cb76fe0de66b31b8fc67db2b, archive_url, files, branch and config_yaml "sources/config.yaml".
- A build of sources/config.yaml at the recorded commit reproduces the shipped variable fonts functionally once the upstream post-build step scripts/fix_fonts.py is applied. That step lives outside the gftools-builder config. Without it, the default no-break space advance differs and the avar table is missing.

## Update: version 1.003 (2026-11-13)

**Model**: Claude Fable 5.2

- After the checks above, google/fonts moved the family to version 1.003 (commit cc49734e6, "update to 1.003", Simon Cozens, 2026-10-06). METADATA.pb now records commit bac79adfafa587663c134599c2afc31b00c402c0 ("Release v1.003 sources", 2026-10-06), which is the tag v1.003 and the head of `main`, and the v1.003 release archive.
- Verified the new pin: the two shipped variable fonts and `OFL.txt` are byte-identical to the files in `scoutie-v1.003.zip`.
- `sources/config.yaml` and `scripts/fix_fonts.py` did not change between v1.001 and v1.003, and both sources the config lists exist at the new commit. The build comparison above was made at v1.001 and was not repeated.
- `config_yaml: "sources/config.yaml"` is added to the current source block.
