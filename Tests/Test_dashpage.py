import time

from Pages.Dashpage import Dashpage
from Pages.Loginpage import Loginpage
from Pages.Basepage import BasePage
from Tests.BaseTest import BaseTest

class Test_dashpage(BaseTest):
    def test_dashpage_tc1(self):
        self.loginpage = Loginpage(self.driver)
        dashpage= self.loginpage.do_login()
        dashpage.get_dashboardtitle()
        dashpage.click_username()
        time.sleep(10)


