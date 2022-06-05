import os
import pytest
from selenium import webdriver

DRIVERS = os.path.expanduser("~/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="chrome browser")


@pytest.fixture(scope="module")
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    elif browser_name == "safari":
        browser = webdriver.Safari()
    else:
        raise ValueError("Browser not found")
    request.addfinalizer(browser.close)
    return browser
