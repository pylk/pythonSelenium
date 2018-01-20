import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class PolymerizationTest(FlowTest):
    '''流程聚合'''
    
    menu1 = '流程'
    menu2 = '审批送出设置'  # 主页打开菜单时使用
    menu3 = '流程聚合'


    def test_polymerization_case(self):
        '''流程聚合'''
        menu1 = '流程'
        menu2 = '审批送出设置'  # 主页打开菜单时使用
        menu3 = '流程聚合'
        name = "流程聚合"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        #判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲建单提交
        comp.launch_a_flowform(name)
        #time.sleep(0.5)
        #退出当前登录，切换账号并打开菜单记录for视图
        comp.logoff_and_openrecord('weiqiang', '123456',menu1,menu2,menu3,name)
        #time.sleep(0.5)
        comp.direct_sumit()
        #再次打开记录获取流程状态处理人
        text = comp.openagain_to_getapprover(name)
        self.assertIn('张强', text, msg=name + "检验不通过")
        #退出切换账号，查看是否有提交按钮
        bb = comp.logoff_and_check_submitbtn('zjl01', '123456',menu1,menu2,menu3,name)
        self.assertEqual("false",bb,msg=name + "检验不通过")
        # 退出当前登录，切换账号并打开菜单记录for视图
        comp.logoff_and_openrecord('zhangqiang', '123456',menu1,menu2,menu3,name)
        #time.sleep(0.5)
        comp.direct_sumit()
        #time.sleep(0.5)
        # 退出当前登录，切换账号并打开菜单记录for视图
        comp.logoff_and_openrecord('zjl01', '123456',menu1,menu2,menu3,name)
        #time.sleep(0.5)
        #表单是否已归档
        bool2 = comp.is_filed_for_aftersumbit(name)
        self.assertIsNone(bool2, msg=name + "检验不通过")

    def init(self):
        self.test_polymerization_case()

if __name__ == '__main__':
    unittest.main()

