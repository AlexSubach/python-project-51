import os
import requests
from page_loader.html_parser import update_html_info
from page_loader.rename import get_name_local
from page_loader.downloader import downland_resources
from page_loader import logger_config


logger = logger_config.make_logger(__name__)


def download(url, dir_path=os.getcwd()):
    logger.info(f'Request_url: {url}')
    logger.info(f'Output_path: {dir_path}')
    response = requests.get(url)
    html = response.text
    html_name = get_name_local(url, ext='.html')
    html_path = os.path.join(dir_path, html_name)
    dir_files_name = get_name_local(url, ext='_files')
    update_html, url_file = update_html_info(html, url, dir_files_name)
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(update_html)
    if url_file:
        directory_path = os.path.join(dir_path, dir_files_name)
        os.makedirs(directory_path, exist_ok=True)
        logger.info(f'Downloading resources...')
        downland_resources(url_file, directory_path)

    logger.info(f'All resources downloaded!')
    logger.info(f"Page was downloaded as: '{html_path}'")
    return html_path
