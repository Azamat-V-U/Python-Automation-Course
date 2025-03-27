import csv
from hw_4.test_data import CSV_FILE_PATH


def get_endpoints():
    with open(CSV_FILE_PATH, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            yield row


expected_data = get_endpoints()
