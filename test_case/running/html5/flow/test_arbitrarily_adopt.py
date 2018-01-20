import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class ArbitrarilyAdoptTest(FlowTest):
    '''任意审批人通过则节点通过'''
    
    menu1 = '流程'
    menu2 = '流程节点通过条件'  # 主页打开菜单时使用
    menu3 = '任意审批人通过则节点通过'


    def test_arbitrarily_adopt_case(self):
        '''任意审批人通过则节点通过'''
        menu1 = '流程'
        menu2 = '流程节点通过条件'  # 主页打开菜单时使用
        menu3 = '任意审批人通过则节点通过'
        name = "任意审批人通过则节点通过"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        #把消息关掉
        self.driver.switch_to_default_content()
        comp.close_message()
        comp.switch_to_formiframe()
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        comp.launch_a_flowform(name)
        comp.goback()
        comp.switch_account('zhangqiang', '123456')
        comp.close_message()
        comp.open_m(menu1,menu2,menu3)
        text = comp.openagain_to_getapprover(name)
        # 断言
        self.assertIn('王聪', text, msg=name + "检验不通过")
        # 判断总经理此时有无提交按钮
        bb = comp.is_elementPresent()
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        #提交后判断流程是否已归档
        bool = comp.is_filed_for_aftersumbit(name)
        self.assertIsNone(bool, msg=name + "检验不通过")

        def init(self):
            self.test_arbitrarily_adopt_case()


if __name__ == '__main__':
    unittest.main()
