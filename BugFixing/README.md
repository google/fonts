# Google Fonts bug fixing

A guide to fixing fonts stored in the [google/fonts](https://github.com/google/fonts) repository.

For adding new families see [ProjectChecklist.md](https://github.com/googlefonts/gf-docs/blob/master/ProjectChecklist.md).

## Rules

1. PR must contain only one family
2. Fix must be done at source
3. Post processing and hotfixes must be repeatable
4. PR title must mention family folder
5. PR message must mention which bug is fixed
6. METADATA.pb must be regenerated for each PR if a font has been modified
7. Version number must advance since previous release

## 1. PR must contain only one family

We want each commit to be as granular as possible. This makes it easier for us to rollback to previous commits if a problem occurs in just one family.

## 2. Fix must be done at source

Google/fonts holds font binaries, it does not contain any sources. 

Sources are usually other upstream git repositories which are hosted by their authors e.g [Montserrat](https://github.com/JulietaUla/Montserrat), [Amiri](https://github.com/alif-type/amiri), [Work Sans](https://github.com/weiweihuanghuang/Work-Sans).

The Github group [googlefonts](https://github.com/googlefonts) containts several families which are looked after by the Google Fonts team.
These families are looked after by us because the author may not be on Github or they stopped producing fonts.

Many older projects are not on Github yet. The [old Google Fonts repository](https://bitbucket.org/lassefister/old-googlefontdirectory) may contain sources for these missing families.
If this is the case, the person commiting the fix should create a new repo for the family in the [googlefonts](https://github.com/googlefonts) group.

If the family is not hosted on Github or in the old Google Fonts repository. It is advisable to contact the author to ask for sources. The last resort is to rebuild the sources from the binaries hosted on fonts.google.com. This has many risks and is not advisable.

## 3. Post processing and hotfixes must be repeatable

We can ignore this if we have made the fix to the source files. If the fix is a hot fix, the result must be repeatable. In order to acheive this, we must use tools which have a CLI;
this rules out VTT, VOLT, DTL OT Master. The hotfix should also have its own repo e.g [https://github.com/m4rc1e/archivo-hotfix](https://github.com/m4rc1e/archivo-hotfix). Hotfixes are not an ideal solution but may be needed in some circumstances.

## 4. PR title must mention family folder

The folder structure for [google/fonts](https://github.com/google/fonts) contains a directory for each font family.  The top level directories indicate the license of all files found within them.  Subdirectories are named according to the family name of the fonts within:

```
.
├── apache
│   ├── aclonica
│   ├── arimo
│   ├── ...
├── ofl
│   ├── abeezee
│   ├── abel
│   ├── ...
└── ufl
    ├── ubuntu
    ├── ubuntucondensed
    └── ...

```

By mentioning the family folder, repo contributors/viewers know which family has been modified by the pr.

## 5. PR message must mention which bug is fixed

Include a hyperlink to the issue in the pr message. This will alert individuals who are tracking the issue that a pr to solve it has been submitted. A good template for this rule and no 4 is:

```
<folder name>: <family version> added. Updated <mention fix solution>

<fix solution> has been updated which solves #<issue number>

Changes implemented in upstream <upstream repo url pr>
```

Eg,

```
mavenpro: v1.006 added. Updated Autohinting.

Autohinting has been redone using [ttf autohint v1.6](https://www.freetype.org/ttfautohint/#download) which solves #106

Changes implemented in upstream, 
```

## 6. METADATA.pb must be regenerated for each PR if a font has been modified

Each family folder contains a [METADATA.pb](https://github.com/google/fonts/blob/master/ofl/montserrat/METADATA.pb) file, which uses the [Protobuf format](https://developers.google.com/protocol-buffers/).
These metadata files are used for each family on [fonts.google.com](https://fonts.google.com). They contain information about which codepages the family supports, what category the family is, who the author is etc.

The script [./tools/add_font.py](https://github.com/google/fonts/blob/master/tools/add_font.py) will generate these files.
Once you've replaced the fonts in the family folder, execute the script:

    python add_font.py /path/to/familyfolder --update

Eg,

    python add_font.py ./ofl/mavenpro --update

If the codepages differ from the previous file, make sure the glyph counts are similiar to the current family hosted on [fonts.google.com](https://fonts.google.com). We can't release fonts where the codepages have regressed. This means we'll lose support for those languages and users will complain.

## 7. Version number must advance since previous release

Each new PR must increase the version number of a family. If we don't increase the version number, it is difficult to troubleshoot issues for users.

You can increase the version number when hotfixing by using [Font Bakery](https://github.com/googlefonts/fontbakery) with the following command:

    fontbakery update-version [fonts] <old number> <new number>

Eg

    fontbakery update-version ./MavenPro-Regular.ttf ./MavenPro-Bold.ttf 1.000 1.001;

## 8. Fonts must be run through [Font Bakery](https://github.com/googlefonts/fontbakery)

Before sending a PR, make sure the updated fonts are run through [Font Bakery](https://github.com/googlefonts/fontbakery). There should not be any regression errors, name errors, fsSelection, macStyle usWeightClass bit errors. If there are more than 10 errors, the font most likely contains serious issues.
