import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class LoginPageTestData:
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    email_placeholder = "e-mail address"
    password_placeholder = "password"
    expected_page_title = "My Account"
    invalid_email = "test@@mail.ru"
    valid_password = "jhjklhRt!"
    expected_message = "warning: no match for e-mail address and/or password."
