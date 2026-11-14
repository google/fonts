name: "AR One Sans"
designer: "Niteesh Yadav"
license: "OFL"
category: "SANS_SERIF"
date_added: "2023-09-06"
fonts {
  name: "AR One Sans"
  style: "normal"
  weight: 400
  filename: "AROneSans[ARRR,wght].ttf"
  post_script_name: "AROneSans-Regular"
  full_name: "AR One Sans Regular"
  copyright: "Copyright 2018 The AR One Project Authors (https://github.com/niteeshy/ar-one-sans)"
}
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "ARRR"
  min_value: 10.0
  max_value: 60.0
}
axes {
  tag: "wght"
  min_value: 400.0
  max_value: 700.0
}
source {
  repository_url: "https://github.com/niteeshy/ar-one-sans"
  commit: "6dc5e6850f2ced9f28e733c9a7860c54246e17a8"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/AROneSans[ARRR,wght].ttf"
    dest_file: "AROneSans[ARRR,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
