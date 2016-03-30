# Introduction

This page offers a checklist for running a libre font project. 

## Libre Fonts Culture

Since fonts are software, it is helpful for all type designers to understand typical ways of running software projects. 
For type designers involved in starting or participating in libre font projects, it is especially helpful to understand how libre software project operate.

The libre software culture has had an influence on restricted software development practices, and is a leading influence on type design today. 
David Lemon, the senior manager of the Adobe Type group, said at ATypI 2014 how the Adobe Type team has benefited from libre fonts culture, and that Git and Github was one of the most positive things ([reference](https://www.youtube.com/watch?v=DBz0rVUYNPA).)
Adobe have recently used the "publish early and often, gathering feedback" approach typical of libre project with the Vortice typeface project ([reference](http://blog.typekit.com/2015/03/04/introducing-vortice-and-the-adobe-type-concepts-program/).) 
A Thai type designer and web developer said this about his experience with Git:

> I used to hate Git because I don’t understand why I had to use it… until I started working with agile methods. Since then I keep using Git even on projects that I work on alone, because commit messages help me remember things I did and why I did them on each project.

Ideally all development of libre fonts is done publicly, from day one. 
This enables the public to see work in progress and point out issues during development instead of after the typical 1.0 release.

Github is a public project collaboration platform that is somewhat similar to Dropbox, but more fine-grained. 
It provides the best and most well-designed experience for public project development.

However, it is very project-centered. 

Please join the Fonts-Discuss Google Group, and when you have some work to show start a new thread and describe the work. You'll see a lot of other Israeli designers did the same, and the responses have been great.

If possible, add screenshots of your designs in your posts (and not just links to Github) - it makes the conversation on the Google Group much easier.

**Note:** The github messages are emailed to you and anyone who clicks 'watch' at the top of your project. 
You can reply via email to these messages and they will be posted publicly on the Github issue tracker (although attachments will be dropped.)
So its a good idea to set up an email filter to label github emails as such, to be sure you know when your reply will become public. 
 
* The [Producing Open Source Software](http://producingoss.com) book
* A list of [99 anti-patterns](http://opensoul.org/2015/07/22/99ways/)
* [The Free Font Movement](https://davelab6.github.io/matd-dissertation) MATD Dissertation

## Tools

Before you start your project, it is wise to set up all the tools that you will need in the course of development. 

### Mobile

Testing your type on mobile devices is essential, and even more important than testing on desktops.
You'll need both iOS and Android devices to do this testing.

* iPhone 4S+ with iOS 8+ ([reference](https://david-smith.org/iosversionstats/)) Safari
* Android 4.x or higher (ideally latest) with a "normal" size screen ([reference](https://developer.android.com/about/dashboards/index.html)) Chrome

Safari may have issues with OpenType feature processing, especially for complex scripts.

### Windows

No Windows-only tools are required for libre font development today.
But you will need a Windows 7 computer for testing your fonts as web fonts, especially the hinting rendering.
You can use either a physical computer, like a cheap laptop from craigslist or similar, or a virtual machine for this.

Windows 7 is the most commonly used desktop operating system ([reference](https://en.wikipedia.org/wiki/Usage_share_of_operating_systems)). 
It can also be the most challenging font rendering system compared to all other alternatives in common mass use today.

Microsoft offers zero-price virtual machine images at [modern.ie](https://dev.modern.ie/tools/vms/mac/) that can be run with [Virtual Box](https://www.virtualbox.org).

#### Web Browsers

* [Chrome 48](http://www.google.com/chrome)
* [Firefox 44](https://www.getfirefox.com)
* Microsoft Edge
* Microsoft Internet Explorer 10 (from [modern.ie](https://dev.modern.ie/tools/vms/mac/))
* [Opera 31](https://www.opera.com)
* ~~Safari~~ (No longer supported by Apple)

#### Office Applications

Many Windows users install fonts to use them in Microsoft Word or LibreOffice, so check that your fonts can be installed and set paragraphs normally in 

* Windows installation
* Microsoft Word
* Libre Office 5.1

### GNU+Linux

The [Ubuntu](https://www.ubuntu,com) distribution of GNU+Linux is the most popular, and it is important that your web fonts work with it. 
Like Windows, if your main working environment is Mac OS X, it can be run as virtual machine.

#### Web Browsers

* [Chrome 48](http://www.google.com/chrome)
* [Firefox 44](https://www.getfirefox.com)
* [Opera 31](https://www.opera.com)

#### FontForge PPA

A FontForge PPA is available. 
TODO include details

Install the python module with

    apt-get install python-fontforge;

### Mac

#### Web Browsers

* [Chrome 48](http://www.google.com/chrome)
* [Firefox 44](https://www.getfirefox.com)
* Safari 9
* [Opera 31](https://www.opera.com)

Safari may have issues with OpenType feature processing, especially for complex scripts.

#### Office Applications

* Microsoft Word 
* LibreOffice 5.1

#### Adobe Creative Suite

Since Google Fonts are primarily for use on the web, how web browsers render the font is primarily important. 
Today web browser applications tend to have the best and most up-to-date OpenType support anywhere, thanks to the Windows operating system and harfbuzz library efforts to be best-in-class. 
However, other applications that rely on their own OpenType processing may often exhibit font bugs that are not the fault of the font, but of the application. 
Most designers use Photoshop, Illustrator, and InDesign, so ideally your fonts will work well with these applications, but these are part of the set that do not use standard operating system OpenType processing. 

If your font works on Windows Firefox and Android Chrome, but not in Adobe applications, then it may be due to an Adobe bug. 
Be sure to check that you are using the "World Ready Composer" option which is required for many scripts to work correctly, and that your text language has been set correctly. 
If these things are confirmed, please report the issue to Adobe.

#### Libre Graphics Suite

Most designers using libre software use GIMP, Inkscape, Scribus, but currently these applications do not support OpenType.

#### Font Editors

Some useful font editor GUI applications:

* FontForge [fontforge.github.io](http://fontforge.github.io)
* Glyphs [glyphsapp.com](https://glyphsapp.com)
* FontLab [fontlab.com](https://fontlab.com)
* OTMaster [dtl.nl](http://dtl.nl)

#### Terminal Tools

Some useful font tools used in Terminal. 
When you need to type a filename for a command, you can drag and drop files from finder into Terminal and their full path will be added.

##### pip

Package manager for installing python tools. 
[pip.pypa.io](https://pip.pypa.io)

    sudo easy_install pip;

##### iPython 

Interactive python that makes writing python scripts interactive. 
Jupyter Notebook is a web UI that makes iPython even easier to use.

    sudo pip install ipython jupyter;
    jupyter notebook;

##### fonttools 

Python package for operating on binary font files. 
Install the very latest version from git master:

    sudo pip install git+git://github.com/behdad/fonttools.git;

##### pyfontaine 

Python package for analysing binary font files for script and language support. 
Install the very latest version from git master:

    sudo CFLAGS=-I/usr/local/opt/icu4c/include LDFLAGS=-L/usr/local/opt/icu4c/lib pip install pyicu;
    sudo pip install git+git://github.com/davelab6/pyfontaine.git;

##### Homebrew

Package manager for installing unix tools, such as FontForge. 
[brew.sh](http://brew.sh)

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)";
    sudo xcodebuild -license;

#### FontForge

FontForge offers a python module that can be useful.
[fontforge.org](https://fontforge.org)

    brew install python; 
    brew install fontforge --HEAD;

##### ttfautohint

Autohinter for TTF files.
[freetype.org/ttfautohint](http://freetype.org/ttfautohint/) and [manual](http://freetype.org/ttfautohint/doc/)

Install the latest version of ttfautohint from git master:

    brew install --HEAD ttfautohint --with-qt;

##### Web Font Tools

Some command line web font tools can be useful for converting to and from various web font formats.

    brew tap bramstein/webfonttools; 
    brew update; 
    brew install sfnt2woff sfnt2woff-zopfli woff2 ttf2eot sfntly;

##### OTS 

Web font sanitiser, used by Firefox and Chromium to reject buggy binary font files. 
**Your OTF and TTF files must pass its checks.**

Install [homebrew](#homebrew) (as above) then:

    brew tap bramstein/webfonttools; 
    brew update; 
    brew install ots --HEAD; # install

Use it like this:

    ot-sanitiser font.ttf;

When run and no output appears, it means the file is good.

##### fontbakery 

Font checking and fixing tools. 
Install the very latest version from git master:

    mkdir -p ~/src/github.com/googlefonts;
    cd ~/src/github.com/googlefonts;
    git clone git@github.com:googlefonts/fontbakery.git;
    cd fontbakery;
    sudo pip install git+git://github.com/googlefonts/fontbakery.git;

##### fontmake

New UFO and Glyphs compiler (which is still experimental, but the libre font movement is adopting so please do use and test.)
Install the very latest version from git master:

    mkdir -p ~/src/github.com/googlei18n;
    cd ~/src/github.com/googlei18n;
    git clone git@github.com:googlei18n/fontmake;
    cd fontmake;
    sudo python -m pip install -r requirements.txt;
    sudo python setup.py develop;

##### Apple OS X Font Tools

Apple provides various font utilities, and `ftxvalidator` is especially useful as it runs the same checks that are run for users when they install a font using Font Book.
You must use your Apple ID to sign in to http://developer.apple.com and download `osxfonttools.dmg` and then:

    cd ~/Downloads/ ;
    hdiutil attach osxfonttools.dmg ;
    mkdir -p /tmp/ftx ;
    cd /tmp/ftx ;
    cp "/Volumes/OS X Font Tools/OS X Font Tools.pkg" . ;
    xar -xf "OS X Font Tools.pkg" ;
    cd fontTools.pkg/ ;
    cat Payload | gunzip -dc | cpio -i ;
    sudo mv ftx* /usr/local/bin/

##### meld, icdiff

File/folder comparison application and tool, that shows two files or directories side by side, with helpful graphics to show how the files are different.

    brew install meld icdiff;

To compare two fonts using fonttools `ttx` and `meld`:

    mkdir OLD;
    mkdir NEW;
    mv Acme*.ttf OLD/;
    mv ~/Desktop/Acme*.ttf NEW/;
    ttx -s */*ttf;
    meld OLD NEW;

To use icdiff with the `git` command:

    # FIXME TODO

## Project Repository

### Github

There are many good guides for learning how to use Github around the web, including:

* <https://github.com/davelab6/git-for-type-designers>
* <https://try.github.io>, a 15 minute interactive game
* <http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1>, an introduction article
* <https://guides.github.com>, well written and illustrated guides
* <http://nvie.com/posts/a-successful-git-branching-model>, an essay about using Git for ongoing project management.
* [Articles about Github in Wired.com](https://www.google.com/search?q=github+everything+site:wired.com)

Tip: When working with font projects on Github, it is typical to work with several "forks" of the same project, each driven by different people or organizations.
To keep things simple you should repeat the github.com site structure on your harddisk:
Create a folder in your projects directory called `github.com`, inside that make a directory for each username/organization you work with, and clone each repo inside its correpsonding folder. 

If you use Glyphs, use this plugin that makes working with Git just like saving: [github.com/simoncozens/GlyphsGit](https://github.com/simoncozens/GlyphsGit)

### Your Repository

#### Name Your Project

Aim for short, snappy, memorable name that is easy to pronounce in English. Long names can be harder for people to remember and type correctly, and problematic for software with name length limitations.

You may include stylistic or genre names in the family name. 
There are already families such as "Family Cursive" or "Family Sans" or "Family Mono," and other scripts also have visual genre names that do not refer to a particular language or set of unicode characters, like "Family Nastaliq" or "Family Kufi" or "Family Naskh" for Arabic genres.

Do not use a name already used by another published font project. [namecheck.fontdata.com](http://namecheck.fontdata.com) is a handy tool to assist such checks, along with a general web search for `name + font`

Do not include any script or language names. Eg, `Acme Arabic` or `Acme Persian`. 
(The Google Fonts API will by default serve only Basic Latin fonts; users must specify additoinal scripts. 
This means a family named with a language or script in the name will confuse users, because the font will often be served without any support for that language or script. 
More details in this [discussion](https://github.com/vaishnavimurthy/Akaya-Kannada/issues/1).)

Do not use non-ASCII alphabet characters in the family name: 
No dashes, numbers, or diacritics.

Do not use any company names, including your own. 
Large distributors (such as Google) can not redistribute the fonts without neccessarily endorsing the named company, and companies with policies against endorsement will therefore need to rename the fonts, which is not ideal.  

Do not use any trademark names. 
Google and other redistributors may not be able to get permission to use the trademark, even if you can.

If you are making a libre version of your prior proprietary font, or designing something in an established genre, add "Libre" or a local equivalent to that well-known name Eg, `Vesper Libre` or `Libre Baskerville` or `David Hofshi` (Hebrew) or `Something Mukta` (Hindi)

#### Trademarks 

Typically libre fonts are not subject to any trademarks.

If you do not trademark your project name:

* Do not declare trademarks in font metadata

If you do trademark your project name:

* Declare trademarks in font metadata
* License your trademarks for redistribution in a TRADEMARKS.md file ([example](https://github.com/mooniak/ayanna-font/blob/master/TRADEMARKS.md))
* Explicitly permit Google to use the trademarks. Contact Dave Crossland via email to learn how

#### Create and name your repository

Each repository should be all lowercase, with no spaces or dashes `-` for spaces.

* [Github Blog: Introducing Organizations](https://github.com/blog/674-introducing-organizations)
* [Github Help: Setting up and managing organizations and teams](https://help.github.com/categories/setting-up-and-managing-organizations-and-teams/)
* [Github Help: What's the difference between user and organization accounts?](https://help.github.com/articles/what-s-the-difference-between-user-and-organization-accounts/)
* Github Organization examples: [github.com/rosettatype](https://github.com/rosettatype) [github.com/cadsondemak](https://github.com/cadsondemak) [github.com/cyrealtype](https://github.com/cyrealtype) 

If you are a foundry or collaborative project:

* set up a [Github organization](https://help.github.com/articles/creating-a-new-organization-account/)
* create usernames for each person involved in the project, and 
* create each repo inside that organization

#### Short summary and website

At the top of the repo page is a summary input, that can be set to a short (10 words or less) description of the project. 

If the project has a gh-pages branch (see below) then use that URL, typically `https://username.github.io/project`. If you maintain a project homepage elsewhere, use that URL.

### Repository Files

#### Keep a clean repo, with `.gitignore`

There should not be 'stray' files in the repo. 

The `.gitignore` file can prevent such files being casually commited to the repo.

Each Github repo must have a `.gitignore` file with at least the following contents

    # file manager empty files
    .DS_Store
    .empty
    .sparkleshare
    # font editor temporary files
    *(Autosaved).glyphs
    *.vfbak

#### README.md

Each Github repo **MUST** have a README.md that includes at the top a descriptive summary of the design and project.

* FIXME TODO Add examples of great ones

Ideally, include an inline image near the top (see below)

#### OFL.txt

Each Github repo **MUST** have an OFL.txt containing the full text of the SIL Open Font License, and a copyright notice on the first line. 

The copyright notice on line 1 of the OFL.txt **MUST** match the copyright notice inside each font file.

Typically this notice does **not** have a Reserved Font Name at the end, or if it does, the name declared is not used anywhere else in the project. 

Since the copyright authors can change over time, such as when another author contributes to the project, write the notice for the "Acme" family as 

    Copyright 2016 The Acme Project Authors (info@foundry.com)

This necessarily means the list the authors must be maintained somewhere, so really 3 files are required:

* `OFL.txt` with the license text ([example](https://github.com/NDISCOVER/Arima-Font/blob/master/OFL.txt))
* `AUTHOR.txt` listing copyright holders ([example](https://github.com/NDISCOVER/Arima-Font/blob/master/AUTHORS.txt))
* `CONTRIBUTORS.txt` listing people who contribute but who are not actually copyright holders, eg people who work for a company that holds their copyrights as part of their employment contract ([example](https://github.com/NDISCOVER/Arima-Font/blob/master/CONTRIBUTORS.txt))

#### TRADEMARKS.md

If you do trademark your project name, license your trademarks for redistribution in a TRADEMARKS.md file ([example](https://github.com/mooniak/ayanna-font/blob/master/TRADEMARKS.md))

#### `documentation/`

During the course of a project many documents may be written that can be useful to store for archival purposes, such as email reviews and so on.

If you wish to include dated versions of files inside the version control system repository, the filenames should start with YYYY-MM-DD so that when the directory is listed alphabetically, the contents are sorted by date order.

Convert any offline rich document formats (DOC, RTF, etc) to MarkDown.
Some handy MarkDown editors are:

* http://macdown.uranusjr.com
* https://cloose.github.io/CuteMarkEd

#### `documentation/sample.png`

A sample.png banner image showing the project, so people get an instant and visual overview. 

Create a `documentation` subdirectory for keeping this and other such files.

#### `documentation/DESCRIPTION.en_us.html`

Description paragraphs in HTML to be used directly in the Google Fonts directory and elsewhere.

If you omit this, Google Fonts will create one based on the contents of the `README.md`

#### `documentation/BRIEF.md`

A design brief that describes the intentions and goals of the project. 
Ideally this will be be added at the start of a project, defining the milestones that will be completed.
Typically it will be based on a proposal document made by the designers for financial support to enable their project.

#### `sources/`

Project must include **actual** source files - all the files that you use yourself when developing the project, in your preferred form of modification.
These are typically files with font editor extensions (`.glyphs .ufo .vfb .sfd .sfdir`) and are often quite _messy._

Common indications of actual source files in glyph drawings are:

* guidelines
* overlapping shapes
* multiple layers with alternative drawings
* unencoded glyphs with alternative drawings
* 'smart components'

For feature files:

* descriptive comments
* commented out blocks

If your preferred form of modification us UFO, integrate [ufoNormalizer](https://github.com/unified-font-object/ufoNormalizer) into your workflow so that the UFOs saved are always in the same order and disk layout.

(If you are unfamiliar with UFO, you can learn more at [unifiedfontobject.org](http://unifiedfontobject.org). 
The UFO format is itself developed on Github at [github.com/unified-font-object](https://github.com/unified-font-object/ufo-spec) and the [ufo-spec mailing list](https://groups.google.com/forum/#!forum/ufo-spec).)

#### `sources/builds/` (optional)

Some type projects maintain a set of 'build sources', which are used as input to a build script. 
They are updated less frequently than the actual source files, and updated from those with care from time to time.
These are typically a set of UFOs and FDK files that are compiled with the [afdko](https://github.com/adobe-type-tools/afdko).

Common indications of build source files are:

* no or minimal guidelines
* no overlapping shapes (the result of a Remove Overlaps operation)
* a single layer per Master
* no unusual or additional unencoded glyphs with alternative drawings
* no 'smart components'

#### `sources/README.md`

Build process documentation, that explains the steps you take to build your sources into binary files.
This might also be named `BUILD-HOWTO.md` or `BUILD-INSTRUCTIONS.md`, but if it is named README.md then when you browse the `sources/` directory on Github it will be shown inline at the bottom of the page.

#### `tools/build.py` 

You may maintain a build script that runs the build steps. 

This typically accompanies the documentation above for taking those steps manually (or a mix.)

#### `fonts/otf/` and `fonts/ttf/` 

It is common to keep development versions of your fonts in the Github repo. 
However, it is hard to see the differences in binaries as they change, and makes it easy for development binaries to spread into wider use when they may not have been through the typical full testing processes used before a release.
So:

**Include font binaries only in the TTX XML format**

This is also helpful from version to version, because you can see what changed using diff tools (discussed above regarding `meld`.)

Actual OTF and TTF files should be included in a ZIP and attached to a Github Release (see below regarding Releases.)

## Pre-Production

Here are production steps you can take at the start of a project when setting up your font source files.

#### Instance and File Naming

Set up all your masters and instances at the start of the project to keep the project process iterative. 

You should plan and develop the weights of each instance early in the process.
The Impallari Type Family Steps page helps to plan the weight progression on a curve, so that the weight of middle instances are suitably light.
The master and instance interpolation values should be representative of stem weights. 
This makes it easier for people who want generate their own fonts in the future to do so. 

* http://www.impallari.com/familysteps

Name files and naming-metadata canonically, so that your OTF and TTF files follow this ([family naming scheme spreadsheet](https://docs.google.com/spreadsheets/d/1ckHigO7kRxbm9ZGVQwJ6QJG_HjV_l_IRWJ_xeWnTSBg/edit#gid=0))

Here is the default value in FontLab 5:

![Regular PSName Setting in FontLab - default](ProjectChecklist-FL-regular-default.png)

Here is the corrected value:

![Regular PSName Setting in FontLab - fixed](ProjectChecklist-FL-regular-fixed.png)

#### fsType

The `fsType` embedding bits must be set to 0.

![Set fsType to 0 in Glyphs](ProjectChecklist-G-fstype.png)

![Set fsType to 0 in FontLab 5](ProjectChecklist-FL-fstype.png)

#### VendorID

You should set your own unique VendorID and register it with Microsoft.

* https://www.microsoft.com/typography/otspec/os2.htm#vendid

#### FFTM

If you are using FontForge, do not include the `FFTM` table.
You can do this by passing an argument to the fontforge python `font.generate()` argument.

#### DSIG table

The `DSIG` table should be included.

There is a fontbakery tool to add one, that uses fonttools:

    fontbakery-fix-dsig.py Family-Style.ttf --autofix;
    mv Family-Style.ttf.fix Family-Style.ttf;

#### gasp table 

The `gasp` should be set to 15

#### License

The license metadata should be set to the long line (which is cut off on Github, but if you triple click to select the whole line, you'll get it all - and watch out for your editor adding an unneccessary line break after the line when you paste it:

    This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL

#### License URL 

The license URL metadata should be set to

    http://scripts.sil.org/OFL

#### Copyright Notice

Must match line 1 of OFL.txt

#### Trademark 

Only if required, trademark metadata should be filled in ([example](https://github.com/mooniak/ayanna-font/blob/master/TRADEMARKS.md))

#### TTFAutohint Settings and Controls File

Early on in your development process, add ttf output and ttfautohint to your build process or script, and test the output on various Windows browsers. 
Be sure to use all relevant and specific command line options, which you can learn about in the ttfautohint manual.

You can improve the results of ttfautohint using a 'controls' file.
Early on in your development process, add a 'stub' controls file and improve it as the design progresses. 
There is often a sweet spot that you can reach early in the design process by scaling your design to improve the base ttfautohint results, reducing the need for controls file adjustments.

ttfautohint info should include version and parameters, by passing the `-I` option.

TTFA Info Table should not be included.

* TTFAutohint manual is at http://freetype.org/ttfautohint/doc/ttfautohint.html

#### UPM

Use a UPM of 1000 (even for TrueType fonts)

#### Vertical Metrics

Throughout development the 3 sets of vertical metrics should be set to the y bounding box **of the family,** and both linegaps should be set to zero.
The `fontbakery-fix-vertical-metrics.py` script can help with this. 
It is wise to determine the tallest and deepest glyphs possible in the design early in your process; these may be outside the glyph set you are intending to cover during this round of development, but should be set to allow for future development without changing the vertical metrics.

Ideally, keep all points below `1056` and above `-270`, which is 132% of a 1000 UPM font.
At the time of writing (late 2015) Android TextView widgets will clip fonts beyond that if there's no explicit padding, and app designers tend to work just in Latin, so are unlikely to set it ([discussion](https://groups.google.com/d/msg/googlefonts-discuss/qIPdk9Y7YUY/Eu21xtm0YrsJ).
However, this may mean that your design would be scaled small on the body, so you can go outside this range if you need to. 

#### Codepages

The codepages set will determine how the font family is ordered in some software's font family lists ([discussion](https://github.com/Tarobish/Jomhuria/issues/40).)

In fonttools, Arabic fonts codepages can be set like this:

    >>> font['OS/2'].ulCodePageRange1 = 64
    >>> font['OS/2'].ulCodePageRange2 = 0

Then the family will be included with the Arabic fonts, like this:

![Katibeh in Adobe](https://cloud.githubusercontent.com/assets/8403973/13370134/8f5f3bd0-dcb4-11e5-8336-7b608ebe483e.png)

#### Vendor ID

You may wish to set the OS/2 Vendor ID to your own 4 ASCII character value. 
Your value should be registered with Microsoft. 
If you do not yet have a value, review the Microsoft list to ensure your value is unique.

* https://www.microsoft.com/typography/links/vendorlist.aspx

#### Glyphs Specific Steps

If you are using the Glyphs editor, there are some specific steps you should take. 

Font Info, Font, Compact File Storage enabled.

### Project Website

[pages.github.com](https://pages.github.com) offers a convenient way to create a blog for the project, and host live testing pages.
Some relevant links and examples:

* https://github.com/barryclark/jekyll-now is a helpful demo site
* http://tarobish.github.io/Mirza/ and http://tarobish.github.io/Katibeh/ are advanced font testing pages
* https://rosettatype.github.io and https://cadsondemak.github.io are a great examples of how to set up a Github Organization if you are practising as a foundry

## Post-Production

Here are production steps you can take during or near the end of a period of development.

#### File Names

File and naming metadata follows this ([family naming scheme spreadsheet](https://docs.google.com/spreadsheets/d/1ckHigO7kRxbm9ZGVQwJ6QJG_HjV_l_IRWJ_xeWnTSBg/edit#gid=0))

#### Vertical Metrics 

Must be set to the __family's__ y-axis bbox values, with linegaps of 0. 

This is where to find these values for each font in FontLab 5:

![BBox values in FontLab 5](ProjectChecklist-FL-vertical-metrics-id.png)

This is where to set the vertical metrics in FontLab 5:

![Vertical Metrics set correctly in FontLab 5](ProjectChecklist-FL-vertical-metrics-set.png)

#### PostScript Hinting

Production masters have PostScript manual hinting https://www.glyphsapp.com/tutorials/hinting-manual-postscript-hinting

#### TTFAutohint

Develop a ttfautohint controls file to correct any problems in hinting. 

#### Kerning

Must be included in both `GPOS` and `kern` table formats, since older versions of MS Office only use the 'kern' feature (and drop it if extension-type lookups are used.) 

FIXME TODO research this topic more to find out what essential kerning should be.

## Latin Design

#### Latin Glyph Set

There are currently 3 milestones for Latin glyphs:

* Support the 219 "base Latin" glyphs ([latin_unique-glyphs.nam](https://github.com/google/fonts/blob/master/tools/encodings/latin_unique-glyphs.nam))
* Support Abode Latin 3 (http://davelab6.github.io/abode-latin-charsets)
* Support Abode Latin 4 (mainly Vietnamese) 

FIXME TODO Come up with a definitive `latin-ext` glyph set

#### Figure Sets

Support all four figure sets. 

The general public calls old style the "jumping numbers" and like their tables to line up, so lining numerals with tabular spacing must be default.

Old style figures, and proportional variants, should be included with appropriate OpenType features. 

Tabular numbers must have a consistent glyph width across the Regular, Italic, Bold and Bold Italic styles of a family, but in other styles can be only consistent with other glyphs in the same style. 

* http://typedrawers.com/discussion/1103/tabular-figures-width-consistency 
* https://www.glyphsapp.com/tutorials/figure-sets/

#### Diacritics

Support mark based diacritics 

* https://www.glyphsapp.com/tutorials/diacritics 
* https://www.glyphsapp.com/tutorials/advanced-diacritics-multiple-anchors
* https://www.glyphsapp.com/tutorials/advanced-diacritics-narrow-marks
* http://www.urtd.net/x/cod (+ introduction at http://www.urtd.net/blog/cod)

#### Future Proof Tallest + Deepest Glyphs

Even if your planned glyph set does not include them, to future proof your design you should support from [Abode Latin 5](http://davelab6.github.io/abode-latin-charsets)

* the tallest glyph (perhaps Ǻ, per http://typedrawers.com/discussion/65/r-i-p) 
* the deepest glyph (perhaps FIXME TODO)

#### notdef

The `.notdef` glyph should be the recommended design 

* https://www.microsoft.com/typography/otspec/recom.htm

#### Anchors

Anchors for all letter and diacritics 

* https://github.com/weiweihuanghuang/Work-Sans/pull/17#issuecomment-139910842

#### Prime 

The prime designs must be distinct from apostrophe 

* https://github.com/googlei18n/noto-fonts/issues/510#issue-105444463

## Kerning

All kerning and GPOS in the font is checked for mistakes

* [Mark Foley's GlyphsApp script](https://github.com/m4rc1e/mf-glyphs-scripts)) 

FIXME TODO which one exactly, and how to use it

## OpenType

You must comment all feature code that is not automatically generated.
It’s not always obvious what OpenType code in a font does, particularly with non-Latin scripts where the features that are specific to a font can be entangled with features that are required for language support. 

#### fractions, superscript and subscript numerals 

* https://www.glyphsapp.com/tutorials/fractions 
* https://www.glyphsapp.com/tutorials/superscript-and-subscript-figures 

#### Slashed Zero 

* https://www.glyphsapp.com/tutorials/slashed-zero
* https://forum.glyphsapp.com/t/tabular-slashed-zero/3987

#### Catalan 

* https://www.glyphsapp.com/tutorials/localize-your-font-catalan-punt-volat

#### Dutch 

* https://www.glyphsapp.com/tutorials/localize-your-font-accented-dutch-ij

TODO As of March 2016 this Glyphs tutorial is incomplete, we should find how what is needed to make it complete.

#### German 

* https://www.glyphsapp.com/tutorials/localize-your-font-german-capital-sharp-s

#### Polish 

* https://www.glyphsapp.com/tutorials/localize-your-font-polish-kreska 
* http://www.twardoch.com/download/polishhowto/ogonek.html 

TODO The Polish kreska is not always needed, we should find out when it is and is not needed. 

#### Romanian and Moldovian 

* https://www.glyphsapp.com/tutorials/localize-your-font-romanian-and-moldovan

#### Turkish 

* https://www.glyphsapp.com/tutorials/localize-your-font-turkish http://typedrawers.com/discussion/1101/izmir-turkey

#### Lowercase octothorpe (optional)

* ([discussion](http://typedrawers.com/discussion/1377/lowercase-hashtag#latest))

## Test Documents

Your project should include comprehensive testing documents, both for yourself to confirm your design works well, and so that others can evaluate their modifications.

These testing document projects may also be helpful:

* http://understandingfonts.com/2011/fonttest
* http://impallari.com/testing
* http://testmyfont.com

Test for all letter/diacritic combinations and complex script conjuncts.

* https://github.com/weiweihuanghuang/Work-Sans/pull/17#issuecomment-139910842

## Release

Abstractly, we can distinguish between work that is public and publicised. 
Proprietary software/fonts are developed privately, and then tightly couple their releases' publication and publicity, marking clear versions in each release. 

Publicly developed libre software/fonts necessarily make more of a difference between the two concepts, since publication is a constant factor.

#### Versioning

Practically speaking, the availability of fonts in the Google Fonts API is the primary point of publicity. 
A secondary point is the Github releases system, which is the best way of marking new versions available for Google Fonts to queue up to follow.

Its important that the version fields inside the source and binary font files in a release (eg in the NAME table, or Font Info inputs) match the version labelled on the release. 

[semver.org](http://semver.org) is growing in popularity as a deeply considered way of versioning software that uses 3 version numbers, `MAJOR.MINOR.PATCH`, but it does not work well for fonts because the OpenType standard only allows binary font metadata to have one period separator. 

So a `MAJOR.MINOR-or-PATCH` scheme is better for fonts, starting with `1.000` and incrementing from there (`1.001`, `1.002`, etc.) 

A MAJOR number of 0 will cause problems for some software, so `0.1` is not allowed.

It would be good to have some note in the version string where possible like 'development version' that is removed when making a release build. 
Some systems will not accept fonts with a version number of `0.something` so that can be good to use in development sources.

#### `FONTLOG.txt`
 
Create or update the FONTLOG.txt file to detail each release of the project and what changed. 

* https://github.com/fonts/skeleton/blob/skeleton/tools/FONTLOG.py can generate one.

#### `project.zip`

Use the Github Releases system to tag a release of your git repository.

* https://help.github.com/articles/about-releases/
* https://github.com/blog/1547-release-your-software
* https://help.github.com/articles/creating-releases/

and then upload a ZIP with only the actual release:

* TTF files
* OTF files
* OFL.txt
* FONTLOG.txt
* README.md

#### Release Branch

You may wish to maintain `dist` or `release` branches similar to [Git Flow]() FIXME TODO ([discussion](https://github.com/khaledhosny/libertinus/issues/13#issuecomment-176641248))

## Post Release

#### Social Media

Promote your project on social media

#### Awards

Submit your project to the many internaional type awards competitions

* TDC
* TDC2
* Granshan
* Morisawa

TODO FIXME Add more competitions

#### Fund The Next Round

As your font grows a loyal following of users, reach out to them and find out how the font can be improved, and ask them to co-pay for improvements. 

* Patreon
* Kickstarter
* SnowDrift
* Fund-IO

FIXME TODO Write more about how to do this
