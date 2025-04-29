from hw_6.pages.locators.site_map_page_locators import SiteMapLoc
from hw_6.pages.site_map_page import SiteMapPage

# --url=http://localhost/en-gb?route=information/sitemap


def test_breadcrumbs_verification(browser, base_url):
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.element_visibility_verification(SiteMapLoc.breadcrumb_home)


def test_header_name_verification(browser, base_url):
    expected_header = "site map"
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.text_verification(SiteMapLoc.sitemap_header, expected_header)


def test_link_names_verification(browser, base_url):
    expected_link_list = [
        "desktops", "laptops & notebooks", "components", "tablets",
        "software", "phones & pdas", "cameras", "mp3 players",
        "special offers", "my account", "shopping cart", "checkout", "search"
    ]
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.catalog_names_verification(SiteMapLoc.sitemap_links, expected_link_list)


def test_my_account_link_names_verification(browser, base_url):
    expected_link_list = [
        "account information", "password", "address book", "order history", "downloads"
    ]
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.catalog_names_verification(SiteMapLoc.my_account_links, expected_link_list)


def test_information_link_names_verification(browser, base_url):
    expected_link_list = [
        "terms & conditions", "delivery information", "about us", "privacy policy", "contact us"
    ]
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.catalog_names_verification(SiteMapLoc.information_links, expected_link_list)
