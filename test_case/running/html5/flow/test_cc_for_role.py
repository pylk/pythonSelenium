import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.app_test import AppTest
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class CcForRoleTest(FlowTest):
    '''流程抄送通过角色'''
    
    menu1 = '流程'
    menu2 = '抄送设置'  # 主页打开菜单时使用
    menu3 = '流程抄送'


    def test_ccForRole_case(self):
            '''流程抄送通过角色'''
            menu1 = '流程'
            menu2 = '抄送设置'  # 主页打开菜单时使用
            menu3 = '流程抄送'
            name = "流程抄送"
            name2 = "消息中心"
            #time.sleep(0.5)
            comp = ProcessApproverPage(self.driver)
            comp.goback()
            # 伟强去消息中心清空数据
            comp.switch_account('weiqiang', '123456')
            comp.go_messagecenter_toclear()
            #退出登录#33
            comp.goback()
            # 切换账号登陆
            comp.switch_account('liling', '123456')
            #李玲发起请假申请单
            comp.open_m(menu1,menu2,menu3)
            # 判断是否要删除记录
            lp = ListViewPage(self.driver)
            lp.judge_delete(name)
            comp.click_newbtn()
            #李玲建单提交
            # 录入请假原因
            comp.input_reason(name)
            # 点击提交按钮
            comp.click_flow_processbtn()
            #选择抄送人
            comp.select_user_by_rolename("测试主管")
            # 返回到表单所在的iframe
            comp.switch_to_formiframe()
            # 点击确认提交
            comp.submit()
            #退出登录
            comp.goback()
            #张强进入消息中心获取抄送消息
            comp.switch_account('weiqiang', '123456')
            # 获取消息中心的工作事项内容
            text = comp.get_messagecentercontent()
            self.assertIn("流程抄送",text,msg=name+"检验不通过")

    def init(self):
        self.test_ccForRole_case()

if __name__ == '__main__':
    unittest.main()
