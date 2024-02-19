from pprint import pprint
from absl import app
from absl import flags
from gftools import knowledge_pb2
from google.protobuf import text_format
import itertools
import mistune  # markdown => ast
from xml.dom import minidom
from pathlib import Path
import re
import sys
from typing import Callable, Iterable, List, Mapping, NamedTuple, Optional, Tuple, Set, Union
import requests
from functools import lru_cache


MAX_RASTER_IMAGE_SIZE_KB = 800
MAX_VECTOR_IMAGE_SIZE_KB = 1750


def _topic_target_to_path(_: Set[str], target: str) -> str:
    # TODO sanity check if this is the only valid update
    return Path(target.replace("/topic/", "topics/")) / "topic.textproto"


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
    (re.compile("^/topic/"), _topic_target_to_path),
    (re.compile("^/lesson/"), _lesson_target_to_path),
    (re.compile("^/module/"), _module_target_to_path),
    (re.compile("[^/]+"), _any_unique_name_to_path)
]


FLAGS = flags.FLAGS


flags.DEFINE_bool("print_valid", False, "Whether to print valid links")
flags.DEFINE_bool("check_outbound_links", False, "Check outbound urls")


MdValue = Union[Mapping[str, "MdValue"]]


class KnowledgeContent(NamedTuple):
    repo_root: Path
    knowledge_dir: Path
    md_files: Tuple[Path, ...]
    textproto_files: Tuple[Path, ...]
    unambiguous_names: Mapping[str, Path]

    def module_name_to_path(self: "KnowledgeContent", name: str) -> Path:
        return self.knowledge_dir / "modules" / name.lower().replace(" ", "_") / "module.textproto"

    def lesson_target_to_path(self: "KnowledgeContent", target: str) -> Path:
        return self.knowledge_dir / _link_target_to_path(self.unambiguous_names, "/lesson/" + target)

    def term_target_to_path(self: "KnowledgeContent", target: str) -> Path:
        return self.knowledge_dir / _link_target_to_path(self.unambiguous_names, "/glossary/" + target)

    def topic_target_to_path(self: "KnowledgeContent", target: str) -> Path:
        return self.knowledge_dir / _link_target_to_path(self.unambiguous_names, "/topic/" + target)

    def link_target_to_path(self: "KnowledgeContent", target: str) -> Path:
        return self.knowledge_dir / _link_target_to_path(self.unambiguous_names, target)

    @classmethod
    def load(cls, repo_root: Path) -> "KnowledgeContent":
        knowledge_dir =  repo_root / "cc-by-sa" / "knowledge"
        assert knowledge_dir.is_dir(), f"No dir {knowledge_dir}"

        md_files = []
        textproto_files = []
        for file in knowledge_dir.rglob("*"):
            if file.suffix.lower() == ".md":
                md_files.append(file)
            elif file.suffix.lower() == ".textproto":
                textproto_files.append(file)
            else:
                pass

        unambiguous_names = {}
        for name, entries in itertools.groupby(sorted(md_files, key=lambda p: p.parent.name), key=lambda p: p.parent.name):
            entries = list(entries)
            if len(entries) != 1:
                print(name, "is ambiguous")
                continue
            unambiguous_names[name] = str(entries[0].relative_to(knowledge_dir).parent)

        return cls(repo_root, knowledge_dir, tuple(md_files), tuple(textproto_files), unambiguous_names)


def _markdown_ast(md_file: Path) -> List[MdValue]:
    return mistune.create_markdown(renderer='ast')(md_file.read_text())


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


def _link_target_to_path(names: Mapping[str, Path], target: str) -> Path:
    for matcher, link_to_path_fn in _LINK_TO_PATH:
        if matcher.search(target):
            return link_to_path_fn(names, target)
    raise ValueError(f"Unrecognized target {target}")


def _safe_relative_to(parent: Path, child: Path) -> Path:
    try:
        return child.relative_to(parent)
    except ValueError:
        return child


def _maybe_print_check(result: bool, repo_root: Path, referrer: Path, ref: str, target: Optional[Path]) -> bool:
    if FLAGS.print_valid or not result:
        message = "valid   "
        if not result:
            message = "INVALID "
        suffix = ""
        if target is not None:
            suffix = " => " + str(_safe_relative_to(repo_root, target))
        print(message, _safe_relative_to(repo_root, referrer), f"\"{ref}\"{suffix}")
    return result


def _check_file_present(repo_root: Path, referrer: Path, ref: str, target: Path) -> bool:
    return _maybe_print_check(target.is_file(), repo_root, referrer, ref, target)


def _check_contributor(repo_root: Path, referrer: Path, ref: str, contributors: Set[str]) -> bool:
    return _maybe_print_check(ref in contributors, repo_root, referrer, ref, None)


