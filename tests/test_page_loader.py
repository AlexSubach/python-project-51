import tempfile
import os
import pytest
from urllib.parse import urljoin
import requests_mock

from page_loader import loader


def read_file(path, flag='r'):
    with open(path, flag) as file:
        return file.read()


url = 'https://ru.hexlet.io/courses'


def test_download(before_html, update_html, png, css, js, inner_html):
    with tempfile.TemporaryDirectory() as tmpdirname:
        with requests_mock.Mocker() as m:
            m.get(urljoin(url, '/assets/professions/python.png'), content=read_file(png, 'rb'))
            m.get(urljoin(url, '/assets/application.css'), text=read_file(css))
            m.get(urljoin(url, '/packs/js/runtime.js'), text=read_file(js))
            m.get(urljoin(url, '/courses'), text=read_file(inner_html))
            m.get(url, text=read_file(before_html))

            result_path = loader.download(url, tmpdirname)
            expected_path = os.path.join(tmpdirname, 'ru-hexlet-io-courses.html')
            assert result_path == expected_path

            result_content = read_file(result_path)
            expected_content = read_file(update_html)
            assert result_content == expected_content
            assert m.call_count == 5

