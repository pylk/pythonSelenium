import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.radio_page import RadioPage
from selenium.webdriver.support.ui import Select


class RadioTest(ComponentTest):
    '''单选框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '单选框'  # 主页打开菜单时使用

    def test_type_case(self):
        '''类型'''
        name = '单选框_名称'
        comp = RadioPage(self.driver, name)
        bool = comp.elements_attr_test('type','radio')
        self.assertTrue(bool,msg=name + '检验不通过')

    def test_readonly_case(self):
        '''显示只读和条件只读'''
        name = '单选框_只读'
        comp = RadioPage(self.driver, name)
        bool = comp.elements_attr_test ('disabled', 'true')
        self.assertTrue (bool, msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '单选框_刷新'
        name2 = '单选框_重计算'
        num = 0
        comp = RadioPage (self.driver, name)
        target_element = self.driver.find_elements_by_name(name)[0]
        comp.scroll_to_target_element(target_element)
        #time.sleep(0.5)
        for i in self.driver.find_elements_by_name(name):
            i.click()
            comp.wait_refresh_loading_back_show_then_hide()
            val2 = self.driver.find_elements_by_name(name2)[num].is_selected()
            self.assertTrue(val2, msg='单选框刷新_重计算检验不通过')
            num += 1

    def test_verticallayout_case(self):
        """单选框垂直布局"""
        self.scroll_to('0')
        name = 'span_单选框_垂直布局'
        comp = RadioPage(self.driver, name)
        self.assertIsNotNone(comp.verticallayout_test(), msg=name + '检验不通过')


    def test_valuescript_case(self):
        '''单选框_值脚本'''
        self.scroll_to('300')
        #time.sleep(0.5)
        name = '单选框_值脚本'
        comp = RadioPage(self.driver, name)
        self.assertTrue(comp.valuescript_test(name,"2"), msg=name + '检验不通过')

    def test_designpattern_case(self):
        '''单选框设计模式'''
        #time.sleep(0.5)
        name = '单选框_选项脚本设计模式'
        comp = RadioPage(self.driver, name)
        comp.elements[1].click()
        #time.sleep(0.5)
        self.assertTrue(comp.valuescript_test(name,"2"), msg='单选框_选项脚本设计模式检验不通过')


    def test_not_null_case(self):
        '''非空校验'''
        self.scroll_to('550')
        name = 'span_单选框_非空校验'
        comp = RadioPage(self.driver, name)
        self.assertIn("'单选框_非空校验'必须填写", comp.notnull_test(), msg=name + '检验不通过')


    def test_hide_case(self):
        '''条件隐藏'''
        name = '单选框_隐藏条件'
        self.scroll_to('550')
        bool = self.driver.find_elements_by_name('单选框_隐藏条件')[1].is_displayed()
        self.assertFalse(bool, msg=name + '检验不通过')


    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        self.scroll_to('750')
        name = 'span_单选框_隐藏时显示值'
        comp = RadioPage(self.driver, name)
        self.assertTrue(comp.show_when_hide("控件已隐藏"), msg=name + '检验不通过')

    def test_display_case(self):
        """条件只读"""
        self.scroll_to('550')
        name = '单选框_只读条件'
        comp = RadioPage(self.driver, name)
        r = comp.elements[1].get_attribute('disabled')
        self.assertTrue(r, msg=name + '检验不通过')

    def init(self):
        '''类型、只读、隐藏属性测试'''
#         self.test_type_case()
#         self.test_readonly_case()
#         self.test_refresh_calculate_case()
#         self.test_verticallayout_case()
#         self.test_desription_case()
#         self.test_valuescript_case()
        self.test_designpattern_case()
#         self.test_not_null_case()
#         self.test_hide_case()
#         self.test_show_when_hide_case()


if __name__ == '__main__':
    unittest.main()
