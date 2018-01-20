import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage



class InputTest(ComponentTest):
    '''单行文本框测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '单行文本框'
    
    def test_type_case(self):
        '''类型'''
        name = '单行文本_名称'
        comp = InputPage(self.driver, name)
        self.assertEqual('input', comp.get_tag_name(), msg=name + '检验不通过')
        self.assertIsNotNone(comp.get_attr('placeholder'), msg=name + '检验不通过')
        self.assertEqual('form-control component-input', comp.get_attr('class'), msg=name + '检验不通过')
        self.assertEqual('VALUE_TYPE_VARCHAR', comp.get_attr('fieldtype'), msg=name + '检验不通过')
        
    def test_phone_case(self):
        '''显示手机'''
        name = '单行文本_显示手机'
        comp = InputPage(self.driver, name)
        self.assertIn('tel.png', comp.get_attr('style'), msg=name + '检验不通过')
        
    def test_password_case(self):
        '''显示密码'''
        name = '单行文本_显示密码'
        comp = InputPage(self.driver, name)
        self.assertEqual('password', comp.get_attr('type'), msg=name + '检验不通过')
        
    def test_readonly_case(self):
        '''显示只读和条件只读'''
        name = '单行文本_显示只读'
        comp = InputPage(self.driver, name)
        self.assertTrue(comp.readonly_test(), msg=name + '检验不通过')

        name = '单行文本_只读条件'
        comp = InputPage(self.driver, name)
        self.assertTrue(comp.readonly_test(), msg=name + '检验不通过')
        
    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
        name = '单行文本_显示隐藏'
        comp = InputPage(self.driver, name)
        self.assertEqual('hidden', comp.get_attr('type'), msg=name + '检验不通过')
        
    def test_number_case(self):
        '''类型数字'''
        name = '单行文本_类型数字'
        comp = InputPage(self.driver, name)
        self.assertEqual('', comp.send_keys_get_value('aaaa'), msg=name + '检验不通过')

    def test_switch_key_case(self):
        '''焦点切换'''
        name = '单行文本_焦点切换'
        comp = InputPage(self.driver, name)
        self.assertFalse(comp.switch_key(), msg=name + '检验不通过')
        
    def test_only_value_case(self):
        '''只读时仅显示值'''
        name = '单行文本_只读时仅显示值'
        comp = InputPage(self.driver, name)
        self.assertTrue(comp.only_value(), msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '单行文本_刷新_重计算'
        comp = InputPage(self.driver, name)
        comp.send_keys_trigger_refresh('refresh')
        comp = InputPage(self.driver, name)
        self.assertEqual('refresh end', comp.get_attr('value'), msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        name = '单行文本_描述'
        comp = InputPage(self.driver, name)
        self.assertEqual('单行文本_描述描述', comp.get_attr('discript'), msg=name + '检验不通过')

    def test_value_case(self):
        '''值'''
        name = '单行文本_值脚本'
        comp = InputPage(self.driver, name)
        self.assertEqual('值', comp.get_attr('value'), msg=name + '检验不通过')

    def test_card_case(self):
        '''身份证校验'''
        name = '单行文本_身份证校验'
        comp = InputPage(self.driver, name)
        self.assertIn('身份证号码位数不对', comp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')
        self.assertIn('身份证号码出生日期超出范围或含有非法字符', comp.set_val_save_get_msg('441421111101010012'), msg=name + '检验不通过')
        self.assertNotIn('身份证号码输入不合法', comp.set_val_save_get_msg('441421199001010022'), msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验'''
        name = '单行文本_非空校验'
        comp = InputPage(self.driver, name)
        self.assertIn("'单行文本_非空校验'必须填写", comp.set_val_save_get_msg(''), msg=name + '检验不通过')
        
    def test_email_case(self):
        '''email校验'''
        name = '单行文本_邮箱校验'
        comp = InputPage(self.driver, name)
        self.assertIn("'单行文本_邮箱校验'格式错误", comp.set_val_save_get_msg('aaaaa'), msg=name + '检验不通过')

    def test_only_case(self):
        '''数据唯一校验'''
#         self.scroll_to('800')
        name = '单行文本_数据唯一校验'
        comp = InputPage(self.driver, name)
        self.assertIn("'单行文本_数据唯一校验'不能重复", comp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')
        
    def test_phone_number_case(self):
        '''手机号电话校验'''
#         self.scroll_to('800')
        name = '单行文本_手机号电话校验'
        comp = InputPage(self.driver, name)
        self.assertIn("'单行文本_手机号电话校验'格式错误", comp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')
        
    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        self.scroll_to('1000')
        name = '单行文本_隐藏时显示值'
        comp = InputPage(self.driver, name)
        self.assertTrue(comp.show_when_hide("控件已隐藏"), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
#         self.scroll_to('1000')
        name = '单行文本_打印隐藏时显示值'
        comp = InputPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
        
    def init(self):
        '''所有测试'''
        self.test_type_case()
#         self.test_phone_case()
#         self.test_password_case()
#         self.test_readonly_case()
#         self.test_hide_case()
#         self.test_number_case()
#         self.test_only_value_case()
#         self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_value_case()
#         self.test_card_case()
#         self.test_not_null_case()
#         self.test_email_case()
#         self.test_only_case()
#         self.test_phone_number_case()
#         self.test_show_when_hide_case()
#         self.test_switch_key_case()
#         self.test_show_when_print_case()
        
        
if __name__ == '__main__':
    unittest.main()
