name: "Overpass"
designer: "Delve Withrington, Dave Bailey, Thomas Jockin"
license: "OFL"
category: "SANS_SERIF"
date_added: "2016-12-02"
fonts {
  name: "Overpass"
  style: "normal"
  weight: 400
  filename: "Overpass[wght].ttf"
  post_script_name: "Overpass-Regular"
  full_name: "Overpass Regular"
  copyright: "Copyright 2021 The Overpass Project Authors (https://github.com/RedHatOfficial/Overpass)"
}
fonts {
  name: "Overpass"
  style: "italic"
  weight: 400
  filename: "Overpass-Italic[wght].ttf"
  post_script_name: "Overpass-Italic"
  full_name: "Overpass Italic"
  copyright: "Copyright 2021 The Overpass Project Authors (https://github.com/RedHatOfficial/Overpass)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
source {
  repository_url: "https://github.com/RedHatOfficial/Overpass"
  files {
    source_file: "fonts/variable/Overpass[wght].ttf"
    dest_file: "Overpass[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Overpass-Italic[wght].ttf"
    dest_file: "Overpass-Italic[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
minisite_url: "https://overpassfont.org/"
