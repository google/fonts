# Akt: upstream source metadata

**Model**: Claude Opus 5.5

## Initial state

- `ofl/akt/METADATA.pb` had a source block with `repository_url` https://github.com/dimgrenev/akt, `commit` b3935082b52ae393aef02a679505c028a5256c72, `branch` main and file mappings for `OFL.txt` and `fonts/variable/Akt[wght].ttf`. It had no `config_yaml`.
- The family directory had no override `config.yaml` and no earlier `upstream_info.md`, so there was no earlier content to preserve.
- The family was onboarded in google/fonts commit 88def5c ("Akt: Version 1.100 added", Emma Marichal, 2026-04-24) and merged through PR #10468 on 2026-04-29.

## Actions taken

- Verified the recorded commit. The shipped `Akt[wght].ttf` (git blob fbb52fd7) is byte-identical to `fonts/variable/Akt[wght].ttf` at b3935082 ("Rebuild fonts after glyph update", 2026-04-24), the commit where this binary first appears. `OFL.txt` is identical too. b3935082 is still the head of upstream `main` (mirror fetch and `git ls-remote` on 2026-09-27). The only later upstream work is the unmerged pull request #2 ("Add rupee glyph", 2026-09-23).
- Found the gftools-builder configuration at `sources/config.yaml` (`sources: [Akt.glyphs]`, `axisOrder: [wght]`). Upstream's own `METADATA.pb` also references it.
- Built b3935082 with gftools-builder 3.0.0 (e851b8b, fontc 1.0.0) using `sources/config.yaml`. The build succeeded. Glyph set (1867), cmap (1275 codepoints), axis, 9 instances, advances, vertical metrics and version 1.100 matched the shipped font.
- Ran `sfd-reland/tools/functional_gate.py` on the shipped and built fonts. It reported FAIL on shaping only: 89 of 6,938,749 runs differ. All of the differences come from 10 glyph-pair kerning pairs involving `space` that the shipped font does not contain.
- Traced this to the upstream `makefile`. After `gftools builder`, `make build` runs `tools/add_avar_identity.py`, `tools/add_meta.py`, `tools/fix_names.py` and `tools/cleanup_gpos_pairpos1.py`. The last of these deletes the format 1 (glyph pair) subtables of plain PairPos lookups and leaves Extension-wrapped PairPos lookups untouched. Both the shipped font and the fontc build keep 85 glyph pairs involving `space` in an Extension kern lookup; the fontc build has its 10 extra pairs in the plain kern lookup, where the script removes them. After these four scripts were applied to the fontc build, the gate reported functional PASS (0 of 6,938,749 runs differ).
- Added `config_yaml: "sources/config.yaml"` to the source block.

## Final state

- The `METADATA.pb` source block records the repository, commit b3935082, branch `main` and `config_yaml: "sources/config.yaml"`. No override `config.yaml` is used.
- A build from `sources/config.yaml` alone matches the shipped font in glyphs, cmap, axes, instances and advances. It keeps 10 `space` kerning pairs and lacks the identity `avar`, the `meta` table, name ID 25 and the Macintosh-platform name records; upstream's makefile post-processing scripts listed above remove the pairs and add the rest.
