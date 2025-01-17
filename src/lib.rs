use std::{collections::HashSet, ops::Index};

use indexmap::IndexMap;
#[cfg(feature = "fontations")]
use write_fonts::{
    read::FontRef,
    read::{ReadError, TableProvider},
    FontBuilder,
};

include!(concat!(env!("OUT_DIR"), "/_.rs"));
include!(concat!(env!("OUT_DIR"), "/data.rs"));

const LINKED_VALUES: [(&str, (f32, f32)); 2] = [("wght", (400.0, 700.0)), ("ital", (0.0, 1.0))];
const GF_STATIC_STYLES: [(&str, u16); 18] = [
    ("Thin", 100),
    ("ExtraLight", 200),
    ("Light", 300),
    ("Regular", 400),
    ("Medium", 500),
    ("SemiBold", 600),
    ("Bold", 700),
    ("ExtraBold", 800),
    ("Black", 900),
    ("Thin Italic", 100),
    ("ExtraLight Italic", 200),
    ("Light Italic", 300),
    ("Italic", 400),
    ("Medium Italic", 500),
    ("SemiBold Italic", 600),
    ("Bold Italic", 700),
    ("ExtraBold Italic", 800),
    ("Black Italic", 900),
];

pub struct AxisRegistry {
    axes: BTreeMap<String, Box<AxisProto>>,
}

pub struct FontAxis {
    pub tag: String,
    pub min: f32,
    pub max: f32,
    pub default: f32,
}

pub struct NameParticle {
    pub name: Option<String>,
    pub value: f32,
    pub elided: bool,
}

impl AxisRegistry {
    pub fn new() -> Self {
        Self {
            axes: (*AXES).clone(),
        }
    }

    pub fn get(&self, tag: &str) -> Option<&AxisProto> {
        self.axes.get(tag).map(|v| &**v)
    }

    pub fn contains_key(&self, tag: &str) -> bool {
        self.axes.contains_key(tag)
    }

    pub fn iter(&self) -> impl Iterator<Item = (&String, &AxisProto)> {
        self.axes.iter().map(|(k, v)| (k, &**v))
    }

    pub fn get_fallback<'a>(&'a self, name: &str) -> Option<(&'a str, &'a FallbackProto)> {
        self.axes
            .iter()
            .flat_map(|(tag, axis)| {
                let fallback = axis
                    .fallback
                    .iter()
                    .find(|f| f.name.as_deref() == Some(name));
                fallback.map(|f| (tag.as_str(), f))
            })
            .next()
    }

    // This is fallbacks_in_fvar, but without assuming any particular font representation
    pub fn fallbacks<'a>(
        &'a self,
        font_axes: &'a [FontAxis],
    ) -> impl Iterator<Item = (String, Vec<FallbackProto>)> + 'a {
        font_axes.iter().filter_map(|axis| {
            self.get(&axis.tag).map(|registry_axis| {
                (
                    registry_axis.tag.clone().unwrap_or_default(),
                    registry_axis
                        .fallback
                        .iter()
                        .filter(|f| {
                            f.value.unwrap_or(-f32::INFINITY) <= axis.min
                                && f.value.unwrap_or(f32::INFINITY) >= axis.max
                        })
                        .cloned()
                        .collect(),
                )
            })
        })
    }

    // This is fallbacks_in_name_table, but without assuming any particular font representation
    pub fn name_table_fallbacks<'a>(
        &'a self,
        family_name: &'a str,
        subfamily_name: &'a str,
        font_axes: &'a [FontAxis],
    ) -> impl Iterator<Item = (&'a str, &'a FallbackProto)> + 'a {
        let axis_names: HashSet<&str> = font_axes.iter().map(|axis| axis.tag.as_ref()).collect();
        let tokens = family_name
            .split_whitespace()
            .skip(1)
            .chain(subfamily_name.split_whitespace());
        tokens
            .flat_map(|token| self.get_fallback(token))
            .filter(move |(tag, _)| axis_names.contains(tag))
    }

    pub fn fallback_for_value<'a>(
        &'a self,
        axis_tag: &str,
        value: f32,
    ) -> Option<&'a FallbackProto> {
        self.get(axis_tag)
            .and_then(|axis| axis.fallback.iter().find(|f| f.value == Some(value)))
    }

    pub fn axis_order(&self) -> Vec<&str> {
        let mut axis_tags: Vec<&str> = self.axes.keys().map(|k| k.as_str()).collect();
        axis_tags.sort();
        axis_tags.extend(vec!["opsz", "wdth", "wght", "ital", "slnt"]);
        axis_tags
    }

    pub fn name_particles<'a>(&self, font_axes: &'a [FontAxis]) -> IndexMap<&'a str, NameParticle> {
        let mut particles = IndexMap::new();
        for axis in font_axes {
            if axis.tag == "opsz" {
                particles.insert(
                    "opsz",
                    NameParticle {
                        name: Some(format!("{}pt", axis.default)),
                        value: axis.default,
                        elided: false,
                    },
                );
            } else if let Some(fallback) = self.fallback_for_value(&axis.tag, axis.default) {
                particles.insert(
                    &axis.tag,
                    NameParticle {
                        name: fallback.name.clone(),
                        value: axis.default,
                        elided: (fallback.value() == axis.default)
                            && !(["Regular", "Italic", "14pt"].contains(&fallback.name())),
                    },
                );
            } else {
                particles.insert(
                    &axis.tag,
                    NameParticle {
                        name: None,
                        value: axis.default,
                        elided: true,
                    },
                );
            };
        }
        particles
    }
}

