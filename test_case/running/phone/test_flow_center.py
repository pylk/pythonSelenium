import sys

sys.path.append('../../../')
import unittest
from test_case.running.phone.app_test import AppPhoneTest
from test_case.page_obj.flow_center_page import FlowCenterPhonePage


class FlowCenterPhoneTest(AppPhoneTest):
    '''手机端流程中心测试 '''

    def setUp(self):
        fcp = FlowCenterPhonePage(self.driver)
        fcp.switch_to_flow_page()

    def tearDown(self):
        print('-------tearDown')
        fcp = FlowCenterPhonePage(self.driver)
        if fcp.is_loading_not_visible() == True and fcp.is_msg_not_visible() == True:
            fcp.return_to_homepage()

    def test_open_new_build(self):
        '''打开发起表单测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        menu1 = '表单'
        menu2 = '表单控件'
        menu3 = '单行文本框'
        fcp.open_menus(menu1, menu2, menu3)
        fcp.wait_Tabloading_show_then_hide()
        self.assertEqual('单行文本框_case001', self.driver.title, msg='流程中心-发起 校验不通过')

    def test_open_todo_list(self):
        '''打开待办测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('待办')
        fcp.wait_Tabloading_show_then_hide()
        fcp.click_pending_first_data()
        self.assertTrue(fcp.find_element('#flowhis_panel').is_displayed(), msg='流程中心-待办 校验不通过')

    def test_tdlist_all_filter(self):
        '''待办 全部 和 筛选 的打开折叠测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('待办')
        fcp.wait_Tabloading_show_then_hide()
        self.assertTrue(fcp.is_open_fold('全部\n▲'), msg='流程中心-待办-全部 展开校验不通过')
        self.assertFalse(fcp.is_open_fold('全部\n▲'), msg='流程中心-待办-全部 折叠校验不通过')
        self.assertTrue(fcp.is_open_fold('筛选\n▲'), msg='流程中心-待办-筛选 展开校验不通过')
        self.assertFalse(fcp.is_open_fold('筛选\n▲'), msg='流程中心-待办-筛选 折叠校验不通过')

    def test_tdlist_filter(self):
        '''待办的筛选测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('待办')
        fcp.wait_Tabloading_show_then_hide()
        rlis = fcp.find_elements('#pending .widgetItem.pending-list-con')
        self.assertTrue(fcp.is_filter_effect(rlis), msg='流程中心-待办-筛选 校验不通过')

    def test_open_handle(self):
        '''打开经办测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('经办')
        fcp.wait_Tabloading_show_then_hide()
        fcp.click_processing_first_data()
        self.assertTrue(fcp.find_element('#flowhis_panel').is_displayed(), msg='流程中心-经办 校验不通过')

    def test_handle_all_filter(self):
        '''经办 全部 和 筛选 的打开折叠测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('经办')
        fcp.wait_Tabloading_show_then_hide()
        self.assertTrue(fcp.is_open_fold('全部\n▲'), msg='流程中心-待办-全部 展开校验不通过')
        self.assertFalse(fcp.is_open_fold('全部\n▲'), msg='流程中心-待办-全部 折叠校验不通过')
        self.assertTrue(fcp.is_open_fold('筛选\n▲'), msg='流程中心-待办-筛选 展开校验不通过')
        self.assertFalse(fcp.is_open_fold('筛选\n▲'), msg='流程中心-待办-筛选 折叠校验不通过')

    def test_handle_filter(self):
        '''经办的筛选测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('经办')
        fcp.wait_Tabloading_show_then_hide()
        rlis = fcp.find_elements('.widgetItem.pending-list-con')
        self.assertTrue(fcp.is_filter_effect(rlis), msg='流程中心-经办-筛选 校验不通过')

    def test_open_history(self):
        '''打开历史测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('历史')
        fcp.wait_Tabloading_show_then_hide()
        fcp.click_finished_first_data()
        self.assertTrue(fcp.find_element('#flowhis_panel').is_displayed(), msg='流程中心-待办 校验不通过')

    def test_history_subject(self):
        '''主题搜索测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('历史')
        fcp.wait_Tabloading_show_then_hide()
        fcp.subject_search()  # 主题搜索
        self.assertTrue(fcp.get_subject_search_return, msg='流程中心-历史-主题搜索 校验不通过')

    def test_history_newbuild(self):
        '''我发起的筛选测试'''
        fcp = FlowCenterPhonePage(self.driver)
        fcp.wait_Tabloading_show_then_hide()
        fcp.switch_flow_center_byname('历史')
        fcp.wait_Tabloading_show_then_hide()
        fcp.click_new_build()
        self.assertTrue(fcp.get_click_newbuild_return(), msg='流程中心-历史-我发起的 校验不通过')

    def init(self):
        # self.test_open_new_build()
        # self.test_open_todo_list()
        # self.test_open_handle()
        # self.test_tdlist_all_filter()
        # self.test_handle_all_filter()
        self.test_tdlist_filter()
        # self.test_handle_filter()
        # self.test_open_history()
        # self.test_history_subject()
        # self.test_history_newbuild()


if __name__ == '__main__':
    unittest.main()
