import os
import requests
import traceback
from page_loader.html_parser import update_html_info
from page_loader.rename import get_name_local
from page_loader.downloader import downland_resources, get_content
from page_loader import logger_config


logger = logger_config.make_logger(__name__)


def download(url, dir_path=os.getcwd()):
    html_name = get_name_local(url, ext='.html')
    html_path = os.path.join(dir_path, html_name)

    try:
        page = get_content(url)
    except requests.exceptions.RequestException:
        logger.debug(traceback.format_exc(2, chain=False))
        logger.error(f'Cannot download page: {url} \n{traceback.format_exc(0, chain=False)}')

    dir_files_name = get_name_local(url, ext='_files')
    update_html, url_file = update_html_info(page, url, dir_files_name)

    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(update_html)
    if url_file:
        directory_path = os.path.join(dir_path, dir_files_name)
        os.makedirs(directory_path, exist_ok=True)
        logger.info('Downloading resources...')
        downland_resources(url_file, directory_path)

    logger.info('All resources downloaded!')
    logger.info(f"Page was downloaded as: '{html_path}'")
    return html_path
