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
