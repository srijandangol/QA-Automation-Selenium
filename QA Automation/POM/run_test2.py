import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.pages.contact_us import ContactForm
from POM.pages.placementpartner import Placementpartner
from POM.pages.courses import Ourcourses

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_contact_form(driver):
    contact_form = ContactForm(driver)
    contact_form.Open_page("https://mindrisers.com.np/contact-us")
    driver.maximize_window()

    # Explicit waits to ensure elements are present before interacting with them
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )

    contact_form.Enter_name("Ram")
    contact_form.Enter_Phone("9861616161")
    contact_form.Enter_email("Ram@gmail.com")
    contact_form.Enter_Subject("QA")
    contact_form.Enter_Queries("Hello")

    # Add assertions here to verify the success of form submission, if applicable
    # For example:
    # success_message = driver.find_element(By.ID, "success-message-id")
    # assert "Thank you" in success_message.text

    print("Congrats, the code executed successfully")


def test_placementpartner_page(driver):
    placementpartner_page = Placementpartner(driver)
    placementpartner_page.open_placementpartner_page("https://mindrisers.com.np/placement-partner")
    driver.maximize_window()

    # Get the page height
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Scroll through the page
    scroll_speed = 900
    scroll_iterations = int(page_height / scroll_speed)

    for _ in range(scroll_iterations):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed})")
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loading-spinner")))
        time.sleep(1)  # Adjust as needed for your application
        print("Scrolled successfully")

    # Optionally, add assertions to verify specific elements or conditions after scrolling
    # For example:
    # assert "Footer" in driver.page_source, "Footer not found after scrolling"

    print("Scrolling test completed successfully")

def test_ourcourses_page(driver):
    ourcourse_page = Ourcourses(driver)
    ourcourse_page.open_ourcourses_page("https://mindrisers.com.np/courses")
    driver.maximize_window()

    # Get the page height
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Scroll through the page
    scroll_speed = 900
    scroll_iterations = int(page_height / scroll_speed)

    for _ in range(scroll_iterations):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed})")
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loading-spinner")))
        time.sleep(1)  # Adjust as needed for your application
        print("Scrolled successfully")

    # Optionally, add assertions to verify specific elements or conditions after scrolling
    # For example:
    # assert "Footer" in driver.page_source, "Footer not found after scrolling"

    print("Course page Scrolling test completed successfully")


