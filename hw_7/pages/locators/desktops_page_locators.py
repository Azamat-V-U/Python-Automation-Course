from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class DesktopsLoc:
    desktops_links = (By.XPATH, "(//div[@class='list-group mb-3'])/a")
    breadcrumb_link = (By.XPATH, "(//ul[@class='breadcrumb']//a[contains(text(), 'Desktops')])")
    product_header = (By.XPATH, "//div[@class='col-sm']/h1")
    product_name = (By.XPATH, "(//a[contains(text(), 'Apple Cinema 30')])")
    mac_link = (By.XPATH, "//a[contains(@class, 'list-group-item') and contains(text(), 'Mac')]")
    item_name = (By.XPATH, "(//div[@class='description']//a[contains(text(), 'iMac')])")
