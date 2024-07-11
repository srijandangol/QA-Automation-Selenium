#path locator create/ post method
#import The necessary module
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Set the Chrome Web Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website_url='https://mindrisers.com.np/' #defining the website
driver.get(website_url) #opening website
time.sleep(2)

# Maximize the window
driver.maximize_window()
time.sleep(2)

driver.get('https://mindrisers.com.np/contact-us')

# Find the specific location using the locators
full_name = driver.find_element(By.XPATH,"//input[@placeholder='Name']")
email = driver.find_element(By.XPATH,"//input[@placeholder='Email']")
phone = driver.find_element(By.XPATH,"//input[@placeholder='Phone']")
subject = driver.find_element(By.XPATH,"//input[@placeholder='Subject']")
any_queries = driver.find_element(By.XPATH,"//textarea[@placeholder='Queries']")

# Fill in the form elements
full_name.send_keys('Ram Shyam')
email.send_keys('Ram_Shyam@gmail.com')
phone.send_keys('9876543210')
subject.send_keys('Science')
any_queries.send_keys('No queries at the moment.')


time.sleep(5)
# Close the WebDriver
driver.close()
driver.quit()


