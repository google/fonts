# Investigation: Katibeh

## Summary

| Field | Value |
|-------|-------|
| Family Name | Katibeh |
| Slug | katibeh |
| License Dir | ofl |
| Repository URL | https://github.com/Tarobish/Katibeh |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Katibeh has no `source` block. The font was added on May 23, 2017 via commit `24319bb5f` ("hotfix-katibeh: v1.001 added (#980)").

The commit message and DESCRIPTION.en_us.html both reference the upstream repository: `https://github.com/Tarobish/Katibeh`. This was identified from the DESCRIPTION.en_us.html which states: "To contribute, see github.com/Tarobish/Katibeh".

The upstream repository `Tarobish/Katibeh` is cached at `upstream_repos/fontc_crater_cache/Tarobish/Katibeh`. The repository contains:
- `Sources/Katibeh Master.glyphs` (Glyphs format)
- `Sources/Katibeh-LATIN-OPEN.glyphs`
- `Sources/technical-additions.sfd` (FontForge SFD)
- `Sources/features.fea`, `Sources/pos-specific.fea`
- No `config.yaml`

The git log shows only one commit: `3fde990` ("Merge branch 'gh-pages' of github.com:Tarobish/Katibeh into gh-pages"). This seems to be the gh-pages branch - the repository may have a master branch. The commit was confirmed by checking the cached repo.

The description credits "KB Studio" (www.k-b-studio.com / tarobish@gmail.com), "Lasse Fister" (graphicore.de), and "Eduardo Tunni" (tipo.net.ar).

## Conclusion

The upstream repository URL has been identified as `https://github.com/Tarobish/Katibeh`. A source block needs to be added to METADATA.pb with this URL, a commit hash (to be verified), and a config.yaml path or override. The repository contains Glyphs sources but no config.yaml.
