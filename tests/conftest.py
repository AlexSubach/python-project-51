import os
import pytest


@pytest.fixture
def local_html():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'local_page.html')


@pytest.fixture
def update_html():
    return os.path.join(os.path.dirname(__file__), 'fixtures/assets_files', 'update_page.html')


@pytest.fixture
def download_img():
    return os.path.join(os.path.dirname(__file__), 'fixtures/assets_files', 'image.png')
