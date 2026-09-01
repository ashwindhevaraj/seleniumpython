from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.edge.options import Options as edgeOptions

browser="edge"
if browser=="firefox":
    options=firefoxOptions()
    options.add_argument('-headless')
    options.add_argument("-private")
    driver=webdriver.Firefox(options=options)
elif browser=="chrome":
    options=chromeOptions()
    options.add_argument("--headless=new")
    options.add_argument('--incognito')
    driver=webdriver.Chrome(options=options)
elif browser=="edge":
    options=edgeOptions()
    options.add_argument('--inprivate')
    options.add_argument("--headless=new")
    driver=webdriver.Edge(options=options)
else:
    print("please pass correct browser")


driver.get("https://www.google.com")
print(driver.title)

driver.quit()






