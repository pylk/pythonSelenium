import os,sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.view.queryform_calendar_view_page import QueryFormCalendarViewPage
from test_case.page_obj.view.calendar_view_page import CalendarviewPage
from test_case.page_obj.main_page import MainPage


class QueryFormCalendarViewTest(ViewTest):
    '''查询表单-日历视图测试'''

    menu1 = '视图'
    menu2 = '查询表单'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.3)

    def test_open_fold_query(self):
        '''查询表单-日历视图的折叠展开'''
        menu3 = '查询表单_日历视图'
        cv = CalendarviewPage(self.driver)
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)    # 判断是否需要切换页面
        dv.open_fold_query(1)
        time.sleep(0.5) #必须
        self.assertTrue(dv.get_openfold_query_return(),msg='查询表单-日历视图打开校验不通过')
        dv.open_fold_query(1)
        time.sleep(0.5) #必须
        self.assertFalse(dv.get_openfold_query_return(),msg='查询表单-日历视图折叠校验不通过')

    def test_single_input(self):
        '''单行文本框查询'''
        menu3 = '查询表单_日历视图'
        cv = CalendarviewPage(self.driver)
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        #time.sleep(0.5)
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        dv.open_fold_query(1)
        #time.sleep(0.5)
        self.assertTrue(dv.single_input(),msg='查询表单-日历视图单行文本框查询校验不通过')

    def test_multiline_textbox(self):
        '''多行文本框查询'''
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv = CalendarviewPage(self.driver)
        cv.goto_yearmonth(7,7)
        #cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.multiline_textbox(),msg='查询表单_日历视图多行文本框查询校验不通过')

    def test_multiline_textbox_reset(self):
        '''重置设置查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.multiline_textbox_reset(),msg='查询表单_日历视图重置按钮校验不通过')

    def test_radio(self):
        '''单选框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.radio(),msg='查询表单_日历视图单选框查询校验不通过')

    def test_multiselect(self):
        '''多选框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.multiselect(), msg='查询表单_日历视图多选框校验查询不通过')

    def test_drop_down(self):
        '''下拉框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.drop_down(), msg='查询表单_日历视图下拉框校验查询不通过')

    def test_date_selection(self):
        '''日期选择框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.date_selection(), msg='查询表单_日历视图日期选择框校验查询不通过')

    def test_department_selection(self):
        '''部门选择框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.department_selection(), msg='查询表单_日历视图部门选择框查询校验不通过')

    def test_tree_department_selection(self):
        '''树形部门选择框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()  #切入iframe
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.tree_department_selection(), msg='查询表单_日历视图树形部门选择框查询校验不通过')

    def test_user_selection(self):
        '''用户选择框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.user_selection(), msg='查询表单_日历视图用户选择框查询校验不通过')

    def test_left_right_selection(self):
        '''左右选择框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.left_right_selection(), msg='查询表单_日历视图用户选择框查询校验不通过')

    def test_smart_alert(self):
        '''智能提示选择框查询'''
        cv = CalendarviewPage(self.driver)
        menu3 = '查询表单_日历视图'
        self.open_menu3(menu3)
        dv = QueryFormCalendarViewPage(self.driver)
        dv.close_righttop_message() #关闭消息中心的提示框
        dv.switch_to_iframe()
        cv.goto_yearmonth(7,7)  # 判断是否需要切换页面
        self.assertTrue(dv.smart_alert(), msg='查询表单_日历视图智能提示选择框查询校验不通过')

    def init(self):
#         self.test_open_fold_query()
#         self.test_single_input()
        # self.test_multiline_textbox()
        self.test_multiline_textbox_reset()
        # self.test_radio()
        # self.test_multiselect()
        # self.test_drop_down()
#         self.test_date_selection()
#         self.test_department_selection()
        # self.test_tree_department_selection()
        # self.test_user_selection()
        # self.test_left_right_selection()
        # self.test_smart_alert()

if __name__ == '__main__':
    unittest.main()