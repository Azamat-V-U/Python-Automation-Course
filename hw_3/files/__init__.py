import os.path


FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH = get_path(filename="users.csv")
CSV_FILE_PATH_BOOKS = get_path(filename="books.csv")
JSON_FILE_PATH_READ = get_path(filename="user.json")
JSON_FILE_PATH_WRITE = get_path(filename="result.json")
