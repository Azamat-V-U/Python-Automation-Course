import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_5.pages.locators.login_page_locators import LoginPage
from dotenv import load_dotenv


# --url=http://localhost/en-gb?route=account/login

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def test_login_button_verification(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    wait.until(EC.title_is("Account Login"))
    login_btn = wait.until(EC.visibility_of_element_located(
        LoginPage.login_btn
    ))
    assert login_btn.is_enabled(), f"The 'login' button isn't active"


def test_email_field_placeholder_verification(browser, base_url):
    expected_placeholder = "e-mail address"
    browser.get(base_url)
    email_field = WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located(
        LoginPage.email_field
    ))
    actual_placeholder = email_field.get_attribute("placeholder").strip().lower()
    assert actual_placeholder == expected_placeholder, \
        f"The actual placeholder '{actual_placeholder}' != expected '{expected_placeholder}'"


def test_password_field_placeholder_verification(browser, base_url):
    expected_placeholder = "password"
    browser.get(base_url)
    password_field = WebDriverWait(browser, timeout=3).until(EC.visibility_of_element_located(
        LoginPage.password_field
    ))
    actual_placeholder = password_field.get_attribute("placeholder").strip().lower()
    assert actual_placeholder == expected_placeholder, \
        f"The actual placeholder '{actual_placeholder}' != expected '{expected_placeholder}'"


def test_login_with_valid_credentials(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    email_field = wait.until(EC.visibility_of_element_located(
        LoginPage.email_field
    ))
    password_field = wait.until(EC.visibility_of_element_located(
        LoginPage.password_field
    ))
    login_btn = wait.until(EC.visibility_of_element_located(
        LoginPage.login_btn
    ))
    email_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)
    login_btn.click()
    page_title = wait.until(EC.title_is("My Account"))
    assert page_title == True, f"The actual page title  != expected 'My Account'"


def test_login_with_invalid_credentials(browser, base_url):
    expected_message = "warning: no match for e-mail address and/or password."
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    email_field = wait.until(EC.visibility_of_element_located(
        LoginPage.email_field
    ))
    password_field = wait.until(EC.visibility_of_element_located(
        LoginPage.password_field
    ))
    login_btn = wait.until(EC.visibility_of_element_located(
        LoginPage.login_btn
    ))
    email_field.send_keys("test@@mail.ru")
    password_field.send_keys("jhjklhRt!")
    login_btn.click()
    actual_message = wait.until(EC.visibility_of_element_located(
        LoginPage.error_message
    ))
    actual_message = actual_message.text.strip().lower()
    assert actual_message == expected_message, f"The actual message '{actual_message}' != expected '{expected_message}'"
