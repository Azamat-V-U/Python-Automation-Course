from hw_6.pages.locators.product_page_locators import ProductPageLoc
from hw_6.pages.product_page import ProductPage

# --url=http://localhost/en-gb/product/apple-cinema


def test_page_title_verification(browser, base_url):
    expected_title = "apple cinema 30"
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.page_title_verification(expected_title)


def test_text_area_verification(browser, base_url):
    input_data = "Some Data"
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.enter_value(ProductPageLoc.input_field, input_data)
    product_page.entered_text_verification(ProductPageLoc.input_field, input_data)


def test_add_to_cart_button_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.element_status_verification(ProductPageLoc.add_to_cart_btn)


def test_dropdown_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.select_dropdown_options(ProductPageLoc.dropdown)


def test_checkboxes_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.select_options(ProductPageLoc.check_box)


def test_radio_buttons_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.select_options(ProductPageLoc.radio_button)
