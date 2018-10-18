from zdevelop.make_scripts.common import load_cfg

config = load_cfg()
__version__: str = config.get("bumpversion", "current_version")
