import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class TimeoutSubmissionTest(FlowTest):
    '''审批超时自动提交'''
    
    menu1 = '流程'
    menu2 = '审批时限设置'  # 主页打开菜单时使用
    menu3 = '审批超时自动提交'


    def test_timeout_submit_case(self):
        """超时自动提交"""
        name = "审批超时自动提交"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        #把消息关掉
        self.driver.switch_to_default_content()
        comp.close_message() #关闭消息中心提示
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
        comp.wait_elem_visible('div[data-type="nodeItem"]') #等待提交节点显示
        # 点击确认提交
        comp.submit()
        # 再次相应记录
        comp.openagain_record(name)
        # 获取流程状态的处理人
        text = comp.get_approver()
        # 断言
        self.assertIn('王聪', text, msg=name + "检验不通过")
        #点击返回按钮
        comp.click_rebackbtn()
        time.sleep(60)  #等待系统超时自动提交，再验证是否已提交
        # 再次相应记录
        comp.openagain_record(name)
        #time.sleep(0.5)
        bool = comp.is_filed()
        self.assertIsNone(bool,msg=name + "检验不通过")

        def init(self):
            self.test_timeout_submit_case()

if __name__ == '__main__':
    unittest.main()