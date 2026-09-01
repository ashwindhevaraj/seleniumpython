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


@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("------------------setup--------------------- ")
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    yield
    print("-------------------teardown-----------------")
    driver.quit()


@pytest.mark.usefixtures("init_driver")
def test_title():
    print(driver.title)
    assert driver.title=="Google"

@pytest.mark.usefixtures("init_driver")
def test_url():
    print(driver.current_url)
    assert driver.current_url=="https://www.google.com/"


''' pip install pytest-html to generate report portion'''
''' pytest pytestsession/test_pytestsession3_class17.py -s -v --html=reportname.html'''



