from selenium.webdriver.common.by import By


class MainPage:
    add_to_wishlist = (
        By.XPATH, "//div[contains(@class, 'product-thumb')][.//a[text()='MacBook']]//i[@class='fa-solid fa-heart']"
    )
    actual_message = (By.CSS_SELECTOR, ".alert-dismissible")
    add_to_cart_btn = (
        By.XPATH, "//div[contains(@class, 'product-thumb')][.//a[text()='MacBook']]"
                  "//i[@class='fa-solid fa-shopping-cart']"
    )
    dropdown = (By.CSS_SELECTOR, ".btn-block.dropdown-toggle")
    pound_sterling_currency = (By.XPATH, "//li/a[@href='GBP']")
    pound_sterling_sign = (By.XPATH, "//a[contains(@href,'#') and contains(@class,'dropdown-toggle')]")
    search_field = (By.CSS_SELECTOR, ".form-control-lg")
    catalog_names = (By.XPATH, "(//ul[@class='nav navbar-nav']/li)")
    macbook_link = (By.XPATH, "//a[contains(text(), 'MacBook')]")
