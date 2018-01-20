import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.survey_page import SurveyPage
from test_case.page_obj.button_page import ButtonPage


class SurveyTest(ComponentTest):
    '''调查问卷测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '调查问卷'
    
    def test_type_case(self):
        '''名称'''
        name = '调查问卷_名称'
        comp = SurveyPage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertIn('羽毛球', comp.get_the_div_text(), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '调查问卷_重计算'
        comp = SurveyPage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertIn('羽毛球', comp.get_the_div_text(), msg=name + '检验不通过')
        input = InputPage(self.driver, '单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')

#     def test_desription_case(self):
#         '''描述'''
#         name = '调查问卷_描述'
#         comp = SurveyPage(self.driver, name)
#         comp.from_scroll_to('500')
#         self.assertEqual('调查问卷_描述描述', comp.get_attr('data-discription'), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '调查问卷_隐藏时显示值'
        comp = SurveyPage(self.driver, name)
        comp.from_scroll_to('300')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
        name = '调查问卷_打印隐藏时显示值'
        comp = SurveyPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def test_readonly_case(self):
        '''只读条件'''
        name = '调查问卷_只读条件'
        comp = SurveyPage(self.driver, name)
        comp.from_scroll_to('700')
        self.assertFalse(comp.the_check_is_enabled(), msg=name + '检验不通过')
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
#         self.test_show_when_print_case()
        self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
