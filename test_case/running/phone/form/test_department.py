import sys
import unittest
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.department_page import DepartmentPhonePage
from test_case.page_obj.form.department_page import DepartmentPage


class DepartmentPhoneTest(ComponentPhoneTest):
    '''手机端部门选择框'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '部门选择框'  #主页打开菜单时使用
    

    def test_type_case(self):
        '''类型'''
        name = '部门选择框_名称'
        dp = DepartmentPhonePage(self.driver, name)
        self.assertEqual('select', dp.get_tag_name(), msg=name + '检验不通过')

    def test_readonly_case(self):
        '''只读判断'''
        name = '部门选择框_显示只读'
        dp = DepartmentPhonePage(self.driver, name)
        self.assertTrue(dp.readonly_test(), msg=name + '检验不通过')
        self.assertFalse(dp.is_department_clickable(name), msg=name + '检验不通过')

        name = '部门选择框_条件只读'
        dp = DepartmentPhonePage(self.driver, name)
        self.assertTrue(dp.readonly_test(), msg=name + '检验不通过')
        self.assertFalse(dp.is_department_clickable(name), msg=name + '检验不通过')
    
    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
        name = '部门选择框_显示隐藏'
        dp = DepartmentPhonePage(self.driver, name)
        dname = self.driver.find_element_by_name(name)
        self.assertFalse(dname.is_displayed(), msg=name + '检验不通过')

        name = '部门选择框_隐藏显示值'
        dp = DepartmentPhonePage(self.driver, name)
        dname = self.driver.find_element_by_name(name)
        self.assertFalse(dname.is_displayed(), msg=name + '检验不通过')
                  
    def test_refresh_case(self):
        '''刷新  重计算'''
        '''刷新字段=重计算字段的值'''
        name = '部门选择框_刷新'
        dp = DepartmentPhonePage(self.driver, name)
        dp.wait_Tabloading_show_then_hide()
        # 先定位到下拉菜单
        dp.find_element('select[name="' + name + '"]').click()
        # 再对下拉菜单中的选项进行选择
        dp.find_element('select[name="' + name + '"]> option:nth-child(2)').click()
        dp.wait_Tabloading_show_then_hide()
        # 判断对应的元素有没有被选中
        bool = dp.find_element('select[name="部门选择框_重计算"]> option:nth-child(2)').is_selected()
        self.assertTrue(bool, msg="部门选择框刷新重计算检验不通过")

    def test_desription_case(self):
        '''描述'''
        name = '部门选择框_描述'
        dp = DepartmentPhonePage(self.driver, name)
        self.assertTrue(dp.is_desription_effect(name), msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验和第一选项为空值'''
        name = '部门选择框_非空校验'
        dp = DepartmentPhonePage(self.driver, name)
        self.assertIn("'部门选择框_非空校验'必须填写", dp.notnull_test(), msg=name + '检验不通过')
       
    def test_level_liandong_case(self):
        '''可选一级部门和下级部门联动'''
        name = '部门选择框_可选一级'
        dp = DepartmentPage(self.driver, name)
        dp.wait_Tabloading_show_then_hide()
        #获取可选值的数据量为1  
        self.assertEqual(1, len(dp.get_department_list()), msg=name + '检验不通过')
        #验证联动，可选部门数量为2
        name2 = '部门选择框_上级联动'
        dp2 = DepartmentPage(self.driver, name2)
        self.assertEqual(2, len(dp2.get_department_list()), msg=name2 + '检验不通过')
          
    def test_my_department_case(self):
          '''﻿显示当前用户所属部门及下属部门'''
          name='部门选择框_当前下级部门'
          dp = DepartmentPage(self.driver, name)
          dp.wait_Tabloading_show_then_hide()
          #获取可选值的数据量为2 
          self.assertEqual(2, len(dp.get_department_list()), msg=name + '检验不通过')
          mydept = dp.get_department_list_name()
          self.assertEqual('下属部门;自动化测试组;', mydept, msg=name + '检验不通过')
           
    def test_selected_firt_dept_case(self):
          '''﻿默认值第一个部门'''
          name='部门选择框_默认值第一个'
          dp = DepartmentPage(self.driver, name)
          dp.wait_Tabloading_show_then_hide()
          mydept = dp.get_selected_depart_name()
          print("mydept=======%s"%mydept)
          self.assertEqual('自动化测试用例系统企业域', mydept, msg=name + '检验不通过')
       
    def test_selected_my_dept_case(self):
          '''﻿默认值所属部门'''
          name='部门选择框_默认值所属部门'
          dp = DepartmentPage(self.driver, name)
          dp.wait_Tabloading_show_then_hide()
          mydept = dp.get_selected_depart_name()
          self.assertEqual('自动化测试组', mydept, msg=name + '检验不通过')

    def test_value_design_case(self):
        '''值设计模式'''
        '''部门选择框_名称=部门选择框_值设计'''
  
        reflesh_name = '部门选择框_名称'
        recalculate_name='部门选择框_值设计'
        dp = DepartmentPage(self.driver, reflesh_name)
        dp.wait_Tabloading_show_then_hide()
        #选择第2个选项部门
        reflesh_dept=dp.select_department_num(2)
        dp.wait_Tabloading_show_then_hide()
        dp2 = DepartmentPhonePage(self.driver, recalculate_name)
        self.assertEqual(reflesh_dept,dp2.find_element('#部门选择框_值设计_show').text, msg='刷新重计算检验不通过')
       

    def init(self):
        '''类型、只读、隐藏属性测试'''
#         self.test_type_case()
#         self.test_readonly_case()
#         self.test_hide_case()
#         self.test_refresh_case()
#         self.test_desription_case()
#         self.test_not_null_case()
#         self.test_level_liandong_case()
#         self.test_my_department_case()
#         self.test_selected_firt_dept_case()
#         self.test_selected_my_dept_case()
        self.test_value_design_case()

        
if __name__ == '__main__':
    unittest.main()
