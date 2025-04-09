from selenium.webdriver.common.by import By


class Desktops:
    desktops_links = (By.XPATH, "(//div[@class='list-group mb-3'])/a")
    breadcrumb_link = (By.XPATH, "(//ul[@class='breadcrumb']//a[contains(text(), 'Desktops')])")
    product_header = (By.TAG_NAME, "h1")
    product_name = (By.XPATH, "(//a[contains(text(), 'Apple Cinema 30')])")
    mac_button = (By.XPATH, "//div[@class='list-group mb-3']/a[3]")
    item_name = (By.XPATH, "(//div[@class='description']//a[contains(text(), 'iMac')])")
