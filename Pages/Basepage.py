from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self,driver):
        self.driver=driver
    def do_click(self,bylocator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(bylocator)).click()
    def do_send_keys(self,bylocator,text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(bylocator)).send_keys(text)
    def do_get_text(self,bylocator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(bylocator)).text
