name: "ADLaM Display"
designer: "Mark Jamra, Neil Patel, Andrew Footit"
license: "OFL"
category: "DISPLAY"
date_added: "2023-07-10"
fonts {
  name: "ADLaM Display"
  style: "normal"
  weight: 400
  filename: "ADLaMDisplay-Regular.ttf"
  post_script_name: "ADLaMDisplay-Regular"
  full_name: "ADLaM Display Regular"
  copyright: "Copyright (c) 2022 by Microsoft. All rights reserved."
}
subsets: "adlam"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
source {
  repository_url: "https://github.com/microsoft/ADLaM-Display"
  commit: "879176243e9f7161a8aefdab8c36a4a7318ebe15"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/ttf/ADLaMDisplay-Regular.ttf"
    dest_file: "ADLaMDisplay-Regular.ttf"
  }
  branch: "main"
}
primary_script: "Adlm"
