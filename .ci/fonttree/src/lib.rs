//! Font Tree: decompile a font into a JSON tree in the browser.
//!
//! Built on fontations (read-fonts, skrifa) plus the `ttj` crate from
//! diffenator3, which is the Rust port of diffenator2's jfont serialisers.

use read_fonts::{
    tables::{
        cff::Cff,
        cmap::{CmapSubtable, MapVariant},
        glyf::{Anchor, Glyph},
        kern::SubtableKind,
        postscript::{
            charstring::{self, CommandSink},
            dict::{self, Entry},
            FdSelect, Index, StringId,
        },
    },
    traversal::{FieldType, SomeArray, SomeTable},
    types::{Fixed, GlyphId, Tag},
    FileRef, FontData, FontRead, FontRef, ReadError, TableProvider,
};
use serde_json::{json, Map, Number, Value};
use skrifa::{string::StringId as NameId, MetadataProvider};
use ttj::namemap::NameMap;
use wasm_bindgen::prelude::*;

/// Versions pinned in Cargo.toml, shown in the page status line.
const ENGINE: &str = "read-fonts 0.35 / skrifa 0.37 / ttj 1.1.4";

#[wasm_bindgen]
pub fn init_panic_hook() {
    console_error_panic_hook::set_once();
}

#[wasm_bindgen]
pub fn version() -> String {
    ENGINE.to_string()
}

/// A font file (sfnt, TTC, WOFF or WOFF2) decoded to raw sfnt bytes.
#[wasm_bindgen]
pub struct FontFile {
    data: Vec<u8>,
    flavor: Option<String>,
}

#[wasm_bindgen]
impl FontFile {
    #[wasm_bindgen(constructor)]
    pub fn new(bytes: &[u8]) -> Result<FontFile, JsValue> {
        let (data, flavor) = decode_container(bytes).map_err(|e| JsValue::from_str(&e))?;
        FileRef::new(&data).map_err(|e| JsValue::from_str(&format!("Not a font: {e}")))?;
        Ok(FontFile { data, flavor })
    }

    /// Number of fonts in the file (more than one for a collection).
    pub fn count(&self) -> u32 {
        self.fonts().len() as u32
    }

    /// JSON array with one summary object per font.
    pub fn summaries(&self) -> String {
        let list: Vec<Value> = self
            .fonts()
            .iter()
            .map(|f| summary(f, self.flavor.as_deref()))
            .collect();
        Value::Array(list).to_string()
    }

    /// JSON object with every table of font `index` decompiled.
    pub fn dump(&self, index: u32) -> Result<String, JsValue> {
        let fonts = self.fonts();
        let font = fonts
            .get(index as usize)
            .ok_or_else(|| JsValue::from_str("font index out of range"))?;
        Ok(dump(font).to_string())
    }
}

impl FontFile {
    fn fonts(&self) -> Vec<FontRef<'_>> {
        match FileRef::new(&self.data) {
            Ok(FileRef::Font(f)) => vec![f],
            Ok(FileRef::Collection(c)) => (0..c.len()).filter_map(|i| c.get(i).ok()).collect(),
            Err(_) => vec![],
        }
    }
}

fn decode_container(bytes: &[u8]) -> Result<(Vec<u8>, Option<String>), String> {
    match bytes.get(0..4) {
        Some(b"wOFF") => wuff::decompress_woff1(bytes)
            .map(|d| (d, Some("WOFF".to_string())))
            .map_err(|e| format!("WOFF decode failed: {e:?}")),
        Some(b"wOF2") => wuff::decompress_woff2(bytes)
            .map(|d| (d, Some("WOFF2".to_string())))
            .map_err(|e| format!("WOFF2 decode failed: {e:?}")),
        Some(_) => Ok((bytes.to_vec(), None)),
        None => Err("file is too small to be a font".to_string()),
    }
}

// ---- summary ---------------------------------------------------------------

fn summary(font: &FontRef, flavor: Option<&str>) -> Value {
    let s = |id: NameId| {
        font.localized_strings(id)
            .english_or_first()
            .map(|x| x.to_string())
    };
    let family = s(NameId::TYPOGRAPHIC_FAMILY_NAME).or_else(|| s(NameId::FAMILY_NAME));
    let style = s(NameId::TYPOGRAPHIC_SUBFAMILY_NAME).or_else(|| s(NameId::SUBFAMILY_NAME));
    let container = match font.table_directory.sfnt_version() {
        0x0001_0000 => "TrueType".to_string(),
        0x4F54_544F => "OpenType CFF".to_string(),
        0x7472_7565 => "TrueType (Apple)".to_string(),
        v => format!("0x{v:08X}"),
    };
    let axes: Vec<String> = font
        .axes()
        .iter()
        .map(|a| {
            format!(
                "{} {}..{}..{}",
                a.tag(),
                a.min_value(),
                a.default_value(),
                a.max_value()
            )
        })
        .collect();
    let tables: Vec<Value> = font
        .table_directory
        .table_records()
        .iter()
        .map(|r| json!({ "tag": r.tag().to_string(), "length": r.length() }))
        .collect();
    json!({
        "family": family,
        "style": style,
        "fullName": s(NameId::FULL_NAME),
        "psName": s(NameId::POSTSCRIPT_NAME),
        "version": s(NameId::VERSION_STRING),
        "upm": font.head().ok().map(|h| h.units_per_em()),
        "glyphs": font.maxp().ok().map(|m| m.num_glyphs()),
        "container": container,
        "flavor": flavor,
        "axes": axes,
        "tables": tables,
    })
}

