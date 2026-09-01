import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('num,result', [(1,11),(2,22)])
def test_assertion(num,result):
    assert num*11==result

@pytest.mark.usefixtures("init__driver")
class BaseTest():
    pass

class Test_orangeHRM(BaseTest):
    @pytest.mark.parametrize('username,password',
                             [('Admin','admin123'),])
    def test_orangeHRM(self,username,password):
        self.driver.find_element(By.NAME,'username').send_keys(username)
        self.driver.find_element(By.NAME,'password').send_keys(password)
