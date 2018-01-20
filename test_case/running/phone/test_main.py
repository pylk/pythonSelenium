import sys

sys.path.append('../../../')
import unittest
from test_case.running.phone.app_test import AppPhoneTest
from test_case.page_obj.main_page import MainPhonePage


class MainPhoneTest(AppPhoneTest):
    '''手机端主页测试 '''

    def setUp(self):
        mp = MainPhonePage(self.driver)

    def tearDown(self):
        print('-------tearDown')
        mp = MainPhonePage(self.driver)
        if mp.is_loading_not_visible() == True and mp.is_msg_not_visible() == True:
            mp.return_to_homepage()

    def test_switch_todo_handle(self):
        '''主页我的待办和经办跟踪切换'''
        mp = MainPhonePage(self.driver)
        mp.wait_Tabloading_show_then_hide()
        self.assertTrue(mp.get_switch_nav_return(), msg='主页-我的待办和经办跟踪切换校验不通过')

    def test_open_mainpage_todo(self):
        '''打开 主页-我的待办'''
        mp = MainPhonePage(self.driver)
        mp.wait_Tabloading_show_then_hide()
        mp.click_todo_first_data()  # 打开主页-我的待办第一条数据
        mp.wait_Tabloading_show_then_hide()
        self.assertTrue(mp.find_element('#flowhis_panel').is_displayed(), msg='主页-我的待办打开校验不通过')

    def test_open_todo_more(self):
        '''打开 主页-我的待办-更多'''
        mp = MainPhonePage(self.driver)
        mp.wait_Tabloading_show_then_hide()
        mp.click_todo_handle_more()  # 点击主页-我的待办-更多
        mp.wait_Tabloading_show_then_hide()
        self.assertIn('待办', mp.find_element('.weui_navbar_item.weui_bar_item_on').text, msg='主页-我的待办-更多校验不通过')

    def test_open_mainpage_handle(self):
        '''打开经办跟踪'''
        mp = MainPhonePage(self.driver)
        mp.wait_Tabloading_show_then_hide()
        mp.click_handle_first_data()  # 点击主页-经办跟踪第一条数据
        mp.wait_Tabloading_show_then_hide()
        self.assertTrue(mp.find_element('#flowhis_panel').is_displayed(), msg='主页-经办跟踪打开校验不通过')

    def test_open_handle_more(self):
        '''打开 主页-经办跟踪-更多'''
        mp = MainPhonePage(self.driver)
        mp.wait_Tabloading_show_then_hide()
        mp.click_mainpage_handle()  # 点击切换主页-经办跟踪
        mp.click_todo_handle_more()  # 点击主页-经办跟踪-更多
        mp.wait_Tabloading_show_then_hide()
        self.assertIn('经办', mp.find_element('.weui_navbar_item.weui_bar_item_on').text, msg='主页-经办跟踪-更多校验不通过')

    def init(self):
        # self.test_switch_todo_handle()
        # self.test_open_mainpage_todo()
        # self.test_open_todo_more()
        # self.test_open_mainpage_handle()
        self.test_open_handle_more()

if __name__ == '__main__':
    unittest.main()
