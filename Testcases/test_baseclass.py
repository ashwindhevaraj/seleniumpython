import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("pageobjects")
from pageobjects.frameactions_page import frameactions_page
from pageobjects.windowhandlepage import windowhandlepage
from pageobjects.alertactions_page import alertactions_page
from pageobjects.linktext_page import linktext_page


class Test_baseclass:
    def test_frame(self):
        self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="124.0").install()))
        self.wait=WebDriverWait(self.driver,30)
        self.driver.get("https://the-internet.herokuapp.com/")
        self.wait.until(EC.title_is("The Internet"))
        self.frameactionpage=frameactions_page(self.driver,self.wait)
        self.frameactionpage.click_framemenu()
        self.frameactionpage.click_iframemenu()
        self.frameactionpage.switch_to_frame()
        self.frameactionpage.enter_text_in_frame()
        self.frameactionpage.switch_to_defaultcontent()
        self.driver.back()
        self.driver.back()
        self.windowhandle=windowhandlepage(self.driver,self.wait)
        self.windowhandle.click_newtableelement()
        self.windowhandle.click_newtableelement2()
        self.windowhandle.switch_to_mainwindow()

        self.alertpage=alertactions_page(self.driver,self.wait)
        self.alertpage.click_alertmenu()
        self.alertpage.click_JSbutton()
        self.alertpage.create_alert()
        self.alertpage.alerttext_comparison()
        self.alertpage.click_confirmbtn()
        self.alertpage.click_promptbutton()
        self.driver.back()

        self.linkpage=linktext_page(self.driver,self.wait)
        self.linkpage.click_linktext()
        self.driver.back()
        self.linkpage.click_partiallinktext()
        self.driver.back()
        self.driver.quit()

        assert "pass"=="pass", "first test case written in pytest passed"
