from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class linktext_page:

    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
        self.LINKTEXT1=(By.LINK_TEXT,"A/B Testing")
        self.PARTIAL1=(By.PARTIAL_LINK_TEXT,"Add/Remove")

    def click_linktext(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.LINKTEXT1)))
        self.driver.find_element(*self.LINKTEXT1).click()
    
    def click_partiallinktext(self):
        
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.PARTIAL1)))
        self.driver.find_element(*self.PARTIAL1).click()


    
