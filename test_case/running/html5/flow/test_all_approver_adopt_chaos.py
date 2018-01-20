import unittest
import time
import sys
sys.path.append('../../../../')
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class AllapproverAdoptChaosTest(FlowTest):
    '''所有审批人任意顺序'''
    
    menu1 = '流程'
    menu2 = '流程节点通过条件'  # 主页打开菜单时使用
    menu3 = '所有审批人任意顺序'


    def test_allApprover_adopt_chaos_case(self):
        """所有审批人任意顺序"""
        menu1 = '流程'
        menu2 = '流程节点通过条件'  # 主页打开菜单时使用
        menu3 = '所有审批人任意顺序'
        name = "所有审批人任意顺序"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        #把消息关掉
        self.driver.switch_to_default_content()
        comp.close_message()
        comp.switch_to_formiframe()
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #time.sleep(0.5)
        #李玲建单提交
        comp.launch_a_flowform(name)
        #再次打开记录获取流程状态处理人
        text = comp.openagain_to_getapprover(name)
        #断言
        self.assertIn('王聪', text, msg=name + "检验不通过")
        #time.sleep(0.5)
        #退出切换账号，查看是否有提交按钮
        bb = comp.logoff_and_check_submitbtn("zhangqiang","123456",menu1,menu2,menu3,name)
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        #提交后再次打开表单获取流程处理人
        text2 = comp.aftersumbit_getapprover(name)
        # 断言
        self.assertIn('王聪', text2, msg=name + "检验不通过")
        #time.sleep(0.5)
        # 退出切换账号，查看是否有提交按钮
        bb2 = comp.logoff_and_check_submitbtn("weiqiang", "123456",menu1, menu2, menu3,name)
        self.assertEqual("true", bb2, msg=name + "检验不通过")
        #time.sleep(0.5)
        #提交后再次打开表单获取流程处理人
        text3 = comp.aftersumbit_getapprover(name)
        self.assertIn('王聪', text3, msg=name + "检验不通过")
        #time.sleep(0.5)
        # 退出切换账号，查看是否有提交按钮
        bb3 = comp.logoff_and_check_submitbtn("wangcong", "123456",menu1, menu2, menu3,name)
        self.assertEqual("true", bb3, msg=name + "检验不通过")
        #time.sleep(0.5)
        #提交后判断流程是否已归档
        bool = comp.is_filed_for_aftersumbit(name)
        self.assertIsNone(bool, msg=name + "检验不通过")

        def init(self):
            self.allApprover_adopt_chaos_Test()

if __name__ == '__main__':
    unittest.main()
