import allure
from selenium.webdriver.support import expected_conditions as EC
from hw_7.pages.base_page import BasePage
from hw_7.pages.locators.main_page_locators import MainPageLoc
from hw_7.test_data.main_page_data import MainPageTestData


class MainPage(BasePage):
    test_data = MainPageTestData
    add_to_wishlist_btn = MainPageLoc.add_to_wishlist
    add_to_cart_btn = MainPageLoc.add_to_cart_btn
    cart_dropdown = MainPageLoc.dropdown
    currency_icon = MainPageLoc.currency_icon
    search_field = MainPageLoc.search_field
    catalog_products = MainPageLoc.catalog_products
    macbook_link = MainPageLoc.macbook_link
    actual_message = MainPageLoc.actual_message

    @allure.step("Выбрать валюту для отображения цен продуктов")
    def select_currency(self, currency: str):
        """
        Метод выбирает передаваемую валюту
        :param currency:
        :return:
        """
        if currency == "pound_sterling":
            self.logger.info("%s: Selecting '%s' currency" % (self.class_name, currency))
            self.click_element(MainPageLoc.currency_dropdown, timeout=2)
            self.click_element(MainPageLoc.pound_sterling_currency, timeout=2)
        elif currency == "dollar":
            self.logger.info("%s: Selecting '%s' currency" % (self.class_name, currency))
            self.click_element(MainPageLoc.currency_dropdown, timeout=2)
            self.click_element(MainPageLoc.dollar_currency, timeout=2)
        else:
            self.logger.info("%s: Selecting '%s' currency" % (self.class_name, currency))
            self.click_element(MainPageLoc.currency_dropdown, timeout=2)
            self.click_element(MainPageLoc.euro_currency, timeout=2)

    @allure.step("Кликнуть на иконку 'add to cart'")
    def click_add_to_cart(self):
        self.click_element(self.add_to_cart_btn, timeout=2)

    @allure.step("Кликнуть на иконку 'add to wish list'")
    def click_add_to_wish_list(self):
        self.click_element(self.add_to_wishlist_btn, timeout=10)

    @allure.step("Проверить отображение цены добавленного продукта в корзине")
    def product_price_verification(self):
        """
        Метод проверяет наличие цены добавленого продукта в корзине
        :return:
        """
        expected_price = self.test_data.expected_price
        self.wait(timeout=3).until(EC.text_to_be_present_in_element(self.cart_dropdown, expected_price))
        self.text_verification(self.cart_dropdown, expected_price)

    @allure.step("Проверить иконку выбранной валюты")
    def currency_icon_verification(self, expected_icon: str):
        self.text_verification(self.currency_icon, expected_icon, timeout=3)

    @allure.step("Проверить отображение иконки 'add to wishlist list'")
    def add_to_wish_btn_visibility_verification(self):
        """
        Метод проверяет, что элемент отображается на странице
        :return:
        """
        self.element_visibility_verification(self.add_to_wishlist_btn, timeout=10)

    @allure.step("Ввести в поле поиска 'MacBook'")
    def enter_macbook(self):
        self.enter_value(self.search_field, self.test_data.expected_page_title, timeout=2, enter=True)

    @allure.step("Проверить название страницы найденного продукта ")
    def verify_page_title(self):
        expected_title = self.test_data.expected_page_title
        self.wait_for_page_title(page_title=expected_title, timeout=3)
        self.page_title_verification(expected_title)

    @allure.step("Сравнить текущие названия категорий продуктов каталога с ожидаемыми названиями")
    def catalog_names_verification(self):
        """
        Метод сравнивает текущие названия категорий продуктов с ожидаемым списком
        :return:
        """
        self.names_verification(self.catalog_products, self.test_data.expected_names)

    @allure.step("Проверить текущее название ссылки продукта с ожидаемым")
    def macbook_link_verification(self):
        """
        Метод сравнивает текущее название ссылки продукта с ожидаемым
        :return:
        """
        self.text_verification(self.macbook_link, self.test_data.macbook_link)

    @allure.step("Проверить текущее pop-up сообщение с ожидаемым")
    def message_verification(self):
        """
        Метод сравнивает текущее pop-up сообщение с ожидаемым
        :return:
        """
        self.text_verification(self.actual_message, self.test_data.expected_message)