// ---- dump ------------------------------------------------------------------

fn dump(font: &FontRef) -> Value {
    let names = NameMap::new(font);
    // ttj gives us the readable GDEF/GPOS/GSUB serialisers from diffenator3.
    let mut ttj_map = match ttj::font_to_json(font, Some(&names)) {
        Value::Object(m) => m,
        _ => Map::new(),
    };
    let mut out = Map::new();
    for rec in font.table_directory.table_records() {
        let tag = rec.tag();
        let key = tag.to_string();
        let value = match tag.into_bytes().as_ref() {
            b"GDEF" | b"GPOS" | b"GSUB" => ttj_map
                .remove(&key)
                .unwrap_or_else(|| raw_table(font, tag, rec.length())),
            _ => table_value(font, tag, rec.length(), &names),
        };
        out.insert(key, value);
    }
    Value::Object(out)
}

fn err(e: impl std::fmt::Display) -> Value {
    json!({ "error": e.to_string() })
}

fn trav<'a, T: SomeTable<'a> + 'a>(r: Result<T, ReadError>, names: &NameMap) -> Value {
    match r {
        Ok(t) => ser_table(&t, names),
        Err(e) => err(e),
    }
}

fn table_value(font: &FontRef, tag: Tag, length: u32, names: &NameMap) -> Value {
    match tag.into_bytes().as_ref() {
        b"name" => serialise_name(font),
        b"cmap" => serialise_cmap(font, names),
        b"hmtx" => serialise_hmtx(font, names),
        b"glyf" => serialise_glyf(font, names),
        b"loca" => serialise_loca(font),
        b"CFF " => serialise_cff(font, names),
        b"CFF2" => serialise_cff2(font, names),
        b"kern" => serialise_kern(font, names),
        b"cvt " => match font.cvt() {
            Ok(v) => Value::Array(v.iter().map(|x| Value::from(x.get())).collect()),
            Err(e) => err(e),
        },
        b"fpgm" | b"prep" => {
            let mut v = raw_table(font, tag, length);
            if let Some(o) = v.as_object_mut() {
                o.insert(
                    "note".into(),
                    Value::from("TrueType program; no disassembler in fontations"),
                );
            }
            v
        }
        b"head" => trav(font.head(), names),
        b"hhea" => trav(font.hhea(), names),
        b"vhea" => trav(font.vhea(), names),
        b"vmtx" => serialise_vmtx(font, names),
        b"maxp" => trav(font.maxp(), names),
        b"OS/2" => trav(font.os2(), names),
        b"post" => serialise_post(font, names),
        b"fvar" => trav(font.fvar(), names),
        b"avar" => trav(font.avar(), names),
        b"HVAR" => trav(font.hvar(), names),
        b"VVAR" => trav(font.vvar(), names),
        b"MVAR" => trav(font.mvar(), names),
        b"gvar" => trav(font.gvar(), names),
        b"cvar" => trav(font.cvar(), names),
        b"STAT" => trav(font.stat(), names),
        b"COLR" => trav(font.colr(), names),
        b"CPAL" => trav(font.cpal(), names),
        b"BASE" => trav(font.base(), names),
        b"gasp" => trav(font.gasp(), names),
        b"hdmx" => trav(font.hdmx(), names),
        b"VORG" => trav(font.vorg(), names),
        b"DSIG" => trav(font.dsig(), names),
        b"meta" => trav(font.meta(), names),
        b"sbix" => trav(font.sbix(), names),
        b"SVG " => trav(font.svg(), names),
        b"feat" => trav(font.feat(), names),
        b"ltag" => trav(font.ltag(), names),
        b"ankr" => trav(font.ankr(), names),
        b"trak" => trav(font.trak(), names),
        b"morx" => trav(font.morx(), names),
        b"kerx" => trav(font.kerx(), names),
        b"CBLC" => trav(font.cblc(), names),
        b"CBDT" => trav(font.cbdt(), names),
        b"EBLC" => trav(font.eblc(), names),
        b"EBDT" => trav(font.ebdt(), names),
        b"VARC" => trav(font.varc(), names),
        _ => raw_table(font, tag, length),
    }
}

