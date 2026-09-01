from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,'[aria-label="Search"]').send_keys('naveen automation')
dropdown = driver.find_elements(By.CSS_SELECTOR,'ul.G43f7e li div[role="presentation"]:not([style*="display:none"]):not([style*="display: none"]) span')
time.sleep(3)
for s in dropdown:
    print(s.text)
    if s.text=='naveen automationlabs youtube':
        s.click()
        break
time.sleep(3)
driver.quit()