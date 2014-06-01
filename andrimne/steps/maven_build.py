from andrimne.common import run_shell_command
import andrimne.config as config
import logging


def run():
    logging.info('running maven build')

    flags = config.read_or_default('maven_flags', '')
    run_shell_command('mvn {} clean install'.format(flags), charset='latin-1')
