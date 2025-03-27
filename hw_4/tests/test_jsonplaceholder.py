import pytest
import requests
from pydantic import BaseModel


class Posts(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class UserCompany(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class UserGeo(BaseModel):
    lat: str
    lng: str


class UserAddress(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: UserGeo


class Users(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: UserAddress
    phone: str
    website: str
    company: UserCompany


@pytest.mark.regression
def test_get_posts_validation(placeholder_base_url):
    response = requests.get(f"{placeholder_base_url}/posts")
    response_json = response.json()
    posts = [Posts(**post) for post in response_json]
    assert response.status_code == 200, f"The status code {response.status_code} != 200"
    assert len(posts) > 0, f"The actual posts length is {len(posts)}"
    for post in posts:
        assert isinstance(post, Posts)


@pytest.mark.smoke
def test_get_users_validation(placeholder_base_url):
    response = requests.get(f"{placeholder_base_url}/users")
    response_json = response.json()
    users = [Users(**user) for user in response_json]
    assert response.status_code == 200, f"The status code is {response.status_code}"
    for user in users:
        assert isinstance(user, Users)


@pytest.mark.parametrize(
    "payload", [
        {
            "title": "post title1",
            "body": "post body1",
            "userId": 1
        },
        {
            "title": "post title2",
            "body": "post body2",
            "userId": 2
        },
        {
            "title": "post title3",
            "body": "post body3",
            "userId": 3
        }
    ],
    ids=["userId=1", "userId=2", "userId=3"]
)
def test_create_user_post(placeholder_base_url, payload):
    response = requests.post(
        f"{placeholder_base_url}/posts",
        json=payload
    )
    response_json = response.json()
    post = Posts(**response_json)
    assert response.status_code == 201, f"The status code {response.status_code} != 201"
    assert len(response_json) > 0, f"The actual response length is {len(response_json)}"
    assert isinstance(post, Posts)
    assert response_json["title"] == payload["title"], \
        f"The actual title {response_json['title']} != expected title {payload['title']}"
    assert response_json["body"] == payload["body"], \
        f"The actual body {response_json['body']} != expected {payload['body']}"
    assert response_json["userId"] == payload["userId"], \
        f"The actual userId {response_json['userId']} != expected userId {payload['userId']}"


@pytest.mark.parametrize(
    "payload", [
        {
            "id": 1,
            "title": "post title1",
            "body": "post body1",
            "userId": 1
        },
        {
            "id": 2,
            "title": "post title2",
            "body": "post body2",
            "userId": 2
        },
        {
            "id": 3,
            "title": "post title3",
            "body": "post body3",
            "userId": 3
        }
    ],
    ids=["userId=1", "userId=2", "userId=3"]
)
def test_update_user_post(placeholder_base_url, payload):
    response = requests.put(
        f"{placeholder_base_url}/posts/1",
        json=payload
    )
    response_json = response.json()
    post = Posts(**response_json)
    assert response.status_code == 200, f"The status code {response.status_code} != 200"
    assert len(response_json) > 0, f"The response length is {len(response_json)}"
    assert isinstance(post, Posts)
    assert response_json["title"] == payload["title"], \
        f"The actual title {response_json['title']} != expected title {payload['title']}"
    assert response_json["body"] == payload["body"], \
        f"The actual body {response_json['body']} != expected {payload['body']}"
    assert response_json["userId"] == payload["userId"], \
        f"The actual userId {response_json['userId']} != expected userId {payload['userId']}"


@pytest.mark.parametrize(
    "payload, post_number", [
        ({"title": "my title1"}, 1),
        ({"title": "my title2"}, 2),
        ({"title": "my title3"}, 3),
        ({"title": "my title4"}, 4),
        ({"title": "my title5"}, 5),
        ({"title": "my title6"}, 6),
        ({"title": "my title7"}, 7)
    ]
)
def test_patch_user_post(placeholder_base_url, payload, post_number):
    response = requests.patch(
        f"{placeholder_base_url}/posts/{post_number}",
        json=payload,
        headers={"Content-type": "application/json; charset=UTF-8"}
    )
    response_json = response.json()
    post = Posts(**response_json)
    assert response.status_code == 200, f"The actual status code {response.status_code} != 200"
    assert len(response_json) > 0, f"The response length is {len(response_json)}"
    assert isinstance(post, Posts)
    assert response_json["id"] == post_number, f"{response_json['id']} != {post_number}"
    assert payload["title"] == response_json["title"], f"{payload['title']} != {response_json['title']}"


@pytest.mark.smoke
def test_delete_user_post(placeholder_base_url):
    response = requests.delete(f"{placeholder_base_url}/posts/1")
    assert response.status_code == 200, f"The actual status code {response.status_code} != 200"
