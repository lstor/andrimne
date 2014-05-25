from andrimne.config import config_or_default
import logging


def configure(config):
    log_config = {
        'filename': config_or_default(config, 'logfile', 'log.txt'),
        'level': config_or_default(config, 'loglevel', logging.WARNING),
        'datefmt': config_or_default(config, 'log_timeformat', '%H:%M:%S - %d/%m/%Y'),
        'format': config_or_default(config, 'log_format', '%(asctime)s - %(name)s - %(levelname)-10s %(message)s'),
    }

    logging.basicConfig(**log_config)

    logging.info('')
    logging.info('')
    logging.info('---------------------------------------------------------------------------')
    logging.info('STARTING ...')
    logging.info('---------------------------------------------------------------------------')
    logging.info('')