fn raw_table(font: &FontRef, tag: Tag, length: u32) -> Value {
    const PREVIEW: usize = 64;
    let bytes = font
        .data_for_tag(tag)
        .map(|d| d.as_bytes().to_vec())
        .unwrap_or_default();
    let hex: Vec<String> = bytes
        .iter()
        .take(PREVIEW)
        .map(|b| format!("{b:02x}"))
        .collect();
    let mut hex = hex.join(" ");
    if bytes.len() > PREVIEW {
        hex.push_str(" …");
    }
    json!({ "length": length, "hex": hex })
}

// ---- generic traversal (ported from ttj's serializefont.rs) -----------------

fn ser_table<'a>(t: &dyn SomeTable<'a>, names: &NameMap) -> Value {
    let mut map = Map::new();
    let mut i = 0;
    while let Some(field) = t.get_field(i) {
        map.insert(field.name.to_string(), ser_field(&field.value, names));
        i += 1;
    }
    Value::Object(map)
}

fn ser_array<'a>(a: &dyn SomeArray<'a>, names: &NameMap) -> Value {
    let mut out = Vec::with_capacity(a.len());
    let mut i = 0;
    while let Some(v) = a.get(i) {
        out.push(ser_field(&v, names));
        i += 1;
    }
    Value::Array(out)
}

fn f32v(v: f32) -> Value {
    Number::from_f64(v as f64).map(Value::Number).unwrap_or(Value::Null)
}

fn ser_field<'a>(f: &FieldType<'a>, names: &NameMap) -> Value {
    match f {
        FieldType::I8(v) => Value::from(*v),
        FieldType::U8(v) => Value::from(*v),
        FieldType::I16(v) => Value::from(*v),
        FieldType::U16(v) => Value::from(*v),
        FieldType::I32(v) => Value::from(*v),
        FieldType::U32(v) => Value::from(*v),
        FieldType::I24(v) => Value::from(i32::from(*v)),
        FieldType::U24(v) => Value::from(u32::from(*v)),
        FieldType::Tag(v) => Value::from(v.to_string()),
        FieldType::FWord(v) => Value::from(v.to_i16()),
        FieldType::UfWord(v) => Value::from(v.to_u16()),
        FieldType::MajorMinor(v) => Value::from(format!("{}.{}", v.major, v.minor)),
        FieldType::Version16Dot16(v) => Value::from(v.to_string()),
        FieldType::F2Dot14(v) => f32v(v.to_f32()),
        FieldType::Fixed(v) => f32v(v.to_f32()),
        FieldType::LongDateTime(v) => Value::from(v.as_secs()),
        FieldType::GlyphId16(g) => Value::from(names.get(*g)),
        FieldType::NameId(v) => Value::from(v.to_u16()),
        FieldType::StringOffset(s) => match &s.target {
            Ok(t) => Value::from(t.iter_chars().collect::<String>()),
            Err(e) => err(e),
        },
        FieldType::ArrayOffset(a) => match &a.target {
            Ok(t) => ser_array(t.as_ref(), names),
            Err(e) => err(e),
        },
        FieldType::BareOffset(o) => Value::from(format!("0x{:04X}", o.to_u32())),
        FieldType::ResolvedOffset(o) => match &o.target {
            Ok(t) => ser_table(t.as_ref(), names),
            Err(e) => err(e),
        },
        FieldType::Record(r) => ser_table(r, names),
        FieldType::Array(a) => ser_array(a.as_ref(), names),
        FieldType::Unknown => Value::from("<no representation>"),
    }
}

// ---- name ------------------------------------------------------------------

fn serialise_name(font: &FontRef) -> Value {
    let name = match font.name() {
        Ok(n) => n,
        Err(e) => return err(e),
    };
    let data = name.string_data();
    let mut recs = Vec::new();
    for r in name.name_record() {
        let text = match r.string(data) {
            Ok(s) => Value::from(s.to_string()),
            Err(e) => err(e),
        };
        recs.push(json!({
            "nameID": r.name_id().to_u16(),
            "platformID": r.platform_id(),
            "platEncID": r.encoding_id(),
            "langID": r.language_id(),
            "string": text,
        }));
    }
    let mut by_id: Map<String, Value> = Map::new();
    for r in &recs {
        let key = format!(
            "{} ({},{},0x{:X})",
            r["nameID"],
            r["platformID"],
            r["platEncID"],
            r["langID"].as_u64().unwrap_or(0)
        );
        by_id.insert(key, r["string"].clone());
    }
    json!({ "version": name.version(), "names": by_id, "records": recs })
}

// ---- cmap ------------------------------------------------------------------

