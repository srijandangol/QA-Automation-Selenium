import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # Yield the webdriver instance
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("malikacounter5", "password"), # valid username and password
    ("malikacounter", "password"),  # invalid username and password
    ("1", "pa"),                    # invalid username and password
    ("user", ""),                   # invalid username and password
])
def test_login(driver, username, password):
    driver.get("https://tax.digitalpalika.org/login")
    username_field = driver.find_element(By.XPATH, "//input[@id='username']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
    username_field.send_keys(username)
    password_field.send_keys(password)
    time.sleep(2)
    login_button.click()

    # Adding a small delay
    time.sleep(2)

    page_source = driver.page_source

    if "Successfully login!" in page_source:
        print(f"Login Successfully for {username}")
    else:
        print(f"Incorrect username and Password {username}")
