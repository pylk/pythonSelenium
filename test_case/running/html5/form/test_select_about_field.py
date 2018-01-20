import os
import sys
import time
import unittest
sys.path.append('../../../../')
from selenium.webdriver.common.keys import Keys
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.select_about_page import SelectAboutPage


class SelectAboutFieldTest(ComponentTest):
    '''左右选择框'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '左右选择框'

    def test_type_case(self):
        '''左右选择框类型'''
        comp = SelectAboutPage(self.driver)
        name = '左右框_类型'
        compname = '左右框_刷新'
        self.scroll_to('0')
        a = comp.getcomp(compname)
        type = a.get_attribute("fieldtype")
        self.assertEqual(type,"SelectAboutField", msg=name + '检验不通过')


    def test_refresh_case(self):
        '''左右选择框刷新'''
        comp = SelectAboutPage(self.driver)
        name = '左右框_刷新'
        compname = '左右框_重计算'
        comp.add('左右框_刷新','2')
        comp.wait_refresh_loading_back_show_then_hide()
        equal = comp.checkadd(compname)
        self.assertEqual("左右框2",equal,msg=name + '检验不通过')

    def test_describe_case(self):
        '''左右选择框描述'''
        comp = SelectAboutPage(self.driver)
        name = '测试左右选择框描述'
        compname = '左右框_描述'
        self.scroll_to('200')
        a = comp.getcomp(compname)
        compdiscript = a.get_attribute('discript')
        self.assertEqual("左右框_描述", compdiscript, msg=name + '检验不通过')

    def test_recalculation_case(self):
        '''左右选择框重计算'''
        comp = SelectAboutPage(self.driver)
        name = '左右选择框重计算'
        compname = '左右框_重计算'
        bool1 = comp.check_existence(compname)
        self.assertTrue(bool1,msg=name + '检验不通过')
        comp.find_elem('input[name="单行文本"]').send_keys("隐藏")
        comp.find_elem('input[name="单行文本"]').send_keys(Keys.TAB)
        #time.sleep(0.5)
        bool2 = comp.check_existence(compname)
        self.assertFalse(bool2, msg=name + '检验不通过')


    def test_valueDs_case(self):
        '''左右选择框值脚本设计模式测试'''
        comp = SelectAboutPage(self.driver)
        name = '左右框_值脚本设计模式'
        compname = '左右框_值脚本'
        self.scroll_to('650')
        text1 = comp.checkadd(compname)
        self.assertEqual("没有值被选中",text1,msg=name + '检验不通过')
        #time.sleep(0.5)
        self.scroll_to('0')
        comp.find_elem_visible('input[name="单行文本"]').send_keys("3")
        comp.find_elem_visible('input[name="单行文本"]').send_keys(Keys.TAB)
        #time.sleep(0.5)
        self.scroll_to('650')
        #time.sleep(0.5)
        text2 = comp.checkadd(compname)
        self.assertEqual("左右框3", text2, msg=name + '检验不通过')


    def test_valueJs_caase(self):
        '''左右选择框值脚本js模式测试'''
        comp = SelectAboutPage(self.driver)
        name = '左右框_值脚本JS模式'
        compname = '左右选择框_值脚本'
        self.scroll_to('680')
        #time.sleep(0.5)
        text1 = comp.checkadd(compname)
        print("text-------->>%s"%text1)
        self.assertEqual("左右框2",text1, msg=name + '检验不通过')


    def test_optionDs_case(self):
        '''左右选择框选项设计模式'''
        comp = SelectAboutPage(self.driver)
        name = '左右选择框选项设计模式'
        compname = '左右框_选项脚本设计模式'
        self.scroll_to('1100')
        text1 = comp.checkadd(compname)
        self.assertEqual("没有值被选中", text1, msg=name + '检验不通过')
        #time.sleep(0.5)
        comp.add(compname,'2')
        equal = comp.checkadd(compname)
        self.assertEqual("选择框2",equal,msg=name + '检验不通过')


    def test_optionJs_case(self):
        '''左右选择框选项Js模式'''
        comp = SelectAboutPage(self.driver)
        name = '左右选择框选项Js模式'
        compname = '左右选择框_选项脚本'
        self.scroll_to('1400')
        text1 = comp.checkadd(compname)
        self.assertEqual("没有值被选中", text1, msg=name + '检验不通过')
        #time.sleep(0.5)
        comp.add(compname,'2')
        equal = comp.checkadd(compname)
        self.assertEqual("选择框2",equal,msg=name + '检验不通过')


    def test_notnull_case(self):
        '''左右选择框非空校验'''
        comp = SelectAboutPage(self.driver)
        name = '左右选择框非空校验'
        compname = '左右框_非空校验'
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        #time.sleep(0.5)
        text1 = comp.get_msg()
        self.assertIn("左右框_非空校验'必须填写！;", text1, msg=name + '检验不通过')

    def test_hidevalue_case(self):
        '''左右选择框隐藏时显示值'''
        self.scroll_to('1800')
        comp = SelectAboutPage(self.driver)
        name = '左右选择框隐藏时显示值'
        compname = '左右框_隐藏时显示值'
        bool = comp.check_existence(compname)
        comp.wait_loading_hide()
        self.assertFalse(bool,msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('控件已隐藏'),msg=name + '检验不通过')

    def test_readonly_case(self):
        '''左右选择框只读'''
        self.scroll_to('1900')
        comp = SelectAboutPage(self.driver)
        name = '左右选择框只读'
        compname = '左右框_只读条件'
        a = comp.getcomp(compname)
        val = a.get_attribute("displaytype")
        self.assertEqual('1',val,msg=name + '检验不通过')
        equal = comp.testreadonly(compname,'2')
        self.assertEqual("只读生效",equal,msg=name + '检验不通过')


    def init(self):
#         self.test_type_case()
#         self.test_refresh_case()
#         self.test_describe_case()
#         self.test_recalculation_case()
        self.test_valueDs_case()
#         self.test_valueJs_caase()
#         self.test_optionDs_case()
#         self.test_optionJs_case()
#         self.test_notnull_case()
#         self.test_hidevalue_case()
#         self.test_readonly_case()

if __name__ == '__main__':
    unittest.main()
