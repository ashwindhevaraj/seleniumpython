from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
browser="edge"
if browser=="firefox":
    driver=webdriver.Firefox()
elif browser=="chrome":
    driver=webdriver.Chrome()
elif browser=="edge":
    driver=webdriver.Edge()
else:
    print("please pass correct browser")

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
print(driver.title)
print(driver.current_url)
time.sleep(3)

'''1.alert handling'''
elem1=driver.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']")
elem1.click()
driver.switch_to.alert.accept()
driver.switch_to.default_content()

'''2.alert handling2'''
driver.implicitly_wait(5)
elem2=driver.find_element(By.CSS_SELECTOR,"button[onclick='jsConfirm()']")
elem2.click()
driver.switch_to.alert.dismiss()
driver.switch_to.default_content()


'''3.alert handling2'''
driver.implicitly_wait(5)
elem3=driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']")
elem3.click()
alert1=driver.switch_to.alert
alert1.send_keys("normaldata")
alert1.accept()
driver.switch_to.default_content()
