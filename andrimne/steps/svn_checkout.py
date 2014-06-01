from andrimne.common import run_shell_command
import logging


def run():
    logging.info('checking out from svn')

    run_shell_command('svn update')
