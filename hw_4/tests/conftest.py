import pytest


@pytest.fixture
def dogs_base_url():
    return "https://dog.ceo/api"


@pytest.fixture
def brewery_base_url():
    return "https://api.openbrewerydb.org/v1/breweries"


@pytest.fixture
def placeholder_base_url():
    return "https://jsonplaceholder.typicode.com"
