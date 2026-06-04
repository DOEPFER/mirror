import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def update(source_path: Path, mirror_path: Path, contents: dict[str, set]) -> None:

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

        try:
            if source.stat().st_mtime_ns != mirror.stat().st_mtime_ns:
                try:
                    logger.info(msg=f"> {mirror} | FILE")
                    source.copy(mirror, preserve_metadata=True)
                except Exception as e:
                    logger.error(msg=f"\tERROR | {mirror}")
                    logger.error(msg=f"\t{e}")
                    pass

        except Exception as e:
            logger.error(msg=f"\tERROR | {mirror}")
            logger.error(msg=f"\t{e}")
            pass
