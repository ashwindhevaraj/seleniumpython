from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Basepage import BasePage


class Dashpage(BasePage):
    dashboardtext=(By.CSS_SELECTOR,"[class='oxd-topbar-header-breadcrumb']")
    usernameclick = (By.XPATH,"//p[text()='manda user']")
    def __init__(self,driver):
        super().__init__(driver)

    def get_dashboardtitle(self):
        print(self.do_get_text(self.dashboardtext))

    def click_username(self):
        self.do_click(self.usernameclick)
