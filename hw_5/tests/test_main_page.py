from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from hw_5.pages.locators.main_page_locators import MainPage


def test_add_item_to_wishlist_button_verification(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    add_to_wishlist = wait.until(EC.visibility_of_element_located(
        MainPage.add_to_wishlist)
    )
    assert add_to_wishlist.is_displayed(), f"The add_to_wishlist button isn't visible for user"


def test_add_item_to_wishlist_message_verification(browser, base_url):
    browser.get(base_url)
    expected_message = "You must login or create an account to save MacBook to your wish list!"
    action = ActionChains(browser)
    wait = WebDriverWait(browser, timeout=5)
    add_to_wishlist = wait.until(EC.presence_of_element_located(
        MainPage.add_to_wishlist)
    )
    action.move_to_element(add_to_wishlist)
    action.click(add_to_wishlist)
    action.perform()
    actual_message = wait.until(EC.visibility_of_element_located(
        MainPage.actual_message
    ))
    assert actual_message.text == expected_message, \
        f"Actual message {actual_message.text} != expected message{expected_message}"


def test_add_item_to_cart(browser, base_url):
    browser.get(base_url)
    action = ActionChains(browser)
    wait = WebDriverWait(browser, timeout=5)
    add_to_cart_btn = wait.until(EC.presence_of_element_located(
        MainPage.add_to_cart_btn)

    )
    action.move_to_element(add_to_cart_btn)
    action.perform()
    add_to_cart_btn.click()
    try:
        wait.until(
            EC.text_to_be_present_in_element(
                MainPage.dropdown, "1 item(s) - $602.00")
        )
        dropdown = browser.find_element(*MainPage.dropdown)
    except StaleElementReferenceException:
        dropdown = browser.find_element(*MainPage.dropdown)
    assert dropdown.text == "1 item(s) - $602.00"


def test_select_currency_sign_verification(browser, base_url):
    browser.get(base_url)
    action = ActionChains(browser)
    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.element_to_be_clickable((By.ID, "form-currency"))).click()
    pound_sterling_currency = wait.until(EC.visibility_of_element_located(
        MainPage.pound_sterling_currency)
    )
    action.move_to_element(pound_sterling_currency)
    action.click(pound_sterling_currency)
    action.perform()
    wait.until(EC.visibility_of_element_located(
        MainPage.pound_sterling_sign)
    )
    pound_sterling_sign = browser.find_element(*MainPage.pound_sterling_sign)
    assert pound_sterling_sign.text == "£ Currency"


def test_search_for_product(browser, base_url):
    item = "MacBook"
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=5)
    search_btn = wait.until(EC.visibility_of_element_located(
        MainPage.search_field
    ))
    search_btn.send_keys(item)
    search_btn.send_keys(Keys.ENTER)
    page_title = browser.title.strip()
    assert page_title == "Search - MacBook"


def test_catalog_names_verification(browser, base_url):
    browser.get(base_url)
    catalog = [
        "desktops",  "laptops & notebooks",  "components", "tablets", "software", "phones & pdas", "cameras",
        "mp3 players"
    ]
    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.visibility_of_element_located(
        MainPage.catalog_names
    ))
    catalog_names = browser.find_elements(*MainPage.catalog_names)
    for name in catalog_names:
        name = name.text.strip().lower()
        assert name in catalog, f"Actual catalog name {name} not in expected catalog {catalog}"


def test_macbook_link_verification(browser, base_url):
    item_name = "macbook"
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.visibility_of_element_located(
        MainPage.macbook_link
    ))
    macbook_link = browser.find_element(*MainPage.macbook_link)
    macbook_text = macbook_link.text.strip().lower()
    assert macbook_text == item_name, f"The actual item name {macbook_text} != expected name {item_name}"
