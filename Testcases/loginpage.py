import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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
        self.driver.switch_to.default_content()


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()