from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.basepage import basepage

class freshservice_loginpage(basepage):
    username_field=(By.CSS_SELECTOR,"[id='username']")
    password_field=(By.CSS_SELECTOR,"[id='password']")
    signin_button=(By.CSS_SELECTOR,"[data-testid='login-button']")
    logout_icon=(By.CSS_SELECTOR,"a[id='header-profile-avatar']")
    logout_button=(By.CSS_SELECTOR,"[id='signout-link']")
    

    def __init__(self,driver):
        super().__init__(driver)

    def login_freshservice(self):
        self.input_text(self.username_field,"aswin.devaraj@freshworks.com")
        self.input_text(self.password_field,"12345678")
        self.click_element(self.signin_button)

    def logout_freshservice(self):
        self.click_element(self.logout_icon)
        self.click_element(self.logout_button)




    
