use std::{collections::HashSet, ops::Index};

#[cfg(feature = "fontations")]
use fontations::skrifa::string::StringId;
#[cfg(feature = "fontations")]
use fontations::{
    read::FontRef,
    read::{ReadError, TableProvider},
    write::FontBuilder,
};
use indexmap::IndexMap;

include!(concat!(env!("OUT_DIR"), "/_.rs"));
include!(concat!(env!("OUT_DIR"), "/data.rs"));

const LINKED_VALUES: [(&str, (f32, f32)); 2] = [("wght", (400.0, 700.0)), ("ital", (0.0, 1.0))];

fn linked_value(axis: &str, value: f32) -> Option<f32> {
    LINKED_VALUES
        .iter()
        .find(|(linked_axis, (cur, _link))| *linked_axis == axis && value == *cur)
        .map(|(_, (_, link))| *link)
}

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

#[cfg(feature = "fontations")]
const PROTECTED_IDS: [StringId; 9] = [
    StringId::FAMILY_NAME,
    StringId::SUBFAMILY_NAME,
    StringId::UNIQUE_ID,
    StringId::FULL_NAME,
    StringId::VERSION_STRING,
    StringId::POSTSCRIPT_NAME,
    StringId::TYPOGRAPHIC_FAMILY_NAME,
    StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
    StringId::VARIATIONS_POSTSCRIPT_NAME_PREFIX,
];

pub struct AxisRegistry {
    axes: BTreeMap<String, Box<AxisProto>>,
}

#[derive(Debug, Clone)]
pub struct FontAxis {
    pub tag: String,
    pub min: f32,
    pub max: f32,
    pub default: f32,
}

