from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.common.by import By

browser="chrome"
if browser=="firefox":
    options=firefoxOptions()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--ignore-certificate-errors")
    driver=webdriver.Firefox(options=options)
elif browser=="chrome":
    options=chromeOptions()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--ignore-certificate-errors")
    driver=webdriver.Chrome(options=options)
elif browser=="edge":
    options=edgeOptions()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--ignore-certificate-errors")
    driver=webdriver.Edge(options=options)
else:
    print("please pass correct browser")


driver.get("https://expired.badssl.com")
ele=driver.find_element(By.TAG_NAME,'h1')
print(ele.text)
driver.quit()






