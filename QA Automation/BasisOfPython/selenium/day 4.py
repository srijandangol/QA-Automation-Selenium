#path locator create/ post method
#import The necessary module
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Set the Chrome Web Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website_url='https://demoqa.com/' #defining the website
driver.get(website_url) #opening website
time.sleep(2)

# Maximize the window
driver.maximize_window()
time.sleep(2)

driver.get('https://demoqa.com/alerts')

# Find the specific location using the locators
click_me=driver.find_element(By.XPATH,"//button[@id='alertButton']")
click_me.click()
time.sleep(5)

#Switch to alerts
alert=driver.switch_to.alert

#close the alerts
alert.accept()

#application command
#extract and print the website title
website_title = driver.title
print(f'Website title: {website_title}')

#website current URL
current_url=driver.current_url
print(f'current url: {current_url}')

#get the page source
page_source= driver.page_source
print(f'Page Source: {page_source}')

# Close the WebDriver
driver.close()
driver.quit()


