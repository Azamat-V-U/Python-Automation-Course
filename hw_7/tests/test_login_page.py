import allure
from hw_7.pages.login_page import LoginPage


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/login'")
@allure.story("Тестирование отображения элементов на Login странице")
@allure.title("Проверка активности кнопки login")
def test_login_button_verification(browser, base_url):
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.login_btn_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/login'")
@allure.story("Тестирование отображения элементов на Login странице")
@allure.title("Проверка отображения placeholder в поле email")
def test_email_field_placeholder_verification(browser, base_url):
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.placeholder_verification(field="email")


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/login'")
@allure.story("Тестирование отображения элементов на Login странице")
@allure.title("Проверка отображения placeholder в поле password")
def test_password_field_placeholder_verification(browser, base_url):
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.placeholder_verification(field="password")


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/login'")
@allure.story("Авторизация в системе")
@allure.title("Авторизация в системе с валидными данными")
def test_login_with_valid_credentials(browser, base_url):
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.login_with_valid_data()
    login_page.login_title_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=account/login'")
@allure.story("Авторизация в системе")
@allure.title("Авторизация в системе с не валидными данными")
def test_login_with_invalid_credentials(browser, base_url):
    login_page = LoginPage(browser)
    login_page.open_page(base_url)
    login_page.login_with_invalid_email()
    login_page.message_verification()
