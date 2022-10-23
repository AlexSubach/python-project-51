from urllib.parse import urlparse
import os


def cut_url(url):
    url_parser = urlparse(url)
    clear_url = url_parser.netloc + url_parser.path
    return clear_url


def get_rename(url):
    name = ''
    indent = '-'
    clear_url = cut_url(url)
    for char in clear_url:
        if char.isalnum():
            name += char
        else:
            name += indent
    return name + '.html'


def get_path(path, url):
    rename_file = get_rename(url)
    new_path = os.path.join(path, rename_file)
    return new_path

