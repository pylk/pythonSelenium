import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
os.sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.textarea_page import TextareaPage


class TextareaTest(ComponentTest):
    '''多行文本框测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '多行文本框'  #主页打开菜单时使用
    
    def test_type_case(self):
        '''类型'''
        name = '多行文本_名称'
        comp = TextareaPage(self.driver, name)
        self.assertEqual('textarea', comp.get_tag_name(), msg=name + '检验不通过')
       
     
    def test_only_value_case(self):
        '''只读时仅显示值'''
        name = '多行文本_只读时仅显示值'
        comp = TextareaPage(self.driver, name)
        self.assertTrue(comp.only_value(), msg=name + '检验不通过')
 
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '多行文本_刷新_重计算'
        comp = TextareaPage(self.driver, name)
        comp.send_keys_trigger_refresh('refresh')
        comp = TextareaPage(self.driver, name)
        self.assertEqual('refresh end', comp.get_attr('value'), msg=name + '检验不通过')
 
    def test_desription_case(self):
        '''描述'''
#         self.scroll_to('550')
        name = '多行文本_描述'
        comp = TextareaPage(self.driver, name)
        self.assertEqual('多行文本_描述', comp.get_attr('discript'), msg=name + '检验不通过')
 
    def test_value_case(self):
        '''值'''
#         self.scroll_to('550')
        name = '多行文本_值'
        comp = TextareaPage(self.driver, name)
        self.assertEqual('值', comp.get_attr('value'), msg=name + '检验不通过')
 
    def test_card_case(self):
        '''身份证校验'''
        name = '多行文本_身份证校验'
        comp = TextareaPage(self.driver, name)
        self.assertIn('身份证号码位数不对', comp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')
        self.assertIn('身份证号码出生日期超出范围或含有非法字符', comp.set_val_save_get_msg('441421111101010012'), msg=name + '检验不通过')
        self.assertNotIn('身份证号码输入不合法', comp.set_val_save_get_msg('441421199001010022'), msg=name + '检验不通过')
 
    def test_not_null_case(self):
        '''非空校验'''
#         self.scroll_to('550')
        name = '多行文本_非空校验'
        comp = TextareaPage(self.driver, name)
        self.assertIn("'多行文本_非空校验'必须填写", comp.set_val_save_get_msg(''), msg=name + '检验不通过')
         
    def test_email_case(self):
        '''email校验'''
#         self.scroll_to('800')
        name = '多行文本_邮箱校验'
        comp = TextareaPage(self.driver, name)
        comp.from_scroll_to('800')         
        self.assertIn("'多行文本_邮箱校验'格式错误", comp.set_val_save_get_msg('aaaaa'), msg=name + '检验不通过')
 
    def test_only_case(self):
        '''数据唯一校验'''
#         self.scroll_to('800')
        name = '多行文本_数据唯一校验'
        comp = TextareaPage(self.driver, name)
        comp.from_scroll_to('800') 
        self.assertIn("'多行文本_数据唯一校验'不能重复", comp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')
         
     
    def test_phone_number_case(self):
        '''手机号电话校验'''
 
        name = '多行文本_手机号电话校验'
        comp = TextareaPage(self.driver, name)
        comp.from_scroll_to('800') 
        self.assertIn("'多行文本_手机号电话校验'格式错误", comp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')
#         
#     def test_show_when_hide_case(self):
#         '''隐藏时显示值'''
# 
#         name = '多行文本_隐藏时显示值'
#         comp = TextareaPage(self.driver, name)
#         comp.from_scroll_to('900')        
#         self.assertEqual("控件已隐藏", comp.get_text_by_css_selector('input[name="'+name+'"] + span'), msg=name + '检验不通过')
        

        
    def init(self):
        '''多行文本类型、只读、隐藏属性测试'''
        
        self.test_type_case()
        # self.test_only_value_case()
        # self.test_refresh_calculate_case()
        # self.test_desription_case()
        # self.test_value_case()
        # self.test_card_case()
        # self.test_not_null_case()
        # self.test_email_case()
        # self.test_only_case()
        # self.test_show_when_hide_case()
       
 
#         self.test_print_hide_case()
#         self.test_show_when_print_case()
        
        
if __name__ == '__main__':
    unittest.main()
