import pytest
import allure
from hw_7.pages.main_page import MainPage
import hw_7.test_data.main_page_data as mp

test_data = mp.MainPageTestData


@allure.epic("Open Cart")
@allure.feature("Домашняя страница 'http://localhost:80'")
@allure.story("Тестирование отображения элементов на домашней страницы")
@allure.title("Проверка отображения кнопки 'add to wish list'")
def test_add_item_to_wishlist_button_verification1(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.add_to_wish_btn_visibility_verification()


@allure.epic("Open Cart")
@allure.feature("Домашняя страница")
@allure.story("Тестирование отображения элементов на домашней страницы")
@allure.title("Проверка отображения pop up сообщения при добавлении в wishlist:незарегистрированный пользователь")
def test_add_item_to_wishlist_message_verification(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.click_add_to_wish_list()
    main_page.message_verification()


@allure.epic("Open Cart")
@allure.feature("Домашняя страница")
@allure.story("Тестирование отображения элементов на домашней страницы")
@allure.title("Проверка отображения pop up сообщения после добавления товара в корзину")
def test_add_item_to_cart(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.click_add_to_cart()
    main_page.product_price_verification()


@allure.epic("Open Cart")
@allure.feature("Домашняя страница")
@allure.story("Тестирование отображения элементов на домашней страницы")
@allure.title("Проверка отображения иконки валюты")
@pytest.mark.parametrize("currency, expected_icon", test_data.currency_data)
def test_select_currency(browser, base_url, currency, expected_icon):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.select_currency(currency=currency)
    main_page.currency_icon_verification(expected_icon)


@allure.epic("Open Cart")
@allure.feature("Домашняя страница")
@allure.story("Тестирование отображения элементов на домашней страницы")
@allure.title("Проверка поиска продукта через строку поиска")
def test_search_for_product(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.enter_macbook()
    main_page.verify_page_title()


@allure.epic("Open Cart")
@allure.feature("Домашняя страница")
@allure.story("Тестирование отображения элементов на домашней страницы")
@allure.title("Проверка отображения названий категорий продуктов в каталоге")
def test_catalog_names_verification(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.catalog_names_verification()


@allure.epic("Open Cart")
@allure.feature("Домашняя страница")
@allure.story("Тестирование отображения элементов на домашней страницы")
@allure.title("Проверка отображения ссылки продукта: MacBook")
def test_macbook_link_verification(browser, base_url):
    main_page = MainPage(browser)
    main_page.open_page(base_url)
    main_page.macbook_link_verification()
