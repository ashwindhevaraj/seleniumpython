from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.basepage import basepage

class linktext_page(basepage):

    LINKTEXT1=(By.LINK_TEXT,"A/B Testing")
    PARTIAL1=(By.PARTIAL_LINK_TEXT,"Add/Remove")

    def __init__(self,driver):
        super().__init__(driver)
        
    def click_linktext(self):
        self.click_element(self.LINKTEXT1)
        self.driver.back()
    
    def click_partiallinktext(self):
        self.click_element(self.PARTIAL1)
        self.driver.back()


    
