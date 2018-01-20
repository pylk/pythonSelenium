from selenium import webdriver
import unittest
import os
import sys
import time
from test_case.models.driver import browser
from test_case.running.html5.app_test import AppTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.login_page import LoginPage


class ViewTest(AppTest):
    
    def setUp(self):
        mp = MainPage(self.driver)

        mp.refresh_main()
        if self.menu1 != '':
            mp.open_menu(self.menu1)
        
        if self.menu2 != '':
            mp.open_menu(self.menu2)

        
    def scroll_to(self, y):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        script = 'var $con = $("#_contentTable");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        #time.sleep(0.1)
        