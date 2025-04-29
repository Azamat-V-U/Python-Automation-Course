import pytest
from hw_6.pages.locators.main_page_locators import MainPageLoc
from hw_6.pages.main_page import MainPage


def test_add_item_to_wishlist_button_verification1(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.element_visibility_verification(MainPageLoc.add_to_wishlist)


def test_add_item_to_wishlist_message_verification(browser, base_url):
    expected_message = "you must login or create an account to save macbook to your wish list!"
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.click_element(MainPageLoc.add_to_wishlist)
    main_page.text_verification(MainPageLoc.actual_message, expected_message)


def test_add_item_to_cart(browser, base_url):
    expected_text = "1 item(s) - $602.00"
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.click_element(MainPageLoc.add_to_cart_btn)
    main_page.product_price_verification(MainPageLoc.dropdown, expected_text)


@pytest.mark.parametrize("currency, expected_sign", [
    ("pound_sterling", "£ currency"),
    ("dollar", "$ currency"),
    ("euro", "€ currency")
])
def test_select_currency(browser, base_url, currency, expected_sign):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.select_currency(currency=currency)
    main_page.text_verification(MainPageLoc.currency_sign, expected_sign)


def test_search_for_product(browser, base_url):
    expected_title = "MacBook"
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.get_element(MainPageLoc.search_field)
    main_page.enter_value(MainPageLoc.search_field, expected_title, enter=True)
    main_page.page_title_verification(expected_title)


def test_catalog_names_verification(browser, base_url):
    expected_catalog_items = [
        "desktops", "laptops & notebooks", "components", "tablets", "software", "phones & pdas", "cameras",
        "mp3 players"
    ]
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.catalog_names_verification(MainPageLoc.catalog_names, expected_catalog_items)


def test_macbook_link_verification(browser, base_url):
    item_name = "macbook"
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.text_verification(MainPageLoc.macbook_link, item_name)
