import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class TerminationTest(FlowTest):
    '''允许审批人终止流程'''
    
    menu1 = '流程'
    menu2 = '基本信息'  # 主页打开菜单时使用
    menu3 = '允许审批人终止流程'

    def test_termination_case(self):
        '''允许审批人终止流程'''
        menu1 = '流程'
        menu2 = '基本信息'  # 主页打开菜单时使用
        menu3 = '允许审批人终止流程'
        name = "允许审批人终止流程"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲建单提交
        comp.launch_a_flowform(name)
        #退出当前登录，切换账号并打开菜单记录for视图
        comp.logoff_and_openrecord("zhangqiang", "123456",menu1, menu2, menu3,name)
        #time.sleep(0.5)
        comp.click_terminationbtn() #点击终止按钮
        #time.sleep(0.5)
        # 判段是否已归档
        bool = comp.is_filed()
        self.assertIsNone(bool, msg=name + "检验不通过")

        def init(self):
            self.test_termination_case()

if __name__ == '__main__':
    unittest.main()


