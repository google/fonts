# Investigation Report: Faculty Glyphic

## Summary

| Field | Value |
|---|---|
| **Family Name** | Faculty Glyphic |
| **Designer** | Koto Studio |
| **License** | OFL |
| **Repository URL** | https://github.com/DylanYoungKoto/FacultyGlyphic |
| **Commit** | `0f609bebfae8490a140feebfd3faacf3dfa87d62` |
| **Branch** | main |
| **Config YAML** | `sources/config.yaml` |
| **Status** | complete |
| **Confidence** | HIGH |

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/DylanYoungKoto/FacultyGlyphic"
  commit: "0f609bebfae8490a140feebfd3faacf3dfa87d62"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/FacultyGlyphic-Regular.ttf"
    dest_file: "FacultyGlyphic-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation Details

### Upstream Repository

- **URL**: https://github.com/DylanYoungKoto/FacultyGlyphic
- **Owner**: DylanYoungKoto (Dylan Young)
- **Created**: 2024-08-09
- **Last push**: 2024-10-29
- **Default branch**: main
- **Status**: Active, accessible

### Repository Structure (at commit `0f609be`)

```
AUTHORS.txt
CONTRIBUTORS.txt
documentation/
fonts/
  otf/
  ttf/
    FacultyGlyphic-Regular.ttf
Makefile
OFL.txt
README.md
requirements.in
requirements.txt
requirements-test.in
requirements-test.txt
scripts/
sources/
  config.yaml
  FacultyGlyphic .glyphspackage/
    fontinfo.plist
    glyphs/
    order.plist
```

### config.yaml Contents

```yaml
    sources:
      - FacultyGlyphic .glyphspackage
    familyName: "Faculty Glyphic"
    cleanUp: true
```

The config.yaml is present in the upstream repo at `sources/config.yaml`, as referenced in METADATA.pb.

### Commit History in google/fonts

1. **`007f15f3`** (2024-10-17) by Emma Marichal: "Faculty Glyphic: Version 1.003; ttfautohint (v1.8.4.7-5d5b) added"
   - Initial onboarding, merged via PR #8344 on 2024-10-18
   - Referenced upstream commit `54ab4ddfac95147ffb344c83756e999f60d5e409` ("Merge pull request #2 from emmamarichal/main", 2024-10-17)

2. **`9a17b498`** (2024-10-23) by Emma Marichal: "Faculty Glyphic: Version 1.004; ttfautohint (v1.8.4.7-5d5b) added"
   - Updated font version, merged via PR #8413 on 2024-10-23
   - Referenced upstream commit `217893d53b5e77627f997b41e75e45d5818bc0e2` ("Merge pull request #4 from emmamarichal/main", 2024-10-23)
   - Updated METADATA.pb commit hash from `54ab4dd` to `217893d`

3. **`e946eb4a`** (2024-10-23) by Emma Marichal: "Update METADATA.pb (designer)"
   - Changed designer from "Dylan Young" to "Koto Studio"

4. **`fd06e54a`** / **`adfbb1c9`** (2024-10-31/11-01): Article additions

5. **`19cdcec5`** (2025-03-31) by Felipe Sanches: "[Batch 1/4] port info from fontc_crater targets list"
   - Updated commit hash from `217893d` to `0f609be` and added `config_yaml: "sources/config.yaml"`

### Commit Hash Analysis

The current METADATA.pb references commit `0f609be` ("Update README.md", 2024-10-29), which is the latest commit on the upstream main branch. This commit only modified `README.md` -- no source files or config.yaml were changed. The font sources are identical between:

- `217893d` (the last commit referenced by the onboarding engineer, PR #8413)
- `0f609be` (the current HEAD, set by fontc_crater batch import)

The difference is a single README.md edit. Using the HEAD commit is acceptable since the binary font files and build sources are unchanged.

### Binary File Verification

The TTF file in google/fonts matches the upstream repo exactly:
- **SHA-256**: `27010aebf4430da073b75b8877bc3d3e35bd24d2e4f9403d34418abe94c3d31f`
- Both `ofl/facultyglyphic/FacultyGlyphic-Regular.ttf` and `fonts/ttf/FacultyGlyphic-Regular.ttf` in upstream produce identical hashes.

### Upstream Repository Notes

- The local clone at `upstream_repos/fontc_crater_cache/DylanYoungKoto/FacultyGlyphic` is a **shallow clone** (depth 1), which is why only the HEAD commit (`0f609be`) is visible locally. The full history (30+ commits) is available via the GitHub API.
- The upstream repo was created by Dylan Young on 2024-08-09. Emma Marichal (emmamarichal) contributed fixes and handled the Google Fonts onboarding via PRs #1, #2, and #4 to the upstream repo.
- The font is a single-weight Regular, sourced from a `.glyphspackage` file.

## Conclusion

The source metadata for Faculty Glyphic is **complete and correct**. The repository URL, commit hash, branch, and config_yaml path are all valid and verified. The binary font file in google/fonts matches the upstream repo. No changes are needed.
