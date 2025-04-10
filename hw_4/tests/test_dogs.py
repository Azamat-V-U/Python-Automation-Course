import pytest
import requests
from pytest import param
from hw_4.test_data.test_data import expected_data
from hw_4.response_models.dogs_models import AllBreeds, BreedsList, RandomBreed, ByBreed


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
    assert response.status_code == eval(expected_status_code), \
        f"The actual status code {response.status_code} != expected {expected_status_code}"
    AllBreeds(**response_json)
    assert response.headers["Content-Type"] == expected_content_type, \
        f"The actual content-type is {response.headers["Content-Type"]}"


@pytest.mark.smoke
def test_schema_validation_list_all_breeds(dogs_base_url):
    response = requests.get(f"{dogs_base_url}/breeds/list/all")
    response_json = response.json()
    assert response.status_code == 200, f"The status code {response.status_code} != 200"
    BreedsList(**response_json)
    assert response.headers["Content-Type"] == "application/json", \
        f"The actual content-type is {response.headers["Content-Type"]}"


@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status_code", [
        param("/breeds/image/random", 200, id="get the random breed image"),
        param("/breed/bulldog/images/random", 200, id="browse random breed image"),
]
)
def test_schema_validation_random_breed(dogs_base_url, endpoint, expected_status_code):
    response = requests.get(dogs_base_url + endpoint)
    response_json = response.json()
    assert response.status_code == expected_status_code, \
        f"The actual status code {response.status_code} != expected {expected_status_code}"
    RandomBreed(**response_json)
    assert response.headers["Content-Type"] == "application/json", \
        f"The actual content-type is {response.headers["Content-Type"]}"


@pytest.mark.regression
@pytest.mark.parametrize("endpoint, expected_status_code", [
        param("/breed/bulldog/list", 200, id="get by sub-breed"),
        param("/breed/bulldog/images", 200, id="get the images by breed")
]
)
def test_response_schema_validation_breed_list(dogs_base_url, endpoint, expected_status_code):
    response = requests.get(dogs_base_url + endpoint)
    response_json = response.json()
    assert response.status_code == expected_status_code, \
        f"The actual status code {response.status_code} != expected {expected_status_code}"
    ByBreed(**response_json)
    assert response.headers["Content-Type"] == "application/json", \
        f"The actual content-type is {response.headers["Content-Type"]}"


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
