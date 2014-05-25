import andrimne.config as config
import andrimne.logger as logger

from andrimne.timer import Timer

import logging


def main():
    timer = Timer()
    cfg = config.read_main_configuration()
    logger.configure(cfg)

    steps = map(step_import, read_modules(cfg))

    for step in steps:
        logging.debug('executing step \'%s\'' % step.__name__)
        step.run(cfg)

    logging.info('DONE! elapsed time was %s' % timer.elapsed())


def read_modules(cfg):
    logging.debug('reading step modules')
    return cfg['step_modules']


def step_import(module_name):
    logging.debug('importing step \'%s\'' % module_name)
    return __import__('andrimne.steps.%s' % module_name, fromlist='andrimne.steps')


if __name__ == '__main__':
    main()
