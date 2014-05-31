from andrimne.common import run_shell_command
from andrimne.config import config_or_default
import logging


def run(cfg):
    logging.info('setting permissions')

    version = cfg['version']
    prefix = cfg['module_prefix']
    modules = config_or_default(cfg, 'code_modules', [])

    for module in modules:
        filename = '%s%s/target/%s%s-%s.war' % (prefix, module, prefix, module, version)
        run_shell_command('chmod a+rw %s' % filename)
