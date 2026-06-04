from typing import List


def ignore_dir(contents: dict[str, list], ignore: List[str]) -> dict[str, list]:

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
