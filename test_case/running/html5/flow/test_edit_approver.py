import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class EditApproverTest(FlowTest):
    '''允许编辑当前节点的审批人'''
    
    menu1 = '流程'
    menu2 = '基本信息'  # 主页打开菜单时使用
    menu3 = '允许编辑当前节点的审批人'

    def test_editApprover_case(self):
        '''允许编辑当前节点的审批人'''
        menu1 = '流程'
        menu2 = '基本信息'  # 主页打开菜单时使用
        menu3 = '允许编辑当前节点的审批人'
        name = "允许编辑当前节点的审批人"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲建单提交
        comp.launch_a_flowform(name)
        #退出当前登录，切换账号并打开菜单记录
        comp.logoff_and_openrecord("zhangqiang", "123456",menu1, menu2, menu3,name)
        #time.sleep(0.5)
        comp.select_approver("测试主管")
        #time.sleep(0.5)
        bool = comp.is_elementPresent()
        self.assertEqual("true", bool, msg=name + "检验不通过")
        #time.sleep(0.5)
        #退出当前登录，切换账号并打开菜单记录
        comp.logoff_and_openrecord("weiqiang", "123456",menu1, menu2, menu3,name)
        #提交后判断流程是否已归档
        bool = comp.is_filed_for_aftersumbit(name)
        self.assertIsNone(bool, msg=name + "检验不通过")

        def init(self):
            self.test_editApprover_case()

if __name__ == '__main__':
    unittest.main()


