from selenium import webdriver
import unittest
import os
import sys
sys.path.append('../../../')
import time
from test_case.models.driver import phone_browser
from test_case.running.phone.app_test import AppPhoneTest
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.login_page import LoginPage


class FlowPhoneTest(AppPhoneTest):

    def setUp(self):
        mp = MainPhonePage (self.driver)
        po = LoginPage(self.driver)
        po.user_login('liling', '123456')  # 切换李玲登陆
        mp.switch_to_menu_page ()
        mp.open_menus (self.menu1, self.menu2, self.menu3)


    #def tearDown(self):
     #  self.driver.quit ()
