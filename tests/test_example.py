from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_logo_on_main(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#logo"
    )))


def test_check_menu_on_main(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".container #menu"
    )))


def test_check_main_page_title(browser):
    WebDriverWait(browser, 2).until(EC.title_is("Your Store"))


def test_check_main_page_slider(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div.slideshow")
    ))


def test_check_main_page_product_image(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[alt='Canon EOS 5D']")
    ))


def test_check_macbook_page(browser):
    # /macbook
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Apple")
    ))


def test_check_macbook_price(browser):
    price = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div ul h2")
    ))
    assert price.text == '$602.00'


def test_check_macbook_quantity_input(browser):
    input1 = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-quantity")
    ))
    assert input1.is_enabled()




def test_check_catalog(browser):
    # /tablet
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
