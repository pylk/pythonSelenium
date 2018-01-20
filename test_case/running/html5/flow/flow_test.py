import unittest
import sys
sys.path.append('../../../')
import time
from test_case.page_obj.main_page import MainPage
from test_case.running.html5.app_test import AppTest
from test_case.models.driver import phone_browser
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.login_page import LoginPage


class FlowTest(AppTest):
    
    def open_3_menus(self):
        '''打开一、二、三级菜单'''
        
        mp = MainPage(self.driver)

        if self.menu1 != '':
            mp.open_menu(self.menu1)
        
        if self.menu2 != '':
            mp.open_menu(self.menu2)

        if self.menu3 != '':
            mp.open_menu(self.menu3)


    
    def setUp(self):
        mp = MainPage(self.driver)
        mp.refresh_main()
        self.open_3_menus()
        mp.switch_to_iframe()
        mp.wait_loading_hide()
        mp.wait_elem_visible('#activityTable') #等待按钮栏可见

    def scroll_to(self, y):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        script = 'var $con = $("#_contentTable");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        #time.sleep(0.1)


