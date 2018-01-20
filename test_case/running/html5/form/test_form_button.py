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
from test_case.page_obj.flow.flow_page import ProcessApproverPage


class FormButtonTest(ButtonTest):
    '''表单栏按钮测试'''

    menu1 = '表单'
    menu2 = '表单按钮'

    def test_button_self_print_case(self):
        '''自定义打印按钮'''
        menu3 = '表单按钮_打印导出下载等'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()
        #time.sleep(0.5)
        comp = InputPage(self.driver, '单行文本')
        btn = ButtonPage(self.driver)
        btn.open_and_switch_to_self_print_page()
        self.assertNotEqual('none', comp.find_element_by_css_selector('#MyappsReport'), msg= '自定义打印按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()

    def test_save_btn(self):
        '''保存按钮'''
        menu3 = '表单按钮_保存类'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        '''触发保存、获取提醒消息并返回'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        lp.wait_Tabloading_show_then_hide()
        btn.click_button(btn.save)
        self.assertTrue(lp.is_msg_visiable(),msg= '保存按钮检验不通过')
        msgtitle = lp.is_test_in_msg('保存成功')
        self.assertTrue(msgtitle, msg= '保存按钮检验不通过')
        lp.wait_Tabloading_show_then_hide()

    def test_save_return_btn(self):
        '''保存并返回按钮'''
        menu3 = '表单按钮_保存类'
        Process_approver = ProcessApproverPage(self.driver)
        Process_approver.close_message()
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save_return)
        msgtitle = lp.is_test_in_msg('保存成功')
        #self.assertTrue(lp.is_msg_visiable(),msg='保存并返回按钮检验不通过')
        self.assertTrue(msgtitle, msg='保存并返回按钮检验不通过')
        lp.wait_loading_hide()  # 等待视图加载
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '保存并返回按钮检验不通过')

    def test_save_draft_btn(self):
        '''保存草稿按钮'''
        menu3 = '表单按钮_保存类'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        lp.wait_loading_hide()
        btn.click_button(btn.save_draft)
        self.assertTrue(lp.is_msg_visiable(), msg='保存草稿按钮检验不通过')
        msgtitle = lp.is_test_in_msg('保存成功')
        self.assertTrue(msgtitle, msg='保存草稿按钮检验不通过')

    def test_save_copy_btn(self):
        '''保存并复制按钮'''
        menu3 = '表单按钮_保存并复制'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        #time.sleep(0.5)
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save_copy)
        #time.sleep(0.5)
        self.assertTrue(lp.is_msg_visiable(),msg='保存并复制按钮检验不通过')
        msgtitle = lp.is_test_in_msg('保存成功')
        self.assertTrue(msgtitle, msg='保存并复制按钮检验不通过')
        lp.wait_loading_hide()
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        self.assertEqual(2, lp.get_rows_total(), msg= '保存并复制按钮检验不通过')
        lp.clear_all_data()


    def test_save_start_btn(self):
        '''保存并启动按钮'''
        menu3 = '表单按钮_流程相关'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        lp.wait_Tabloading_show_then_hide()
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save_start)
        lp.wait_Tabloading_show_then_hide()
        self.assertTrue(lp.is_msg_visiable(),msg='保存并启动按钮提示检验不通过')
        msgtitle = lp.is_test_in_msg('保存成功')
        self.assertTrue(msgtitle, msg='保存并启动按钮提示检验不通过')
        lp.wait_Tabloading_show_then_hide()
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        if 0 != lp.get_rows_total():
            lp.clear_all_data()


    def test_flow_start_user_appoint_btn(self):
        '''流程启动用户指定按钮'''
        menu3 = '表单按钮_流程相关'
        Process_approver = ProcessApproverPage(self.driver)
        Process_approver.close_message()
        self.open_menu3(menu3)
        #清数据
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        #新建记录
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        #time.sleep(0.5)
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        #点击流程启动用户指定按钮
        btn.click_button(btn.flow_start)
        #time.sleep(0.5)
        mp = MainPage(self.driver)
        #切到iframe
        mp.switch_to_div_iframe()
        #在启动流程界面指定流程并确定
        btn.appoint_flow()
        mp.switch_to_parent()
        mp.switch_to_iframe()
        #time.sleep(0.5)
        msgtitle = lp.is_test_in_msg('成功保存并开启流程')
        self.assertTrue(msgtitle, msg='流程启动用户指定按钮检验不通过')
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

    def test_flow_start_iscript_btn(self):
        '''流程启动脚本指定按钮'''
        menu3 = '表单按钮_流程相关'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        #time.sleep(0.5)
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        #点击第二个流程启动按钮
        btn.click_default_btn("流程启动脚本")
        #time.sleep(0.5)
        msgtitle = lp.is_test_in_msg('成功保存并开启流程')
        self.assertTrue(msgtitle, msg='流程启动脚本指定按钮检验不通过')
        lp.wait_loading_hide()  # 等待视图加载完成
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        #time.sleep(0.5)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

    def test_flow_process_btn(self):
        '''流程处理按钮'''
        menu3 = '表单按钮_流程相关'
        Process_approver = ProcessApproverPage(self.driver)
        Process_approver.close_message()
        self.open_menu3(menu3)
        #time.sleep(0.5)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        #time.sleep(0.5)
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        #time.sleep(0.5)
        btn.click_button(btn.flow_process) #点击流程提交按钮
        #time.sleep(0.3)
        btn.click_confirm_submit()
        msgtitle = lp.is_test_in_msg('提交成功')
        self.assertTrue(msgtitle, msg= '流程处理按钮检验不通过')
        #time.sleep(0.5)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

    def test_form_page_print_history_btn(self):
        '''网页打印（带流程历史）按钮'''
        menu3 = '表单按钮_流程相关'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        #time.sleep(0.5)
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.form_page_print_history)
        #time.sleep(0.5)
        ip.switch_to_another_window()
        self.assertNotEqual('none', btn.get_history(), msg= '网页打印（带流程历史）按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()

    def test_to_return_btn(self):
        '''返回按钮'''
        menu3 = '表单按钮_分享签章返回等'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        #time.sleep(0.5)
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save)
        #time.sleep(0.5)
        lp.wait_loading_hide()  # 等待视图加载完成
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        self.assertEqual(1, lp.get_rows_total(), msg= '返回按钮检验不通过')
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

    def test_form_page_print_btn(self):
        '''网页打印按钮'''
        menu3 = '表单按钮_打印导出下载等'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.form_page_print)
        #time.sleep(0.5)
        lp.switch_to_another_window()
        #time.sleep(0.5)
        self.assertEqual('按钮测试用例-打印导出下载', btn.get_caption_text(), msg= '网页打印按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()

    def test_user_defined_not_btn(self):
        '''自定义无按钮'''
        menu3 = '表单按钮_自定义按钮'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.user_defined)
        #time.sleep(0.5)
        msgtitle = lp.is_test_in_msg('自定义无成功')
        self.assertTrue(msgtitle, msg='自定义无按钮检验不通过')

    def test_user_defined_return_btn(self):
        '''自定义返回按钮'''
        menu3 = '表单按钮_自定义按钮'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
            lp.add_one_row2()  #添加一条数据
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()
        btn = ButtonPage(self.driver)
        btn.click_default_btn("自定义返回")
        msgtitle = lp.is_test_in_msg('自定义返回成功')
        self.assertTrue(msgtitle, msg='自定义返回按钮检验不通过')

    def test_user_defined_close_btn(self):
        '''自定义关闭按钮'''
        menu3 = '表单按钮_自定义关闭按钮'
        Process_approver = ProcessApproverPage(self.driver)
        Process_approver.close_message()    #
        self.open_menu3(menu3)  # 打开三级菜单
        lp = ListViewPage(self.driver)
        # 清空多余数据
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
            lp.add_one_row_div()
        # 无数据时添加一条数据
        if lp.get_rows_total() == 0:
            lp.add_one_row_div()
        # 点击第一条数据
        lp.open_fisrt_doc()

        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()   # 切换到弹出层页面

        btn = ButtonPage(self.driver)
        btn.click_default_btn("自定义关闭") #点击自定义关闭按钮
        self.assertTrue(lp.is_msg_visiable(),msg='自定义关闭按钮检验不通过')
        msgtitle = lp.is_test_in_msg('自定义关闭成功')
        self.assertTrue(msgtitle, msg='自定义关闭按钮检验不通过')
        lp.wait_loading_hide()  # 等待视图加载完成
        self.assertTrue(mp.div_is_close(), msg= '自定义关闭按钮检验不通过')

    def test_user_defined_jump_btn(self):
        '''自定义跳转按钮'''
        menu3 = '表单按钮_自定义按钮'
        Process_approver = ProcessApproverPage(self.driver)
        Process_approver.close_message()
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_default_btn("自定义跳转列表")
        self.assertTrue(lp.is_msg_visiable(),msg='自定义跳转按钮检验不通过')
        msgtitle = lp.is_test_in_msg('自定义跳转列表成功')
        self.assertTrue(msgtitle, msg='自定义跳转按钮检验不通过')
        #time.sleep(0.5)
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '自定义跳转按钮检验不通过')

    def test_jump_form_div_btn(self):
        '''跳转动态表单弹出层按钮'''
        menu3 = '表单按钮_跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转动态表单弹出层')

        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()

        #time.sleep(0.5)
        self.assertEqual('按钮测试用例-保存类', btn.get_caption_text(), msg= '跳转动态表单弹出层按钮检验不通过')

    def test_jump_form_current_page_btn(self):
        '''跳转动态表单当前页按钮'''
        menu3 = '表单按钮_跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转动态表单当前页')

        #time.sleep(0.5)
        self.assertEqual('按钮测试用例-保存类', btn.get_caption_text(), msg= '跳转动态表单当前页按钮检验不通过')

    def test_jump_form_tab_page_btn(self):
        '''跳转动态表单页签按钮'''
        menu3 = '表单按钮_跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转动态表单页签')

        #time.sleep(0.5)
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertEqual('按钮测试用例-保存类', btn.get_caption_text(), msg= '跳转动态表单页签按钮检验不通过')

    def test_jump_form_new_window_btn(self):
        '''跳转动态表单新窗口按钮'''
        menu3 = '表单按钮_跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据

        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转动态表单新窗口')

        #time.sleep(0.5)
        lp.switch_to_another_window()
        self.assertEqual('按钮测试用例-保存类', btn.get_caption_text(), msg= '跳转动态表单新窗口按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()

    def test_jump_url_div_btn(self):
        '''跳转url弹出层按钮'''
        menu3 = '表单按钮_跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()


        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转URL弹出层')

        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()

        #time.sleep(0.5)
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '跳转URL弹出层按钮检验不通过')

    def test_jump_url_current_page_btn(self):
        '''跳转url当前页按钮'''
        menu3 = '表单按钮_跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn) #点击新建按钮
        lp.wait_Tabloading_show_then_hide()
        btn.click_button_by_type_title(btn.jump_to, '跳转URL当前页面')

        lp.wait_loading_hide() #等待视图页面加载
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '跳转URL当前页面按钮检验不通过')

    def test_jump_url_tab_page_btn(self):
        '''跳转URL页签按钮'''
        menu3 = '表单按钮_跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转URL页签')

        #time.sleep(0.5)
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '跳转URL当前页面按钮检验不通过')

        mp.switch_to_parent()
        mp.close_current_nav()
        mp.switch_to_iframe()   #切换到当前打开页签
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        #time.sleep(0.5)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

    def test_jump_url_new_window_btn(self):
        '''跳转URL新窗口按钮'''
        menu3 = '表单按钮_跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)

        if 0 != lp.get_rows_total():
            lp.clear_all_data()

        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据
        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转URL新窗口')

        #time.sleep(0.5)
        lp.switch_to_another_window()
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '跳转URL当前页面按钮检验不通过')
        lp.close_currentwindow()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()
        #time.sleep(0.3)
        mp.switch_to_iframe()   #切换到当前打开页签
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        #time.sleep(0.5)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

    def test_share_btn(self):
        '''分享按钮'''
        menu3 = '表单按钮_分享签章返回等'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)

        if lp.get_rows_total() == 0:
            lp.add_one_row2()    # 添加一条数据
        lp.open_fisrt_doc() #点击一条数据

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.share_to)  #点击分享按钮

        #time.sleep(0.5)
        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()   # 切换到分享弹出层

        btn.to_share()  # 点击选择邮件复选框，然后点击选择按钮
        #time.sleep(0.5)
        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()   # 切换到用户选择框弹出层

        btn.select_userbyrolename("员工") # 选择员工用户并确定
        time.sleep(0.5)

        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()   # 切换到分享弹出层中
        btn.click_send()    # 点击发送
        self.assertEqual('已发送', btn.get_msg_share_page(), msg='分享按钮检验不通过')

    def test_signature_btn(self):
        '''签章按钮'''
        menu3 = '表单按钮_分享签章返回等'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

        if lp.get_rows_total() == 0:
            lp.add_one_row2()    #无数据时添加一条数据

        lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.signature)

        #time.sleep(0.5)
        btn.select_signature()  #选择签章
        lp.alert_send_keys('123456')    #输入密码
        lp.click_alert_accept() #点击确定
        btn.confirm_signature() #确认盖章
        self.assertTrue(lp.is_msg_visiable(),msg= '签章按钮检验不通过')
        msgtitle = lp.is_test_in_msg('签章成功！') #获取消息
        self.assertTrue(msgtitle, msg= '签章按钮检验不通过')
        btn.wait_loading_hide()
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

    def test_close_window_btn(self):
        '''关闭窗口按钮'''
        menu3 = '表单按钮_关闭窗口'
        self.open_menu3(menu3)
        mp = MainPage(self.driver)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        if lp.get_rows_total() == 0:
            lp.add_one_row_div()    #无数据时添加一条数据
        lp.open_fisrt_doc() #点击第一条数据
        mp.switch_to_div_iframe()   #切换到弹出层页面
        btn = ButtonPage(self.driver)
        btn.click_button(btn.close_window)  #点击关闭窗口按钮
        mp.switch_to_iframe()   #切换到当前打开页签
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '关闭窗口按钮检验不通过')
        if 0 != lp.get_rows_total():
            lp.clear_all_data()

    def init(self):

#         self.test_button_print_case()
#         self.test_button_self_print_case()
#         self.test_save_btn()
#         self.test_save_return_btn()
#         self.test_save_draft_btn()
#         self.test_save_copy_btn()
#         self.test_save_start_btn()
#         self.test_flow_start_user_appoint_btn()
#         self.test_flow_start_iscript_btn()
#         self.test_flow_process_btn()
#         self.test_form_page_print_history_btn()
#         self.test_to_return_btn()
#         self.test_form_page_print_btn()
#         self.test_user_defined_not_btn()
#         self.test_user_defined_return_btn()
#         self.test_user_defined_close_btn()
#         self.test_user_defined_jump_btn()
#         self.test_jump_form_div_btn()
#         self.test_jump_form_current_page_btn()
#         self.test_jump_form_tab_page_btn()
#         self.test_jump_form_new_window_btn()
#         self.test_jump_url_div_btn()
#         self.test_jump_url_current_page_btn()
#         self.test_jump_url_tab_page_btn()
#         self.test_jump_url_new_window_btn()
#         self.test_share_btn()
        self.test_signature_btn()
#         self.test_close_window_btn()

if __name__ == '__main__':
    unittest.main()