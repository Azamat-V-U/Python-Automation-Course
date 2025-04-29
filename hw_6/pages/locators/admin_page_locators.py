from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class AdminPageLoc:
    username = (By.ID, "input-username")
    password = (By.ID, "input-password")
    catalog = (By.XPATH, "//a[@href='#collapse-1' and contains(text(), 'Catalog')]")
    products = (By.XPATH, "//a[contains(text(), 'Products')]")
    hidden_btn = (By.XPATH, "//button[@title='Filter']")
    add_new_btn = (By.XPATH, "//a[@title='Add New']")
    product_name = (By.ID, "input-name-1")
    # meta_tag_title = (By.ID, "input-meta-title-1")
    meta_tag_title = (By.XPATH, "//input[@id='input-meta-title-1']")
    # data_tab = (By.XPATH, "//a[contains(@href, '#tab-data') and contains(text(), 'Data')]")
    data_tab = (By.XPATH, "//a[contains(@role, 'tab') and contains(text(), 'Data')]")
    model = (By.ID, "input-model")
    seo_tab = (By.XPATH, "//a[contains(@href, '#tab-seo') and contains(text(), 'SEO')]")
    default = (By.ID, "input-keyword-0-1")
    save_btn = (By.XPATH, "//button[@type='submit']")
    message = (By.CSS_SELECTOR, ".alert-dismissible")
    logout = (By.XPATH, "//span[@class='d-none d-md-inline']")
    product_name_filter = (By.ID, "input-name")
    filter_btn = (By.ID, "button-filter")
    arrow_link = (By.XPATH, "//a[contains(@class,'page-link') and contains(text(), '>|')]")
    checkbox = (By.XPATH, "//tr[td[contains(text(), 'My apple')]]//input[@type='checkbox']")
    delete_btn = (By.CSS_SELECTOR, ".btn.btn-danger")
