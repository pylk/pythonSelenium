import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.user_select_page import UserSelectPhonePage
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.main_page import MainPhonePage


class UserFieldPhoneTest(ComponentPhoneTest):
    '''用户选择框'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '用户选择框'  # 主页打开菜单时使用

    def test_type_case(self):
        '''类型'''
        name = '用户选择框_名称'
        comp = UserSelectPhonePage(self.driver, name)
        self.assertEqual('UserField', comp.get_attr('fieldtype'), msg=name + '检验不通过')

    def test_readonly_case(self):
        '''只读判断'''
        name = '用户选择框_显示只读'
        comp = UserSelectPhonePage(self.driver, name)
        bool = comp.is_comp_readonly(name)
        self.assertTrue(bool, msg=name + '检验不通过')

    def test_condition_readonly_case(self):
        '''用户选择框_条件只读'''
        name = '用户选择框_条件只读'
        comp = UserSelectPhonePage(self.driver,'')
        bool = comp.is_comp_readonly(name)
        self.assertTrue(bool, msg=name + '检验不通过')

    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
        name = '用户选择框_显示隐藏'
        comp = UserSelectPhonePage(self.driver, name)
        bool = comp.is_comp_hide(name)
        self.assertTrue(bool, msg=name + '检验不通过')

    def test_condition_hide_case(self):
        '''用户选择框_隐藏显示值'''
        compname2 = '用户选择框_隐藏显示值'
        comp = UserSelectPhonePage(self.driver,'')
        self.assertTrue(comp.is_comp_hide(compname2), msg=compname2 + '检验不通过')
        self.assertIn('控件已隐藏', comp.get_curpage_span(), msg=compname2 + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        name = '用户选择框_名称'
        comp = UserSelectPhonePage(self.driver, name)
        bool = comp.is_desription_effect(name)
        self.assertTrue(bool, msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验'''
        name = '用户选择框_非空校验'
        comp = UserSelectPhonePage(self.driver, name)
        btn = ButtonPhonePage(self.driver)
        btn.click_button('保存')
        #time.sleep(0.5)
        text1 = comp.get_msg()
        self.assertIn("'用户选择框_非空校验'必须填写！", text1, msg=name + '检验不通过')

    def test_refresh_recaculate_case(self):
        '''刷新重计算值脚本'''
        refresh_name = '用户选择框_刷新'
        comp1 = UserSelectPhonePage(self.driver, refresh_name)
        comp1.click_adduser_btn(refresh_name)
        comp1.add_user_by_name(['王聪','伟强'])
        comp1.wait_Tabloading_show_then_hide()
        recaculate_name = '用户选择框_重计算'
        comp2 = UserSelectPhonePage(self.driver, recaculate_name)
        self.assertEqual('王聪;伟强', comp2.get_select_users(recaculate_name), msg='刷新重计算值脚本检验不通过')

    def test_selected_radio_type_case(self):
        '''用户单选'''
        name = '用户选择框_单选'
        comp = UserSelectPhonePage(self.driver, name)
        comp.click_adduser_btn(name)
        comp.add_user_by_name(['王聪', '伟强'])
        self.assertEqual('伟强', comp.get_select_users(name),msg=name + '检验不通过')

    def test_selected_checkbox_type_case(self):
        '''用户多选'''
        name = '用户选择框_多选'
        comp = UserSelectPhonePage(self.driver, name)
        comp.click_adduser_btn(name)
        comp.add_user_by_name(['李玲','王聪', '伟强'])
        self.assertEqual('李玲;王聪;伟强', comp.get_select_users(name), msg=name + '检验不通过')

    def test_select_user_bydept_case(self):
        '''从部门中获取用户'''
        name = '用户选择框_名称'
        comp = UserSelectPhonePage(self.driver, name)
        comp.click_adduser_btn(name)
        comp.switch_dept_user_select_page()
        comp.add_user_by_name(['伟强'])
        self.assertIn('伟强',comp.get_select_users(name), msg='从部门中获取用户检验不通过')

    def test_select_user_byrole_case(self):
        '''从职务用户中获取用户'''
        name = '用户选择框_名称'
        comp = UserSelectPhonePage(self.driver, name)
        comp.click_adduser_btn(name)
        comp.switch_role_user_select_page('测试主管')
        #添加等待loading
        comp.wait_Tabloading_show_then_hide()
        comp.add_user_by_name(['伟强'])
        self.assertIn('伟强',comp.get_select_users(name), msg='从职务中获取用户检验不通过')

    def test_select_user_bysearch_case(self):
        '''从查询中获取用户'''
        name = '用户选择框_名称'
        comp = UserSelectPhonePage(self.driver,name)
        comp.set_val('李玲')
        self.assertIn('李玲',comp.get_select_users(name), msg='从通讯录中获取用户检验不通过')

    def test_cleanup_user_case(self):
        '''清除已选用户'''
        name = '用户选择框_名称'
        comp = UserSelectPhonePage(self.driver, name)
        comp.click_adduser_btn(name)
        comp.add_user(['伟强'])
        comp.click_clearall_btn() #点击清空
        self.assertIn('', comp.get_select_users(name), msg='清除已选用户检验不通过')

    def tearDown(self):
        mp = MainPhonePage(self.driver)
        if mp.find_elem('.icon.icon-left-nav.pull-left')!=None:
            mp.find_elem_is_clickable('.icon.icon-left-nav.pull-left').click()
            mp.wait_Tabloading_show_then_hide()
            mp.return_to_homepage()
        else:
            if mp.is_loading_not_visible() == True:
                if mp.is_msg_not_visible() == True:
                    mp.return_to_homepage()

    def init(self):
        '''类型、只读、隐藏属性测试'''
        # self.test_type_case()
        # self.test_readonly_case()
        # self.test_hide_case()
        # self.test_desription_case()
        # self.test_refresh_recaculate_case()
        # self.test_not_null_case()
        # self.test_selected_radio_type_case()
        # self.test_selected_checkbox_type_case()
        # self.test_select_user_bydept_case()
        self.test_select_user_byrole_case()
        # self.test_select_user_bysearch_case()
        # self.test_cleanup_user_case()
        # self.test_condition_hide_case()


if __name__ == '__main__':
    unittest.main()
