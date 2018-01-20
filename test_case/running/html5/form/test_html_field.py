import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.html_page import HtmlPage
from test_case.page_obj.button_page import ButtonPage


class HtmlTest(ComponentTest):
    '''html编辑器测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = 'Html控件'
    
    def test_type_case(self):
        '''名称'''
        name = 'html编辑器_名称'
        comp = HtmlPage(self.driver, name)
        self.assertIsNotNone(comp.get_the_div(), msg=name + '检验不通过')
        self.assertIsNotNone(comp.get_the_div_iframe(), msg=name + '检验不通过')
        
    def test_size_px_case(self):
        '''大小(像素)'''
        name = 'html编辑器_大小_像素'
        comp = HtmlPage(self.driver, name)
        comp.from_scroll_to('450')
        self.assertEqual(800, comp.get_the_div_width(), msg=name + '检验不通过')
        self.assertEqual(400, comp.get_the_div_height(), msg=name + '检验不通过')
        
    def test_size_percent_case(self):
        '''大小(百分比)'''
        name = 'html编辑器_大小_百分比'
        comp = HtmlPage(self.driver, name)
        comp.from_scroll_to('450')
        self.assertIn('80%', comp.get_the_div_width_percent(), msg=name + '检验不通过')
        self.assertEqual(400, comp.get_the_div_height(), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = 'html编辑器_重计算'
        comp = HtmlPage(self.driver, name)
        self.assertIsNotNone(comp.get_the_div(), msg=name + '检验不通过')
        self.assertIsNotNone(comp.get_the_div_iframe(), msg=name + '检验不通过')
        input = InputPage(self.driver, '单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertIsNone(comp.get_the_div(), msg=name + '检验不通过')
        self.assertIsNone(comp.get_the_div_iframe(), msg=name + '检验不通过')

    def test_value_case(self):
        '''值脚本(iscript模式)'''
        name = 'html编辑器_值脚本'
        comp = HtmlPage(self.driver, name)
        comp.from_scroll_to('2850')
        self.assertEqual('aaa', comp.get_the_value(), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = 'html编辑器_隐藏时显示值'
        comp = HtmlPage(self.driver, name)
        comp.from_scroll_to('3500')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
        name = 'html编辑器_打印隐藏时显示值'
        comp = HtmlPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def test_readonly_case(self):
        '''只读条件'''
        name = 'html编辑器_只读条件'
        comp = HtmlPage(self.driver, name)
        comp.from_scroll_to('4000')
        self.assertEqual('bbb', comp.get_readonly_div_text(), msg=name + '检验不通过')
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_size_px_case()
#         self.test_size_percent_case()
#         self.test_refresh_calculate_case()
#         self.test_value_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
        self.test_show_when_print_case()
#         self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
