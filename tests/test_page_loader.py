import tempfile
import os
import requests_mock
from page_loader import loader


def read_file(path):
    with open(path, mode='r') as file:
        return file.read()


def test_download(before_html, update_html, img):
    html_file = read_file(update_html)
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = f"{os.path.abspath(tmpdirname)}"
        with requests_mock.Mocker() as m:
            m.get('https://ru.hexlet.io/courses', text=before_html)
            result = loader.download('https://ru.hexlet.io/courses', temp_dir)
            open_result = read_file(result)
            assert html_file == open_result
