import allure
from hw_7.pages.site_map_page import SiteMapPage


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=information/sitemap'")
@allure.story("Тестирование отображения элементов на Site Map странице")
@allure.title("Проверка отображения breadcrumb страницы")
def test_breadcrumbs_verification(browser, base_url):
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.breadcrumb_visibility_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=information/sitemap'")
@allure.story("Тестирование отображения элементов на Site Map странице")
@allure.title("Проверка отображения заголовка на странице")
def test_header_name_verification(browser, base_url):
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.site_map_header_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=information/sitemap'")
@allure.story("Тестирование отображения элементов на Site Map странице")
@allure.title("Проверка названий ссылок на странице")
def test_link_names_verification(browser, base_url):
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.base_link_names_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=information/sitemap'")
@allure.story("Тестирование отображения элементов на Site Map странице")
@allure.title("Проверка названий ссылок My Account на странице")
def test_my_account_link_names_verification(browser, base_url):
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.my_account_link_names_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb?route=information/sitemap'")
@allure.story("Тестирование отображения элементов на Site Map странице")
@allure.title("Проверка названий Information ссылок на странице")
def test_information_link_names_verification(browser, base_url):
    site_map = SiteMapPage(browser)
    site_map.open_page(base_url)
    site_map.information_link_names_verification()
