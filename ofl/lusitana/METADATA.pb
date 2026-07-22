name: "Lusitana"
designer: "Ana Paula Megda"
license: "OFL"
category: "SERIF"
date_added: "2012-01-11"
fonts {
  name: "Lusitana"
  style: "normal"
  weight: 400
  filename: "Lusitana-Regular.ttf"
  post_script_name: "Lusitana"
  full_name: "Lusitana"
  copyright: "Copyright (c) 2011 by Ana Paula Megda (www.anamegda.com|anapbm@gmail.com), with Reserved Font Name Lusitana."
}
fonts {
  name: "Lusitana"
  style: "normal"
  weight: 700
  filename: "Lusitana-Bold.ttf"
  post_script_name: "Lusitana-Bold"
  full_name: "Lusitana Bold"
  copyright: "Copyright (c) 2011 by Ana Paula Megda (www.anamegda.com|anapbm@gmail.com), with Reserved Font Name Lusitana."
}
subsets: "menu"
subsets: "latin"
subsets: "latin-ext"

source {
  repository_url: "https://github.com/googlefonts/lusitana"
  commit: "393d85168ac2026bfc47c6c15bcb3868e279d92b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Lusitana-Bold.ttf"
    dest_file: "Lusitana-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Lusitana-Regular.ttf"
    dest_file: "Lusitana-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
