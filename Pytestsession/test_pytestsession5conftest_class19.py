import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.edge.options import Options as edgeOptions

@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass
class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        print(self.driver.title)
        assert self.driver.title=="Google"
    def test_google_url(self):
        print(self.driver.current_url)
        assert self.driver.current_url=="https://www.google.com/"




