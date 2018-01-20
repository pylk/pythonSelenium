import sys

sys.path.append('../../../../')
import unittest
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.view.list_view_page import ListViewPage


class FreeFlowTest(FlowTest):
    '''自由流程测试'''

    menu1 = '流程'
    menu2 = '自由流程'
    menu3 = ''

    def test_freeflow_case(self):
        '''自由流程提交'''
        name = '自由流程直接提交'
        comp = ProcessApproverPage(self.driver)
        self.driver.switch_to_default_content()
        comp.close_message()
        comp.switch_to_formiframe()
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        if lp.get_rows_total() != 0:
            lp.delete_all_data()  # 删除所有数据
        comp.click_newbtn()  # 点击新建进入表单
        comp.input_reason(name)  # 录入请假原因
        comp.click_submit_star_flowbtn()  # 点击提交按钮
        comp.select_user('自动化测试组长')  # 选择审批人
        comp.submit()  # 点击确认发起
        lp.click_row()  # 打开第一条记录
        self.assertFalse(comp.is_flow_actbutton_exist('提交 _提交流程'), msg=name + '校验不通过')

    def test_flow_backoff(self):
        '''自由流程回退'''
        name = '自由流程回退'
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        if lp.get_rows_total() != 0:
            lp.delete_all_data()  # 删除所有数据
        comp.click_newbtn()  # 点击新建进入表单
        comp.input_reason(name)  # 录入请假原因
        comp.click_submit_star_flowbtn()  # 点击提交按钮
        comp.select_user('自动化测试组长')  # 选择审批人
        comp.submit()  # 点击确认提交
        comp.goback()  # 退出登录
        # 张强回退流程
        comp.switch_account('zhangqiang', '123456')  # 切换帐号
        self.open_3_menus()
        mp = MainPage(self.driver)
        mp.switch_to_iframe()
        lp.click_row()  # 点击第一条记录
        self.assertTrue(comp.is_flow_actbutton_exist('提交_回退流程'), msg=name + '校验不通过')
        comp.click_backoff_btn()  # 点击回退按钮
        comp.backoff_select_approver('李玲')  # 选择审批人
        comp.wait_lock_screen_div_not_visible()  # 等待用户选择div消失
        comp.submit()  # 点击确认回退

        comp.switch_account('liling', '123456')  # 切换帐号
        self.open_3_menus()
        mp = MainPage(self.driver)
        mp.switch_to_iframe()

        comp.wait_loading_hide()  # 等待视图loading消失
        lp.click_row()  # 点击第一条记录
        self.assertTrue(comp.is_flow_actbutton_exist('提交_回退流程'), msg=name + '校验不通过')

    def test_flow_complete(self):
        '''自由流程结束流程'''
        name = '自由流程结束流程'
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        if lp.get_rows_total() != 0:
            lp.delete_all_data()  # 删除所有数据

        comp.click_newbtn()  # 点击新建进入表单

        comp.input_reason(name)  # 录入请假原因
        comp.click_submit_star_flowbtn()  # 点击提交按钮
        comp.select_user('员工')  # 选择审批人
        comp.submit()  # 点击确认
        comp.wait_loading_hide()  # 等待视图loading消失
        lp.click_row()  # 点击第一条记录
        comp.click_end_flow()  # 点击结束流程按钮
        comp.wait_elem_visible('#flowprocessDiv #div_button_place')  # 等待流程面板展开按钮可见
        comp.submit()  # 点击确认按钮
        #
        comp.wait_loading_hide()  # 等待视图loading消失
        lp.click_row()  # 点击第一条记录
        self.assertFalse(comp.is_flow_actbutton_exist('提交 _结束流程'), msg=name + '校验不通过')

    def init(self):
        self.test_flow_backoff()



if __name__ == '__main__':
    unittest.main()
