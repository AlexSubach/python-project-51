import os
import pytest


@pytest.fixture
def file_html():
    return os.path.join(os.path.dirname(__file__), 'fixtures', 'ru-hexlet-io-courses.html')
