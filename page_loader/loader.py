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

    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL) as error:
        logger.error('Requested url is not correct!')
        raise error
    except requests.exceptions.HTTPError as error:
        logger.error('HTTPError!')
        raise error
    except requests.exceptions.ConnectionError as error:
        logger.error('Connection Error!')
        raise error
    html = response.text
    html_name = get_name_local(url, ext='.html')
    html_path = os.path.join(dir_path, html_name)
    dir_files_name = get_name_local(url, ext='_files')
    update_html, url_file = update_html_info(html, url, dir_files_name)
    try:
        os.path.exists(dir_path)
    except FileNotFoundError as err:
        logger.error('The specified folder does not exist!')
        raise err

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
