from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class basepage:
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locator,timeout=20):
        try:
            element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} not found within timeout {timeout}")

    def click_element(self,locator,timeout=20):
        element=self.find_element(locator,timeout)
        element.click()

    def input_text(self,locator,text,timeout=20):
        element=self.find_element(locator,timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator,timeout=20):
        element=self.find_element(locator,timeout)
        return element.text

    def navigate_to_url(self,url):
        self.driver.get(url)

    def get_title(self,locator):
        return self.driver.title
    
    def switching_to_frame(self,locator,timeout=20):
        element=self.find_element(locator,timeout)
        self.driver.switch_to.frame(element)

    def switching_to_defaultcontent(self):
        self.driver.switch_to.default_content()
