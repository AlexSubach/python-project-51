import logging


FORMAT = "%(asctime)s : %(name)s : %(levelname)s : %(filename)s : %(message)s"

logging.basicConfig(
    format=FORMAT,
    filename='page_loader.log',
    filemode='w',
)


def make_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
