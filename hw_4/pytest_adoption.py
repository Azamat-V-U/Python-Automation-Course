import requests


def test_url_status(base_url, response_status_code):
    response = requests.get(base_url)
    assert response.status_code == response_status_code, \
        f"The actual status code {response.status_code} != expected status code {response_status_code}"
