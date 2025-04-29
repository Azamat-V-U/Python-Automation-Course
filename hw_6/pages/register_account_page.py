from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_6.pages.base_page import BasePage
from hw_6.pages.locators.register_account_locators import RegisterAccountLoc


class RegisterAccount(BasePage):
    page_url = "/en-gb?route=account/register"

    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        self.browser.get(f"{base_url}{self.page_url}")

    def register_new_account_with_valid_data(self, first_name: str, last_name: str, email: str, password: str):
        """
        Метод регистрирует в системе нового пользователя с валидными данными
        :param first_name:
        :param last_name:
        :param email:
        :param password:
        :return:
        """
        self.enter_value(RegisterAccountLoc.first_name, first_name)
        self.enter_value(RegisterAccountLoc.last_name, last_name)
        self.enter_value(RegisterAccountLoc.email, email)
        self.enter_value(RegisterAccountLoc.password, password)
        self.click_element(RegisterAccountLoc.privacy_policy_toggle)
        self.click_element(RegisterAccountLoc.continue_btn)

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

    def register_new_account_with_empty_first_name(self, last_name: str, email: str, password: str):
        """
        Метод регистрирует в системе нового пользователя с незаполненным полем "first name"
        :param last_name:
        :param email:
        :param password:
        :return:
        """
        self.enter_value(RegisterAccountLoc.last_name, last_name)
        self.enter_value(RegisterAccountLoc.email, email)
        self.enter_value(RegisterAccountLoc.password, password)
        self.click_element(RegisterAccountLoc.privacy_policy_toggle)
        self.click_element(RegisterAccountLoc.continue_btn)

    def register_new_account_without_privacy_policy(self, first_name: str, last_name: str, email: str, password: str):
        """
        Метод регистрирует в системе нового пользователя с выключенным "privacy policy"
        :param first_name:
        :param last_name:
        :param email:
        :param password:
        :return:
        """
        self.enter_value(RegisterAccountLoc.first_name, first_name)
        self.enter_value(RegisterAccountLoc.last_name, last_name)
        self.enter_value(RegisterAccountLoc.email, email)
        self.enter_value(RegisterAccountLoc.password, password)
        self.click_element(RegisterAccountLoc.continue_btn)
