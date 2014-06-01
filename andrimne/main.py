import andrimne.config as config
import andrimne.logger as logger

from andrimne.timer import Timer

import logging
import sys


def main():
    timer = Timer()
    config.read_main_configuration()
    logger.configure()

    steps = map(step_import, read_modules())
    successful = True

    for step in steps:
        print_progress()
        logging.debug('executing step \'{}\''.format(step.__name__))
        if not execute_step(step):
            successful = False
            break

    log_run_completed(successful, timer)
    sys.exit(0 if successful else 1)


def print_progress():
    if config.read_or_default('verbosity', 'verbose') == 'verbose':
        sys.stdout.write('.')


def execute_step(step):
    # noinspection PyBroadException
    try:
        result = step.run()
        if result is None or result is True or result == 0:
            return True
    except Exception as e:
        logging.error(e)
        return False


def log_run_completed(successful, timer):
    if successful:
        logging.info('DONE! elapsed time was {}'.format(timer.elapsed()))
    else:
        logging.warning('ABORTED! elapsed time was {}'.format(timer.elapsed()))


def read_modules():
    logging.debug('reading step modules')
    return config.read('step_modules')


def step_import(module_name):
    logging.debug('importing step \'{}\''.format(module_name))
    return __import__('andrimne.steps.{}'.format(module_name), fromlist='andrimne.steps')


if __name__ == '__main__':
    main()
