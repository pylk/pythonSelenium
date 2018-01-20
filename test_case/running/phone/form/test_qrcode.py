import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.qrcode_page import QrcodePhonePage
from test_case.page_obj.button_page import ButtonPage


class QrcodePhoneTest(ComponentPhoneTest):
    '''phone二维码测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  # 主页打开菜单时使用
    menu3 = '二维码'
    
    def test_type_case(self):
        '''名称'''
        name = '二维码_名称'
        comp = QrcodePhonePage(self.driver, name)
        self.assertEqual('hidden', comp.get_attr('type'), msg=name + '检验不通过')
        self.assertEqual('aaa', comp.get_attr('value'), msg=name + '检验不通过')
        self.assertEqual('200', comp.get_attr('data-size'), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.find_element('input[name="' + name + '"] + div canvas'), msg=name + '检验不通过')
        
    def test_size_case(self):
        '''大小'''
        name = '二维码_大小'
        comp = QrcodePhonePage(self.driver, name)
        self.assertEqual('300', comp.get_attr('data-size'), msg=name + '检验不通过')
        self.assertEqual('300', comp.get_canvas_height(), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '二维码_重计算'
        comp = QrcodePhonePage(self.driver, name)
        self.assertNotEqual('none', comp.find_element('input[name="' + name + '"] + div canvas'), msg=name + '检验不通过')
        input = InputPage(self.driver, '二维码_单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertIsNone(comp.find_element('input[name="' + name + '"] + div canvas'), msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        name = '二维码_描述'
        comp = QrcodePhonePage(self.driver, name)
        comp.window_scroll_to('600')
        self.assertEqual('二维码_描述描述', comp.get_attr('data-discription'), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '二维码_隐藏时显示值'
        comp = QrcodePhonePage(self.driver, name)
        comp.window_scroll_to('700')
        self.assertIsNone(comp.find_element('input[name="' + name + '"] + div canvas'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_size_case()
#         self.test_refresh_calculate_case()
#         self.test_desription_case()
        self.test_show_when_hide_case()
        
if __name__ == '__main__':
    unittest.main()
