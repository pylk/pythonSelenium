import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class RetreatTest(FlowTest):
    '''流程回撤'''
    
    menu1 = '流程'
    menu2 = '流程通知'  # 主页打开菜单时使用
    menu3 = '流程回撤'

    def test_retreat_case(self):
        '''流程回撤'''
        menu1 = '流程'
        menu2 = '流程通知'  # 主页打开菜单时使用
        menu3 = '流程回撤'
        name = "流程回撤"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲建单提交
        comp.launch_a_flowform(name)
        #退出切换账号，查看是否有提交按钮
        bb = comp.logoff_and_check_submitbtn("zhangqiang", "123456",menu1, menu2, menu3,name)
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        #退出切换账号，查看是否有提交按钮
        bb2 = comp.logoff_and_check_submitbtn("liling", "123456",menu1, menu2, menu3,name)
        self.assertEqual("false", bb2, msg=name + "检验不通过")
        #time.sleep(0.5)
        bool = comp.is_btn_existed("act_flow_retracement")
        self.assertTrue(bool,msg=name + "检验不通过")
        #time.sleep(0.5)
        #点击回撤按钮
        comp.click_retreatbtn()
        #time.sleep(0.5)
        text = comp.get_approver()
        self.assertIn("李玲",text,msg=name + "检验不通过")
        #time.sleep(0.5)
        comp.direct_sumit()
        text2 = comp.openagain_to_getapprover(name)
        self.assertIn("张强", text2, msg=name + "检验不通过")


        def init(self):
            self.test_retreat_case()

if __name__ == '__main__':
    unittest.main()