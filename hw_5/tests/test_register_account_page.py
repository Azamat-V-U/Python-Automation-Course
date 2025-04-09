from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from hw_5.pages.locators.register_account_locators import RegisterAccount

# --url=http://localhost/en-gb?route=account/register

fake = Faker()


def test_page_header_verification(browser, base_url):
    expected_header = "register account"
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    page_header = wait.until(EC.visibility_of_element_located(
        RegisterAccount.page_header
    ))
    page_header = page_header.text.strip().lower()
    assert page_header == expected_header, f"The actual page header '{page_header}' != expected '{expected_header}'"


def test_link_to_login_page_verification(browser, base_url):
    expected_title = "Account Login"
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    login_link = wait.until(EC.visibility_of_element_located(
        RegisterAccount.login_link
    ))
    login_link.click()
    wait.until(EC.title_is(expected_title))
    page_title = browser.title
    assert page_title == expected_title, f"The actual page title '{page_title}' != expected '{expected_title}'"


def test_register_account_with_valid_credentials(browser, base_url):
    expected_header = "your account has been created!"
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    actions = ActionChains(browser)
    first_name = wait.until(EC.visibility_of_element_located(
        RegisterAccount.first_name
    ))
    last_name = wait.until(EC.visibility_of_element_located(
        RegisterAccount.last_name
    ))
    email = wait.until(EC.visibility_of_element_located(
        RegisterAccount.email
    ))
    password = wait.until(EC.visibility_of_element_located(
        RegisterAccount.password
    ))
    first_name.send_keys(fake.name())
    last_name.send_keys(fake.last_name())
    email.send_keys(fake.email())
    password.send_keys(fake.password())

    privacy_policy_toggle = browser.find_element(*RegisterAccount.privacy_policy_toggle)
    actions.move_to_element(privacy_policy_toggle)
    actions.click(privacy_policy_toggle)
    actions.perform()
    browser.find_element(*RegisterAccount.continue_btn).click()

    wait.until(EC.title_is("Your Account Has Been Created!"))
    page_header = browser.find_element(*RegisterAccount.page_header)
    page_header = page_header.text.strip().lower()
    assert page_header == expected_header, f"The actual page header '{page_header}' != expected '{expected_header}'"


def test_register_account_with_empty_first_name(browser, base_url):
    expected_message = "first name must be between 1 and 32 characters!"
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    actions = ActionChains(browser)
    last_name = wait.until(EC.visibility_of_element_located(
        RegisterAccount.last_name
    ))
    email = wait.until(EC.visibility_of_element_located(
        RegisterAccount.email
    ))
    password = wait.until(EC.visibility_of_element_located(
        RegisterAccount.password
    ))
    last_name.send_keys(fake.last_name())
    email.send_keys(fake.email())
    password.send_keys(fake.password())

    privacy_policy_toggle = browser.find_element(*RegisterAccount.privacy_policy_toggle)
    actions.move_to_element(privacy_policy_toggle)
    actions.click(privacy_policy_toggle)
    actions.perform()
    browser.find_element(*RegisterAccount.continue_btn).click()

    error_message = wait.until(EC.visibility_of_element_located(RegisterAccount.first_name_error_message))
    error_message = error_message.text.strip().lower()
    assert error_message == expected_message, \
        f"The actual error message '{error_message}' != expected '{expected_message}'"


def test_register_account_without_privacy_policy(browser, base_url):
    expected_message = "warning: you must agree to the privacy policy!"
    browser.get(base_url)
    wait = WebDriverWait(browser, timeout=3)
    actions = ActionChains(browser)
    first_name = wait.until(EC.visibility_of_element_located(
        RegisterAccount.first_name
    ))
    last_name = wait.until(EC.visibility_of_element_located(
        RegisterAccount.last_name
    ))
    email = wait.until(EC.visibility_of_element_located(
        RegisterAccount.email
    ))
    password = wait.until(EC.visibility_of_element_located(
        RegisterAccount.password
    ))
    first_name.send_keys(fake.name())
    last_name.send_keys(fake.last_name())
    email.send_keys(fake.email())
    password.send_keys(fake.password())

    continue_btn = browser.find_element(*RegisterAccount.continue_btn)
    actions.move_to_element(continue_btn)
    actions.click(continue_btn)
    actions.perform()

    error_message = wait.until(EC.visibility_of_element_located(
        RegisterAccount.error_message
    ))
    error_message = error_message.text.strip().lower()
    assert error_message == expected_message, \
        f"The actual error message '{error_message}' != expected '{expected_message}'"
