import requests
import pytest
from pytest import param
from jsonschema import validate


@pytest.mark.parametrize("input_city, per_page", [
    param("san diego", 3),
    param("norman", 3),
    param("austin", 10),
    param("mount pleasant", 7),
    param("bend", 7),
    param("portland", 10),
    param("boise", 6),
    param("denver", 9),
    param("el reno", 1),
    param("knoxville", 15),
])
def test_list_breweries_by_city(brewery_base_url, input_city, per_page):
    response = requests.get(
        brewery_base_url,
        params={
            "by_city": input_city,
            "per_page": per_page
        }
    )
    response_json = response.json()
    assert response.status_code == 200, f"The actual status code {response.status_code} != 200"
    assert len(response_json) == per_page, f"The response length is {len(response_json)} != {per_page}"
    for brewery in response.json():
        assert input_city in brewery["city"].lower(), f"The city {input_city} not in city {brewery["city"]}"


@pytest.mark.parametrize(
    "input_city, per_page", [
        param("san diego", 5),
        param("san leandro", 5),
        param("san francisco", 5),
        param("santa rosa", 5),
        param("bend", 5),
        param("portland", 5)
    ]
)
@pytest.mark.parametrize(
    "input_state, input_brewery_type", [
        param("california", "micro"),
        param("california", "regional"),
        param("california", "large")
    ]
)
def test_list_breweries_by_type_and_city(
        brewery_base_url, input_state, input_city, input_brewery_type, per_page):
    response = requests.get(
        brewery_base_url,
        params={
            "by_state": input_state,
            "by_city": input_city,
            "by_type": input_brewery_type,
            "per_page": per_page
        }
    )
    response_json = response.json()
    assert response.status_code == 200, f"The actual status code {response.status_code} != 200"
    assert len(response_json) <= 5, f"The response length is {len(response_json)} != {per_page}"
    for brewery in response_json:
        assert input_brewery_type in brewery["brewery_type"].lower(), \
            f"The brewery_type{input_brewery_type} not in {brewery["brewery_type"]}"
        assert input_city in brewery["city"].lower(), f"The input_city{input_city} not in {brewery["city"]}"
        assert input_state in brewery["state"].lower(), f"The input_state{input_state} not in {brewery["state"]}"


@pytest.mark.smoke
def test_list_breweries_response_schema_validation(brewery_base_url):
    response = requests.get(brewery_base_url)
    response_json = response.json()

    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "address_1": {"type": ["string", "null"]},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "state_province": {"type": ["string", "null"]},
                "postal_code": {"type": ["string", "null"]},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "state": {"type": ["string", "null"]},
                "street": {"type": ["string", "null"]}
            },
            "required": [
                "id", "name", "brewery_type", "address_1", "state_province", "postal_code",
                "country", "longitude", "latitude", "phone", "website_url", "state", "street"
            ]
        }
    }

    validate(instance=response_json, schema=schema)
    assert response.status_code == 200, f"The actual status code {response.status_code} != 200"


@pytest.mark.regression
def test_search_breweries(brewery_base_url):
    city = "san diego"
    per_page = 50
    response = requests.get(
        brewery_base_url + "/search",
        params={
            "query": city,
            "per_page": per_page
        }
    )
    response_json = response.json()
    assert response.status_code == 200, f"The actual status code {response.status_code} != 200"
    assert len(response_json) <= 50, f"The actual response length {len(response_json)} != {per_page}"
    for brewery in response_json:
        assert brewery["city"].lower() == city, f"The expected city {city} not in {brewery["city"]}"


@pytest.mark.parametrize(
    "input_per_page, output_per_page", [
        (1, 1),
        (100, 100),
        (199, 199),
        (200, 200),
        (201, 200)
    ], ids=["per_page=1", "per_page=100", "per_page=199", "per_page=200", "per_page=201"]
)
def test_boundary_analysis_per_page(brewery_base_url, input_per_page, output_per_page):
    response = requests.get(
        brewery_base_url,
        params={
             "per_page": input_per_page
        }
    )
    response_json = response.json()
    assert response.status_code == 200, f"The status code is {response.status_code} != 200"
    assert len(response_json) == output_per_page, \
        f"The actual response length {len(response_json)} != expected {output_per_page}"


@pytest.mark.parametrize(
    "brewery_id_4, brewery_id_5, brewery_id_6", [
        param(
            "d81ff708-b5d2-478f-af6a-6d40f5beb9ac",
            "e5f3e72a-fee2-4813-82cf-f2e53b439ae6",
            "58293321-14ae-49d7-9a7b-08436c9e63a6"
        ),
        param(
            "08f78223-24f8-4b71-b381-ea19a5bd82df",
            "232e8f62-9afc-45f5-b4bc-582c26b5c43b",
            "42aa37d5-8384-4ffe-8c81-7c982eff0384"
        )
    ],
)
@pytest.mark.parametrize(
    "brewery_id_1, brewery_id_2, brewery_id_3", [
        param(
            "5128df48-79fc-4f0f-8b52-d06be54d0cec",
            "9c5a66c8-cc13-416f-a5d9-0a769c87d318",
            "34e8c68b-6146-453f-a4b9-1f6cd99a5ada"
        ),
        param(
            "6d14b220-8926-4521-8d19-b98a2d6ec3db",
            "e2e78bd8-80ff-4a61-a65c-3bfbd9d76ce2",
            "e432899b-7f58-455f-9c7b-9a6e2130a1e0"
        ),
        param(
            "9f1852da-c312-42da-9a31-097bac81c4c0",
            "ea4f30c0-bce6-416b-8904-fab4055a7362",
            "ef970757-fe42-416f-931d-722451f1f59c"
        )
    ],
)
def test_get_breweries_by_ids(
            brewery_base_url, brewery_id_1, brewery_id_2, brewery_id_3, brewery_id_4, brewery_id_5, brewery_id_6
):
    response = requests.get(
        brewery_base_url,
        params={
             "by_ids": f"{brewery_id_1},{brewery_id_2},{brewery_id_3},{brewery_id_4},{brewery_id_5},{brewery_id_6}"
        }
    )
    response_json = response.json()
    expected_ids = {
        brewery_id_1, brewery_id_2, brewery_id_3, brewery_id_4, brewery_id_5, brewery_id_6
    }
    actual_ids = {brewery["id"] for brewery in response_json}
    assert response.status_code == 200, f"The status code {response.status_code} != 200"
    assert len(response_json) == len(expected_ids), \
        f"The actual response length {len(response_json)} != expected {len(expected_ids)}"
    assert actual_ids == expected_ids, f"The actual ids {actual_ids} != expected ids {expected_ids}"
