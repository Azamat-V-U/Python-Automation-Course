import allure
from hw_7.pages.product_page import ProductPage


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb/product/apple-cinema'")
@allure.story("Тестирование отображения элементов на странице продукта")
@allure.title("Проверка названия страницы")
def test_page_title_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.product_tittle_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb/product/apple-cinema'")
@allure.story("Ввод текста в поле")
@allure.title("Проверка ввода текста в поле")
def test_text_area_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.enter_in_text_area()
    product_page.text_area_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb/product/apple-cinema'")
@allure.story("Тестирование отображения элементов на странице продукта")
@allure.title("Проверка отображения конпки add to cart")
def test_add_to_cart_button_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.add_to_cart_btn_verification()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb/product/apple-cinema'")
@allure.story("Выбор значений")
@allure.title("Проверка выбора значений в дропдаун")
def test_dropdown_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.select_dropdown_options()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb/product/apple-cinema'")
@allure.story("Выбор значений")
@allure.title("Проверка выбора чекбоксов")
def test_checkboxes_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.select_all_checkboxes()


@allure.epic("Open Cart")
@allure.feature("Login 'http://localhost/en-gb/product/apple-cinema'")
@allure.story("Выбор чекбоксов")
@allure.title("Проверка выбора радиобатонов")
def test_radio_buttons_verification(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open_page(base_url)
    product_page.select_all_radio_buttons()
