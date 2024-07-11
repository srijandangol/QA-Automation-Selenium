import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the website
website_url = ('https://.com/')
driver.get(website_url)

# Maximize the window
driver.maximize_window()
time.sleep(2)

# Calculate the height of the webpage using JavaScript
page_height = driver.execute_script('return document.body.scrollHeight')
scroll_speed = 300
scroll_iterations = int(page_height / scroll_speed)

# Scroll through the page
for _ in range(scroll_iterations):
    driver.execute_script('window.scrollBy(0, arguments[0]);', scroll_speed)
    time.sleep(0.25)

# Extract the website title and print it
website_title = driver.title
print(f'Website title: {website_title}')
print('Congrats, successful!')

# Close the WebDriver
driver.quit()
