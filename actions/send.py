import logging
import shutil
from pathlib import Path

from utils.hash import generate_hash

logger = logging.getLogger(__name__)


def send(source_path: Path, mirror_path: Path, contents: dict[str, set]) -> None:
    """
    Copy new directories and files from the source to the mirror directory.

    Args:
        source_path (Path): The path of the source directory.
        mirror_path (Path): The path of the mirror directory.
        contents (dict[str, set]): A dictionary containing collections of relative paths
            for directories ('is_dir') and files ('is_file') to be copied.
    """

    # is_dir
    for content in contents["is_dir"]:
        source: Path = source_path / content
        mirror: Path = mirror_path / content

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
        source: Path = source_path / content
        mirror: Path = mirror_path / content
        temporary: Path = mirror.with_suffix(mirror.suffix + ".tmp")

        try:
            logger.info(msg=f"+ {mirror} | FILE")
            source.copy(temporary, preserve_metadata=True)
            if generate_hash(file=source) == generate_hash(file=temporary):
                temporary.replace(mirror)
            else:
                temporary.unlink()
        except Exception as e:
            logger.error(msg=f"\tERROR | {mirror}")
            logger.error(msg=f"\t{e}")
            pass
