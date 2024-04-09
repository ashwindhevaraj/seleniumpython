from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC

class frameactions_page(PageFactory):
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
    

    locators={
        'framemenu':('CSS',"a[href='/frames']"),
        'iframemenu':('CSS',"a[href='/iframe']"),
        'exactframe':('CSS',"#mce_0_ifr"),
        'textarea1':('CSS',"#tinymce")
    }

    def click_framemenu(self):
        self.wait.until(EC.element_to_be_clickable(self.framemenu))
        self.framemenu.click()
    
    def click_iframemenu(self):
        self.wait.until(EC.element_to_be_clickable(self.iframemenu))
        self.iframemenu.click()

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.exactframe)
    
    def enter_text_in_frame(self):
        self.wait.until(EC.element_to_be_clickable(self.textarea1))
        self.textarea1.clear()
        self.textarea1.send_keys("Aswin in Iframe")

    def switch_to_defaultcontent(self):
        self.driver.switch_to.default_content()



    
