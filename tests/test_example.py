from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_logo_on_main(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#logo"
    )))


def test_check_macbook_page(browser):
    # url/macbook
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Apple")
    ))


def test_check_catalog(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content [title='iPhone']")
    ))


def test_check_admin_page(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[for='input-username']")
    ))


def test_check_user_registration_page(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[name = 'firstname']")
    ))
