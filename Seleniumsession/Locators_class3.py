from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://google.com")
element1=driver.find_element(By.CSS_SELECTOR,'[aria-label="Search"]')
element2=driver.find_element(By.ID,'#id1')
element3=driver.find_element(By.NAME,"namevalue")
element4=driver.find_element(By.CLASS_NAME,"classuniquename")
element5=driver.find_element(By.LINK_TEXT,"linktext")
element6=driver.find_element(By.PARTIAL_LINK_TEXT,"partialtext")
element7=driver.find_element(By.TAG_NAME,"tagname")
element8=driver.find_element(By.XPATH,"//div[text()='ash']")
