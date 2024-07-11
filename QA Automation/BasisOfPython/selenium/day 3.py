#path locator create/ post method
#import The necessary module
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Set the Chrome Web Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website_url='https://demoqa.com' #defining the website
driver.get(website_url) #opening website
time.sleep(2)

# Maximize the window
driver.maximize_window()
time.sleep(2)

driver.get('https://demoqa.com/text-box')

#find the specific location by using the locators
full_name=driver.find_element(By.XPATH, "//input[@id='userName']")
email=driver.find_element(By.XPATH, "//input[@id='userEmail']")
current_address=driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
permanent_address=driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")


#fill the form element
full_name.send_keys('Ram Shyam')
email.send_keys('Ram_Shyam@gmail.com')
current_address.send_keys('ktm')
permanent_address.send_keys('Rasuwa')
time.sleep(5)
# Close the WebDriver
driver.quit()