fn serialise_cmap(font: &FontRef, names: &NameMap) -> Value {
    let cmap = match font.cmap() {
        Ok(c) => c,
        Err(e) => return err(e),
    };
    let mut best = Map::new();
    for (cp, gid) in font.charmap().mappings() {
        best.insert(format!("U+{cp:04X}"), Value::from(names.get(gid)));
    }
    let data = cmap.offset_data();
    let mut subtables = Vec::new();
    for rec in cmap.encoding_records() {
        let platform = rec.platform_id() as u16;
        let encoding = rec.encoding_id();
        let value = match rec.subtable(data) {
            Err(e) => err(e),
            Ok(st) => {
                let mut mapping = Map::new();
                let (format, extra) = match &st {
                    CmapSubtable::Format4(t) => {
                        for (cp, gid) in t.iter() {
                            mapping.insert(format!("U+{cp:04X}"), Value::from(names.get(gid)));
                        }
                        (4, json!({ "language": t.language() }))
                    }
                    CmapSubtable::Format12(t) => {
                        for (cp, gid) in t.iter() {
                            mapping.insert(format!("U+{cp:04X}"), Value::from(names.get(gid)));
                        }
                        (12, json!({ "language": t.language() }))
                    }
                    CmapSubtable::Format13(t) => {
                        for (cp, gid) in t.iter() {
                            mapping.insert(format!("U+{cp:04X}"), Value::from(names.get(gid)));
                        }
                        (13, json!({ "language": t.language() }))
                    }
                    CmapSubtable::Format14(t) => {
                        for (cp, selector, variant) in t.iter() {
                            let key = format!("U+{cp:04X} U+{selector:04X}");
                            let v = match variant {
                                MapVariant::UseDefault => Value::from("default"),
                                MapVariant::Variant(gid) => Value::from(names.get(gid)),
                            };
                            mapping.insert(key, v);
                        }
                        (14, json!({}))
                    }
                    CmapSubtable::Format0(t) => {
                        for cp in 0u32..256 {
                            if let Some(gid) = t.map_codepoint(cp) {
                                if gid.to_u32() != 0 {
                                    mapping
                                        .insert(format!("U+{cp:04X}"), Value::from(names.get(gid)));
                                }
                            }
                        }
                        (0, json!({ "language": t.language() }))
                    }
                    CmapSubtable::Format6(t) => {
                        for cp in 0u32..0x10000 {
                            if let Some(gid) = t.map_codepoint(cp) {
                                if gid.to_u32() != 0 {
                                    mapping
                                        .insert(format!("U+{cp:04X}"), Value::from(names.get(gid)));
                                }
                            }
                        }
                        (6, json!({ "language": t.language() }))
                    }
                    other => (other.format(), json!({ "note": "mapping not expanded" })),
                };
                let mut o = Map::new();
                o.insert("platformID".into(), Value::from(platform));
                o.insert("platEncID".into(), Value::from(encoding));
                o.insert("format".into(), Value::from(format));
                if let Value::Object(e) = extra {
                    for (k, v) in e {
                        o.insert(k, v);
                    }
                }
                o.insert("cmap".into(), Value::Object(mapping));
                Value::Object(o)
            }
        };
        subtables.push(value);
    }
    json!({ "best": best, "subtables": subtables })
}

// ---- metrics ---------------------------------------------------------------

fn num_glyphs(font: &FontRef) -> u32 {
    font.maxp().map(|m| m.num_glyphs() as u32).unwrap_or(0)
}

fn serialise_hmtx(font: &FontRef, names: &NameMap) -> Value {
    let hmtx = match font.hmtx() {
        Ok(h) => h,
        Err(e) => return err(e),
    };
    let mut map = Map::new();
    for gid in 0..num_glyphs(font) {
        let g = GlyphId::new(gid);
        map.insert(
            names.get(g),
            json!({ "width": hmtx.advance(g), "lsb": hmtx.side_bearing(g) }),
        );
    }
    Value::Object(map)
}

fn serialise_vmtx(font: &FontRef, names: &NameMap) -> Value {
    let vmtx = match font.vmtx() {
        Ok(h) => h,
        Err(e) => return err(e),
    };
    let mut map = Map::new();
    for gid in 0..num_glyphs(font) {
        let g = GlyphId::new(gid);
        map.insert(
            names.get(g),
            json!({ "height": vmtx.advance(g), "tsb": vmtx.side_bearing(g) }),
        );
    }
    Value::Object(map)
}

fn serialise_post(font: &FontRef, names: &NameMap) -> Value {
    let mut v = trav(font.post(), names);
    if let (Ok(post), Some(o)) = (font.post(), v.as_object_mut()) {
        if post.num_names() > 0 {
            let list: Vec<Value> = (0..num_glyphs(font))
                .map(|g| Value::from(names.get(GlyphId::new(g))))
                .collect();
            o.insert("glyphOrder".into(), Value::Array(list));
        }
    }
    v
}

fn serialise_loca(font: &FontRef) -> Value {
    match font.loca(None) {
        Ok(loca) => json!({
            "count": loca.len(),
            "note": "offsets omitted; see glyf",
        }),
        Err(e) => err(e),
    }
}

// ---- glyf ------------------------------------------------------------------

