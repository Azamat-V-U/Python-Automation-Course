from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open_page(self, base_url):
        self.browser.get(base_url)

    def get_element(self, locator: tuple[str, str], timeout=20):
        """
        Метод возвращает элемент, когда он отображается на веб странице
        :param locator:
        :param timeout:
        :return:
        """
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple[str, str], timeout=3):
        """
        Метод возвращает список элементов, когда они отображается на веб странице
        :param locator:
        :param timeout:
        :return:
        """
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click_element(self, locator: tuple[str, str]):
        """
        Метод переводит фокус на требуемый элемент и кликает по нему, если элемент виден на веб странице
        :param locator:
        :return:
        """
        # WebDriverWait(self.browser, timeout=5).until(EC.element_to_be_clickable(locator))
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(1).click().perform()

    def enter_value(self, locator: tuple[str, str], text: str, enter=False):
        """
        Метод вводит в поле требуемый текст. Если выставить enter=True иммитирует нажание кнопки Enter с клавиатуры
        :param locator:
        :param text:
        :param enter:
        :return:
        """
        if enter:
            self.get_element(locator).send_keys(text)
            self.get_element(locator).send_keys(Keys.ENTER)
        else:
            self.get_element(locator).send_keys(text)

    def element_visibility_verification(self, locator: tuple[str, str]):
        """
        Метод проверяет, что элемент отображается на странице
        :param locator:
        :return:
        """
        element = self.get_element(locator)
        assert element.is_displayed(), f"The '{element}' isn't visible for user"

    def text_verification(self, locator: tuple[str, str], expected_text: str):
        """
        Метод сравнивает текущий текст элемента с ожидаемым
        :param locator:
        :param expected_text:
        :return:
        """
        if self.get_element(locator):
            actual_text = self.get_element(locator).text.strip().lower()
            assert actual_text == expected_text, \
                f"Actual message '{actual_text}' != expected message '{expected_text}'"

    def page_title_verification(self, expected_text: str):
        """
        Метод сравнивает ожидаемый заголовок страницы с текущим заголовоком
        :param expected_text:
        :return:
        """
        actual_title = self.browser.title.strip().lower()
        expected_title = expected_text.lower()
        assert expected_title in actual_title, \
            f"Expected title '{expected_title}' not in page title '{actual_title}'"

    def catalog_names_verification(self, locator: tuple[str, str], expected_items: list[str]):
        """
        Метод сравнивает текущий текст каждого найденного элемента со с ожидаемым списком
        :param locator:
        :param expected_items:
        :return:
        """
        catalog_names = self.get_elements(locator)
        for name in catalog_names:
            name = name.text.strip().lower()
            assert name in expected_items, f"The actual name '{name}' not in expected names {expected_items}"

    def element_status_verification(self, locator: tuple[str, str]):
        assert self.get_element(locator).is_enabled(), f"The element '{self.get_element(locator)}' isn't active"
