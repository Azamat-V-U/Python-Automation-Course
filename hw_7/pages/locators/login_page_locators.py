from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class LoginPageLoc:
    login_btn = (By.XPATH, "(//button[@type='submit'])")
    email_field = (By.CSS_SELECTOR, "[placeholder='E-Mail Address']")
    password_field = (By.CSS_SELECTOR, "[placeholder='Password']")
    error_message = (By.CSS_SELECTOR, ".alert-dismissible")
