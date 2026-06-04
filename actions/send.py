import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def send(source_path: Path, mirror_path: Path, contents: dict[str, set]) -> None:

    # is_dir
    for content in contents["is_dir"]:
        source = source_path / content
        mirror = mirror_path / content

        try:
            logger.info(msg=f"+ {mirror} | DIRECTORY")
            mirror.mkdir(parents=True, exist_ok=True)
            shutil.copystat(source, mirror)
        except Exception as e:
            logger.error(msg=f"\tERROR | {mirror}")
            logger.error(msg=f"\t{e}")
            pass

    # is_file
    for content in contents["is_file"]:
        source = source_path / content
        mirror = mirror_path / content

        try:
            logger.info(msg=f"+ {mirror} | FILE")
            source.copy(mirror, preserve_metadata=True)
        except Exception as e:
            logger.error(msg=f"\tERROR | {mirror}")
            logger.error(msg=f"\t{e}")
            pass
