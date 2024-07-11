import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from POM.pages.login_page import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # yield the webdriver instance
    yield driver
    # close the webdriver instance
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://tax.digitalpalika.org/login")
    time.sleep(1)
    login_page.enter_username("malikacounter5")
    time.sleep(1)
    login_page.enter_password("password")
    time.sleep(2)
    login_page.click_login()
    time.sleep(1)