fn serialise_glyf(font: &FontRef, names: &NameMap) -> Value {
    let loca = match font.loca(None) {
        Ok(l) => l,
        Err(e) => return err(e),
    };
    let glyf = match font.glyf() {
        Ok(g) => g,
        Err(e) => return err(e),
    };
    let mut map = Map::new();
    for gid in 0..num_glyphs(font) {
        let g = GlyphId::new(gid);
        let v = match loca.get_glyf(g, &glyf) {
            Ok(None) => json!({}),
            Ok(Some(Glyph::Simple(s))) => {
                let ends: Vec<usize> = s
                    .end_pts_of_contours()
                    .iter()
                    .map(|e| e.get() as usize)
                    .collect();
                let pts: Vec<Value> = s
                    .points()
                    .map(|p| json!({ "x": p.x, "y": p.y, "on": p.on_curve }))
                    .collect();
                let mut contours = Vec::new();
                let mut start = 0;
                for end in ends {
                    let stop = (end + 1).min(pts.len());
                    if start < stop {
                        contours.push(Value::Array(pts[start..stop].to_vec()));
                    }
                    start = stop;
                }
                json!({
                    "numberOfContours": s.number_of_contours(),
                    "xMin": s.x_min(), "yMin": s.y_min(), "xMax": s.x_max(), "yMax": s.y_max(),
                    "contours": contours,
                    "instructions": s.instructions().len(),
                })
            }
            Ok(Some(Glyph::Composite(c))) => {
                let comps: Vec<Value> = c
                    .components()
                    .map(|comp| {
                        let anchor = match comp.anchor {
                            Anchor::Offset { x, y } => json!({ "x": x, "y": y }),
                            Anchor::Point { base, component } => {
                                json!({ "basePoint": base, "componentPoint": component })
                            }
                        };
                        let t = comp.transform;
                        json!({
                            "glyph": names.get(comp.glyph),
                            "flags": format!("{:?}", comp.flags),
                            "anchor": anchor,
                            "transform": [t.xx.to_f32(), t.yx.to_f32(), t.xy.to_f32(), t.yy.to_f32()],
                        })
                    })
                    .collect();
                json!({
                    "numberOfContours": c.number_of_contours(),
                    "xMin": c.x_min(), "yMin": c.y_min(), "xMax": c.x_max(), "yMax": c.y_max(),
                    "components": comps,
                    "instructions": c.instructions().map(|i| i.len()).unwrap_or(0),
                })
            }
            Err(e) => err(e),
        };
        map.insert(names.get(g), v);
    }
    Value::Object(map)
}

// ---- kern ------------------------------------------------------------------

fn serialise_kern(font: &FontRef, names: &NameMap) -> Value {
    let kern = match font.kern() {
        Ok(k) => k,
        Err(e) => return err(e),
    };
    let mut subtables = Vec::new();
    for st in kern.subtables() {
        let st = match st {
            Ok(s) => s,
            Err(e) => {
                subtables.push(err(e));
                continue;
            }
        };
        let mut o = Map::new();
        o.insert("vertical".into(), Value::from(st.is_vertical()));
        o.insert("crossStream".into(), Value::from(st.is_cross_stream()));
        o.insert("variable".into(), Value::from(st.is_variable()));
        match st.kind() {
            Ok(SubtableKind::Format0(s)) => {
                let mut pairs = Map::new();
                for p in s.pairs() {
                    pairs.insert(
                        format!("{} {}", names.get(p.left()), names.get(p.right())),
                        Value::from(p.value()),
                    );
                }
                o.insert("format".into(), Value::from(0));
                o.insert("pairs".into(), Value::Object(pairs));
            }
            Ok(SubtableKind::Format1(_)) => {
                o.insert("format".into(), Value::from(1));
                o.insert("note".into(), Value::from("state table; not expanded"));
            }
            Ok(SubtableKind::Format2(_)) => {
                o.insert("format".into(), Value::from(2));
                o.insert("note".into(), Value::from("class table; not expanded"));
            }
            Ok(SubtableKind::Format3(_)) => {
                o.insert("format".into(), Value::from(3));
                o.insert("note".into(), Value::from("index table; not expanded"));
            }
            Err(e) => {
                o.insert("error".into(), Value::from(e.to_string()));
            }
        }
        subtables.push(Value::Object(o));
    }
    json!({ "subtables": subtables })
}

// ---- CFF / CFF2 ------------------------------------------------------------

struct PathSink {
    cmds: Vec<String>,
}

fn fx(v: Fixed) -> f32 {
    v.to_f32()
}

