**Model**: Claude Opus 4.6

## Tuffy

**Designer**: Thatcher Ulrich

### Upstream Repository Search

Tuffy was designed by Thatcher Ulrich and is available from his website tulrich.com. The font sources are in FontForge SFD format, originally hosted on SourceForge.

The following searches were conducted:

1. **tulrich GitHub**: Thatcher Ulrich's GitHub account (`tulrich`) was found but contained no font repositories (only game/graphics engine projects: dropoutspy, drums, floorplanner, etc.).
2. **deepin-community/fonts-tuffy**: A packaging repository was found containing SFD (FontForge) source files (`tuffy_regular.sfd`, `tuffy_bold.sfd`, `tuffy_italic.sfd`, `tuffy_bold_italic.sfd`) alongside compiled OTF/TTF files. However, SFD is a FontForge-specific format and does not meet the requirement for UFO or Glyphs sources.
3. **SourceForge**: The DESCRIPTION referenced a SourceForge CVS repository for the SFD sources, confirming FontForge as the original authoring tool.
4. **Broader searches**: No GitHub repository with UFO or Glyphs sources for Tuffy was found.

### Status

No canonical upstream repository with UFO or Glyphs sources was found. The original sources are in FontForge SFD format. No source block was added to `METADATA.pb`.

### Conclusion

Tuffy's sources exist in FontForge SFD format at SourceForge and are mirrored in deepin-community/fonts-tuffy, but SFD sources are not eligible per the source block policy (which requires UFO or Glyphs format). The font was released to the public domain.
