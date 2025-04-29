import pytest
import allure
from hw_7.pages.admin_page import AdminPage
from hw_7.test_data.admin_page_data import AdminPageData


@allure.epic("Open Cart")
@allure.feature("Админка Open Cart 'http://localhost/administration/'")
@allure.story("Возможность добавления нового продукта")
@allure.title("Добавления нового продукта")
@pytest.mark.parametrize("product_name, meta, model, default", AdminPageData.new_product_data)
def test_add_product(browser, base_url, product_name, meta, model, default):
    admin_page = AdminPage(browser)
    admin_page.open_page(base_url)
    admin_page.login_page()
    admin_page.add_new_product(product=product_name, meta=meta, model=model, default=default)
    admin_page.message_verification()
    admin_page.logout_page()


@allure.epic("Open Cart")
@allure.feature("Админка Open Cart 'http://localhost/administration/'")
@allure.story("Возможность удаления продукта")
@allure.title("Удаление продукта")
@pytest.mark.parametrize("product_name", AdminPageData.product_name)
def test_delete_product(browser, base_url, product_name):
    admin_page = AdminPage(browser)
    admin_page.open_page(base_url)
    admin_page.login_page()
    admin_page.delete_product(product_name)
    admin_page.message_verification()
    admin_page.logout_page()
