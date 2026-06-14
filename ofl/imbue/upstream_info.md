# Investigation: Imbue

## Summary

| Field | Value |
|-------|-------|
| Family Name | Imbue |
| Slug | imbue |
| License Dir | ofl |
| Repository URL | https://github.com/Etcetera-Type-Co/Imbue |
| Commit Hash | 41b16f3fd61d33cacad0e579c35ef9566817184b |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Etcetera-Type-Co/Imbue"
  commit: "41b16f3fd61d33cacad0e579c35ef9566817184b"
  files {
    source_file: "fonts/variable/Imbue[opsz,wght].ttf"
    dest_file: "Imbue[opsz,wght].ttf"
  }
  files {
    source_file: "fonts/ttf/Imbue10pt-Black.ttf"
    dest_file: "static/Imbue10pt-Black.ttf"
  }
  ... (additional static file mappings)
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb at `ofl/imbue/METADATA.pb` contains a complete source block with repository URL, commit hash, file mappings, and branch. The font was added to google/fonts via PR #2805, committed by Rosalie Wagner (commit `5377e4c5ca6b224e0deb0dee313888bb46eaea35`).

The PR commit message body explicitly states:

> "Imbue Version 1.102 taken from the upstream repo https://github.com/Etcetera-Type-Co/Imbue at commit https://github.com/Etcetera-Type-Co/Imbue/commit/41b16f3fd61d33cacad0e579c35ef9566817184b."

This directly confirms the repository URL and commit hash recorded in METADATA.pb.

The upstream repository `https://github.com/Etcetera-Type-Co/Imbue` is available in the cache at `upstream_repos/fontc_crater_cache/Etcetera-Type-Co/Imbue`. Commit `41b16f3fd61d33cacad0e579c35ef9566817184b` exists in the cached repository with the message "Merge pull request #2 from RosaWagner/master" (dated 2020-12-01), confirming this is the correct merge commit for version 1.102.

The upstream repository contains the Glyphs source file `Sources/Imbue.glyphs`. There is no `config.yaml` in the upstream repository, but an override `config.yaml` exists in `ofl/imbue/config.yaml` within google/fonts with the following content:

```yaml
buildVariable: true
sources:
  - Sources/Imbue.glyphs
```

This config correctly references the Glyphs source file that exists in the upstream repo. The `build.sh` and `build-others.sh` shell scripts in `Sources/` are legacy build scripts.

Note: The METADATA.pb also includes explicit `files {}` mappings for the prebuilt TTFs, which means gftools-packager fetched the prebuilt binaries rather than compiling from source. This is consistent with the variable font era approach used for Imbue 1.102.

## Conclusion

The source block in METADATA.pb is complete and correct. The repository URL points to `Etcetera-Type-Co/Imbue`, the commit hash `41b16f3` is verified to exist in the cached repo, and an override `config.yaml` is present in the google/fonts family directory. No action is needed.
