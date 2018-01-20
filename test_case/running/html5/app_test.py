import unittest
import sys
import time
sys.path.append('../../../')
from test_case.models.driver import browser
from test_case.page_obj.login_page import LoginPage
from test_case.page_obj.main_page import MainPage




class AppTest(unittest.TestCase):
    '''生命周期调用方法中实现打开浏览器登录和关闭浏览器'''
    
    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.driver.maximize_window()

        # 登录页面
        po = LoginPage(self.driver)
        po.user_login('liling', '123456')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        
    def tearDown(self):
        mp = MainPage(self.driver)
        mp.accept_alert_for_teardown() #teardown生命周期判断是否存在alert并且接受alert
        if len(self.driver.window_handles)>=2: #判断是否打开了多个窗口
            self.driver.close()
            mp.switch_to_current_window()
        # mp.refresh_main()

    
if __name__ == '__main__':
    unittest.main()
