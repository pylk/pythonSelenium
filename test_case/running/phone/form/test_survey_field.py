import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.form.survey_page import SurveyPhonePage


class SurveyPhoneTest(ComponentPhoneTest):
    '''调查问卷手机端测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '调查问卷'
    
    def test_type_case(self):
        '''名称'''
        name = '调查问卷_名称'
        comp = SurveyPhonePage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertIn('羽毛球', comp.get_the_div_text(), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '调查问卷_重计算'
        comp = SurveyPhonePage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertIn('羽毛球', comp.get_the_div_text(), msg=name + '检验不通过')
        input = InputPhonePage(self.driver, '单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertIsNone(comp.find_element('input[name="'+name+'"]'), msg=name + '检验不通过')

    def test_readonly_case(self):
        '''只读条件'''
        name = '调查问卷_只读条件'
        comp = SurveyPhonePage(self.driver, name)
        self.assertFalse(comp.the_check_is_enabled(), msg=name + '检验不通过')
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_refresh_calculate_case()
        self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
