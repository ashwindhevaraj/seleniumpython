import pytest
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
    '''options.add_argument('--inprivate')
    options.add_argument("--headless=new")'''
    driver=webdriver.Edge(options=options)
else:
    print("please pass correct browser")

@pytest.mark.login
def test_google():
    driver.get("https://www.google.com")
    print(driver.title)
    assert driver.title=="Google"
    driver.quit()
def test_instagram():
    driver.get("https://www.instagram.com")
    print(driver.title)
    assert driver.title=="Instagram"
    driver.quit()


''' pip install pytest-xdist to install feature to run in parallel'''
''' py.test pytestsession/test_pytestsession2_class16.py -n 2   to run test in parallel'''
''' py.test pytestsession/test_pytestsession2_class16.py -m login   to run test in groups'''



