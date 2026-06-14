# Investigation: Hanna

## Summary

| Field | Value |
|-------|-------|
| Family Name | Hanna |
| Slug | hanna |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

(No METADATA.pb exists for this family. It is an Early Access font.)

## Investigation

The family directory is at `ofl/hanna/` and contains:
- `BM-HANNA.ttf`
- `DESCRIPTION.en_us.html`
- `EARLY_ACCESS.category` (value: "Sans Serif")
- `OFL.txt`

**No METADATA.pb exists.** This is an Early Access font that predates the modern METADATA.pb onboarding process.

### Git History

```
90abd17b4  2015-03-07  Initial commit
49fbebd3d             chmod -x {apache,ofl,ufl}/*/*.*
96df2d3e5             Updating Hanna EARLY_ACCESS.category to Sans Serif
28fff5fa7             Renaming EARLYACCESS.category files to EARLY_ACCESS.category
4f889caf0             Adding Early Access category files
```

- **commit `90abd17b4`** (2015-03-07, Dave Crossland): The font was added in the very first "Initial commit" of the google/fonts repository. The initial commit included `BM-HANNA.ttf`, `DESCRIPTION.en_us.html`, and `OFL.txt`.

### Creator Information

The `DESCRIPTION.en_us.html` states:
> "Woowa Brothers, a company dedicated to contributing to the world's graceful progress by utilizing information technology, has created the 'Hanna' font for everyone to use."

The `OFL.txt` copyright line reads:
> "Copyright 2013 Woowa Brothers Corporation (help@woowahan.com), with Reserved Font Name 'Hanna'"

**Woowa Brothers** (우아한형제들) is a South Korean company best known for the food delivery app "Baemin" (배달의민족). The font is named "BM-HANNA" (Baemin Hanna).

### Upstream Repository Search

No GitHub repository URL appears in any file within the `ofl/hanna/` directory. The description only contains prose with no hyperlinks. No `upstream.yaml` or `METADATA.json` exists.

The font "BM-HANNA" (Baemin Hanna) was released as a free font by Woowa Brothers. They have released multiple Korean fonts, but the specific source repository for BM-Hanna is not documented in the google/fonts commit history.

Woowa Brothers is known to have released fonts on their corporate site (https://www.woowahan.com). A GitHub repository may exist but is not referenced in any google/fonts metadata.

The upstream repo `woowahan` or similar is **not** found in `upstream_repos/fontc_crater_cache/`.

### No config.yaml Known

The font file `BM-HANNA.ttf` is a binary-only delivery. Korean corporate fonts often do not have open-source build toolchains. The source format is unknown.

## Conclusion

This Early Access font by Woowa Brothers Corporation has no documented upstream repository in google/fonts. The `BM-HANNA.ttf` was included in the very first commit of the repository (March 2015) with no reference to an upstream source location.

**Action needed**: Investigate whether Woowa Brothers has published a GitHub repository for BM-Hanna (check https://github.com/woowahan-company or similar). If a source repository exists, clone it, identify the applicable commit, and create a METADATA.pb. If no source repo is available (binary-only distribution), this family may be a candidate for `missing_url` with a note that the upstream is a closed corporate release.

**Person to ask**: The Google Fonts team (Dave Crossland onboarded this in the initial commit) or Woowa Brothers directly at help@woowahan.com.
