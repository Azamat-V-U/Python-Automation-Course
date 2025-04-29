import allure
from selenium.webdriver.support.select import Select
from hw_7.pages.base_page import BasePage
from hw_7.pages.locators.product_page_locators import ProductPageLoc
from hw_7.test_data.product_page import ProductPageTestData


class ProductPage(BasePage):
    page_url = "/en-gb/product/apple-cinema"
    test_data = ProductPageTestData
    input_field = ProductPageLoc.input_field
    add_to_cart_btn = ProductPageLoc.add_to_cart_btn
    dropdown = ProductPageLoc.dropdown
    check_box = ProductPageLoc.check_box
    radio_button = ProductPageLoc.radio_button

    @allure.step("Открыть страницу продукта 'Apple Cinema 30'")
    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        full_url = base_url + self.page_url
        self.logger.info("%s: Opening url: '%s'" % (self.class_name, full_url))
        self.browser.get(f"{full_url}")

    @allure.step("Ввести текст в поле 'Text_area'")
    def enter_in_text_area(self):
        """
        Метод вводит текст в поле 'Textarea'
        :return:
        """
        data = self.test_data.input_data
        self.enter_value(self.input_field, data, timeout=2)

    @allure.step("Проверить введенный в поле текст")
    def text_area_verification(self):
        """
        Метод проверяет отображение введенного в поле текста
        :return:
        """
        entered_value = self.test_data.input_data
        actual_value = self.get_element(self.input_field, timeout=2).get_attribute("value")
        self.logger.info("%s: Getting the entered text '%s'" % (self.class_name, entered_value))
        assert actual_value == entered_value, f"The actual value '{actual_value} != expected '{entered_value}'"
        self.logger.info("%s: Asserting the actual value '%s == '%s' entered" % (self.class_name, actual_value, entered_value))

    @allure.step("Проверить активность кнопки 'Add to cart'")
    def add_to_cart_btn_verification(self):
        """
        Метод проверяет активность кнопки 'Add to cart'
        :return:
        """
        self.element_status_verification(self.add_to_cart_btn, timeout=2)

    @allure.step("Проверка выбора значений в dropdown")
    def select_dropdown_options(self):
        """
        Метод перебирает последовательно все опции дропдауна  с подтверждением, что опция выбрана.
        :return: True | False
        """
        select = self.get_element(self.dropdown, timeout=2)
        dropdown_list = Select(select)
        dropdown_options = dropdown_list.options
        for index in range(len(dropdown_options)):
            dropdown_list.select_by_index(index)
            self.logger.info(
                "%s: Asserting the '%s' option  is selected" % (self.class_name, index)
            )
            assert True, f"The dropdown list wasn't selected"

    def select_options(self, locator: tuple[str, str]):
        """
        Метод выбирает последовательно все опции(checkbox | radiobutton) с подтверждением, что опция был выбрана
        :return: True | False
        """
        options = self.get_elements(locator, timeout=2)
        if options is not None:
            for option in options:
                option_id = option.get_attribute("id")
                self.click_element(option)
                self.logger.info(
                    "%s: Asserting the '%s' option  is selected" % (self.class_name, option_id)
                )
                assert option.is_selected(), f"The checkbox '{option_id}' wasn't selected"

    @allure.step("Выбрать последовательно все чек-боксы")
    def select_all_checkboxes(self):
        """
        Метод выбирает последовательно все опции(checkbox)
        :return:
        """
        self.select_options(self.check_box)

    @allure.step("Выбрать последовательно все радио-батоны")
    def select_all_radio_buttons(self):
        """
        Метод выбирает последовательно все опции(radiobutton)
        :return:
        """
        self.select_options(self.radio_button)

    @allure.step("Проверить название страницы на соответсвие ожидаемому")
    def product_tittle_verification(self):
        """
        Метод проверяет название страницы на соответсвие ожидаемому
        :return:
        """
        self.page_title_verification(self.test_data.expected_title, timeout=2)
