from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class basepage:
    def __init__(self,driver):
        self.driver=driver

    def find_Element(self,locator,timeout=20):
        try:
            element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} not found within timeout {timeout}")

    def click_element(self,locator,timeout=20):
        element=self.find_Element(locator,timeout)
        element.click()

    def input_text(self,locator,text,timeout=20):
        element=self.find_Element(locator,timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator,timeout=20):
        element=self.find_Element(locator,timeout)
        return element.text

    def navigate_to_url(self,url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def switching_to_frame(self,locator,timeout=20):
        element=self.find_Element(locator,timeout)
        self.driver.switch_to.frame(element)

    def switching_to_defaultcontent(self):
        self.driver.switch_to.default_content()

    #creation of alert object and returning them    
    def alert_object(self):
        self.alert=Alert(self.driver)
        return self.alert

    #will switch to all windows one by one and printing title and switching back to main window    
    def switch_to_all_windows(self):
        self.main_window_handle=self.driver.current_window_handle
        for self.handle in self.driver.window_handles:
            if self.handle!=self.main_window_handle:
                self.driver.switch_to.window(self.handle)
                print(self.driver.title)
        self.driver.switch_to.window(self.main_window_handle)

    def convert_locator_to_string(self,locator):
        loc=str(locator)
        res=[s.strip() for s in loc.split(',')]
        v=res[1]
        k=v[:-1]
        m=k[1:-1]
        return m

    #scroll to element
    def scroll_to_an_element(self,locator):
        txt=self.convert_locator_to_string(locator)
        self.driver.execute_script("arguments[0].scrollIntoView()",self.driver.find_element(By.XPATH,txt))


