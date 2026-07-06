import logging
import shutil
from pathlib import Path

from utils.hash import generate_hash

logger = logging.getLogger(__name__)


def update(source_path: Path, mirror_path: Path, contents: dict[str, set]) -> None:
    """
    Update modified directories and files in the mirror directory from the source.

    This function compares the modification times of the source and mirror items,
    and updates the mirror if there are differences.

    Args:
        source_path (Path): The path of the source directory.
        mirror_path (Path): The path of the mirror directory.
        contents (dict[str, set]): A dictionary containing collections of relative paths
            for directories ('is_dir') and files ('is_file') to be updated.
    """

    # is_dir
    for content in contents["is_dir"]:
        source = source_path / content
        mirror = mirror_path / content

        try:
            if source.stat().st_mtime_ns != mirror.stat().st_mtime_ns:
                try:
                    logger.info(msg=f"> {mirror} | DIRECTORY")
                    shutil.copystat(source, mirror)
                except Exception as e:
                    logger.error(msg=f"\tERROR | {mirror}")
                    logger.error(msg=f"\t{e}")
                    pass
        except Exception as e:
            logger.error(msg=f"\tERROR | {mirror}")
            logger.error(msg=f"\t{e}")
            pass

    # is_file
    for content in contents["is_file"]:
        source = source_path / content
        mirror = mirror_path / content
        temporary = mirror.with_suffix(mirror.suffix + ".tmp")

        try:
            if source.stat().st_mtime_ns != mirror.stat().st_mtime_ns:
                try:
                    logger.info(msg=f"> {mirror} | FILE")
                    source.copy(temporary, preserve_metadata=True)
                    if generate_hash(source) == generate_hash(file=temporary):
                        temporary.replace(mirror)
                except Exception as e:
                    logger.error(msg=f"\tERROR | {mirror}")
                    logger.error(msg=f"\t{e}")
                    pass

        except Exception as e:
            logger.error(msg=f"\tERROR | {mirror}")
            logger.error(msg=f"\t{e}")
            pass
