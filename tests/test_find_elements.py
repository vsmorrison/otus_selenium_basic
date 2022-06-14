from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# main page
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


# macbook page
def test_check_macbook_page(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Apple")
    ))


def test_check_macbook_price(browser):
    price = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div ul h2")
    ))
    assert price.text == '$602.00'


def test_check_macbook_quantity_input(browser):
    q_input = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#input-quantity")
    ))
    assert q_input.is_enabled()


def test_check_macbook_tabs(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".nav-tabs")
    ))
    tabs = browser.find_elements(By.CSS_SELECTOR, '.nav-tabs li')
    for tab in tabs:
        assert tab.text in ['Description', 'Specification', 'Reviews (0)']


def test_add_macbook_to_cart(browser):
    button = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button#button-cart")
    ))
    button.click()
    alert = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    ))
    assert alert.text == \
           'Success: You have added MacBook to your shopping cart!\n×'


# catalog/smartphone
def test_check_catalog_name(browser):
    cat_name = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "h2")
    ))
    assert cat_name.text == 'Phones & PDAs'


def test_check_catalog_breadcrumb(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".breadcrumb")
    ))
    breadcrumbs = browser.find_elements(
        By.CSS_SELECTOR, '#product-category .breadcrumb a'
    )
    assert breadcrumbs[1].text == 'Phones & PDAs'


def test_check_catalog_title(browser):
    WebDriverWait(browser, 3).until(EC.title_is('Phones & PDAs'))


def test_check_catalog_items(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content")
    ))
    smartphones = browser.find_elements(By.CSS_SELECTOR, '#content .caption a')
    for smartphone in smartphones:
        assert smartphone.text in ['HTC Touch HD', 'iPhone', 'Palm Treo Pro']


def test_check_catalog_add_to_cart(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content")
    ))
    add_to_cart_buttons = browser.find_elements(
        By.CSS_SELECTOR, '.button-group button span'
    )
    add_to_cart_buttons[0].click()
    alert = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    ))
    assert alert.text == \
           'Success: You have added HTC Touch HD to your shopping cart!\n×'


# admin page
def test_check_admin_page(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[for='input-username']")
    ))


def test_check_admin_page_title(browser):
    WebDriverWait(browser, 3).until(EC.title_is('Administration'))


def test_check_admin_page_heading(browser):
    heading = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".panel-heading")
    ))
    assert heading.text == 'Please enter your login details.'


def test_check_admin_page_password_recovery(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Forgotten Password")
    ))


def test_check_admin_page_button_enabled(browser):
    button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button")
    ))
    assert button.is_enabled()


# user registration page
def test_check_user_registration_page_username_input(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[name = 'firstname']")
    ))


def test_check_user_registration_page_title(browser):
    WebDriverWait(browser, 2).until(EC.title_is('Register Account'))


def test_check_user_registration_page_checkbox(browser):
    checkbox = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "[type='checkbox']")
    ))
    assert checkbox.get_attribute("value") == '1'


def test_check_user_registration_page_breadcrumb(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".breadcrumb")
    ))
    breadcrumbs = browser.find_elements(
        By.CSS_SELECTOR, '.breadcrumb li'
    )
    assert breadcrumbs[1].text == 'Account'
    assert breadcrumbs[2].text == 'Register'


def test_check_user_registration_page_legends(browser):
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content")
    ))
    legends = browser.find_elements(By.CSS_SELECTOR, 'legend')
    for legend in legends:
        assert legend.text in ['Your Personal Details',
                               'Your Password',
                               'Newsletter']
