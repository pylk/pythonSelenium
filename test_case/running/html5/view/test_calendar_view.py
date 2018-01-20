import random
import os
import sys
sys.path.append('../../../../')
import time
import datetime
import unittest
from selenium.webdriver.common.keys import Keys
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.view.calendar_view_page import CalendarviewPage
sys.path.append('../')


class CalendarViewTest(ViewTest):
    '''日历视图'''
    
    menu1 = '视图'
    menu2 = '日历视图'
    menu3 = '日历视图_case001'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.3)
        mp.switch_to_iframe()
        mp.wait_loading_hide()
    
    def test_new_case(self):
        '''日历视图新建记录'''
        self.open_menu3(self.menu3)
        name = "日历视图新建记录"
        comp = CalendarviewPage(self.driver)
        btn = ButtonPage(self.driver)
        num = comp.buildnum()
        text = '自动化测试'+num
        comp.new_record(text)
        bool = comp.check_add(text)
        self.assertTrue(bool,msg=name + '检验不通过')

    def test_gotodayview_case(self):
        '''进入日历视图日视图'''
        self.open_menu3(self.menu3)
        name = "进入日历视图日视图"
        comp = CalendarviewPage(self.driver)
        comp.switch_calendartype("日视图")
        text = comp.get_dayandweek_title()
        self.assertEqual('时间 内容',text,msg=name + '检验不通过')

    def test_gotoweekview_case(self):
        '''进入日历视图周视图'''
        self.open_menu3(self.menu3)
        name = "进入日历视图周视图"
        comp = CalendarviewPage(self.driver)
        comp.switch_calendartype("周视图")
        text = comp.get_dayandweek_title()
        self.assertEqual('周 内容',text,msg=name + '检验不通过')

    def test_gotomonthview_case(self):
        '''进入日历视图月视图'''
        self.open_menu3(self.menu3)
        name = "进入日历视图月视图"
        comp = CalendarviewPage(self.driver)
        comp.switch_calendartype("月视图")
        text = comp.get_month_title()
        self.assertEqual('星期日 星期一 星期二 星期三 星期四 星期五 星期六',text,msg=name + '检验不通过')

    def test_gomore_case(self):
        '''进入more'''
        #time.sleep(0.5)
        self.open_menu3(self.menu3)
        name = "进入日历视图more"
        comp = CalendarviewPage(self.driver)
        comp.goto_yearmonth(7,8)
        #time.sleep(0.5)
        comp.click_more()
        text = comp.get_viewText()
        self.assertIn("\n任务1\n任务2\n任务3\n任务4",text,msg=name + '检验不通过')

    def init(self):
        self.test_new_case()
        self.test_gotodayview_case()
        self.test_gotoweekview_case()
        self.test_gotomonthview_case()
        self.test_gomore_case()


if __name__ == '__main__':
    unittest.main()
