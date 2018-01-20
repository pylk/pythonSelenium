import unittest
import sys
from test_case.running.phone.app_test import AppPhoneTest
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.login_page import LoginPage


class ComponentPhoneTest(AppPhoneTest):

#     def setUp(self):
#         print('-------%s' % self)

#         mp = MainPhonePage(self.driver)
#         mp.switch_to_menu_page()
#         mp.hide_elem_by_jq('section>i.iconfont.if-phone-plus') #隐藏悬浮的导航图标
#         mp.open_menus(self.menu1,self.menu2,self.menu3)
#         mp.show_elem_by_jq('section>i.iconfont.if-phone-plus') #显示悬浮的导航图标

    def setUp(self):
        mp = MainPhonePage(self.driver)
        mp.switch_to_menu_page()
        mp.hide_elem_by_jq('section>i.iconfont.if-phone-plus') #隐藏悬浮的导航图标
        mp.open_menus (self.menu1, self.menu2, self.menu3)
        mp.show_elem_by_jq('section>i.iconfont.if-phone-plus') #显示悬浮的导航图标

    def tearDown(self):
        mp = MainPhonePage(self.driver)
        if mp.is_loading_not_visible() == True:
            if mp.is_msg_not_visible() == True:
                mp.return_to_homepage()


