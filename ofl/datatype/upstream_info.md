# Datatype: source metadata

**Provenance: verified** - 2026-09-27 - no gftools-builder config possible (Python-generated font) - **Model**: Claude Opus 5.5

| Repo | Commit | Config | Source |
|------|--------|--------|--------|
| [franktisellano/datatype](https://github.com/franktisellano/datatype) | `1a17d76` (tag v1.2.2 + README) | none possible | Python programs + fontTools; VF wdth,wght |

## Initial state

- METADATA.pb had a complete source block (repository_url, commit
  `1a17d767ba7fecd54d47ec11b2f7ed644a31513d`, branch `main`, files `OFL.txt` and
  `fonts/variable/Datatype[wdth,wght].ttf`) but no `config_yaml`, and the family directory
  had no override `config.yaml`.
- The gftools-packager commit 2a727e4 ("Datatype: Version 1.202 added") named upstream
  commit 1a17d76. PR #10267 merged it on 2026-02-26 (merge commit d2249ce).

## Actions taken

- Verified the recorded commit against a mirror of the upstream repo, fetched 2026-09-27.
  1a17d76 changed only `README.md`. Its parent 04e189f is tag v1.2.2, "Bump version to 1.2.2
  (font string: 1.202)". `fonts/variable/Datatype[wdth,wght].ttf` at 1a17d76 is
  byte-identical to the shipped font (sha256 ecc12db4d3d268be...). The shipped font's
  head.modified (2026-02-22 23:29:05, local time) is five minutes before the 04e189f commit.
  No upstream commit landed between 1a17d76 and the merge. The next one, 937a14a
  (2026-02-27), added only promo images and a `.gitignore` entry.
- Searched every ref of the mirror (main, tags v1.0.0 to v1.2.2, pull/1, pull/3) for
  gftools-builder inputs. None has a `.glyphs`, `.glyphspackage`, `.ufo` or `.designspace`
  file, or a YAML file with a `sources:` list. `python sources/build.py` draws every glyph in
  Python (the Latin outlines are unpickled from `sources/imported_glyphs.pkl`, which was
  extracted from IBM Plex Mono). It builds nine TTF masters with fontTools FontBuilder and
  merges them with fontTools varLib. There is no source for a config to point
  gftools-builder or fontc at, so no override `config.yaml` was written.
- Rebuilt the font twice with the upstream script at 1a17d76 (Python 3.11.15; fonttools
  4.60.2 and brotli 1.2.0, as pinned in `requirements.txt`). Both rebuilds were identical
  apart from the head timestamps and checksum. Compared with the shipped font, they differed
  only in:
  - the head timestamps and checksum;
  - the GSUB byte layout (the decompiled table is identical);
  - one point in each of `pie_21`, `pie_30`, `pie_53` and `pie_65`, which is at 679 in the
    shipped default master and at 680 in the rebuild, with the matching glyf, loca and gvar
    bytes. At the wght 100 and 900 masters these glyphs differ by at most 1 unit.

  That point is the first off-curve point of the inner ring arc. Its exact y value is 680,
  and `sources/glyphs/pie.py` truncates it with `int()`, so the last bit of `math.sin` and
  `math.cos` decides between 679 and 680. On this machine six other pie glyphs truncate to
  679, as they do in the shipped font. A probe showed that one-ulp changes in these results
  are enough to flip each of the four to 679. This is consistent with a floating-point
  difference between the author's platform and this one, not with a source change. A
  functional comparison (sfd-reland `tools/functional_gate.py`: HarfBuzz shaping,
  diffenator3 1.1.4 rendering) gave PASS:
  - 319 codepoints exact;
  - 630647 shaping runs with 0 differences;
  - 0 rendering differences;
  - names, line spacing, all 10850 advances and GDEF (absent) equal.

## Final state

- METADATA.pb is unchanged. repository_url, commit and branch are correct. `config_yaml`
  stays unset because the upstream has no gftools-builder config, and none that compiles
  font sources can be written.
- No override `config.yaml` was added.
- Status: no_config_possible. Confidence: HIGH.
- This file supersedes the upstream_info.md of 2026-03-03 (google/fonts commit 7380f7c), which
  reached the same conclusion without a local clone of the upstream repo. It is kept below.

## Open items

- The shipped `OFL.txt` lacks the IBM Plex Mono credit ("Copyright 2017 IBM Corp. with
  Reserved Font Name "Plex"") that the upstream `OFL.txt` carries. google/fonts commit
  2ed2495 removed it, although the font contains glyphs derived from IBM Plex Mono.
  Repackaging from 1a17d76 with the current `files` mapping would restore it.

## Previous upstream_info.md (2026-03-03, commit 7380f7ceb)

### Investigation Report: Datatype

#### Summary

Datatype is a variable font (with `wdth` and `wght` axes) designed by Frank Tisellano that turns text into charts. It was very recently added to Google Fonts on 2026-02-25 via PR #10267, authored by Emma Marichal. The upstream repository at `franktisellano/datatype` already has a complete source block in METADATA.pb with commit hash and repository URL. However, the font uses a custom Python-based build system rather than gftools-builder, so there is no config.yaml and none can be created.

#### Key Findings

| Field               | Value                                                    |
|---------------------|----------------------------------------------------------|
| Family Name         | Datatype                                                 |
| Designer            | Frank Tisellano                                          |
| License             | OFL                                                      |
| Date Added          | 2026-02-25                                               |
| Repository URL      | https://github.com/franktisellano/datatype               |
| Commit Hash         | 1a17d767ba7fecd54d47ec11b2f7ed644a31513d                 |
| Branch              | main                                                     |
| Config YAML         | None (custom Python build system, not gftools-builder)   |
| Source Types         | Custom Python (sources/build.py, sources/font_builder.py)|
| Status              | no_config_possible                                       |
| Confidence          | HIGH                                                     |

#### Investigation Details

##### METADATA.pb Analysis

The METADATA.pb at `ofl/datatype/METADATA.pb` already has a **complete source block**:

```
source {
  repository_url: "https://github.com/franktisellano/datatype"
  commit: "1a17d767ba7fecd54d47ec11b2f7ed644a31513d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Datatype[wdth,wght].ttf"
    dest_file: "Datatype[wdth,wght].ttf"
  }
  branch: "main"
}
```

The font file is a variable font: `Datatype[wdth,wght].ttf` with width axis (50-150) and weight axis (100-900).

##### Git History in google/fonts

Four commits touch this family:
1. `2a727e489` (2026-02-25, Emma Marichal): "Datatype: Version 1.202 added" -- initial onboarding
2. `2ed24956d`: "Remove IBM Plex copyright notice from OFL.txt"
3. `956f0091b`: "Add font information and contribution details to ARTICLE.en_us.html"
4. `91bf91951`: "Add sample_text section to METADATA.pb"

These were all merged via PR #10267 on 2026-02-26.

##### Upstream Repository Verification

The repository `https://github.com/franktisellano/datatype` was created on 2026-02-15. The referenced commit `1a17d767ba7fecd54d47ec11b2f7ed644a31513d` was authored on 2026-02-23 with the message "gives well-deserved thanks to Emma and Dave for their guidance and support". This commit predates the PR merge on 2026-02-26, which is consistent.

The commit message in google/fonts explicitly states: "Taken from the upstream repo https://github.com/franktisellano/datatype at commit https://github.com/franktisellano/datatype/commit/1a17d767ba7fecd54d47ec11b2f7ed644a31513d."

##### Source Files and Build System

The upstream repo does **not** use gftools-builder. Instead, it has a custom Python-based build system:

- `sources/build.py` -- Main build script that orchestrates font generation
- `sources/font_builder.py` -- Font building utilities
- `sources/config.py` -- Configuration for family name, axes, masters, instances
- `sources/glyphs/` -- Python modules that programmatically draw glyphs (bar charts, sparklines, pie charts)
- `sources/glyphs/base_imported.py` -- Imports base glyphs from IBM Plex Mono
- `Makefile` -- Runs `python sources/build.py`

The font is built programmatically rather than designed in a traditional font editor. There are no `.glyphs`, `.ufo`, or `.designspace` files. The build is invoked via `make build` which runs `python sources/build.py`.

No `config.yaml` exists in the upstream repo, and an override config.yaml cannot be created because there are no gftools-builder compatible source files.

The repo is **not cached locally** at `fontc_crater_cache/`. Due to disk space constraints (98%), no clone was performed.

##### Onboarding Commit Verification

The commit hash `1a17d767ba7fecd54d47ec11b2f7ed644a31513d` is verified:
- It exists in the upstream repo on the `main` branch
- It was authored on 2026-02-23, three days before the PR merge on 2026-02-26
- The PR commit message explicitly references this exact commit
- The files entry references `fonts/variable/Datatype[wdth,wght].ttf` which is present at that commit

#### Conclusion

**Status: no_config_possible**

The source block in METADATA.pb is already complete and correct. The font uses a custom Python build system (not gftools-builder), so no config.yaml is applicable. No changes are needed for this family.

##### Current METADATA.pb source block (already correct)

```
source {
  repository_url: "https://github.com/franktisellano/datatype"
  commit: "1a17d767ba7fecd54d47ec11b2f7ed644a31513d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Datatype[wdth,wght].ttf"
    dest_file: "Datatype[wdth,wght].ttf"
  }
  branch: "main"
}
```
