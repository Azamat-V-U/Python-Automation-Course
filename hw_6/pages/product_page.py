from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from hw_6.pages.base_page import BasePage


class ProductPage(BasePage):
    page_url = "/en-gb/product/apple-cinema"

    def open_page(self, base_url):
        """
        Дополненный метод "open_page" из модуля base_page
        :param base_url:
        :return:
        """
        self.browser.get(f"{base_url}{self.page_url}")

    def entered_text_verification(self, locator: tuple[str, str], input_data: str):
        entered_value = self.get_element(locator).get_attribute("value")
        assert entered_value == input_data, f"The entered value '{entered_value} != expected '{input_data}'"

    def select_dropdown_options(self, locator: tuple[str, str]):
        """
        Метод перебирает последовательно все опции дропдауна  с подтверждением, что опция выбрана.
        :param locator:
        :return: True | False
        """
        select = self.get_element(locator)
        dropdown_list = Select(select)
        dropdown_options = dropdown_list.options
        for index in range(len(dropdown_options)):
            dropdown_list.select_by_index(index)
            assert True, f"The dropdown list wasn't selected"

    def select_options(self, locator: tuple[str, str]):
        """
        Метод выбирает последовательно все опции(checkbox | radiobutton) с подтверждением, что опция был выбрана
        :param locator:
        :return: True | False
        """
        actions = ActionChains(self.browser)
        check_boxes = self.get_elements(locator)
        if check_boxes is not None:
            for check_box in check_boxes:
                actions.move_to_element(check_box)
                actions.pause(1)
                actions.click(check_box)
                actions.perform()
                assert check_box.is_selected(), f"The checkbox '{check_box}' wasn't selected"
