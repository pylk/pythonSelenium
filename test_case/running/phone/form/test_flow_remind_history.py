import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.page_obj.form.flow_remind_history_page import FlowRemindHistoryPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage
from test_case.running.phone.form.component_test import ComponentPhoneTest


class FlowRemindHistoryPhoneTest(ComponentPhoneTest):
    '''流程催办历史控件手机端测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '流程催办历史控件'
    
    def test_type_case(self):
        '''描述'''
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()
        name = '流程催办历史_描述'
        comp = FlowRemindHistoryPhonePage(self.driver, name)
        self.assertEqual('序号', comp.get_table_head_first_td_text(), msg=name + '检验不通过')
        self.assertEqual('1', comp.get_table_tbody_first_td_text(), msg=name + '检验不通过')

    def init(self):
        '''所有测试'''
        self.test_type_case()
        
        
if __name__ == '__main__':
    unittest.main()
