from selenium.webdriver.common.by import By


class MainPage:
    add_to_wishlist = (By.XPATH, "//div[@class='col mb-3'][1]//button[@type='submit'][2]")
    actual_message = (By.CSS_SELECTOR, ".alert-dismissible")
    add_to_cart_btn = (By.XPATH, "//div[@class='col mb-3'][1]//button[@type='submit'][1]")
    dropdown = (By.CSS_SELECTOR, ".btn-block.dropdown-toggle")
    pound_sterling_currency = (By.XPATH, "//ul[@class='dropdown-menu show']/li[2]")
    pound_sterling_sign = (By.XPATH, "//div[@class='dropdown']/a[1]")
    catalog_names = (By.XPATH, "(//ul[@class='nav navbar-nav']/li)")
    macbook_link = (By.XPATH, "(//h4/a[@href='http://localhost/en-gb/product/macbook'])")
