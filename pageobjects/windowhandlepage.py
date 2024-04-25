from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.basepage import basepage

class windowhandlepage(basepage):
    newtableelement=(By.CSS_SELECTOR,"a[href='/windows']")
    newtableelement2=(By.CSS_SELECTOR,"[href='/windows/new']")
    def __init__(self,driver):
        super().__init__(driver)
        

    def click_newtableelement(self):
        self.click_element(self.newtableelement)
    
    def click_newtableelement2(self):
        self.click_element(self.newtableelement2)

    def switch_to_mainwindow(self):
        self.switch_to_all_windows()
        self.driver.back()



    
