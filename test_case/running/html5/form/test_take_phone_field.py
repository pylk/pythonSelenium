import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.take_phone_page import TakephotoPage
from test_case.page_obj.button_page import ButtonPage


class TakephoneTest(ComponentTest):
    '''在线拍照测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '在线拍照'
    
    def test_type_case(self):
        '''名称'''
        name = '在线拍照_名称'
        comp = TakephotoPage(self.driver, name)
        self.assertEqual('OnLineTakePhotoField', comp.get_attr('fieldtype'), msg=name + '检验不通过')
        self.assertEqual('/resource/image/photo.png', comp.get_attr('value'), msg=name + '检验不通过')
        self.assertTrue(comp.check_img(), msg=name + '检验不通过')
        comp.click_btn()
        self.assertEqual('在线拍照', comp.get_out_win_title(), msg=name + '检验不通过')
        
    def test_size_case(self):
        '''大小'''
        name = '在线拍照_大小'
        comp = TakephotoPage(self.driver, name)
        self.assertEqual('200', comp.get_size(), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '在线拍照_重计算'
        comp = TakephotoPage(self.driver, name)
        self.assertEqual('OnLineTakePhotoField', comp.get_attr('fieldtype'), msg=name + '检验不通过')
        self.assertEqual('/resource/image/photo.png', comp.get_attr('value'), msg=name + '检验不通过')
        self.assertTrue(comp.check_img(), msg=name + '检验不通过')
        input = InputPage(self.driver, '单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '在线拍照_隐藏时显示值'
        comp = TakephotoPage(self.driver, name)
        comp.from_scroll_to('700')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('该控件已隐藏'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
#         self.scroll_to('1000')
        name = '在线拍照_打印隐藏时显示值'
        comp = TakephotoPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def test_readonly_case(self):
        '''只读条件'''
        name = '在线拍照_只读条件'
        comp = TakephotoPage(self.driver, name)
        comp.from_scroll_to('700')
        self.assertEqual('none', comp.get_btn(), msg=name + '检验不通过')
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_size_case()
#         self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
#         self.test_show_when_print_case()
        self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
