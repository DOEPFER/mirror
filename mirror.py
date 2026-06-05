from pathlib import Path
from typing import List

from actions.delete import delete
from actions.send import send
from actions.update import update
from cli import args
from log import setup_logging
from utils.content import contents
from utils.ignore import ignore_dir
from utils.validate import validate_source_mirror


def sync_mirror(source_path: Path, mirror_path: Path, ignore: List[str]) -> None:

    if not validate_source_mirror(source_path=source_path, mirror_path=mirror_path):
        return

    content_source = contents(source_path)
    content_mirror = contents(mirror_path)

    if ignore:
        content_source = ignore_dir(content_source, ignore)

    # UPDATE
    to_update = dict()
    to_update["is_dir"] = list(
        set(content_source["is_dir"]) & set(content_mirror["is_dir"])
    )
    to_update["is_dir"] = sorted(to_update["is_dir"])  # type: ignore
    to_update["is_file"] = list(
        set(content_source["is_file"]) & set(content_mirror["is_file"])
    )
    update(source_path=source_path, mirror_path=mirror_path, contents=to_update)

    # SEND
    to_send = dict()
    to_send["is_dir"] = list(
        set(content_source["is_dir"]) - set(content_mirror["is_dir"])
    )
    to_send["is_dir"] = sorted(to_send["is_dir"])  # type: ignore
    to_send["is_file"] = list(
        set(content_source["is_file"]) - set(content_mirror["is_file"])
    )
    send(source_path=source_path, mirror_path=mirror_path, contents=to_send)

    # DELETE
    to_delete = dict()
    to_delete["is_dir"] = list(
        set(content_mirror["is_dir"]) - set(content_source["is_dir"])
    )
    to_delete["is_dir"] = sorted(to_delete["is_dir"], reverse=True)  # type: ignore
    to_delete["is_file"] = list(
        set(content_mirror["is_file"]) - set(content_source["is_file"])
    )
    delete(mirror_path=mirror_path, contents=to_delete)


logger = setup_logging(logprefix=args.logprefix, verbose=args.verbose)

if args.source and args.mirror:
    source_path = Path(args.source)
    mirror_path = Path(args.mirror)

    sync_mirror(source_path=source_path, mirror_path=mirror_path, ignore=args.ignore)
