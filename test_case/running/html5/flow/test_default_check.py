import os,sys
sys.path.append('../../../../')
import time
import unittest
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class DefaultCheckTest(FlowTest):
    '''并行默认选中'''
    
    menu1 = '流程'
    menu2 = '流程并行'  # 主页打开菜单时使用
    menu3 = '并行默认选中'


    def test_default_check_case(self):
        """并行默认选中"""
        name = "并行默认选中"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        #把消息关掉
        self.driver.switch_to_default_content()
        comp.close_message()
        comp.switch_to_formiframe()
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        # 点击新建进入表单
        comp.click_newbtn()
        # 录入请假原因
        comp.input_reason(name)
        # 点击提交按钮
        comp.click_flow_processbtn()
        #time.sleep(0.5)
        bool1 = comp.find_elem('fieldset#fieldset_commit_to > div:nth-child(2)>label>input').is_selected()
        self.assertTrue(bool1, msg=name + '检验不通过')
        bool2 = comp.find_elem('fieldset#fieldset_commit_to > div:nth-child(3)>label>input').is_selected()
        self.assertTrue(bool2, msg=name + '检验不通过')
        comp.find_elem('fieldset#fieldset_commit_to > div:nth-child(3)>label>input').click()
        # 点击确认提交
        comp.submit()
        #time.sleep(0.5)
        # 再次相应记录
        comp.openagain_record(name)
        # 获取流程状态的处理人
        text = comp.get_approver()
        # 断言
        self.assertIn('王聪', text, msg=name + "检验不通过")



        def init(self):
            self.test_default_check_case()

if __name__ == '__main__':
    unittest.main()