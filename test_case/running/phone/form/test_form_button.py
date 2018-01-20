import sys
import unittest

sys.path.append('../../../../')
from test_case.running.phone.button_test import ButtonPhoneTest
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage
from test_case.page_obj.form.input_page import InputPhonePage


class FormButtonPhoneTest(ButtonPhoneTest):
    '''手机端表单按钮测试'''
    
    menu1 = '表单'
    menu2 = '表单按钮'

    def test_flow_process_btn(self):
        '''流程处理按钮'''
        
        menu3 = '表单按钮_流程相关'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        
        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() != 0:
            lp.clear_all_data() #清除数据

        bt = ButtonPhonePage(self.driver)
        bt.click_button('新建')   #点击新建按钮
        lp.wait_Tabloading_show_then_hide()
        ip = InputPhonePage(self.driver, '单行文本')
        ip.element.send_keys('保存')  #输入文本
        bt.click_button('流程处理') #点击按钮
        bt.click_button('提交')   #点击按钮

        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[提交成功]', msgtitle, msg= '流程处理按钮检验不通过')

    def test_save_start_btn(self):
        '''保存并启动流程按钮'''
        
        menu3 = '表单按钮_流程相关'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)

        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() != 0:
            lp.clear_all_data() #清除数据

        bt = ButtonPhonePage(self.driver)
        bt.click_button('新建')   #点击新建
        lp.wait_Tabloading_show_then_hide()
        ip = InputPhonePage(self.driver, '单行文本')
        ip.element.send_keys('保存')  #输入文本
        bt.click_button('保存并启动流程')  #点击按钮

        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[保存成功]', msgtitle, msg='保存并启动按钮检验不通过')

    def test_save_copy_btn(self):
        '''保存并复制按钮'''
        
        menu3 = '表单按钮_保存并复制'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)

        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() != 0:
            lp.clear_all_data() #清除数据

        bt = ButtonPhonePage(self.driver)
        bt.click_button('新建')   #点击按钮
        lp.wait_Tabloading_show_then_hide()
        ip = InputPhonePage(self.driver, '单行文本')
        ip.element.send_keys('保存')  #输入文本
        bt.click_button('保存并复制')    #点击按钮
        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[保存成功]', msgtitle, msg='保存并复制按钮检验不通过')

        lp.wait_msg_show_then_hide()
        bt.click_button('返回')   #点击按钮
        self.assertEqual(2, lp.get_rows_total(), msg= '保存并复制按钮检验不通过')

    def test_save_btn(self):
        '''保存按钮'''
        
        menu3 = '表单按钮_保存类'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)

        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() != 0:
            lp.clear_all_data() #清除数据
                
        bt = ButtonPhonePage(self.driver)
        bt.click_button('新建')   #点击按钮

        lp.wait_Tabloading_show_then_hide()
        ip = InputPhonePage(self.driver, '单行文本')
        ip.element.send_keys('保存')  #输入文本
        bt.click_button('保存')   #点击按钮
        msgtitle = lp.get_msg()     #获取消息
        self.assertEqual('[保存成功]', msgtitle, msg= '保存按钮检验不通过')

    def test_save_return_btn(self):
        '''保存并返回按钮'''
        
        menu3 = '表单按钮_保存类'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc() #打开第一条数据
        bt = ButtonPhonePage(self.driver)
        bt.click_button('保存并返回')    #点击按钮
        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[保存成功]', msgtitle, msg='保存并返回按钮检验不通过')
        self.assertEqual('保存', lp.get_column_row1_col2(), msg= '保存并返回按钮检验不通过')

    def test_save_draft_btn(self):
        '''保存草稿按钮'''
        
        menu3 = '表单按钮_保存类'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc() #打开第一条数据
        bt = ButtonPhonePage(self.driver)
        bt.click_button('保存草稿') #点击按钮

        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[保存成功]', msgtitle, msg='保存草稿按钮检验不通过')

    def test_user_defined_not_btn(self):
        '''自定义无按钮'''
        
        menu3 = '表单按钮_自定义按钮'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc() #打开第一条数据
        bt = ButtonPhonePage(self.driver)
        bt.click_button('自定义无') #点击按钮

        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[自定义无成功]', msgtitle, msg='自定义无按钮检验不通过')

    def test_user_defined_return_btn(self):
        '''自定义返回按钮'''
        
        menu3 = '表单按钮_自定义按钮'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc() #打开第一条数据
        bt = ButtonPhonePage(self.driver)
        bt.click_button('自定义返回')    #点击按钮

        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[自定义返回成功]', msgtitle, msg='自定义返回按钮检验不通过')

    def test_user_defined_close_btn(self):
        '''自定义关闭按钮'''
        
        menu3 = '表单按钮_自定义按钮'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc() #打开第一条数据
        bt = ButtonPhonePage(self.driver)
        bt.click_button('自定义关闭')    #点击按钮

        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[自定义关闭成功]', msgtitle, msg='自定义关闭按钮检验不通过')

    def test_user_defined_jump_btn(self):
        '''自定义跳转按钮'''
        
        menu3 = '表单按钮_自定义按钮'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        lp.open_fisrt_doc() #打开第一条数据
        bt = ButtonPhonePage(self.driver)
        bt.click_button('自定义跳转列表')  #点击按钮
        msgtitle = lp.get_msg() #获取消息
        self.assertEqual('[自定义跳转列表成功]', msgtitle, msg='自定义跳转按钮检验不通过')
        self.assertEqual('保存',lp.get_column_row1_col2(),msg='自定义跳转按钮检验不通过')

    def init(self):
        self.test_flow_process_btn()
        # self.test_save_start_btn()
        # self.test_save_copy_btn()
        # self.test_save_btn()
        # self.test_save_return_btn()
        # self.test_save_draft_btn()
#         self.test_user_defined_not_btn()
        # self.test_user_defined_return_btn()
        # self.test_user_defined_jump_btn()
        # self.test_user_defined_close_btn()


if __name__ == '__main__':
    unittest.main()