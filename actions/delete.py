import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def delete(mirror_path: Path, contents: dict[str, set]) -> None:
    """
    Delete directories and files from the mirror directory that are not in the source.

    Args:
        mirror_path (Path): The path of the mirror directory.
        contents (dict[str, set]): A dictionary containing collections of relative paths
            for directories ('is_dir') and files ('is_file') to be deleted.
    """

    # is_file
    for content in contents["is_file"]:
        mirror = mirror_path / content

        try:
            logger.info(msg=f"- {mirror} | FILE")
            mirror.unlink(missing_ok=True)
        except Exception as e:
            logger.error(msg=f"\tERROR | {mirror}")
            logger.error(msg=f"\t{e}")
            pass

    # is_dir
    for content in contents["is_dir"]:
        mirror = mirror_path / content

        try:
            logger.info(msg=f"- {mirror} | DIRECTORY")
            mirror.rmdir()
        except Exception as e:
            logger.error(msg=f"\tERROR | {mirror}")
            logger.error(msg=f"\t{e}")
            pass
