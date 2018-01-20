import os
import sys
import time
import unittest
sys.path.append('../../../../')
from selenium.webdriver.common.keys import Keys
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.view.gantt_view_page import GanttViewPage


class GanttViewTest(ViewTest):
    '''甘特视图'''
    
    menu1 = '视图'
    menu2 = '甘特视图'
    menu3 = '甘特视图_case001'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.3)
        mp.switch_to_iframe()
        mp.wait_loading_hide()

    def test_new_case(self):
        '''甘特视图新建记录'''
        self.open_menu3(self.menu3)
        name = "甘特视图新建记录"
        text = '自动化测试'
        comp = GanttViewPage(self.driver)
        btn = ButtonPage(self.driver)
        comp.judge_delete(text)
        #time.sleep(0.5)
        btn.click_activityTable_button(btn.new_btn)
        #time.sleep(0.5)
        comp.find_elem('input[name="名称"]').send_keys(text)
        comp.find_elem('input[name="开始时间"]').send_keys("2017-07-16")
        comp.find_elem('input[name="结束时间"]').send_keys("2017-08-01")
        comp.find_elem('input[name="完成度"]').send_keys("60")
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        btn.click_button(btn.to_return)
        btn.wait_loading_hide()  #表单中
        #time.sleep(0.5)
        bool = comp.check_add(text)
        self.assertTrue(bool,msg=name + '检验不通过')

    def test_month_case(self):
        '''甘特视图月表示'''
        self.open_menu3(self.menu3)
        comp = GanttViewPage(self.driver)
        name = '甘特视图月表示'
        comp.find_elem_is_clickable('.fn-content > div > input[type="radio"]:nth-child(1)').click()
        #time.sleep(0.5)
        bool1 = comp.checkhour()
        self.assertFalse(bool1, msg=name + '检验不通过')
        bool2 = comp.check_hang('3')
        self.assertFalse(bool2, msg=name + '检验不通过')


    def test_week_case(self):
        '''甘特视图周表示'''
        comp = GanttViewPage(self.driver)
        self.open_menu3(self.menu3)
        name = "甘特视图周表示"
        comp.find_elem_is_clickable('.fn-content > div > input[type="radio"]:nth-child(2)').click()
        #time.sleep(0.5)
        bool1 = comp.checkhour()
        self.assertFalse(bool1,msg=name + '检验不通过')
        bool2 = comp.check_hang('4')
        self.assertFalse(bool2, msg=name + '检验不通过')


    def test_hour_case(self):
        '''甘特视图小时表示'''
        comp = GanttViewPage(self.driver)
        self.open_menu3(self.menu3)
        name = "甘特视图小时表示"
        comp.find_elem_is_clickable('.fn-content > div > input[type="radio"]:nth-child(4)').click()
        #time.sleep(0.5)
        bool1 = comp.checkhour()
        self.assertTrue(bool1,msg=name + '检验不通过')


    def test_day_case(self):
        '''甘特视图日表示'''
        comp = GanttViewPage(self.driver)
        self.open_menu3(self.menu3)
        name = "甘特视图日表示"
        comp.find_elem_is_clickable('.fn-content > div > input[type="radio"]:nth-child(3)').click()
        #time.sleep(0.5)
        bool1 = comp.checkhour()
        self.assertFalse(bool1,msg=name + '检验不通过')
        bool2 = comp.check_hang('4')
        self.assertTrue(bool2, msg=name + '检验不通过')

    def init(self):
#         self.test_hour_case()
#         self.test_day_case()
#         self.test_week_case()
#         self.test_month_case()
        self.test_new_case()

if __name__ == '__main__':
    unittest.main()







    



