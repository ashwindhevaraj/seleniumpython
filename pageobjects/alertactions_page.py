from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from pageobjects.basepage import basepage

class alertactions_page(basepage):
    alertmenu=(By.CSS_SELECTOR,"a[href='/javascript_alerts']")
    JSalertbtn=(By.XPATH,"//button[text()='Click for JS Alert']")
    result_text=(By.XPATH,"//h4[text()='Result:']//following::p")
    JSconfirmbtn=(By.CSS_SELECTOR,"button[onclick='jsConfirm()']")
    JSpromptbtn=(By.CSS_SELECTOR,"button[onclick='jsPrompt()']")

    def __init__(self,driver):
        super().__init__(driver)

    def click_alertmenu(self):
        self.click_element(self.alertmenu)

    def click_JSbutton(self):
        self.click_element(self.JSalertbtn)

    def accept_alert(self):
        self.alert=self.alert_object()
        self.alert.accept()
        
    def alerttext_comparison(self):
        if "You successfully clicked an alert"==self.get_text(self.result_text):
            print("text inside alert is true")

    def click_confirmbtn(self):
        self.click_element(self.JSconfirmbtn)
        self.alert=self.alert_object()
        self.alert.dismiss()
        if "You clicked: Cancel"==self.get_text(self.result_text):
            print("Both texts are same from confirm button")

    def click_promptbutton(self):
        self.click_element(self.JSpromptbtn)
        self.alert=self.alert_object()
        self.alert.send_keys("Inside prompt")
        self.alert.accept()
        if "You entered: Inside prompt"==self.get_text(self.result_text):
            print("Both texts are same from prompt button of alert")
        
        