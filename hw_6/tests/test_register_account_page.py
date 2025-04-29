import pytest
from hw_6.pages.locators.register_account_locators import RegisterAccountLoc
from hw_6.pages.register_account_page import RegisterAccount
from faker import Faker

# --url=http://localhost/en-gb?route=account/register

fake = Faker()


def test_page_header_verification(browser, base_url):
    expected_header = "register account"
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.text_verification(RegisterAccountLoc.page_header, expected_header)


def test_link_to_login_page_verification(browser, base_url):
    expected_title = "Account Login"
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.click_element(RegisterAccountLoc.login_link)
    register_account.page_title_verification(expected_title)


@pytest.mark.parametrize("first_name, last_name, email, password", [
    (fake.first_name_male(), fake.last_name_male(), fake.email(), fake.password()),
    (fake.first_name_female(), fake.last_name_female(), fake.email(), fake.password()),
    (fake.first_name(), fake.last_name(), fake.email(), fake.password()),
])
def test_register_account_with_valid_credentials(browser, base_url, first_name, last_name, email, password):
    expected_title = "Your Account Has Been Created!"
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.register_new_account_with_valid_data(
        first_name=first_name, last_name=last_name, email=email, password=password
    )
    register_account.page_title_verification(expected_title)


def test_register_account_with_empty_first_name(browser, base_url):
    expected_message = "first name must be between 1 and 32 characters!"
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.register_new_account_with_empty_first_name(
        fake.last_name(), fake.email(), fake.password()
    )
    register_account.text_verification(RegisterAccountLoc.first_name_error_message, expected_message)


def test_register_account_without_privacy_policy(browser, base_url):
    expected_message = "warning: you must agree to the privacy policy!"
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.register_new_account_without_privacy_policy(
        fake.first_name(), fake.last_name(), fake.email(), fake.password()
    )
    register_account.text_verification(RegisterAccountLoc.error_message, expected_message)
