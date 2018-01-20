import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.tree_department_page import TreeDepartmentPhonePage
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.main_page import MainPhonePage


class TreeDepartmentPhoneTest(ComponentPhoneTest):
    '''树形部门选择框'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '树形部门选择框'  # 主页打开菜单时使用

    def test_type_case(self):
        '''类型'''
        name = '树形部门选择框_名称'
        comp = TreeDepartmentPhonePage(self.driver)
        self.assertEqual('TreeDepartmentField', comp.find_elem(comp.get_tree_elem(name)).get_attribute('fieldtype'), msg=name + '检验不通过')

    def test_show_readonly_case(self):
        '''树形部门选择框_显示只读'''
        compname = '树形部门选择框_显示只读'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname)
        bool = comp.is_comp_readonly(compname)
        self.assertTrue(bool, msg=compname + '检验不通过')

    def test_condition_readonly_case(self):
        '''树形部门选择框_只读条件'''
        compname2 = '树形部门选择框_只读条件'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname2)
        comp.scroll_to_target_element(target)
        bool = comp.is_comp_readonly(compname2)
        self.assertTrue(bool, msg=compname2 + '检验不通过')

    def test_show_hide_case(self):
        '''显示隐藏和条件隐藏'''
        compname = '树形部门选择框_显示隐藏'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname)
        self.assertTrue(comp.is_comp_hide(compname), msg=compname + '检验不通过')

    def test_condition_hide_case(self):
        '''树形部门选择框_隐藏时显示值'''
        compname2 = '树形部门选择框_隐藏时显示值'
        comp = TreeDepartmentPhonePage(self.driver)
        # target = comp.get_dept(compname2)
        self.assertTrue(comp.is_comp_hide(compname2), msg=compname2 + '检验不通过')
        self.assertIn('控件已隐藏', comp.get_curpage_span(), msg=compname2 + '检验不通过')

    # def test_show_when_hide_case(self):
    #     '''隐藏时显示值'''
    #     compname = '树形部门选择框_隐藏时显示值'
    #     comp = TreeDepartmentPhonePage(self.driver)
    #     target = comp.get_dept(compname)
    #     bool = comp.is_comp_hide(compname)
    #     self.assertTrue(bool,msg=compname + '检验不通过')
    #     self.assertIn('控件已隐藏', comp.get_curpage_span(), msg=compname + '检验不通过')

    def test_only_value_case(self):
        '''只读时仅显示值'''
        name = '树形部门选择框_只读时仅显示值'
        compname = '树形部门选择框_重计算'
        inputtext_name = '只读刷新'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname)
        comp.scroll_to_target_element(target)
        comp.select_depts(compname,['产品部','测试部'])
        self.assertTrue(comp.is_comp_readonly(compname), msg=name + '检验不通过')
        textInput = InputPhonePage(self.driver,inputtext_name)
        textInput.send_keys_trigger_refresh('只读')
        self.assertTrue(comp.is_comp_readonly(compname), msg=name + '检验不通过')
        self.assertEqual('产品部;测试部',comp.get_select_depts_readonly(compname), msg=name + '检验不通过')

    def test_refresh_case(self):
        '''刷新'''
        compname = '树形部门选择框_刷新'
        inputtext_name = '已选部门数'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname)
        comp.scroll_to_target_element(target)
        comp.select_depts(compname, ['产品部', '测试部'])
        textInput = InputPhonePage(self.driver, inputtext_name)
        self.assertEqual("已刷新", textInput.get_attr('value'), msg=compname + '检验不通过')


    def test_recaculate_case(self):
        '''重计算'''
        name = '树形部门选择框_只读时仅显示值'
        compname = '树形部门选择框_重计算'
        inputtext_name = '只读刷新'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname)
        comp.scroll_to_target_element(target)
        comp.select_depts(compname, ['产品部', '测试部'])
        self.assertTrue(comp.is_comp_readonly(compname), msg=name + '检验不通过')
        textInput = InputPhonePage(self.driver, inputtext_name)
        textInput.send_keys_trigger_refresh('只读')
        self.assertTrue(comp.is_comp_readonly(compname), msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        compname = '树形部门选择框_描述'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname)
        comp.scroll_to_target_element(target)
        bool = comp.is_desription_effect(compname)
        self.assertTrue(bool, msg=compname + '检验不通过')



    def test_not_null_case(self):
        '''非空校验'''
        name = '树形部门选择框_非空校验'
        comp = TreeDepartmentPhonePage(self.driver)
        btn = ButtonPhonePage(self.driver)
        btn.click_button('保存')
        #time.sleep(0.5)
        text1 = comp.get_msg()
        self.assertIn("树形部门选择框_非空校验'必须填写", text1, msg=name + '检验不通过')

    def test_clean_button(self):
        '''选择部门后清除数据'''
        compname = '树形部门选择框_点击清除'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname)
        comp.scroll_to_target_element(target)
        comp.select_depts(compname,['产品部','测试部'])
        self.assertEqual('产品部;测试部',comp.get_select_depts(compname),msg=compname + '检验不通过')
        comp.go_to_depts(compname)
        bt = ButtonPhonePage(self.driver)
        bt.click_iframe_button('清除')
        bt.click_iframe_button('保存')
        self.driver.switch_to.default_content()
        self.assertEqual('', comp.get_select_depts(compname), msg=compname + '检验不通过')


    def test_close_button(self):
        '''树形部门取消按钮'''
        compname = '树形部门选择框_点击退出'
        comp = TreeDepartmentPhonePage(self.driver)
        target = comp.get_dept(compname)
        comp.scroll_to_target_element(target)
        comp.select_depts(compname, ['产品部', '测试部'])
        self.assertEqual('产品部;测试部', comp.get_select_depts(compname), msg=compname + '检验不通过')
        comp.select_depts_no_save(compname, ['产品部'])
        bt = ButtonPhonePage(self.driver)
        bt.click_iframe_button('取消')
        self.driver.switch_to.default_content()
        self.assertEqual('产品部;测试部', comp.get_select_depts(compname), msg=compname + '检验不通过')

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
        # self.test_show_readonly_case()
        # self.test_condition_readonly_case()
        # self.test_show_hide_case()
#         self.test_condition_hide_case()
        # self.test_only_value_case()
        # self.test_refresh_case()
        self.test_recaculate_case()
        # self.test_desription_case()
        # self.test_not_null_case()
        # self.test_clean_button()
        # self.test_close_button()


if __name__ == '__main__':
    unittest.main()
