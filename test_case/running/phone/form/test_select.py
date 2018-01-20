import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.select_page import SelectPhonePage
from selenium.webdriver.support.ui import Select


class SelectPhoneTest(ComponentPhoneTest):
    '''下拉选择框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '下拉框'  # 主页打开菜单时使用

    def test_type_case(self):
        '''类型'''
        name = '下拉框_名称'
        sp = SelectPhonePage(self.driver, name)
        self.assertEqual('select', sp.get_tag_name(), msg=name + '检验不通过')

    def test_only_value_case(self):
        '''下拉框显示只读'''
        name = '下拉框_只读'
        sp = SelectPhonePage(self.driver, name)
        self.assertTrue(sp.readonly_test(),msg=name + '检验不通过')

    def test_display_case(self):
        '''下拉框显示隐藏'''
        name = '下拉框_隐藏'
        sp = SelectPhonePage(self.driver, name)
        dname = self.driver.find_element_by_name(name)
        self.assertFalse(dname.is_displayed(),msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '下拉框_刷新'
        sp = SelectPhonePage(self.driver, name)
        sp.wait_Tabloading_show_then_hide()
        # 先定位到下拉菜单
        sp.find_element('select[name="' + name + '"]').click()
        #time.sleep(0.5)
        # 再对下拉菜单中的选项进行选择
        sp.find_element('select[name="' + name + '"]> option:nth-child(3)').click()
        sp.wait_Tabloading_show_then_hide()
        #判断对应的元素有没有被选中
        bool = sp.find_element('select[name="下拉框_重计算"]> option:nth-child(3)').is_selected()
        self.assertTrue(bool,msg="下拉框刷新重计算检验不通过")

    def test_desription_case(self):
        '''下拉框_描述测试'''
        name = '下拉框_描述'
        sp = SelectPhonePage(self.driver, name)
        self.assertTrue(sp.is_desription_effect(name), msg=name + '检验不通过')

    def test_valuescript_case(self):
        '''下拉框_值脚本测试'''
        name = '下拉框_值脚本'
        sp = SelectPhonePage(self.driver, name)
        bool = sp.find_element('select[name="'+name+'"]> option:nth-child(2)').is_selected()
        self.assertTrue(bool, msg=name+"检验不通过")

    def test_designpattern_case(self):
        '''下拉框_选项脚本设计模式'''
        name = '下拉框_选项脚本设计模式'
        sp = SelectPhonePage(self.driver, name)
        sp.wait_Tabloading_show_then_hide()
        # 先定位到下拉菜单
        sp.find_element('select[name="' + name + '"]').click()
        #time.sleep(0.5)
        # 再对下拉菜单中的选项进行选择
        sp.find_element('select[name="' + name + '"]> option:nth-child(6)').click()
        sp.wait_Tabloading_show_then_hide()
        bool = sp.find_element('select[name="' + name + '"]> option:nth-child(6)').is_selected()
        self.assertTrue(bool, msg=name + "检验不通过")

    def test_not_null_case(self):
        '''非空校验'''
        name = '下拉框_非空校验'
        sp = SelectPhonePage(self.driver, name)
        self.assertIn("'下拉框_非空校验'必须填写", sp.notnull_test(), msg=name + '检验不通过')

    def test_hide_case(self):
        '''条件隐藏'''
        name = '下拉框_隐藏条件'
        sp = SelectPhonePage(self.driver, name)
        dname = self.driver.find_element_by_name(name)
        self.assertFalse(dname.is_displayed(), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '下拉框_隐藏时显示值'
        sp = SelectPhonePage(self.driver, name)
        dname = self.driver.find_element_by_name(name)
        self.assertFalse(dname.is_displayed(), msg=name + '检验不通过')

    def test_readonly_case(self):
        '''条件只读'''
        name = '下拉框_只读条件'
        sp = SelectPhonePage(self.driver, name)
        self.assertTrue(sp.readonly_test(), msg=name + '检验不通过')

    def init(self):
        # self.test_type_case()
        # self.test_only_value_case()
        # self.test_display_case()
        # self.test_refresh_calculate_case()
        # self.test_desription_case()
        # self.test_valuescript_case()
        # self.test_designpattern_case()
        # self.test_not_null_case()
        # self.test_hide_case()
        # self.test_show_when_hide_case()
        self.test_readonly_case()

if __name__ == '__main__':
    unittest.main()