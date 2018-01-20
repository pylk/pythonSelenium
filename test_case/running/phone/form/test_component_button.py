import os
import sys
import time
import unittest

sys.path.append('../../../../')
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.running.phone.button_test import ButtonPhoneTest


class ComponentButtonPhoneTest(ButtonPhoneTest):
    '''手机端按钮控件保存类测试'''

    menu1 = '表单'
    menu2 = '表单按钮'
    menu3 = '按钮控件_保存类'

    def setUp(self):
        mp = MainPhonePage(self.driver)
        mp.switch_to_menu_page()
        mp.open_menus(self.menu1, self.menu2, self.menu3)  # 打开菜单
        
    def test_save_btn(self):
        '''保存按钮'''

        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开第一条数据
        bt = ButtonPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        bt.click_button('保存')  # 点击按钮
        self.assertEqual('[保存成功]', lp.get_msg(), msg='保存按钮检验不通过')

    def test_save_return_btn(self):
        '''保存并返回按钮'''

        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开第一条数据
        bt = ButtonPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        bt.click_button('保存并返回')  # 点击按钮
        self.assertEqual('[保存成功]', lp.get_msg(), msg='保存并返回按钮检验不通过')
        self.assertEqual('保存', lp.get_column_row1_col2(), msg='保存并返回按钮检验不通过')

    def test_save_draft_btn(self):
        '''保存草稿按钮'''

        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开第一条数据
        bt = ButtonPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        bt.click_button('保存草稿')  # 点击按钮
        self.assertEqual('[保存成功]', lp.get_msg(), msg='保存草稿按钮检验不通过')

    def test_save_copy_btn(self):
        '''保存并复制按钮'''

        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() != 0:
            lp.clear_all_data()  # 清除数据

        bt = ButtonPhonePage(self.driver)
        bt.click_button('新建')  # 点击新建
        lp.wait_Tabloading_show_then_hide()
        ip = InputPhonePage(self.driver, '单行文本')
        ip.element.send_keys('保存')  # 输入文本
        bt.click_button('保存并复制')  # 点击按钮
        msgtitle = lp.get_msg()  # 获取消息
        self.assertEqual('[保存成功]', msgtitle, msg='保存并复制按钮检验不通过')

        lp.wait_msg_show_then_hide()
        bt.click_button('返回')  # 点击按钮
        self.assertEqual(2, lp.get_rows_total(), msg='保存并复制按钮检验不通过')

    def test_save_new_btn(self):
        '''保存并新建按钮'''
        lp = ListViewPhonePage(self.driver)

        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() != 0:
            lp.clear_all_data()  # 清除数据

        bt = ButtonPhonePage(self.driver)
        bt.click_button('新建')  # 点击按钮

        lp.wait_Tabloading_show_then_hide()
        ip = InputPhonePage(self.driver, '单行文本')
        ip.element.send_keys('保存')  # 输入文本
        bt.click_button('保存并新建')  # 点击按钮
        msgtitle = lp.get_msg()  # 获取消息
        self.assertEqual('[保存成功]', msgtitle, msg='保存并新建按钮检验不通过')

        lp.wait_msg_show_then_hide()
        ip2 = InputPhonePage(self.driver, '单行文本')
        ip2.element.send_keys('保存')
        bt.click_button('保存')  # 点击按钮

        msgtitle = lp.get_msg()  # 获取消息
        self.assertEqual('[保存成功]', msgtitle, msg='保存并新建按钮检验不通过')

        lp.wait_msg_show_then_hide()
        bt.click_button('返回')  # 点击按钮
        self.assertEqual(2, lp.get_rows_total(), msg='保存并新建按钮检验不通过')

    def init(self):
        # self.test_save_btn()
        # self.test_save_return_btn()
        # self.test_save_draft_btn()
        # self.test_save_copy_btn()
        self.test_save_new_btn()


if __name__ == '__main__':
    unittest.main()
