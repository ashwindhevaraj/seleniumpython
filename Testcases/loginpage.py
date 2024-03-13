import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time

class loginpage(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
    def test_openbrowser(self):
        driver=self.driver
        #self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(30)
        """self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.elem1=self.driver.find_element(By.NAME,"username")
        #WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.elem1)).click()
        self.elem1.send_keys("Admin")
        self.elem2=self.driver.find_element(By.CSS_SELECTOR,"[name='password']")
        self.elem2.send_keys("admin123")
        self.elem3=self.driver.find_element(By.CSS_SELECTOR,"[type='submit']")
        self.elem3.click()
        self.elem4=self.driver.find_element(By.XPATH,"//span[text()='Directory']")
        self.elem4.click()
        self.elem5=self.driver.find_element(By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
        self.elem5.click()
        self.elem6=self.driver.find_elements(By.XPATH,"//div[@role='listbox']//div[@role='option']")
        for x in self.elem6:
            print(x.text)
            if x.text=="Automaton Tester":
                x.click()
                break
        self.assertIn("Aswin","Aswin")
        self.elem7=self.driver.find_element(By.XPATH,"//span[text()='My Info']")
        self.elem7.click()
        self.elem8=self.driver.find_element(By.XPATH,"//a[text()='Personal Details']")
        self.actionchains=ActionChains(self.driver)
        self.elem9=self.driver.find_element(By.XPATH,"//label[text()='Other Id']//parent::div//following-sibling::div//input")
        time.sleep(3)
        self.actionchains.drag_and_drop(self.elem8,self.elem9).perform()
        time.sleep(3)"""
        self.driver.get("https://the-internet.herokuapp.com/")
        self.framemenu=self.driver.find_element(By.CSS_SELECTOR,"a[href='/frames']")
        self.framemenu.click()
        self.iframemenu=self.driver.find_element(By.CSS_SELECTOR,"a[href='/iframe']")
        self.iframemenu.click()
        self.exactframe=self.driver.find_element(By.CSS_SELECTOR,"#mce_0_ifr")
        self.driver.switch_to.frame(self.exactframe)
        self.textarea1=self.driver.find_element(By.CSS_SELECTOR,"#tinymce>p")
        self.textarea1.clear()
        self.textarea1.send_keys("Aswin in Iframe")
        self.driver.switch_to.default_content()
        time.sleep(3)
        self.driver.back()
        self.driver.back()

        self.newtabelement=self.driver.find_element(By.CSS_SELECTOR,"a[href='/windows']")
        self.newtabelement.click()
        self.newtablelement2=self.driver.find_element(By.CSS_SELECTOR,"[href='/windows/new']")
        self.newtablelement2.click()
        self.main_window_handle=driver.current_window_handle
        for handle in driver.window_handles:
            if handle!=self.main_window_handle:
                self.driver.switch_to.window(handle)
                print(self.driver.title)
        self.driver.switch_to.window(self.main_window_handle)
        self.driver.back()

        self.alertmenu=self.driver.find_element(By.CSS_SELECTOR,"a[href='/javascript_alerts']")
        self.alertmenu.click()
        self.JSalertbtn=self.driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']")
        self.JSalertbtn.click()
        #self.driver.switch_to.alert
        self.alert=Alert(self.driver)
        self.alert.accept()
        self.result_text=self.driver.find_element(By.XPATH,"//h4[text()='Result:']//following::p")
        self.assertIn("You successfully clicked an alert",self.result_text.text)

        self.JSconfirmbtn=self.driver.find_element(By.CSS_SELECTOR,"button[onclick='jsConfirm()']")
        self.JSconfirmbtn.click()
        self.alert=Alert(self.driver)
        self.alert.dismiss()
        self.assertIn("You clicked: Cancel",self.result_text.text)

        self.JSpromptbtn=self.driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']")
        self.JSpromptbtn.click()
        self.alert=Alert(self.driver)
        self.alert.send_keys("Inside prompt")
        self.alert.accept()
        self.assertIn("You entered: Inside prompt",self.result_text.text)
        self.driver.back()

        self.linktext1=self.driver.find_element(By.LINK_TEXT,"A/B Testing")
        self.linktext1.click()
        self.driver.back()
        self.partiallink1=self.driver.find_element(By.PARTIAL_LINK_TEXT,"Add/Remove")
        self.partiallink1.click()
        self.driver.back()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()