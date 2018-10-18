import pathlib
from configparser import ConfigParser

CONFIG_PATH: pathlib.Path = pathlib.Path(__file__).parent.parent / "setup.cfg"
CONFIG_PATH: str = str(CONFIG_PATH.absolute())

raise ValueError(CONFIG_PATH)

config = ConfigParser()
config.read(CONFIG_PATH)

__version__: str = config.get("bumpversion", "current_version")
print(__version__)
