import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.form.included_page import IncludedPhonePage
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.form.text_page import TextPhonePage


class IncludedPhoneTest(ComponentPhoneTest):
    '''包含元素'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '包含元素'

    def test_parent_case(self):
        """包含元素父子关系"""
        name = '包含元素_父子关系'
        comp = IncludedPhonePage(self.driver,name)
        text = comp.getrecord(name)
        self.assertEqual("0",text,msg=name + "检验不通过")
        comp.click_included_btn(name)
        self.assertTrue(comp.is_contentIsNull(),msg=name + "检验不通过")

    def test_noparent_case(self):
        """包含元素非父子关系"""
        name = '包含元素_非父子关系'
        comp = IncludedPhonePage(self.driver,name)
        comp.clera_value()
        text = comp.getrecord(name)
        self.assertEqual("6",text,msg=name + "检验不通过")
        comp.click_included_btn(name)
        self.assertFalse(comp.is_contentIsNull(),msg=name + "检验不通过")
        self.assertEqual(6,comp.get_curpage_included_num(),msg=name + "检验不通过")

    def test_type_case(self):
        '''包含元素刷新'''
        name = '包含元素_刷新'
        name2 = '真实值'
        name3 = '显示值'
        name4 = '包含元素_父子关系'
        comp = IncludedPhonePage(self.driver,name)
        comp.clera_value()
        #点击新建一条数据
        comp.set_value(name,name2,'10',name3,'选择框10')
        self.assertEqual('1',comp.getrecord(name4),msg="包含元素刷新重计算检验不通过")

    def test_contain_hide_case(self):
        '''包含元素隐藏'''
        name = "包含元素重计算"
        comp = IncludedPhonePage(self.driver,name)
        bool = comp.is_comp_hide(name)
        self.assertTrue(bool,msg=name + "检验不通过")
        textInput = InputPhonePage(self.driver, '单行文本')
        textInput.send_keys_trigger_refresh('隐藏')
        bool2 = comp.is_comp_hide(name)
        self.assertFalse(bool2,msg=name + "检验不通过")

    def test_hidevalue_case(self):
        """包含元素隐藏时显示值"""
        name = "包含元素_隐藏时显示值"
        comp = IncludedPhonePage(self.driver,name)
        bool = comp.is_comp_hide(name)
        self.assertFalse(bool, msg=name + "检验不通过")
        self.assertIn('控件已隐藏', comp.get_curpage_span(), msg=name + '检验不通过')

    def test_grid_case(self):
        '''包含元素网格视图'''
        name = '包含元素_网格视图'
        name2 = '真实值'
        name3 = '显示值'
        comp = IncludedPhonePage(self.driver,name)
        comp.clera_value()
        # 点击新建一条数据
        comp.set_value(name, name2, '10', name3, '选择框10')
        self.assertEqual('1', comp.getrecord(name), msg=name + '检验不通过')
        
    def init(self):
        self.test_grid_case()
        # self.test_type_case()

if __name__ == '__main__':
    unittest.main()
    

