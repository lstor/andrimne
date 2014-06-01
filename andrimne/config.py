from pkg_resources import resource_stream
import yaml

_MAIN_CONFIG_FILE = ['andrimne', 'configuration/andrimne.yaml']

_config = {}


def read_main_configuration():
    global _config
    _config = yaml.load(resource_stream(*_MAIN_CONFIG_FILE))


def read(key):
    return _config[key]


def read_or_default(key, default=None):
    try:
        return _config[key]
    except KeyError:
        return default


# STORING CONFIGURATION VALUES
#
# This allows us to write the following:
#
# config.store['key'] = value
#
# I'm not really sure if I like this approach, but I think store[key] = value is more readable than store(key, value).
# This approach may change at a later time.  -lstor

class Store:
    def __setitem__(self, key, value):
        _config[key] = value

store = Store()


