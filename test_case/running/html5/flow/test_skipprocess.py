import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class SkipprocessTest(FlowTest):
    '''流程节点跳过'''
    
    menu1 = '流程'
    menu2 = '审批送出设置'  # 主页打开菜单时使用
    menu3 = '流程节点跳过'


    def test_skipprocess_case(self):
        """流程节点跳过"""
        name = "流程节点跳过"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        #把消息关掉
        self.driver.switch_to_default_content()
        comp.close_message()
        comp.switch_to_formiframe()
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        # 点击新建进入表单
        comp.click_newbtn()
        # 录入请假原因
        comp.input_reason(name)
        # 点击提交按钮
        comp.click_flow_processbtn()
        # 点击确认提交
        comp.submit()
        time.sleep(10)
        # 再次相应记录
        comp.openagain_record(name)
        #表单是否已归档
        bool = comp.is_filed()
        self.assertIsNone(bool,msg=name + "检验不通过")

    def init(self):
        self.test_skipprocess_case()

if __name__ == '__main__':
    unittest.main()
