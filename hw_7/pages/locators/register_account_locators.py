from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class RegisterAccountLoc:
    privacy_policy_toggle = (By.NAME, "agree")
    error_message = (By.CSS_SELECTOR, ".alert-dismissible")
    page_header = (By.XPATH, "//div[@id='content']/h1")
    first_name_error_message = (By.ID, "error-firstname")
    login_link = (By.XPATH, "//div[@id='content']//a[contains(text(),'login page')]")
    first_name = (By.NAME, "firstname")
    last_name = (By.NAME, "lastname")
    email = (By.NAME, "email")
    password = (By.NAME, "password")
    continue_btn = (By.XPATH, "//button[@type='submit']")
