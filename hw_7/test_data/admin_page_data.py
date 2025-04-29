import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class AdminPageData:
    username = os.getenv("ADMIN_USERNAME")
    password = os.getenv("ADMIN_PASSWORD")
    page_title = "Dashboard"
    new_product_data = [
        ("My apple", "meta apple", "12345", "moby"),
        ("My phone", "phone meta", "yund", "word"),
        ("My device", "meta device", "1234Io5", "link")
    ]
    product_name = [
        'My apple',
        'My phone',
        'My device'
    ]
    expected_message = "success: you have modified products!"