impl Default for AxisRegistry {
    fn default() -> Self {
        Self::new()
    }
}

impl Index<&str> for AxisRegistry {
    type Output = AxisProto;

    fn index(&self, tag: &str) -> &Self::Output {
        self.get(tag).expect("No such axis")
    }
}

#[cfg(feature = "fontations")]
mod nametable;

#[cfg(feature = "fontations")]
mod fontations {
    use super::*;
    use nametable::{best_familyname, best_subfamilyname, find_or_add_name, rewrite_or_insert};
    use skrifa::{string::StringId, Tag};
    use std::{cmp::Reverse, collections::HashMap};
    use write_fonts::{
        from_obj::ToOwnedTable,
        tables::{
            name::{Name, NameRecord},
            os2::Os2,
            stat::{AxisValue, Stat},
        },
        types::Fixed,
    };

    pub fn build_name_table(
        font: FontRef,
        family_name: Option<&str>,
        style_name: Option<&str>,
        siblings: &[FontRef],
    ) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
        let mut new_font = FontBuilder::new();
        let family_name = family_name
            .map(|x| x.to_string())
            .unwrap_or_else(|| best_familyname(&font).unwrap_or("Unknown".to_string()));
        let style_name = style_name
            .map(|x| x.to_string())
            .unwrap_or_else(|| best_subfamilyname(&font).unwrap_or("Regular".to_string()));

        if font.table_data(Tag::new(b"fvar")).is_some() {
            build_vf_name_table(&mut new_font, &font, &family_name, siblings)?;
        } else {
            // build_static_name_table_v1(&mut new_font, &font, &family_name, &style_name)
        }

