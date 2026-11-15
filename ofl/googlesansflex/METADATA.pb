name: "Google Sans Flex"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2024-11-21"
fonts {
  name: "Google Sans Flex"
  style: "normal"
  weight: 400
  filename: "GoogleSansFlex[ROND,opsz,slnt,wdth,wght].ttf"
  post_script_name: "GoogleSansFlex-Regular"
  full_name: "Google Sans Flex Regular"
  copyright: "Copyright 2025 The Google Sans Flex Project Authors (https://github.com/googlefonts/googlesans-flex)"
}
subsets: "canadian-aboriginal"
subsets: "cherokee"
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "nushu"
subsets: "symbols"
subsets: "syriac"
subsets: "tifinagh"
subsets: "vietnamese"
axes {
  tag: "ROND"
  min_value: 0.0
  max_value: 100.0
}
axes {
  tag: "opsz"
  min_value: 1.0
  max_value: 144.0
}
axes {
  tag: "slnt"
  min_value: -10.0
  max_value: 0.0
}
axes {
  tag: "wdth"
  min_value: 25.0
  max_value: 151.0
}
axes {
  tag: "wght"
  min_value: 1.0
  max_value: 1000.0
}
source {
  repository_url: "https://github.com/googlefonts/googlesans-flex"
  commit: "cedf1e9cef08ddf33d711dd259601ea3017b7cd4"
  archive_url: "https://github.com/googlefonts/googlesans-flex/releases/download/v5.000/GoogleSansFlex-v5.000.zip"
  files {
    source_file: "GoogleSansFlex[ROND,opsz,slnt,wdth,wght].ttf"
    dest_file: "GoogleSansFlex[ROND,opsz,slnt,wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
registry_default_overrides {
  key: "opsz"
  value: 18
}
