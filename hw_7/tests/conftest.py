import allure
import datetime
import os
import pytest
import logging
import re
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption(
        "--url",
        # default="http://host.docker.internal:80",
        default="http://192.168.0.105/",
        help="This is the base url"
    )
    parser.addoption(
        "--maximize",
        action="store_true",
        help="This is maximize window configuration"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="This is the headless configuration"
    )
    parser.addoption("--bv")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--runner", action="store_true")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    runner = request.config.getoption("--runner")
    log_level = request.config.getoption("--log_level").upper()
    executor = request.config.getoption("--executor")
    maximize = request.config.getoption("--maximize")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")

    test_name = request.node.name
    safe_test_name = re.sub(r'[^\w\-_. ]', '_', test_name)
    log_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{safe_test_name}.log")

    logger = logging.getLogger(safe_test_name)

    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S'))

    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (safe_test_name, datetime.datetime.now()))

    capabilities = {
        "browserName": browser,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": os.getenv("BUILD_NUMBER",
                              str(random.randint(9000, 10000))),
            "screenResolution": "1280x1024x24",
            "applicationContainers": [" python-automation-course-opencart-1:opencart", "python-automation-course-mariadb-1:mariadb"],
            "additionalNetworks": ["selenoid_net"],
            "enableVideo": True,
            "timeZone": "Europe/Moscow",
            "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC-ALL=ru_RU.UTF-8"]
        },
        "acceptInsecureCerts": True
    }

    driver = None
    if runner:
        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        elif browser == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError("Browser name must be either 'chrome', 'firefox' or 'edge'")
    else:
        if browser == "chrome":
            options = ChromeOptions()
        elif browser == "firefox":
            options = FirefoxOptions()
        elif browser == "edge":
            options = EdgeOptions()
        else:
            raise ValueError("Browser name must be either 'chrome', 'firefox' or 'edge'")

        if headless:
            options.add_argument("--headless")

        for k, v in capabilities.items():
            options.set_capability(k, v)

        executor_url = f"http://{executor}:4444/wd/hub"
        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    if maximize:
        driver.maximize_window()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = safe_test_name

    logger.info("Browser %s started" % browser)

    def fin():
        if request.node.status == "failed":
            allure.attach(
                name=f"{safe_test_name}_screenshot",
                body=driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )

        driver.quit()
        logger.info("===> Test %s finished at %s" % (safe_test_name, datetime.datetime.now()))

    request.addfinalizer(fin)
    yield driver
