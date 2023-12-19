import time
import pytest
from selenium.webdriver.common.by import By
from pages.login_admin_page import LoginAdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import browser


class TestAdminPage(LoginAdminPage):

    @pytest.fixture()
    def setupclass(self, browser):
        browser.get(browser.url + "/administration")
        browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("user")
        browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami")
        browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).submit()

    def test_main_page_title(self, browser):
        browser.get(browser.url)
        time.sleep(1)
        assert browser.title == "Your Store"

    def test_admin_page_title(self, browser):
        browser.get(f"{browser.url}/administration")
        time.sleep(1)
        assert browser.title == "Administration"

    def test_main_page_menu(self, browser):
        time.sleep(1)  # Пауза для демонстрации
        menu_items = browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")
        assert len(menu_items) == 8, "Неверное количество элементов меню"

    def test_login_page_admin(self, browser):
        wait = WebDriverWait(browser, 5, poll_frequency=1)

        wait.until(EC.title_is("Dashboard"))
        browser.find_element(*LoginAdminPage.PERSON_LABEL)
        browser.find_element(*LoginAdminPage.BUTTON_LOGIUT)
        assert_percent = "Счетчик процентов работает некорректно! Значение превышает 100%"

        percent_orders = wait.until(
            EC.visibility_of_element_located(LoginAdminPage.PERCENT_ORDERS)).text
        assert percent_orders >= "5%", assert_percent

        percent_sales = wait.until(
            EC.visibility_of_element_located(LoginAdminPage.PERCENT_SALES)).text
        assert percent_sales >= "5%", assert_percent

        percent_customers = wait.until(
            EC.visibility_of_element_located(LoginAdminPage.PERCENT_CUSTOMERS)).text
        assert percent_customers >= "5%", assert_percent

        browser.find_element(*LoginAdminPage.BUTTON_LOGIUT).click()
        # time.sleep(5)

    def test_login_page(self, browser):
        browser.get(browser.url + "/administration")
        browser.find_element(By.ID, "input-username")
        browser.find_element(By.NAME, "password")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        browser.find_element(By.ID, "input-password")
        browser.find_element(By.XPATH, "//*[text()='OpenCart']")
        time.sleep(2)  # Для демонстрации3
