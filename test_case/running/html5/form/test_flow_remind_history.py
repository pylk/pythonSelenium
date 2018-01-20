import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.flow_remind_history_page import FlowRemindHistoryPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.view.list_view_page import ListViewPage
from test_case.running.html5.form.component_test import ComponentTest


class FlowRemindHistoryTest(ComponentTest):
    '''流程催办历史控件测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '流程催办历史控件'
    
    def test_desription_case(self):
        '''描述'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程催办历史_描述'
        comp = FlowRemindHistoryPage(self.driver, name)
        self.assertTrue(comp.check_title(), msg=name + '检验不通过')
        self.assertEqual('序号', comp.get_table_head_first_td_text(), msg=name + '检验不通过')
        self.assertEqual('1', comp.get_table_tbody_first_td_text(), msg=name + '检验不通过')
        self.assertEqual('流程催办历史_描述', comp.get_description_text(), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程催办历史_隐藏时显示值'
        comp = FlowRemindHistoryPage(self.driver, name)
        self.assertTrue( comp.is_elem_invisibility('[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
        lp = ListViewPage(self.driver)
        lp.click_row()
        name = '流程催办历史_打印隐藏时显示值'
        comp = FlowRemindHistoryPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def init(self):
        '''所有测试'''
#         self.test_desription_case()
#         self.test_show_when_hide_case()
        self.test_show_when_print_case()
        
        
if __name__ == '__main__':
    unittest.main()
