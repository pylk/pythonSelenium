import unittest
import sys
sys.path.append('../../../../')
from test_case.models.driver import browser
from test_case.page_obj.login_page import LoginPage


class LoginTest(unittest.TestCase):
    '''myapps登录测试'''

    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.driver.maximize_window()
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_login(self):
        '''用户名、密码'''
        po = LoginPage(self.driver)
        po.user_login('liling', '123456')
        self.assertIn('天翎', self.driver.title)

if __name__ == '__main__':
    unittest.main()