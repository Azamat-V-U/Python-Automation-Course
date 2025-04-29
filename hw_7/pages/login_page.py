import allure
from hw_7.pages.base_page import BasePage
from hw_7.pages.locators.login_page_locators import LoginPageLoc
from hw_7.test_data.login_page_data import LoginPageTestData


class LoginPage(BasePage):

    page_url = "/en-gb?route=account/login"
    test_data = LoginPageTestData
    login_btn = LoginPageLoc.login_btn
    email_field = LoginPageLoc.email_field
    password_field = LoginPageLoc.password_field
    error_message = LoginPageLoc.error_message

    @allure.step("Открыть страницу 'Account Login' ")
    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        full_url = base_url + self.page_url
        self.logger.info("%s: Opening url: '%s'" % (self.class_name, full_url))
        self.browser.get(f"{full_url}")

    @allure.step("Проверить название страницы")
    def login_title_verification(self):
        """
        Метод сравнивает ожидаемый заголовок страницы с текущим заголовоком
        :return:
        """
        self.page_title_verification(self.test_data.expected_page_title, timeout=2)

    @allure.step("Проверить placeholder в поле ввода")
    def placeholder_verification(self, field: str):
        """
        Метод сравнивает текущий и ожидаемый placeholder в поле ввода email или password
        :param field:
        :return:
        """
        email_placeholder = self.test_data.email_placeholder
        password_placeholder = self.test_data.password_placeholder
        if field == "email":
            placeholder = self.get_element(self.email_field, timeout=2).get_attribute("placeholder").strip().lower()
            self.logger.info(
                "%s: Asserting the actual placeholder '%s'== '%s' expected placeholder"
                % (self.class_name, placeholder, email_placeholder))
            assert placeholder == email_placeholder, \
                f"The actual placeholder value '{placeholder}' != expected '{email_placeholder}'"
        elif field == "password":
            placeholder = self.get_element(self.password_field, timeout=2).get_attribute("placeholder").strip().lower()
            self.logger.info(
                "%s: Asserting the actual placeholder '%s'== '%s' expected placeholder"
                % (self.class_name, placeholder, password_placeholder))
            assert placeholder == password_placeholder, \
                f"The actual placeholder value '{placeholder}' != expected '{password_placeholder}'"

    @allure.step("Авторизоваться с валидными данными")
    def login_with_valid_data(self):
        """
        Метод проверяет возможность входа в систему с валидными данными
        :return:
        """
        self.logger.info("%s: Logging with valid date" % self.class_name)
        self.enter_value(self.email_field, self.test_data.email, timeout=2)
        self.enter_value(self.password_field, self.test_data.password, timeout=2)
        self.click_element(self.login_btn, timeout=2)

    @allure.step("Авторизоваться с не заполненным полем email")
    def login_with_invalid_email(self):
        """
        Метод проверяет невозможность входа в систему с не валидным email
        :return:
        """
        self.logger.info("%s: Logging with invalid email" % self.class_name)
        self.enter_value(self.email_field, self.test_data.invalid_email, timeout=2)
        self.enter_value(self.password_field, self.test_data.valid_password, timeout=2)
        self.click_element(self.login_btn, timeout=2)

    @allure.step("Проверить активность кнопки 'Login'")
    def login_btn_verification(self):
        """
        Метод проверяет активность кнопки 'Login'
        :return:
        """
        self.element_status_verification(self.login_btn, timeout=2)

    @allure.step("Проверить pop-up сообщение на соответсвие ожидаемому")
    def message_verification(self):
        """
        Метод проверяет pop-up сообщение на соответсвие ожидаемому
        :return:
        """
        self.text_verification(self.error_message, self.test_data.expected_message, timeout=3)
