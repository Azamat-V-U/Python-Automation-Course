import json
from csv import DictReader
from itertools import cycle
from pydantic import BaseModel, Field
from typing import List
from files import CSV_FILE_PATH_BOOKS, JSON_FILE_PATH_READ, JSON_FILE_PATH_WRITE


class Book(BaseModel):
    Title: str
    Author: str
    Pages: str
    Genre: str


class User(BaseModel):
    name: str
    gender: str
    address: str
    age: int
    books: List[Book] = Field(default_factory=list)


def read_csv():
    """
    Вычитывает данные из CSV-файла и возвращает список объектов books с использованием Pydantic схем.
    :return: books
    """
    with open(CSV_FILE_PATH_BOOKS, newline="", encoding="utf-8") as file:
        reader = DictReader(file)
        books = [Book(**book) for book in reader]
    return books


new_books = read_csv()


def read_json():
    """
    Вычитывает данные из JSON-файла и возвращает список объектов users с использованием Pydantic схем.
    :return: users
    """
    with open(JSON_FILE_PATH_READ, "r") as file:
        users_data = json.load(file)
        users = [User(**user) for user in users_data]
    return users


new_users = read_json()


def distribute_books(users_list: List[User], books_list: List[Book]) -> List[User]:
    """
    Распределяет книги books поровну среди пользователей users.
    :param users_list:
    :param books_list:
    :return: List[User]
    """
    user_cycle = cycle(users_list)
    for book in books_list:
        next(user_cycle).books.append(book)
    return users_list


updated_users = distribute_books(new_users, new_books)


def write_json():
    """
    Преобразует и записывет обьект "updated_users" в JSON файл.
    """
    with open(JSON_FILE_PATH_WRITE, "w", encoding="utf-8") as file:
        json.dump([user.model_dump() for user in updated_users], file, indent=4, ensure_ascii=False)


write_json()
