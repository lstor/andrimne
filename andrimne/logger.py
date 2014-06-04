from andrimne.config import read_or_default
import logging


def configure():
    log_config = {
        'filename': read_or_default('logfile', 'log.txt'),
        'level': read_or_default('loglevel', logging.WARNING),
        'datefmt': read_or_default('log_timeformat', '%H:%M:%S - %d/%m/%Y'),
        'format': read_or_default('log_format', '%(asctime)s - %(name)s - %(levelname)-10s %(message)s'),
    }

    logging.basicConfig(**log_config)

    logging.info('')
    logging.info('')
    logging.info('---------------------------------------------------------------------------')
    logging.info('STARTING ...')
    logging.info('---------------------------------------------------------------------------')
    logging.info('')


def log_step(step_name):
    message = 'step: {}'.format(step_name.replace('_', ' '))
    logging.info(message)


