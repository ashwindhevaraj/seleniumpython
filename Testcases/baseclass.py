from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("pageobjects")
from frameactions_page import frameactions_page
from windowhandlepage import windowhandlepage



driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="122.0").install()))
wait=WebDriverWait(driver,30)

driver.get("https://the-internet.herokuapp.com/")
wait.until(EC.title_is("The Internet"))


frameactionpage=frameactions_page(driver,wait)
frameactionpage.click_framemenu()
frameactionpage.click_iframemenu()
frameactionpage.switch_to_frame()
frameactionpage.enter_text_in_frame()
frameactionpage.switch_to_defaultcontent()

driver.back()
driver.back()

windowhandle=windowhandlepage(driver,wait)
windowhandle.click_newtableelement()
windowhandle.click_newtableelement2()
windowhandle.switch_to_mainwindow()

driver.quit()
