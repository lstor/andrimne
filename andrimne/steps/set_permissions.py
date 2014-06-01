from andrimne.common import run_shell_command
import andrimne.config as config
import logging


def run():
    logging.info('setting permissions')

    version = config.read('version')
    prefix = config.read('module_prefix')
    modules = config.read_or_default('code_modules', [])

    for module in modules:
        filename = u'{0}{1}/target/{0}{1}-{2}.war'.format(prefix, module, version)
        run_shell_command('chmod a+rw {}'.format(filename))
