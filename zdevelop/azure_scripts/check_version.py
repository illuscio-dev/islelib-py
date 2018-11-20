import pathlib
import shlex
import subprocess
import re
import sys

from configparser import ConfigParser
from typing import List


CONFIG_PATH = pathlib.Path(__file__).parent.parent.parent / "setup.cfg"


def load_cfg() -> ConfigParser:
    """
    loads library config file
    :return: loaded `ConfigParser` object
    """
    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config


if __name__ == "__main__":

    config: ConfigParser = load_cfg()
    version: str = config.get("bumpversion", "current_version")
    name: str = config.get("metadata", "name")

    pip_command = f"pip install {name}=="
    pip_command = shlex.split(pip_command)

    pip_response: str = str(
        subprocess.Popen(
            pip_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ).communicate()[1]
    )

    versions_pattern = re.compile(r"\(from versions: (.+)\)")  # noqa: W605

    existing_versions: str = re.findall(versions_pattern, pip_response)[0]
    existing_versions: List[str] = existing_versions.split(", ")

    try:
        assert version not in existing_versions
    except AssertionError:
        error_message = (
            f'version {version} of package "{name}" exists in azure artifacts. '
            f"please version up before release\n"
        )
        print(error_message)
        sys.stderr.write(error_message)