#[derive(Debug, Clone)]
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
                        .filter(|f| f.value() >= axis.min && f.value() <= axis.max)
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
            .filter(move |(tag, _)| !axis_names.contains(tag))
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
        let mut axis_tags: Vec<&str> = self
            .axes
            .keys()
            .filter(|k| k.chars().all(|c| c.is_ascii_uppercase()))
            .map(|k| k.as_str())
            .collect();
        axis_tags.sort();
        axis_tags.extend(vec!["opsz", "wdth", "wght", "ital", "slnt"]);
        axis_tags
    }

    // This is the old "_fvar_dflts"
    pub fn name_particles<'a>(&self, font_axes: &'a [FontAxis]) -> IndexMap<&'a str, NameParticle> {
        let mut particles = IndexMap::new();
        for axis in font_axes {
            if axis.tag == "opsz" {
                particles.insert(
                    "opsz",
                    NameParticle {
                        name: Some(format!("{}pt", axis.default)),
                        value: axis.default,
                        elided: true,
                    },
                );
            } else if let Some(fallback) = self.fallback_for_value(&axis.tag, axis.default) {
                particles.insert(
                    &axis.tag,
                    NameParticle {
                        name: fallback.name.clone(),
                        value: axis.default,
                        elided: (fallback.value() == self.get(&axis.tag).unwrap().default_value())
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
mod monkeypatching;
#[cfg(feature = "fontations")]
mod nametable;
#[cfg(feature = "fontations")]
mod stat;
#[cfg(feature = "fontations")]
mod fontations_impl {
    use super::*;
    use fontations::{
        skrifa::{string::StringId, MetadataProvider, Tag},
        write::{
            from_obj::ToOwnedTable,
            tables::{
                fvar::{Fvar, InstanceRecord},
                name::{Name, NameRecord},
                os2::Os2,
                stat::Stat,
            },
            types::Fixed,
        },
    };
    use monkeypatching::{AxisValueNameId, SetAxisValueNameId};
    use nametable::{
        add_name, best_familyname, best_subfamilyname, find_or_add_name, rewrite_or_insert,
    };
    use stat::{AxisLocation, AxisRecord, AxisValue, StatBuilder};
    use std::{cmp::Reverse, collections::HashMap};

    #[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
    pub enum RenameAggressiveness {
        #[default]
        Aggressive,
        Conservative,
    }

    pub fn build_name_table(
        font: FontRef,
        family_name: Option<&str>,
        style_name: Option<&str>,
        siblings: &[FontRef],
        aggressive: Option<RenameAggressiveness>,
    ) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
        let mut new_font = FontBuilder::new();
        let family_name = family_name
            .map(|x| x.to_string())
            .unwrap_or_else(|| best_familyname(&font).unwrap_or("Unknown".to_string()));
        let style_name = style_name
            .map(|x| x.to_string())
            .unwrap_or_else(|| best_subfamilyname(&font).unwrap_or("Regular".to_string()));

        let mut new_name = if font.table_data(Tag::new(b"fvar")).is_some() {
            build_vf_name_table(&mut new_font, &font, &family_name, siblings, aggressive)?
        } else {
            build_static_name_table_v1(&mut new_font, &font, &family_name, &style_name, aggressive)?
        };

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
        new_name.name_record.sort();
        new_font.add_table(&new_name)?;
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
        is_italic.len() != is_italic.iter().collect::<HashSet<_>>().len()
    }

    fn build_vf_name_table(
        newfont: &mut FontBuilder,
        font: &FontRef,
        family_name: &str,
        siblings: &[FontRef],
        aggressive: Option<RenameAggressiveness>,
    ) -> Result<Name, Box<dyn std::error::Error>> {
        let style_name = vf_style_name(font, family_name)?;
        let mut new_name: Name = (if fvar_instance_collisions(font, siblings) {
            build_static_name_table_v1(newfont, font, family_name, &style_name, aggressive)
        } else {
            build_static_name_table(newfont, font, family_name, style_name, aggressive)
        })?;
        // println!("Records: {:#?}", new_name.name_record);
        build_variations_ps_name(&mut new_name, font, Some(family_name));

        // Ensure table records are sorted
        new_name.name_record.sort();
        Ok(new_name)
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
        rewrite_or_insert(
            &mut newname.name_record,
            StringId::VARIATIONS_POSTSCRIPT_NAME_PREFIX,
            &var_ps,
        );
    }

    fn build_static_name_table_v1(
        newfont: &mut FontBuilder,
        font: &FontRef,
        family_name: &str,
        style_name: &str,
        aggressive: Option<RenameAggressiveness>,
    ) -> Result<Name, Box<dyn std::error::Error>> {
        let (v1_tokens, non_weight) = style_name
            .split_whitespace()
            .partition::<Vec<_>, _>(|token| GF_STATIC_STYLES.iter().any(|(name, _)| name == token));
        let family_tokens = family_name.split_whitespace();
        let mut new_family_name = vec![];
        for token in family_tokens {
            if non_weight.contains(&token) || new_family_name.contains(&token) {
                continue;
            }
            new_family_name.push(token);
        }
        new_family_name.extend(non_weight);
        let family_name = new_family_name.join(" ");
        let mut style_name = v1_tokens
            .join(" ")
            .replace("Regular Italic", "Italic")
            .trim()
            .to_string();
        if style_name.is_empty() {
            style_name = "Regular".to_string();
        }
        build_static_name_table(newfont, font, &family_name, style_name, aggressive)
    }

    fn build_static_name_table(
        newfont: &mut FontBuilder,
        font: &FontRef,
        family_name: &str,
        style_name: String,
        aggressive: Option<RenameAggressiveness>,
    ) -> Result<Name, Box<dyn std::error::Error>> {
        let mut name: Name = font.name()?.to_owned_table();
        let mut records = name.name_record.into_iter().collect::<Vec<NameRecord>>();
        records.retain(|record| record.platform_id != 1);
        let existing_name = best_familyname(font).unwrap_or("New Font".to_string());
        let mut removed_names: HashMap<StringId, String> = HashMap::new();
        let full_name = family_name.to_string() + " " + &style_name;
        let ps_name = (family_name.to_string() + "-" + &style_name).replace(" ", "");
        let removeable_name_ids =
            if ["Italic", "Bold Italic", "Bold", "Regular"].contains(&style_name.as_str()) {
                rewrite_or_insert(&mut records, StringId::FAMILY_NAME, family_name);
                rewrite_or_insert(&mut records, StringId::SUBFAMILY_NAME, &style_name);
                rewrite_or_insert(&mut records, StringId::FULL_NAME, &full_name);
                rewrite_or_insert(&mut records, StringId::POSTSCRIPT_NAME, &ps_name);
                vec![
                    StringId::TYPOGRAPHIC_FAMILY_NAME,
                    StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
                    StringId::new(21),
                    StringId::new(22),
                ]
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

                rewrite_or_insert(&mut records, StringId::FAMILY_NAME, &new_family_name);
                rewrite_or_insert(&mut records, StringId::SUBFAMILY_NAME, new_style_name);
                rewrite_or_insert(&mut records, StringId::FULL_NAME, &full_name);
                rewrite_or_insert(&mut records, StringId::POSTSCRIPT_NAME, &ps_name);
                rewrite_or_insert(&mut records, StringId::TYPOGRAPHIC_FAMILY_NAME, family_name);
                rewrite_or_insert(
                    &mut records,
                    StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
                    &style_name,
                );

                vec![StringId::new(21), StringId::new(22)]
            };

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
                    if let Some(name_id) = axis_value.value_name_id() {
                        if let Some(old_name) = removed_names.get(&name_id) {
                            axis_value.set_value_name_id(find_or_add_name(&mut records, old_name));
                        }
                    }
                }
            }
            newfont.add_table(&stat)?;
        }

        if let Some(existing) = records.iter_mut().find(|r| {
            r.name_id == StringId::UNIQUE_ID
                && r.platform_id == 3
                && r.encoding_id == 1
                && r.language_id == 0x409
        }) {
            if let Some(new_unique) = new_unique_id(font, &full_name, &ps_name, &existing.string) {
                *existing.string = new_unique;
            }
        }
        if aggressive.unwrap_or_default() == RenameAggressiveness::Aggressive {
            for record in records.iter_mut() {
                if PROTECTED_IDS.contains(&record.name_id)
                    || !record.string.contains(&existing_name)
                {
                    continue;
                }
                if !record.string.contains(' ') {
                    *record.string = record
                        .string
                        .replace(&existing_name, family_name)
                        .replace(" ", "");
                } else {
                    *record.string = record.string.replace(&existing_name, family_name);
                }
            }
        }
        name.name_record = records;
        name.name_record.sort();
        Ok(name)
    }

    fn new_unique_id(
        font: &FontRef<'_>,
        full_name: &str,
        ps_name: &str,
        existing: &str,
    ) -> Option<String> {
        let new = existing.to_string();
        if let Some(existing_full_name) = font
            .localized_strings(StringId::FULL_NAME)
            .english_or_first()
        {
            let existing_full_name = existing_full_name.chars().collect::<String>();
            if new.contains(&existing_full_name) {
                return Some(new.replace(&existing_full_name, full_name));
            }
        }
        if let Some(existing_ps_name) = font
            .localized_strings(StringId::POSTSCRIPT_NAME)
            .english_or_first()
        {
            let existing_ps_name = existing_ps_name.chars().collect::<String>();
            if new.contains(&existing_ps_name) {
                return Some(new.replace(&existing_ps_name, ps_name));
            }
        }
        None
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
        let subfamily_name = best_subfamilyname(font);
        let font_styles = axisregistry
            .name_table_fallbacks(
                family_name,
                subfamily_name.as_deref().unwrap_or("Regular"),
                &axes,
            )
            .map(|(_tag, proto)| proto.name())
            .filter(|name| !family_name_tokens.contains(name))
            .map(|name| name.to_string())
            .filter(|name| !relevant_particles.contains(name))
            .collect::<Vec<_>>();
        relevant_particles.extend(font_styles);
        let name = relevant_particles
            .join(" ")
            .replace("Regular Italic", "Italic");
        Ok(name)
    }

    /// Return a font with an fvar table which conforms to the Google Fonts instance spec:
    /// https://github.com/googlefonts/gf-docs/tree/main/Spec#fvar-instances
    pub fn build_fvar_instances(
        font: FontRef,
        axis_dflts: Option<HashMap<String, f32>>,
    ) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
        let axis_registry = AxisRegistry::new();
        let mut new_font = FontBuilder::new();
        let mut fvar: Fvar = font.fvar().unwrap().to_owned_table();
        let mut name_table: Name = font.name().unwrap().to_owned_table();
        let family_name = best_familyname(&font).unwrap_or("New Font".to_string());
        let style_name = best_subfamilyname(&font).unwrap_or("Regular".to_string());
        // Protect name IDs which are shared with the STAT table
        let mut stat_name_ids = HashSet::new();
        if let Ok(stat) = font.stat() {
            for axis in stat.design_axes()?.iter() {
                stat_name_ids.insert(axis.axis_name_id());
            }
            if let Some(axis_values_offset) = stat.offset_to_axis_values().transpose()? {
                for axis_value in axis_values_offset.axis_values().iter().flatten() {
                    stat_name_ids.insert(axis_value.value_name_id());
                }
            }
        }

        // Remove old fvar subfamily and ps name records
        for instance in fvar.axis_instance_arrays.instances.iter() {
            if instance.subfamily_name_id != StringId::SUBFAMILY_NAME
                && instance.subfamily_name_id != StringId::TYPOGRAPHIC_SUBFAMILY_NAME
                && !stat_name_ids.contains(&instance.subfamily_name_id)
            {
                name_table
                    .name_record
                    .retain(|record| record.name_id != instance.subfamily_name_id);
            }
            if let Some(psname) = instance.post_script_name_id {
                if psname != StringId::POSTSCRIPT_NAME {
                    name_table
                        .name_record
                        .retain(|record| record.name_id != psname);
                }
            }
        }

        let axes = font_axes(&font)?;
        let fvar_defaults = axis_registry.name_particles(&axes);

        let axis_dflts = axis_dflts.unwrap_or_else(|| {
            fvar_defaults
                .iter()
                .map(|(tag, particle)| (tag.to_string(), particle.value))
                .collect()
        });

        let is_italic = style_name.contains("Italic");
        let is_roman_and_italic =
            fvar_defaults.contains_key("ital") || fvar_defaults.contains_key("slnt");

        let mut fallbacks: HashMap<String, Vec<FallbackProto>> =
            axis_registry.fallbacks(&axes).collect();
        if !fvar_defaults.contains_key("wght") {
            fallbacks.insert(
                "wght".to_string(),
                axis_registry
                    .get("wght")
                    .unwrap()
                    .fallback
                    .iter()
                    .filter(|f| f.value == Some(400.0))
                    .take(1)
                    .cloned()
                    .collect(),
            );
        }
        let wght_fallbacks = fallbacks.get("wght").ok_or("No wght fallbacks")?;
        let min_ital: Option<f32> = axes
            .iter()
            .filter(|axis| axis.tag == "ital")
            .map(|axis| axis.min)
            .next();
        let min_slnt: Option<f32> = axes
            .iter()
            .filter(|axis| axis.tag == "ital")
            .map(|axis| axis.min)
            .next();

        let mut instances = vec![];
        let do_italic = if is_roman_and_italic {
            vec![false, true]
        } else if is_italic {
            vec![true]
        } else {
            vec![false]
        };
        for italic in do_italic.into_iter() {
            for fallback in wght_fallbacks.iter() {
                let mut name = fallback.name.as_ref().unwrap().to_string();
                if italic {
                    name += " Italic";
                }
                name = name.replace("Regular Italic", "Italic");
                let mut coordinates = axis_dflts.clone();
                if fvar_defaults.contains_key("wght") {
                    coordinates.insert("wght".to_string(), fallback.value.unwrap());
                }
                if italic {
                    if let Some(min) = min_ital {
                        coordinates.insert("ital".to_string(), min);
                    } else if let Some(min) = min_slnt {
                        coordinates.insert("slnt".to_string(), min);
                    }
                }
                let subfamily_name_id = add_name(&mut name_table.name_record, &name);
                let post_script_name_id = add_name(
                    &mut name_table.name_record,
                    &format!("{}-{}", family_name, name).replace(" ", ""),
                );
                let coordinates = axes
                    .iter()
                    .map(|axis| coordinates.get(&axis.tag).cloned().unwrap_or(axis.default))
                    .map(|val| Fixed::from_f64(val as f64))
                    .collect();
                instances.push(InstanceRecord {
                    subfamily_name_id,
                    flags: 0,
                    coordinates,
                    post_script_name_id: Some(post_script_name_id),
                })
            }
        }

        fvar.axis_instance_arrays.instances = instances;

        new_font.add_table(&fvar)?;
        name_table.name_record.sort();
        new_font.add_table(&name_table)?;
        Ok(new_font.copy_missing_tables(font).build())
    }

    // All right, let's do it
    pub fn build_stat(
        font: FontRef,
        siblings: &[FontRef],
    ) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
        let mut new_font = FontBuilder::new();
        let axes = font_axes(&font)?;
        let axis_registry = AxisRegistry::new();
        let fallbacks_in_fvar: IndexMap<String, Vec<FallbackProto>> =
            axis_registry.fallbacks(&axes).collect();

        let mut fallbacks_in_siblings: Vec<(String, FallbackProto)> = vec![];
        for fnt in siblings {
            let family_name = best_familyname(fnt).unwrap_or("New Font".to_string());
            let subfamily_name = best_subfamilyname(fnt).unwrap_or("Regular".to_string());
            let font_axes = font_axes(fnt).unwrap_or_default();
            fallbacks_in_siblings.extend(
                axis_registry
                    .name_table_fallbacks(&family_name, &subfamily_name, &font_axes)
                    .map(|(tag, proto)| (tag.to_string(), proto.clone())),
            )
        }
        // And for this font
        let family_name = best_familyname(&font).unwrap_or("New Font".to_string());
        let subfamily_name = best_subfamilyname(&font).unwrap_or("Regular".to_string());
        let fallbacks_in_names =
            axis_registry.name_table_fallbacks(&family_name, &subfamily_name, &axes);

        let fvar: Fvar = font.fvar().unwrap().to_owned_table();
        let mut name: Name = font.name().unwrap().to_owned_table();
        let fvar_name_ids: HashSet<StringId> = fvar
            .axis_instance_arrays
            .instances
            .iter()
            .map(|x| x.subfamily_name_id)
            .chain(
                fvar.axis_instance_arrays
                    .axes
                    .iter()
                    .map(|x| x.axis_name_id),
            )
            .collect();
        let keep = |name_id: StringId| -> bool {
            name_id.to_u16() <= 25 || fvar_name_ids.contains(&name_id)
        };
        let mut delete_ids = vec![];
        if let Ok(stat) = font.stat() {
            for axis in stat.design_axes()?.iter() {
                let id = axis.axis_name_id.get();
                if !keep(id) {
                    delete_ids.push(id);
                }
            }
            if let Some(axis_values) = stat.offset_to_axis_values().transpose()? {
                for axis_value in axis_values.axis_values().iter().flatten() {
                    let id = axis_value.value_name_id();
                    if !keep(id) {
                        delete_ids.push(id);
                    }
                }
            }
        }
        name.name_record
            .retain(|record| !delete_ids.contains(&record.name_id));
        let mut axis_records: Vec<AxisRecord> = vec![];
        let mut values: Vec<AxisValue> = vec![];
        let mut seen_axes = HashSet::new();

        fn make_location(axis: Tag, value: f32, linked_value: Option<f32>) -> AxisLocation {
            if let Some(linked_value) = linked_value {
                AxisLocation::Three {
                    tag: axis,
                    value: Fixed::from_f64(value as f64),
                    linked: Fixed::from_f64(linked_value as f64),
                }
            } else {
                AxisLocation::One {
                    tag: axis,
                    value: Fixed::from_f64(value as f64),
                }
            }
        }

        for (axis, fallbacks) in fallbacks_in_fvar.iter() {
            let tag = Tag::new_checked(&axis.as_bytes()[0..4])?;
            let ar_axis = axis_registry.get(axis).unwrap();
            seen_axes.insert(tag);
            axis_records.push(AxisRecord {
                tag,
                name: ar_axis.display_name().to_string(),
                ordering: 0,
            });
            let fallback_values = fallbacks.iter().map(|f| f.value()).collect::<Vec<f32>>();
            for fallback in fallbacks.iter() {
                values.push(AxisValue {
                    flags: if fallback.value() == ar_axis.default_value() {
                        0x2
                    } else {
                        0x0
                    },
                    name: fallback.name().to_string(),
                    location: make_location(
                        tag,
                        fallback.value(),
                        linked_value(axis, fallback.value())
                            .filter(|value| fallback_values.contains(value)),
                    ),
                })
            }
        }

        for (axis, fallback) in fallbacks_in_names {
            let tag = Tag::new_checked(&axis.as_bytes()[0..4])?;
            if seen_axes.contains(&tag) {
                continue;
            }
            // println!("Adding {} in names", axis);
            seen_axes.insert(tag);

            let ar_axis = axis_registry.get(axis).unwrap();
            axis_records.push(AxisRecord {
                tag,
                name: ar_axis.display_name().to_string(),
                ordering: 0,
            });
            values.push(AxisValue {
                flags: 0x0,
                name: fallback.name().to_string(),
                location: make_location(
                    tag,
                    fallback.value(),
                    linked_value(axis, fallback.value()),
                ),
            });
        }

        for (axis, _fallback) in fallbacks_in_siblings {
            let tag = Tag::new_checked(&axis.as_bytes()[0..4])?;
            if seen_axes.contains(&tag) {
                continue;
            }
            seen_axes.insert(tag);

            // println!("Adding {} in siblings", axis);
            let ar_axis = axis_registry.get(&axis).unwrap();
            let elided_value = ar_axis.default_value();
            axis_records.push(AxisRecord {
                tag,
                name: ar_axis.display_name().to_string(),
                ordering: 0,
            });
            if let Some(elided_fallback) = axis_registry.fallback_for_value(&axis, elided_value) {
                values.push(AxisValue {
                    flags: 0x2,
                    name: elided_fallback.name().to_string(),
                    location: make_location(tag, elided_value, linked_value(&axis, elided_value)),
                })
            }
        }
        axis_records.iter_mut().enumerate().for_each(|(i, record)| {
            record.ordering = i as u16;
        });

        let stat_builder = StatBuilder {
            records: axis_records,
            values,
        };
        let stat = stat_builder.build(&mut name.name_record);
        name.name_record.sort();
        new_font.add_table(&name)?;
        new_font.add_table(&stat)?;
        Ok(new_font.copy_missing_tables(font).build())
    }

    pub fn build_filename(font: FontRef, extension: &str) -> String {
        let family_name = best_familyname(&font)
            .unwrap_or("New Font".to_string())
            .replace(" ", "");
        let style_name = best_subfamilyname(&font).unwrap_or("Regular".to_string());
        if font.table_data(Tag::new(b"fvar")).is_some() {
            let is_italic = style_name.contains("Italic");
            let axes = font_axes(&font).unwrap_or_default();
            // Sort uppercase axes first, then lowercase axes
            let mut axes = axes
                .iter()
                .map(|axis| axis.tag.to_string())
                .collect::<Vec<_>>();
            axes.sort();
            let axes = axes.join(",");
            return format!(
                "{}{}[{}].{}",
                family_name,
                if is_italic { "-Italic" } else { "" },
                axes,
                extension
            );
        }
        format!("{family_name}-{style_name}.{extension}").replace(" ", "")
    }
}

