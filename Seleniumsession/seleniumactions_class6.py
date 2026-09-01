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

driver.get("https://the-internet.herokuapp.com/drag_and_drop")
print(driver.title)
print(driver.current_url)
time.sleep(3)

'''1.drag and drop'''
drag1=driver.find_element(By.ID,'column-a')
drag2=driver.find_element(By.ID,'column-b')
action = ActionChains(driver)
action.drag_and_drop(drag1,drag2).perform()

'''2.move to element'''
driver.get('https://the-internet.herokuapp.com/jqueryui/menu')
driver.implicitly_wait(10);
elem1=driver.find_element(By.LINK_TEXT,'Enabled')
action.move_to_element(elem1).perform()


'''3. context click'''
driver.get('https://the-internet.herokuapp.com/context_menu')
elem2=driver.find_element(By.ID,'hot-spot')
action.context_click(elem2).perform()
time.sleep(3)
driver.quit()
