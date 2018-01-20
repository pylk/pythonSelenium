import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.record_page import RecordPage
from test_case.page_obj.view.list_view_page import ListViewPage


class RecordTest(ComponentTest):
    '''微信录音控件测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '微信录音'
    
    def test_type_case(self):
        '''控件属性'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '微信录音控件_名称'
        #time.sleep(0.5)
        comp = RecordPage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.get_the_audio(), msg=name + '检验不通过')
        self.assertEqual('none', comp.check_del_function(), msg=name + '检验不通过') #删除后音频文件不存在

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '微信录音控件_隐藏时显示值'
        comp = RecordPage(self.driver, name)
        self.assertEqual('none', comp.find_element_by_css_selector('[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '微信录音控件_打印隐藏时显示值'
        comp = RecordPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def test_readonly_case(self):
        '''控件属性'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '微信录音控件_只读条件'
        comp = RecordPage(self.driver, name)
        #time.sleep(0.5)
        comp.from_scroll_to('300')
        self.assertFalse(comp.check_del_icon(), msg=name + '检验不通过') #删除后音频文件不存在
        
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
#         self.test_show_when_print_case()
        self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
