import allure
from hw_7.pages.desktops_page import DesktopsPage


@allure.epic("Open Cart")
@allure.feature("Descktops 'http://localhost/en-gb/catalog/desktops'")
@allure.story("Тестирование отображения элементов на Desctops странице")
@allure.title("Проверка названия страницы")
def test_page_title_verification(browser, base_url):
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.desktops_page_title_verification()


@allure.epic("Open Cart")
@allure.feature("Descktops 'http://localhost/en-gb/catalog/desktops'")
@allure.story("Тестирование отображения элементов на Desctops странице")
@allure.title("Проверка названия breadcrumb на странице")
def test_breadcrumb_link_name_verification(browser, base_url):
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.breadcrumb_name_verification()


@allure.epic("Open Cart")
@allure.feature("Descktops 'http://localhost/en-gb/catalog/desktops'")
@allure.story("Тестирование отображения элементов на Desctops странице")
@allure.title("Проверка названия ссылок каталога на странице")
def test_catalog_links_verification(browser, base_url):
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.link_names_verification()


@allure.epic("Open Cart")
@allure.feature("Descktops 'http://localhost/en-gb/catalog/desktops'")
@allure.story("Тестирование отображения элементов на Desctops странице")
@allure.title("Переход в карточку продукта")
def test_view_product(browser, base_url):
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.click_product_name("apple cinema 30")
    desktop_page.product_header_verification()


@allure.epic("Open Cart")
@allure.feature("Descktops 'http://localhost/en-gb/catalog/desktops'")
@allure.story("Тестирование отображения элементов на Desctops странице")
@allure.title("Переход по ссылке в категорию продуктов")
def test_product_name_verification(browser, base_url):
    desktop_page = DesktopsPage(browser)
    desktop_page.open_page(base_url)
    desktop_page.click_product_name("mac")
    desktop_page.product_name_verification()
