import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="http://localhost:80",
        help="This is the base url"
    )
    parser.addoption(
        "--browser",
        default="chrome",
        help="This is the browser configuration"
    )
    parser.addoption(
        "--maximize",
        action="store_true",
        help="This is maximize window configuration"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    if browser_name == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError("Browser name must be either 'chrome', 'firefox' or 'edge'")
    if maximize:
        driver.maximize_window()
    yield driver
    driver.quit()
