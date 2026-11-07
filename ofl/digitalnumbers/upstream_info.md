# Digital Numbers

## Summary

| Field | Value |
|---|---|
| **Family name** | Digital Numbers |
| **Designer** | Stephan Ahlf |
| **License** | OFL |
| **Date added** | 2015-06-24 |
| **Repository URL** | https://github.com/s-a/digital-numbers-font |
| **Commit** | `b58e33a259af2872522fcddbfd02dad3732ccadd` |
| **Config YAML** | N/A (SFD-only sources, not gftools-builder compatible) |
| **Status** | missing_config |

## Upstream Repository

The upstream repo at `s-a/digital-numbers-font` contains:
- `src/digital-numbers.sfd` - FontForge SFD source (the only source format)
- `dist/DigitalNumbers-Regular.ttf` - Pre-built TTF
- SVG and PNG source images in `src/`
- No `.glyphs`, `.ufo`, or `.designspace` files
- No `config.yaml` file

The repo was created by Stephan Ahlf and has commits up to `6c52a4a` (README update).

## Commit Verification

The tracked commit `b58e33a` ("updated description", 2015-06-08) was the latest commit in the repo at the time the font was added to Google Fonts by Dave Crossland on 2015-06-23 (commit `e860dd850` in google/fonts). This is confirmed by examining the timeline:
- `b58e33a` (2015-06-08) - last commit before onboarding
- `e860dd850` (2015-06-23) - font added to google/fonts
- `e5b4d59` (2015-06-06) - last commit that changed font sources (correctDirection fix)
- Later commits (`4172c78`, `8921f16`) were made after the font was onboarded

The commit `8921f16` explicitly references the google/fonts addition commit: "cut from https://github.com/google/fonts/commit/e860dd8502bff9c68f345ed29e82fe929038f4d6".

## Source Block Status

The METADATA.pb currently has:
```
source {
  repository_url: "https://github.com/s-a/digital-numbers-font"
}
```

The commit hash and repository URL were added in the batch commit `9a14639f3`.

## Build Configuration

This font uses SFD (FontForge) format sources exclusively. SFD is not compatible with gftools-builder, so a config.yaml is not applicable. The font would need to be rebuilt from scratch in a modern format (.glyphs or .ufo) to become gftools-builder compatible.

## Conclusion

- Repository URL: Verified correct
- Commit hash: Verified correct (`b58e33a` was the latest commit at time of onboarding)
- Config YAML: Not applicable (SFD-only sources)
- Status: `missing_config` - SFD-only sources, not gftools-builder compatible
