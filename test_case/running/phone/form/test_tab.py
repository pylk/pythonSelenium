import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.form.tab_page import TabPhonePage
from test_case.page_obj.form.input_page import InputPhonePage


class TabPhoneTest(ComponentPhoneTest):
    '''手机端选项卡测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = ""

    def open_menus(self, menu1, menu2, menu3):
        mp = MainPhonePage(self.driver)
        mp.open_menu(menu1)
        mp.open_menu(menu2)
        #time.sleep(0.5)
        mp.made_nav_hide()
        mp.open_menu(menu3)

    def test_tab_switch_case(self):
        '''选项卡切换'''
        # 判断切换后的字段是否可见
        menu3 = '选项卡_普通'
        self.open_menus(self.menu1, self.menu2, menu3)
        comp = TabPhonePage(self.driver)
        self.assertTrue(comp.is_lable_visit('选项卡_页签1_文本一'), msg='选项卡模板有问题')
        comp.switch_tabpage('页签')
        self.assertFalse(comp.is_lable_visit('选项卡_页签1_文本一'), msg='选项卡切换不生效')
        self.assertTrue(comp.is_lable_visit('选项卡_页签2_文本一'), msg='选项卡切换不生效')

    def test_tab_save_case(self):
        '''选项卡保存'''
        # 判断切换后的字段是否可见
        menu3 = '选项卡_普通'
        self.open_menus(self.menu1, self.menu2, menu3)
        comp = TabPhonePage(self.driver)
        comp.switch_tabpage('页签')
        textInput = InputPhonePage(self.driver,'选项卡_页签2_文本一')
        text1 = textInput.set_val_save_get_msg('选项卡保存测试')
        self.assertIn("保存成功", text1, msg='选项卡保存检验不通过')
        comp.switch_tabpage('页签')
        self.assertEqual('选项卡保存测试',textInput.get_inputtext_value(), msg='选项卡保存检验不通过')

    def test_tab_readonly_case(self):
        '''选项卡只读'''
        menu3 = '选项卡_只读条件'
        self.open_menus(self.menu1, self.menu2, menu3)
        comp = TabPhonePage(self.driver)
        textInput = InputPhonePage(self.driver, '选项卡_页签1_文本一')
        self.assertTrue(textInput.is_comp_readonly('选项卡_页签1_文本一'),msg='选项卡_只读条件不生效')
        comp.switch_tabpage('页签')
        textInput2 = InputPhonePage(self.driver, '选项卡_页签2_文本一')
        self.assertFalse(textInput.is_comp_readonly('选项卡_页签2_文本一'), msg='选项卡_只读条件不生效')

    def test_tab_hide_case(self):
        '''选项卡隐藏'''
        menu3 = '选项卡_隐藏条件'
        self.open_menus(self.menu1, self.menu2, menu3)
        comp = TabPhonePage(self.driver)
        self.assertFalse(comp.is_comp_hide('页签1'),msg=menu3+'不生效')
        self.assertTrue(comp.is_comp_hide('页签'),msg=menu3+'不生效')
        self.assertTrue(comp.is_comp_hide('页签3'),msg=menu3+'不生效')

    def test_tab_selected_case(self):
        '''选项卡默认选择'''
        # 判断切换后的字段是否可见
        menu3 = '选项卡_页签选中脚本'
        self.open_menus(self.menu1, self.menu2, menu3)
        comp = TabPhonePage(self.driver)
        self.assertTrue(comp.is_lable_visit('选项卡_页签1_文本一'), msg='选项卡默认选择不生效')

    def test_tab_parentview_case(self):
        '''视图记录_父子关系'''
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menus(self.menu1, self.menu2, menu3)
        comp = TabPhonePage(self.driver)
        comp.switch_tabpage('父子视图')
        self.assertTrue(comp.is_tab_viewname_visit('父子视图'),msg='选项卡_父子关系视图不生效')
        self.assertEqual('0',comp.get_tab_view_record_num('父子视图'),msg='选项卡_父子关系视图不生效')
        comp.setvalue('父子视图','网格视图_数字','父子视图记录')
        self.assertEqual('1', comp.get_tab_view_record_num('父子视图'), msg='选项卡_父子关系视图不生效')
        comp.del_val('父子视图')
        self.assertEqual('0', comp.get_tab_view_record_num('父子视图'), msg='选项卡_父子关系视图删除数据不生效')

    def test_tab_noparentview_case(self):
        '''视图记录_非父子关系'''
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menus(self.menu1, self.menu2, menu3)
        comp = TabPhonePage(self.driver)
        comp.switch_tabpage('非父子视图')
        comp.clera_value()#恢复包含元素数据
        self.assertTrue(comp.is_tab_viewname_visit('非父子视图'), msg='选项卡_非父子视图不生效')
        self.assertEqual('6', comp.get_tab_view_record_num('非父子视图'), msg='选项卡_父子关系视图不生效')
        comp.setvalue('非父子视图', '选项卡_字段2','非父子视图记录')
        self.assertEqual('7', comp.get_tab_view_record_num('非父子视图'), msg='选项卡_非父子视图不生效')
        comp.clera_value()
        self.assertEqual('6', comp.get_tab_view_record_num('非父子视图'), msg='选项卡_非父子视图删除数据不生效')

    def test_tab_reflesh_recalcalate_case(self):
        '''选项卡刷新重计算'''
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menus(self.menu1, self.menu2, menu3)
        comp = TabPhonePage(self.driver)
        self.assertTrue(comp.is_comp_hide('父子视图'),msg='选项卡刷新重计算不生效')
        self.assertTrue(comp.is_comp_hide('非父子视图'),msg='选项卡刷新重计算不生效')
        inputtext = InputPhonePage(self.driver,'重计算')
        inputtext.send_keys_trigger_refresh('隐藏')
        self.assertFalse(comp.is_comp_hide('非父子视图'),msg='选项卡刷新重计算不生效')
        self.assertFalse(comp.is_comp_hide('父子视图'),msg='选项卡刷新重计算不生效')

    def init(self):
        self.test_tab_switch_case()

if __name__ == '__main__':
    unittest.main()