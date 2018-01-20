import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.button_test import ButtonPhoneTest
from test_case.page_obj.login_page import LoginPage
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage
from test_case.page_obj.form.input_page import InputPhonePage


class ViewButtonPhoneTest(ButtonPhoneTest):
    '''视图按钮测试'''
    
    menu1 = '视图'
    menu2 = '视图按钮'
   
    def test_new_case(self):
        '''新建按钮'''
        menu3 = '按钮_case001'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        mp.wait_Tabloading_show_then_hide()
        btn = ButtonPhonePage(self.driver)
        btn.click_button('新建')   #点击新建
        mp.wait_Tabloading_show_then_hide()
        self.assertTrue(btn.is_button_exist('保存'), msg='新建按钮检验不通过')
    
    def test_delete_case(self):
        '''删除按钮'''
        menu3 = '按钮_case001'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        
        lp = ListViewPhonePage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()     #清空所有数据

        else:
            #新建一条数据
            btn = ButtonPhonePage(self.driver)
            btn.click_button('新建')   #点击新建
            mp.wait_Tabloading_show_then_hide()
            ip = InputPhonePage(self.driver, '单行文本')
            ip.element.send_keys('保存')
            btn.click_button('保存')
            mp.wait_Tabloading_show_then_hide()
            mp.wait_msg_show_then_hide()
            btn.click_button('返回')
            mp.wait_Tabloading_show_then_hide()
            #确定已经有一条数据
            self.assertEqual(1, lp.get_rows_total(), msg= '删除按钮检验不通过')
            lp.clear_all_data()   #点击全选
        
        self.assertEqual(0, lp.get_rows_total(), msg= '删除按钮检验不通过')
    
    def test_import_view_case(self):
        '''载入视图按钮'''
        menu3 = '按钮_case002'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        mp.wait_Tabloading_show_then_hide()
        
        btn = ButtonPhonePage(self.driver)
        btn.click_button('载入视图')   #点击载入视图
        mp.wait_Tabloading_show_then_hide()
        
        lp = ListViewPhonePage(self.driver)
        self.assertIsNotNone(lp.get_column_head('单行文本_载入视图'), msg='载入视图按钮检验不通过')

    def init(self):
#         self.test_new_case()
#         self.test_delete_case()
        self.test_import_view_case()
    
if __name__ == '__main__':
    unittest.main()