        let mut styles: Vec<_> = GF_STATIC_STYLES.iter().collect();
        styles.sort_by_key(|(name, _weight)| Reverse(name.len()));
        for (name, weight) in styles.iter() {
            if style_name.contains(name) {
                let mut new_os2: Os2 = font.os2()?.to_owned_table();
                new_os2.us_weight_class = *weight;
                new_font.add_table(&new_os2)?;
                break;
            }
        }
        // Set RIBBI bits
        Ok(new_font.copy_missing_tables(font).build())
    }

    fn fvar_instance_collisions(font: &FontRef, siblings: &[FontRef]) -> bool {
        let fonts = siblings.iter().chain(std::iter::once(font));
        let is_italic = fonts
            .map(|f| {
                f.post()
                    .map(|post| post.italic_angle().abs() != Fixed::from_f64(0.0))
                    .unwrap_or(false)
            })
            .collect::<Vec<_>>();
        // Any duplicates?
        is_italic.iter().any(|&x| x) && is_italic.iter().all(|&x| x)
    }

    fn build_vf_name_table(
        newfont: &mut FontBuilder,
        font: &FontRef,
        family_name: &str,
        siblings: &[FontRef],
    ) -> Result<(), Box<dyn std::error::Error>> {
        let style_name = vf_style_name(font, family_name)?;
        let mut new_name: Name = (if fvar_instance_collisions(font, siblings) {
            build_static_name_table_v1(newfont, font, family_name, style_name)
        } else {
            build_static_name_table(newfont, font, family_name, style_name)
        })?;
        build_variations_ps_name(&mut new_name, font, Some(family_name));
        newfont.add_table(&new_name)?;
        Ok(())
    }

    fn build_variations_ps_name(newname: &mut Name, font: &FontRef, family_name: Option<&str>) {
        let fallback = best_familyname(font);
        let family_name = family_name.or(fallback.as_deref()).unwrap_or("New Font");
        let subfamily_name = best_subfamilyname(font).unwrap_or("Regular".to_string());
        let font_axes = font_axes(font).unwrap_or_default();
        let registry = AxisRegistry::new();
        let font_styles = registry.name_table_fallbacks(family_name, &subfamily_name, &font_axes);
        let mut var_ps = family_name.replace(" ", "");
        for (_, fallback) in font_styles {
            let fallback_name = fallback.name();
            if !var_ps.contains(fallback_name) {
                var_ps.push_str(fallback_name);
            }
        }
        rewrite_or_insert(&mut newname.name_record, StringId::POSTSCRIPT_NAME, var_ps);
    }

    fn build_static_name_table_v1(
        _newfont: &mut FontBuilder,
        _font: &FontRef,
        _family_name: &str,
        _style_name: String,
    ) -> Result<Name, Box<dyn std::error::Error>> {
        unimplemented!()
    }

    fn build_static_name_table(
        newfont: &mut FontBuilder,
        font: &FontRef,
        family_name: &str,
        style_name: String,
    ) -> Result<Name, Box<dyn std::error::Error>> {
        let mut name: Name = font.name()?.to_owned_table();
        let mut records = name.name_record.into_iter().collect::<Vec<NameRecord>>();
        records.retain(|record| record.platform_id != 1);
        // let existing_name = best_familyname(font).unwrap_or("New Font".to_string());
        let mut removed_names: HashMap<StringId, String> = HashMap::new();
        let (new_family_name, new_style_name, removeable_name_ids) =
            if ["Italic", "Bold Italic", "Bold", "Regular"].contains(&style_name.as_str()) {
                (
                    family_name.to_string(),
                    style_name,
                    vec![
                        StringId::TYPOGRAPHIC_FAMILY_NAME,
                        StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
                        StringId::new(21),
                        StringId::new(22),
                    ],
                )
            } else {
                let style_tokens = style_name.split_whitespace().collect::<Vec<_>>();
                let mut new_family_name_tokens = family_name.split_whitespace().collect::<Vec<_>>();
                let is_italic = style_tokens.contains(&"Italic");
                let additional_tokens = (style_tokens.into_iter().filter(|token| {
                    !(*token == "Regular"
                        || *token == "Italic"
                        || new_family_name_tokens.contains(token))
                }))
                .collect::<Vec<_>>();
                new_family_name_tokens.extend(additional_tokens);
                let new_family_name = new_family_name_tokens.join(" ");
                let new_style_name = if is_italic { "Italic" } else { "Regular" };
                rewrite_or_insert(
                    &mut records,
                    StringId::TYPOGRAPHIC_FAMILY_NAME,
                    family_name.to_string(),
                );
                rewrite_or_insert(
                    &mut records,
                    StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
                    style_name,
                );
                (
                    new_family_name,
                    new_style_name.to_string(),
                    vec![StringId::new(21), StringId::new(22)],
                )
            };
        let full_name = new_family_name.to_string() + " " + &new_style_name;
        let ps_name = (new_family_name.to_string() + "-" + &new_style_name).replace(" ", "");
        rewrite_or_insert(&mut records, StringId::FAMILY_NAME, family_name.to_string());
        rewrite_or_insert(&mut records, StringId::SUBFAMILY_NAME, new_style_name);
        rewrite_or_insert(&mut records, StringId::FULL_NAME, full_name);
        rewrite_or_insert(&mut records, StringId::POSTSCRIPT_NAME, ps_name);
        let mut to_delete = vec![];
        for name_id in removeable_name_ids.into_iter() {
            if let Some(existing) = records.iter_mut().position(|r| {
                r.name_id == name_id
                    && r.platform_id == 3
                    && r.encoding_id == 1
                    && r.language_id == 0x409
            }) {
                removed_names.insert(name_id, records[existing].string.to_string());
                to_delete.push(existing);
            }
        }
        for i in to_delete.into_iter().rev() {
            records.remove(i);
        }

        // If STAT table was using any removed names, add then back with a new ID
        if !removed_names.is_empty() && font.table_data(Tag::from_be_bytes(*b"STAT")).is_some() {
            let mut stat: Stat = font.stat()?.to_owned_table();
            for axis in stat.design_axes.iter_mut() {
                let id = axis.axis_name_id;
                if let Some(old_name) = removed_names.get(&id) {
                    axis.axis_name_id = find_or_add_name(&mut records, old_name);
                }
            }
            // Also do the axis value array
            if let Some(axis_values) = stat.offset_to_axis_values.as_deref_mut() {
                for axis_value in axis_values.iter_mut() {
                    match &mut **axis_value {
                        AxisValue::Format1(ref mut axis_value) => {
                            if let Some(old_name) = removed_names.get(&axis_value.value_name_id) {
                                axis_value.value_name_id = find_or_add_name(&mut records, old_name);
                            }
                        }
                        AxisValue::Format2(ref mut axis_value) => {
                            if let Some(old_name) = removed_names.get(&axis_value.value_name_id) {
                                axis_value.value_name_id = find_or_add_name(&mut records, old_name);
                            }
                        }
                        AxisValue::Format3(ref mut axis_value) => {
                            if let Some(old_name) = removed_names.get(&axis_value.value_name_id) {
                                axis_value.value_name_id = find_or_add_name(&mut records, old_name);
                            }
                        }
                        AxisValue::Format4(_axis_value_format4) => {
                            // We don't do any magic here in Python; maybe we should...
                        }
                    }
                }
            }
            newfont.add_table(&stat)?;
        }
        name.name_record = records;
        Ok(name)
    }

    fn font_axes(font: &FontRef) -> Result<Vec<FontAxis>, ReadError> {
        let fvar = font.fvar().unwrap();
        let mut axes = vec![];
        for axis in fvar.axes()? {
            let tag = axis.axis_tag().to_string();
            let min = axis.min_value().to_f32();
            let max = axis.max_value().to_f32();
            let default = axis.default_value().to_f32();
            axes.push(FontAxis {
                tag,
                min,
                max,
                default,
            });
        }
        Ok(axes)
    }

    fn vf_style_name(font: &FontRef, family_name: &str) -> Result<String, ReadError> {
        let axisregistry = AxisRegistry::new();
        let axes: Vec<_> = font_axes(font)?;
        let fvar_dflts = axisregistry.name_particles(&axes);
        let mut relevant_particles: Vec<String> = axisregistry
            .axis_order()
            .iter()
            .flat_map(|tag| fvar_dflts.get(tag))
            .filter(|particle| !particle.elided)
            .flat_map(|particle| particle.name.clone())
            .collect::<Vec<_>>();
        let family_name_tokens = family_name.split_whitespace().collect::<HashSet<_>>();
        let subfamily_name = best_subfamilyname(&font);
        let font_styles = axisregistry
            .name_table_fallbacks(
                family_name,
                subfamily_name.as_deref().unwrap_or("Regular"),
                &axes,
            )
            .map(|(_tag, proto)| proto.name())
            .filter(|name| !family_name_tokens.contains(name))
            .map(|name| name.to_string())
            .filter(|name| !relevant_particles.contains(&name))
            .collect::<Vec<_>>();
        relevant_particles.extend(font_styles);
        let name = relevant_particles
            .join(" ")
            .replace("Regular Italic", "Italic");
        Ok(name)
    }
}

#[cfg(feature = "fontations")]
pub use fontations::*;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn opsz() {
        let ar = AxisRegistry::new();
        assert!(ar.contains_key("opsz"));
        assert_eq!(ar["opsz"].display_name.as_deref(), Some("Optical Size"));
    }
}
