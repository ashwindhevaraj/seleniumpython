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
        'result_text':('XPATH',"//h4[text()='Result:']//following::p"),
        'JSconfirmbtn':('CSS',"button[onclick='jsConfirm()']"),
        'JSpromptbtn':('CSS',"button[onclick='jsPrompt()']")
    }

    def click_alertmenu(self):
        self.wait.until(EC.element_to_be_clickable(self.alertmenu))
        self.alertmenu.click()

    def click_JSbutton(self):
        self.wait.until(EC.element_to_be_clickable(self.JSalertbtn))
        self.JSalertbtn.click()

    def alert_object(self):
        self.alert=Alert(self.driver)
        return self.alert

    def create_alert(self):
        #self.alert=Alert(self.driver)
        self.alert=self.alert_object()
        self.alert.accept()
        
    def alerttext_comparison(self):
        if "You successfully clicked an alert"==self.result_text.text:
            print("text inside alert is true")

    def click_confirmbtn(self):
        self.wait.until(EC.element_to_be_clickable(self.JSconfirmbtn))
        self.JSconfirmbtn.click()
        self.alert=self.alert_object()
        self.alert.dismiss()
        if "You clicked: Cancel"==self.result_text.text:
            print("Both texts are same from confirm button")

    def click_promptbutton(self):
        self.wait.until(EC.element_to_be_clickable(self.JSpromptbtn))
        self.JSpromptbtn.click()
        self.alert=self.alert_object()
        self.alert.send_keys("Inside prompt")
        self.alert.accept()
        if "You entered: Inside prompt"==self.result_text.text:
            print("Both texts are same from prompt button of alert")
        
        