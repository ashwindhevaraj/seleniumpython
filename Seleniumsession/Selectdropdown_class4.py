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

driver.get("https://qaplayground.com/practice/dropdowns")
print(driver.title)
print(driver.current_url)
selectelement=driver.find_element(By.ID,'fruitSelect')
selectelement1=Select(selectelement)
#selectelement1.select_by_value("apple")
#selectelement1.select_by_visible_text("Banana")
#selectelement1.select_by_index(3)
linklist=selectelement1.options
for s in linklist:
   print(s.text)
   if s.text=='Orange':
       print('just a simple validations')
time.sleep(3)
driver.quit()