#[cfg(feature = "fontations")]
pub use fontations_impl::*;

#[cfg(test)]
mod tests {
    use fontations::{
        skrifa::{string::StringId, MetadataProvider, Tag},
        write::{
            from_obj::ToOwnedTable,
            tables::{
                name::Name,
                stat::{AxisValue, Stat},
            },
        },
    };
    use pretty_assertions::assert_eq;

    use super::*;

    #[test]
    fn opsz() {
        let ar = AxisRegistry::new();
        assert!(ar.contains_key("opsz"));
        assert_eq!(ar["opsz"].display_name.as_deref(), Some("Optical Size"));
    }
    const MAVEN_PRO: &[u8; 83576] = include_bytes!("../tests/data/MavenPro-Regular.ttf");
    const OPEN_SANS: &[u8; 532636] = include_bytes!("../tests/data/OpenSans[wdth,wght].ttf");
    const OPEN_SANS_ITALIC: &[u8; 584112] =
        include_bytes!("../tests/data/OpenSans-Italic[wdth,wght].ttf");
    const OPEN_SANS_CONDENSED: &[u8; 973780] =
        include_bytes!("../tests/data/OpenSansCondensed[wght].ttf");
    const OPEN_SANS_CONDENSED_ITALIC: &[u8; 1054652] =
        include_bytes!("../tests/data/OpenSansCondensed-Italic[wght].ttf");
    const WONKY: &[u8; 532564] = include_bytes!("../tests/data/Wonky[wdth,wght].ttf");
    const PLAYFAIR: &[u8; 1150824] = include_bytes!("../tests/data/Playfair[opsz,wdth,wght].ttf");

