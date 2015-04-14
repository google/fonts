# `METADATA.json` File Specification

The `METADATA.json` file is a [JSON](http://en.wikipedia.org/wiki/JSON)-formatted metadata file that contains some information derived from the font files, and some information about the status of the fonts at Google Fonts. 
The file uses UTF-8 encoding, though it may also include backslashed Unicode characters in form of `\u00e1`. 
Below is an example `METADATA.json` file for [/ofl/abeezee](ofl/abeezee/METADATA.json): 

```
{
  "name": "ABeeZee",
  "designer": "Anja Meiners",
  "license": "OFL",
  "visibility": "Sandbox",
  "category": "Sans Serif",
  "size": 24918,
  "fonts": [
    {
      "name": "ABeeZee",
      "postScriptName": "ABeeZee-Italic",
      "fullName": "ABeeZee Italic",
      "style": "italic",
      "weight": 400,
      "filename": "ABeeZee-Italic.ttf",
      "copyright": "Copyright (c) 2011 by Anja Meiners (www.carrois.com post@carrois.com), with Reserved Font Name 'ABeeZee'"
    },
    {
      "name": "ABeeZee",
      "postScriptName": "ABeeZee-Regular",
      "fullName": "ABeeZee",
      "style": "normal",
      "weight": 400,
      "filename": "ABeeZee-Regular.ttf",
      "copyright": "Copyright (c) 2011 by Anja Meiners (www.carrois.com post@carrois.com), with Reserved Font Name 'ABeeZee'"
    }
  ],
  "subsets": [
    "latin",
    "menu"
  ],
  "dateAdded": "2012-09-30"
}
```

Below is a brief description of the most important top-level fields of `METADATA.json` (those which provide unique information which cannot otherwise be derived from the font files themselves). 
Each top-level field can only occur once in the file.

### `license`

The license field declares the license of the fonts in the family. 
Can contain one of 3 possible values:

* `"license": "Apache2"`
* `"license": "OFL"`
* `"license": "UFL"`

### `visibility`

The visibility field determines the current release status of the font on Google Fonts. 
One of 3 possible values:

* `"visibility": "External"` — font available on Google Fonts (both website and API)
* `"visibility": "Sandbox"` — font will be available shortly on Google Fonts (being tested)
* `"visibility": "Internal"` — the font will be served by the Google Fonts API but is not listed on the Google Fonts website

### `category`

Typographic category used on Google Fonts, one of 5 possible values:

* `"category": "Serif"`
* `"category": "Sans Serif"`
* `"category": "Display"`
* `"category": "Handwriting"`
* `"category": "Monospace"`

### `dateAdded`

Date when the font was first added to the Google Fonts collection, in `YYYY-MM-DD` format. 
Example:

* `"dateAdded": "2012-09-30"`

### `name`

The family name of the font as shown in the Google Fonts user interface. 
Example:

* `"name": "ABeeZee"`

### `designer`

The name of the type designer(s) who created the fonts. 
Example entries:

* `"designer": "Anja Meiners"`
* `"designer": "Multiple Designers"`
* `"designer": "TypeTogether"`
* `"designer": "TypeSETit"`
* `"designer": "Huerta Tipogr\u00e1fica"`
* `"designer": "Huerta Tipográfica"`

This info may differ from the designer info included inside the font files. 

### `fonts`

A list of entries which point to font files in each family, looking like this:

```
{
	"name": "ABeeZee",
	"postScriptName": "ABeeZee-Italic",
	"fullName": "ABeeZee Italic",
	"style": "italic",
	"weight": 400,
	"filename": "ABeeZee-Italic.ttf",
	"copyright": "Copyright (c) 2011 by Anja Meiners, with Reserved Font Name 'ABeeZee'"
},
```

The info in this section is derived from the information included inside the font files. 

### `subsets`

List of all character set subsets available in Google Fonts API for the given font family. 
Possible values (current as of 2015-04-14):

* `"latin"`
* `"latin-ext"`
* `"cyrillic"`
* `"cyrillic-ext"`
* `"greek"`
* `"greek-ext"`
* `"vietnamese"`
* `"arabic"`
* `"devanagari"`
* `"hebrew"`
* `"khmer"`
* `"telugu"`
