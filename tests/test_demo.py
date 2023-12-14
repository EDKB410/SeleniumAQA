import time

def test_main_page_title(browser):
    browser.get(browser.url)
    time.sleep(1)
    assert browser.title == "Your Store"

def test_admin_page_title(browser, base_url):
    browser.get(f"{base_url}/administration")
    time.sleep(1)
    assert browser.title == "Administration"