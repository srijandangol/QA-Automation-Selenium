# Import the necessary modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the website URL and open it
website_url = 'https://demoqa.com/automation-practice-form'
driver.get(website_url)
time.sleep(2)

# Maximize the window
driver.maximize_window()
time.sleep(2)

# Find the specific location using the locators
gender = driver.find_element(By.XPATH, "//input[@id='gender-radio-1']").is_selected()
print(gender)
driver.find_element(By.XPATH, "//input[@id='gender-radio-1']").click()
gender = driver.find_element(By.XPATH, "//input[@id='gender-radio-1']").is_selected()
print(gender)

# Close the WebDriver
driver.close()
driver.quit()
