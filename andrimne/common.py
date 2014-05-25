import logging
import subprocess


def run_shell_command(command, charset='utf-8'):
    output = subprocess.check_output(command, shell=True)
    logging.info('output:\n%s' % output.decode(charset).strip())
