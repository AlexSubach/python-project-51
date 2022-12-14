from urllib.parse import urlparse
import os


def get_rename(url):
    name = ''
    indent = '-'
    clear_name = url.rstrip('/')
    for char in clear_name:
        if char.isalnum():
            name += char
        else:
            name += indent
    return name


def get_name_local(url, ext='.html'):
    url_parser = urlparse(url)
    root, extension = os.path.splitext(url_parser.path)
    path = get_rename(os.path.join(url_parser.netloc + root))
    if extension:
        ext = extension
    return path + ext


def is_local(full_url, url):
    return urlparse(full_url).netloc == urlparse(url).netloc
