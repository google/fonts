# Investigation Report: Goldman

## Summary

Goldman is a display typeface designed by Jaikishan Patel, added to Google Fonts on 2020-07-22 via PR #2569. The upstream repository is at `https://github.com/magictype/goldman`. The source block with repository URL and commit hash is already present on the `main` branch of google/fonts, along with an override config.yaml. The family is complete.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Goldman                                                            |
| Designer           | Jaikishan Patel                                                    |
| Repository URL     | https://github.com/magictype/goldman                              |
| Commit Hash        | 3fdf428a931f7a39b3f2f1681c16bfa664ca89dd                          |
| Config YAML        | Override config.yaml in google/fonts                               |
| Status             | complete                                                           |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb (current state on main)

The METADATA.pb on the `main` branch already contains a complete source block:

```
source {
  repository_url: "https://github.com/magictype/goldman"
  commit: "3fdf428a931f7a39b3f2f1681c16bfa664ca89dd"
}
```

Other key fields:
- name: "Goldman"
- designer: "Jaikishan Patel"
- license: OFL
- category: DISPLAY
- date_added: 2020-07-22
- Two weights: Regular (400) and Bold (700)
- Subsets: latin, latin-ext, menu, vietnamese
- stroke: SANS_SERIF, classifications: DISPLAY

### Git History in google/fonts

- **`37e0f8a4f`** (2020-07-23): Onboarding by Viviana Monsalve. Commit message: "[Font Bakery Dashboard] create: ofl/goldman (#2569)". Added `Goldman-Regular.ttf`, `Goldman-Bold.ttf`, `DESCRIPTION.en_us.html`, `METADATA.pb`, `OFL.txt`.
- **`f7455d788`** (2023-08-15): Simon Cozens populated `source.repository_url` field.
- **`2423d2aef`** (2023-12-14): Simon Cozens "Update upstreams" -- added the source block with repository_url (this was the version that landed on main).
- **`36dbd4af7`** (2025-10-30): Felipe Sanches added commit hash and override config.yaml. Commit message: "sources info for Goldman v1.000 (PR #2569)". This was on branches that were merged to main.

### Upstream Repository

Cached at: `upstream_repos/fontc_crater_cache/magictype/goldman`
Remote: `https://github.com/magictype/goldman`

The repository HEAD is at `3fdf428a931f7a39b3f2f1681c16bfa664ca89dd`, which matches the commit hash in METADATA.pb. This is the latest commit (a merge of PR #10: "Merge pull request #10 from vv-monsalve/master"), dated 2020-07-22, one day before the google/fonts onboarding commit.

Repository structure:
- `sources/Goldman.glyphs` (Glyphs format, 1.15 MB)
- `sources/build.sh` (custom build script using fontmake)
- `fonts/ttf/Goldman-Regular.ttf`, `fonts/ttf/Goldman-Bold.ttf`
- `fonts/otf/`, `fonts/woff2/`
- `AUTHORS.txt`, `CONTRIBUTORS.txt`, `Copyright.txt`, `DESCRIPTION.en_us.html`
- `OFL.txt`, `README.md`, `requirements.txt`

### Source Files

The primary source file is `sources/Goldman.glyphs` (Glyphs format). This is compatible with gftools-builder.

The repo also contains `sources/build.sh`, a custom build script that uses fontmake directly:
```bash
fontmake -g Goldman.glyphs -o ttf -i --output-dir ../fonts/ttf -a
```

### Commit Hash Verification

The commit `3fdf428` is the HEAD and last commit of the repository. It was created on 2020-07-22, which is the `date_added` in METADATA.pb and one day before the google/fonts onboarding commit (`37e0f8a4f`, 2020-07-23). The timing is consistent: the upstream PR #10 was merged on July 22, and the font was onboarded the next day (July 23). There are no subsequent commits in the upstream repo, so `3fdf428` is definitively the correct onboarding commit.

### Config YAML

The upstream repo does **not** have a `config.yaml`. It uses a custom `sources/build.sh` script instead.

An override `config.yaml` has been created in the google/fonts family directory (`ofl/goldman/config.yaml`):
```yaml
buildVariable: false
sources:
  - sources/Goldman.glyphs
```

This override is present on the `main` branch. Since google-fonts-sources auto-detects local override config.yaml files, no `config_yaml` field is needed in the METADATA.pb source block.

## Conclusion

Goldman is fully complete. The source block with repository URL and commit hash is on main. An override config.yaml exists in google/fonts. No further action is needed.

### Current METADATA.pb source block (already on main)

```
source {
  repository_url: "https://github.com/magictype/goldman"
  commit: "3fdf428a931f7a39b3f2f1681c16bfa664ca89dd"
}
```

Override config.yaml in `ofl/goldman/config.yaml`:
```yaml
buildVariable: false
sources:
  - sources/Goldman.glyphs
```
