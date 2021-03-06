import logging
import subprocess


def run_shell_command(command, charset='utf-8'):
    output = subprocess.check_output(command, shell=True)

    # Swallow *all* errors from logging. We really don't want to interrupt flow just because logging fails.
    # noinspection PyBroadException
    try:
        logging.info('output:\n{}'.format(output.decode(charset).strip()))
    except:
        logging.warning('error in logging, output from \'{}\' is missing.'.format(command))
