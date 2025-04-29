import allure
from hw_7.pages.base_page import BasePage
from hw_7.pages.locators.site_map_page_locators import SiteMapLoc
from hw_7.test_data.site_map_page_data import SiteMapTestData


class SiteMapPage(BasePage):
    page_url = "/en-gb?route=information/sitemap"
    test_data = SiteMapTestData
    breadcrumb_home = SiteMapLoc.breadcrumb_home
    sitemap_header = SiteMapLoc.sitemap_header
    base_links = SiteMapLoc.base_links
    my_account_links = SiteMapLoc.my_account_links
    information_links = SiteMapLoc.information_links

    @allure.step("Открытие site map страницы")
    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        full_url = base_url + self.page_url
        self.logger.info("%s: Opening url: '%s'" % (self.class_name, full_url))
        self.browser.get(f"{full_url}")

    @allure.step("Проверить отображение breadcrumb 'home' на странице")
    def breadcrumb_visibility_verification(self):
        """
        Метод проверяет, что breadcrumb home отображается на странице
        :return:
        """
        self.element_visibility_verification(self.breadcrumb_home, timeout=2)

    @allure.step("Проверить хедера страницы 'site map'")
    def site_map_header_verification(self):
        """
        Метод проверяет отображение названия страницы
        :return:
        """
        self.text_verification(self.sitemap_header, self.test_data.sitemap_page_header, timeout=2)

    @allure.step("Проверить, что названия основных ссылок на странице соотвестуют ожидаемым")
    def base_link_names_verification(self):
        """
        Метод проверяет соответствие названий основных ссылок на страницы с ожидаемыми
        :return:
        """
        self.names_verification(self.base_links, self.test_data.base_links, timeout=2)

    @allure.step("Проверить, что названия ссылок 'my account' соотвестуют ожидаемым")
    def my_account_link_names_verification(self):
        """
        Метод проверяет соответствие названий  ссылок в 'my account'  с ожидаемыми
        :return:
        """
        self.names_verification(self.my_account_links, self.test_data.my_account_links, timeout=2)

    @allure.step("Проверить, что названия ссылок 'information' соотвестуют ожидаемым")
    def information_link_names_verification(self):
        """
        Метод проверяет соответствие названий  ссылок в 'information'  с ожидаемыми
        :return:
        """
        self.names_verification(self.information_links, self.test_data.information_links, timeout=2)
