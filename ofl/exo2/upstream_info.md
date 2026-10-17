# Investigation Report: Exo 2

## Family Details
- **Family name**: Exo 2
- **Designer**: Natanael Gama
- **License**: OFL
- **Category**: Sans Serif
- **Date added**: 2013-12-04
- **Google Fonts path**: `ofl/exo2/`

## Source Metadata Status
- **Status**: complete
- **Confidence**: HIGH
- **Repository URL**: https://github.com/googlefonts/Exo-2.0
- **Commit**: `f83ea8a02d3e1d6963ab6e910038521f27e283a2`
- **Branch**: master
- **Config**: `sources/config.yaml` (in upstream repo)

## METADATA.pb Source Block

The METADATA.pb already contains a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/Exo-2.0"
  commit: "f83ea8a02d3e1d6963ab6e910038521f27e283a2"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Exo2[wght].ttf"
    dest_file: "Exo2[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Exo2-Italic[wght].ttf"
    dest_file: "Exo2-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Repository Investigation

### Upstream Repository

The upstream repository is at https://github.com/googlefonts/Exo-2.0. This was originally hosted at https://github.com/NDISCOVER/Exo-2.0 (Natanael Gama's GitHub account). The NDISCOVER repo still exists (HTTP 200), but the googlefonts fork is now the canonical upstream.

The repository was transferred/forked to googlefonts as part of the v2.010 update by Emma Marichal in September-October 2024.

### Repository Cache

The upstream repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/Exo-2.0/`. The repo is clean (only a deleted `.ninja_log` build artifact).

The original NDISCOVER/Exo-1.0 (Exo version 1) is also cached at `upstream_repos/fontc_crater_cache/NDISCOVER/Exo-1.0/`.

### Source Files

The upstream repo contains the following source files at HEAD (`f83ea8a`):

- `sources/Glyphs/Exo2.glyphs` (Glyphs source, Roman)
- `sources/Glyphs/Exo2-Italic.glyphs` (Glyphs source, Italic)
- `sources/Exo2.designspace` (designspace, Roman - commented out in config.yaml)
- `sources/Exo2-Italic.designspace` (designspace, Italic - commented out in config.yaml)
- `sources/Exo 2-Regular.ufo`, `sources/Exo 2-Thin.ufo`, `sources/Exo 2-Black.ufo` (UFO masters, Roman)
- `sources/Exo 2-Italic.ufo`, `sources/Exo 2-Thin Italic.ufo`, `sources/Exo 2-Black Italic.ufo` (UFO masters, Italic)

### Config.yaml

The `sources/config.yaml` file exists in the upstream repo and uses the Glyphs sources:

```yaml
sources:
  # - Exo2.designspace
  # - Exo2-Italic.designspace
  - Glyphs/Exo2.glyphs
  - Glyphs/Exo2-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Exo2
stat: [...]
```

The designspace sources are commented out; the active sources are the Glyphs files. No override config.yaml exists in the google/fonts family directory.

## Onboarding History

### Version Timeline

1. **Initial commit** (2013-12-04): Exo 2 added to Google Fonts as static font files.

2. **v1.100** (`907d74f`, undated in commit message): Static font update.

3. **v2.000** (`f3742603`, 2020-03-10): Conversion from static to variable fonts. Taken from NDISCOVER/Exo-2.0 at commit `6ce85fdb06fc174d485ad70a15afbcbf23ff2b53` (2020-03-09, "Merge pull request #8 from m4rc1e/gf-fix" by NDISCOVER). Work was done by Marc Foley (m4rc1e) and Denis Moyogo Jacquerye at TypeNetwork. This was the variable font onboarding.

4. **v2.002 STAT fix** (`8d29a3e`, PR #3636, 2021-08-17): Rebuilt fonts with STAT table fix. Done by Aaron Bell (aaronbell), who updated the repo to UFR format, fixed a quotesinglbase incompatibility, and bumped the version. Co-authored with Marc Foley. This used upstream commit `182060cd38adf3cde0d22add3f8009d30bd48cde` (2021-10-11, "Merge pull request #22 from aaronbell/master").

5. **v2.001 via gftools-packager** (`afab6b16`, PR #4767, 2022-06-16): METADATA.pb update only (no font binary changes). Added the initial source block pointing to NDISCOVER/Exo-2.0 at commit `182060cd`. Done by Emma Marichal.

6. **v2.010 (first attempt)** (`f286865`, PR #8209, 2024-09-26, merged 2024-10-01): Font binary update taken from googlefonts/Exo-2.0 at commit `54902ff3d6cf21615ca8de74727e316ceb363a14` (2024-09-20, "Merge pull request #1 from emmamarichal/master"). This was Emma Marichal's work to update the sources - she created Glyphs sources, fixed FontBakery issues, added axis mapping/rvrn features, and fixed interpolation issues.

7. **v2.010 (final)** (`8445cfa`, PR #8273, 2024-10-04, merged 2024-10-08): Font binary update taken from googlefonts/Exo-2.0 at commit `f83ea8a02d3e1d6963ab6e910038521f27e283a2` (2024-10-04, "Merge pull request #2 from emmamarichal/master"). This updated the copyright strings to reference googlefonts/Exo-2.0 instead of NDISCOVER/Exo-2.0. This is the current state.

8. **Batch port** (`19cdcec`, 2025-03-31): Added `config_yaml: "sources/config.yaml"` to the source block, ported from fontc_crater targets list.

### Commit Hash Verification

The commit hash `f83ea8a02d3e1d6963ab6e910038521f27e283a2` in METADATA.pb is correct and verified:

- It is the HEAD of the master branch of googlefonts/Exo-2.0
- It is a merge commit from 2024-10-04 by Emma Marichal ("changed repo url in copyright")
- It is explicitly referenced in the google/fonts commit `8445cfa` message and PR #8273
- The fonts in google/fonts were last updated from this exact commit
- The repo only has one merge commit at HEAD (this is it), and it is the latest commit in the repo

### Repository Ownership

The repo was originally under NDISCOVER (Natanael Gama's account). The timeline shows:
- Pre-2024: All references point to `NDISCOVER/Exo-2.0`
- September 2024: Emma Marichal created the googlefonts fork and did substantial work (Glyphs source creation, fixes)
- October 2024: The copyright and METADATA.pb were updated to point to `googlefonts/Exo-2.0`

## Conclusion

This family is **complete**. All source metadata fields are present and verified:
- Repository URL is valid and accessible
- Commit hash matches the latest font binary update (v2.010, October 2024)
- Config.yaml exists in the upstream repo at `sources/config.yaml`
- Source files are Glyphs format (.glyphs) with UFO and designspace also present
- No override config.yaml is needed
