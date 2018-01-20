import os,sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.view.queryform_tree_view_page import QueryFormTreeViewPage
from test_case.page_obj.main_page import MainPage


class QueryFormTreeViewTest(ViewTest):
    '''查询表单-树形视图测试'''

    menu1 = '视图'
    menu2 = '查询表单'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.3)

    def test_open_fold_query(self):
        '''查询表单-树形视图的折叠展开'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        tv.open_fold_query(2)
        time.sleep(0.5) #必须
        self.assertTrue(tv.get_openfold_query_return(), msg='查询表单_树形视图打开校验不通过')
        tv.open_fold_query(2)
        time.sleep(0.5) #必须
        self.assertFalse(tv.get_openfold_query_return(), msg='查询表单_树形视图折叠校验不通过')

    def test_single_input(self):
        '''单行文本框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertEqual(None,tv.single_input(), msg='查询表单-树形视图单行文本框查询校验不通过')

    def test_multiline_textbox(self):
        '''多行文本框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.multiline_textbox(), msg='查询表单-树形视图多行文本框查询校验不通过')

    def test_multiline_textbox_reset(self):
        '''重置设置查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertTrue(tv.multiline_textbox_reset(), msg='查询表单-树形视图重置按钮校验不通过')

    def test_radio(self):
        '''单选框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.radio(), msg='查询表单-树形视图单选框查询校验不通过')

    def test_multiselect(self):
        '''多选框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.multiselect(), msg='查询表单-树形视图多选框校验查询不通过')

    def test_drop_down(self):
        '''下拉框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.drop_down(), msg='查询表单-树形视图下拉框校验查询不通过')

    def test_date_selection(self):
        '''日期选择框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.date_selection(), msg='查询表单-树形视图日期选择框校验查询不通过')

    def test_department_selection(self):
        '''部门选择框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.department_selection(), msg='查询表单-树形视图部门选择框查询校验不通过')

    def test_tree_department_selection(self):
        '''树形部门选择框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.tree_department_selection(), msg='查询表单-树形视图树形部门选择框查询校验不通过')

    def test_user_selection(self):
        '''用户选择框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.user_selection(), msg='查询表单-树形视图用户选择框查询校验不通过')

    def test_left_right_selection(self):
        '''左右选择框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.left_right_selection(), msg='查询表单-树形视图用户选择框查询校验不通过')

    def test_smart_alert(self):
        '''智能提示选择框查询'''
        menu3 = '查询表单_树形视图'
        self.open_menu3(menu3)
        tv = QueryFormTreeViewPage(self.driver)
        tv.close_righttop_message()
        tv.switch_to_iframe()
        tv.wait_loading_hide()
        tv.switch_to_right_iframe()
        self.assertFalse(tv.smart_alert(), msg='查询表单-树形视图智能提示选择框查询校验不通过')

    def init(self):
        # self.test_open_fold_query()
#         self.test_single_input()
        # self.test_multiline_textbox()
        # self.test_multiline_textbox_reset()
        # self.test_radio()
        # self.test_multiselect()
        self.test_drop_down()
        # self.test_date_selection()
        # self.test_department_selection()
        # self.test_tree_department_selection()
        # self.test_user_selection()
        # self.test_left_right_selection()
        # self.test_smart_alert()

if __name__ == '__main__':
    unittest.main()
