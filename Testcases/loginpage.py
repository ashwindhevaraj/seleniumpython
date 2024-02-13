import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class loginpage:
    def openbrowser(self):
        self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(30)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.elem1=self.driver.find_element(By.NAME,"username")
        #WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.elem1)).click()
        self.elem1.send_keys("Admin")
        self.elem2=self.driver.find_element(By.CSS_SELECTOR,"[name='password']")
        self.elem2.send_keys("admin123")
        self.elem3=self.driver.find_element(By.CSS_SELECTOR,"[type='submit']")
        self.elem3.click()
        assert "aswintest" in "aswintest"

        

    def browserclose(self):
        self.driver.quit()

login=loginpage()
login.openbrowser()
login.browserclose()