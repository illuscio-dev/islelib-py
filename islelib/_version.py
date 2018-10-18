import pathlib
from configparser import ConfigParser

CONFIG_PATH = pathlib.Path(__file__).parent.parent / "setup.cfg"
config = ConfigParser()
config.read(CONFIG_PATH)

__version__: str = config.get("bumpversion", "current_version")
