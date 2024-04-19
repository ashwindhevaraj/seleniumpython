from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class linktext_page(PageFactory):

    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
        
    """locators:{
        'LINKTEXT1':('LINKTEXT',"A/B Testing"),
        'PARTIAL1':('PARTIALLINKTEXT',"Add/Remove")
    }"""
    

    def click_linktext(self):
        self.LINKTEXT1=self.driver.find_element(By.LINK_TEXT,"A/B Testing")
        self.wait.until(EC.element_to_be_clickable(self.LINKTEXT1))
        self.LINKTEXT1.click()
    
    def click_partiallinktext(self):
        self.PARTIAL1=self.driver.find_element(By.PARTIAL_LINK_TEXT,"Add/Remove")
        self.wait.until(EC.element_to_be_clickable(self.PARTIAL1))
        self.PARTIAL1.click()


    
