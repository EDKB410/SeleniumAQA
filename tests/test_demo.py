import time
from selenium.webdriver.common.by import By
from pages.login_admin_page import LoginAdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import browser


def test_main_page_title(browser):
    browser.get(browser.url)
    time.sleep(1)
    assert browser.title == "Your Store"


def test_admin_page_title(browser):
    browser.get(f"{browser.url}/administration")
    time.sleep(1)
    assert browser.title == "Administration"


def test_main_page_menu(browser):
    time.sleep(1)  # Пауза для демонстрации
    menu_items = browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def test_check_title(browser):
#     browser.get("https://konflic.github.io/examples/pages/slowlyloading.html")
#     # Можно создать экземляр класса
#     wait = WebDriverWait(browser, 10, poll_frequency=1)
#     # И потом использовать ожидания от него
#     wait.until(EC.title_is("Loaded!"))
#     wait.until(EC.visibility_of_element_located((By.ID, "header")), message='')
#     el = wait.until(EC.visibility_of_element_located((By.ID, "content")))
#     wait.until(EC.text_to_be_present_in_element((By.ID, "content"), "This is else page content."))
#     assert el.text == "This is else page content."


def test_login_page_external(browser):
    wait = WebDriverWait(browser, 5, poll_frequency=1)

    browser.get(browser.url + "/administration")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("user")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami")
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).click()
    wait.until(EC.title_is("Dashboard"))
    percent_orders = wait.until(
        EC.visibility_of_element_located(LoginAdminPage.PERCENT_ORDERS)).text
    print(f"\n{percent_orders}")
    assert percent_orders == "0%", ""

def test_login_page(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(By.ID, "input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.ID, "input-password")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
    time.sleep(2)  # Для демонстрации3