impl CommandSink for PathSink {
    fn move_to(&mut self, x: Fixed, y: Fixed) {
        self.cmds.push(format!("moveTo {} {}", fx(x), fx(y)));
    }
    fn line_to(&mut self, x: Fixed, y: Fixed) {
        self.cmds.push(format!("lineTo {} {}", fx(x), fx(y)));
    }
    fn curve_to(&mut self, cx0: Fixed, cy0: Fixed, cx1: Fixed, cy1: Fixed, x: Fixed, y: Fixed) {
        self.cmds.push(format!(
            "curveTo {} {} {} {} {} {}",
            fx(cx0),
            fx(cy0),
            fx(cx1),
            fx(cy1),
            fx(x),
            fx(y)
        ));
    }
    fn close(&mut self) {
        self.cmds.push("closePath".to_string());
    }
    fn hstem(&mut self, y: Fixed, dy: Fixed) {
        self.cmds.push(format!("hstem {} {}", fx(y), fx(dy)));
    }
    fn vstem(&mut self, x: Fixed, dx: Fixed) {
        self.cmds.push(format!("vstem {} {}", fx(x), fx(dx)));
    }
}

fn sid_value(cff: Option<&Cff>, id: StringId) -> Value {
    match cff.and_then(|c| c.string(id)) {
        Some(s) => Value::from(s.to_string()),
        None => match id.standard_string() {
            Ok(s) => Value::from(s.to_string()),
            Err(_) => Value::from(format!("SID {}", id.to_u16())),
        },
    }
}

fn fixed_list(v: &[Fixed]) -> Value {
    Value::Array(v.iter().map(|x| f32v(x.to_f32())).collect())
}

fn blues(b: &dict::Blues) -> Value {
    Value::Array(
        b.values()
            .iter()
            .map(|(a, b)| json!([f32v(a.to_f32()), f32v(b.to_f32())]))
            .collect(),
    )
}

fn entry_kv(e: Entry, cff: Option<&Cff>) -> (&'static str, Value) {
    let sid = |id| sid_value(cff, id);
    let f = |v: Fixed| f32v(v.to_f32());
    match e {
        Entry::Version(s) => ("version", sid(s)),
        Entry::Notice(s) => ("Notice", sid(s)),
        Entry::FullName(s) => ("FullName", sid(s)),
        Entry::FamilyName(s) => ("FamilyName", sid(s)),
        Entry::Weight(s) => ("Weight", sid(s)),
        Entry::Copyright(s) => ("Copyright", sid(s)),
        Entry::PostScript(s) => ("PostScript", sid(s)),
        Entry::BaseFontName(s) => ("BaseFontName", sid(s)),
        Entry::FontName(s) => ("FontName", sid(s)),
        Entry::FontBbox(b) => ("FontBBox", fixed_list(&b)),
        Entry::CharstringsOffset(o) => ("CharStrings", json!({ "offset": o })),
        Entry::PrivateDictRange(r) => ("Private", json!({ "offset": r.start, "size": r.len() })),
        Entry::VariationStoreOffset(o) => ("vstore", json!({ "offset": o })),
        Entry::IsFixedPitch(b) => ("isFixedPitch", Value::from(b)),
        Entry::ItalicAngle(v) => ("ItalicAngle", f(v)),
        Entry::UnderlinePosition(v) => ("UnderlinePosition", f(v)),
        Entry::UnderlineThickness(v) => ("UnderlineThickness", f(v)),
        Entry::PaintType(v) => ("PaintType", Value::from(v)),
        Entry::CharstringType(v) => ("CharstringType", Value::from(v)),
        Entry::FontMatrix(m, scale) => (
            "FontMatrix",
            json!({ "matrix": fixed_list(&m), "scaledUpem": scale }),
        ),
        Entry::StrokeWidth(v) => ("StrokeWidth", f(v)),
        Entry::FdArrayOffset(o) => ("FDArray", json!({ "offset": o })),
        Entry::FdSelectOffset(o) => ("FDSelect", json!({ "offset": o })),
        Entry::BlueValues(b) => ("BlueValues", blues(&b)),
        Entry::OtherBlues(b) => ("OtherBlues", blues(&b)),
        Entry::FamilyBlues(b) => ("FamilyBlues", blues(&b)),
        Entry::FamilyOtherBlues(b) => ("FamilyOtherBlues", blues(&b)),
        Entry::SubrsOffset(o) => ("Subrs", json!({ "offset": o })),
        Entry::VariationStoreIndex(v) => ("vsindex", Value::from(v)),
        Entry::BlueScale(v) => ("BlueScale", f(v)),
        Entry::BlueShift(v) => ("BlueShift", f(v)),
        Entry::BlueFuzz(v) => ("BlueFuzz", f(v)),
        Entry::LanguageGroup(v) => ("LanguageGroup", Value::from(v)),
        Entry::ExpansionFactor(v) => ("ExpansionFactor", f(v)),
        Entry::Encoding(o) => ("Encoding", json!({ "offset": o })),
        Entry::Charset(o) => ("charset", json!({ "offset": o })),
        Entry::UniqueId(v) => ("UniqueID", Value::from(v)),
        Entry::Xuid => ("XUID", Value::Null),
        Entry::SyntheticBase(v) => ("SyntheticBase", Value::from(v)),
        Entry::BaseFontBlend => ("BaseFontBlend", Value::Null),
        Entry::Ros {
            registry,
            ordering,
            supplement,
        } => (
            "ROS",
            json!({ "registry": sid(registry), "ordering": sid(ordering), "supplement": f(supplement) }),
        ),
        Entry::CidFontVersion(v) => ("CIDFontVersion", f(v)),
        Entry::CidFontRevision(v) => ("CIDFontRevision", f(v)),
        Entry::CidFontType(v) => ("CIDFontType", Value::from(v)),
        Entry::CidCount(v) => ("CIDCount", Value::from(v)),
        Entry::UidBase(v) => ("UIDBase", Value::from(v)),
        Entry::StdHw(v) => ("StdHW", f(v)),
        Entry::StdVw(v) => ("StdVW", f(v)),
        Entry::DefaultWidthX(v) => ("defaultWidthX", f(v)),
        Entry::NominalWidthX(v) => ("nominalWidthX", f(v)),
        Entry::StemSnapH(s) => ("StemSnapH", fixed_list(s.values())),
        Entry::StemSnapV(s) => ("StemSnapV", fixed_list(s.values())),
        Entry::ForceBold(b) => ("ForceBold", Value::from(b)),
        Entry::InitialRandomSeed(v) => ("initialRandomSeed", Value::from(v)),
    }
}

