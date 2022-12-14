import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from page_loader.rename import is_local, get_name_local


ATTR = {'img': 'src', 'link': 'href', 'script': 'src'}


def update_html_info(html, url, dir_data):
    data = {}
    make_tree = BeautifulSoup(html, 'html.parser')
    tags = make_tree.find_all(ATTR.keys())
    for tag in tags:
        name = ATTR[tag.name]
        data_url = tag.get(name)
        full_url = urljoin(url, data_url)
        if is_local(full_url, url):
            local_name = get_name_local(full_url)
            data[full_url] = local_name
            tag[name] = os.path.join(dir_data, local_name)
    new_html = make_tree.prettify()
    return new_html, data
