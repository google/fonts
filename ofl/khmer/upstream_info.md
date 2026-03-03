# Investigation: Khmer

## Summary

| Field | Value |
|-------|-------|
| Family Name | Khmer |
| Slug | khmer |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Khmer has no `source` block. The font was present in the initial commit of google/fonts (`90abd17b4`), with an additional `chmod -x` commit (`49fbebd3d`).

The copyright notice credits "Danh Hong (khmertype.blogspot.com danhhong@gmail.com)" and mentions "Reserved Font Name Khmer OS."

The DESCRIPTION.en_us.html links to Danh Hong's blog (http://www.khmertype.blogspot.com) and the KhmerOS project.

The Khmer font is available as part of the KhmerOS project. The cached repository at `upstream_repos/fontc_crater_cache/librefonts/khmer` contains TTX dumps of the binary font. Danh Hong's GitHub repositories (`danhhong`) were checked but no "Khmer" repository was found — only more recent Khmer fonts like KohSantepheap, Koulen, Battambang, etc.

The "Khmer" font appears to predate GitHub-based workflows and may have been built using FontForge with Graphite/AAT tables (the TTX dump includes `_m_o_r_x_` and `_f_e_a_t_` tables which are Apple-specific). No gftools-builder compatible sources were found.

## Conclusion

The font is a very old Khmer font (2011) with no tracked upstream GitHub repository. The sources likely pre-date modern font tooling workflows. No `config.yaml` is possible. This family would require contacting Danh Hong or researching the KhmerOS project to find original sources.
