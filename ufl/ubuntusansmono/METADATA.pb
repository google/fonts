name: "Ubuntu Sans Mono"
designer: "Dalton Maag"
license: "UFL"
category: "MONOSPACE"
date_added: "2024-03-22"
fonts {
  name: "Ubuntu Sans Mono"
  style: "normal"
  weight: 400
  filename: "UbuntuSansMono[wght].ttf"
  post_script_name: "UbuntuSansMono-Regular"
  full_name: "Ubuntu Sans Mono Regular"
  copyright: "Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0"
}
fonts {
  name: "Ubuntu Sans Mono"
  style: "italic"
  weight: 400
  filename: "UbuntuSansMono-Italic[wght].ttf"
  post_script_name: "UbuntuSansMono-Italic"
  full_name: "Ubuntu Sans Mono Italic"
  copyright: "Copyright 2011, 2022, 2023 Canonical Ltd.  Licensed under the Ubuntu Font Licence 1.0"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "greek-ext"
subsets: "latin"
subsets: "latin-ext"
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/canonical/Ubuntu-Sans-Mono-fonts"
  commit: "5f47c8f963e2863468e49d2bb5bb6e6c4eb18ef7"
  files {
    source_file: "LICENCE.txt"
    dest_file: "LICENCE.txt"
  }
  files {
    source_file: "fonts/variable-subset/UbuntuSansMono[wght]-subset.ttf"
    dest_file: "UbuntuSansMono[wght].ttf"
  }
  files {
    source_file: "fonts/variable/UbuntuSansMono-Italic[wght].ttf"
    dest_file: "UbuntuSansMono-Italic[wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
