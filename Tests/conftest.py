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
        driver=webdriver.Chrome(options=options)
    elif request.param=='firefox':
        options = firefoxOptions()
        '''options.add_argument('-headless')
        options.add_argument("-private")'''
        driver=webdriver.Firefox(options=options)
    elif request.param=='edge':
        options = edgeOptions()
        '''options.add_argument('--inprivate')
        options.add_argument("--headless=new")'''
        driver=webdriver.Edge(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(20)
    request.cls.driver=driver
    yield
    print("-------------------teardown-----------------")
    driver.quit()