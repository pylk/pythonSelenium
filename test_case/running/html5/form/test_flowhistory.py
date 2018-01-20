import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.flowhistory_page import FlowhistoryPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.view.list_view_page import ListViewPage
from test_case.running.html5.form.component_test import ComponentTest


class FlowhistoryTest(ComponentTest):
    '''流程历史控件测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '流程历史控件'
    
    def test_text_list_case(self):
        '''文本列表'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程历史_文本列表'
        comp = FlowhistoryPage(self.driver, name)
        self.assertTrue(comp.check_title(), msg=name + '检验不通过')
        self.assertEqual('审批节点', comp.get_table_head_first_td_text(), msg=name + '检验不通过')
        self.assertEqual('申请人', comp.get_table_tbody_first_td_text(), msg=name + '检验不通过')
        
    def test_flow_img_case(self):
        '''图表'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程历史_图表'
        comp = FlowhistoryPage(self.driver, name)
        self.assertTrue(comp.check_flow_img(), msg=name + '检验不通过')
        
    def test_text_list_flow_img_case(self):
        '''文本列表与图表'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程历史_文本列表与图表'
        #time.sleep(0.5)
        comp = FlowhistoryPage(self.driver, name)
        self.assertTrue(comp.check_title(), msg=name + '检验不通过')
        self.assertEqual('审批节点', comp.get_table_head_first_td_text(), msg=name + '检验不通过')
        self.assertEqual('申请人', comp.get_table_tbody_first_td_text(), msg=name + '检验不通过')
        self.assertTrue(comp.check_flow_img(), msg=name + '检验不通过')
        
    def test_desription_case(self):
        '''描述'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程历史_描述'
        #time.sleep(0.5)
        comp = FlowhistoryPage(self.driver, name)
        self.assertEqual('流程历史_描述描述', comp.get_description_text(), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程历史_隐藏时显示值'
        comp = FlowhistoryPage(self.driver, name)
        #time.sleep(0.5)
        comp.from_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程历史_打印隐藏时显示值'
        comp = FlowhistoryPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_flow_img_case()
#         self.test_text_list_flow_img_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
        self.test_show_when_print_case()
        
        
if __name__ == '__main__':
    unittest.main()
