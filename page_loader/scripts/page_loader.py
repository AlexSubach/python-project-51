#!/usr/bin/env python

from page_loader.loader import download
from page_loader.cli import pars


def main():
    url_page, output = pars()
    print(download(url_page, output))


if __name__ == '__main__':
    main()
