name: "PT Serif"
designer: "ParaType"
license: "OFL"
category: "SERIF"
date_added: "2011-02-09"
fonts {
  name: "PT Serif"
  style: "normal"
  weight: 400
  filename: "PT_Serif-Web-Regular.ttf"
  post_script_name: "PTSerif-Regular"
  full_name: "PT Serif"
  copyright: "Copyright © 2010 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Serif"
  style: "italic"
  weight: 400
  filename: "PT_Serif-Web-Italic.ttf"
  post_script_name: "PTSerif-Italic"
  full_name: "PT Serif Italic"
  copyright: "Copyright © 2010 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Serif"
  style: "normal"
  weight: 700
  filename: "PT_Serif-Web-Bold.ttf"
  post_script_name: "PTSerif-Bold"
  full_name: "PT Serif Bold"
  copyright: "Copyright © 2010 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
fonts {
  name: "PT Serif"
  style: "italic"
  weight: 700
  filename: "PT_Serif-Web-BoldItalic.ttf"
  post_script_name: "PTSerif-BoldItalic"
  full_name: "PT Serif Bold Italic"
  copyright: "Copyright © 2010 ParaType Ltd (yakupov@paratype.com). All rights reserved."
}
subsets: "menu"
subsets: "cyrillic"
subsets: "cyrillic-ext"
subsets: "latin"
subsets: "latin-ext"
source {
  repository_url: "https://github.com/googlefonts/ptserif"
  commit: "54cfef3107a5fd42ecbb6d7ce9d2e5f7978458f3"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/PTSerif-Bold.ttf"
    dest_file: "PT_Serif-Web-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSerif-BoldItalic.ttf"
    dest_file: "PT_Serif-Web-BoldItalic.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSerif-Italic.ttf"
    dest_file: "PT_Serif-Web-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/PTSerif-Regular.ttf"
    dest_file: "PT_Serif-Web-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
