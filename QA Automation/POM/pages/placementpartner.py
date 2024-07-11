from selenium.webdriver.common.by import By

class Placementpartner:
    def __init__(self, driver):
        self.driver=driver
        self.placementpartner_button=(By.XPATH,"//a[contains(text(),'placement partner')]")

    def open_placementpartner_page(self,url):
        self.driver.get(url)