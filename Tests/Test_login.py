from Pages.Loginpage import Loginpage
from Pages.Basepage import BasePage
from Tests.BaseTest import BaseTest

class Test_login(BaseTest):
    def test_login_tc1(self):
        self.loginpage = Loginpage(self.driver)
        self.loginpage.do_login()
