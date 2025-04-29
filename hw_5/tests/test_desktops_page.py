from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from hw_5.pages.locators.desktops_page_locators import Desktops

# --url=http://localhost/en-gb/catalog/desktops


def test_page_title_verification(browser, base_url):
    expected_title = "desktops"
    browser.get(base_url)
    page_title = browser.title.strip().lower()
    assert page_title == expected_title, f"The actual page title '{page_title}' != expected {expected_title}"


def test_breadcrumb_link_name_verification(browser, base_url):
    browser.get(base_url)
    expected_name = "desktops"
    wait = WebDriverWait(browser, timeout=3)
    breadcrumb_link_name = wait.until(EC.visibility_of_element_located(
        Desktops.breadcrumb_link
    ))
    breadcrumb_link_name = breadcrumb_link_name.text.strip().lower()
    assert breadcrumb_link_name == expected_name, \
        f"The actual link name '{breadcrumb_link_name} != expected '{expected_name}'"


def test_catalog_links_verification(browser, base_url):
    expected_link_names = [
        'desktops (13)', '- pc (0)', '- mac (1)', 'laptops & notebooks (5)', 'components (2)', 'tablets (1)',
        'software (0)', 'phones & pdas (3)', 'cameras (2)', 'mp3 players (4)'
    ]
    browser.get(base_url)
    catalog_link_names = browser.find_elements(*Desktops.desktops_links)
    for link_name in catalog_link_names:
        link_name = link_name.text.strip().lower()
        assert link_name in expected_link_names, \
            f"The actual link_name name '{link_name} != expected {expected_link_names}'"


def test_add_product_to_compare_list(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=4)
    actions = ActionChains(browser)
    product_name = wait.until(EC.visibility_of_element_located(
        Desktops.product_name
    )).text
    product_btn = browser.find_element(*Desktops.product_name)
    actions.move_to_element(product_btn)
    actions.click(product_btn)
    actions.perform()
    product_header = WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located(
        Desktops.product_header
    )).text
    assert product_header == product_name, \
        f"The actual product name '{product_header}' != expected product name '{product_name}'"


def test_product_name_verification(browser, base_url):
    expected_name = "imac"
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=4)
    wait.until(EC.visibility_of_element_located(
        Desktops.mac_link
    ))
    browser.find_element(*Desktops.mac_link).click()
    product_name = wait.until(EC.visibility_of_element_located(
        Desktops.item_name
    ))
    product_name = product_name.text.strip().lower()
    assert product_name == expected_name, f"The actual item name '{product_name}' != expected '{expected_name}'"
