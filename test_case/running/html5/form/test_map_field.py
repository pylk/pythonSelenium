import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.map_page import MapPage
from test_case.page_obj.button_page import ButtonPage


class MapTest(ComponentTest):
    '''地图测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '地图'
    
    def test_type_case(self):
        '''名称'''
        name = '地图_名称'
        comp = MapPage(self.driver, name)
        iframe = comp.get_the_map_iframe()
        comp.switch_to_the_iframe(iframe)
        self.assertTrue(comp.is_map_page(), msg=name + '检验不通过')
        
    def test_type_out_case(self):
        '''弹出窗口'''
        name = '地图_弹出窗口'
        comp = MapPage(self.driver, name)
        comp.click_out_btn()
        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()
        self.assertTrue(comp.is_map_page(), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '地图_重计算'
        comp = MapPage(self.driver, name)
        iframe = comp.get_the_map_iframe()
        comp.switch_to_the_iframe(iframe)
        self.assertTrue(comp.is_map_page(), msg=name + '检验不通过')
        
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        mp.switch_to_iframe()
        
        input = InputPage(self.driver, '单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertFalse(comp.is_element_visible('input[name="' + name + '"]'), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '地图_隐藏时显示值'
        comp = MapPage(self.driver, name)
        comp.from_scroll_to('1700')
        self.assertFalse(comp.is_element_visible('input[name="' + name + '"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
        name = '地图_打印隐藏时显示值'
        comp = MapPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_type_out_case()
#         self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
        self.test_show_when_print_case()
        
        
if __name__ == '__main__':
    unittest.main()
