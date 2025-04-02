name: "Artifika"
designer: "Cyreal"
license: "OFL"
category: "SERIF"
date_added: "2011-06-01"
fonts {
  name: "Artifika"
  style: "normal"
  weight: 400
  filename: "Artifika-Regular.ttf"
  post_script_name: "Artifika-Regular"
  full_name: "Artifika Regular"
  copyright: "Copyright 2010 The Artifika Project Authors (https://github.com/cyrealtype/Artifika)"
}
subsets: "latin"
subsets: "menu"
source {
  repository_url: "https://github.com/cyrealtype/Artifika"
  commit: "c317fd292b4e15dc5f42f91c3ec9dff3f7654535"
  config_yaml: "sources/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Artifika-Regular.ttf"
    dest_file: "Artifika-Regular.ttf"
  }
  branch: "master"
}
