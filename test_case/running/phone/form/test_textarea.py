import os
import unittest

os.sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.textarea_page import TextareaPhonePage


class TextareaPhoneTest(ComponentPhoneTest):
    '''手机端多行文本框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '多行文本框'

    def test_type_case(self):
        '''类型'''
        name = '多行文本_名称'
        tp = TextareaPhonePage(self.driver, name)
        self.assertEqual('textarea', tp.get_tag_name(), msg=name + '检验不通过')

    def test_only_value_case(self):
        '''只读时仅显示值'''
        name = '多行文本_只读时仅显示值'
        tp = TextareaPhonePage(self.driver, name)
        self.assertTrue(tp.only_value(), msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '多行文本_刷新_重计算'
        tp = TextareaPhonePage(self.driver, name)
        tp.send_keys_trigger_refresh('refresh')
        tp = TextareaPhonePage(self.driver, name)   #刷新重计算执行后控件被重新渲染，之前的ip已不存在
        self.assertEqual('refresh end', tp.get_attr('value'), msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        name = '多行文本_描述'
        tp = TextareaPhonePage(self.driver, name)
        self.assertTrue(tp.is_desription_effect(name), msg=name + '检验不通过')

    def test_value_case(self):
        '''值'''
        name = '多行文本_值'
        tp = TextareaPhonePage(self.driver, name)
        self.assertEqual('值', tp.get_attr('value'), msg=name + '检验不通过')

    def test_card_case(self):
        '''身份证校验'''
        name = '多行文本_身份证校验'
        tp = TextareaPhonePage(self.driver, name)
        self.assertIn('身份证号码位数不对', tp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')
        tp.wait_msg_show_then_hide()
        self.assertIn('身份证号码出生日期超出范围或含有非法字符', tp.set_val_save_get_msg('441421111101010012'), msg=name + '检验不通过')
        tp.wait_msg_show_then_hide()
        self.assertNotIn('身份证号码输入不合法', tp.set_val_save_get_msg('441421199001010022'), msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验'''
        name = '多行文本_非空校验'
        tp = TextareaPhonePage(self.driver, name)
        self.assertIn("'多行文本_非空校验'必须填写", tp.set_val_save_get_msg(''), msg=name + '检验不通过')

    def test_email_case(self):
        '''email校验'''
        name = '多行文本_邮箱校验'
        tp = TextareaPhonePage(self.driver, name)
        self.assertIn("'多行文本_邮箱校验'格式错误", tp.set_val_save_get_msg('aaaaa'), msg=name + '检验不通过')

    def test_only_case(self):
        '''数据唯一校验'''
        name = '多行文本_数据唯一校验'
        tp = TextareaPhonePage(self.driver, name)
        self.assertIn("'多行文本_数据唯一校验'不能重复", tp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')

    def test_phone_number_case(self):
        '''手机号电话校验'''
        name = '多行文本_手机号电话校验'
        tp = TextareaPhonePage(self.driver, name)
        self.assertIn("'多行文本_手机号电话校验'格式错误", tp.set_val_save_get_msg('aaa'), msg=name + '检验不通过')


    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '多行文本_隐藏时显示值'
        tp = TextareaPhonePage(self.driver, name)
        self.assertEqual('display: none;',tp.get_attr('style'), msg=name + '检验不通过')

    def test_readonly_case(self):
        '''条件只读'''
        name = '多行文本_只读条件'
        tp = TextareaPhonePage(self.driver, name)
        self.assertTrue(tp.readonly_test(), msg=name + '检验不通过')



    def init(self):
        '''多行文本类型、只读、隐藏属性测试'''

#         self.test_type_case()
        # self.test_only_value_case()
#         self.test_refresh_calculate_case()
        # self.test_desription_case()
        # self.test_value_case()
        # self.test_card_case()
        # self.test_not_null_case()
#         self.test_email_case()
        # self.test_only_case()
        self.test_phone_number_case()
        # self.test_show_when_hide_case()
        # self.test_readonly_case()


if __name__ == '__main__':
    unittest.main()
