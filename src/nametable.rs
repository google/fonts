/// Utility functions for name table handling.
use std::collections::HashSet;

use fontations::skrifa::{string::StringId, FontRef, MetadataProvider};
use fontations::write::tables::name::NameRecord;

pub(crate) fn get_best_name(font: &FontRef, ids: &[StringId]) -> Option<String> {
    for id in ids {
        if let Some(name) = font.localized_strings(*id).english_or_first() {
            return Some(name.chars().collect());
        }
    }
    None
}

pub(crate) fn best_familyname(font: &FontRef) -> Option<String> {
    get_best_name(
        font,
        &[
            StringId::WWS_FAMILY_NAME,
            StringId::TYPOGRAPHIC_FAMILY_NAME,
            StringId::FAMILY_NAME,
        ],
    )
}

pub(crate) fn best_subfamilyname(font: &FontRef) -> Option<String> {
    get_best_name(
        font,
        &[
            StringId::WWS_SUBFAMILY_NAME,
            StringId::TYPOGRAPHIC_SUBFAMILY_NAME,
            StringId::SUBFAMILY_NAME,
        ],
    )
}

pub(crate) fn rewrite_or_insert(records: &mut Vec<NameRecord>, name_id: StringId, string: &str) {
    if let Some(existing) = records.iter_mut().find(|r| {
        r.name_id == name_id && r.platform_id == 3 && r.encoding_id == 1 && r.language_id == 0x409
    }) {
        *existing.string = string.to_string();
    } else {
        records.push(NameRecord {
            platform_id: 3,
            encoding_id: 1,
            language_id: 0x409,
            name_id,
            string: string.to_string().into(),
        });
    }
}

pub(crate) fn find_or_add_name(records: &mut Vec<NameRecord>, string: &str) -> StringId {
    if let Some(existing) = records.iter().find(|r| {
        r.string.to_string() == string
            && r.platform_id == 3
            && r.encoding_id == 1
            && r.language_id == 0x409
    }) {
        return existing.name_id;
    }
    add_name(records, string)
}

pub(crate) fn add_name(records: &mut Vec<NameRecord>, string: &str) -> StringId {
    let existing_ids: HashSet<u16> = records.iter().map(|r| r.name_id.to_u16()).collect();
    let mut id: u16 = 256;
    while existing_ids.contains(&id) {
        id += 1;
    }
    let name_id = StringId::new(id);
    records.push(NameRecord {
        platform_id: 3,
        encoding_id: 1,
        language_id: 0x409,
        name_id,
        string: string.to_string().into(),
    });
    name_id
}
