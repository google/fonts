name: "Honk"
designer: "Ek Type"
license: "OFL"
category: "DISPLAY"
date_added: "2023-11-15"
fonts {
  name: "Honk"
  style: "normal"
  weight: 400
  filename: "Honk[MORF,SHLN].ttf"
  post_script_name: "Honk-Regular"
  full_name: "Honk Regular"
  copyright: "Copyright 2023 The Honk Project Authors (https://github.com/EkType/Honk)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "math"
subsets: "menu"
subsets: "symbols"
subsets: "vietnamese"
axes {
  tag: "MORF"
  min_value: 0.0
  max_value: 45.0
}
axes {
  tag: "SHLN"
  min_value: 0.0
  max_value: 100.0
}
registry_default_overrides {
  key: "MORF"
  value: 15.0
}
source {
  repository_url: "https://github.com/EkType/Honk"
  commit: "964739fca4b7f5485b21525df1e803fffbe6da99"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Honk[MORF,SHLN].ttf"
    dest_file: "Honk[MORF,SHLN].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
