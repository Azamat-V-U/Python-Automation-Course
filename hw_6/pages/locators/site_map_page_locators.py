from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class SiteMapLoc:
    breadcrumb_home = (By.XPATH, "//li[@class='breadcrumb-item']/a[contains(@href, 'home')]")
    sitemap_header = (By.XPATH, "(//div[@id='content']/h1)")
    sitemap_links = (By.XPATH, "//div[@class='col-sm-6']/ul/li[a]/a")
    my_account_links = (By.XPATH, "//li[a[contains(text(), 'My Account')]]/ul/li/a")
    information_links = (By.XPATH, "//li[normalize-space(text())='Information']/ul/li/a")
