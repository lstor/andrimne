import yaml

MAIN_CONFIG_FILE = 'config/andrimne.yaml'


def read_main_configuration():
    return yaml.load(open(MAIN_CONFIG_FILE))


def config_or_default(config, value, default):
    try:
        return config[value]
    except KeyError:
        return default
