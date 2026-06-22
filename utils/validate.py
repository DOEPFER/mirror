import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


def validate_source_mirror(source_path: Path, mirror_path: Path) -> bool:
    """
    Validate the source and mirror paths for synchronization.

    This function checks if both paths exist and ensures there are no circular
    references (e.g., one path being a subdirectory of the other, or both being identical).

    Args:
        source_path (Path): The path of the source directory.
        mirror_path (Path): The path of the mirror directory.

    Returns:
        bool: True if the paths are valid and safe for synchronization, False otherwise.
    """
    commonpath = ""

    if source_path.anchor == mirror_path.anchor:
        commonpath = os.path.commonpath([source_path, mirror_path])

    if (
        source_path == mirror_path
        or commonpath == source_path
        or commonpath == mirror_path
    ):
        logger.error(msg="ERROR | CIRCULAR REFERENCE")
        return False

    if not source_path.exists():
        logger.error(msg=f"ERROR | SOURCE PATH NOT FOUND | {source_path}")
        return False

    if not mirror_path.exists():
        logger.error(msg=f"ERROR | MIRROR PATH NOT FOUND | {mirror_path}")
        return False

    return True
