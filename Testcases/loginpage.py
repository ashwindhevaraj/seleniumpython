import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
class loginpage:
    def openbrowser(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.hotmail.com")

    def browserclose():
        driver.quit()

login=loginpage()
login.openbrowser()
login.browserclose()