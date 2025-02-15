import pytest
import requests
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import API

@pytest.fixture(scope='session')
def create_api():
    session = requests.Session()

    api_instance = API(session)
    
    yield api_instance
    
    session.close()
