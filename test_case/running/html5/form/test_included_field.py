import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.form.included_page import IncludedPage


class IncludedTest(ComponentTest):
    '''包含元素'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '包含元素'

    def test_parent_case(self):
        """包含元素父子关系"""
        name = '包含元素_父子关系'
        #time.sleep(0.5)
        self.scroll_to('200')
        comp = IncludedPage(self.driver)
        text = comp.getrecord(name)
        self.assertEqual("总记录数:(0)",text,msg=name + "检验不通过")

    def test_noparent_case(self):
        """包含元素非父子关系"""
        name = '包含元素_非父子关系'
        #time.sleep(0.5)
        self.scroll_to('200')
        comp = IncludedPage(self.driver)
        text = comp.getrecord(name)
        self.assertEqual("总记录数:(6)",text,msg=name + "检验不通过")

    def test_type_case(self):
        '''包含元素刷新'''
        self.scroll_to('0')
        name = '包含元素_刷新'
        name2 = '真实值'
        name3 = '显示值'
        name4 = '包含元素_父子关系'
        comp = IncludedPage(self.driver)
        #点击新建按钮，进入新建数据
        comp.clicknew(name)
        #time.sleep(0.5)
        #进入子表录入数据
        sw = MainPage(self.driver)
        sw.switch_to_div_iframe()
        #time.sleep(0.5)
        self.driver.find_element_by_name(name2).send_keys("10")
        self.driver.find_element_by_name(name3).send_keys("选择框10")
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        sw.wait_loading_hide()
        btn.click_button(btn.to_return)
        time.sleep(0.5)
        #返回主表单，检查时候生成数据
        sw.switch_to_iframe()
        bool = comp.successnew(name4)
        self.assertTrue(
        bool,msg=name + "检验不通过")


    def test_contain_hide_case(self):
        '''包含元素隐藏'''
        name = "包含元素重计算"
        self.scroll_to('0')
        comp = IncludedPage(self.driver)
        bool = comp.is_included_existed(name)
        self.assertTrue(bool,msg=name + "检验不通过")
        a = comp.find_elem('input[name="单行文本"]')
        a.send_keys("隐藏")
        #time.sleep(0.5)
        a.send_keys(Keys.TAB)
        #time.sleep(0.5)
        bool2 = comp.is_included_existed(name)
        self.assertFalse(bool2,msg=name + "检验不通过")

    def test_hidevalue_case(self):
        """包含元素隐藏时显示值"""
        self.scroll_to('800')
        name = "包含元素_隐藏时显示值"
        comp = IncludedPage(self.driver)
        bool = comp.is_included_existed(name)
        self.assertFalse(bool,msg=name + "检验不通过")
        self.assertTrue(comp.show_when_hide('该控件已隐藏，显示值'), msg=name + '检验不通过')


    def test_grid_case(self):
        '''包含元素网格视图'''
        name = '包含元素_网格视图'
        self.scroll_to('850')
        #time.sleep(0.5)
        comp = IncludedPage(self.driver)
        comp.switch_grid(name)
        #time.sleep(0.5)
        comp.clicknewgrid(name)
        #time.sleep(0.5)
        comp.find_elem('input[name="真实值"]').send_keys("10")
        comp.find_elem('input[name="显示值"]').send_keys("选择框10")
        #time.sleep(0.5)
        comp.clicksavegrid(name)
        #time.sleep(0.5)
        bool = comp.successnewgrid(name)
        self.assertTrue(bool,msg=name + "检验不通过")

    def init(self):
#         self.test_grid_case()
#         self.test_hidevalue_case()
        self.test_noparent_case()

if __name__ == '__main__':
    unittest.main()
