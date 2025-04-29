from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class ProductPageLoc:
    input_field = (By.NAME, "option[209]")
    dropdown = (By.NAME, "option[217]")
    add_to_cart_btn = (By.CLASS_NAME, "btn-primary.btn-lg.btn-block")
    check_box = (By.NAME, "option[223][]")
    radio_button = (By.NAME, "option[218]")
