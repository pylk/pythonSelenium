import os
import sys
sys.path.append('../../../../')
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from test_case.running.html5.app_test import AppTest
from test_case.models.driver import browser
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.login_page import LoginPage
from test_case.page_obj.cross_report_page import CrossReportPage


class CrossReportTest(AppTest):
    '''交叉报表测试'''

    menu1 = '报表'
    menu2 = '交叉报表'

    def test_type(self):
        '''类型'''
        cr = CrossReportPage(self.driver)
        self.assertIn('crossreport',cr.check_type(),msg='交叉报表类型校验不通过')

    def test_summary(self):
        '''汇总'''
        cr = CrossReportPage(self.driver)
        self.assertTrue(cr.check_summary(),msg='交叉报表汇总校验不通过')

    def test_total(self):
        '''总计'''
        cr = CrossReportPage(self.driver)
        self.assertTrue(cr.check_total(),msg='交叉报表总计校验不通过')

    def scroll_to(self, y):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        script = 'var $con = $("#_contentTable");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        #time.sleep(0.1)

    def setUp(self):
        print('-------%s' %self)
        
        mp = MainPage(self.driver)
        mp.refresh_main()
        if self.menu1 != '':
            mp.open_menu(self.menu1)
        #time.sleep(0.2)
        
        if self.menu2 != '':
            mp.open_menu(self.menu2)
        #time.sleep(0.2)

        mp.switch_to_iframe()

    def init(self):
        # self.test_type()
        # self.test_summary()
        self.test_total()

if __name__ == '__main__':
    unittest.main()