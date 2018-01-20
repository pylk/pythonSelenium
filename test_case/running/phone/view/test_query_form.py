import sys
import time
import unittest
from selenium.webdriver.remote.switch_to import SwitchTo
sys.path.append('../../../../')
from test_case.running.phone.view.view_test import ViewPhoneTest
from test_case.page_obj.view.queryform_list_view_page import QueryFormPhonePage
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.form.textarea_page import TextareaPhonePage
from test_case.page_obj.form.radio_page import RadioPhonePage
from test_case.page_obj.form.checkbox_page import CheckboxPhonePage
from test_case.page_obj.form.select_page import SelectPhonePage
from test_case.page_obj.form.date_field_page import DatePhonePage
from test_case.page_obj.form.department_page import DepartmentPhonePage
from test_case.page_obj.form.tree_department_page import TreeDepartmentPhonePage
from test_case.page_obj.form.user_select_page import UserSelectPhonePage
from test_case.page_obj.form.suggest_page import SuggestPhonePage
from test_case.page_obj.button_page import ButtonPhonePage

from test_case.page_obj.view.list_view_page import ListViewPhonePage



class QueryFormPhoneTest(ViewPhoneTest):
    '''查询表单测试'''

    menu1 = '视图'
    menu2 = '查询表单'
    menu3 = '查询表单_列表视图'

    '''
    @param type: 控件类型，如单行为input
    @param comp_name: 控件名称
    @param val: 要输入的值
    @param col_num: 第几列
    '''
    def set_val_by_component_type(self, type, comp_name, val):
        '''根据类型初始化控件并设置控件值'''
        col_num = '2'
        
        if type == 'input':
            comp = InputPhonePage(self.driver, comp_name)
            comp.set_val(val) # 输入文本
            col_num = '2'
        if type == 'textarea':
            comp = TextareaPhonePage(self.driver, comp_name)
            comp.set_val(val) # 输入文本
            col_num = '3'
        if type == 'radio':
            comp = RadioPhonePage(self.driver, comp_name)
            comp.set_val(val) # 输入文本
            col_num = '4'
        if type == 'checkbox':
            comp = CheckboxPhonePage(self.driver, comp_name)
            comp.set_val(val) # 输入文本
            col_num = '5'
        if type == 'select':
            comp = SelectPhonePage(self.driver, comp_name)
            comp.set_val(val) # 输入文本
            col_num = '6'
        if type == 'date':
            comp = DatePhonePage(self.driver, comp_name)
            comp.set_val(val) # 输入文本
            col_num = '7'
        if type == 'depart':
            comp = DepartmentPhonePage(self.driver, comp_name)
            comp.set_val(val) # 输入文本
            col_num = '8'
        if type == 'tree_depart':
            comp = TreeDepartmentPhonePage(self.driver)
            comp.select_depts(comp_name, [val]) # 输入文本
            col_num = '9'
        if type == 'user':
            comp = UserSelectPhonePage(self.driver, comp_name)
            comp.set_val(val) # 输入文本
            col_num = '10'
        if type == 'suggest':
            comp = SuggestPhonePage(self.driver, (comp_name + '_show'))
            comp.set_val(val) # 输入文本
            col_num = '12'
        if type == 'reset':
            comp = ButtonPhonePage(self.driver)
            comp.click_button('重置')
            col_num = '3'
        
        return col_num
    
    def open_menu_send_keys_search(self, type, comp_name, val):
        '''打开菜单设置控件值并查询和返回检验结果'''
        
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, self.menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        qf = QueryFormPhonePage(self.driver)
        
        qf.wait_Tabloading_show_then_hide()
        lp.set_td_by_title(comp_name)   #设置显示列
        qf.click_fold_query()   # 点击查询按钮
        time.sleep(0.3) #时间稳定，等查询页面展示，中间无loading，不受服务器速度影响，作判断无意义
        col_num = self.set_val_by_component_type(type, comp_name, val)  # 设置查询控件值并返回当前检验是第几列
        qf.click_search() # 点击查询按钮
        qf.wait_Tabloading_show_then_hide()
        return col_num
    
    def open_menu_send_keys_search_check(self, type, comp_name, val):
        '''打开菜单设置控件值并查询和返回检验结果'''
        col_num = self.open_menu_send_keys_search(type, comp_name, val)
        qf = QueryFormPhonePage(self.driver)
        return qf.check_search_result(col_num, val)
    
    def test_open_fold_query(self):
        '''查询表单-列表视图的折叠展开'''
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, self.menu3)  # 打开菜单
        qf = QueryFormPhonePage(self.driver)
        qf.click_fold_query()   # 点击查询按钮
        #time.sleep(0.5)
        self.assertTrue(qf.is_open_query_page(), msg='查询表单-列表视图打开校验不通过')
        qf.click_close_query()   # 点击关闭查询表单的图标
        time.sleep(0.3) # 必须，时间稳定。过程无loading，判断查询表单消失/消失后的界面再断言没有意义
        self.assertFalse(qf.is_open_query_page(), msg='查询表单-列表视图打开校验不通过')

    def test_single_input(self):
        '''单行文本框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('input', '单行文本框', 'test1'), msg='查询表单-列表视图单行文本框查询校验不通过')

    def test_textarea(self):
        '''多行文本框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('textarea', '多行文本框', 'test1'), msg='查询表单-列表视图多行文本框查询校验不通过')
 
    def test_reset(self):
        '''重置设置查询'''
        col_num = self.open_menu_send_keys_search('reset', '多行文本框', '')
        qf = QueryFormPhonePage(self.driver)
        self.assertTrue(qf.check_result_4_reset(col_num, ['test1', 'test2', 'test3']), msg='查询表单-列表视图重置按钮校验不通过')
 
    def test_radio(self):
        '''单选框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('radio', '单选框', '男'), msg='查询表单-列表视图单选框查询校验不通过')
 
    def test_checkbox(self):
        '''多选框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('checkbox', '多选框', '苹果'), msg='查询表单-列表视图多选框校验查询不通过')
 
    def test_select(self):
        '''下拉框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('select', '下拉框', '广州'), msg='查询表单-列表视图下拉框校验查询不通过')
 
    def test_date_selection(self):
        '''日期选择框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('date', '日期选择框', '2018-02-04'), msg='查询表单-列表视图日期选择框校验查询不通过')
 
    def test_department(self):
        '''部门选择框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('depart', '部门选择框', '产品部'), msg='查询表单-列表视图部门选择框查询校验不通过')
 
    def test_tree_department(self):
        '''树形部门选择框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('tree_depart', '树形部门选择框', '产品部'), msg='查询表单-列表视图树形部门选择框查询校验不通过')
 
    def test_user_selection(self):
        '''用户选择框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('user', '用户选择框', '李玲'), msg='查询表单-列表视图用户选择框查询校验不通过')
 
    def test_smart_alert(self):
        '''智能提示选择框查询'''
        self.assertTrue(self.open_menu_send_keys_search_check('suggest', '智能提示选择框', 'aa'), msg='查询表单-列表视图智能提示选择框查询校验不通过')

    def init(self):
#         self.test_open_fold_query()
#         self.test_single_input()
#         self.test_textarea()
#         self.test_reset()
#         self.test_radio()
#         self.test_checkbox()
#         self.test_select()
#         self.test_date_selection()
#         self.test_department()
        self.test_tree_department()
#         self.test_user_selection()
#         self.test_smart_alert()

if __name__ == '__main__':
     unittest.main()