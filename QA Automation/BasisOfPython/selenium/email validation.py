# Import the necessary modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re

# Set the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the function for valid email and phone validation
def is_valid_email(email):
    try:
        # Check the format using re (regular expression)
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(email_pattern, email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$', phone))

# Open the website
driver.get('https://mindrisers.com.np/contact-us')
driver.maximize_window()
time.sleep(2)

# Set the scroll parameter
target_y = 6000
scroll_distance = 1000
current_y = 0

# Scrolling the page
while current_y < target_y:
    driver.execute_script(f'window.scrollBy(0, {scroll_distance})')
    current_y += scroll_distance
    time.sleep(0.25)

# Interact with web elements
full_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
phone_field = driver.find_element(By.XPATH, "//input[@placeholder='Phone']")
time.sleep(2)

# Fill the form with example data
full_name = 'ram'
email = 'ram@gmail.com'
# email = 'ramgmail.com'  # Uncomment to test invalid email
# email = 'ram@gmailcom'  # Uncomment to test invalid email
# email = 'ram1235'       # Uncomment to test invalid email
# phone = '9876543210'  # Example valid phone number
# phone = ''            # Uncomment to test empty phone number
phone = '987654'      # Uncomment to test invalid phone number

time.sleep(2)

# Check if name is empty
if not full_name:
    print('Name cannot be empty')

# Clear the field and pass the value
full_name_field.clear()
full_name_field.send_keys(full_name)

# Check the validation of email
if is_valid_email(email):
    print('Email is valid')
else:
    print('Email is invalid')

email_field.clear()
email_field.send_keys(email)
time.sleep(2)

# Validate phone number
if len(phone) == 0:
    print('Phone cannot be empty')
elif len(phone) > 0 and len(phone) < 10:
    print('Enter a valid phone number')
elif not is_valid_phone(phone):
    print('Enter a valid phone number')
else:
    print('Phone is valid')

phone_field.clear()
phone_field.send_keys(phone)
time.sleep(2)

# Close the WebDriver
driver.quit()
