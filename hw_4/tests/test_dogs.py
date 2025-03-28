import pytest
import requests
from pytest import param
from pydantic import BaseModel
from typing import Dict, List, Union
from hw_4.test_data.test_data import expected_data


class AllBreeds(BaseModel):
    message: Union[Dict[str, List[str]], List[str], str]
    status: str


class BreedsList(BaseModel):
    message: Dict[str, List[str]]
    status: str


class ByBreed(BaseModel):
    message: List[str]
    status: str


class RandomBreed(BaseModel):
    message: str
    status: str


def id_val(val):
    return val[0]


@pytest.mark.smoke
@pytest.mark.parametrize("data", expected_data, ids=id_val)
def test_get_dogs_endpoints(data, dogs_base_url):
    endpoint = dogs_base_url + data[0]
    expected_status_code = data[2]
    expected_content_type = data[3]
    response = requests.get(url=endpoint)
    response_json = response.json()
    breeds_model = AllBreeds(**response_json)
    assert response.status_code == eval(expected_status_code), \
        f"The actual status code {response.status_code} != expected {expected_status_code}"
    assert response.headers["Content-Type"] == expected_content_type, \
        f"The actual content-type is {response.headers["Content-Type"]}"
    assert len(response_json) > 0, f"The actual response length is {len(response_json)}"
    assert isinstance(breeds_model, AllBreeds)


@pytest.mark.smoke
def test_schema_validation_list_all_breeds(dogs_base_url):
    response = requests.get(f"{dogs_base_url}/breeds/list/all")
    response_json = response.json()
    breeds_model = BreedsList(**response_json)
    assert response.status_code == 200, f"The status code {response.status_code} != 200"
    assert response.headers["Content-Type"] == "application/json", \
        f"The actual content-type is {response.headers["Content-Type"]}"
    assert len(response_json) > 0, f"The actual response length is {len(response_json)}"
    assert isinstance(breeds_model, BreedsList)


@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status_code", [
        param("/breeds/image/random", 200, id="get the random breed image"),
        param("/breed/bulldog/images/random", 200, id="browse random breed image"),
]
)
def test_schema_validation_random_breed(dogs_base_url, endpoint, expected_status_code):
    response = requests.get(dogs_base_url + endpoint)
    response_json = response.json()
    breeds_model = RandomBreed(**response_json)
    assert response.status_code == expected_status_code, \
        f"The actual status code {response.status_code} != expected {expected_status_code}"
    assert response.headers["Content-Type"] == "application/json", \
        f"The actual content-type is {response.headers["Content-Type"]}"
    assert len(response_json) > 0, f"The actual response length is {len(response_json)}"
    assert isinstance(breeds_model, RandomBreed)


@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status_code", [
        param("/breed/bulldog/list", 200, id="get by sub-breed"),
        param("/breed/bulldog/images", 200, id="get the images by breed")
]
)
def test_response_schema_validation_breed_list(dogs_base_url, endpoint, expected_status_code):
    response = requests.get(dogs_base_url + endpoint)
    response_json = response.json()
    breed_model = ByBreed(**response_json)
    assert response.status_code == expected_status_code, \
        f"The actual status code {response.status_code} != expected {expected_status_code}"
    assert response.headers["Content-Type"] == "application/json", \
        f"The actual content-type is {response.headers["Content-Type"]}"
    assert len(response_json) > 0, f"The actual response length is {len(response_json)}"
    assert isinstance(breed_model, ByBreed)


@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status_code", [
        param("/breeds/list/all", 405),
        param("/breed/bulldog/images", 405),
        param("/breed/bulldog/list", 405),
        param("/breeds/image/random", 405),
        param("/breed/bulldog/images/random", 405)
], ids=["list all breeds", "get by breed", "get by sub-breed", "get the random breed image", "browse breed list"]
)
def test_incorrect_method(dogs_base_url, endpoint, expected_status_code):
    response = requests.post(dogs_base_url + endpoint)
    assert response.status_code == expected_status_code, f"The status code {response.status_code} != 405"


@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status_code", [
        param("//breeds/list/all", 404),
        param("//breed/bulldog/images", 404),
        param("//breed/bulldog/list", 404),
        param("//breeds/image/random", 404),
        param("//breed/bulldog/images/random", 404)
], ids=["list all breeds", "get by breed", "get by sub-breed", "get the random breed image", "get the breeds list"]
)
def test_incorrect_url(dogs_base_url, endpoint, expected_status_code):
    response = requests.post(dogs_base_url + endpoint)
    assert response.status_code == expected_status_code, f"The status code {response.status_code} != 404"