fn dict_to_value(data: &[u8], cff: Option<&Cff>) -> Value {
    let mut map = Map::new();
    for e in dict::entries(data, None) {
        match e {
            Ok(e) => {
                let (k, v) = entry_kv(e, cff);
                map.insert(k.to_string(), v);
            }
            Err(e) => {
                map.insert("error".into(), Value::from(e.to_string()));
                break;
            }
        }
    }
    Value::Object(map)
}

/// The parts of a top dict or FD dict we need to walk charstrings.
#[derive(Default)]
struct DictInfo {
    charstrings: Option<usize>,
    private: Option<std::ops::Range<usize>>,
    fd_array: Option<usize>,
    fd_select: Option<usize>,
}

fn dict_info(data: &[u8]) -> DictInfo {
    let mut info = DictInfo::default();
    for e in dict::entries(data, None).flatten() {
        match e {
            Entry::CharstringsOffset(o) => info.charstrings = Some(o),
            Entry::PrivateDictRange(r) => info.private = Some(r),
            Entry::FdArrayOffset(o) => info.fd_array = Some(o),
            Entry::FdSelectOffset(o) => info.fd_select = Some(o),
            _ => {}
        }
    }
    info
}

/// Local subrs for a private dict range, if it declares any.
fn local_subrs<'a>(
    data: &'a [u8],
    private: &Option<std::ops::Range<usize>>,
    is_cff2: bool,
) -> Option<Index<'a>> {
    let r = private.clone()?;
    let pdata = data.get(r.clone())?;
    let off = dict::entries(pdata, None)
        .flatten()
        .find_map(|e| match e {
            Entry::SubrsOffset(o) => Some(o),
            _ => None,
        })?;
    Index::new(data.get(r.start + off..)?, is_cff2).ok()
}

struct CharstringEnv<'a> {
    data: &'a [u8],
    charstrings: Index<'a>,
    global_subrs: Index<'a>,
    subrs: Option<Index<'a>>,
    fd_subrs: Vec<Option<Index<'a>>>,
    fd_select: Option<FdSelect<'a>>,
}

fn charstrings_value(env: &CharstringEnv, names: &NameMap) -> Value {
    let mut map = Map::new();
    for gid in 0..env.charstrings.count() {
        let g = GlyphId::new(gid);
        let v = match env.charstrings.get(gid as usize) {
            Err(e) => err(e),
            Ok(cs) => {
                let subrs = match &env.fd_select {
                    Some(sel) => sel
                        .font_index(g)
                        .and_then(|fd| env.fd_subrs.get(fd as usize).cloned().flatten()),
                    None => env.subrs.clone(),
                };
                let mut sink = PathSink { cmds: Vec::new() };
                match charstring::evaluate(
                    env.data,
                    env.charstrings.clone(),
                    env.global_subrs.clone(),
                    subrs,
                    None,
                    cs,
                    &mut sink,
                ) {
                    Ok(()) => json!({ "length": cs.len(), "program": sink.cmds }),
                    Err(e) => {
                        json!({ "length": cs.len(), "program": sink.cmds, "error": e.to_string() })
                    }
                }
            }
        };
        map.insert(names.get(g), v);
    }
    Value::Object(map)
}

