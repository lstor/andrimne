from pkg_resources import resource_stream
import yaml

MAIN_CONFIG_FILE = ['andrimne', 'config/andrimne.yaml']


def read_main_configuration():
    return yaml.load(resource_stream(*MAIN_CONFIG_FILE))


def config_or_default(config, value, default):
    try:
        return config[value]
    except KeyError:
        return default
