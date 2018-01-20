import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class RemindersTest(FlowTest):
    '''流程催办'''
    
    menu1 = '流程'
    menu2 = '流程通知'  # 主页打开菜单时使用
    menu3 = '流程催办'

    def test_Reminders_case(self):
        '''流程催办'''
        menu1 = '流程'
        menu2 = '流程通知'  # 主页打开菜单时使用
        menu3 = '流程催办'
        name = "流程催办"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        #退出登录
        comp.goback()
        #切换张强账号登陆，
        comp.switch_account("zhangqiang", "123456")
        #进入消息中心清空工作事项通知"
        comp.go_messagecenter_toclear()
        #退出当前登录，切换账号并打开菜单记录for表单
        comp.logoff_and_openmenu("liling", "123456",menu1, menu2, menu3)
        #time.sleep(0.5)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲建单提交
        comp.launch_a_flowform(name)
        comp.openagain_record(name)
        bool = comp.is_btn_existed("act_flow_reminder")
        self.assertTrue(bool,msg=name + "检验不通过")
        #time.sleep(0.5)
        #发起催办
        comp.send_reminder("流程催办")
        #退出登录
        comp.goback()
        #切换张强账号登陆，
        comp.switch_account("zhangqiang", "123456")
        #获取消息中心的工作事项内容
        text = comp.get_messagecentercontent()
        self.assertIn("催办",text,msg=name+"检验不通过")



        def init(self):
            self.test_Reminders_case()

if __name__ == '__main__':
    unittest.main()