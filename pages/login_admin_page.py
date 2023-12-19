from selenium.webdriver.common.by import By


class LoginAdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_SUCCESS = (By.LINK_TEXT, "logout")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "#input-password")

    PERCENT_ORDERS = (By.XPATH, "//*[text()='Total Orders ']/span[@class='float-end']")
    PERCENT_SALES = (By.XPATH, "//*[text()='Total Sales ']/span[@class='float-end']")
    PERCENT_CUSTOMERS = (By.XPATH, "//*[text()='Total Customers ']/span[@class='float-end']")
    PERSON_LABEL = (By.XPATH, "//span[@class='d-none d-md-inline d-lg-inline']")

    BUTTON_LOGIUT = (By.XPATH, "//span[@class='d-none d-md-inline']")



