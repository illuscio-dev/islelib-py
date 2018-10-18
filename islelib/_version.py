from configparser import ConfigParser

CONFIG_PATH = "../setup.cfg"
config = ConfigParser()
config.read(CONFIG_PATH)

__version__: str = config.get("bumpversion", "current_version")
print(__version__)
