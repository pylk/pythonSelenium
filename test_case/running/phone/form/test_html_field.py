import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.form.html_page import HtmlPhonePage


class HtmlPhoneTest(ComponentPhoneTest):
    '''html编辑器测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = 'Html控件'
    
    def test_type_case(self):
        '''名称'''
        name = 'html编辑器_名称'
        comp = HtmlPhonePage(self.driver, name)
        self.assertIsNotNone(comp.check_dom(), msg=name + '检验不通过')
         
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = 'html编辑器_重计算'
        comp = HtmlPhonePage(self.driver, name)
        self.assertIsNotNone(comp.check_dom(), msg=name + '检验不通过')
        input = InputPhonePage(self.driver, '单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertFalse(comp.is_displayed(), msg=name + '检验不通过')
 
    def test_desription_case(self):
        '''描述'''
        name = 'html编辑器_描述'
        comp = HtmlPhonePage(self.driver, name)
        self.assertTrue(comp.is_desription_effect(name), msg=name + '检验不通过')
        
    def test_value_case(self):
        '''值脚本(iscript模式)'''
        name = 'html编辑器_值脚本'
        comp = HtmlPhonePage(self.driver, name)
        self.assertEqual('aaa', comp.get_the_value(), msg=name + '检验不通过')
 
    def test_readonly_case(self):
        '''只读条件'''
        name = 'html编辑器_只读条件'
        comp = HtmlPhonePage(self.driver, name)
        self.assertEqual('bbb', comp.get_readonly_div_text(), msg=name + '检验不通过')
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_value_case()
        self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
