import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.models.driver import browser
from test_case.running.html5.button_test import ButtonTest
from test_case.page_obj.login_page import LoginPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.view.list_view_page import ListViewPage
from test_case.page_obj.form.input_page import InputPage


class ViewButtonTest(ButtonTest):
    '''视图按钮测试'''
    
    menu1 = '视图'
    menu2 = '视图按钮'
   
    def test_new_case(self):
        '''新建按钮'''
        menu3 = '按钮_case001'
        self.open_menu3(menu3)  #打开菜单
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)   #点击新建
        #time.sleep(0.5)
        #确定已经跳转到对应的表单页面
        self.assertEqual('视图按钮测试用例-case001', btn.get_caption_text(), msg= '新建按钮检验不通过')
    
    def test_delete_case(self):
        '''删除按钮'''
        menu3 = '按钮_case001'
        self.open_menu3(menu3)  #打开菜单
        
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()     #清空所有数据
        
        #新建一条数据
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        #time.sleep(0.5)
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save_start)
        lp.wait_Tabloading_show_then_hide() #等待loading消失
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        lp.wait_loading_hide()  #视图中
        #确定已经有一条数据
        self.assertEqual(1, lp.get_rows_total(), msg= '删除按钮检验不通过')
        lp.click_select_all()   #点击全选
        btn.click_button(btn.del_btn)   #点击删除
        lp.click_alert_accept() #确定确认框
        lp.wait_loading_hide()  # 等待loading消失
        #确定数据条数为0
        self.assertEqual(0, lp.get_rows_total(), msg= '删除按钮检验不通过')
    
    def test_clear_data_case(self):
        '''清空所有数据按钮'''
        menu3 = '按钮_case001'
        self.open_menu3(menu3)  #打开菜单
        
        #新建一条数据
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        btn.wait_Tabloading_show_then_hide()
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save_start)
        btn.wait_Tabloading_show_then_hide()
        btn.click_button(btn.to_return)
        
        lp = ListViewPage(self.driver)
        lp.wait_loading_hide()  #表单中
        lp.wait_loading_hide()  #视图中
        #确定数据不止一条
        self.assertNotEqual(0, lp.get_rows_total(), msg= '清空所有数据按钮检验不通过')
        lp.clear_all_data()     #执行清空数据操作
        #确定数据为空
        self.assertEqual(0, lp.get_rows_total(), msg= '清空所有数据按钮检验不通过')
    
    def test_batch_submit_case(self):
        '''批量提交按钮'''
        menu3 = '按钮_case001'
        self.open_menu3(menu3)  #打开菜单
        
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()     #清空数据
        
        #新建一条数据
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        lp.wait_Tabloading_show_then_hide()
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save_start)
        lp.wait_Tabloading_show_then_hide()
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        lp.wait_loading_hide()  #视图中
        
        #确定数据不止一条
        self.assertNotEqual(0, lp.get_rows_total(), msg= '批量提交按钮检验不通过')
        lp.click_select_all()   #全选
        btn.click_button(btn.batch_submit)  #点击批量提交

        lp.wait_Tabloading_show_then_hide()
        mp = MainPage(self.driver)
        mp.switch_to_parent()       #切换到主页
        #time.sleep(0.5)
        lp.set_val_and_submit('请审批')    #填写审批意见并确定

        lp.wait_Tabloading_show_then_hide()
        mp.switch_to_iframe()   #切换回iframe中
        #time.sleep(0.5)
        lp.click_row()  #点击第一行数据
        lp.wait_Tabloading_show_then_hide()  # 等待表单页面的loading加载完
        #没有流程处理按钮则通过
        self.assertIsNone(btn.get_button(btn.flow_process), msg= '批量提交按钮检验不通过')
        
        btn.click_button(btn.to_return) #点击返回
        lp.wait_loading_hide()  #表单中
        lp.wait_loading_hide()  #视图中
        if 0 != lp.get_rows_total():    #清空数据
            lp.clear_all_data()
    
    
    def test_import_view_case(self):
        '''载入视图按钮'''
        menu3 = '按钮_case002'
        self.open_menu3(menu3)  #打开菜单
        
        btn = ButtonPage(self.driver)
        btn.wait_loading_hide() #等待视图加载完
        btn.click_button(btn.import_view)   #点击载入视图
        #time.sleep(0.5)
        btn.wait_loading_hide() #等待后台响应返回新的视图页面
        btn.wait_loading_hide() #等待视图加载完
        
        lp = ListViewPage(self.driver)
        self.assertEqual('单行文本_载入视图', lp.get_head_td1_text(), msg= '载入视图按钮检验不通过')
    
    def test_jump_url_current_page_btn(self):
        '''跳转(当前页)按钮'''
        menu3 = '按钮_case002'
        self.open_menu3(menu3)      #打开菜单
        
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转(当前页)')  #点击跳转
        #time.sleep(0.5)
        lp = ListViewPage(self.driver)
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '跳转(当前页)按钮检验不通过')
        
    def test_jump_url_div_btn(self):
        '''跳转(弹出层)按钮'''
        menu3 = '按钮_case002'
        self.open_menu3(menu3)
        
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转(弹出层)')
        
        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()
        
        #time.sleep(0.5)
        lp = ListViewPage(self.driver)
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '跳转(弹出层)按钮检验不通过')
        
    def test_jump_url_tab_page_btn(self):
        '''跳转(页签)按钮'''
        menu3 = '按钮_case002'
        self.open_menu3(menu3)
        
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转(页签)')
        
        #time.sleep(0.5)
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        mp.switch_to_iframe()
        lp = ListViewPage(self.driver)
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '跳转(页签)按钮检验不通过')
        
    def test_jump_url_new_window_btn(self):
        '''跳转(新窗口)按钮'''
        menu3 = '按钮_case002'
        self.open_menu3(menu3)
        
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转(新窗口)')
        
        #time.sleep(0.5)
        lp = ListViewPage(self.driver)
        lp.switch_to_another_window()
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '跳转(新窗口)按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()
        
    def test_page_print_btn(self):
        '''网页打印按钮'''
        menu3 = '按钮_case003'
        self.open_menu3(menu3)  #打开菜单
        
        btn = ButtonPage(self.driver)
        btn.click_button(btn.view_page_print)   #点击打印按钮
        
        #time.sleep(0.5)
        lp = ListViewPage(self.driver)
        lp.switch_to_another_window()
        self.assertEqual('单行文本', lp.get_print_table_head_td1_text(), msg= '网页打印按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()
        
    def init(self):
#         self.test_new_case()
#         self.test_delete_case()
#         self.test_clear_data_case()
#         self.test_batch_submit_case()
        self.test_import_view_case()
#         self.test_jump_url_current_page_btn()
#         self.test_jump_url_div_btn()
#         self.test_jump_url_tab_page_btn()
#         self.test_jump_url_new_window_btn()
#         self.test_page_print_btn()
    
if __name__ == '__main__':
    unittest.main()