import os
import requests
from progress.bar import Bar
from page_loader.logger_config import make_logger


logger = make_logger(__name__)


def downland_resources(files, dir_path):
    bar = Bar('Downloading resources: ', max=len(files))
    for url, name_local in files.items():
        try:
            response = requests.get(url)
            content = response.content
            local_path = os.path.join(dir_path, name_local)
            with open(local_path, 'wb') as file:
                file.write(content)
            bar.next()
        except requests.exceptions.RequestException:
            logger.error('Connection Error while downloading resources!')
