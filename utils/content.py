from pathlib import Path


def contents(path: Path) -> dict[str, list]:
    is_dir = []
    is_file = []

    for content in list(path.glob(pattern="**/*")):
        path_relative_as_posix = content.relative_to(path).as_posix()

        if content.is_dir():
            is_dir.append(path_relative_as_posix)
        else:
            is_file.append(path_relative_as_posix)

    return {"is_dir": is_dir, "is_file": is_file}
