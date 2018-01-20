import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.app_test import AppPhoneTest
from test_case.page_obj.main_page import MainPhonePage


class ButtonPhoneTest(AppPhoneTest):
    '''生命周期调用方法中实现打开浏览器登录和关闭浏览器'''
    
    def setUp(self):
        mp = MainPhonePage(self.driver)
        mp.switch_to_menu_page()

    def tearDown(self):
        mp = MainPhonePage(self.driver)
        if mp.is_loading_not_visible() == True:
            if mp.is_msg_not_visible() == True:
                mp.return_to_homepage()
    
if __name__ == '__main__':
    unittest.main()
