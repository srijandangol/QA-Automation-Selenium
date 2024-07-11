import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the function for valid email and phone validation
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None

def is_valid_phone(phone):
    phone_pattern = r'^\+977-98\d{8}$'
    return re.match(phone_pattern, phone) is not None

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

# Function to generate random data
def generate_random_email():
    domain = 'test.com'
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + '@' + domain
    return email

def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

def generate_random_phone():
    return '+977-98' + ''.join(random.choice(string.digits) for _ in range(8))

# Generate random data
name = generate_random_name()
email = generate_random_email()
phone = generate_random_phone()
time.sleep(2)

# Locate the form fields
try:
    name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'name')))
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    phone_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'phone')))
except Exception as e:
    print(f"Error locating fields: {e}")
    driver.quit()
    exit()

# Check if name is empty
if not name:
    print('Name cannot be empty')

# Clear the field and pass the value
name_field.clear()
name_field.send_keys(name)

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
