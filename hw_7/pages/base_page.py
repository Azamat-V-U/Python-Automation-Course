import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.actions = ActionChains(browser)
        self.class_name = type(self).__name__

    @allure.step("Открытие домашней страницы")
    def open_page(self, base_url):
        """
        Открытие домашней страницы
        :param base_url:
        :return:
        """
        self.logger.info("%s: Opening url: %s" % (self.class_name, base_url))
        self.browser.get(base_url)

    def wait(self, timeout=1):
        return WebDriverWait(self.browser, timeout)

    def get_element(self, locator: tuple[str, str], timeout=1):
        """
        Метод возвращает элемент, когда он отображается на веб странице
        :param timeout:
        :param locator:
        :return:
        """
        self.logger.info("%s: Checking if element %s is present" % (self.class_name, str(locator)))
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple[str, str], timeout=1):
        """
        Метод возвращает список элементов, когда они отображается на веб странице
        :param timeout:
        :param locator:
        :return:
        """
        self.logger.info("%s: Check if elements %s are present" % (self.class_name, str(locator)))
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    def click_element(self, locator: tuple[str, str], timeout=1):
        """
        Метод переводит фокус на требуемый элемент и кликает по нему, если элемент виден на веб странице
        :param timeout:
        :param locator:
        :return:
        """
        element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        self.logger.info("%s: Clicking element: %s" % (self.class_name, str(locator)))
        self.actions.move_to_element(element).pause(1).click().perform()

    def enter_value(self, locator: tuple[str, str], text: str, timeout=1, enter=False):
        """
        Метод вводит в поле требуемый текст. Если выставить enter=True иммитирует нажание кнопки Enter с клавиатуры
        :param timeout:
        :param locator:
        :param text:
        :param enter:
        :return:
        """
        element = self.get_element(locator, timeout)
        if enter:
            element.clear()
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
            self.logger.info("%s: Entered input '%s' in input field '%s'" % (self.class_name, text, locator))
        else:
            element.clear()
            element.send_keys(text)
            self.logger.info("%s: Entered input '%s' in input field '%s'" % (self.class_name, text, locator))

    def element_visibility_verification(self, locator: tuple[str, str], timeout=1):
        """
        Метод проверяет, что элемент отображается на странице
        :param timeout:
        :param locator:
        :return:
        """
        element = self.get_element(locator, timeout)
        self.logger.info("%s: Asserting if element %s is present" % (self.class_name, locator))
        assert element.is_displayed(), f"The '{element}' isn't visible for user"

    def text_verification(self, locator: tuple[str, str], expected_text: str, timeout=2):
        """
        Метод сравнивает текущий текст элемента с ожидаемым
        :param timeout:
        :param locator:
        :param expected_text:
        :return:
        """
        element = self.wait(timeout).until(EC.visibility_of_element_located(locator))
        if element:
            actual_text = element.text.strip().lower()
            self.logger.info(
                "%s: Asserting if element text '%s' == '%s'" % (self.class_name, actual_text, expected_text)
            )
            assert actual_text == expected_text, \
                f"Actual element text '{actual_text}' != expected text '{expected_text}'"

    def page_title_verification(self, expected_text: str, timeout=1):
        """
        Метод сравнивает ожидаемый заголовок страницы с текущим заголовоком
        :param timeout:
        :param expected_text:
        :return:
        """
        self.wait(timeout).until(EC.title_contains(expected_text))
        actual_title = self.browser.title.strip().lower()
        expected_title = expected_text.lower()
        self.logger.info(
            "%s: Asserting the expected title '%s' in '%s' page title" % (self.class_name, expected_title, actual_title)
        )
        assert expected_title in actual_title, \
            f"Expected title '{expected_title}' not in page title '{actual_title}'"

    def wait_for_page_title(self, page_title: str, timeout=1):
        """
        Метод возвращает заголовок страницы в нижнем регистре
        :param timeout:
        :param page_title:
        :return:
        """
        self.wait(timeout).until(EC.title_contains(page_title))
        return self.browser.title.strip().lower()

    def names_verification(self, locator: tuple[str, str], expected_names: list[str], timeout=1):
        """
        Метод сравнивает текущий текст каждого найденного элемента со с ожидаемым списком
        :param timeout:
        :param locator:
        :param expected_names:
        :return:
        """
        catalog_names = self.get_elements(locator, timeout)
        for name in catalog_names:
            name = name.text.strip().lower()
            self.logger.info(
                "%s: Asserting the '%s' name  in  '%s' expected names" % (self.class_name, name, expected_names)
            )
            assert name in expected_names, f"The actual name '{name}' not in expected names {expected_names}"

    def element_status_verification(self, locator: tuple[str, str], timeout=1):
        element = self.get_element(locator, timeout)
        self.logger.info("%s: Asserting '%s' element is active" % (self.class_name, locator))
        assert element.is_enabled(), f"The element '{self.get_element(locator)}' isn't active"
