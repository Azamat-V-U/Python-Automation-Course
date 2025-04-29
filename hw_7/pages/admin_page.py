import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from hw_7.pages.base_page import BasePage
from hw_7.pages.locators.admin_page_locators import AdminPageLoc
from hw_7.test_data.admin_page_data import AdminPageData


class AdminPage(BasePage):

    page_url = "/administration/"
    username = AdminPageLoc.username
    password = AdminPageLoc.password
    test_data = AdminPageData
    catalog = AdminPageLoc.catalog
    products = AdminPageLoc.products
    add_new_btn = AdminPageLoc.add_new_btn
    product_name = AdminPageLoc.product_name
    meta_tag_title = AdminPageLoc.meta_tag_title
    data_tab = AdminPageLoc.data_tab
    model = AdminPageLoc.model
    seo_tab = AdminPageLoc.seo_tab
    default = AdminPageLoc.default
    save_btn = AdminPageLoc.save_btn
    logout = AdminPageLoc.logout
    product_name_filter = AdminPageLoc.product_name_filter
    filter_btn = AdminPageLoc.filter_btn
    checkbox = AdminPageLoc.checkbox
    delete_btn = AdminPageLoc.delete_btn
    message = AdminPageLoc.message

    @allure.step("Открытие страницы администратора")
    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        full_url = base_url + self.page_url
        self.logger.info("%s: Opening url: '%s'" % (self.class_name, full_url))
        self.browser.get(f"{full_url}")

    @allure.step("Авторизоваться в системе с правами администратора")
    def login_page(self):
        """
        Метод для входа в админку
        :return:
        """
        self.logger.info("%s: Logging in with administrator rights" % self.class_name)
        self.enter_value(self.username, self.test_data.username, timeout=2)
        self.enter_value(self.password, self.test_data.password, timeout=2,  enter=True)
        self.page_title_verification(self.test_data.page_title, timeout=3)

    @allure.step("Выйти из админки")
    def logout_page(self):
        """
        Метод для выхода из админки
        :return:
        """
        self.logger.info("%s: Logging out" % self.class_name)
        self.click_element(self.logout, timeout=2)

    @allure.step("Добавить  новый продукт")
    def add_new_product(self, product: str, meta: str, model: str, default: str):
        """
        Метод для добавления нового продукта
        :param product:
        :param meta:
        :param model:
        :param default:
        :return:
        """
        self.logger.info("%s: Adding the new product" % self.class_name)
        self.click_element(self.catalog, timeout=2)
        self.click_element(self.products, timeout=2)
        self.click_element(self.add_new_btn, timeout=2)
        self.enter_value(self.product_name, product, timeout=2)
        self.enter_value(self.meta_tag_title, meta, timeout=2)
        self.click_element(self.data_tab, timeout=3)
        self.enter_value(self.model, model, timeout=2)
        self.click_element(self.seo_tab, timeout=3)
        self.enter_value(self.default, default, timeout=2)
        self.click_element(self.save_btn, timeout=2)

    @allure.step("Проверить сообщение об успешном изменении")
    def message_verification(self):
        """
        Метод проверяет сообщение об успешном изменении
        :return:
        """
        self.text_verification(self.message, self.test_data.expected_message)

    @allure.step("Принять алерт")
    def accept_alert(self):
        """
        Метод для подверждения алерта
        :return:
        """
        self.logger.info("%s: Accepting alert" % self.class_name)
        alert = Alert(self.browser)
        alert.accept()

    @allure.step("Удалить продукт")
    def delete_product(self, name, product=False):
        """
        Метод для удаления продукта
        :param product:
        :param name:
        :return:
        """
        if product:
            self.logger.info("%s: Deleting the product" % self.class_name)
            self.click_element(self.products, timeout=2)
            self.enter_value(self.product_name_filter, name, timeout=4, enter=True)
            self.click_element(self.filter_btn, timeout=2)
            self.click_element((By.XPATH, self.checkbox.format(name=name)), timeout=3)
            self.click_element(self.delete_btn, timeout=3)
            self.accept_alert()
        else:
            self.logger.info("%s: Deleting the product" % self.class_name)
            self.click_element(self.catalog, timeout=2)
            self.click_element(self.products, timeout=2)
            self.enter_value(self.product_name_filter, name, timeout=4, enter=True)
            self.click_element(self.filter_btn, timeout=2)
            self.click_element((By.XPATH, self.checkbox.format(name=name)), timeout=3)
            self.click_element(self.delete_btn, timeout=3)
            self.accept_alert()
