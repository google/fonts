name: "Nanum Pen Script"
designer: "Sandoll Communication"
license: "OFL"
category: "HANDWRITING"
date_added: "2012-05-09"
fonts {
  name: "Nanum Pen Script"
  style: "normal"
  weight: 400
  filename: "NanumPenScript-Regular.ttf"
  post_script_name: "NanumPen"
  full_name: "Nanum Pen"
  copyright: "Copyright © 2010 NHN Corporation. All rights reserved. Font designed by Sandoll Communications Inc."
}
subsets: "menu"
subsets: "latin"
subsets: "korean"
primary_script: "Kore"
source {
  repository_url: "https://github.com/googlefonts/nanumpenscript"
  commit: "404860478f027e805535e22988a7823fc43d1848"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/NanumPen-Regular.ttf"
    dest_file: "NanumPenScript-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
