import sys
import pathlib
import os

from configparser import ConfigParser

CONFIG_PATH = pathlib.Path(__file__).parent.parent.parent / "setup.cfg"


def load_cfg() -> ConfigParser:
    """
    loads library config file
    :return: loaded `ConfigParser` object
    """
    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config

"""
changes name of module in file path file path directory and all relevant config settings
"""


def edit_cfg(new_name: str) -> str:
    """
    edits setup.cfg with new name of library in necessary fields

    :param new_name: new name for the library
    """

    config = load_cfg()
    old_name = config.get("metadata", "name")

    config.set("metadata", "name", new_name)
    config.set("coverage:run", "source", new_name)
    config.set("coverage:html", "title", f"coverage report for {new_name}")

    with open(CONFIG_PATH, mode="w") as f:
        config.write(f)

    return old_name


def rename_dirs(old_name, target_name: str):
    """
    renames top level directory, module package, and changes active directory to it
    :param old_name: old name of lib
    :param target_name: new name of lib
    :return:
    """

    # rename module folder name
    pathlib.Path(f"./{old_name}").rename(target_name)

    # change active directory
    os.chdir("..")

    # rename top level directory
    try:
        pathlib.Path(f"./{old_name}-py").rename(f"{target_name}-py")
    except OSError as error:
        raise error
    else:
        os.chdir(f"./{target_name}-py")


def main():
    """
    renames lib and writes 1 or 0 to stdout for whether .egg needs to be
    rewritten
    """
    do_install = "1"

    try:
        target_name = sys.argv[1]
    except IndexError:
        raise ValueError("new name must be passed with name=[name] param")

    if pathlib.Path(f"../{target_name}-py").exists():
        raise FileExistsError(f"target lib folder exists {target_name}-py")

    # edit the config file and get current name
    old_name = edit_cfg(target_name)

    # remove .egg info
    try:
        os.remove(f"{old_name}.egg-info")
    except (FileExistsError, OSError):
        do_install = "0"

    # rename directory
    rename_dirs(old_name, target_name)

    # write result
    sys.stdout.write(do_install)


if __name__ == "__main__":
    main()
