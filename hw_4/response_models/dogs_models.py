from pydantic import BaseModel
from typing import Dict, List, Union


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
