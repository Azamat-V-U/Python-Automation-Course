from hw_6.pages.base_page import BasePage


class SiteMapPage(BasePage):
    page_url = "/en-gb?route=information/sitemap"

    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        self.browser.get(f"{base_url}{self.page_url}")
