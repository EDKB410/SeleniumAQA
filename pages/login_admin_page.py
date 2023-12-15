from selenium.webdriver.common.by import By


class LoginAdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_SUCCESS = (By.LINK_TEXT, "logout")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    TOTAL_ORDERS = (By.CLASS_NAME, "tile-heading")
    PERCENT_ORDERS = (By.XPATH, "//*[text()='Total Orders ']/span[@class='float-end']")
