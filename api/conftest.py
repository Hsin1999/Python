import pytest
import requests

token=None

@pytest.fixture(scope='session')
def set_up():
    if token:
        return token