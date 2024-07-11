#import the necessary modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#Set the Chrome Web Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the required url
website_url = 'https://mindrisers.com.np/'

#open the website
driver.get(website_url)
time.sleep(4)

#maximize the window
driver.maximize_window()
time.sleep(6)

#extract the website title and print it
website_title = driver.title
print(f'website_title: {website_title}')
print('Congrats successful !!!!')

#close the webdriver
driver.quit()