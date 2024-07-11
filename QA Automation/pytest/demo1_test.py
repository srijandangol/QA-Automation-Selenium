import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


def test_google_search():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/')

    # Corrected XPath syntax and element selection
    search_box = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    search_box.send_keys("mindrisers.com.np")
    search_box.send_keys(Keys.RETURN)

    # Pause for search results to load
    time.sleep(2)

    # Corrected XPath syntax and element selection
    link = driver.find_element(By.XPATH,
                               "//a[@href='https://mindrisers.com.np/']//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal')]")
    link.click()

    # Pause to allow the new page to load
    time.sleep(5)

    print('Congrats!!!')
    driver.quit()
