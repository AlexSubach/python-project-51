import os
import pytest


@pytest.fixture
def update_html():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'update_page.html')


@pytest.fixture
def before_html():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'local_page.html')


@pytest.fixture
def img():
    return os.path.join(os.path.dirname(__file__), 'fixtures/page_files', 'image.png')
