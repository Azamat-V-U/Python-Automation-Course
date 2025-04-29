from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_6.pages.base_page import BasePage
from hw_6.pages.locators.desktops_page_locators import DesktopsLoc


class DesktopsPage(BasePage):

    page_url = "/en-gb/catalog/desktops"
    breadcrumb_link = DesktopsLoc.breadcrumb_link
    product_header = DesktopsLoc.product_header

    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        self.browser.get(f"{base_url}{self.page_url}")

    @property
    def get_element_text(self):
        """
        Метод возвращает текст из элемента в нижнем регистре
        :return:
        """
        element_text = WebDriverWait(self.browser, timeout=3).until(
            EC.visibility_of_element_located(DesktopsLoc.product_name)
        ).text.strip().lower()
        return element_text
