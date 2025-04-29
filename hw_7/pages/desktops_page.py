import allure
from selenium.webdriver.support import expected_conditions as EC
from hw_7.pages.base_page import BasePage
from hw_7.pages.locators.desktops_page_locators import DesktopsLoc
from hw_7.test_data.desktops_page_data import DesktopsPageTestData


class DesktopsPage(BasePage):

    page_url = "/en-gb/catalog/desktops"
    test_data = DesktopsPageTestData
    breadcrumb_link = DesktopsLoc.breadcrumb_link
    desktops_links = DesktopsLoc.desktops_links
    product_name = DesktopsLoc.product_name
    product_header = DesktopsLoc.product_header
    mac_link = DesktopsLoc.mac_link
    item_name = DesktopsLoc.item_name

    @allure.step("Открытие страницы 'descktops' ")
    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        full_url = base_url + self.page_url
        self.logger.info("%s: Opening url: '%s'" % (self.class_name, full_url))
        self.browser.get(f"{full_url}")

    @property
    def get_element_text(self):
        """
        Метод возвращает текст из элемента в нижнем регистре
        :return:
        """
        element_text = self.wait(timeout=3).until(
            EC.visibility_of_element_located(self.product_name)
        ).text.strip().lower()
        self.logger.info("%s: Getting the element '%s' text" % (self.class_name, element_text))
        return element_text

    @allure.step("Проверить название страницы на соответстие ожидаемому")
    def desktops_page_title_verification(self):
        """
           Метод проверяет название страницы на соответстие ожидаемому
        """
        self.page_title_verification(self.test_data.expected_title, timeout=3)

    @allure.step("Проверить название breadcrumb страницы на соответствие ожидаемому")
    def breadcrumb_name_verification(self):
        """
        Метод проверяет название breadcrumb страницы на соответствие ожидаемому
        :return:
        """
        self.text_verification(self.breadcrumb_link, self.test_data.expected_breadcrumb_name, timeout=2)

    @allure.step("Проверить название ссылок на соответсвие ожидаемым")
    def link_names_verification(self):
        """
        Метод проверяет название ссылок на соответсвие ожидаемым
        :return:
        """
        self.names_verification(self.desktops_links, self.test_data.expected_link_names, timeout=3)

    @allure.step("Кликнуть на ссылку продукта")
    def click_product_name(self, product_name: str):
        """
        Метод кликает по ссылке в зависимости от переданного названия продукта
        :param product_name:
        :return:
        """
        if product_name == "apple cinema 30":
            self.click_element(self.product_name, timeout=2)
        elif product_name == "mac":
            self.click_element(self.mac_link, timeout=2)

    @allure.step("Проверить название хедера страницы на странице продукта")
    def product_header_verification(self):
        """
        Метод проверяет название хедера страницы на странице продукта
        :return:
        """
        self.text_verification(self.product_header, self.get_element_text)

    @allure.step("Проверить название продукта на странице продукта")
    def product_name_verification(self):
        """
        Метод проверяет название продукта на странице продукта
        :return:
        """
        self.text_verification(self.item_name, self.test_data.expected_product_name, timeout=2)
