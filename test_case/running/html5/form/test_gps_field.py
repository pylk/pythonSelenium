import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.gps_page import GPSPage


class GPSTest(ComponentTest):
    '''GPS定位控件测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = 'GPS定位'
    
    def test_type_case(self):
        '''描述'''
        name = 'GPS定位_名称'
        #time.sleep(0.5)
        comp = GPSPage(self.driver, name)
        self.assertIsNotNone(comp.get_gps_div(), msg=name + '检验不通过')


    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = 'GPS定位_隐藏时显示值'
        comp = GPSPage(self.driver, name)
        #time.sleep(0.5)
        comp.from_scroll_to('300')
        self.assertTrue(comp.is_gps_elem_invisibility(), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('该控件已隐藏'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
        name = 'GPS定位_打印隐藏时显示值'
        comp = GPSPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertIsNone(comp.find_elem('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
        self.test_show_when_print_case()
        
        
if __name__ == '__main__':
    unittest.main()
