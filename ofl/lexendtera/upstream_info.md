# Investigation Report: Lexend Tera

**Family Name**: Lexend Tera
**Directory**: `ofl/lexendtera`
**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Confidence**: HIGH

## Summary

Lexend Tera is one of eight Lexend sub-families (Lexend, Deca, Exa, Giga, Mega, Peta, Tera, Zetta) all built from the same upstream repository. The source block in METADATA.pb was already fully populated with repository URL, commit hash, config path, file mappings, and branch. All data was verified as correct through binary comparison and PR history analysis.

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/googlefonts/lexend"
  commit: "20491885ca2cf7ffc556432973e7bdbc701952b5"
  config_yaml: "sources/tera.yaml"
  files {
    source_file: "fonts/tera/variable/LexendTera[wght].ttf"
    dest_file: "LexendTera[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
```

## Upstream Repository

- **URL**: https://github.com/googlefonts/lexend
- **Local cache**: `upstream_repos/fontc_crater_cache/googlefonts/lexend/`
- **Source type**: Glyphs (`.glyphs` file)
- **Build config**: `sources/tera.yaml` (gftools-builder YAML config)
- **Source file**: `sources/Lexend.glyphs` (shared across all Lexend sub-families)

## Commit Hash Verification

The METADATA.pb references commit `20491885ca2cf7ffc556432973e7bdbc701952b5`.

### Verification Steps

1. **google/fonts history**: The last commit to modify `ofl/lexendtera/LexendTera[wght].ttf` was `beda156f5` ("Lexend Tera: Version 1.007 added [...] (#3623)"), merged on 2021-07-30. The squashed commit body explicitly stated: "Lexend Tera Version 1.007 taken from the upstream repo https://github.com/googlefonts/lexend at commit [...]/20491885ca2cf7ffc556432973e7bdbc701952b5."

2. **PR #3623 analysis**: The PR was authored by Rosalie Wagner (RosaWagner). The PR body initially referenced an earlier commit `9455faee86b7f915f7633301c48dc9125c2d4b49` (from gftools-packager), but the final squashed merge used commit `2049188`. Investigation revealed that between `9455fae` (2021-07-30 15:33) and `2049188` (2021-07-30 18:27), Rosa Wagner merged PR #2 which re-added a forgotten parenthesis in the copyright string (`6b22831`). This changed the font binaries slightly (192,540 bytes at `9455fae` vs. 192,544 bytes at `2049188`).

3. **Binary comparison**: The font binary at commit `2049188` in the upstream repo exactly matched the binary in google/fonts:
   - Upstream blob SHA256: `153c623deb39a4a79f26972e1a7b61651c16f9d567d4af83be2942303307dfac`
   - google/fonts SHA256: `153c623deb39a4a79f26972e1a7b61651c16f9d567d4af83be2942303307dfac`
   - File size: 192,544 bytes (both match)

4. **OFL.txt comparison**: The OFL.txt file at commit `2049188` also matched exactly (SHA256: `5da8505887d0fa7fe963445fd58852707fda34adfeb65af25c99d152bab285bd`).

**Conclusion**: Commit `20491885ca2cf7ffc556432973e7bdbc701952b5` is confirmed as the correct onboarding commit. The PR body's reference to `9455fae` was a gftools-packager hint from before the copyright fix was applied; the actual fonts shipped from the later commit.

## Config YAML Verification

The config file `sources/tera.yaml` existed at the referenced commit and was a valid gftools-builder configuration:

```yaml
    sources:
      - Lexend.glyphs
    familyName: "Lexend Tera"
    outputDir: ../fonts/tera
    buildStatic: False
    buildWebfont: False
    axisOrder:
      - wght
    stat:
      - name: Weight
        tag: wght
        values:
        - name: Thin
          value: 100
        ...
        - name: Black
          value: 900
```

The config file was unchanged between the referenced commit and the current main branch.

## Upstream Activity Since Onboarding

There were 21 commits on main after `2049188`, mostly CI/workflow changes and a HEXP axis build experiment (PR #12, September 2022). The most recent upstream commit was `7894f02` (March 2023, a README update). None of these changes have been pulled into google/fonts.

## Prior Source Block History

The source block was added incrementally:
- The `repository_url` and `files` mappings were populated by automated tooling (commit `f7455d788`, "Populate source.repository_url"; commit `66f91f10f`, "Merge upstream.yaml into METADATA.pb").
- The `commit` and `config_yaml` fields were added in commit `11e18675f` (2025-04-02, "sources info for Lexend (incl. Deca, Exa, Giga, Mega, Peta, Tera & Zetta)") by Felipe Sanches as part of the source metadata enrichment project.

## Conclusion

The Lexend Tera source block is complete and fully verified. No changes are needed.
