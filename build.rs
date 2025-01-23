use proc_macro2::TokenStream;
use protobuf::reflect::{FieldDescriptor, ReflectValueRef};
use quote::quote;
use serde_json::Map;
use std::io::{BufWriter, Write};
use std::{env, fs::File, path::Path};

fn main() {
    // First we load up the descriptor using the protobuf crate
    // so that we can do reflection on it.
    let descriptors = protobuf_parse::Parser::new()
        .pure()
        .include(".")
        .input("Lib/axisregistry/axes.proto")
        .file_descriptor_set()
        .expect("Could not parse axes.proto");
    let protofile = descriptors.file.first().expect("No file in descriptor");
    let descriptor = protobuf::reflect::FileDescriptor::new_dynamic(protofile.clone(), &[])
        .expect("Could not create descriptor");

    // Now we use the prost crate to compile them, so that we can
    // generate Rust structs.
    let mut config = prost_build::Config::new();
    // config.boxed(".google.axes.LanguageProto.sample_text");
    // config.boxed(".google.axes.LanguageProto.exemplar_chars");

    // The reflection can tell us what messages we have, so we can configure
    // them to be deserializable with serde
    for message in descriptor.messages() {
        config.type_attribute(
            message.full_name(),
            "#[derive(serde::Serialize, serde::Deserialize)]",
        );
    }
    // Let's make our structs; this produces google.axes.rs
    config
        .compile_protos(&["Lib/axisregistry/axes.proto"], &["Lib/axisregistry/"])
        .expect("Could not compile axes.proto");

    let path = Path::new(&env::var("OUT_DIR").unwrap()).join("data.rs");
    let mut file = BufWriter::new(File::create(path).unwrap());
    let mut output = quote! { use std::collections::BTreeMap; use std::sync::LazyLock; };

    output.extend(serialize_a_structure(
        ".AxisProto",
        "Lib/axisregistry/data/*.textproto",
        "AXES",
        &descriptor,
    ));

    // file.write_all(output.to_string().as_bytes())
    //     .expect("Could not write to file");

    let abstract_file: syn::File = syn::parse2(output).expect("Could not parse output");
    let formatted = prettyplease::unparse(&abstract_file);
    file.write_all(formatted.as_bytes())
        .expect("Could not write to file");
}

fn serialize_a_structure(
    proto_name: &str,
    pathglob: &str,
    output_variable: &str,
    descriptor: &protobuf::reflect::FileDescriptor,
) -> TokenStream {
    let proto = descriptor
        .message_by_full_name(proto_name)
        .unwrap_or_else(|| panic!("No {} message", proto_name));
    let files: Vec<std::path::PathBuf> = glob::glob(pathglob)
        .expect("Failed to read glob pattern")
        .flatten()
        .collect();
    let name: TokenStream = proto.name().parse().unwrap();
    let variable: TokenStream = output_variable.parse().unwrap();
    let mut map = Map::new();
    for file in files.into_iter() {
        serialize_file(file, &proto, &mut map);
    }
    let json_var: TokenStream = format!("__{}", output_variable).parse().unwrap();
    let docmsg = format!("A map of all the {} objects", name);
    let json_dump = serde_json::to_string(&map).expect("Could not serialize");
    quote! {
        static #json_var: &str = #json_dump;

        #[doc = #docmsg]
        pub static #variable: LazyLock<BTreeMap<String, Box<#name>>> = LazyLock::new(|| {
            serde_json::from_str(#json_var).expect("Could not deserialize")
        });
    }
}
fn serialize_file(
    path: std::path::PathBuf,
    descriptor: &protobuf::reflect::MessageDescriptor,
    value: &mut Map<String, serde_json::Value>,
) {
    let mut message = descriptor.new_instance();
    let message_mut = message.as_mut();
    let input = std::fs::read_to_string(&path).expect("Could not read file");
    protobuf::text_format::merge_from_str(message_mut, &input)
        .unwrap_or_else(|e| panic!("Could not parse file {:?}: {:?}", path, e));
    let message = serialize_message(message_mut);
    value.insert(
        message.get("tag").unwrap().as_str().unwrap().to_string(),
        message,
    );
}

fn serialize_message(message: &dyn protobuf::MessageDyn) -> serde_json::Value {
    let descriptor = message.descriptor_dyn();
    // let descriptor_name: TokenStream = descriptor.name().parse().unwrap();
    let mut output = Map::new();
    for field in descriptor.fields() {
        let field_name: TokenStream = field.name().parse().unwrap();
        let field_contents = serialize_field(&field, message);
        output.insert(field_name.to_string(), field_contents);
    }
    output.into()
}

fn serialize_field(
    field: &FieldDescriptor,
    message: &dyn protobuf::MessageDyn,
) -> serde_json::Value {
    if field.is_repeated() {
        let v: Vec<serde_json::Value> = field
            .get_repeated(message)
            .into_iter()
            .map(|value| serialize_field_value(field, value))
            .collect();
        v.into()
    } else if field.is_required() {
        serialize_field_value(field, field.get_singular(message).unwrap())
    } else if field.has_field(message) {
        let value = serialize_field_value(field, field.get_singular(message).unwrap());
        value.into()
    } else {
        serde_json::Value::Null
    }
}

fn serialize_field_value(_field: &FieldDescriptor, value: ReflectValueRef) -> serde_json::Value {
    match value {
        ReflectValueRef::Bool(value) => value.into(),
        ReflectValueRef::I32(value) => value.into(),
        ReflectValueRef::I64(value) => value.into(),
        ReflectValueRef::U32(value) => value.into(),
        ReflectValueRef::U64(value) => value.into(),
        ReflectValueRef::F32(value) => value.into(),
        ReflectValueRef::F64(value) => value.into(),
        ReflectValueRef::String(value) => value.into(),
        ReflectValueRef::Bytes(value) => value.into(),
        ReflectValueRef::Enum(_value, _ix) => unimplemented!(),
        ReflectValueRef::Message(value) => serialize_message(&*value),
    }
}
