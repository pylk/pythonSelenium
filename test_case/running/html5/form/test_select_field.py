import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.select_page import SelectPage
from selenium.webdriver.support.ui import Select


class SelectTest(ComponentTest):
    '''下拉选择框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '下拉框'  # 主页打开菜单时使用

    def test_type_case(self):
        '''类型'''
        name = '下拉框_名称'
        comp = SelectPage(self.driver, name)
        a = comp.get_attr("fieldtype")
        self.assertEqual('SelectField', a, msg=name + '检验不通过')

    def test_readonlyshowvalonly_case(self):
        '''下拉框显示只读'''
        name = '下拉框_只读'
        comp = SelectPage(self.driver, name)
        self.assertTrue(comp.readonlyshowvalonly(),msg=name + '检验不通过')

    def test_display_case(self):
        '''下拉框显示隐藏'''
        name = '下拉框_隐藏'
        comp = SelectPage(self.driver, name)
        self.assertIn('display: none;',comp.get_attr('style'),msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '下拉框_刷新'
        comp = SelectPage(self.driver, name)
        # 先定位到下拉菜单
        comp.find_elem('select[name="' + name + '"] > option').click()
        #time.sleep(0.5)
        # 再对下拉菜单中的选项进行选择
        comp.find_elem('select[name="' + name + '"]> option:nth-child(3)').click()
        comp.wait_refresh_loading_back_show_then_hide()
        #判断对应的元素有没有被选中
        bool = comp.find_elem('select[name="下拉框_重计算"]> option:nth-child(3)').is_selected()
        self.assertTrue(bool,msg="下拉框刷新重计算检验不通过")

    def test_desription_case(self):
        '''下拉框_描述测试'''
        self.scroll_to('300')
        #time.sleep(0.5)
        name = '下拉框_描述'
        comp = SelectPage(self.driver, name)
        self.assertEqual('下拉框_描述测试',comp.get_attr('discript'),msg=name + '检验不通过')

    def test_valuescript_case(self):
        '''下拉框_值脚本测试'''
        self.scroll_to('300')
        #time.sleep(0.5)
        name = '下拉框_值脚本'
        comp = SelectPage(self.driver, name)
        bool = comp.find_elem('select[name="'+name+'"]> option:nth-child(2)').is_selected()
        self.assertTrue(bool, msg=name+"检验不通过")

    def test_designpattern_case(self):
        '''下拉框_选项脚本设计模式'''
        self.scroll_to('300')
        #time.sleep(0.5)
        name = '下拉框_选项脚本设计模式'
        comp = SelectPage(self.driver, name)
        # 先定位到下拉菜单
        comp.find_elem('select[name="' + name + '"] > option').click()
        #time.sleep(0.5)
        # 再对下拉菜单中的选项进行选择
        comp.find_elem('select[name="' + name + '"]> option:nth-child(6)').click()
        #time.sleep(0.5)
        bool = comp.find_elem('select[name="' + name + '"]> option:nth-child(6)').is_selected()
        self.assertTrue(bool, msg=name + "检验不通过")

    def test_not_null_case(self):
        '''非空校验'''
        self.scroll_to('550')
        name = '下拉框_非空校验'
        comp = SelectPage(self.driver, name)
        self.assertIn("'下拉框_非空校验'必须填写", comp.notnull_test(), msg=name + '检验不通过')

    def test_hide_case(self):
        '''条件隐藏'''
        name = '下拉框_隐藏条件'
        self.scroll_to('550')
        name = '下拉框_隐藏条件'
        comp = SelectPage(self.driver, name)
        self.assertIn('display: none;',comp.get_attr('style'),msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        self.scroll_to('550')
        name = '下拉框_隐藏时显示值'
        comp = SelectPage(self.driver, name)
        self.assertTrue(comp.show_when_hide("控件已隐藏"),msg=name + '检验不通过')

    def test_readonly_case(self):
        '''条件只读'''
        self.scroll_to('550')
        name = '下拉框_只读条件'
        comp = SelectPage(self.driver, name)
        self.assertTrue(comp.readonlyshowvalonly(), msg=name + '检验不通过')

    def init(self):
        self.test_type_case()
        self.test_readonlyshowvalonly_case()
        self.test_display_case()
        self.test_refresh_calculate_case()
        self.test_desription_case()
        self.test_valuescript_case()
        self.test_designpattern_case()
        self.test_not_null_case()
        self.test_hide_case()
        self.test_show_when_hide_case()

if __name__ == '__main__':
    unittest.main()