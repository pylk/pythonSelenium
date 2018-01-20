import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.tree_department_page import TreeDepartmentPage
from test_case.page_obj.form.input_page import InputPage


class TreeDepartmentTest(ComponentTest):
    '''树形部门选择框'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '树形部门选择框'  #主页打开菜单时使用
    

    def test_type_case(self):
        '''类型'''
#         self.scroll_to('0')
        name = '树形部门选择框_名称'
        comp = TreeDepartmentPage(self.driver, name)
        self.assertEqual('TreeDepartmentField', comp.get_attr('fieldtype'), msg=name + '检验不通过')
        self.assertEqual('form-control department-cmd', comp.get_attr('class'), msg=name + '检验不通过')
  
    def test_readonly_case(self):
        '''只读判断'''
#         self.scroll_to('0')
        name = '树形部门选择框_显示只读'
        comp = TreeDepartmentPage(self.driver, name)
        self.assertTrue(comp.span_is_displayed(), msg=name + '检验不通过')
          
        comp.from_scroll_to('800') 
        name = '树形部门选择框_只读条件'
        comp = TreeDepartmentPage(self.driver, name)
        self.assertTrue(comp.span_is_displayed(), msg=name + '检验不通过')
  
    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
#         self.scroll_to('0')
        name = '树形部门选择框_显示隐藏'
        comp = TreeDepartmentPage(self.driver, name)
        self.assertIn('display: none', comp.get_dept().get_attribute("style"), msg=name + '检验不通过')
        
          
        comp.from_scroll_to('800') 
        name = '树形部门选择框_隐藏时显示值'
        comp = TreeDepartmentPage(self.driver, name)
        self.assertIn('display: none', comp.get_dept().get_attribute("style"), msg=name + '检验不通过')
          
    def test_only_value_case(self):
        '''只读时仅显示值'''
#         self.scroll_to('0')
        name = '树形部门选择框_只读时仅显示值'
        comp = TreeDepartmentPage(self.driver, name)
        self.assertTrue(comp.span_is_displayed(), msg=name + '检验不通过')  
                
    def test_refresh_case(self):
        '''刷新'''
#         self.scroll_to('0')
        name = '树形部门选择框_刷新'
        cmpname='已选部门数'
        comp = TreeDepartmentPage(self.driver, name)
        depts=comp.select_dept()
          
        print("depts=========%s"%depts)
        comp2 = InputPage(self.driver, cmpname)
        self.assertEqual("已刷新",comp2.get_attr('value'), msg=name + '检验不通过')
          
    def test_recaculate_case(self):
        '''重计算'''
#         self.scroll_to('0')
        reflesh_name='只读刷新'
        name = '树形部门选择框_重计算'
        comp = InputPage(self.driver, reflesh_name)
        comp.send_keys_trigger_refresh('只读')
   
        comp2 = TreeDepartmentPage(self.driver, name)                   
        self.assertTrue(comp2.span_is_displayed(), msg=name + '检验不通过') 
  
    def test_desription_case(self):
        '''描述'''

        name = '树形部门选择框_描述'
        comp = TreeDepartmentPage(self.driver, name)
        comp.from_scroll_to('400')         
        self.assertEqual('树形部门选择框_描述', comp.get_attr('discript'), msg=name + '检验不通过')
  
    def test_show_when_hide_case(self):
        '''隐藏时显示值'''

        name = '树形部门选择框_隐藏时显示值'
        comp = TreeDepartmentPage(self.driver, name)
        comp.from_scroll_to('800')         
        self.assertEqual("控件已隐藏", comp.get_text_by_css_selector('input[name="'+name+'"] + span'), msg=name + '检验不通过')
    
    def test_not_null_case(self):
        '''非空校验'''
        name = '树形部门选择框_非空校验'
        comp = TreeDepartmentPage(self.driver, name)
        comp.from_scroll_to('400')         
        self.assertIn("'树形部门选择框_非空校验'必须填写", comp.save_get_msg(), msg=name + '检验不通过')

    def test_clean_button(self):
          '''选择部门后清除数据'''

          name='树形部门选择框_点击清除'
          comp = TreeDepartmentPage(self.driver, name)
          comp.from_scroll_to('700')           
          #选择2个部门          
          comp.select_dept()  
          #点击【清除】按钮
          comp.clean_button()
          self.assertEqual('',comp.get_attr('value'), msg=name + '检验不通过')
   
         
 
    def test_close_button(self):
          '''关闭树形部门弹出框'''

          name='树形部门选择框_点击退出'
          comp = TreeDepartmentPage(self.driver, name)  
          comp.from_scroll_to('700')                           
          self.assertEqual("closed",comp.close_dept(), msg=name + '检验不通过')
         

    def init(self):
        '''类型、只读、隐藏属性测试'''
        self.test_type_case()
        self.test_readonly_case()
        self.test_hide_case()
        self.test_only_value_case()
        self.test_refresh_case()
        self.test_recaculate_case()
        self.test_desription_case()
        self.test_show_when_hide_case()
        self.test_not_null_case()
#         self.test_beyond_dept_num_case()
        self.test_clean_button()
        self.test_close_button()

            
        
if __name__ == '__main__':
    unittest.main()
