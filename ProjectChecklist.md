# Introduction

This page lists how to learn enough about Git to move an open font project available in this Mercurial repository to a Git repository, and how to manage a open font project with it.

## Tools

### Mobile

Testing your type on mobile devices is essential, and more important than on desktops.
You'll need both iOS and Android devices to do this testing.

- [ ] iPhone 4S+ with iOS 8+ ([reference](https://david-smith.org/iosversionstats/))
- [ ] Android 4.x or higher (ideally latest) with a "normal" size screen ([reference](https://developer.android.com/about/dashboards/index.html))

### Windows

You will need a Windows 7 computer, real or virtual machine, for testing your fonts as web fonts.
Windows 7 is the most commonly used desktop operating system ([reference](https://en.wikipedia.org/wiki/Usage_share_of_operating_systems)), and also the most challenging font rendering system compared to alternatives.

- [ ] Microsoft offers zero-price virtual machine images at https://dev.modern.ie/tools/vms/mac/
- [ ] MSIE
- [ ] Firefox
- [ ] Chrome
- [ ] Safari
- [ ] Opeta

### Mac

- [ ] Homebrew is a package manager for installing unix tools, such as FontForge. http://brew.sh
```sh
brew install fontforge;
```

- [ ] pip is a package manager for installing python tools. https://pip.pypa.io
```
pip install pyfontaine;
pip install fontbakery;
```

- [ ] FontForge http://fontforge.github.io
- [ ] Glyphs https://glyphsapp.com
- [ ] FontLab https://fontlab.com
- [ ] OTMaster http://dtl.nl

## Project Repository

- [ ] Set up a Github Repo

New to Git and Github? Play the http://try.github.io 15 minute interactive game, and read http://nvie.com/posts/a-successful-git-branching-model, an essay about using Git for ongoing project management.

- [ ] README.md file

Each Github repo must have a README.md that summarises the project. This may include

- [ ] DESCRIPTION.en_us.html

Description paragraph in HTML to be used directly in font directories. 
This may be omitted by the designer, but if so requires Google to create one based on the contents of the README.md.

- [ ] BRIEF.md

A design brief that describes the intentions and goals of the project. 
Ideally this will be be added at the start of a project, defining the milestones that will be completed.
Typically it will be based on a proposal document made by the designer for financial support.

- [ ] Actual source files

A type project will include _actual_ source files, the ones that designers use ourselves when drawing the design. 
These are typically files with extensions like `.glyphs .ufo .vfb .sfd .sfdir`.
These are often quite 'messy'. 
Common indications of actual source files are:

- guidelines
- overlapping shapes
- multiple layers with alternative drawings
- unencoded glyphs with alternative drawings
- 'smart components'

- [ ] Build source files

Some type projects maintain a set of 'build sources', which are used as input to a build script. 
They are updated less frequently than the actual source files, and updated with care. 
These are typically UFO files, compiled with the [afdko](https://github.com/adobe-type-tools/afdko)
Common indications of build source files are:

- no or minimal guidelines
- no overlapping shapes (the result of a Remove Overlaps operation)
- a single layer per Master
- no unusual or additional unencoded glyphs with alternative drawings
- no 'smart components'

- [ ] Build process documentation
- [ ] Build process script

You may maintain a build script that runs the build steps, or you may make a tutorial for taking those steps manually (or a mix.)

- [ ] "Clean" repo

There should not be 'stray' files in the repo, such as `.empty` 

- [ ] Binary files
 
After the build process you will have OTF and TTF files, which must be included in the repo.

## Production

- [ ] The `fsType` embedding bits must be set to 0
- [ ] The Vertical Metrics must be set correctly
- [ ] The `FFTM` table should not be included
- [ ] The `DSIG` table should be included
- [ ] The `gasp` table should be included and set to 15
- [ ] Include ttfautohint command line options in build script
- [ ] Include ttfautohint controls file
- [ ] Name files according to the [DWFF Family Naming](http://designwithfontforge.com/en-US/Font_Info_&_Metadata.html) scheme ([spreadsheet](https://docs.google.com/spreadsheets/d/1ckHigO7kRxbm9ZGVQwJ6QJG_HjV_l_IRWJ_xeWnTSBg/edit#gid=0))
- [ ] Set vertical metrics to the _family's_ y-axis bbox values, with linegaps of 0. 
- [ ] Use a UPM of 1000 (even for TrueType fonts)
- [ ] Keep all points below `1056` and above `-270`, which is 132% of a 1000 UPM font; Android TextView widgets will clip fonts beyond that if there's no explicit padding (and designers tend to work just in Latin, so are unlikely to set it) says [Raph](https://groups.google.com/d/msg/googlefonts-discuss/qIPdk9Y7YUY/Eu21xtm0YrsJ)
- [ ] Production masters have PostScript manual hinting https://www.glyphsapp.com/tutorials/hinting-manual-postscript-hinting
- [ ] 

## Latin Design

- [ ] Support the 219 "base Latin" glyphs https://github.com/google/fonts/blob/master/tools/encodings/latin_unique-glyphs.nam
- [ ] Support all four figure sets https://www.glyphsapp.com/tutorials/figure-sets/
- [ ] Support mark based diacritics https://www.glyphsapp.com/tutorials/diacritics https://www.glyphsapp.com/tutorials/advanced-diacritics-narrow-marks
- [ ] Support the tallest glyph (perhaps Ǻ http://typedrawers.com/discussion/65/r-i-p) 
- [ ] Lining numerals with tabular spacing should be default; old style figures, and proportional variants, should be included with appropriate OpenType features. 
The general public calls old style the "jumping numbers" and like their tables to line up.
- [ ] Support Adobe Latin 3 http://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-3.html
- [ ] Support Adobe Latin 4 (mainly Vietnamese) http://adobe-type-tools.github.io/adobe-latin-charsets/adobe-latin-4.html https://www.glyphsapp.com/tutorials/advanced-diacritics-multiple-anchors
- [ ] `.notdef` glyph is a recommended design https://www.microsoft.com/typography/otspec/recom.htm
- [ ] Anchors for all letter and diacritics https://github.com/weiweihuanghuang/Work-Sans/pull/17#issuecomment-139910842
- [ ] Prime design distinct from apostrophe https://github.com/googlei18n/noto-fonts/issues/510#issue-105444463
- [ ] Support Catalan https://www.glyphsapp.com/tutorials/localize-your-font-catalan-punt-volat
- [ ] Support Dutch https://www.glyphsapp.com/tutorials/localize-your-font-accented-dutch-ij
- [ ] Support German https://www.glyphsapp.com/tutorials/localize-your-font-german-capital-sharp-s
- [ ] Support Polish https://www.glyphsapp.com/tutorials/localize-your-font-polish-kreska http://www.twardoch.com/download/polishhowto/ogonek.html 
- [ ] Support Romanian and Moldovian https://www.glyphsapp.com/tutorials/localize-your-font-romanian-and-moldovan
- [ ] Support Turkish https://www.glyphsapp.com/tutorials/localize-your-font-turkish
- [ ] Support Slashed Zero https://www.glyphsapp.com/tutorials/slashed-zero
- [ ] Support fractions, superscript and subscript numerals https://www.glyphsapp.com/tutorials/fractions https://www.glyphsapp.com/tutorials/superscript-and-subscript-figures 


## OpenType

- [ ] Support Turkish with OpenType http://typedrawers.com/discussion/1101/izmir-turkey
- [ ] Support tabular numbers with a consistent glyph width across the Regular, Italic, Bold and Bold Italic styles of a family http://typedrawers.com/discussion/1103/tabular-figures-width-consistency

## Test Documents

- [ ] http://understandingfonts.com/2011/fonttest
- [ ] http://impallari.com/testing
- [ ] http://testmyfont.com

### Tests

- [ ] Test for all letter/diacritic combinations https://github.com/weiweihuanghuang/Work-Sans/pull/17#issuecomment-139910842

# Further reading

### UFO

The UFO format is documented at http://unifiedfontobject.org and developed on Github (https://github.com/unified-font-object/ufo-spec) and the ufo-spec mailing list (https://groups.google.com/forum/#!forum/ufo-spec)
