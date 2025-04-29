from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_6.pages.base_page import BasePage
from hw_6.pages.locators.login_page_locators import LoginPageLoc


class LoginPage(BasePage):

    page_url = "/en-gb?route=account/login"

    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        self.browser.get(f"{base_url}{self.page_url}")

    def page_title_verification(self, expected_text: str):
        """
        Метод сравнивает ожидаемый заголовок страницы с текущим заголовоком
        :param expected_text:
        :return:
        """
        WebDriverWait(self.browser, timeout=3).until(EC.title_is(expected_text))
        actual_title = self.browser.title.strip().lower()
        expected_title = expected_text.lower()
        assert expected_title in actual_title, \
            f"Expected title '{expected_title}' not in page title '{actual_title}'"

    def placeholder_verification(self, attribute: str, field=""):
        """
        Метод сравнивает текущий и ожидаемый placeholder в поле ввода email или password
        :param attribute:
        :param field:
        :return:
        """
        if field == "email":
            actual_attribute = self.get_element(LoginPageLoc.email_field).get_attribute("placeholder").strip().lower()
            assert actual_attribute == attribute, \
                f"The actual placeholder value '{actual_attribute}' != expected '{attribute}'"
        elif field == "password":
            actual_attribute = self.get_element(LoginPageLoc.password_field).get_attribute("placeholder").strip().lower()
            assert actual_attribute == attribute, \
                f"The actual placeholder value '{actual_attribute}' != expected '{attribute}'"

    def login_with_valid_data(self, email: str, password: str):
        """
        Метод проверяет возможность входа в систему с валидными данными
        :param email:
        :param password:
        :return:
        """
        self.enter_value(LoginPageLoc.email_field, email)
        self.enter_value(LoginPageLoc.password_field, password)
        self.click_element(LoginPageLoc.login_btn)

    def login_with_invalid_data(self, email: str, password: str):
        """
        Метод проверяет невозможность входа в систему с не валидным email
        :param email:
        :param password:
        :return:
        """
        self.enter_value(LoginPageLoc.email_field, email)
        self.enter_value(LoginPageLoc.password_field, password)
        self.click_element(LoginPageLoc.login_btn)
