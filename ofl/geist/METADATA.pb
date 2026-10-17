name: "Geist"
designer: "Andrés Briganti, Mateo Zaragoza, Guillermo Rauch, Evil Rabbit, José Rago, Facundo Santana"
license: "OFL"
category: "SANS_SERIF"
date_added: "2024-10-02"
fonts {
  name: "Geist"
  style: "normal"
  weight: 400
  filename: "Geist[wght].ttf"
  post_script_name: "Geist-Regular"
  full_name: "Geist Regular"
  copyright: "Copyright 2024 The Geist Project Authors (https://github.com/vercel/geist-font)"
}
fonts {
  name: "Geist"
  style: "italic"
  weight: 400
  filename: "Geist-Italic[wght].ttf"
  post_script_name: "Geist-Italic"
  full_name: "Geist Italic"
  copyright: "Copyright 2024 The Geist Project Authors (https://github.com/vercel/geist-font)"
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
  repository_url: "https://github.com/vercel/geist-font"
  commit: "a6d260e6cbc07eafdfad438f33601fe3c38b1e6f"
  files {
    source_file: "fonts/Geist/variable/Geist[wght].ttf"
    dest_file: "Geist[wght].ttf"
  }
  files {
    source_file: "fonts/Geist/variable/Geist-Italic[wght].ttf"
    dest_file: "Geist-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config-Geist.yaml"
}
minisite_url: "https://vercel.com/font"
primary_script: "Latn"
stroke: "SANS_SERIF"
