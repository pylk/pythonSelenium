import unittest
import sys
sys.path.append('../../../')
from test_case.models.driver import phone_browser
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.login_page import LoginPage


class AppPhoneTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = phone_browser()
        self.driver.maximize_window()

        po = LoginPage(self.driver)
        po.user_login()
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def tearDown(self):
        mp = MainPhonePage(self.driver)
        if mp.is_loading_not_visible() == True:
            if mp.is_msg_not_visible() == True:
                mp.return_to_homepage()


if __name__ == '__main__':
    unittest.main()
