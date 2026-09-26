name: "IBM Plex Sans"
designer: "Mike Abbink, Bold Monday"
license: "OFL"
category: "SANS_SERIF"
date_added: "2018-03-12"
fonts {
  name: "IBM Plex Sans"
  style: "normal"
  weight: 400
  filename: "IBMPlexSans[wdth,wght].ttf"
  post_script_name: "IBMPlexSans-Regular"
  full_name: "IBM Plex Sans Regular"
  copyright: "Copyright 2019 IBM Corp. All rights reserved."
}
fonts {
  name: "IBM Plex Sans"
  style: "italic"
  weight: 400
  filename: "IBMPlexSans-Italic[wdth,wght].ttf"
  post_script_name: "IBMPlexSans-Italic"
  full_name: "IBM Plex Sans Italic"
  copyright: "Copyright 2019 IBM Corp. All rights reserved."
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "wdth"
  min_value: 75.0
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/googlefonts/plex"
  commit: "3e312890b3b9e47378b30dedfe4196a42151243c"
  files {
    source_file: "LICENSE.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Google-Fonts-Fixes/descriptions/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans/fonts/complete/ttf/IBMPlexSans[wdth,wght].ttf"
    dest_file: "IBMPlexSans[wdth,wght].ttf"
  }
  files {
    source_file: "Google-Fonts-Fixes/fonts/IBM-Plex-Sans/fonts/complete/ttf/IBMPlexSans-Italic[wdth,wght].ttf"
    dest_file: "IBMPlexSans-Italic[wdth,wght].ttf"
  }
  branch: "master"
}
