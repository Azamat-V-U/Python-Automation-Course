from pydantic import BaseModel, Field
from typing import Optional


class Brewery(BaseModel):
    id: str = Field(str, description='Required field')
    name: str = Field(str, description='Required field')
    brewery_type: str = Field(str, description='Required field')
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str = Field(str, description='Required field')
    state_province: str = Field(str, description='Required field')
    postal_code: Optional[str]
    country: str = Field(str, description='Required field')
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: str = Field(str, description='Required field')
    street: Optional[str]
