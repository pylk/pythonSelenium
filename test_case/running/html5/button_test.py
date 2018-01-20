import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.models.driver import browser
from test_case.running.html5.app_test import AppTest
from test_case.page_obj.login_page import LoginPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.form_page import FormPage


class ButtonTest(AppTest):
    '''生命周期调用方法中实现打开浏览器登录和关闭浏览器'''
    
    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.5)
        mp.switch_to_iframe()
        fp = FormPage(self.driver)
        fp.wait_loading_hide()
    
    def setUp(self):
        mp = MainPage(self.driver)
        mp.refresh_main()
        if self.menu1 != '':
            mp.open_menu(self.menu1)
        #time.sleep(0.3)
        
        if self.menu2 != '':
            mp.open_menu(self.menu2  )
        #time.sleep(0.3)
    
if __name__ == '__main__':
    unittest.main()
