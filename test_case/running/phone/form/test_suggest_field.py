import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.suggest_page import SuggestPhonePage


class SuggestPhoneTest(ComponentPhoneTest):
    '''智能选择框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '智能提示框'  # 主页打开菜单时使用

    def test_type_case(self):
        '''类型'''
        
        name = '智能提示框_名称_show'
        comp = SuggestPhonePage(self.driver, name)
        self.assertEqual('text', comp.get_attr('type'), msg=name + '检验不通过')
        self.assertIn('form-control', comp.get_attr('class'), msg=name + '检验不通过')

    def test_readonly_case(self):
        '''显示只读和条件只读'''
        
        name = '智能提示框_只读'
        comp = SuggestPhonePage(self.driver, name)
        self.assertTrue(comp.span_is_displayed(), msg=name + '检验不通过')

        name = '智能提示框_只读条件_show'
        comp = SuggestPhonePage(self.driver, name)
        self.assertTrue(comp.readonly_test(), msg=name + '检验不通过')

    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
        
        name = '智能提示框_隐藏'
        comp = SuggestPhonePage(self.driver, name)
        self.assertEqual('hidden', comp.get_attr('type'), msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''

        name = '智能提示框_刷新'
        ipname = '智能提示框_刷新_show'
        comp = SuggestPhonePage(self.driver, name)
        comp.smart_set_value(ipname)
        comp.find_elem_is_clickable('.typeahead.dropdown-menu[role="listbox"]').click()
        comp.wait_elem_show_then_hide('#loadingToast')
        name = '智能提示框_重计算_show'
        comp = SuggestPhonePage(self.driver, name)
        self.assertEqual('智能提示框2', comp.get_attr('text'), msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        
        name = '智能提示框_描述'
        comp = SuggestPhonePage(self.driver, name)
        self.assertTrue(comp.is_desription_effect(name), msg=name + '检验不通过')

    def test_value_case(self):
        '''值脚本'''
        
        name = '智能提示框_搜索方式动态'
        ipname = '智能提示框_搜索方式动态_show'
        comp = SuggestPhonePage(self.driver, name)
        comp.smart_set_value(ipname)
        self.assertTrue(comp.is_exist_typeahead(), msg="输入之后，智能提示框没有提示")
        self.assertTrue(comp.get_value_case_return(ipname), msg=name + '检验不通过')

    def test_select_iscript(self):
        '''选项脚本'''
        
        name = '智能提示_选项脚本'
        ipname = '智能提示_选项脚本_show'
        comp = SuggestPhonePage(self.driver, name)
        comp.smart_set_value(ipname)
        self.assertTrue(comp.is_exist_typeahead(), msg="输入之后，智能提示框没有提示")
        self.assertTrue(comp.get_value_case_return(ipname), msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验'''
        
        name = '智能提示框_非空校验_show'
        comp = SuggestPhonePage(self.driver, name)
        self.assertIn("'智能提示框_非空校验'必须填写", comp.set_val_save_get_msg(''), msg=name + '检验不通过')

#     def test_show_when_hide_case(self):
#         '''隐藏时显示值'''
#         
#         name = '智能提示框_隐藏时显示值'
#         comp = SuggestPhonePage(self.driver, name)
#         self.assertEqual('hidden', comp.get_attr('type'), msg=name + '检验不通过')
#         self.assertEqual("控件已隐藏", comp.get_text_by_css_selector('input[name="' + name + '"] + span'),
#                          msg=name + '检验不通过')

    def init(self):
        '''智能提示框测试'''
        
#         self.test_type_case()
#         self.test_readonly_case()
#         self.test_hide_case()
        self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_value_case()
#         self.test_select_iscript()
#         self.test_not_null_case()
#         self.test_show_when_hide_case()


if __name__ == '__main__':
    unittest.main()
