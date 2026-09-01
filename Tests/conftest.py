import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.edge.options import Options as edgeOptions

@pytest.fixture(params=['chrome','firefox','edge'],scope="class")
def init__driver(request):
    if request.param=='chrome':
        options = chromeOptions()
        '''options.add_argument("--headless=new")
        options.add_argument('--incognito')'''
        web_driver=webdriver.Chrome(options=options)
    if request.param=='firefox':
        options = firefoxOptions()
        '''options.add_argument('-headless')
        options.add_argument("-private")'''
        web_driver=webdriver.Firefox(options=options)
    if request.param=='edge':
        options = edgeOptions()
        '''options.add_argument('--inprivate')
        options.add_argument("--headless=new")'''
        web_driver=webdriver.Edge(options=options)
    web_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    web_driver.implicitly_wait(10)
    request.cls.driver=web_driver
    yield
    print("-------------------teardown-----------------")
    web_driver.close()