import pytest
import allure
from hw_7.pages.register_account_page import RegisterAccount
from hw_7.test_data.register_account_page_data import RegisterAccountPageTestData


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/register'")
@allure.story("Тестирование отображения элементов на Register Account странице")
@allure.title("Проверка отображения заголовка страницы")
def test_page_header_verification(browser, base_url):
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.page_header_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/register'")
@allure.story("Тестирование отображения элементов на Register Account странице")
@allure.title("Проверка перехода по ссылке login page")
def test_link_to_login_page_verification(browser, base_url):
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.click_on_login_page()
    register_account.login_title_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/register'")
@allure.story("Регистрация нового аккаунта")
@allure.title("Регистрация нового аккаунта с валидными данными")
@pytest.mark.parametrize("first_name, last_name, email, password", RegisterAccountPageTestData.valid_credentials)
def test_register_account_with_valid_credentials(browser, base_url, first_name, last_name, email, password):
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.register_new_account_with_valid_data(
        first_name, last_name, email, password
    )
    register_account.new_account_title_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/register'")
@allure.story("Регистрация нового аккаунта")
@allure.title("Невозможность регистрации нового аккаунта с пустым полем first name")
def test_register_account_with_empty_first_name(browser, base_url):
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.register_new_account_with_empty_first_name()
    register_account.empty_fist_name_message_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/register'")
@allure.story("Регистрация нового аккаунта")
@allure.title("Невозможность регистрации нового аккаунта без установки флага privacy policy")
def test_register_account_without_privacy_policy(browser, base_url):
    register_account = RegisterAccount(browser)
    register_account.open_page(base_url)
    register_account.register_new_account_without_privacy_policy()
    register_account.required_privacy_policy_message_verification()
