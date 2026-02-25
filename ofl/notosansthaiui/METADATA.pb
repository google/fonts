name: "Noto Sans Thai UI"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
source {
  repository_url: "https://github.com/notofonts/thai"
  commit: "fe7c82a2e55c38c5296d6415ba07015ef490970a"
  config_yaml: "sources/config.yaml"
}

fonts {
  name: "Noto Sans Thai UI"
  style: "normal"
  weight: 400
  filename: "NotoSansThaiUI[wdth,wght].ttf"
  post_script_name: "NotoSansThaiUI-Regular"
  full_name: "Noto Sans Thai UI Regular"
  copyright: "Copyright 2016 Google Inc. All Rights Reserved."
}
subsets: "menu"
subsets: "thai"
axes {
  tag: "wdth"
  min_value: 62.5
  max_value: 100.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 900.0
}
is_noto: true
languages: "kdt_Thai"  # Kuy
languages: "kxm_Thai"  # Northern Khmer
languages: "lcp_Thai"  # Western Lawa
languages: "lwl_Thai"  # Eastern Lawa
languages: "pi_Thai"  # Pali, Thai
languages: "sou_Thai"  # Southern Thai
languages: "th_Thai"  # Thai
languages: "tts_Thai"  # Northeastern Thai
primary_script: "Thai"