def _check_md_file_contents(repo_root: Path, md_file: Path, ast: List[MdValue]) -> bool:
    for el in _ast_iter(ast, lambda v: v.get("type", None) == "inline_html"):
        text = el.get("text", "")
        if re.search(' id="[^"]+"', text):
            print("INVALID ", _safe_relative_to(repo_root, md_file), "attr.id not allowed:", text)
            return False
    f = open(md_file,"r")
    content = "".join(f.readlines())
    if re.search('</figcaption>(?!.*</figure>)', content, re.MULTILINE | re.DOTALL):
        print("INVALID ", _safe_relative_to(repo_root, md_file), "Cannot have a <figcaption> outside of a <figure>")
        return False
    f.close()
    return True


@lru_cache()
def _check_outbound_link(url: str):
    # Following urls work correctly on a web browser but raise a 400 code when using python requests
    whitelist = frozenset([
        "https://www.jessicahische.is/talkingtype",
        "http://www.layoutgridcalculator.com/typographic-scale/",
        "https://www.figma.com/community/plugin/1088610476491668236/Material-Symbols",
        "https://www.researchgate.net/publication/274013793_Legibility_in_Industrial_AR_Text_Style_Color_Coding_and_Illuminance",
        "https://www.researchgate.net/figure/Biblia-latina-The-42-Line-Bible-Mainz-Johannes-Gutenberg-for-Johann-Fust-ca_fig3_317915502",
        "https://www.nytimes.com/2003/10/21/business/the-media-business-a-face-lift-for-the-times-typographically-that-is.html",
        "https://www.circuitousroot.com/artifice/letters/pantocut/benton/vertical/index.html",
        "https://www.circuitousroot.com/artifice/letters/press/typemaking/after-casting/mortising/rouse/inst-and-print/index.html",
        "https://www.paulshawletterdesign.com/2011/11/tutorial-no-6%E2%80%94tight-but-not-touching-kerning/",
        "https://codepen.io/mandymichael/pen/pxXNbr",
        "https://typetura.com",
        "https://gigapress.net/reduce-http-requests/",
        "https://help.figma.com/hc/en-us/articles/5579502031511-Use-variable-fonts#Replace_static_fonts",
        "https://twitter.com/romanshamin_en/status/1562801657691672576",
        "https://www.sciencedirect.com/science/article/pii/S0042698907005561",
        "https://doi.org/10.1002/rrq.411",
        "https://www.webmd.com/healthy-aging/news/20140318/color-vision-tends-to-fade-with-age-study#1",
        "https://support.google.com/accessibility/android/answer/12159181?hl=en",
        "http://www.languagegeek.com/typography/syllabics/syllabic_variation.pdf",
        "https://www.freepik.com/free-photos-vectors/travel",
        "https://psycnet.apa.org/record/2018-13691-001",
        "https://www.cortezlawfirmpllc.com/wp-content/uploads/sites/1600711/2020/05/glare_congressional_report.pdf",
        "http://kupferschrift.de/cms/2012/03/on-classifications/",
        "https://medium.engineering/typography-is-impossible-5872b0c7f891",
        "https://medium.com/microsoft-design/leading-trim-the-future-of-digital-typesetting-d082d84b202",
        "https://medium.com/eightshapes-llc/space-in-design-systems-188bcbae0d62#:~:text=Solve%20Collisions%20like%20Line%20Height%20Systematically",
        "https://nedwin.medium.com/the-1-5m-napkin-abd2702927d0",
        "https://www.colourblindawareness.org/colour-blindness/types-of-colour-blindness/",
        "https://medium.com/the-readability-group/whats-in-a-word-53bcf217d5c1",
        "https://medium.com/the-readability-group/a-guide-to-understanding-what-makes-a-typeface-accessible-and-how-to-make-informed-decisions-9e5c0b9040a0",
        "https://medium.com/@mcpflug/whats-in-a-name-the-perception-of-pro-7fffa6cddcb8",
        "https://medium.com/@tilougarou/the-typographic-scale-reworked-a1b441b2beb2",
    ])
    # Following urls will be fixed at a later date. If the CI is failing and a suitable
    # replacement url cannot be found, please add them to this set.
    to_fix = frozenset()
    if url in whitelist | to_fix:
        return True

    response = requests.head(url, allow_redirects=True)
    if not response.ok:
        print(f"INVALID url {url}' returned response status code '{response.status_code}'")
    return response.ok


def _check_md_files(knowledge: KnowledgeContent) -> bool:
    result = True
    for md_file in knowledge.md_files:
        ast = _markdown_ast(md_file)
        result = _check_md_file_contents(knowledge.repo_root, md_file, ast) and result
        for link in _ast_iter(ast, lambda v: v.get("type", None) == "link"):
            target = link["attrs"]["url"]
            # mistune cannot parse urls that end with a closing parenthesis,
            # https://github.com/lepture/mistune/issues/355
            # A possible fix is to do some regex acrobatics in:
            # https://github.com/lepture/mistune/blob/master/src/mistune/helpers.py#L12-L18,
            if "(" in target:
                target += ")"
            if not target:
                continue  # TODO: are empty links bad
            if re.search("^http(s)?://", target.lower()):
                if FLAGS.check_outbound_links:
                    result = _check_outbound_link(target) and result
            else:
                target_path = knowledge.link_target_to_path(target)
                result = _check_file_present(knowledge.repo_root, md_file, target, target_path) and result
    return result


