# Investigation Report: Geo

## Summary

Geo is a geometric sans-serif display typeface designed by Ben Weiner, added to Google Fonts on 2010-11-30. The font was part of the initial commit (90abd17b) to the google/fonts repository. The upstream repository is at `https://github.com/librefonts/geo` and contains only SFD (FontForge) source files -- no `.glyphs`, `.ufo`, or `.designspace` files, and no `config.yaml`. Since SFD sources are not compatible with gftools-builder, no config.yaml can be provided.

## Key Findings

| Field              | Value                                                    |
|--------------------|----------------------------------------------------------|
| Family Name        | Geo                                                      |
| Designer           | Ben Weiner                                               |
| Date Added         | 2010-11-30                                               |
| Repository URL     | https://github.com/librefonts/geo                        |
| Commit Hash        | 0d2a51963d3c6e52d7b8edc50a5d7b457bb1a663 (only commit)  |
| Config YAML        | None (SFD-only sources)                                  |
| Source Files       | src/Geo-Regular-TTF.sfd, src/Geo-Oblique-TTF.sfd        |
| Status             | no_config_possible                                       |
| Confidence         | HIGH                                                     |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has no `source { }` block at all. The font was added in the initial commit of the google/fonts repository (90abd17b, dated 2015-03-07 in git, but `date_added` shows 2010-11-30). No repository_url, commit hash, or config_yaml are recorded.

### Upstream Repository

The upstream repository at `https://github.com/librefonts/geo` is cached at `upstream_repos/fontc_crater_cache/librefonts/geo/`. It has a single commit:

- `0d2a519` (2014-10-17): "update .travis.yml"

This is a shallow/squashed history. The repo contains:
- **Source files**: `src/Geo-Regular-TTF.sfd` and `src/Geo-Oblique-TTF.sfd` (FontForge SFD format)
- **TTX decompositions**: Multiple `.ttx` files for both Regular and Oblique
- **No config.yaml** anywhere in the repo
- **No `.glyphs`, `.ufo`, or `.designspace` files**

Since the repo has only one commit, that commit (0d2a519) is the only valid reference. The font files in google/fonts have never been updated since the initial commit.

### Build Configuration

The upstream sources are in SFD (FontForge) format only. SFD files are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. Therefore, no config.yaml can be created -- neither as an upstream file nor as an override.

### Google Fonts History

The Geo font files (`Geo-Regular.ttf`, `Geo-Oblique.ttf`) have only been touched in the initial commit (90abd17b). No subsequent updates have been made to the binary fonts.

## Conclusion

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/geo"
  commit: "0d2a51963d3c6e52d7b8edc50a5d7b457bb1a663"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
}
```

### Status: no_config_possible

The upstream repo only has SFD sources, which are not compatible with gftools-builder. A `config_yaml` field cannot be set. The source block can still document the repository URL and commit for provenance tracking.
