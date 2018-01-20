import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class NonPolymerizationTest(FlowTest):
    '''流程非聚合'''
    
    menu1 = '流程'
    menu2 = '审批送出设置'  # 主页打开菜单时使用
    menu3 = '流程非聚合'


    def test_non_polymerization_case(self):
        '''流程非聚合'''
        menu1 = '流程'
        menu2 = '审批送出设置'  # 主页打开菜单时使用
        menu3 = '流程非聚合'
        name = "流程非聚合"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲建单提交
        comp.launch_a_flowform(name)
        #time.sleep(0.5)
        #退出当前登录，切换账号并打开菜单记录
        comp.logoff_and_openrecord('weiqiang', '123456',menu1,menu2,menu3,name)
        #time.sleep(0.5)
        comp.direct_sumit()
        #退出当前登录，切换账号并打开菜单记录for表单
        comp.logoff_and_openmenu('zjl01', '123456',menu1,menu2,menu3)
        text = comp.openagain_to_getapprover(name)
        # 断言
        self.assertIn('张强', text, msg=name + "检验不通过")
        # 判断总经理此时有无提交按钮
        bb = comp.is_elementPresent()
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        #提交后判断流程是否已归档
        bool = comp.is_filed_for_aftersumbit(name)
        self.assertIsNone(bool, msg=name + "检验不通过")

        def init(self):
            self.test_non_polymerization_case()

if __name__ == '__main__':
    unittest.main()