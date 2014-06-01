from pkg_resources import resource_stream
import yaml

_MAIN_CONFIG_FILE = ['andrimne', 'configuration/andrimne.yaml']

_config = {}


def read_main_configuration():
    global _config
    _config = yaml.load(resource_stream(*_MAIN_CONFIG_FILE))


def read(key):
    return _config[key]


def store(key, value):
    _config[key] = value


def read_or_default(key, default=None):
    try:
        return _config[key]
    except KeyError:
        return default
