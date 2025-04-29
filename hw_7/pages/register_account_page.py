import allure
from hw_7.pages.base_page import BasePage
from hw_7.pages.locators.register_account_locators import RegisterAccountLoc
from hw_7.test_data.register_account_page_data import RegisterAccountPageTestData


class RegisterAccount(BasePage):
    page_url = "/en-gb?route=account/register"
    test_data = RegisterAccountPageTestData
    page_header = RegisterAccountLoc.page_header
    login_link = RegisterAccountLoc.login_link
    first_name = RegisterAccountLoc.first_name
    last_name = RegisterAccountLoc.last_name
    email = RegisterAccountLoc.email
    password = RegisterAccountLoc.password
    privacy_policy_toggle = RegisterAccountLoc.privacy_policy_toggle
    continue_btn = RegisterAccountLoc.continue_btn
    first_name_error_message = RegisterAccountLoc.first_name_error_message
    error_message = RegisterAccountLoc.error_message

    @allure.step("Открытие страницы для регистрации")
    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        full_url = base_url + self.page_url
        self.logger.info("%s: Opening url: '%s'" % (self.class_name, full_url))
        self.browser.get(f"{full_url}")

    @allure.step("Проверить заголовок страницы на соответствие ожидаемому")
    def page_header_verification(self):
        """
        Метод проверяет заголовок страницы на соответствие ожидаемому
        :return:
        """
        self.text_verification(self.page_header, self.test_data.expected_header, timeout=2)

    @allure.step("Кликнуть на ссылку 'login page'")
    def click_on_login_page(self):
        """
        Метод кликает по ссылке 'login page'
        :return:
        """
        self.click_element(self.login_link, timeout=2)

    @allure.step("Регистрация в системе нового аккаунта с валидными данными")
    def register_new_account_with_valid_data(self, first_name: str, last_name: str, email: str, password: str):
        """
        Метод регистрирует в системе нового пользователя с валидными данными
        :param first_name:
        :param last_name:
        :param email:
        :param password:
        :return:
        """
        self.logger.info("%s: Registering the new user with valid data" % self.class_name)
        self.enter_value(self.first_name, first_name, timeout=2)
        self.enter_value(self.last_name, last_name, timeout=2)
        self.enter_value(self.email, email, timeout=2)
        self.enter_value(self.password, password, timeout=2)
        self.click_element(self.privacy_policy_toggle, timeout=2)
        self.click_element(self.continue_btn, timeout=2)

    @allure.step("Проверить название страницы")
    def login_title_verification(self):
        """
        Метод сравнивает ожидаемый заголовок страницы с текущим заголовоком
        :return:
        """
        self.page_title_verification(self.test_data.expected_title, timeout=3)

    @allure.step("Регистрация в системе нового аккаунта с незаполненным полем 'email'")
    def register_new_account_with_empty_first_name(self):
        """
        Метод регистрирует в системе нового пользователя с незаполненным полем "first name"
        :return:
        """
        self.logger.info("%s: Registering the new user with empty empty email field" % self.class_name)
        self.enter_value(self.last_name, self.test_data.last_name, timeout=2)
        self.enter_value(self.email, self.test_data.email, timeout=2)
        self.enter_value(self.password, self.test_data.password, timeout=2)
        self.click_element(self.privacy_policy_toggle, timeout=2)
        self.click_element(self.continue_btn, timeout=2)

    @allure.step("Проверить сообщение о не заполненном 'first name' на соответствие ожидаемому")
    def empty_fist_name_message_verification(self):
        """
        Метод проверяет сообщение о не заполненном first name на соответствие ожидаемому
        :return:
        """
        self.text_verification(self.first_name_error_message, self.test_data.expected_message, timeout=2)

    @allure.step("Проверить название страницы")
    def new_account_title_verification(self):
        """
        Метод сравнивает ожидаемый заголовок страницы с текущим заголовоком
        :return:
        """
        self.page_title_verification(self.test_data.expected_page_title, timeout=3)

    @allure.step("Регистрация в системе нового аккаунта с не включенным 'privacy policy'")
    def register_new_account_without_privacy_policy(self):
        """
        Метод регистрирует в системе нового пользователя с выключенным "privacy policy"
        :return:
        """
        self.logger.info("%s: Registering the new user without privacy policy" % self.class_name)
        self.enter_value(self.first_name, self.test_data.first_name)
        self.enter_value(self.last_name, self.test_data.last_name, timeout=2)
        self.enter_value(self.email, self.test_data.email, timeout=2)
        self.enter_value(self.password, self.test_data.password, timeout=2)
        self.click_element(RegisterAccountLoc.continue_btn)

    @allure.step("Проверить сообщение об обязательности принятия 'privacy policy' на соответствие ожидаемому")
    def required_privacy_policy_message_verification(self):
        """
        Метод проверяет сообщение об обязательности принятия 'privacy policy' на соответствие ожидаемому
        :return:
        """
        self.text_verification(self.error_message, self.test_data.error_message, timeout=2)
