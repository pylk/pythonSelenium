import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.qrcode_page import QrcodePage
from test_case.page_obj.button_page import ButtonPage


class QrcodeTest(ComponentTest):
    '''二维码测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '二维码'
    
    def test_type_case(self):
        '''名称'''
        name = '二维码_名称'
        comp = QrcodePage(self.driver, name)
        self.assertEqual('hidden', comp.get_attr('type'), msg=name + '检验不通过')
        self.assertEqual('aaa', comp.get_attr('value'), msg=name + '检验不通过')
        self.assertEqual('200', comp.get_attr('data-size'), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"] + div > canvas'), msg=name + '检验不通过')
        
    def test_size_case(self):
        '''大小'''
        name = '二维码_大小'
        comp = QrcodePage(self.driver, name)
        self.assertEqual('300', comp.get_attr('data-size'), msg=name + '检验不通过')
        self.assertEqual('300', comp.get_canvas_height(), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '二维码_重计算'
        comp = QrcodePage(self.driver, name)
        self.assertIsNotNone(comp.find_elem('input[name="'+name+'"] + div > canvas'), msg=name + '检验不通过')
        input = InputPage(self.driver, '二维码_单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertTrue(comp.is_elem_invisibility('input[name="'+name+'"] + div > canvas'), msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        name = '二维码_描述'
        comp = QrcodePage(self.driver, name)
        comp.from_scroll_to('500')
        self.assertEqual('二维码_描述描述', comp.get_attr('data-discription'), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '二维码_隐藏时显示值'
        comp = QrcodePage(self.driver, name)
        comp.from_scroll_to('700')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"] + div > canvas'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
#         self.scroll_to('1000')
        name = '二维码_打印隐藏时显示值'
        comp = QrcodePage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
#     def test_readonly_case(self):
#         '''只读'''
# #         self.scroll_to('0')
#         name = '二维码_显示只读'
#         comp = QrcodePage(self.driver, name)
#         self.assertTrue(comp.readonly_test(), msg=name + '检验不通过')
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
        self.test_size_case()
#         self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
#         self.test_show_when_print_case()
#         self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
