# Import the necessary modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
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
first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
last_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
gender = driver.find_element(By.XPATH, "//input[@id='gender-radio-1']")
phone = driver.find_element(By.XPATH, "//input[@id='userNumber']")
dob = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
subjects = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
hobbies = driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-1']")
address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
state_dropdown = driver.find_element(By.XPATH, "//div[@id='state']")
city_dropdown = driver.find_element(By.XPATH, "//div[@id='city']")
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")

# Fill in the form elements
first_name.send_keys('Ram')
last_name.send_keys('Shyam')
email.send_keys('Ram_Shyam@gmail.com')
driver.execute_script("arguments[0].click();", gender)
phone.send_keys('9876543210')
dob.clear()
dob.send_keys('10 Nov 2000')
dob.send_keys(Keys.RETURN)
subjects.send_keys('Maths')
subjects.send_keys(Keys.RETURN)
driver.execute_script("arguments[0].click();", hobbies)
address.send_keys('Kathmandu')

# Select state and city
wait = WebDriverWait(driver, 10)
state_dropdown.click()
state_option = driver.find_element(By.XPATH, "//div[contains(text(), 'NCR')]")
state_option.click()

time.sleep(5)  # Adding a small delay to ensure the city dropdown is loaded

city_dropdown.click()
city_option = driver.find_element(By.XPATH, "//div[contains(text(), 'Delhi')]")
city_option.click()

# Click the submit button
submit_button.click()

# Wait for a few seconds to observe the result
time.sleep(5)

# Close the WebDriver
driver.quit()

