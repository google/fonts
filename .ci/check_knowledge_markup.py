import re
import sys
from pathlib import Path

MARKDOWN_LINK = re.compile(r'(?<!!)\[[^\]]+\]\([^)]+\)')
MARKDOWN_BOLD = re.compile(r'\*\*[^*\n]+\*\*')
MARKDOWN_ITALIC = re.compile(r'(?<!\*)\*(?!\*)[^*\n]+\*(?!\*)')
MARKDOWN_CODE = re.compile(r'`[^`\n]+`')
MARKDOWN_HEADING = re.compile(r'(?m)^#{1,6}\s')

ALL_PATTERNS = [
    (MARKDOWN_LINK,    "markdown link [text](url)"),
    (MARKDOWN_BOLD,    "markdown bold **text**"),
    (MARKDOWN_ITALIC,  "markdown italic *text*"),
    (MARKDOWN_CODE,    "markdown code `backtick`"),
    (MARKDOWN_HEADING, "markdown heading #"),
]

INLINE_TAG_RE = re.compile(
    r'<(figcaption|p|li|dt|dd|td|th)[^>]*>[^\n]+</\1>',
    re.IGNORECASE,
)

ADJACENT_BLOCK_RE = re.compile(
    r'<(figure|aside|div|section|blockquote)[^>]*>\n([^\n].*?)\n</\1>',
    re.DOTALL | re.IGNORECASE,
)


def check_inline_tags(content, md_file, errors):
    """Catch markdown inside single-line HTML tags like <figcaption>...</figcaption>."""
    for match in INLINE_TAG_RE.finditer(content):
        line = match.group(0)
        line_num = content[:match.start()].count('\n') + 1
        for pattern, description in ALL_PATTERNS:
            if pattern.search(line):
                errors.append(
                    f"{md_file}:{line_num}: {description} inside inline HTML tag:\n"
                    f"  {line[:200]!r}"
                )
                break


def check_adjacent_blocks(content, md_file, errors):
    """Catch markdown on lines immediately adjacent to block HTML tags (no blank line)."""
    for block_match in ADJACENT_BLOCK_RE.finditer(content):
        inner = block_match.group(2)
        if not inner.strip():
            continue
        inner_no_images = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', inner)
        line_num = content[:block_match.start()].count('\n') + 1
        for pattern, description in ALL_PATTERNS:
            if pattern.search(inner_no_images):
                errors.append(
                    f"{md_file}:{line_num}: {description} adjacent to HTML block tag "
                    f"(no blank line separator):\n"
                    f"  {block_match.group(0)[:200].strip()!r}"
                )
                break


def main():
    knowledge_root = Path("cc-by-sa/knowledge")
    files = sorted(knowledge_root.rglob("*.md"))

    if not files:
        print("No .md files found under cc-by-sa/knowledge/")
        sys.exit(1)

    errors = []
    for md_file in files:
        content = md_file.read_text(encoding="utf-8")
        check_inline_tags(content, md_file, errors)
        check_adjacent_blocks(content, md_file, errors)

    if errors:
        print(f"❌ Found {len(errors)} markdown-in-HTML error(s):\n")
        for e in errors:
            print(f"  {e}\n")
        sys.exit(1)

    print(f"✅ Checked {len(files)} files — no markdown markup inside HTML blocks.")


if __name__ == "__main__":
    main()