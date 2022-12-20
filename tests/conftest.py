import os
import pytest


@pytest.fixture
def update_html():
    return os.path.join(os.path.dirname(__file__), 'fixtures',
                        'ru-hexlet-io-courses.html')


@pytest.fixture
def before_html():
    return os.path.join(os.path.dirname(__file__), 'fixtures',
                        'before_page.html')


@pytest.fixture
def png():
    return os.path.join(os.path.dirname(__file__), 'fixtures/ru-hexlet-io-courses_files',
                        'ru-hexlet-io-assets-professions-python.png')


@pytest.fixture
def css():
    return os.path.join(os.path.dirname(__file__), 'fixtures/ru-hexlet-io-courses_files',
                        'ru-hexlet-io-assets-application.css')


@pytest.fixture
def js():
    return os.path.join(os.path.dirname(__file__), 'fixtures/ru-hexlet-io-courses_files',
                        'ru-hexlet-io-packs-js-runtime.js')


@pytest.fixture
def inner_html():
    return os.path.join(os.path.dirname(__file__), 'fixtures/ru-hexlet-io-courses_files',
                        'ru-hexlet-io-courses.html')
