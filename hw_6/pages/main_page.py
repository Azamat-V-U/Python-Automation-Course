from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_6.pages.base_page import BasePage
from hw_6.pages.locators.main_page_locators import MainPageLoc


class MainPage(BasePage):

    def select_currency(self, currency: str):
        """
        Метод выбирает передаваемую валюту
        :param currency:
        :return:
        """
        if currency == "pound_sterling":
            self.click_element(MainPageLoc.currency_dropdown)
            self.click_element(MainPageLoc.pound_sterling_currency)
        elif currency == "dollar":
            self.click_element(MainPageLoc.currency_dropdown)
            self.click_element(MainPageLoc.dollar_currency)
        else:
            self.click_element(MainPageLoc.currency_dropdown)
            self.click_element(MainPageLoc.euro_currency)

    def product_price_verification(self, locator: tuple[str, str], expected_text: str):
        """
        Метод сравнивает текущий текст элемента с ожидаемым
        :param locator:
        :param expected_text:
        :return:
        """
        if self.get_element(locator):
            WebDriverWait(self.browser, timeout=3).until(EC.text_to_be_present_in_element(locator, expected_text))
            actual_text = self.get_element(locator).text.strip().lower()
            assert actual_text == expected_text, \
                f"Actual message '{actual_text}' != expected message '{expected_text}'"
