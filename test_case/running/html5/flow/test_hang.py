import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class HangTest(FlowTest):
    '''流程挂起'''
    
    menu1 = '流程'
    menu2 = '流程通知'  # 主页打开菜单时使用
    menu3 = '流程挂起'

    def test_Hang_case(self):
        '''流程挂起'''
        menu1 = '流程'
        menu2 = '流程通知'  # 主页打开菜单时使用
        menu3 = '流程挂起'
        name = "流程挂起"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲建单提交
        comp.launch_a_flowform(name)
        #退出登录
        comp.goback()
        #切换张强账号登陆，
        comp.switch_account("zhangqiang", "123456")
        comp.close_message()
        # 打开菜单
        comp.open_m(menu1, menu2, menu3)
        #time.sleep(0.5)
        #检查有没有提交按钮
        bb = comp.is_submit_existed(name)
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        comp.click_hangbtn()
        #time.sleep(0.5)
        bb2 = comp.is_elementPresent()
        self.assertEqual("false", bb2, msg=name + "检验不通过")
        #time.sleep(0.5)
        comp.click_retracementbtn()
        #time.sleep(0.5)
        bb3 = comp.is_elementPresent()
        self.assertEqual("true", bb3, msg=name + "检验不通过")
        #time.sleep(0.5)
        comp.direct_sumit()
        #time.sleep(0.5)
        #'''表单是否已归档'''
        bool = comp.is_filed_for_openagin(name)
        self.assertIsNone(bool, msg=name + "检验不通过")

        def init(self):
            self.test_Hang_case()

if __name__ == '__main__':
    unittest.main()




