# Investigation Report: Frank Ruhl Libre

## Summary

| Field | Value |
|---|---|
| Family Name | Frank Ruhl Libre |
| Designer | Yanek Iontef |
| License | OFL |
| Repository URL | https://github.com/fontef/frankruhllibre |
| Commit | `2372d1998e51dc011f86554c0d23f1ccf44afddf` |
| Branch | master |
| Config YAML | `sources/config.yaml` |
| Override Config | No |
| Status | **complete** |
| Confidence | **HIGH** |

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/fontef/frankruhllibre"
  commit: "2372d1998e51dc011f86554c0d23f1ccf44afddf"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/FrankRuhlLibre[wght].ttf"
    dest_file: "FrankRuhlLibre[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation Details

### Upstream Repository

The upstream repository is at https://github.com/fontef/frankruhllibre, maintained by Meir Sadan (fontef) and with significant contributions from Emma Marichal. The repo has 54 commits on master, with history going back to January 2016. The latest commit is `2372d19` (2024-02-25), which is the same commit referenced in METADATA.pb.

### Font History in google/fonts

Frank Ruhl Libre was first added to Google Fonts on 2016-06-20. The font has gone through several updates:

1. **Initial add** (2016) - Static TTF files for 5 weights
2. **v5.001 hotfix** (commit `0538aa296`, via PR #971)
3. **Version 6.000** (commit `347416452`, PR #5528, 2022-11-18) - Conversion to variable font (single `FrankRuhlLibre[wght].ttf`), removing the 5 static TTFs. Referenced upstream commit `f08f641`.
4. **Version 6.000 packager rebuild** (commit `17f173c7f`, PR #5852, 2023-02-01) - Rebuilt via gftools-packager
5. **Hotfix** (commit `1f8b42569`, 2023-02-01) - Bumped version number
6. **Version 6.002** (commit `488a9adcc`, PR #6178, 2023-04-12) - Referenced upstream commit `f276090`
7. **Version 6.003** (commit `7f75b40b4`, PR #6355, 2023-06-14) - Referenced upstream commit `82ba585`
8. **Version 6.004** (commit `3b340129b`, PR #7332, 2024-02-28) - Referenced upstream commit `2372d19` (current)

### Commit Hash Verification

The commit `2372d1998e51dc011f86554c0d23f1ccf44afddf` in METADATA.pb is:
- The HEAD of the `master` branch in the upstream repo
- A merge commit by Meir Sadan dated 2024-02-25: "Merge pull request #26 from emmamarichal/master" (Update Frank Ruhl Libre)
- Explicitly referenced in the google/fonts commit `3b340129b` message: "Frank Ruhl Libre Version 6.004 taken from the upstream repo https://github.com/fontef/frankruhllibre at commit https://github.com/fontef/frankruhllibre/commit/2372d1998e51dc011f86554c0d23f1ccf44afddf"

**Binary verification**: The `FrankRuhlLibre[wght].ttf` in google/fonts matches the file at `fonts/variable/FrankRuhlLibre[wght].ttf` in the upstream repo at this commit exactly (MD5: `ebc976487074831f0b7a12e43e36da20`, size: 178,468 bytes).

### Config YAML Verification

The file `sources/config.yaml` exists in the upstream repo at commit `2372d19`. It was first introduced at commit `e942d45` (2022-10-13) and has not been modified since. Contents:

```yaml
    sources:
      - FrankRuhlLibre.glyphs
    axisOrder:
      - wght
    familyName: Frank Ruhl Libre
    stat:
      FrankRuhlLibre[wght].ttf:
      - name: Weight
        tag: wght
        values:
        - name: Light
          value: 300
        - name: Regular
          value: 400
          linkedValue: 700
          flags: 2
        - name: Medium
          value: 500
        - name: SemiBold
          value: 600
        - name: Bold
          value: 700
        - name: ExtraBold
          value: 800
        - name: Black
          value: 900
```

The source file `sources/FrankRuhlLibre.glyphs` exists at this commit (Glyphs format v3).

### OFL.txt Difference

There is a minor difference between the OFL.txt files: the google/fonts copy references `https://openfontlicense.org` while the upstream copy references `https://scripts.sil.org/OFL`. This is a known URL migration for the OFL and is not material.

### Files Mapping

The METADATA.pb `files` entries correctly map:
- `OFL.txt` -> `OFL.txt` (license file at repo root)
- `fonts/variable/FrankRuhlLibre[wght].ttf` -> `FrankRuhlLibre[wght].ttf` (variable font binary)

### Notes

- The `config_yaml` field was added by the fontc_crater batch commit `19cdcec59` (2025-03-31) and correctly points to `sources/config.yaml` in the upstream repo.
- The `files` and `branch` fields were added by Simon Cozens' upstream.yaml merge commit `66f91f10f` (2024-04-03).
- No override config.yaml is needed since the upstream repo already has one.
- The upstream repo has had no commits since `2372d19` (2024-02-25), so there is no drift between google/fonts and upstream.
- The font was last updated by Emma Marichal via gftools-packager.

## Conclusion

All source metadata for Frank Ruhl Libre is complete and verified. The repository URL, commit hash, branch, config_yaml, and file mappings are all correct and consistent with the binary font file in google/fonts.
