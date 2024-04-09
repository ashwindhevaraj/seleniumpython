from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC

class windowhandlepage(PageFactory):
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
    

    locators={
        'newtableelement':('CSS',"a[href='/windows']"),
        'newtableelement2':('CSS',"[href='/windows/new']")
    }

    def click_newtableelement(self):
        self.wait.until(EC.element_to_be_clickable(self.newtableelement))
        self.newtableelement.click()
    
    def click_newtableelement2(self):
        self.wait.until(EC.element_to_be_clickable(self.newtableelement2))
        self.newtableelement2.click()

    def switch_to_mainwindow(self):
        self.main_window_handle=self.driver.current_window_handle
        for self.handle in self.driver.window_handles:
            if self.handle!=self.main_window_handle:
                self.driver.switch_to.window(self.handle)
                print(self.driver.title)
        self.driver.switch_to.window(self.main_window_handle)
        self.driver.back()



    
