from glob import iglob
from configparser import ConfigParser


from zdevelop.make_scripts.common import load_cfg, CONFIG_PATH


if __name__ == '__main__':

    config: ConfigParser = load_cfg()
    version: str = config.get("bumpversion", "current_version")

    version_path_pattern: str = str(CONFIG_PATH.parent / '**' / '_version.py')
    version_file = next(iglob(version_path_pattern, recursive=True))

    with open(version_file, mode='w') as f:
        f.write(f'__version__ = \"{version}\"')
