import logging

FORMAT = '%(asctime)s %(levelname)-8s %(name)s [%(filename)s:%(lineno)d] %(message)s'  # noqa E501


def get_logger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():
        # create console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # create formatter
        formatter = logging.Formatter(FORMAT)

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

    return logger
