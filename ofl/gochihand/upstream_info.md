# Investigation Report: Gochi Hand

## Summary

Gochi Hand is a handwriting-style typeface designed by Juan Pablo del Peral for Huerta Tipografica, added to Google Fonts on 2011-10-05. The upstream repository is at `https://github.com/librefonts/gochihand`. The repo contains only SFD (FontForge) and VFB sources, making it incompatible with gftools-builder. No config.yaml is possible.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gochi Hand                                                         |
| Designer           | Huerta Tipografica (Juan Pablo del Peral)                          |
| Repository URL     | https://github.com/librefonts/gochihand                           |
| Commit Hash        | e202a9f4b7cd6f9c84440e684f0a3d0b5dd234e0                          |
| Config YAML        | N/A (SFD-only sources)                                             |
| Status             | no_config_possible                                                 |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb (current state on main)

The METADATA.pb on the `main` branch of google/fonts does **not** contain a source block. A source block was added on the branch `sources_info_2026-02-25` (commit `9a14639f3`) but has not yet been merged to main.

Current METADATA.pb fields:
- name: "Gochi Hand"
- designer: "Huerta Tipografica"
- license: OFL
- category: HANDWRITING
- date_added: 2011-10-05
- classifications: DISPLAY, HANDWRITING

### Git History in google/fonts

- **`90abd17b4`** (2015-03-07): Initial commit by Dave Crossland. Added `GochiHand-Regular.ttf`, `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `METADATA.json`, `OFL.txt`.
- **`480630de3`** (2015-12-08): METADATA.pb textproto created from METADATA.json.
- **`883939708`** (2016-01-11): METADATA.json removed.
- **`76adaf1d2`** (2021-11-01): Deploy commit deleted all gochihand files. This was on a non-main branch (`upstream/davelab6-date`, `upstream/gh-pages`).
- **`633ebadbf`** (2021-12-12): Language support metadata added. This is on main and the TTF file exists on main from the initial commit.
- **`47a6c224b`** (2023-08-08): Stroke and classifications added.
- **`9a14639f3`** (2026-02-25): Source block added on branch `sources_info_2026-02-25` (not yet on main).

The font binary has never been updated since the initial commit. The TTF was added in the Initial commit (`90abd17b4`, March 2015) and has not been modified since.

### Upstream Repository

Cached at: `upstream_repos/fontc_crater_cache/librefonts/gochihand`
Remote: `https://github.com/librefonts/gochihand`

The repository has exactly **one commit**:
- `e202a9f4b7cd6f9c84440e684f0a3d0b5dd234e0` (2014-10-17) by hash3g: "update .travis.yml"

This single commit is an initial import that created the entire repository with all files at once. The repo contains:
- `.travis.yml` (CI config for fontbakery)
- TTX decomposed tables of the TrueType font
- `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `METADATA.json`, `OFL.txt`
- `src/GochiHand-Regular-TTF.sfd` (FontForge SFD source)
- `src/GochiHand-Regular-OTF.vfb` (FontLab VFB source)
- TTX decomposed tables of the OTF in `src/`

### Source Files

The only editable source files are:
- `src/GochiHand-Regular-TTF.sfd` -- FontForge SFD format
- `src/GochiHand-Regular-OTF.vfb` -- FontLab VFB format (binary, not buildable by gftools)

Neither SFD nor VFB is supported by gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` files.

### Commit Hash Verification

The upstream repo has only one commit (`e202a9f`), which is also HEAD. The font was added to google/fonts in the initial commit of that repo (March 2015), after the upstream commit (October 2014). The single commit hash `e202a9f4b7cd6f9c84440e684f0a3d0b5dd234e0` is the correct and only possible reference.

### Config YAML

No config.yaml exists in the upstream repo. No config.yaml can be created because:
- The source format (SFD/VFB) is not supported by gftools-builder
- gftools-builder requires `.glyphs`, `.ufo`, or `.designspace` sources

## Conclusion

The upstream repository and commit hash are correctly identified. Since the sources are SFD/VFB only, no config.yaml is possible, and the status should be `no_config_possible`.

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/librefonts/gochihand"
  commit: "e202a9f4b7cd6f9c84440e684f0a3d0b5dd234e0"
}
```

No `config_yaml` field is applicable (SFD-only sources).
