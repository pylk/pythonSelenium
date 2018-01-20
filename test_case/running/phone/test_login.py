from time import sleep
import unittest
import sys
import random
sys.path.append('../../../')
from test_case.models.driver import phone_browser
from test_case.page_obj.login_page import LoginPage


class LoginPhoneTest(unittest.TestCase):
    '''myapps phone登录测试'''

    @classmethod
    def setUpClass(self):
        self.driver = phone_browser()
        self.driver.maximize_window()
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_login(self):
        '''用户名、密码'''
        po = LoginPage(self.driver)
        po.user_login()
        self.assertEqual('自动化测试系统', self.driver.title, msg='登录校验不通过')

if __name__ == '__main__':
    unittest.main()