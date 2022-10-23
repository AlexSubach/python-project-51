import tempfile
import os
import requests_mock
from page_loader import page_loader


def read_file(path):
    with open(path, 'r') as file:
        return file.read()


def test_download(file_html):
    html_file = read_file(file_html)
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = f"{os.path.abspath(tmpdirname)}"
        with requests_mock.Mocker() as m:
            m.get('http://test.com/about', text=html_file)

            result = page_loader.download('http://test.com/about', temp_dir)
            open_result = read_file(result)
            assert html_file == open_result
