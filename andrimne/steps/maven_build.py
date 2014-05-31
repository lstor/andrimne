from andrimne.config import config_or_default
from andrimne.common import run_shell_command
import logging


def run(cfg):
    logging.info('running maven build')

    flags = config_or_default(cfg, 'maven_flags', '')
    run_shell_command('mvn {} clean install'.format(flags), charset='latin-1')
