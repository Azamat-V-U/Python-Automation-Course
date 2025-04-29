import os
from dotenv import load_dotenv
from hw_6.pages.login_page import LoginPage
from hw_6.pages.locators.login_page_locators import LoginPageLoc


# --url=http://localhost/en-gb?route=account/login


load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def test_login_button_verification(browser, base_url):
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.element_status_verification(LoginPageLoc.login_btn)


def test_email_field_placeholder_verification(browser, base_url):
    expected_placeholder = "e-mail address"
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.placeholder_verification(expected_placeholder, field="email")


def test_password_field_placeholder_verification(browser, base_url):
    expected_placeholder = "password"
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.placeholder_verification(expected_placeholder, field="password")


def test_login_with_valid_credentials(browser, base_url):
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.login_with_valid_data(email=EMAIL, password=PASSWORD)
    login_page.page_title_verification("My Account")


def test_login_with_invalid_credentials(browser, base_url):
    expected_message = "warning: no match for e-mail address and/or password."
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.login_with_invalid_data(email="test@@mail.ru", password="jhjklhRt!")
    login_page.text_verification(LoginPageLoc.error_message, expected_message)
