from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class alertactions_page(PageFactory):
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait

    locators={
        'alertmenu':('CSS',"a[href='/javascript_alerts']"),
        'JSalertbtn':('XPATH',"//button[text()='Click for JS Alert']"),
        'result_text':('XPATH',"//h4[text()='Result:']//following::p")
    }

    def click_alertmenu(self):
        self.wait.until(EC.element_to_be_clickable(self.alertmenu))
        self.alertmenu.click()

    def click_JSbutton(self):
        self.wait.until(EC.element_to_be_clickable(self.JSalertbtn))
        self.JSalertbtn.click()

    def create_alert(self):
        self.alert=Alert(self.driver)
        self.alert.accept()
        
    def alerttext_comparison(self):
        if "You successfully clicked an alert"==self.result_text.text:
            print("text inside alert is true")
        
        