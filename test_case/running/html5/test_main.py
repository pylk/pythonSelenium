import os
import sys

sys.path.append('../../../../')
from test_case.models.driver import browser
import time
import unittest
from test_case.running.html5.app_test import AppTest
from test_case.page_obj.main_page import MainPage
from selenium.webdriver.common.keys import Keys


class MainTest(AppTest):
    '''主页测试 '''

    def setUp(self):
        mp = MainPage(self.driver)
        mp.refresh_main()

    def test_flowcenter_check(self):
        '''流程中心'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        self.assertIn('发起新建', mp.check_flowcenter(), msg='流程中心校验不通过')

    def test_new_build_open(self):
        '''打开发起新建'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开 发起新建
        mp.open_new_built()
        self.assertIn('内容', mp.get_new_built_return(), msg='发起新建打开校验不通过')

    def test_check_new_built(self):
        '''流程中心-发起新建-表单'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开发起新建
        mp.open_new_built()  # 点击发起新建按钮
        bool = mp.check_new_built()
        self.assertFalse(bool, msg='流程中心-发起新建_列表校验不通过')

    def test_check_new_built_icon(self):
        '''流程中心-发起新建-表单'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开发起新建
        mp.open_new_built()  # 点击发起新建按钮
        bool = mp.switch_new_built_icon()
        self.assertFalse(bool, msg='流程中心-发起新建-图标显示校验不通过')

    def test_new_built_search(self):
        '''流程中心-发起新建-搜索'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息中心消息
        mp.click_flowcenter()  # 点击打开流程中心
        mp.open_new_built()  # 点击流程新建
        self.assertTrue(mp.new_built_search(), msg='流程中心-发起新建-搜索校验不通过')

    def test_todo_list_open(self):
        '''打开我的代办'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 点击打开我的待办
        mp.open_todo_list()
        mp.switch_to_iframe()
        self.assertIn('主题', mp.get_todo_list_return(), msg='我的代办打开校验不通过')

    def test_todolist_num(self):
        '''我的待办数值显示'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开我的待办
        mp.open_todo_list()
        # time.sleep(0.5)
        mp.switch_to_iframe()
        # time.sleep(0.5)
        self.assertFalse(mp.check_todolist_number(), msg='我的待办数值校验不通过')

    def test_todolist_switch(self):
        '''我的待办切换待办'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开我的待办
        mp.open_todo_list()
        mp.switch_to_iframe()
        self.assertFalse(mp.switch_todo_list(), msg='我的待办切换校验不通过')

    def test_todolist_open_close(self):
        '''我的待办-打开关闭待办'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开我的待办
        mp.open_todo_list()
        mp.switch_to_iframe()
        self.assertTrue(mp.todolist_open_close(), msg='我的待办-打开关闭待办校验不通过')

    def test_todolist_search_by_user(self):
        '''我的待办-搜索_用户'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.close_righttop_message()  # 关闭消息提示
        mp.click_flowcenter()  # 点击流程中心
        mp.open_todo_list()  # 打开我的待办
        mp.switch_to_iframe()
        mp.select_user()  # 添加用户查询
        mp.switch_to_parent()
        mp.switch_to_iframe()
        mp.click_search()  # 点击查询按钮
        self.assertTrue(mp.is_noAvatar('李玲'), msg='我的待办-按主题搜索及按用户申请人搜索')

    def test_todolist_search_by_theme(self):
        '''我的待办-搜索_用户_主题'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.close_righttop_message()  # 关闭消息提示
        mp.click_flowcenter()  # 点击流程中心
        mp.open_todo_list()  # 打开我的待办
        mp.switch_to_iframe()
        self.assertTrue(mp.is_text_center_invisibility(), msg='我的待办-按主题搜索及按用户申请人搜索')
        # 在主题搜素框中输入“主题”搜索
        mp.find_elem('#flowtitle').send_keys('主题')
        # 用Enter键代替点击搜索
        mp.find_elem('#flowtitle').send_keys(Keys.ENTER)
        self.assertFalse(mp.is_text_center_invisibility(), msg='我的待办-按主题搜索及按用户申请人搜索')

    def test_handle_track_open(self):
        '''打开经办跟踪'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开经办跟踪
        mp.open_handle_track()
        mp.switch_to_iframe()
        self.assertIn('完结', mp.get_handle_track_return(), msg='经办跟踪打开校验不通过')

    def test_handle_track_num(self):
        '''经办跟踪数值显示'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开经办跟踪
        mp.open_handle_track()
        mp.switch_to_iframe()
        self.assertFalse(mp.check_handle_track_number(), msg='经办跟踪数值校验不通过')

    def test_handle_track_switch(self):
        '''经办跟踪切换待办'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开经办跟踪
        mp.open_handle_track()
        mp.switch_to_iframe()
        self.assertFalse(mp.switch_handle_track(), msg='经办跟踪切换校验不通过')

    def test_unfinished_handle_track(self):
        '''经办跟踪-未完结的'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开经办跟踪
        mp.open_handle_track()
        mp.switch_to_iframe()
        self.assertFalse(mp.unfinished_handle_track(), msg='经办跟踪-未完结的 校验不通过')

    def test_flip_handle_track(self):
        '''经办跟踪-我发起的'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开经办跟踪
        mp.open_handle_track()
        mp.switch_to_iframe()
        self.assertFalse(mp.flip_handle_track(), msg='经办跟踪-我发起的 校验不通过')

    def test_meter_analyse_open(self):
        '''打开仪表分析'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开仪表分析
        mp.open_meter_analyse()
        mp.switch_to_iframe()
        self.assertIn('软件', mp.get_meter_analyse_return(), msg='仪表分析打开校验不通过')

    def test_userbox_open(self):
        '''用户设置打开'''
        mp = MainPage(self.driver)
        # 悬停显示
        mp.over_userbox()
        self.assertIn('open', mp.get_userbox_return_class(), msg='用户设置校验不通过')

    def test_check_number_equal(self):
        '''头像数值与消息中心数值相等'''
        mp = MainPage(self.driver)
        mp.over_userbox()
        # time.sleep(0.3)
        self.assertTrue(mp.check_message_number(), msg='消息中心显示数目校验不通过')

    def test_message_center_open(self):
        '''消息中心打开'''
        mp = MainPage(self.driver)
        mp.over_userbox()
        # 打开消息中心
        mp.open_message_center()
        mp.switch_to_iframe()
        self.assertIn('企业动态', mp.get_message_center_return(), msg='消息中心校验不通过')

    def test_personal_setting_open(self):
        '''个人设置打开'''
        mp = MainPage(self.driver)
        mp.over_userbox()
        # 点击个人设置
        mp.open_user_setting()
        mp.switch_to_div_iframe()  # 切换到弹出层内部--在最外层打开弹出层
        self.assertEqual('基本信息', mp.get_user_setting_return(), msg='个人设置校验不通过')

    def test_logout_open(self):
        '''注销打开'''
        mp = MainPage(self.driver)
        mp.over_userbox()
        # 点击注销
        mp.open_logout()
        # time.sleep(0.5)
        self.assertIn('退出', mp.get_user_logout_return(), msg='注销校验不通过')

    def test_isEeterpriseAdmin(self):
        '''企业管理员配置'''
        # 李玲配置企业管理员
        mp = MainPage(self.driver)
        mp.over_userbox()
        self.assertIn('管理', mp.IsEnterpriseAdmin_return(), msg='企业域管理员配置不通过')

    def test_enterprise_admin_open(self):
        '''管理打开'''
        mp = MainPage(self.driver)
        mp.over_userbox()
        # 点击下拉菜单管理
        mp.open_enterprise_admin()
        mp.switch_to_iframe()
        self.assertIn('企业域信息管理', mp.get_EnterpriseAdmin_return(), msg='企业域管理员配置管理打开不通过')

    def test_switch_nav(self):
        '''切换多页签'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开经办跟踪
        mp.open_handle_track()
        # 打开我的待办
        mp.open_todo_list()
        # time.sleep(0.5)
        mp.switch_nav_1()
        mp.switch_to_iframe()
        msg1 = self.assertTrue(mp.get_switchnav_1_return(), msg='页签1不正常')
        mp.switch_to_parent()
        mp.switch_nav_2()
        mp.switch_to_iframe()
        msg2 = self.assertTrue(mp.get_switchnav_2_return(), msg='页签2不正常')
        if msg1 == '页签1不正常' and msg2 == '页签2不正常':
            print('切换多页签校验不通过')

    def test_nav_close_click(self):
        '''关闭多页签'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开我的待办
        mp.open_todo_list()
        # time.sleep(0.5)
        # 关闭页签
        mp.nav_close_click()
        self.assertTrue(mp.get_navclose_click_return(), msg='页签关闭校验不通过')

    def test_Is_nav_close_exist(self):
        '''鼠标悬浮多页签关闭出现'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开我的待办
        mp.open_todo_list()
        # 鼠标悬浮关闭是否出现
        mp.is_nav_close_exist()
        # time.sleep(0.5)
        self.assertTrue(mp.get_isnavclose_exist_return(), msg='鼠标悬浮页签关闭按钮校验不通过')

    def test_nav_preview_count(self):
        '''打开多页签数等于预览数目等于缩略图显示数'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        # 点击流程中心
        mp.click_flowcenter()
        # 打开发起新建
        mp.open_new_built()
        mp.switch_to_parent()
        # time.sleep(0.5)
        # 打开我的待办
        mp.open_todo_list()
        # time.sleep(0.5)
        # 打开多页签预览
        mp.open_preview()
        self.assertTrue(mp.get_nav_preview_return(), msg='预览数目校验不通过')

    def test_open_preview(self):
        '''打开预览'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开发起新建
        mp.open_new_built()
        mp.switch_to_parent()
        # 打开多页签预览
        mp.open_preview()
        self.assertTrue(mp.get_open_preview_return(), msg='预览打开校验不通过')

    def test_nav_closs_all(self):
        '''关闭全部窗口'''
        mp = MainPage(self.driver)
        # 点击流程中心
        mp.click_flowcenter()
        # 打开发起新建
        mp.open_new_built()
        # 打开多页签预览
        mp.open_preview()
        # time.sleep(0.5)
        # 点击关闭全部窗口
        mp.nav_closs_all()
        # time.sleep(0.5)
        self.assertIn('流程中心', mp.get_nav_clossall_return(), msg='预览关闭全部窗口校验不通过')

    def test_nav_preview_click(self):
        '''打开预览点击页面返回页面'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        # 点击流程中心
        mp.click_flowcenter()
        # 打开发起新建
        mp.open_new_built()
        mp.switch_to_parent()
        # 打开我的待办
        mp.open_todo_list()
        # 打开多页签预览
        mp.open_preview()
        # 点击一个预览缩略图
        mp.click_preview_page()
        mp.switch_to_iframe()
        self.assertIn('内容', mp.get_new_built_return(), msg='预览缩略图点击校验不通过')

    def test_nav_closs_one(self):
        '''关闭一个预览页面'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        mp.click_flowcenter()
        mp.open_new_built()
        # time.sleep(0.5)
        mp.open_preview()
        # time.sleep(0.5)
        mp.nav_closs_one()
        # time.sleep(0.5)
        self.assertIn('流程中心', mp.get_nav_clossall_return(), msg='预览关闭全部窗口校验不通过')

    def test_widget_summary(self):
        '''widget_摘要'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        mp.switch_to_iframe()
        time.sleep(0.1)  # 必须，等待摘要加载完
        mp.restore_configure()
        self.assertIn('摘要', mp.widget_summary(), msg='摘要校验不通过')

    def test_open_view_icon(self):
        '''打开widget_视图_icon'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        mp.switch_to_iframe()
        mp.widget_view_icon()
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertIn('文本一', mp.get_view_icon_return(), msg='打开widget_视图_icon校验不通过')

    def test_open_view(self):
        '''打开widget_视图'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        mp.switch_to_iframe()
        self.assertTrue(mp.widget_view(), msg='打开widget_视图校验不通过')

    def test_open_fastentry_font(self):
        '''打开widget_快速入口'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        mp.switch_to_iframe()
        mp.fast_entry_font()  # 打开widget_快速入口
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertIn('新闻', mp.get_fastentry_font_return(), msg='打开widget_快速入口校验不通过')

    def test_open_fastentry_img(self):
        '''打开widget_快速入口_icon'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        mp.switch_to_iframe()
        mp.fast_entry_img()
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertIn('新闻', mp.get_fastentry_font_return(), msg='打开widget_快速入口_icon校验不通过')

    def test_open_contect_icon(self):
        '''打开widget_链接内容_icon'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        mp.switch_to_iframe()
        mp.link_contect_icon()
        # time.sleep(0.5)
        mp.switch_to_parent()
        mp.switch_to_iframe()
        # time.sleep(0.5)
        self.assertIn('选择', mp.get_linkcotect_icon_return(), msg='打开widget_链接内容_icon校验不通过')

    def test_open_ageing_report(self):
        '''打开widget_时效报表'''
        mp = MainPage(self.driver)
        mp.switch_to_iframe()
        mp.ageing_report()
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertIn('模块', mp.get_ageing_report_return(), msg='打开widget_时效报表校验不通过')

    def test_open_img_report(self):
        '''打开widget_图形报表'''
        mp = MainPage(self.driver)
        mp.switch_to_iframe()
        mp.img_report()
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertTrue(mp.get_img_report_return(), msg='打开widget_图形报表校验不通过')

    def test_widget_calculate_script(self):
        '''widget_计算脚本'''
        mp = MainPage(self.driver)
        mp.switch_to_iframe()
        mp.widget_calculate_script()
        mp.switch_to_parent()
        mp.switch_to_iframe()
        self.assertIn('新闻', mp.get_fastentry_font_return(), msg='打开widget_计算脚本校验不通过')

    def test_open_homepage_setting(self):
        '''打开homepage设置'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息
        mp.switch_to_iframe()
        mp.click_homepage_setting()  # 点击打开收起主页设置
        self.assertFalse(mp.get_hpset_return(), msg='打开homepage设置校验不通过')
        mp.click_homepage_setting()  # 点击打开收起主页设置
        self.assertTrue(mp.get_hpset_return(), msg='隐藏homepage设置校验不通过')

    def test_hpicon_link_set(self):
        '''图标链接设置'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()
        mp.switch_to_iframe()
        mp.click_homepage_setting()
        self.assertFalse(mp.homepage_icon_link_set(), msg='图标链接设置校验不通过')

    def test_hpmodule_set(self):
        '''模块设置'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()
        mp.switch_to_iframe()
        mp.click_homepage_setting()
        self.assertFalse(mp.homepage_module_set(), msg='模块设置校验不通过')

    def test_hpset_operations(self):
        '''homppage设置操作按钮'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息提示
        mp.switch_to_iframe()  # 切换到homepage中
        mp.click_homepage_setting()  # 点击设置图标
        mp.click_reset_setting()  # 点击重置按钮
        time.sleep(0.5)  # 必须，界面会重绘

        mp.click_homepage_setting()  # 点击设置图标
        mp.click_the_text_icon('链接内容_icon')  # 点击图标-取消显示
        mp.click_save_setting()  # 点击保存设置
        time.sleep(0.1)  # 必须，界面会重绘
        self.assertFalse(mp.is_text_in_icons('链接内容_icon'), msg='homepage设置保存按钮校验不通过')

        mp.click_homepage_setting()  # 点击设置图标
        mp.click_reset_setting()  # 点击重置按钮
        time.sleep(0.1)  # 必须，界面会重绘
        self.assertTrue(mp.is_text_in_icons('链接内容_icon'), msg='homepage设置重置按钮校验不通过')

        mp.click_homepage_setting()  # 点击设置图标
        mp.click_the_text_icon('链接内容_icon')  # 点击图标-取消显示
        mp.click_cancel_setting()  # 点击取消按钮
        self.assertTrue(mp.is_text_in_icons('链接内容_icon'), msg='homepage设置重置按钮校验不通过')

    def test_hpset_layout(self):
        '''homepage布局设置'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()
        mp.switch_to_iframe()
        mp.restore_configure()
        mp.click_homepage_setting()  # 点击主页设置按钮
        self.assertTrue(mp.homepage_setting_layout(), msg='homepage设置布局设置校验不通过')

    def test_wgiscript_height(self):
        '''计算脚本高度的设置'''
        mp = MainPage(self.driver)
        mp.switch_to_iframe()
        self.assertTrue(mp.check_widget_iscript_hight(), msg='计算脚本高度校验不通过')

    def test_Is_widget_imgicon(self):
        '''widget图标类型：图片图标'''
        mp = MainPage(self.driver)
        mp.switch_to_iframe()
        self.assertTrue(mp.widget_linkcontect_imgicon('链接内容'), msg='链接内容-图片图标校验不通过')

    def test_widget_changecity_weather(self):
        '''天气预报更换城市'''
        mp = MainPage(self.driver)
        mp.close_righttop_message()  # 关闭消息
        mp.switch_to_iframe()
        mp.click_homepage_setting()  # 点击打开homepage设置
        self.assertTrue(mp.widget_weather_change_city(), msg='天气预报更换城市校验不通过')

    # 需重写
    # def test_widget_operation(self):
    #     '''widget的标题悬浮3个操作'''
    #     mp = MainPage(self.driver)
    #     mp.close_righttop_message() # 关闭消息
    #     mp.switch_to_iframe()
    #     mp.widget_view_icon() #打开视图图标
    #     mp.switch_to_parent()
    #     mp.switch_to_iframe() #切入对应iframe
    #     self.assertTrue(mp.widget_operation(), msg='widget 悬浮显示操作校验不通过')

    # def test_widget_close(self):
    #     '''widget的标题悬浮关闭操作'''
    #     mp = MainPage(self.driver)
    #     mp.switch_to_iframe()
    #     mp.over_widget_action('摘要')
    #     mp.find_elem_is_clickable('.action[style="display:block;"]>a[title="关闭"]',timeout=2).click()


    # def test_Is_menu_open(self):
    #     '''左侧菜单展开折叠'''
    #     mp = MainPage(self.driver)
    #     mp.Is_menu_open()
    #     self.assertTrue(mp.Is_menu_open(), msg='菜单打开校验不通过')

    def init(self):
        # self.test_userbox_open()
        #         self.test_check_number_equal()
        # self.test_message_center_open()
        # self.test_personal_setting_open()
        # self.test_logout_open()
        # self.test_isEeterpriseAdmin()
        # self.test_enterprise_admin_open()
        # self.test_flowcenter_check()
        # self.test_new_build_open()
        # self.test_check_new_built()
        self.test_new_built_search()
        #         self.test_todo_list_open()
        # self.test_todolist_num()
        #         self.test_todolist_switch()
        # self.test_todolist_open_close()
        # self.test_todolist_search()
        # self.test_handle_track_open()
        # self.test_handle_track_num()
        #         self.test_handle_track_switch()
        # self.test_unfinished_handle_track()
        # self.test_flip_handle_track()
        # self.test_meter_analyse_open()
        # self.test_switch_nav()
        # self.test_nav_close_click()
        # self.test_Is_nav_close_exist()
        # self.test_nav_preview_count()
        # self.test_open_preview()
        # self.test_nav_closs_all()
        # self.test_nav_preview_click()
        # self.test_nav_closs_one()
        #         self.test_widget_summary()
        # self.test_open_view_icon()
        # self.test_open_view()
        # self.test_open_fastentry_font()
        # self.test_open_fastentry_img()
        # self.test_open_ageing_report()
        # self.test_open_img_report()
        # self.test_open_view_icon()
        #         self.test_open_contect_icon()
        # self.test_widget_calculate_script()
        #         self.test_open_homepage_setting()
        #         self.test_hpicon_link_set()
        #         self.test_hpmodule_set()
        # self.test_wgiscript_height()
        # self.test_Is_widget_imgicon()
        #         self.test_widget_changecity_weather()
        #         self.test_widget_operation()
        #         self.test_hpset_operations()
        # self.test_hpset_layout()


if __name__ == '__main__':
    unittest.main()
