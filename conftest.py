import os
import pytest
from selenium import webdriver

DRIVERS = os.path.expanduser("~/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://192.168.31.140:8081/")


@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("Browser not found")
    driver.get(url)
    request.addfinalizer(driver.close)
    return driver
