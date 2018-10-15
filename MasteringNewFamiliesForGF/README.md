# A quick guide to mastering new families for Google Fonts.

## Useful resources

### Tools

- [Font Bakery](http://github.com/googlefonts/fontbakery)
- [gf-glyphs-scripts](https://github.com/googlefonts/gf-glyphs-scripts)

### Docs

- [Project Checklist](ProjectChecklist.md)
- [GlyphsApp Quick Start](QuickStartGlyphs.md)

## Mastering process

### Repo layout

Arrange your repo into the following folder structure - the following are **mandatory**:

    .
    ├── AUTHORS.txt
    ├── CONTRIBUTORS.txt
    ├── OFL.txt
    ├── README.md
    ├── fonts
    │   └── Notable-Regular.ttf
    └── sources
        └── Notable.glyphs

A good project to study is [github.com/googlefonts/mavenproFont](https://github.com/googlefonts/mavenproFont)

This has additional **optional** parts, like the `/docs` folder, which is a good place to put automatically generated content, or image files used in the README. Eg,

    ├── docs
    │   └── sample.png

Note that the `/docs` folder is special, because its contents is directly available to web browsers.

### Design Inspection

Check each glyph is good. A simple way to do this is copy all glyphs in GlyphsApp into a tab.

![All glyphs of a font open in a tab of GlyphsApp](assets/Mastering0.png 'All glyphs of a font open in a tab of GlyphsApp')

### Update Metadata so it's correct

Inside Glyphsapp with all open .glyphs sources execute the following:

Run Script > Google Fonts > QA. Fix everything until it clears

![Google Fonts QA Script](assets/Mastering1.png 'Google Fonts QA Script')

### Double Check designer/meta info

Ensure copyright, author names etc are correct.

![GlyphsApp font info window](assets/Mastering2.png 'GlyphsApp font info window')

### Generate TTFs and check with Fontbakery

![Checking TTF font files with FontBakery in the command line](assets/Mastering3.png 'Checking TTF font files with FontBakery in the command line')

Fix all FAILS/ERRORs until capcake appears. If error cannot be cleared, post issue to [https://github.com/googlefonts/fontbakery](https://github.com/googlefonts/fontbakery)

### Push changes to git!

Push your latest revision to github, and file a request for a family update or publication on [https://github.com/google/fonts/issues](https://github.com/google/fonts/issues)
