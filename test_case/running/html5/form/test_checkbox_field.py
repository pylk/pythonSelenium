import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.checkbox_page import CheckboxPage
from selenium.webdriver.support.ui import Select


class CheckboxTest(ComponentTest):
    '''复选框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '复选框'

    def test_type_case(self):
        '''类型'''
        name = '复选框_名称'
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        a = comp.elements[2].get_attribute('type')
        self.assertEqual('checkbox', a, msg=name + '检验不通过')

    def test_readonly_case(self):
        '''显示只读和条件只读'''
        name = '复选框_只读'
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        r = comp.elements[1].get_attribute('disabled')
        self.assertTrue(r, msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '复选框_刷新'
        #time.sleep(0.5)
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        comp.elements[2].click()
        r = comp.elements[2].is_selected()
        comp.wait_refresh_loading_back_show_then_hide()
        val2 = self.driver.find_elements_by_name('复选框_重计算')[2].is_selected()
        self.assertTrue(val2, msg='单选框刷新_重计算检验不通过')

    def test_verticallayout_case(self):
        """复选框垂直布局"""
        name = '复选框_垂直布局'
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        self.assertIsNotNone(comp.verticallayout_test, msg=name + '检验不通过')

    def test_valuescript_case(self):
        '''复选框_值脚本'''
        #time.sleep(0.5)
        name = '复选框_值脚本'
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        self.assertTrue(comp.valuescript_test(name,"2"), msg=name + '检验不通过')

    def test_designpattern_case(self):
        '''复选框设计模式'''
        #time.sleep(0.5)
        name = '复选框_选项脚本设计模式'
        comp = CheckboxPage(self.driver,name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[1])
        #time.sleep(0.5)
        comp.elements[2].click()
        #time.sleep(0.5)
        self.assertTrue(comp.valuescript_test(name,"2"), msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验'''
        #time.sleep(0.5)
        name = '复选框_非空校验'
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        self.assertIn("'复选框_非空校验'必须填写", comp.notnull_test(), msg=name + '检验不通过')

    def test_hide_case(self):
        '''条件隐藏'''
        name = '复选框_隐藏条件'
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        a = comp.elements[2].is_displayed()
        self.assertFalse(a, msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = 'span_复选框_隐藏时显示值'
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        self.assertIn("控件已隐藏", comp.get_text_by_css_selector('span[name="' + name + '"] > span:nth-last-child(1)'), msg=name + '检验不通过')

    def test_display_case(self):
        """条件只读"""
        name = '复选框_只读条件'
        comp = CheckboxPage(self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        r = comp.elements[1].get_attribute('disabled')
        self.assertTrue(r, msg=name + '检验不通过')

    def init(self):
        '''类型、只读、隐藏属性测试'''
        self.test_type_case()
        self.test_readonly_case()
        self.test_refresh_calculate_case()
        self.test_verticallayout_case()
        self.test_valuescript_case()
        self.test_designpattern_case()
        self.test_not_null_case()
        self.test_hide_case()
        self.test_show_when_hide_case()
        self.test_display_case()

if __name__ == '__main__':
    unittest.main()
