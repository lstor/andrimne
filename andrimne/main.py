import andrimne.config as config
import andrimne.logger as logger

import logging


def main():
    cfg = config.read_main_configuration()
    logger.configure(cfg)

    steps = map(step_import, read_modules(cfg))

    for step in steps:
        logging.info('executing step \'%s\'' % step.__name__)
        step.run()


def read_modules(cfg):
    logging.info('reading step modules')
    return cfg['step_modules']


def step_import(module_name):
    logging.info('importing step \'%s\'' % module_name)
    return __import__('andrimne.steps.%s' % module_name, fromlist='andrimne.steps')


if __name__ == '__main__':
    main()
