from selenium.webdriver.common.by import By

class Ourcourses:
    def __init__(self, driver):
        self.driver=driver
        self.ourcourses_button=(By.XPATH,"//a[contains(text(),'our courses')]")

    def open_ourcourses_page(self,url):
        self.driver.get(url)