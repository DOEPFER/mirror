import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


def validate_source_mirror(source_path: Path, mirror_path: Path) -> bool:
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
