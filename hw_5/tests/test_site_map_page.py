from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_5.pages.locators.site_map_page_locators import SiteMap

# --url=http://localhost/en-gb?route=information/sitemap


def test_breadcrumbs_verification(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.visibility_of_element_located(
        SiteMap.breadcrumb
    ))
    breadcrumb_link = browser.find_element(*SiteMap.breadcrumb_link)
    assert breadcrumb_link.is_displayed() == True


def test_header_name_verification(browser, base_url):
    browser.get(base_url)
    expected_header = "site map"
    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.visibility_of_element_located(
        SiteMap.sitemap_header
    ))
    sitemap_header = browser.find_element(*SiteMap.sitemap_header).text.lower()
    assert sitemap_header == expected_header, f"The actual sitemap header '{sitemap_header}' != {expected_header}"


def test_item_names_1(browser, base_url):
    expected_link_list = [
        "desktops", "laptops & notebooks", "components", "tablets",
        "software", "phones & pdas", "cameras", "mp3 players"
    ]
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.visibility_of_element_located(
        SiteMap.catalog_links1
    ))
    catalog_links = browser.find_elements(*SiteMap.catalog_links1)
    for link in catalog_links:
        link = link.text.strip().lower()
        assert link in expected_link_list, f"The actual link name '{link}' not in expected items {expected_link_list}"


def test_item_names_2(browser, base_url):
    expected_link_list = [
        "special offers", "my account", "shopping cart", "checkout", "search"
    ]
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.visibility_of_element_located(
        SiteMap.catalog_links2
    ))
    catalog_links = browser.find_elements(*SiteMap.catalog_links2)
    for link in catalog_links:
        link = link.text.strip().lower()
        assert link in expected_link_list, f"The actual link name '{link}' not in expected items {expected_link_list}"


def test_my_account_link_names_verification(browser, base_url):
    expected_link_list = [
        "account information", "password", "address book", "order history", "downloads"
    ]
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=5)
    wait.until(EC.visibility_of_element_located(
        SiteMap.my_account_links
    ))
    my_account_links = browser.find_elements(*SiteMap.my_account_links)
    for link in my_account_links:
        link = link.text.strip().lower()
        assert link in expected_link_list, f"The actual link name '{link}' not in expected items {expected_link_list}"


def test_information_link_names_verification(browser, base_url):
    expected_link_list = [
        "terms & conditions", "delivery information", "about us", "privacy policy", "contact us"
    ]
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=4)
    wait.until(EC.visibility_of_element_located(
        SiteMap.information_list
    ))
    catalog_links = browser.find_elements(*SiteMap.information_links)
    link_name_list = [link.text.lower().strip() for link in catalog_links]
    assert link_name_list == expected_link_list, \
        f"The actual link list '{link_name_list}' != expected {expected_link_list}"
