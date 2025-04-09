from selenium.webdriver.common.by import By


class SiteMap:
    breadcrumb = (By.XPATH, "//ul[@class='breadcrumb']/li[1]")
    breadcrumb_link = (By.XPATH, "//ul[@class='breadcrumb']/li[1]/a")
    sitemap_header = (By.XPATH, "(//div[@id='content']/h1)")
    catalog_links1 = (By.XPATH, "(//div[@class='col-sm-6'][1]/ul/li/a)")
    catalog_links2 = (By.XPATH, "(//div[@class='col-sm-6'][2]/ul/li/a)")
    my_account_links = (By.XPATH, "//div[@class='col-sm-6'][2]/ul/li[2]/ul/li")
    information_list = (By.XPATH, "//div[@class='col-sm-6'][1]/ul/li/a")
    information_links = (By.XPATH, "//div[@class='col-sm-6'][2]/ul/li[6]/ul/li")
