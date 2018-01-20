import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class FallbackTest(FlowTest):
    '''流程回退'''
    
    menu1 = '流程'
    menu2 = '流程通知'  # 主页打开菜单时使用
    menu3 = '流程回退'

    def test_Fallback_case(self):
        '''流程回退'''
        menu1 = '流程'
        menu2 = '流程通知'  # 主页打开菜单时使用
        menu3 = '流程回退'
        name = "流程回退"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        #把消息关掉
        self.driver.switch_to_default_content()
        comp.close_message()
        comp.switch_to_formiframe()
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲建单提交
        comp.launch_a_flowform(name)
		#进入消息中心清空工作事项通知
        comp.go_messagecenter_toclear()
        #退出切换账号，查看是否有提交按钮
        bb = comp.logoff_and_check_submitbtn("zhangqiang", "123456",menu1, menu2, menu3,name)
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        comp.click_fallbackbtn()
        #退出登录
        comp.goback()
        #切换张强账号登陆，
        comp.switch_account("liling", "123456")
        #获取消息中心的工作事项内容
        text = comp.get_messagecentercontent()
        self.assertIn("流程回退",text,msg=name+"检验不通过")
        bname = '消息中心'
        comp.close_tab(bname)
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        # 打开菜单c
        comp.open_m(menu1, menu2, menu3)
        #time.sleep(0.5)
        #检查有没有提交按钮
        bb = comp.is_submit_existed(name)
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        #提交后再次打开表单获取流程处理人
        text = comp.aftersumbit_getapprover(name)
        #time.sleep(0.5)
        self.assertIn('张强',text,msg=name + "检验不通过")

    def init(self):
        self.test_Fallback_case()

if __name__ == '__main__':
    unittest.main()




