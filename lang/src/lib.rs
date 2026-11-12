include!(concat!(env!("OUT_DIR"), "/google.languages_public.rs"));
include!(concat!(env!("OUT_DIR"), "/data.rs"));

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn regions() {
        assert!((*REGIONS).contains_key("BG"));
        assert_eq!(REGIONS.get("BG").unwrap().name.as_deref(), Some("Bulgaria"));
    }

    #[test]
    fn scripts() {
        assert!((*SCRIPTS).contains_key("Arab"));
        assert_eq!(SCRIPTS.get("Arab").unwrap().name.as_deref(), Some("Arabic"));
    }

    #[test]
    fn languages() {
        assert!(LANGUAGES.len() > 1000);
        assert!((*LANGUAGES).contains_key("ar_Arab"));
    }
}
