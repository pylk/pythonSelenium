import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.view.queryform_list_view_page import QueryFormListViewPage
from test_case.page_obj.main_page import MainPage


class QueryFormListViewTest(ViewTest):
    '''查询表单-列表视图测试'''

    menu1 = '视图'
    menu2 = '查询表单'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)

    def test_open_fold_query(self):
        '''查询表单-列表视图的折叠展开'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.wait_loading_hide()   # 等待视图loading图标消失
        qf.close_righttop_message() # 关闭右上角的消息提示
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        qf.open_fold_query(2)   # 点击高级展开查询头
        time.sleep(0.5) #必须
        self.assertTrue(qf.get_openfold_query_return(),msg='查询表单-列表视图打开校验不通过')
        qf.open_fold_query(2)
        time.sleep(0.5) #必须
        self.assertFalse(qf.get_openfold_query_return(),msg='查询表单-列表视图折叠校验不通过')

    def test_single_input(self):
        '''单行文本框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message() # 关闭右上角的消息提示
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.single_input(),msg='查询表单-列表视图单行文本框查询校验不通过')

    def test_multiline_textbox(self):
        '''多行文本框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message() # 关闭右上角的消息提示
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.multiline_textbox(),msg='查询表单-列表视图多行文本框查询校验不通过')

    def test_multiline_textbox_reset(self):
        '''重置设置查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertTrue(qf.multiline_textbox_reset(),msg='查询表单-列表视图重置按钮校验不通过')

    def test_radio(self):
        '''单选框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.radio(),msg='查询表单-列表视图单选框查询校验不通过')

    def test_multiselect(self):
        '''多选框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.multiselect(), msg='查询表单-列表视图多选框校验查询不通过')

    def test_drop_down(self):
        '''下拉框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.drop_down(), msg='查询表单-列表视图下拉框校验查询不通过')

    def test_date_selection(self):
        '''日期选择框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.date_selection(), msg='查询表单-列表视图日期选择框校验查询不通过')

    def test_department_selection(self):
        '''部门选择框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.department_selection(), msg='查询表单-列表视图部门选择框查询校验不通过')

    def test_tree_department_selection(self):
        '''树形部门选择框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message() #关闭消息提示
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.tree_department_selection(), msg='查询表单-列表视图树形部门选择框查询校验不通过')

    def test_user_selection(self):
        '''用户选择框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.user_selection(), msg='查询表单-列表视图用户选择框查询校验不通过')

    def test_left_right_selection(self):
        '''左右选择框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.left_right_selection(), msg='查询表单-列表视图用户选择框查询校验不通过')

    def test_smart_alert(self):
        '''智能提示选择框查询'''
        menu3 = '查询表单_列表视图'
        self.open_menu3(menu3)
        qf = QueryFormListViewPage(self.driver)
        qf.close_righttop_message()
        qf.switch_to_iframe()
        qf.wait_loading_hide()
        self.assertFalse(qf.smart_alert(), msg='查询表单-列表视图智能提示选择框查询校验不通过')

    def init(self):
        # self.test_open_fold_query()
        # self.test_single_input()
        # self.test_multiline_textbox()
        # self.test_multiline_textbox_reset()
        # self.test_radio()
        self.test_multiselect()
        # self.test_drop_down()
#         self.test_date_selection()
#         self.test_department_selection()
        # self.test_tree_department_selection()
        # self.test_user_selection()
        # self.test_left_right_selection()
        # self.test_smart_alert()

if __name__ == '__main__':
     unittest.main()