import pytest
import requests

from api import API

@pytest.fixture(scope='session')
def create_api():
    session = requests.Session()

    api_instance = API(session)
    
    yield api_instance
    
    session.close()
