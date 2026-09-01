from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage


class Loginpage(BasePage):
    username=(By.NAME,"username")
    password=(By.NAME,"password")
    submitbutton = (By.XPATH,"//button[@type='submit']")
    def __init__(self,driver):
        super().__init__(driver)

    def goto_loginpage(self):
        self.driver.get(self.driver.current_url)

    def do_login(self):
        self.do_send_keys(self.username,"Admin")
        self.do_send_keys(self.password,"admin123")
        self.do_click(self.submitbutton)
