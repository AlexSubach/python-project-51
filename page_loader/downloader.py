import os
import requests


def downland_resources(files, dir_path):
    for url, name_local in files.items():
        response = requests.get(url)
        local_path = os.path.join(dir_path, name_local)
        with open(local_path, 'wb') as file:
            file.write(response.content)
