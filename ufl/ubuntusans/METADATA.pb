name: "Ubuntu Sans"
designer: "Dalton Maag"
license: "UFL"
category: "SANS_SERIF"
date_added: "2024-03-22"
fonts {
  name: "Ubuntu Sans"
  style: "normal"
  weight: 400
  filename: "UbuntuSans[wdth,wght].ttf"
  post_script_name: "UbuntuSans-Regular"
  full_name: "Ubuntu Sans Regular"
  copyright: "Copyright 2011, 2022, 2023 Canonical Ltd. Licensed under the Ubuntu Font Licence 1.0"
}
fonts {
  name: "Ubuntu Sans"
  style: "italic"
  weight: 400
  filename: "UbuntuSans-Italic[wdth,wght].ttf"
  post_script_name: "UbuntuSans-Italic"
  full_name: "Ubuntu Sans Italic"
  copyright: "Copyright 2011, 2022, 2023 Canonical Ltd. Licensed under the Ubuntu Font Licence 1.0"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "greek-ext"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
axes {
  tag: "wdth"
  min_value: 75.0
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 800.0
}
source {
  repository_url: "https://github.com/canonical/Ubuntu-Sans-fonts"
  commit: "9554af00fb9d438a12c916df8451c10dcedc9b7e"
  files {
    source_file: "LICENCE.txt"
    dest_file: "LICENCE.txt"
  }
  files {
    source_file: "fonts/variable/UbuntuSans[wdth,wght].ttf"
    dest_file: "UbuntuSans[wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/UbuntuSans-Italic[wdth,wght].ttf"
    dest_file: "UbuntuSans-Italic[wdth,wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
