name: "Cossette Texte"
designer: "Cossette"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-07-29"
fonts {
  name: "Cossette Texte"
  style: "normal"
  weight: 400
  filename: "CossetteTexte-Regular.ttf"
  post_script_name: "CossetteTexte-Regular"
  full_name: "Cossette Texte Regular"
  copyright: "Copyright 2025 The Cossette Texte Project Authors (https://github.com/googlefonts/cossette-fonts)"
}
fonts {
  name: "Cossette Texte"
  style: "normal"
  weight: 700
  filename: "CossetteTexte-Bold.ttf"
  post_script_name: "CossetteTexte-Bold"
  full_name: "Cossette Texte Bold"
  copyright: "Copyright 2025 The Cossette Texte Project Authors (https://github.com/googlefonts/cossette-fonts)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/googlefonts/cossette-fonts"
  commit: "ee99cea3c23039e31865c3c37bd7d716278e546b"
  config_yaml: "sources/config-texte.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/CossetteTexte-Regular.ttf"
    dest_file: "CossetteTexte-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/CossetteTexte-Bold.ttf"
    dest_file: "CossetteTexte-Bold.ttf"
  }
  branch: "main"
}
