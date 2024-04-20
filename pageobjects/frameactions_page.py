from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class frameactions_page:
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
        self.framemenu=(By.CSS_SELECTOR,"a[href='/frames']")
        self.iframemenu=(By.CSS_SELECTOR,"a[href='/iframe']")
        self.exactframe=(By.CSS_SELECTOR,"#mce_0_ifr")
        self.textarea1=(By.CSS_SELECTOR,"#tinymce")

    def click_framemenu(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.framemenu)))
        self.driver.find_element(*self.framemenu).click()
    
    def click_iframemenu(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.iframemenu)))
        self.driver.find_element(*self.iframemenu).click()

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.exactframe))
    
    def enter_text_in_frame(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.textarea1)))
        self.driver.find_element(*self.textarea1).clear()
        self.driver.find_element(*self.textarea1).send_keys("Aswin in Iframe")

    def switch_to_defaultcontent(self):
        self.driver.switch_to.default_content()



    
