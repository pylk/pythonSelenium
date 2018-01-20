import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
os.sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.date_field_page import DatePhonePage
from datetime import timedelta, datetime


class DatePhoneTest(ComponentPhoneTest):
    '''日期选择框测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '日期选择框'

    def test_case_limited(self):
        '''限制_刷新_重计算'''
        state_date = '开始日期'
        dp = DatePhonePage(self.driver, state_date)
        dp.wait_Tabloading_show_then_hide()
        #点击日期确认按钮
        today =  datetime.today().strftime('%Y-%m-%d')
        start_time = dp.select_start_date()
        self.assertEqual(today, start_time, msg=state_date + '检验不通过')
        end_date = '结束日期'
        dp = DatePhonePage(self.driver, end_date)
        # 结束时间只能选择开始时间之后是数据
        self.assertEqual("2099", dp.is_ymd_reflash(0), msg=end_date + '检验不通过')

    def test_type_case(self):
        '''类型'''
        name = '日期选择框_名称'
        dp = DatePhonePage(self.driver, name)
        self.assertEqual('input', dp.get_tag_name(), msg=name + '检验不通过')
        self.assertEqual('contactField requiredField Wdate', dp.get_attr('class'), msg=name + '检验不通过')
        self.assertEqual('DateField', dp.get_attr('fieldtype'), msg=name + '检验不通过')
 
    def test_readonly_case(self):
        '''显示只读和条件只读'''
        name = '日期选择框_显示只读'
        dp = DatePhonePage(self.driver, name)
        self.assertTrue(dp.readonly_test(), msg=name + '检验不通过')
        self.assertEqual('true',dp.get_attr('readonlyshowvalonly'), msg=name + '检验不通过')

        name = '日期选择框_只读条件'
        dp = DatePhonePage(self.driver, name)
        self.assertTrue(dp.readonly_test(), msg=name + '检验不通过')
        self.assertEqual('false',dp.get_attr('readonlyshowvalonly'), msg=name + '检验不通过')
         
    def test_hide_case(self):
        '''显示隐藏'''
        name = '日期选择框_显示隐藏'
        dp = DatePhonePage(self.driver, name)
        dname = self.driver.find_element_by_name(name)
        self.assertFalse(dname.is_displayed(), msg=name + '检验不通过')

    def test_only_value_case(self):
        '''只读时仅显示值'''
        name = '日期选择框_只读时仅显示值'
        dp = DatePhonePage(self.driver, name)
        self.assertEqual('display: none;',dp.get_attr('style'), msg=name + '检验不通过')
 
    def test_desription_case(self):
        '''描述'''
        name = '日期选择框_描述'
        dp = DatePhonePage(self.driver, name)
        self.assertTrue(dp.is_desription_effect(name), msg=name + '检验不通过')
 
    def test_value_case(self):
        '''值'''
        name = '日期选择框_值脚本'
        dp = DatePhonePage(self.driver, name)
        self.assertEqual(datetime.today().strftime('%Y-%m-%d'), dp.get_attr('value'), msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验'''
        name = '日期选择框_非空校验'
        dp = DatePhonePage(self.driver, name)
        self.assertIn("'日期选择框_非空校验'必须填写", dp.notnull_test(), msg=name + '检验不通过')
         
    def test_show_when_hide_case(self):
        name = '日期选择框_隐藏时显示值'
        dp = DatePhonePage(self.driver, name)
        dname = self.driver.find_element_by_name(name)
        self.assertFalse(dname.is_displayed(), msg=name + '检验不通过')
 
    def test_format_case(self):
        '''显示只读和条件只读'''
        name = '日期选择框_格式年'
        dp = DatePhonePage(self.driver, name)
        self.assertEqual('yyyy',dp.get_attr('datefmt'), msg=name + '检验不通过')
 
        name = '日期选择框_格式年月'
        dp = DatePhonePage(self.driver, name)
        self.assertEqual('yyyy-MM-dd',dp.get_attr('datefmt'), msg=name + '检验不通过')     
         
        name = '日期选择框_格式年到秒'
        dp = DatePhonePage(self.driver, name)
        self.assertEqual('yyyy-MM-dd HH:mm:ss',dp.get_attr('datefmt'), msg=name + '检验不通过')   
         
        name = '日期选择框_格式时分秒'
        dp = DatePhonePage(self.driver, name)
        self.assertEqual('HH:mm:ss',dp.get_attr('datefmt'), msg=name + '检验不通过')
          
        
    def init(self):
        self.test_case_limited()
        # self.test_type_case()
        # self.test_readonly_case()
        # self.test_hide_case()
        # self.test_only_value_case()
        # self.test_desription_case()
        # self.test_value_case()
        # self.test_not_null_case()
        # self.test_show_when_hide_case()
        # self.test_format_case()

        
if __name__ == '__main__':
    unittest.main()
