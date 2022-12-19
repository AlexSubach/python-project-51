#!/usr/bin/env python
import sys

from page_loader.loader import download
from page_loader.cli import pars
from page_loader.logger_config import make_logger


logger = make_logger(__name__)


def main():
    url_page, output = pars()
    try:
        output_path = download(url_page, output)
    except Exception as error:
        logger.exception(error)
        print('Sorry, there was an error!')
        print('See log.file for details')
        sys.exit(1)
    print(output_path)


if __name__ == '__main__':
    main()
