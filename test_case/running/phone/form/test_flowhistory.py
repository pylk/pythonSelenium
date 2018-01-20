import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.page_obj.form.flowhistory_page import FlowhistoryPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage
from test_case.running.phone.form.component_test import ComponentPhoneTest


class FlowhistoryPhoneTest(ComponentPhoneTest):
    '''流程历史控件手机端测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '流程历史控件'
    
    def test_text_list_case(self):
        '''文本列表'''
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()
        name = '流程历史_文本列表'
        comp = FlowhistoryPhonePage(self.driver, name)
        self.assertTrue(comp.check_title(), msg=name + '检验不通过')
        self.assertEqual('审批节点', comp.get_table_head_first_td_text(), msg=name + '检验不通过')
        self.assertEqual('申请人', comp.get_table_tbody_first_td_text(), msg=name + '检验不通过')
        
    def test_flow_img_case(self):
        '''图表'''
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()
        name = '流程历史_图表'
        comp = FlowhistoryPhonePage(self.driver, name)
        self.assertTrue(comp.check_title(), msg=name + '检验不通过')
        self.assertTrue(comp.check_flow_img(), msg=name + '检验不通过')
        
    def test_text_list_flow_img_case(self):
        '''文本列表与图表'''
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()
        name = '流程历史_文本列表与图表'
        comp = FlowhistoryPhonePage(self.driver, name)
        self.assertTrue(comp.check_title(), msg=name + '检验不通过')
        self.assertEqual('审批节点', comp.get_table_head_first_td_text(), msg=name + '检验不通过')
        self.assertEqual('申请人', comp.get_table_tbody_first_td_text(), msg=name + '检验不通过')
        self.assertTrue(comp.check_flow_img(), msg=name + '检验不通过')
        
    def test_desription_case(self):
        '''描述'''
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()
        name = '流程历史_描述'
        comp = FlowhistoryPhonePage(self.driver, name)
        self.assertTrue(comp.is_desription_effect(name), msg=name + '检验不通过')

    def init(self):
        '''所有测试'''
#         self.test_text_list_case()
#         self.test_flow_img_case()
#         self.test_text_list_flow_img_case()
        self.test_desription_case()
        
        
if __name__ == '__main__':
    unittest.main()
