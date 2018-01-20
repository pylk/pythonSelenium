import os,sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.view.queryform_gantt_view_page import QueryFormGanttViewPage
from test_case.page_obj.main_page import MainPage


class QueryFormGanttViewTest(ViewTest):
    '''查询表单-甘特视图测试'''

    menu1 = '视图'
    menu2 = '查询表单'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)


    def test_open_fold_query(self):
        '''查询表单-甘特视图的折叠展开'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        gv.open_fold_query(1) #点击查询按钮展开
        self.assertTrue(gv.get_openfold_query_return(),msg='查询表单-甘特视图打开校验不通过')
        gv.open_fold_query(1) #点击查询按钮
        time.sleep(2)
        self.assertFalse(gv.get_openfold_query_return(),msg='查询表单-甘特视图折叠校验不通过')

    def test_single_input(self):
        '''单行文本框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        gv.open_fold_query(1)
        self.assertTrue(gv.single_input(),msg='查询表单_甘特视图单行文本框查询校验不通过')

    def test_multiline_textbox(self):
        '''多行文本框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.multiline_textbox(),msg='查询表单_甘特视图多行文本框查询校验不通过')

    def test_multiline_textbox_reset(self):
        '''重置设置查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.multiline_textbox_reset(),msg='查询表单_甘特视图重置按钮校验不通过')

    def test_radio(self):
        '''单选框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.radio(),msg='查询表单_甘特视图单选框查询校验不通过')

    def test_multiselect(self):
        '''多选框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.multiselect(), msg='查询表单_甘特视图多选框校验查询不通过')

    def test_drop_down(self):
        '''下拉框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.drop_down(), msg='查询表单_甘特视图下拉框校验查询不通过')

    def test_date_selection(self):
        '''日期选择框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.date_selection(), msg='查询表单_甘特视图日期选择框校验查询不通过')

    def test_department_selection(self):
        '''部门选择框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.department_selection(), msg='查询表单_甘特视图部门选择框查询校验不通过')

    def test_tree_department_selection(self):
        '''树形部门选择框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.tree_department_selection(), msg='查询表单_甘特视图树形部门选择框查询校验不通过')

    def test_user_selection(self):
        '''用户选择框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.user_selection(), msg='查询表单_甘特视图用户选择框查询校验不通过')

    def test_left_right_selection(self):
        '''左右选择框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.left_right_selection(), msg='查询表单_甘特视图用户选择框查询校验不通过')

    def test_smart_alert(self):
        '''智能提示选择框查询'''
        menu3 = '查询表单_甘特视图'
        self.open_menu3(menu3)
        gv = QueryFormGanttViewPage(self.driver)
        gv.close_righttop_message()
        gv.switch_to_iframe()
        self.assertTrue(gv.smart_alert(), msg='查询表单_甘特视图智能提示选择框查询校验不通过')

    def init(self):
        # self.test_open_fold_query()
#         self.test_single_input()
#         self.test_multiline_textbox()
#         self.test_multiline_textbox_reset()
        # self.test_radio()
        # self.test_multiselect()
        # self.test_drop_down()
        # self.test_date_selection()
        # self.test_department_selection()
        # self.test_tree_department_selection()
        # self.test_user_selection()
        # self.test_left_right_selection()
        # self.test_left_right_selection()
        self.test_smart_alert()

if __name__ == '__main__':
    unittest.main()