def _check_proto_files(knowledge: KnowledgeContent) -> bool:
    # TODO support alt_ids, many Knowledge constructs have them

    # The set of valid contributors is useful in upcoming validations
    contributors_file = knowledge.knowledge_dir / "contributors.textproto"
    assert contributors_file.is_file(), contributors_file
    contributors = {c.name for c in text_format.Parse(contributors_file.read_text(), knowledge_pb2.ContributorsProto()).contributors}

    result = True
    for textproto_file in knowledge.textproto_files:
        expected_files = set()

        if textproto_file.stem == "contributors":
            pass  # handled above

        elif textproto_file.stem == "knowledge":
            proto = text_format.Parse(textproto_file.read_text(), knowledge_pb2.KnowledgeProto())
            expected_files |= {(m, knowledge.module_name_to_path(m)) for m in proto.modules}

        elif textproto_file.stem == "term":
            proto = text_format.Parse(textproto_file.read_text(), knowledge_pb2.TermProto())
            expected_files |= {(n, knowledge.lesson_target_to_path(n)) for n in proto.related_lessons}

        elif textproto_file.stem == "lesson":
            proto = text_format.Parse(textproto_file.read_text(), knowledge_pb2.LessonProto())
            for author in set(proto.authors) | set(proto.reviewers):
                result = _check_contributor(knowledge.repo_root, textproto_file, author, contributors) and result
            expected_files |= {(n, knowledge.topic_target_to_path(n)) for n in proto.topics}
            expected_files |= {(n, knowledge.lesson_target_to_path(n)) for n in proto.prev_lessons}
            expected_files |= {(n, knowledge.lesson_target_to_path(n)) for n in proto.next_lessons}
            expected_files |= {(n, knowledge.term_target_to_path(n)) for n in proto.related_terms}

            # thumbnail is mandatory
            expected_files.add(("thumbnail", textproto_file.parent / "images" / "thumbnail.svg"))


        elif textproto_file.stem == "module":
            proto = text_format.Parse(textproto_file.read_text(), knowledge_pb2.ModuleProto())
            expected_files |= {(n, knowledge.lesson_target_to_path(n)) for n in proto.lessons}

        elif textproto_file.stem == "topic":
            # The Topic parses. And that's enough.
            text_format.Parse(textproto_file.read_text(), knowledge_pb2.TopicProto())

        else:
            raise ValueError("No handler for " + textproto_file.relative_to(knowledge.repo_root))

        for ref, expected_file in expected_files:
            result = _check_file_present(knowledge.repo_root, textproto_file, ref, expected_file) and result


    return result


def _is_svg(image_file: Path) -> bool:
  return image_file.suffix == ".svg"


def _is_svg(image_file: Path) -> bool:
  return image_file.suffix == ".svg"


def _check_image_files(knowledge: KnowledgeContent) -> bool:
    result = True
    image_files = list(knowledge.knowledge_dir.glob("**/images/*"))
    for image_file in image_files:
        st_size = image_file.stat().st_size
        if _is_svg(image_file):
            if st_size > MAX_VECTOR_IMAGE_SIZE_KB * 1024:
                print("File exceeds max size of %s KB (%s KB):" % (MAX_VECTOR_IMAGE_SIZE_KB, st_size // 1024), image_file.relative_to(knowledge.knowledge_dir))
                result = False
            root = minidom.parseString(image_file.read_text()).documentElement
            if root.tagName != "svg":
                print("Root element must be <svg>:", image_file.relative_to(knowledge.repo_root))
                result = False
            has_view_box = "viewBox" in root.attributes
            has_width_and_height = "width" in root.attributes and "height" in root.attributes
            if not has_view_box and not has_width_and_height:
                print("Must specify viewBox and/or width+height on <svg>:", image_file.relative_to(knowledge.knowledge_dir))
                result = False
            for stopEl in root.getElementsByTagName("stop"):
                if "offset" not in stopEl.attributes:
                    print("Must specify offset on <stop>:", image_file.relative_to(knowledge.knowledge_dir))
                    result = False
        else:
            if st_size > MAX_RASTER_IMAGE_SIZE_KB * 1024:
                print("File exceeds max size of %s KB (%s KB):" % (MAX_RASTER_IMAGE_SIZE_KB, st_size // 1024), image_file.relative_to(knowledge.knowledge_dir))
                result = False
    return result


def main(_):
    knowledge = KnowledgeContent.load(Path(__file__).parent.parent.parent)

    return_code = 1
    if (_check_md_files(knowledge)
        and _check_proto_files(knowledge)
        and _check_image_files(knowledge)):
        return_code = 0

    sys.exit(return_code)


if __name__ == "__main__":
    app.run(main)
