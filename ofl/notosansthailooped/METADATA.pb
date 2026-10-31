name: "Noto Sans Thai Looped"
designer: "Google"
license: "OFL"
category: "SANS_SERIF"
date_added: "2020-11-19"
fonts {
  name: "Noto Sans Thai Looped"
  style: "normal"
  weight: 400
  filename: "NotoSansThaiLooped[wdth,wght].ttf"
  post_script_name: "NotoSansThaiLooped-Regular"
  full_name: "Noto Sans Thai Looped Regular"
  copyright: "Copyright 2022 The Noto Project Authors (https://github.com/notofonts/thai)"
}
subsets: "latin"
subsets: "latin-ext"
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
source {
  repository_url: "https://github.com/notofonts/thai"
  commit: "c62000b1b2328aa5e08470c1924ac9987fdb83b9"
  config_yaml: "sources/config-sans-thai-looped.yaml"
  archive_url: "https://github.com/notofonts/thai/releases/download/NotoSansThaiLooped-v2.000/NotoSansThaiLooped-v2.000.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "NotoSansThaiLooped/googlefonts/variable-ttf/NotoSansThaiLooped[wdth,wght].ttf"
    dest_file: "NotoSansThaiLooped[wdth,wght].ttf"
  }
  branch: "main"
}
is_noto: true
languages: "kdt_Thai"  # Kuy
languages: "kxm_Thai"  # Northern Khmer
languages: "lcp_Thai"  # Western Lawa
languages: "lwl_Thai"  # Eastern Lawa
languages: "pi_Thai"  # Pali (Thai)
languages: "sou_Thai"  # Southern Thai
languages: "th_Thai"  # Thai
languages: "tts_Thai"  # Northeastern Thai
primary_script: "Thai"
