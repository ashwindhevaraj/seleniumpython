from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

def selectdropdown(dropdownxpath,value):
    if not value[0]=='all':
        droplist=driver.find_elements(By.XPATH,dropdownxpath)
        for ele in droplist:
            print(ele.text)
            for x in range(len(value)):
                if ele.text == value[x]:
                    ele.click()
    else:
        dropdownxpath+="//input"
        droplist = driver.find_elements(By.XPATH, dropdownxpath)
        for ele in droplist:
            print(ele.text)
            ele.click()


driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
print(driver.title)
print(driver.current_url)
time.sleep(3)
dropdown=driver.find_element(By.ID,'justAnInputBox')
dropdown.click()
dropdown_xpath = (
    "//h3[text()='Multi Selection']"
    "//following::div[@class='comboTreeDropDownContainer'][1]"
    "//span"
)
#dropdownlist=driver.find_elements(By.XPATH,"//h3[text()='Multi Selection']//following::div[@class='comboTreeDropDownContainer'][1]//span")
value=["choice 2","choice 6 2 1"]
#value=["all"]
selectdropdown(dropdown_xpath,value)
time.sleep(3)
driver.quit()