from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class windowhandlepage:
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
        self.newtableelement=(By.CSS_SELECTOR,"a[href='/windows']")
        self.newtableelement2=(By.CSS_SELECTOR,"[href='/windows/new']")

    def click_newtableelement(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.newtableelement)))
        self.driver.find_element(*self.newtableelement).click()
    
    def click_newtableelement2(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.newtableelement2)))
        self.driver.find_element(*self.newtableelement2).click()

    def switch_to_mainwindow(self):
        self.main_window_handle=self.driver.current_window_handle
        for self.handle in self.driver.window_handles:
            if self.handle!=self.main_window_handle:
                self.driver.switch_to.window(self.handle)
                print(self.driver.title)
        self.driver.switch_to.window(self.main_window_handle)
        self.driver.back()



    
