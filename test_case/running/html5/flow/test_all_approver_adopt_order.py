import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.app_test import AppTest
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
#引入鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains
#引入登陆操作类
from test_case.page_obj.login_page import LoginPage
#引入
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.view.list_view_page import ListViewPage


class AllapproverAdoptOrderTest(FlowTest):
    '''所有审批人按顺序'''
    
    menu1 = '流程'
    menu2 = '流程节点通过条件'  # 主页打开菜单时使用
    menu3 = '所有审批人按顺序'


    def test_allApprover_adopt_order_case(self):
        '''所有审批人按顺序'''
        menu1 = '流程'
        menu2 = '流程节点通过条件'  # 主页打开菜单时使用
        menu3 = '所有审批人按顺序'
        name = "所有审批人按顺序"
        #李玲提交，后流程处理人有没有王聪
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
        #time.sleep(0.5)
        #再次打开记录获取流程状态处理人
        text = comp.openagain_to_getapprover(name)
        #time.sleep(0.5)
        # 断言
        self.assertIn('王聪', text, msg=name + "检验不通过")
        #time.sleep(0.5)
        # 退出切换账号，查看是否有提交按钮
        bb = comp.logoff_and_check_submitbtn("zhangqiang", "123456",menu1, menu2, menu3,name)
        self.assertEqual("false", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        # 退出切换账号，查看是否有提交按钮
        bb2 = comp.logoff_and_check_submitbtn("weiqiang", "123456", menu1, menu2, menu3, name)
        self.assertEqual("false", bb2, msg=name + "检验不通过")
        #time.sleep(0.5)
        # 退出切换账号，查看是否有提交按钮
        bb3 = comp.logoff_and_check_submitbtn("wangcong", "123456", menu1, menu2, menu3, name)
        self.assertIn("true", bb3, msg=name + "检验不通过")
        #time.sleep(0.5)
        #提交后再次打开表单获取流程处理人
        text2 = comp.aftersumbit_getapprover(name)
        self.assertIn("伟强", text2, msg=name + "检验不通过")
        #time.sleep(0.5)
        # 退出切换账号，查看是否有提交按钮
        bb4 = comp.logoff_and_check_submitbtn("zhangqiang", "123456", menu1, menu2, menu3, name)
        self.assertEqual("false", bb4, msg=name + "检验不通过")
        #time.sleep(0.5)
        #伟强提交
        # 退出切换账号，查看是否有提交按钮
        bb5 = comp.logoff_and_check_submitbtn("weiqiang", "123456", menu1, menu2, menu3, name)
        self.assertEqual("true", bb5, msg=name + "检验不通过")
        #time.sleep(0.5)
        text3 = comp.aftersumbit_getapprover(name)
        self.assertIn("张强", text3, msg=name + "检验不通过")
        #time.sleep(0.5)
        #张强提交
        # 退出切换账号，查看是否有提交按钮
        bb6 = comp.logoff_and_check_submitbtn("zhangqiang", "123456", menu1, menu2, menu3, name)
        self.assertEqual("true", bb6, msg=name + "检验不通过")
        #提交后判断流程是否已归档
        bool = comp.is_filed_for_aftersumbit(name)
        self.assertIsNone(bool, msg=name + "检验不通过")

    def init(self):
        self.test_allApprover_adopt_order_case()

if __name__ == '__main__':
    unittest.main()
