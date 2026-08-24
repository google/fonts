import sys
import argparse
from gflanguages import LoadLanguages

def get_exemplar_set(exemplar_str):
    """
    Parses space-separated exemplar characters. 
    Multi-character clusters (e.g. {ch}) are stripped of curly braces.
    """
    if not exemplar_str:
        return set()
    return {item.strip('{}') for item in exemplar_str.split()}

def find_locales_for_char(char, languages):
    """
    Finds all locales that support a specific character either as a Base or Auxiliary exemplar.
    """
    matching_locales = {}
    for lang_id, lang_data in languages.items():
        if not hasattr(lang_data, 'exemplar_chars') or not lang_data.exemplar_chars:
            continue
            
        exemplar = lang_data.exemplar_chars
        
        is_base = False
        if hasattr(exemplar, 'base') and exemplar.base:
            base_set = get_exemplar_set(exemplar.base)
            if char in base_set:
                is_base = True
                
        is_auxiliary = False
        if hasattr(exemplar, 'auxiliary') and exemplar.auxiliary:
            aux_set = get_exemplar_set(exemplar.auxiliary)
            if char in aux_set:
                is_auxiliary = True
                
        if is_base or is_auxiliary:
            matching_locales[lang_id] = {
                "name": lang_data.name,
                "type": "Base" if is_base else "Auxiliary"
            }
    return matching_locales

def main():
    parser = argparse.ArgumentParser(
        description="Find which locales use given Unicode characters using gflanguages."
    )
    parser.add_argument(
        "chars",
        type=str,
        nargs="?",
        default="ăâî",
        help="A string of Unicode characters to search for (default: 'ăâî')"
    )
    args = parser.parse_args()
    
    search_string = args.chars
    if not search_string:
        print("Please provide a non-empty string.")
        sys.exit(1)
        
    unique_chars = list(dict.fromkeys(search_string))
    
    print(f"Loading gflanguages database...")
    try:
        languages = LoadLanguages()
    except Exception as e:
        print(f"Error loading gflanguages: {e}")
        sys.exit(1)
        
    # Store results for each character
    char_results = {}
    for char in unique_chars:
        results = find_locales_for_char(char, languages)
        char_results[char] = results
        
        print(f"\n### Locales using '{char}' (U+{ord(char):04X})")
        print(f"Total locales found: {len(results)}\n")
        print(f"| Language ID | Language Name | Character Role |")
        print(f"|:---|:---|:---|")
        for lang_id, info in sorted(results.items()):
            print(f"| {lang_id} | {info['name']} | {info['type']} |")
            
    # Compute intersection: locales that support ALL characters
    all_locales = set(languages.keys())
    for char in unique_chars:
        all_locales = all_locales.intersection(char_results[char].keys())
        
    print(f"\n### Locales using ALL characters in '{search_string}'")
    print(f"Total locales found: {len(all_locales)}\n")
    
    if all_locales:
        # Create headers dynamically for the characters
        char_headers = " | ".join([f"'{c}' (U+{ord(c):04X})" for c in unique_chars])
        separator = "|:---" * (2 + len(unique_chars)) + "|"
        
        print(f"| Language ID | Language Name | {char_headers} |")
        print(separator)
        
        for lang_id in sorted(all_locales):
            lang_name = languages[lang_id].name
            roles = []
            for char in unique_chars:
                role = char_results[char][lang_id]["type"]
                roles.append(role)
            roles_str = " | ".join(roles)
            print(f"| {lang_id} | {lang_name} | {roles_str} |")
    else:
        print("No locales support all specified characters simultaneously.")

if __name__ == '__main__':
    main()

