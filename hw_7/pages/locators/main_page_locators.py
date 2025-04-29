from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class MainPageLoc:
    add_to_wishlist = (By.XPATH, "//h4[a[contains(text(), 'MacBook')]]/following::i[2]")
    actual_message = (By.CSS_SELECTOR, ".alert-dismissible")
    add_to_cart_btn = (By.XPATH, "//h4[a[contains(text(), 'MacBook')]]/following::i[1]")
    dropdown = (By.CSS_SELECTOR, ".btn-block.dropdown-toggle")
    currency_dropdown = (By.ID, "form-currency")
    euro_currency = (By.XPATH, "//li/a[@href='EUR']")
    pound_sterling_currency = (By.XPATH, "//li/a[@href='GBP']")
    dollar_currency = (By.XPATH, "//li/a[@href='USD']")
    currency_icon = (By.XPATH, "//a[contains(@href,'#') and contains(@class,'dropdown-toggle')]")
    search_field = (By.CSS_SELECTOR, ".form-control-lg")
    catalog_products = (By.XPATH, "(//ul[@class='nav navbar-nav']/li)")
    macbook_link = (By.XPATH, "//a[contains(text(), 'MacBook')]")
