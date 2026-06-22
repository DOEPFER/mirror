from typing import List


def ignore_dir(contents: dict[str, list], ignore: List[str]) -> dict[str, list]:
    """
    Filter out ignored directories and files from the synchronization contents.

    This function iterates through the provided contents dictionary and removes
    any directory or file paths that contain a folder specified in the ignore list.

    Args:
        contents (dict[str, list]): A dictionary containing lists of relative paths
            for directories ('is_dir') and files ('is_file').
        ignore (List[str]): A list of directory names to ignore.

    Returns:
        dict[str, list]: The modified contents dictionary with ignored paths removed.
    """

    # is_dir
    index = 0
    while index < len(contents["is_dir"]):
        values = contents["is_dir"][index].split("/")
        if any(_ignore in values for _ignore in ignore):
            contents["is_dir"].pop(index)
            index -= 1

        index += 1

    # is_file
    index = 0
    while index < len(contents["is_file"]):
        values = contents["is_file"][index].split("/")[:-1]
        if any(_ignore in values for _ignore in ignore):
            contents["is_file"].pop(index)
            index -= 1

        index += 1

    return contents
