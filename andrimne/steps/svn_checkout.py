import logging
import subprocess


def run(cfg):
    logging.info('checking out from svn')

    output = subprocess.check_output('svn update', shell=True)

    for line in output.splitlines():
        logging.info(line.decode('utf-8'))
