use gf_metadata::AxisProto;
use proc_macro2::TokenStream;
use quote::quote;
use std::{
    env,
    fs::File,
    io::{BufWriter, Write},
    path::Path,
};

fn main() {
    let path = Path::new(&env::var("OUT_DIR").unwrap()).join("data.rs");
    let mut file = BufWriter::new(File::create(path).unwrap());
    let mut output = quote! { use std::collections::BTreeMap; use std::sync::LazyLock; };

    output.extend(serialize_a_structure(
        "Lib/axisregistry/data/*.textproto",
        "AXES",
    ));

    // let formatted = output.to_string();

    let abstract_file: syn::File = syn::parse2(output).expect("Could not parse output");
    let formatted = prettyplease::unparse(&abstract_file);
    file.write_all(formatted.as_bytes())
        .expect("Could not write to file");
}

fn serialize_a_structure(pathglob: &str, output_variable: &str) -> TokenStream {
    let files: Vec<std::path::PathBuf> = glob::glob(pathglob)
        .expect("Failed to read glob pattern")
        .flatten()
        .collect();
    let variable: TokenStream = output_variable.parse().unwrap();
    let mut gobbets = vec![];
    let mut names = vec![];
    let mut tags = vec![];
    for file in files.into_iter() {
        let (gobbet, name, tag) = serialize_file(file);
        gobbets.push(gobbet);
        names.push(name);
        tags.push(tag);
    }
    quote! {
        #(#gobbets)*
        #[doc = "A map of all the Axis objects"]
        pub static #variable: LazyLock<BTreeMap<String, Box<AxisProto>>> = LazyLock::new(|| {
            let mut m = BTreeMap::new();
            #(
                let proto: AxisProto = AxisProto::parse_from_str(#names).expect("Could not parse JSON");
                m.insert(#tags.to_string(), Box::new(proto));
            )*
            m
        });
    }
}
fn serialize_file(path: std::path::PathBuf) -> (TokenStream, TokenStream, String) {
    let contents = std::fs::read_to_string(&path).expect("Could not read file");
    let proto: AxisProto = AxisProto::parse_from_str(&contents)
        .unwrap_or_else(|_| panic!("Could not parse proto {}", path.display()));
    let name: TokenStream = format!("AXIS_{}", proto.tag().to_ascii_uppercase())
        .parse()
        .unwrap();
    // Resolve absolute path here
    let path = std::fs::canonicalize(path).unwrap();
    let path_as_string = path.to_str().unwrap();
    let tag: String = proto.tag().to_string().parse().unwrap();
    let include_gobbet = quote! {
        const #name: &str = include_str!(#path_as_string);
    };
    (include_gobbet, name, tag)
}
