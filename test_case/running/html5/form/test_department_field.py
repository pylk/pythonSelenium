import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.department_page import DepartmentPage
from test_case.page_obj.form.input_page import InputPage


class DepartmentTest(ComponentTest):
    '''部门选择框'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '部门选择框'  #主页打开菜单时使用
    

    def test_type_case(self):
        '''类型'''
        name = '部门选择框_名称'
        comp = DepartmentPage(self.driver, name)
        self.assertEqual('DepartmentField', comp.get_attr('fieldtype'), msg=name + '检验不通过')
        self.assertEqual('form-control component-select', comp.get_attr('class'), msg=name + '检验不通过')
 
   
    def test_readonly_case(self):
        '''只读判断'''
        name = '部门选择框_显示只读'
        comp = DepartmentPage(self.driver, name)
        self.assertIsNotNone(comp.get_attr("disabled"), msg=name + '检验不通过')
        self.assertEqual("false",comp.get_attr("readonlyshowvalonly"), msg=name + '检验不通过')   
        self.scroll_to('800')
        name = '部门选择框_条件只读'
        comp = DepartmentPage(self.driver, name)
        self.assertTrue(comp.span_is_displayed(), msg=name + '检验不通过')
        self.assertEqual("true",comp.get_attr("readonlyshowvalonly"), msg=name + '检验不通过')  
    
    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
        name = '部门选择框_显示隐藏'
        comp = DepartmentPage(self.driver, name)
        self.assertIn('display: none', comp.get_attr("style"), msg=name + '检验不通过')           
        name = '部门选择框_隐藏显示值'
        comp = DepartmentPage(self.driver, name)
        comp.from_scroll_to('800')
        self.assertIsNotNone(comp.get_attr("disabled"), msg=name + '检验不通过')        
        self.assertIn("控件已隐藏",comp.get_curpage_span(), msg=name + '检验不通过')
                  
    def test_refresh_case(self):
        '''刷新  重计算'''
        '''刷新字段=重计算字段的值'''
#         self.scroll_to('200')
        reflesh_name = '部门选择框_刷新'
        recalculate_name='部门选择框_重计算'
        cmpname='已选部门数'
        comp1 = DepartmentPage(self.driver, reflesh_name)
        comp1.from_scroll_to('400')
        #选择第2个选项部门
        reflesh_dept=comp1.select_department_num(2)
        comp1.wait_refresh_loading_back_show_then_hide()
        self.assertEqual(reflesh_dept,comp1.get_text_by_css_selector('select[name="'+recalculate_name+'"]+span'), msg='刷新重计算检验不通过')
              
                
    def test_desription_case(self):
        '''描述'''
#         self.scroll_to('500')
        name = '部门选择框_描述'
        comp = DepartmentPage(self.driver, name)
        self.assertEqual('部门选择框_描述', comp.get_attr('discript'), msg=name + '检验不通过')
     
     
    def test_not_null_case(self):
        '''非空校验和第一选项为空值'''
        name = '部门选择框_非空校验'
        comp = DepartmentPage(self.driver, name)
        self.assertIn("'部门选择框_非空校验'必须填写", comp.save_get_msg(), msg=name + '检验不通过')
       
    def test_level_liandong_case(self):
        '''可选一级部门和下级部门联动'''
        name = '部门选择框_可选一级'
        comp = DepartmentPage(self.driver, name)
        #获取可选值的数据量为1  
        self.assertEqual(1, len(comp.get_department_list()), msg=name + '检验不通过')
        #验证联动，可选部门数量为2
        name2 = '部门选择框_上级联动'
        comp2 = DepartmentPage(self.driver, name2)        
        self.assertEqual(2, len(comp2.get_department_list()), msg=name2 + '检验不通过')
          
    def test_my_department_case(self):
          '''﻿显示当前用户所属部门及下属部门'''
          name='部门选择框_当前下级部门'
          comp = DepartmentPage(self.driver, name)
          #获取可选值的数据量为2 
          self.assertEqual(2, len(comp.get_department_list()), msg=name + '检验不通过')
          mydept = comp.get_department_list_name()
          print("mydept=======%s"%mydept)
          self.assertEqual('下属部门;自动化测试组;', mydept, msg=name + '检验不通过')
           
    def test_selected_firt_dept_case(self):
          '''﻿默认值第一个部门'''
          name='部门选择框_默认值第一个'
          comp = DepartmentPage(self.driver, name)
          mydept = comp.get_selected_depart_name()
          print("mydept=======%s"%mydept)
          self.assertEqual('自动化测试用例系统企业域', mydept, msg=name + '检验不通过')
       
    def test_selected_my_dept_case(self):
          '''﻿默认值所属部门'''
          name='部门选择框_默认值所属部门'
          comp = DepartmentPage(self.driver, name)
          mydept = comp.get_selected_depart_name()
          print("mydept=======%s"%mydept)
          self.assertEqual('自动化测试组', mydept, msg=name + '检验不通过')
              
                    
    def test_value_design_case(self):
        '''值设计模式'''
        '''部门选择框_名称=部门选择框_值设计'''
  
        reflesh_name = '部门选择框_名称'
        recalculate_name='部门选择框_值设计'
        comp1 = DepartmentPage(self.driver, reflesh_name)
        #选择第2个选项部门
        reflesh_dept=comp1.select_department_num(2)
        self.scroll_to('600')
        self.assertEqual(reflesh_dept,comp1.get_text_by_css_selector('select[name="'+recalculate_name+'"]+span'), msg='部门选择框_名称=部门选择框_值设计')
       

    def init(self):
        '''类型、只读、隐藏属性测试'''
        self.test_type_case()
        self.test_readonly_case()
        self.test_hide_case()
        self.test_only_value_case()
        self.test_refresh_case()
        self.test_desription_case()
        self.test_not_null_case()
        self.test_level_liandong_case()
        self.test_my_department_case()
        self.test_selected_firt_dept_case()
        self.test_selected_my_dept_case()
        self.test_value_design_case()

            
        
if __name__ == '__main__':
    unittest.main()
