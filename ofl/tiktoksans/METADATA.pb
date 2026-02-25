name: "TikTok Sans"
designer: "Grilli Type, Contrast Foundry, Type Network"
license: "OFL"
category: "SANS_SERIF"
date_added: "2025-07-09"
fonts {
  name: "TikTok Sans"
  style: "normal"
  weight: 400
  filename: "TikTokSans[opsz,slnt,wdth,wght].ttf"
  post_script_name: "TikTokSans-Light"
  full_name: "TikTok Sans Light"
  copyright: "Copyright 2024 TikTok Inc. (https://github.com/tiktok/TikTokSans)"
}
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "greek"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "opsz"
  min_value: 12.0
  max_value: 36.0
}
axes {
  tag: "slnt"
  min_value: -6.0
  max_value: 0.0
}
axes {
  tag: "wdth"
  min_value: 75.0
  max_value: 150.0
}
axes {
  tag: "wght"
  min_value: 300.0
  max_value: 900.0
}

source {
  repository_url: "https://github.com/TikTok/TikTokSans"
  commit: "44862db3a4bf3a544b664a90245ca5daa5393571"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/TikTokSans[opsz,slnt,wdth,wght].ttf"
    dest_file: "TikTokSans[opsz,slnt,wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}

stroke: "SANS_SERIF"
minisite_url: "https://tiktok.com/font"
