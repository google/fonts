# Investigation: Lemonada VF Beta

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lemonada VF Beta |
| Slug | lemonada-vf-beta |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block (no METADATA.pb found)
```

## Investigation

The directory `google/fonts/ofl/lemonadavfbeta/` exists but contains only:
- `LemonadaVFBeta.ttf`
- `OFL.txt`

There is no `METADATA.pb` file in this directory at all. This is an unusual situation.

The google/fonts git history shows:
- `a8d8b0994` — "Move VF Beta files to their own directories"
- `088ee305a` — "Add missing licenses"
- `11f456a09` — "Adjust license format"

The `a8d8b0994` commit description "Move VF Beta files to their own directories" suggests these were pre-release variable font beta versions that were moved to dedicated subdirectories. This is consistent with historical practice of storing preview/beta fonts without full metadata.

This appears to be a legacy beta preview of Lemonada's variable font, predating the full Lemonada variable font release (which is now in `ofl/lemonada/`). Without a METADATA.pb, this cannot be formally tracked in the same way as production fonts.

## Conclusion

No METADATA.pb exists for this entry. This appears to be a legacy VF beta preview of Lemonada that has since been superseded by the production `lemonada` family. The directory may be a historical artifact. No source tracking is needed for beta previews without METADATA.pb. This family should likely be flagged for cleanup review.
