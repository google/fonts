from absl import app
from absl import flags
import itertools
import mistune  # markdown => ast
from xml.dom import minidom
from pathlib import Path
import re
import sys
from typing import Callable, Iterable, List, Mapping, Set, Union


MAX_IMAGE_SIZE_KB = 750


def _topic_target_to_path(_: Set[str], target: str) -> str:
    # TODO sanity check if this is the only valid update
    return Path(target.replace("/topic/", "topics/")) / "topic.textproto"


def _topics_target_to_path(_: Set[str], target: str) -> str:
    return Path(target.replace("/topics/", "topics/")) / "topic.textproto"


def _module_target_to_path(_: Set[str], target: str) -> str:
    return Path(target.replace("/module/", "modules/")) / "module.textproto"


def _content_md(path: str) -> Path:
    return Path(path) / "content.md"


def _glossary_target_to_path(_: Set[str], target: str) -> str:
    # TODO sanity check if this is the only valid update
    return _content_md(target.replace("/glossary/", "glossary/terms/"))


def _lesson_target_to_path(names: Mapping[str, str], target: str) -> str:
    # /lesson/choosing_type/choosing_reliable_typefaces => modules/choosing_type/lessons/choosing_reliable_typefaces/
    parts = target[1:].split("/")
    assert parts[0] == "lesson"
    if len(parts) == 2:
        path = names.get(parts[1], "")
        if not path.startswith("modules/"):
            return _content_md(target)
        return _content_md(path)
    elif len(parts) == 3:
        return _content_md(f"modules/{parts[1]}/lessons/{parts[2]}")
    else:
        return _content_md(target)


def _any_unique_name_to_path(names: Mapping[str, str], target: str) -> str:
    return _content_md(names.get(target, target))


_LINK_TO_PATH = [
    (re.compile("^/glossary/"), _glossary_target_to_path),
    # TODO accept only one of /topic and /topics
    (re.compile("^/topic/"), _topic_target_to_path),
    (re.compile("^/topics/"), _topics_target_to_path),
    (re.compile("^/lesson/"), _lesson_target_to_path),
    (re.compile("^/module/"), _module_target_to_path),
    (re.compile("[^/]+"), _any_unique_name_to_path)
]


FLAGS = flags.FLAGS


flags.DEFINE_bool("print_valid", False, "Whether to print valid links")


MdValue = Union[Mapping[str, "MdValue"]]


def _markdown_ast(md_file: Path) -> List[MdValue]:
    return mistune.create_markdown(renderer=mistune.AstRenderer())(md_file.read_text())


def _ast_iter(root: List[MdValue], filter_fn: Callable[[MdValue], bool]) -> Iterable[MdValue]:
    frontier = list(root)
    while frontier:
        current = frontier.pop(0)
        assert isinstance(current, dict), f"What is {current}"
        if filter_fn(current):
            yield current

        for entry in current.values():
            if isinstance(entry, list):
                frontier.extend(entry)


def _link_target_to_path(names: Mapping[str, str], target: str) -> Path:
    for matcher, link_to_path_fn in _LINK_TO_PATH:
        if matcher.search(target):
            return link_to_path_fn(names, target)
    raise ValueError(f"Unrecognized target {target}")


def main(_):
    return_code = 0

    knowledge_dir = Path(__file__).parent.parent.parent / "cc-by-sa" / "knowledge"
    assert knowledge_dir.is_dir(), f"No dir {knowledge_dir}"

    md_files = list(knowledge_dir.glob("**/*.md"))
    unambiguous_names = {}
    for name, entries in itertools.groupby(sorted(md_files, key=lambda p: p.parent.name), key=lambda p: p.parent.name):
        entries = list(entries)
        if len(entries) != 1:
            print(name, "is ambiguous")
            continue
        unambiguous_names[name] = str(entries[0].relative_to(knowledge_dir).parent)

    for md_file in md_files:
        ast = _markdown_ast(md_file)
        for link in _ast_iter(ast, lambda v: v.get("type", None) == "link"):
            target = link.get("link", "")
            if not target:
                continue  # TODO: are empty links bad
            if re.search("^http(s)?://", target.lower()):
                continue  # we aren't in the business of validating outbound links

            target_path = knowledge_dir / _link_target_to_path(unambiguous_names, target)

            should_print = True
            result = "valid   "
            if target_path.is_file():
                should_print = FLAGS.print_valid
            else:
                result = "INVALID "
                return_code = 1

            if should_print:
                print(result, target, "=>", target_path)
                print("  in", md_file.relative_to(knowledge_dir))

    image_files = list(knowledge_dir.glob("**/images/*"))
    for image_file in image_files:
      if image_file.name == "thumbnail.svg":
        root = minidom.parseString(image_file.read_text()).documentElement
        if root.tagName != "svg":
          print("Root element must be <svg>:", image_file.relative_to(knowledge_dir))
          return_code = 1
        has_view_box = "viewBox" in root.attributes
        has_width_and_height = "width" in root.attributes and "height" in root.attributes
        if not has_view_box and not has_width_and_height:
          print("Must specify viewBox and/or width+height on <svg>:", image_file.relative_to(knowledge_dir))
          return_code = 1
      if image_file.stat().st_size > MAX_IMAGE_SIZE_KB * 1024:
        print("File exceeds max size of %s KB:" % MAX_IMAGE_SIZE_KB, image_file.relative_to(knowledge_dir))
        return_code = 1

    sys.exit(return_code)


if __name__ == "__main__":
    app.run(main)
