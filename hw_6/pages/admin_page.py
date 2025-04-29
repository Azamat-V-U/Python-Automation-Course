from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from hw_6.pages.base_page import BasePage
from hw_6.pages.locators.admin_page_locators import AdminPageLoc


class AdminPage(BasePage):

    page_url = "/administration/"

    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        self.browser.get(f"{base_url}{self.page_url}")

    def login_page(self):
        """
        Метод для входа в админку
        :return:
        """
        self.enter_value(AdminPageLoc.username, "user")
        self.enter_value(AdminPageLoc.password, "bitnami", enter=True)
        self.page_title_verification("administration")

    def logout_page(self, locator: tuple[str, str]):
        """
        Метод для выхода из админки
        :param locator:
        :return:
        """
        self.click_element(locator)

    def add_new_product(self, product: str, meta: str, model: str, default: str):
        """
        Метод для добавления нового продукта
        :param product:
        :param meta:
        :param model:
        :param default:
        :return:
        """
        self.click_element(AdminPageLoc.catalog)
        self.click_element(AdminPageLoc.products)
        self.click_element(AdminPageLoc.add_new_btn)
        self.enter_value(AdminPageLoc.product_name, text=product)
        self.enter_value(AdminPageLoc.meta_tag_title, text=meta)
        self.click_element(AdminPageLoc.data_tab)
        self.enter_value(AdminPageLoc.model, text=model)
        self.click_element(AdminPageLoc.seo_tab)
        self.enter_value(AdminPageLoc.default, text=default)
        self.click_element(AdminPageLoc.save_btn)

    def accept_alert(self):
        alert = Alert(self.browser)
        alert.accept()

    def delete_product(self, text):
        """
        Метод для удаления продукта
        :param text:
        :return:
        """
        self.click_element(AdminPageLoc.catalog)
        self.click_element(AdminPageLoc.products)
        self.enter_value(AdminPageLoc.product_name_filter, text=text, enter=True)
        self.click_element(AdminPageLoc.filter_btn)
        self.click_element((By.XPATH, f"//tr[td[contains(text(), '{text}')]]//input[@type='checkbox']"))
        self.click_element(AdminPageLoc.delete_btn)
        self.accept_alert()
