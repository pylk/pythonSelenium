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
from selenium.webdriver.common.action_chains import ActionChains


class ComponentButtonTest(ButtonTest):
    '''按钮控件测试'''
    
    menu1 = '表单'
    menu2 = '表单按钮'

    def test_save_btn_case(self):
        '''保存按钮'''
        menu3 = '按钮控件_保存类'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        lp.open_fisrt_doc()
        #time.sleep(0.5)
        '''触发保存、获取提醒消息并返回'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        #time.sleep(0.5)
        self.assertEqual('[保存成功]', lp.get_msg(), msg= '保存按钮检验不通过')

    def test_save_return_btn_case(self):
        '''保存并返回按钮'''
        menu3 = '按钮控件_保存类'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        lp.open_fisrt_doc()
        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save_return)
        self.assertEqual('[保存成功]', lp.get_msg(), msg= '保存并返回按钮检验不通过')
        #time.sleep(0.5)
        self.assertEqual('保存', lp.get_column_row1_col1(), msg= '保存并返回按钮检验不通过')

    def test_save_draft_btn_case(self):
        '''保存草稿按钮'''
        menu3 = '按钮控件_保存类'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        lp.open_fisrt_doc()
        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save_draft)
        #time.sleep(0.5)
        self.assertEqual('[保存成功]', lp.get_msg(), msg= '保存草稿按钮检验不通过')

    def test_save_copy_btn_case(self):
        '''保存并复制按钮'''
        menu3 = '按钮控件_保存并复制和新建'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save_copy)
        #time.sleep(0.5)
        self.assertEqual('[保存成功]', lp.get_msg(), msg= '保存并复制按钮检验不通过')
        lp.wait_loading_hide()
        btn.click_button(btn.to_return)
        lp.wait_loading_hide()  #表单中
        lp.wait_loading_hide()  #视图中
        #time.sleep(0.5)
        self.assertEqual(2, lp.get_rows_total(), msg= '保存并复制按钮检验不通过')
        lp.clear_all_data()

    def test_save_new_btn_case(self):
        '''保存并新建按钮'''
        menu3 = '按钮控件_保存并复制和新建'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        if 0 != lp.get_rows_total():
            lp.clear_all_data()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn) #点击新建按钮
        lp.wait_loading_hide()  # 等待loading消失
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save_new) #点击保存并新建按钮
        self.assertEqual('[保存成功]', lp.get_msg(), msg= '保存并新建按钮检验不通过')
        lp.wait_loading_hide() #等待loading消失
        time.sleep(10)
        ip2 = InputPage(self.driver, '单行文本')
        ip2.element.send_keys('保存')
        btn.click_button(btn.save)
        lp.wait_loading_hide()  # 等待loading消失
        time.sleep(10)
        btn.click_button(btn.to_return)
        if(lp.is_alert_present()):
            lp.accept_alert()
        lp.wait_loading_hide()  #等待loading消失
        self.assertEqual(2, lp.get_rows_total(), msg= '保存并新建按钮检验不通过')
        lp.clear_all_data()

    def test_jump_form_current_page_btn_case(self):
        '''跳转动态表单当前页按钮'''
        menu3 = '按钮控件_自定义跳转'
        self.open_menu3(menu3)
        #lp = ListViewPage(self.driver)
        #lp.open_fisrt_doc()

        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转动态表单当前页')

        #time.sleep(0.5)
        self.assertEqual('按钮测试用例-保存类', btn.get_caption_text(), msg='跳转动态表单当前页按钮检验不通过')

    def test_jump_url_tab_page_btn_case(self):
        '''跳转URL页签按钮'''
        menu3 = '按钮控件_自定义跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)

        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转URL页签')

        #time.sleep(0.5)
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertEqual('保存', lp.get_column_row1_col1(), msg='跳转URL当前页面按钮检验不通过')

    def test_jump_url_new_window_btn_case(self):
        '''跳转URL新窗口按钮'''
        menu3 = '按钮控件_自定义跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)

        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转URL新窗口')

        #time.sleep(0.5)
        lp.switch_to_another_window()
        self.assertEqual('保存', lp.get_column_row1_col1(), msg='跳转URL当前页面按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()

    def test_jump_url_div_btn_case(self):
        '''跳转url弹出层按钮'''
        menu3 = '按钮控件_自定义跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)

        btn = ButtonPage(self.driver)
        btn.click_button_by_type_title(btn.jump_to, '跳转动态表单弹出层')

        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()

        #time.sleep(0.5)
        self.assertEqual('按钮测试用例-保存类', btn.get_caption_text(), msg='跳转动态表单当前页按钮检验不通过')

    def test_user_defined_btn_case(self):
        '''自定义按钮'''
        menu3 = '按钮控件_自定义跳转'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        #lp.open_fisrt_doc()

        btn = ButtonPage(self.driver)
        bool1 = lp.find_elem('input[value="未更新"]').is_selected()
        self.assertFalse(bool1,msg='自定义按钮检验不通过')
        #time.sleep(0.5)
        bool2 = lp.find_elem('input[value="已更新"]').is_selected()
        self.assertFalse(bool2,msg='自定义按钮检验不通过')
        lp.find_elem('input[name="名称"]').send_keys("测试")
        btn.click_button(btn.save)
        lp.wait_loading_hide()
        btn.click_button(btn.user_defined)
        lp.wait_refresh_loading_back_show_then_hide()
        bool3 = lp.find_elem('input[value="已更新"]').is_selected()
        self.assertTrue(bool3,msg='自定义按钮检验不通过')
        #self.assertEqual('[自定义成功]', lp.get_msg(), msg='自定义按钮检验不通过')

    def test_form_page_print_btn_case(self):
        '''网页打印按钮'''
        menu3 = '按钮控件_打印导出下载等'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)

        btn = ButtonPage(self.driver)
        btn.click_button(btn.form_page_print)
        #time.sleep(0.5)
        lp.switch_to_another_window()
        #time.sleep(0.5)
        self.assertEqual('按钮测试用例-保存类', btn.get_caption_text(), msg='网页打印按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()

    def test_button_self_print_case(self):
        '''自定义打印按钮'''
        menu3 = '按钮控件_打印导出下载等'
        self.open_menu3(menu3)
        comp = InputPage(self.driver, '单行文本')
        btn = ButtonPage(self.driver)
        btn.open_and_switch_to_self_print_page()
        self.assertNotEqual('none', comp.find_element_by_css_selector('#MyappsReport'), msg= '自定义打印按钮检验不通过')
        self.driver.close()
        mp = MainPage(self.driver)
        mp.switch_to_current_window()

    def test_share_btn_case(self):
        '''分享按钮'''
        menu3 = '按钮控件_分享签章返回等'
        self.open_menu3(menu3)
        mp = MainPage(self.driver)
        btn = ButtonPage(self.driver)
        self.assertIsNone(mp.find_elem('.btn-info[title="分享"]'),msg='表单未保存时分享按钮不应存在，测试不通过')
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        btn.click_button(btn.save)#点击保存按钮
        mp.wait_Tabloading_show_then_hide()#等待loading消失
        self.assertFalse(mp.is_elem_invisibility('.btn-info[title="分享"]'), msg='表单未保存时分享按钮不应存在，测试不通过')
        btn.click_button(btn.share_to) #点击分享按钮
        mp.switch_to_div_iframe()   #切换到分享弹出层中
        btn.to_share()  #点击选择邮件复选框，然后点击选择按钮
        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()   #切换到用户选择框弹出层
        btn.select_user()   # 选择用户
        mp.switch_to_div_iframe()   # 切换到分享弹出层中
        btn.click_send()    # 点击发送
        self.assertEqual('已发送', btn.get_msg_share_page(), msg='分享按钮检验不通过')

    def test_signature_btn(self):
        '''签章按钮'''
        menu3 = '按钮控件_分享签章返回等'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        #lp.open_fisrt_doc()

        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.signature)

        #time.sleep(0.5)
        btn.select_signature()
        lp.alert_send_keys('123456')
        lp.click_alert_accept()

        #time.sleep(0.5)
        btn.confirm_signature()
        #time.sleep(0.5)
        self.assertEqual('[签章成功！]', lp.get_msg(), msg='签章按钮检验不通过')

    def test_close_window_btn(self):
        '''关闭窗口按钮'''
        menu3 = '按钮控件_分享签章返回等'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        #lp.open_fisrt_doc()
        #time.sleep(0.5)
        mp = MainPage(self.driver)
        #mp.switch_to_div_iframe()
        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.close_window)
        self.driver.switch_to_default_content()
        text = mp.find_elem('div.navbar-tabs-panel>ul li>a>div').text
        #time.sleep(0.5)
        self.assertNotIn('按钮控件_分享签章返回等', text, msg='关闭窗口按钮检验不通过')

    def init(self):

#         self.test_save_btn_case()
#         self.test_save_return_btn_case()
#         self.test_save_draft_btn_case()
#         self.test_save_copy_btn_case()
#         self.test_save_new_btn_case()
#         self.test_jump_form_current_page_btn_case()
#         self.test_jump_url_tab_page_btn_case()
#         self.test_jump_url_new_window_btn_case()
#         self.test_jump_url_div_btn_case()
        self.test_user_defined_btn_case()
#         self.test_form_page_print_btn_case()
#         self.test_button_self_print_case()
#         self.test_share_btn_case()
#         self.test_signature_btn()
#         self.test_close_window_btn()


if __name__ == '__main__':
    unittest.main()