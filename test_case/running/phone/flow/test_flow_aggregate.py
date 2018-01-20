import os, sys

sys.path.append('../../../../')
import unittest
import time
from test_case.running.phone.flow.flow_test import FlowPhoneTest
from test_case.page_obj.login_page import LoginPage
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.flow.flow_page import FlowPhonePage
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage
from test_case.page_obj.form.user_select_page import UserSelectPhonePage


class FlowAggregatePhoneTest(FlowPhoneTest):
    """流程测试集合"""
    menu1 = '流程'
    menu2 = ""
    menu3 = ""

    def open_menus(self, menu1, menu2, menu3):
        mp = MainPhonePage(self.driver)
        mp.open_menu(menu1)
        mp.open_menu(menu2)
        #time.sleep(0.5)
        mp.open_menu(menu3)

    def test_adjustment_process_case(self):
        """前台手动调整流程"""

        menu2 = '基本信息'
        menu3 = '前台手动调整流程'
        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        lp.clear_all_data()  # 清空所有数据
        bt = ButtonPhonePage(self.driver)
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason('前台手动调整流程')  # 录入请假原因
        bt.click_button('保存')  # 点击保存并启动流程按钮
        fp.wait_msg_show_then_hide()
        bool = bt.is_button_exist('流程调整')
        self.assertFalse(bool, msg="前台手动调整流程测试不通过")

    def test_editApprover_case(self):
        """允许编辑当前节点的审批人"""

        menu2 = '基本信息'
        menu3 = '允许编辑当前节点的审批人'
        title = '允许编辑当前节点的审批人'
        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')
        fp.flow_sumit()  # 提交流程

        po = LoginPage(self.driver)
        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('编辑流程审批人')  # 查看有没有编辑流程审批人按钮
        self.assertTrue(bool, msg="编辑流程审批人测试不通过")

        bt.click_button('编辑流程审批人')
        mp.select_user_by_name_for_form('伟强')

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool2 = bt.is_button_exist('编辑流程审批人')  # 查看有没有编辑流程审批人按钮
        self.assertTrue(bool2, msg="编辑流程审批人测试不通过")

        bt.click_button('提交')
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertTrue(fp.is_flow_end(), msg='编辑流程审批人测试不通过')

    def test_termination_case(self):
        """允许审批人终止流程"""

        menu2 = '基本信息'  # 主页打开菜单时使用
        menu3 = '允许审批人终止流程'
        title = '允许审批人终止流程'
        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')
        fp.flow_sumit()  # 提交流程

        po = LoginPage(self.driver)
        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('终止流程')  # 查看有没有编辑流程审批人按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('终止流程')  # 点击终止流程按钮
        fp.sendkey_in_confirmPanel_textarea('终止流程')
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('终止', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是终止

    def test_approver_organization_case(self):
        '''流程审批人for组织形式'''

        menu2 = '审批人设置'  # 主页打开菜单时使用
        menu3 = ''
        title = '流程审批人for组织形式'
        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver,'通过角色指定')

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.click_flow_submit_user_avatar()  # 点击选择流程审批人
        us.select_user_by_name('伟强')
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('通过角色指定', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是通过角色指定

    def test_approver_role_case(self):
        '''流程审批人for角色形式'''

        menu2 = '审批人设置'  # 主页打开菜单时使用
        menu3 = ''
        title = '流程审批人for角色形式'
        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver,'通过角色指定')
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.click_flow_submit_user_avatar()  # 点击选择流程审批人
        us.select_user_by_name('伟强')
        fp.flow_sumit()  # 提交流程

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('通过iscript指定', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是通过iscript指定

    def test_approver_iscript_case(self):
        '''流程审批人for_iscript形式'''
        menu2 = '审批人设置'  # 主页打开菜单时使用
        menu3 = ''
        title = '流程审批人for_iscript形式'
        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver,'通过角色指定')
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.click_flow_submit_user_avatar()  # 点击选择流程审批人
        us.select_user_by_name('伟强')
        fp.flow_sumit()  # 提交流程

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_timeout_submit_case(self):
        """超时自动提交"""

        menu2 = '审批时限设置'  # 主页打开菜单时使用
        menu3 = '审批超时自动提交'

        title = '审批超时自动提交'
        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('审批人', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是审批人
        po.user_login('liling', '123456')  # 切换李玲登陆
        time.sleep(60)

        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_allApprover_adopt_chaos_case(self):
        """所有审批人任意顺序"""

        menu2 = '流程节点通过条件'  # 主页打开菜单时使用
        menu3 = '所有审批人任意顺序'
        title = "所有审批人任意顺序"

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('wangcong', '123456')  # 切换王聪登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_allApprover_adopt_order_case(self):
        '''所有审批人按顺序'''

        menu2 = '流程节点通过条件'  # 主页打开菜单时使用
        menu3 = '所有审批人按顺序'
        title = "所有审批人按顺序"

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertFalse(bool, msg=title + "测试不通过")

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertFalse(bool, msg=title + "测试不通过")

        po.user_login('wangcong', '123456')  # 切换王聪登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertNotIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertFalse(bool, msg=title + "测试不通过")

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertNotIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_arbitrarily_adopt_case(self):
        '''任意审批人通过则节点通过'''

        menu2 = '流程节点通过条件'  # 主页打开菜单时使用
        menu3 = '任意审批人通过则节点通过'
        title = "任意审批人通过则节点通过"

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        po.user_login('wangcong', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertFalse(bool, msg=title + "测试不通过")

    def test_cc_for_iscript_case(self):
        '''流程抄送通过iscript'''

        menu2 = '抄送设置'  # 主页打开菜单时使用
        menu3 = '流程抄送通过iscript'
        title = "流程抄送通过iscript"

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver,'copyto_user_select')
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮

        self.assertTrue(fp.is_flow_copyTo_exsit(), msg=title + '测试不通过')

        fp.click_flow_copyTo()  # 点击选择抄送人
        us.select_user_by_name('张强')
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_ccForRole_case(self):
        '''流程抄送通过角色'''

        menu2 = '抄送设置'  # 主页打开菜单时使用
        menu3 = '流程抄送'
        title = "流程抄送通过角色"

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver,'copyto_user_select')
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.click_flow_copyTo()  # 点击选择抄送人

        self.assertTrue(fp.is_flow_copyTo_exsit(), msg=title + '测试不通过')
        us.select_user_by_name('伟强')
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_default_check_case(self):
        """并行默认选中"""

        menu2 = '流程并行'  # 主页打开菜单时使用
        menu3 = '并行默认选中'
        title = '并行默认选中'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮

        self.assertNotIn(False, fp.get_nodes_checked_stable(), msg=title + '测试不通过')

        fp.find_elem(
            '#flow-submit__node-box > div:nth-child(4) > label > div.weui-cell__hd > i').click()  # 点击 第一个流程节点状态使他成为未选中
        self.assertFalse(fp.get_nodes_checked_stable()[0], msg=title + '测试不通过')

        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

    def test_default_lockandcheck_case(self):
        """并行默认选中并锁定"""

        menu2 = '流程并行'  # 主页打开菜单时使用
        menu3 = '并行默认选中并锁定'
        title = '并行默认选中并锁定'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮

        self.assertNotIn(False, fp.get_nodes_checked_stable(), msg=title + '测试不通过')

        fp.find_elem(
            '#flow-submit__node-box > div:nth-child(4) > label > div.weui-cell__hd > i').click()  # 点击 第一个流程节点状态使他成为未选中
        self.assertNotIn(False, fp.get_nodes_checked_stable(), msg=title + '测试不通过')

        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def default_notcheck_case(self):
        """并行默认不选中"""

        menu2 = '流程并行'  # 主页打开菜单时使用
        menu3 = '并行默认不选中'
        title = '并行默认不选中'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮

        self.assertNotIn(True, fp.get_nodes_checked_stable(), msg=title + '测试不通过')

        fp.flow_sumit()  # 提交流程
        self.assertIn('请选择一项操作', fp.is_alert_exist(), msg=title + '测试不通过')

        fp.accept_alert()  # 接受alert
        fp.find_elem(
            '#flow-submit__node-box > div:nth-child(4) > label > div.weui-cell__hd > i').click()  # 点击 第一个流程节点状态使他成为选中

        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertNotIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_Fallback_case(self):
        '''流程回退'''

        menu2 = '流程通知'  # 主页打开菜单时使用
        menu3 = '流程回退'
        title = '流程回退'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('回退')  # 查看有没有提交按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('回退')
        bt.click_flowpanel_button('回退')
        lp.open_fisrt_doc()  # 打开记录
        self.assertEqual('李玲', fp.get_curnode_user(), msg=title + '测试不通过')
        bool = bt.is_button_exist('回退')  # 查看有没有提交按钮
        self.assertFalse(bool, msg=title + "测试不通过")
        boo2 = bt.is_button_exist('提交')  # 查看有没有提交按钮
        self.assertFalse(boo2, msg=title + "测试不通过")

    def test_Hang_case(self):
        '''流程挂起'''

        menu2 = '流程通知'  # 主页打开菜单时使用
        menu3 = '流程挂起'
        title = '流程挂起'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录
        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bool = bt.is_button_exist('挂起')  # 查看有没有挂起按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('挂起')
        bool2 = bt.is_button_exist('恢复')  # 查看有没有恢复按钮
        self.assertTrue(bool2, msg=title + "测试不通过")

        bt.click_button('恢复')
        bool = bt.is_button_exist('挂起')  # 查看有没有挂起按钮
        self.assertTrue(bool, msg=title + "测试不通过")

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_non_polymerization_case(self):
        '''流程非聚合'''

        menu2 = '审批送出设置'  # 主页打开菜单时使用
        menu3 = '流程非聚合'
        title = '流程非聚合'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录

        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('经理', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        self.assertNotIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('经理', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zjl01', '123456')  # 切换经理登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        self.assertTrue(bt.is_button_exist('提交'), msg=title + '测试不通过')

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_polymerization_case(self):
        '''流程聚合'''

        menu2 = '审批送出设置'  # 主页打开菜单时使用
        menu3 = '流程聚合'
        title = "流程聚合"

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录

        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('经理', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        self.assertNotIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('经理', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zjl01', '123456')  # 切换经理登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        self.assertFalse(bt.is_button_exist('提交'), msg=title + '测试不通过')

        po.user_login('weiqiang', '123456')  # 切换伟强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        self.assertNotIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('王聪', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertNotIn('伟强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertIn('经理', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('zjl01', '123456')  # 切换经理登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_Reminders_case(self):
        '''流程催办'''
        menu2 = '流程通知'  # 主页打开菜单时使用
        menu3 = '流程催办'
        title = "流程催办"

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录

        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertTrue(bt.is_button_exist('催办'), msg=title + '测试不通过')

        bt.click_button('催办')
        self.assertEqual('催办', fp.get_flowReminder_title(), msg=title + '测试不通过')

        fp.sendkey_for_flowReminder(title)

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_retreat_case(self):
        '''流程回撤'''

        menu2 = '流程通知'  # 主页打开菜单时使用
        menu3 = '流程回撤'
        title = "流程回撤"

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        lp.open_fisrt_doc()  # 打开记录

        self.assertIn('张强', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertTrue(bt.is_button_exist('回撤'), msg=title + '测试不通过')

        bt.click_button('回撤')
        self.assertIn('李玲', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertFalse(bt.is_button_exist('回撤'), msg=title + '测试不通过')
        self.assertTrue(bt.is_button_exist('提交'), msg=title + '测试不通过')

        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        po.user_login('zhangqiang', '123456')  # 切换张强登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程

        lp.open_fisrt_doc()  # 打开记录

        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_skipprocess_case(self):
        """流程节点跳过"""

        menu2 = '审批送出设置'  # 主页打开菜单时使用
        menu3 = '流程节点跳过'
        title = '流程节点跳过'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.flow_sumit()  # 提交流程
        time.sleep(10)
        lp.open_fisrt_doc()  # 打开记录
        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('归档', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def test_freeflow_submit_case(self):
        '''自由流程提交'''
        menu2 = '自由流程'  # 主页打开菜单时使用
        menu3 = ''
        title = '自由流程提交'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver,'free_flow')
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.click_flow_submit_user_avatar()  # 点击选择流程审批人
        us.select_user_by_name('王聪')
        bt.click_flowpanel_button('取消')  # 点击取消按钮
        self.assertTrue(bt.is_button_exist('提交'), msg=title + '测试不通过')
        bt.click_button('提交')  # 点击提交按钮

        fp.click_flow_submit_user_avatar()  # 点击选择流程审批人
        us.select_user_by_name('王聪')
        bt.click_flowpanel_button('发起')  # 提交流程
        lp.open_fisrt_doc()  # 打开记录

        self.assertEqual('王聪', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('wangcong', '123456')  # 切换王聪登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录

        self.assertTrue(bt.is_button_exist('提交'), msg=title + '测试不通过')
        self.assertTrue(bt.is_button_exist('回退'), msg=title + '测试不通过')
        self.assertTrue(bt.is_button_exist('结束流程'), msg=title + '测试不通过')

    def test_freeflow_backoff_case(self):
        '''自由流程回退'''
        menu2 = '自由流程'  # 主页打开菜单时使用
        menu3 = ''
        title = '自由流程回退'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver,'free_flow')
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.click_flow_submit_user_avatar()  # 点击选择流程审批人
        us.select_user_by_name('王聪')
        bt.click_flowpanel_button('发起')  # 提交流程
        lp.open_fisrt_doc()  # 打开记录

        self.assertEqual('王聪', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('wangcong', '123456')  # 切换王聪登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bt.click_button('回退')  # 点击提交按钮
        fp.click_flow_submit_user_avatar()  # 点击选择流程审批人

        self.assertIn('李玲', us.get_all_noAvatar_name(), msg=title + '测试不通过')
        self.assertNotIn('王聪', us.get_all_noAvatar_name(), msg=title + '测试不通过')
        us.select_user_by_name('李玲')
        bt.click_flowpanel_button('回退')
        lp.open_fisrt_doc()  # 打开记录

        self.assertEqual('李玲', fp.get_curnode_user(), msg=title + '测试不通过')
        self.assertFalse(bt.is_button_exist('提交'), msg=title + '测试不通过')
        self.assertFalse(bt.is_button_exist('回退'), msg=title + '测试不通过')
        self.assertFalse(bt.is_button_exist('结束流程'), msg=title + '测试不通过')

        po.user_login('liling', '123456')  # 切换李玲登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        self.assertTrue(bt.is_button_exist('提交'), msg=title + '测试不通过')
        self.assertTrue(bt.is_button_exist('回退'), msg=title + '测试不通过')
        self.assertTrue(bt.is_button_exist('结束流程'), msg=title + '测试不通过')

    def test_freeflow_complete(self):
        '''自由流程结束流程'''
        menu2 = '自由流程'  # 主页打开菜单时使用
        menu3 = ''
        title = '自由流程结束流程'

        self.open_menus(self.menu1, menu2, menu3)

        fp = FlowPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        mp = MainPhonePage(self.driver)
        bt = ButtonPhonePage(self.driver)
        us = UserSelectPhonePage(self.driver,'free_flow')
        po = LoginPage(self.driver)

        lp.clear_all_data()  # 清空所有数据
        bt.click_button('新建')  # 点击新建按钮
        fp.input_reason(title)  # 录入请假原因
        bt.click_button('提交')  # 点击提交按钮
        fp.click_flow_submit_user_avatar()  # 点击选择流程审批人
        us.select_user_by_name('王聪')
        bt.click_flowpanel_button('发起')  # 提交流程
        lp.open_fisrt_doc()  # 打开记录

        self.assertEqual('王聪', fp.get_curnode_user(), msg=title + '测试不通过')

        po.user_login('wangcong', '123456')  # 切换王聪登陆
        mp.switch_to_menu_page()
        self.open_menus(self.menu1, menu2, menu3)  # 打开相应的菜单
        lp.open_fisrt_doc()  # 打开记录
        bt.click_button('结束流程')  # 点击提交按钮
        bt.click_flowpanel_button('结束')
        lp.open_fisrt_doc()  # 打开记录

        fp.click_flow_more()  # 点击流程栏更多
        self.assertEqual('完成', fp.get_cur_flow_state(), msg=title + '测试不通过')  # 检查当前流程状态是不是归档

    def init(self):
        ''''''
        # self.test_skipprocess_case()
        # self.test_adjustment_process_case()
        # self.test_editApprover_case()
#         self.test_termination_case()
        # self.test_approver_organization_case()
        # self.test_approver_role_case()
        # self.test_approver_iscript_case()
        self.test_timeout_submit_case()
        # self.test_allApprover_adopt_chaos_case()
        # self.test_allApprover_adopt_order_case()
        # self.test_arbitrarily_adopt_case()
#         self.test_cc_for_iscript_case()
        # self.test_ccForRole_case()
#         self.test_default_check_case()
#         self.test_default_lockandcheck_case()
        # self.default_notcheck_case()
#         self.test_Fallback_case()
        # self.test_Hang_case()
        # self.test_non_polymerization_case()
        # self.test_polymerization_case()
        # self.test_Reminders_case()
        # self.test_retreat_case()
        # self.test_freeflow_submit_case()
        # self.test_freeflow_backoff_case()
        # self.test_freeflow_complete()


if __name__ == '__main__':
    unittest.main()






























