import pytest
from hw_6.pages.admin_page import AdminPage
from hw_6.pages.locators.admin_page_locators import AdminPageLoc


@pytest.mark.parametrize("product, meta, model, default", [
    ("My apple", "meta apple", "12345", "moby"),
    ("My phone", "phone meta", "yund", "word"),
    ("My device", "meta device", "1234Io5", "link")
])
def test_add_product(browser, base_url, product, meta, model, default):
    admin_page = AdminPage(browser)
    admin_page.open_page(base_url)
    admin_page.login_page()
    admin_page.add_new_product(product=product, meta=meta, model=model, default=default)
    admin_page.text_verification(AdminPageLoc.message, "success: you have modified products!")
    admin_page.logout_page(AdminPageLoc.logout)


@pytest.mark.parametrize("product_name", [
    'My apple',
    'My phone',
    'My device'
])
def test_delete_product(browser, base_url, product_name):
    admin_page = AdminPage(browser)
    admin_page.open_page(base_url)
    admin_page.login_page()
    admin_page.delete_product(product_name)
    admin_page.text_verification(AdminPageLoc.message, "success: you have modified products!")
    admin_page.logout_page(AdminPageLoc.logout)
