import os
import traceback
import requests
from progress.bar import Bar
from page_loader.logger_config import make_logger


logger = make_logger(__name__)


def downland_resources(resources_url, dir_path):
    bar = Bar('Downloading resources: ', max=len(resources_url))
    for url, name_local in resources_url.items():
        try:
            content = get_content(url)
            local_path = os.path.join(dir_path, name_local)
            with open(local_path, 'wb') as file:
                file.write(content)
            bar.next()
        except requests.exceptions.RequestException:
            logger.debug(traceback.format_exc(2, chain=False))
            logger.warning(f'{url} download will be skipped')


def get_content(url):
    response = requests.get(url)
    response.raise_for_status()
    logger.info(f'Got content {url}')
    return response.content