    struct NameTableTestCase {
        binary: &'static [u8],
        family_name: &'static str,
        subfamily_name: Option<&'static str>,
        siblings: Vec<&'static [u8]>,
        expectations: Vec<(StringId, Option<&'static str>)>,
    }

    #[test]
    fn test_name_table() {
        let cases: Vec<NameTableTestCase> = vec![
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("Regular"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro")),
                    (StringId::SUBFAMILY_NAME, Some("Regular")),
                    (StringId::UNIQUE_ID, Some("2.003;NONE;MavenPro-Regular")),
                    (StringId::FULL_NAME, Some("Maven Pro Regular")),
                    (StringId::POSTSCRIPT_NAME, Some("MavenPro-Regular")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                ],
            },
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("Italic"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro")),
                    (StringId::SUBFAMILY_NAME, Some("Italic")),
                    (StringId::UNIQUE_ID, Some("2.003;NONE;MavenPro-Italic")),
                    (StringId::FULL_NAME, Some("Maven Pro Italic")),
                    (StringId::POSTSCRIPT_NAME, Some("MavenPro-Italic")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                ],
            },
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("Bold"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro")),
                    (StringId::SUBFAMILY_NAME, Some("Bold")),
                    (StringId::UNIQUE_ID, Some("2.003;NONE;MavenPro-Bold")),
                    (StringId::FULL_NAME, Some("Maven Pro Bold")),
                    (StringId::POSTSCRIPT_NAME, Some("MavenPro-Bold")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                ],
            },
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("Bold Italic"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro")),
                    (StringId::SUBFAMILY_NAME, Some("Bold Italic")),
                    (StringId::UNIQUE_ID, Some("2.003;NONE;MavenPro-BoldItalic")),
                    (StringId::FULL_NAME, Some("Maven Pro Bold Italic")),
                    (StringId::POSTSCRIPT_NAME, Some("MavenPro-BoldItalic")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                ],
            },
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("Black"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro Black")),
                    (StringId::SUBFAMILY_NAME, Some("Regular")),
                    (StringId::UNIQUE_ID, Some("2.003;NONE;MavenPro-Black")),
                    (StringId::FULL_NAME, Some("Maven Pro Black")),
                    (StringId::POSTSCRIPT_NAME, Some("MavenPro-Black")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, Some("Maven Pro")),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, Some("Black")),
                ],
            },
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("Black Italic"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro Black")),
                    (StringId::SUBFAMILY_NAME, Some("Italic")),
                    (StringId::UNIQUE_ID, Some("2.003;NONE;MavenPro-BlackItalic")),
                    (StringId::FULL_NAME, Some("Maven Pro Black Italic")),
                    (StringId::POSTSCRIPT_NAME, Some("MavenPro-BlackItalic")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, Some("Maven Pro")),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, Some("Black Italic")),
                ],
            },
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("ExtraLight Italic"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro ExtraLight")),
                    (StringId::SUBFAMILY_NAME, Some("Italic")),
                    (
                        StringId::UNIQUE_ID,
                        Some("2.003;NONE;MavenPro-ExtraLightItalic"),
                    ),
                    (StringId::FULL_NAME, Some("Maven Pro ExtraLight Italic")),
                    (StringId::POSTSCRIPT_NAME, Some("MavenPro-ExtraLightItalic")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, Some("Maven Pro")),
                    (
                        StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
                        Some("ExtraLight Italic"),
                    ),
                ],
            },
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("UltraExpanded Regular"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro UltraExpanded")),
                    (StringId::SUBFAMILY_NAME, Some("Regular")),
                    (
                        StringId::UNIQUE_ID,
                        Some("2.003;NONE;MavenProUltraExpanded-Regular"),
                    ),
                    (StringId::FULL_NAME, Some("Maven Pro UltraExpanded Regular")),
                    (
                        StringId::POSTSCRIPT_NAME,
                        Some("MavenProUltraExpanded-Regular"),
                    ),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                ],
            },
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("Condensed ExtraLight Italic"),
                siblings: vec![],
                expectations: vec![
                    (
                        StringId::FAMILY_NAME,
                        Some("Maven Pro Condensed ExtraLight"),
                    ),
                    (StringId::SUBFAMILY_NAME, Some("Italic")),
                    (
                        StringId::UNIQUE_ID,
                        Some("2.003;NONE;MavenProCondensed-ExtraLightItalic"),
                    ),
                    (
                        StringId::FULL_NAME,
                        Some("Maven Pro Condensed ExtraLight Italic"),
                    ),
                    (
                        StringId::POSTSCRIPT_NAME,
                        Some("MavenProCondensed-ExtraLightItalic"),
                    ),
                    (
                        StringId::TYPOGRAPHIC_FAMILY_NAME,
                        Some("Maven Pro Condensed"),
                    ),
                    (
                        StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
                        Some("ExtraLight Italic"),
                    ),
                ],
            },
            NameTableTestCase {
                binary: OPEN_SANS,
                family_name: "Open Sans",
                subfamily_name: None,
                siblings: vec![
                    OPEN_SANS_ITALIC,
                    OPEN_SANS_CONDENSED,
                    OPEN_SANS_CONDENSED_ITALIC,
                ],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Open Sans")),
                    (StringId::SUBFAMILY_NAME, Some("Regular")),
                    (StringId::UNIQUE_ID, Some("3.000;GOOG;OpenSans-Regular")),
                    (StringId::FULL_NAME, Some("Open Sans Regular")),
                    (StringId::POSTSCRIPT_NAME, Some("OpenSans-Regular")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                    (
                        StringId::VARIATIONS_POSTSCRIPT_NAME_PREFIX,
                        Some("OpenSans"),
                    ),
                ],
            },
            NameTableTestCase {
                binary: OPEN_SANS_ITALIC,
                family_name: "Open Sans",
                subfamily_name: None,
                siblings: vec![OPEN_SANS, OPEN_SANS_CONDENSED, OPEN_SANS_CONDENSED_ITALIC],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Open Sans")),
                    (StringId::SUBFAMILY_NAME, Some("Italic")),
                    (StringId::UNIQUE_ID, Some("3.000;GOOG;OpenSans-Italic")),
                    (StringId::FULL_NAME, Some("Open Sans Italic")),
                    (StringId::POSTSCRIPT_NAME, Some("OpenSans-Italic")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                    (
                        StringId::VARIATIONS_POSTSCRIPT_NAME_PREFIX,
                        Some("OpenSansItalic"),
                    ),
                ],
            },
            NameTableTestCase {
                binary: OPEN_SANS_CONDENSED,
                family_name: "Open Sans Condensed",
                subfamily_name: None,
                siblings: vec![OPEN_SANS, OPEN_SANS_ITALIC, OPEN_SANS_CONDENSED_ITALIC],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Open Sans Condensed")),
                    (StringId::SUBFAMILY_NAME, Some("Regular")),
                    (
                        StringId::UNIQUE_ID,
                        Some("3.000;GOOG;OpenSansCondensed-Regular"),
                    ),
                    (StringId::FULL_NAME, Some("Open Sans Condensed Regular")),
                    (StringId::POSTSCRIPT_NAME, Some("OpenSansCondensed-Regular")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                    (
                        StringId::VARIATIONS_POSTSCRIPT_NAME_PREFIX,
                        Some("OpenSansCondensed"),
                    ),
                ],
            },
            NameTableTestCase {
                binary: OPEN_SANS_CONDENSED_ITALIC,
                family_name: "Open Sans Condensed",
                subfamily_name: None,
                siblings: vec![OPEN_SANS, OPEN_SANS_ITALIC, OPEN_SANS_CONDENSED],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Open Sans Condensed")),
                    (StringId::SUBFAMILY_NAME, Some("Italic")),
                    (
                        StringId::UNIQUE_ID,
                        Some("3.000;GOOG;OpenSansCondensed-Italic"),
                    ),
                    (StringId::FULL_NAME, Some("Open Sans Condensed Italic")),
                    (StringId::POSTSCRIPT_NAME, Some("OpenSansCondensed-Italic")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                    (
                        StringId::VARIATIONS_POSTSCRIPT_NAME_PREFIX,
                        Some("OpenSansCondensedItalic"),
                    ),
                ],
            },
            // Bad names
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Maven Pro",
                subfamily_name: Some("Fat"),
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Maven Pro Fat")),
                    (StringId::SUBFAMILY_NAME, Some("Regular")),
                    (StringId::UNIQUE_ID, Some("2.003;NONE;MavenProFat-Regular")),
                    (StringId::FULL_NAME, Some("Maven Pro Fat Regular")),
                    (StringId::POSTSCRIPT_NAME, Some("MavenProFat-Regular")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                ],
            },
            NameTableTestCase {
                binary: WONKY,
                family_name: "Wonky",
                subfamily_name: None,
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Wonky")),
                    (StringId::SUBFAMILY_NAME, Some("Regular")),
                    (StringId::UNIQUE_ID, Some("3.000;GOOG;Wonky-Regular")),
                    (StringId::FULL_NAME, Some("Wonky Regular")),
                    (StringId::POSTSCRIPT_NAME, Some("Wonky-Regular")),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, None),
                    (StringId::TYPOGRAPHIC_SUBFAMILY_NAME, None),
                ],
            },
            NameTableTestCase {
                binary: PLAYFAIR,
                family_name: "Playfair",
                subfamily_name: None,
                siblings: vec![],
                expectations: vec![
                    (StringId::FAMILY_NAME, Some("Playfair SemiExpanded Light")),
                    (StringId::SUBFAMILY_NAME, Some("Regular")),
                    (
                        StringId::UNIQUE_ID,
                        Some("2.000;FTH;Playfair-SemiExpandedLight"),
                    ),
                    (StringId::FULL_NAME, Some("Playfair SemiExpanded Light")),
                    (
                        StringId::POSTSCRIPT_NAME,
                        Some("Playfair-SemiExpandedLight"),
                    ),
                    (StringId::TYPOGRAPHIC_FAMILY_NAME, Some("Playfair")),
                    (
                        StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
                        Some("SemiExpanded Light"),
                    ),
                ],
            },
        ];

        run_name_table_tests(&cases, None);
    }

    fn run_name_table_tests(cases: &[NameTableTestCase], aggression: Option<RenameAggressiveness>) {
        for (ix, case) in cases.iter().enumerate() {
            let font = FontRef::new(case.binary).expect("Failed to read font");
            let siblings: Vec<FontRef> = case
                .siblings
                .iter()
                .map(|b| FontRef::new(b).unwrap())
                .collect();
            let result = build_name_table(
                font,
                Some(case.family_name),
                case.subfamily_name,
                &siblings,
                aggression,
            )
            .unwrap();
            let result_font = FontRef::new(&result).unwrap();
            for (id, expectation) in case.expectations.iter() {
                let record = result_font.localized_strings(*id).english_or_first();
                if let Some(expectation) = expectation {
                    assert_eq!(
                        record.unwrap().chars().collect::<String>(),
                        *expectation,
                        "Case {}, {}",
                        ix + 1,
                        id
                    );
                } else {
                    assert!(record.is_none());
                }
            }
        }
    }

    #[test]
    fn test_name_table_aggression() {
        let cases = [
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Raven Am",
                subfamily_name: Some("Regular"),
                siblings: vec![],
                expectations: vec![
                    (StringId::COPYRIGHT_NOTICE, Some("Copyright 2011 The Raven Am Project Authors (http://www.vissol.co.uk/mavenpro/), with Reserved Font Name \"Raven Am\".")),
                    (StringId::FULL_NAME, Some("Raven Am Regular")),
                ]
            }
        ];
        run_name_table_tests(&cases, Some(RenameAggressiveness::Aggressive));
        let cases = [
            NameTableTestCase {
                binary: MAVEN_PRO,
                family_name: "Raven Am",
                subfamily_name: Some("Regular"),
                siblings: vec![],
                expectations: vec![
                    (StringId::COPYRIGHT_NOTICE, Some("Copyright 2011 The Maven Pro Project Authors (http://www.vissol.co.uk/mavenpro/), with Reserved Font Name \"Maven Pro\".")),
                    (StringId::FULL_NAME, Some("Raven Am Regular")),
                ]
            }
        ];
        run_name_table_tests(&cases, Some(RenameAggressiveness::Conservative));
    }

    #[derive(Debug, Clone, PartialEq)]
    struct DumpStatValue<'a> {
        axis: Tag,
        name: &'a str,
        value: f32,
        linked: Option<f32>,
    }

    fn dump_stat_values<'a>(stat: &Stat, name: &'a Name) -> Vec<DumpStatValue<'a>> {
        let mut values = vec![];
        let tags = stat
            .design_axes
            .iter()
            .map(|a| a.axis_tag)
            .collect::<Vec<_>>();
        if let Some(axis_values) = stat.offset_to_axis_values.as_ref() {
            for axis_value in axis_values.iter() {
                match axis_value.as_ref() {
                    AxisValue::Format1(v) => values.push(DumpStatValue {
                        axis: tags[v.axis_index as usize],
                        name: name
                            .name_record
                            .iter()
                            .find(|record| record.name_id == v.value_name_id)
                            .map(|record| record.string.as_str())
                            .unwrap_or(""),
                        value: v.value.to_f32(),
                        linked: None,
                    }),
                    AxisValue::Format2(_) => {
                        panic!("I didn't produce this")
                    }
                    AxisValue::Format3(v) => values.push(DumpStatValue {
                        axis: tags[v.axis_index as usize],
                        name: name
                            .name_record
                            .iter()
                            .find(|record| record.name_id == v.value_name_id)
                            .map(|record| record.string.as_str())
                            .unwrap_or(""),
                        value: v.value.to_f32(),
                        linked: Some(v.linked_value.to_f32()),
                    }),
                    AxisValue::Format4(_) => {
                        panic!("I didn't produce this")
                    }
                }
            }
        }
        values
    }

    fn value<'a>(axis: &str, name: &'a str, value: f32, linked: Option<f32>) -> DumpStatValue<'a> {
        DumpStatValue {
            axis: Tag::new_checked(axis.as_bytes()).unwrap(),
            name,
            value,
            linked,
        }
    }

    #[test]
    fn test_build_stat() {
        let font_data = build_stat(
            FontRef::new(OPEN_SANS).unwrap(),
            &[
                FontRef::new(OPEN_SANS_ITALIC).unwrap(),
                FontRef::new(OPEN_SANS_CONDENSED).unwrap(),
                FontRef::new(OPEN_SANS_CONDENSED_ITALIC).unwrap(),
            ],
        )
        .unwrap();
        let new_font = FontRef::new(&font_data).unwrap();
        let new_stat: Stat = new_font.stat().unwrap().to_owned_table();
        let name: Name = new_font.name().unwrap().to_owned_table();
        // We expect three axes, wght, wdth, and ital
        assert_eq!(
            new_stat
                .design_axes
                .iter()
                .map(|a| a.axis_tag)
                .collect::<Vec<_>>(),
            vec![Tag::new(b"wght"), Tag::new(b"wdth"), Tag::new(b"ital")]
        );
        assert_eq!(
            dump_stat_values(&new_stat, &name),
            vec![
                value("wght", "Light", 300.0, None),
                value("wght", "Regular", 400.0, Some(700.0)),
                value("wght", "Medium", 500.0, None),
                value("wght", "SemiBold", 600.0, None),
                value("wght", "Bold", 700.0, None),
                value("wght", "ExtraBold", 800.0, None),
                value("wdth", "Condensed", 75.0, None),
                value("wdth", "SemiCondensed", 87.5, None),
                value("wdth", "Normal", 100.0, None),
                value("ital", "Roman", 0.0, Some(1.0)),
            ]
        )
    }

    #[test]
    fn test_build_stat2() {
        let font_data = build_stat(
            FontRef::new(OPEN_SANS_ITALIC).unwrap(),
            &[
                FontRef::new(OPEN_SANS).unwrap(),
                FontRef::new(OPEN_SANS_CONDENSED).unwrap(),
                FontRef::new(OPEN_SANS_CONDENSED_ITALIC).unwrap(),
            ],
        )
        .unwrap();
        let new_font = FontRef::new(&font_data).unwrap();
        let new_stat: Stat = new_font.stat().unwrap().to_owned_table();
        let name: Name = new_font.name().unwrap().to_owned_table();
        // We expect three axes, wght, wdth, and ital
        assert_eq!(
            new_stat
                .design_axes
                .iter()
                .map(|a| a.axis_tag)
                .collect::<Vec<_>>(),
            vec![Tag::new(b"wght"), Tag::new(b"wdth"), Tag::new(b"ital")]
        );
        assert_eq!(
            dump_stat_values(&new_stat, &name),
            vec![
                value("wght", "Light", 300.0, None),
                value("wght", "Regular", 400.0, Some(700.0)),
                value("wght", "Medium", 500.0, None),
                value("wght", "SemiBold", 600.0, None),
                value("wght", "Bold", 700.0, None),
                value("wght", "ExtraBold", 800.0, None),
                value("wdth", "Condensed", 75.0, None),
                value("wdth", "SemiCondensed", 87.5, None),
                value("wdth", "Normal", 100.0, None),
                value("ital", "Italic", 1.0, None),
            ]
        )
    }

    #[test]
    fn test_build_filename() {
        let maven_pro = FontRef::new(MAVEN_PRO).unwrap();
        assert_eq!(build_filename(maven_pro, "ttf"), "MavenPro-Regular.ttf");
        let open_sans = FontRef::new(OPEN_SANS).unwrap();
        assert_eq!(build_filename(open_sans, "ttf"), "OpenSans[wdth,wght].ttf");
        let open_sans_italic = FontRef::new(OPEN_SANS_ITALIC).unwrap();
        assert_eq!(
            build_filename(open_sans_italic, "ttf"),
            "OpenSans-Italic[wdth,wght].ttf"
        );
        let open_sans_condensed = FontRef::new(OPEN_SANS_CONDENSED).unwrap();
        assert_eq!(
            build_filename(open_sans_condensed, "ttf"),
            "OpenSansCondensed[wght].ttf"
        );
        let open_sans_condensed_italic = FontRef::new(OPEN_SANS_CONDENSED_ITALIC).unwrap();
        assert_eq!(
            build_filename(open_sans_condensed_italic, "ttf"),
            "OpenSansCondensed-Italic[wght].ttf"
        );
        let wonky = FontRef::new(WONKY).unwrap();
        assert_eq!(build_filename(wonky, "ttf"), "Wonky[wdth,wght].ttf");
        let playfair = FontRef::new(PLAYFAIR).unwrap();
        assert_eq!(
            build_filename(playfair, "ttf"),
            "Playfair[opsz,wdth,wght].ttf"
        );
    }
}