fn fd_array_value<'a>(
    data: &'a [u8],
    offset: usize,
    cff: Option<&Cff>,
    is_cff2: bool,
) -> (Value, Vec<Option<Index<'a>>>) {
    let idx = match data.get(offset..).map(|d| Index::new(d, is_cff2)) {
        Some(Ok(i)) => i,
        Some(Err(e)) => return (err(e), vec![]),
        None => return (err("FDArray offset out of range"), vec![]),
    };
    let mut list = Vec::new();
    let mut subrs = Vec::new();
    for i in 0..idx.count() as usize {
        match idx.get(i) {
            Ok(fd) => {
                let info = dict_info(fd);
                let private = info
                    .private
                    .as_ref()
                    .and_then(|r| data.get(r.clone()))
                    .map(|p| dict_to_value(p, cff));
                list.push(json!({ "dict": dict_to_value(fd, cff), "Private": private }));
                subrs.push(local_subrs(data, &info.private, is_cff2));
            }
            Err(e) => {
                list.push(err(e));
                subrs.push(None);
            }
        }
    }
    (Value::Array(list), subrs)
}

fn serialise_cff(font: &FontRef, names: &NameMap) -> Value {
    let cff = match font.cff() {
        Ok(c) => c,
        Err(e) => return err(e),
    };
    let data = cff.offset_data().as_bytes();
    let h = cff.header();
    let mut out = Map::new();
    out.insert(
        "header".into(),
        json!({ "major": h.major(), "minor": h.minor(), "hdrSize": h.hdr_size(), "offSize": h.off_size() }),
    );
    let font_names: Vec<Value> = (0..cff.names().count() as usize)
        .filter_map(|i| cff.name(i))
        .map(|s| Value::from(s.to_string()))
        .collect();
    out.insert("fontNames".into(), Value::Array(font_names));
    let top = cff.top_dicts().get(0).unwrap_or(&[]);
    out.insert("topDict".into(), dict_to_value(top, Some(&cff)));
    out.insert("strings".into(), json!({ "count": cff.strings().count() }));
    out.insert(
        "globalSubrs".into(),
        json!({ "count": cff.global_subrs().count() }),
    );
    let info = dict_info(top);
    if let Some(p) = info.private.as_ref().and_then(|r| data.get(r.clone())) {
        out.insert("Private".into(), dict_to_value(p, Some(&cff)));
    }
    let mut fd_subrs = Vec::new();
    if let Some(off) = info.fd_array {
        let (v, s) = fd_array_value(data, off, Some(&cff), false);
        out.insert("FDArray".into(), v);
        fd_subrs = s;
    }
    let fd_select = info
        .fd_select
        .and_then(|off| data.get(off..))
        .and_then(|d| FdSelect::read(FontData::new(d)).ok());
    if let Some(off) = info.charstrings {
        match data.get(off..).map(|d| Index::new(d, false)) {
            Some(Ok(cs)) => {
                let env = CharstringEnv {
                    data,
                    charstrings: cs,
                    global_subrs: Index::Format1(cff.global_subrs()),
                    subrs: local_subrs(data, &info.private, false),
                    fd_subrs,
                    fd_select,
                };
                out.insert("CharStrings".into(), charstrings_value(&env, names));
            }
            Some(Err(e)) => {
                out.insert("CharStrings".into(), err(e));
            }
            None => {
                out.insert("CharStrings".into(), err("offset out of range"));
            }
        }
    }
    Value::Object(out)
}

fn serialise_cff2(font: &FontRef, names: &NameMap) -> Value {
    let cff2 = match font.cff2() {
        Ok(c) => c,
        Err(e) => return err(e),
    };
    let data = cff2.offset_data().as_bytes();
    let h = cff2.header();
    let mut out = Map::new();
    out.insert(
        "header".into(),
        json!({
            "majorVersion": h.major_version(), "minorVersion": h.minor_version(),
            "headerSize": h.header_size(), "topDictLength": h.top_dict_length(),
        }),
    );
    let top = cff2.top_dict_data();
    out.insert("topDict".into(), dict_to_value(top, None));
    out.insert(
        "globalSubrs".into(),
        json!({ "count": cff2.global_subrs().count() }),
    );
    let info = dict_info(top);
    let mut fd_subrs = Vec::new();
    if let Some(off) = info.fd_array {
        let (v, s) = fd_array_value(data, off, None, true);
        out.insert("FDArray".into(), v);
        fd_subrs = s;
    }
    let fd_select = info
        .fd_select
        .and_then(|off| data.get(off..))
        .and_then(|d| FdSelect::read(FontData::new(d)).ok());
    if let Some(off) = info.charstrings {
        match data.get(off..).map(|d| Index::new(d, true)) {
            Some(Ok(cs)) => {
                let env = CharstringEnv {
                    data,
                    charstrings: cs,
                    global_subrs: Index::Format2(cff2.global_subrs()),
                    subrs: None,
                    fd_subrs,
                    fd_select,
                };
                out.insert("CharStrings".into(), charstrings_value(&env, names));
                out.insert(
                    "note".into(),
                    Value::from(
                        "charstrings are shown at the default location; blend operators are not applied",
                    ),
                );
            }
            Some(Err(e)) => {
                out.insert("CharStrings".into(), err(e));
            }
            None => {
                out.insert("CharStrings".into(), err("offset out of range"));
            }
        }
    }
    Value::Object(out)
}
