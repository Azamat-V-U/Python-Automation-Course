from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from hw_5.pages.locators.product_page_locators import ProductPage

# --url=http://localhost/en-gb/product/apple-cinema


def test_page_title_verification(browser, base_url):
    expected_title = "apple cinema 30"
    browser.get(base_url)
    page_title = browser.title.strip().lower()
    assert page_title == expected_title, f"The actual page title '{page_title}' != expected {expected_title}"


def text_area_verification(browser, base_url):
    input_data = "Enter something"
    browser.get(base_url)
    text_area = WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located(
        ProductPage.input_field
    ))
    text_area.send_keys(input_data)
    entered_value = text_area.get_attribute("value")
    assert entered_value == input_data, f"The actual value '{entered_value} != expected '{input_data}'"


def test_add_to_cart_button_verification(browser, base_url):
    browser.get(base_url)
    add_to_cart_btn = WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located(
        ProductPage.add_to_cart_btn
    ))
    assert add_to_cart_btn.is_enabled(), f"The 'add to cart button' isn't active"


def test_dropdown_verification(browser, base_url):
    browser.get(base_url)
    select = WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located(
        ProductPage.dropdown
    ))
    dropdown_list = Select(select)
    options = dropdown_list.options

    for index in range(len(options)):
        dropdown_list.select_by_index(index)
        assert True, f"The dropdown list wasn't selected"


def test_checkboxes_verification(browser, base_url):
    browser.get(base_url)
    actions = ActionChains(browser)
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located(
        ProductPage.check_box
    ))
    check_boxes = browser.find_elements(*ProductPage.check_box)

    if check_boxes is not None:
        for check_box in check_boxes:
            actions.move_to_element(check_box)
            actions.click(check_box)
            actions.perform()
            assert check_box.is_selected(), f"The checkbox '{check_box}' wasn't selected"


def test_radio_buttons_verification(browser, base_url):
    browser.get(base_url)
    actions = ActionChains(browser)
    WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located(
        ProductPage.radio_button
    ))
    radio_buttons = browser.find_elements(*ProductPage.radio_button)

    if radio_buttons is not None:
        for radio_button in radio_buttons:
            actions.move_to_element(radio_button)
            actions.click(radio_button)
            actions.perform()
            assert radio_button.is_selected(), f"The radio button '{radio_buttons}' wasn't selected"
