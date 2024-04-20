from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class alertactions_page:
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
        self.alertmenu=(By.CSS_SELECTOR,"a[href='/javascript_alerts']")
        self.JSalertbtn=(By.XPATH,"//button[text()='Click for JS Alert']")
        self.result_text=(By.XPATH,"//h4[text()='Result:']//following::p")
        self.JSconfirmbtn=(By.CSS_SELECTOR,"button[onclick='jsConfirm()']")
        self.JSpromptbtn=(By.CSS_SELECTOR,"button[onclick='jsPrompt()']")


    def click_alertmenu(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.alertmenu)))
        self.driver.find_element(*self.alertmenu).click()

    def click_JSbutton(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.JSalertbtn)))
        self.driver.find_element(*self.JSalertbtn).click()

    def alert_object(self):
        self.alert=Alert(self.driver)
        return self.alert

    def create_alert(self):
        #self.alert=Alert(self.driver)
        self.alert=self.alert_object()
        self.alert.accept()
        
    def alerttext_comparison(self):
        if "You successfully clicked an alert"==self.driver.find_element(*self.result_text).text:
            print("text inside alert is true")

    def click_confirmbtn(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.JSconfirmbtn)))
        self.driver.find_element(*self.JSconfirmbtn).click()
        self.alert=self.alert_object()
        self.alert.dismiss()
        if "You clicked: Cancel"==self.driver.find_element(*self.result_text).text:
            print("Both texts are same from confirm button")

    def click_promptbutton(self):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*self.JSpromptbtn)))
        self.driver.find_element(*self.JSpromptbtn).click()
        self.alert=self.alert_object()
        self.alert.send_keys("Inside prompt")
        self.alert.accept()
        if "You entered: Inside prompt"==self.driver.find_element(*self.result_text).text:
            print("Both texts are same from prompt button of alert")
        
        