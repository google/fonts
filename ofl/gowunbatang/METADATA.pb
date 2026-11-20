name: "Gowun Batang"
designer: "Yanghee Ryu"
license: "OFL"
category: "SERIF"
date_added: "2021-06-10"
fonts {
  name: "Gowun Batang"
  style: "normal"
  weight: 400
  filename: "GowunBatang-Regular.ttf"
  post_script_name: "GowunBatang-Regular"
  full_name: "Gowun Batang Regular"
  copyright: "Copyright 2021 The Gowun Batang Project Authors (https://github.com/yangheeryu/Gowun-Batang)"
}
fonts {
  name: "Gowun Batang"
  style: "normal"
  weight: 700
  filename: "GowunBatang-Bold.ttf"
  post_script_name: "GowunBatang-Bold"
  full_name: "Gowun Batang Bold"
  copyright: "Copyright 2021 The Gowun Batang Project Authors (https://github.com/yangheeryu/Gowun-Batang)"
}
subsets: "korean"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
source {
  repository_url: "https://github.com/googlefonts/gowunbatang"
  commit: "bf6ce63b0e0655f80f377a7ffd28b974903a7908"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/GowunBatang-Regular.ttf"
    dest_file: "GowunBatang-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/GowunBatang-Bold.ttf"
    dest_file: "GowunBatang-Bold.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
primary_script: "Kore"
