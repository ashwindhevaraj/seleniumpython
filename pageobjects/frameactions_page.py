from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.basepage import basepage

class frameactions_page(basepage):
    framemenu=(By.CSS_SELECTOR,"a[href='/frames']")
    iframemenu=(By.CSS_SELECTOR,"a[href='/iframe']")
    exactframe=(By.CSS_SELECTOR,"#mce_0_ifr")
    textarea1=(By.CSS_SELECTOR,"#tinymce")

    def __init__(self,driver):
        super().__init__(driver)

    def click_framemenu(self):
        self.click_element(self.framemenu)
    
    def click_iframemenu(self):
        self.click_element(self.iframemenu)

    def switch_to_frame(self):
        self.switching_to_frame(self.exactframe)
    
    def enter_text_in_frame(self):
        self.input_text(self.textarea1,"Aswin in Iframe")

    def switch_to_defaultcontent(self):
        self.switching_to_defaultcontent()



    
