import time

from percy import percy_snapshot
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_tesla_homepage_snapshot():
    browser = webdriver.Chrome()
    try:
        browser.get("https://tesla.com")
        WebDriverWait(browser, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        time.sleep(5)
        percy_snapshot(browser, "Tesla Homepage")
    finally:
        browser.quit()
