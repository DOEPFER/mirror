import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def delete(mirror_path: Path, contents: dict[str, set]) -> None:

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
