import andrimne.config as config
import andrimne.logger as logger


def main():
    cfg = config.read_main_configuration()
    logger.configure(cfg)


if __name__ == '__main__':
    main()
