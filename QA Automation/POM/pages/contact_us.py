from selenium.webdriver.common.by import By

class ContactForm:
    def __init__(self, driver):
        self.driver=driver
        self.Name_textbox=(By.XPATH, "//input[@placeholder='Name']")
        self.Email_textbox = (By.XPATH, "//input[@placeholder='Email']")
        self.Phone_textbox = (By.XPATH, "//input[@placeholder='Phone']")
        self.Subject_textbox = (By.XPATH, "//input[@placeholder='Subject']")
        self.Queries_textbox = (By.XPATH, "//input[@placeholder='Queries']")

    def Open_page(self, url):
        self.driver.get(url)

    def Enter_name(self, Name):
        self.driver.find_element(*self.Name_textbox).send_keys(Name)

    def Enter_email(self, Email):
        self.driver.find_element(*self.Email_textbox).send_keys(Email)

    def Enter_Phone(self, Phone):
        self.driver.find_element(*self.Name_textbox).send_keys(Phone)

    def Enter_Subject(self, Subject):
        self.driver.find_element(*self.Name_textbox).send_keys(Subject)

    def Enter_Queries(self, Queries):
        self.driver.find_element(*self.Name_textbox).send_keys(Queries)
