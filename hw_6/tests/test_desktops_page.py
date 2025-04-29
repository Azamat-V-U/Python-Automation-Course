from hw_6.pages.locators.desktops_page_locators import DesktopsLoc
from hw_6.pages.desktops_page import DesktopsPage

# --url=http://localhost/en-gb/catalog/desktops


def test_page_title_verification(browser, base_url):
    expected_title = "Desktops"
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.page_title_verification(expected_title)


def test_breadcrumb_link_name_verification(browser, base_url):
    expected_name = "desktops"
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.text_verification(DesktopsLoc.breadcrumb_link, expected_name)


def test_catalog_links_verification(browser, base_url):
    expected_link_names = [
        'desktops (13)', '- pc (0)', '- mac (1)', 'laptops & notebooks (5)', 'components (2)', 'tablets (1)',
        'software (0)', 'phones & pdas (3)', 'cameras (2)', 'mp3 players (4)'
    ]
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.catalog_names_verification(DesktopsLoc.desktops_links, expected_link_names)


def test_add_product_to_compare_list(browser, base_url):
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    product_name = desktop_page.get_element_text
    desktop_page.click_element(DesktopsLoc.product_name)
    desktop_page.text_verification(DesktopsLoc.product_header, product_name)


def test_product_name_verification(browser, base_url):
    expected_name = "imac"
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.click_element(DesktopsLoc.mac_link)
    desktop_page.text_verification(DesktopsLoc.item_name, expected_name)
