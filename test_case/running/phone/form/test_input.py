import os
import sys
import time
import unittest

sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.input_page import InputPhonePage


class InputPhoneTest(ComponentPhoneTest):
    '''手机端单行文本框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '单行文本框'

    def test_type_case(self):
        '''类型'''
        name = '单行文本_名称'
        ip = InputPhonePage(self.driver, name)
        self.assertEqual('input', ip.get_tag_name(), msg=name + '检验不通过')

    def test_phone_case(self):
        '''显示手机'''
        name = '单行文本_显示手机'
        ip = InputPhonePage(self.driver, name)
        self.assertIn('tel.png', ip.get_attr('style'), msg=name + '检验不通过')

    def test_password_case(self):
        '''显示密码'''
        name = '单行文本_显示密码'
        ip = InputPhonePage(self.driver, name)
        self.assertEqual('password', ip.get_attr('type'), msg=name + '检验不通过')

    def test_readonly_case(self):
        '''显示只读和条件只读'''
        name = '单行文本_显示只读'
        ip = InputPhonePage(self.driver, name)
        self.assertTrue(ip.readonly_test(), msg=name + '检验不通过')

        name = '单行文本_只读条件'
        ip = InputPhonePage(self.driver, name)
        self.assertTrue(ip.readonly_test(), msg=name + '检验不通过')

    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
        name = '单行文本_显示隐藏'
        ip = InputPhonePage(self.driver, name)
        self.assertEqual('hidden', ip.get_attr('type'), msg=name + '检验不通过')

    def test_number_case(self):
        '''类型数字'''
        name = '单行文本_类型数字'
        ip = InputPhonePage(self.driver, name)
        self.assertEqual('', ip.send_keys_get_value('aaaa'), msg=name + '检验不通过')

    def test_switch_key_case(self):
        '''焦点切换'''
        name = '单行文本_焦点切换'
        ip = InputPhonePage(self.driver, name)
        ip.wait_Tabloading_show_then_hide()
        self.assertFalse(ip.switch_key(), msg=name + '检验不通过')

    def test_only_value_case(self):
        '''只读时仅显示值'''
        name = '单行文本_只读时仅显示值'
        ip = InputPhonePage(self.driver, name)
        self.assertTrue(ip.only_value(), msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''  # bug
        name = '单行文本_刷新_重计算'
        ip = InputPhonePage(self.driver, name)
        ip.send_keys_trigger_refresh('refresh')
        ip = InputPhonePage(self.driver, name)  #刷新重计算执行后控件被重新渲染，之前的ip已不存在
        self.assertEqual('refresh\xa0end', ip.get_attr('value'), msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        name = '单行文本_描述'
        ip = InputPhonePage(self.driver, name)
        self.assertTrue(ip.is_desription_effect(name), msg=name + '检验不通过')

    def test_value_case(self):
        '''值'''
        name = '单行文本_值脚本'
        ip = InputPhonePage(self.driver, name)
        self.assertEqual('值', ip.get_attr('value'), msg=name + '检验不通过')

    def test_card_case(self):
        '''身份证校验'''
        name = '单行文本_身份证校验'
        ip = InputPhonePage(self.driver, name)
        self.assertIn('身份证号码位数不对', ip.set_val_save_get_msg('aaa'), msg=name + '检验不通过')
        ip.wait_msg_show_then_hide()
        self.assertIn('身份证号码出生日期超出范围或含有非法字符', ip.set_val_save_get_msg('441421111101010012'), msg=name + '检验不通过')
        ip.wait_msg_show_then_hide()
        self.assertNotIn('身份证号码输入不合法', ip.set_val_save_get_msg('441421199001010022'), msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验'''
        name = '单行文本_非空校验'
        ip = InputPhonePage(self.driver, name)
        self.assertIn("'单行文本_非空校验'必须填写", ip.set_val_save_get_msg(''), msg=name + '检验不通过')

    def test_email_case(self):
        '''email校验'''
        name = '单行文本_邮箱校验'
        ip = InputPhonePage(self.driver, name)
        self.assertIn("'单行文本_邮箱校验'格式错误", ip.set_val_save_get_msg('aaaaa'), msg=name + '检验不通过')

    def test_only_case(self):
        '''数据唯一校验'''
        name = '单行文本_数据唯一校验'
        ip = InputPhonePage(self.driver, name)
        self.assertIn("'单行文本_数据唯一校验'不能重复", ip.set_val_save_get_msg('aaa'), msg=name + '检验不通过')

    def test_phone_number_case(self):
        '''手机号电话校验'''
        name = '单行文本_手机号电话校验'
        ip = InputPhonePage(self.driver, name)
        self.assertIn("'单行文本_手机号电话校验'格式错误", ip.set_val_save_get_msg('aaa'), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '单行文本_隐藏时显示值'
        ip = InputPhonePage(self.driver, name)
        self.assertEqual('hidden', ip.get_attr('type'), msg=name + '检验不通过')

    def init(self):
        '''所有测试'''
        # self.test_type_case()
        # self.test_phone_case()
        # self.test_password_case()
        # self.test_readonly_case()
        # self.test_hide_case()
        # self.test_number_case()
        # self.test_only_value_case()
        self.test_refresh_calculate_case()
#         self.test_desription_case()
        # self.test_value_case()
        # self.test_card_case()
        # self.test_not_null_case()
        # self.test_email_case()
        # self.test_only_case()
        # self.test_phone_number_case()
        # self.test_show_when_hide_case()
        # self.test_switch_key_case()


if __name__ == '__main__':
    unittest.main()
