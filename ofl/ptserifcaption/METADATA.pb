name: "PT Serif Caption"
designer: "ParaType"
license: "OFL"
category: "SERIF"
date_added: "2011-02-09"
fonts {
  name: "PT Serif Caption"
  style: "normal"
  weight: 400
  filename: "PT_Serif-Caption-Web-Regular.ttf"
  post_script_name: "PTSerif-Caption"
  full_name: "PT Serif Caption"
  copyright: "Copyright © 2010 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Serif Caption"
  style: "italic"
  weight: 400
  filename: "PT_Serif-Caption-Web-Italic.ttf"
  post_script_name: "PTSerif-CaptionItalic"
  full_name: "PT Serif Caption Italic"
  copyright: "Copyright © 2010 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
subsets: "menu"
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
source {
  repository_url: "https://github.com/googlefonts/ptserifcaption"
  commit: "95cb161f0ed9d42004b5a88144d434319eb53a75"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/PTSerifCaption-Italic.ttf"
    dest_file: "PT_Serif-Caption-Web-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSerifCaption-Regular.ttf"
    dest_file: "PT_Serif-Caption-Web-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
