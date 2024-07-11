# Import the necessary modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the website URL and open it
website_url = 'https://meroshare.cdsc.com.np'
driver.get(website_url)
time.sleep(1)

driver.maximize_window()
time.sleep(2)

wait = WebDriverWait(driver, 10)
down_button=driver.find_element(*(By.XPATH, "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1] "))
down_button.click()
time.sleep(2)

drop_option= driver.find_element(By.XPATH, "//li[contains(text(), 'AAKASH CAPITAL LIMITED (19000)')]")
drop_option.click()
time.sleep(5)

driver.close()
driver.quit()
print('finish success')

