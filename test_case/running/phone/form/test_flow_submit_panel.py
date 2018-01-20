import sys
import unittest

import time

sys.path.append('../../../../')
from test_case.page_obj.form.flow_submit_panel_page import FlowSubmitPanelPage
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage
from test_case.page_obj.flow.flow_page import FlowPhonePage
from test_case.page_obj.page import PhonePage


class FlowSubmitPanelTest(ComponentPhoneTest):
    '''手机端流程面板测试'''

    menu1 = '流程'
    menu2 = '基本信息'
    menu3 = '流程基本信息_名称'  # 打开菜单

    def test_select_usefulopinions_case(self):
        '''选择常用意见'''
        bt = ButtonPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)

        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() != 0:
            lp.clear_all_data()  # 清除数据

        bt.click_button('新建')  # 点击按钮
        lp.wait_Tabloading_show_then_hide()
        bt.click_button('提交')  # 点击按钮
        fsp = FlowSubmitPanelPage(self.driver)
        fsp.click_usefulopinions()  # 展开常用意见
        fsp.wait_elem_visible('.flow-submit__proposal-box')
        fsp.select_usefulopinions('同意')  # 选择意见
        self.assertEqual('同意', fsp.get_usefulopinions(), msg='选择常用意见校验不通过')
        
        fsp.click_usefulopinions()  # 收起常用意见
        bt.click_flowpanel_button('提交')  # 点击按钮
        mp = MainPhonePage(self.driver)
        lp.wait_msg_show_then_hide()
        lp.wait_Tabloading_show_then_hide()
        mp.return_to_homepage()  # 返回主页
        mp.switch_to_flow_page()  # 切换到流程面板
        mp.switch_flow_center_byname('经办')  # 点击切换到经办页面
                
        mp.click_processing_first_data()  # 点击经办第一条数据
        fp = FlowPhonePage(self.driver)
        fp.click_flow_more()  # 点击更多切换到流程历史
        self.assertEqual('同意', fp.get_flow_history_useopinions(), msg='选择常用意见校验不通过')


    def init(self):
        self.test_select_usefulopinions_case()


if __name__ == '__main__':
    unittest.main()