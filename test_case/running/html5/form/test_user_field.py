import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.user_select_page import UserSelectPage
from test_case.page_obj.form.input_page import InputPage


class UserFieldTest(ComponentTest):
    '''用户选择框'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '用户选择框'  #主页打开菜单时使用
    

    def test_type_case(self):
        '''类型'''
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)
        self.assertEqual('UserField', comp.get_attr('fieldtype'), msg=name + '检验不通过')
        self.assertEqual('form-control', comp.get_attr('class'), msg=name + '检验不通过')
    
    def test_readonly_case(self):
        '''只读判断'''
        name = '用户选择框_显示只读_text'
        comp = UserSelectPage(self.driver, name)
        self.assertTrue(comp.span_is_displayed(), msg=name + '检验不通过')
             
        comp.from_scroll_to('400') 
        name = '用户选择框_条件只读_text'
        comp = UserSelectPage(self.driver, name)
        self.assertTrue(comp.readonly_test(), msg=name + '检验不通过') 
   
   
    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
        name = '用户选择框_显示隐藏_text'
        comp = UserSelectPage(self.driver, name)
        self.assertEqual('hidden', comp.get_attr("type"), msg=name + '检验不通过')         
        name1 = '用户选择框_隐藏显示值_text'
        comp = UserSelectPage(self.driver, name1)
        self.assertEqual('hidden', comp.get_attr("type"), msg=name1 + '检验不通过')
        self.assertEqual("控件已隐藏", comp.get_text_by_css_selector('input[name="'+name1+'"] + span'), msg=name + '检验不通过')
   
    def test_desription_case(self):
        '''描述'''
   
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)        
        self.assertEqual('用户选择框_描述', comp.get_attr('discript'), msg='用户选择框_描述检验不通过')
   
    def test_not_null_case(self):
        '''非空校验'''
        name = '用户选择框_非空校验_text'
        comp = UserSelectPage(self.driver, name)
        comp.from_scroll_to('400')         
        self.assertIn("'用户选择框_非空校验'必须填写！", comp.save_get_msg(), msg=name + '检验不通过')
  
   
    def test_refresh_recaculate_case(self):
        '''刷新重计算值脚本'''
        refresh_name = '用户选择框_刷新_text'
        comp1 = UserSelectPage(self.driver, refresh_name)       
        comp1.select_user_byroles()
    
        recaculate_name='用户选择框_重计算_text'
        comp2 = UserSelectPage(self.driver, recaculate_name)              
        self.assertEqual(comp1.get_attr('value'),comp2.get_attr('value'), msg= '刷新重计算值脚本检验不通过')                
    
    def test_selected_radio_type_case(self):
        '''用户单选'''
        name = '用户选择框_单选_text'
        comp = UserSelectPage(self.driver, name)
        select_type = comp.select_user_byroles()
        self.assertEqual('radio', select_type, msg=name + '检验不通过')         
        self.assertEqual('伟强', comp.get_attr("title"), msg=name + '检验不通过')         
   
    def test_selected_checkbox_type_case(self):
        '''用户多选'''
        name = '用户选择框_多选_text'
        comp = UserSelectPage(self.driver, name)
        select_type = comp.select_user_byroles()
        self.assertEqual('checkbox', select_type, msg=name + '检验不通过')         
        self.assertEqual('王聪;伟强', comp.get_attr("title"), msg=name + '检验不通过')
   
    def test_select_user_bydept_case(self):
        '''从部门中获取用户'''
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)
        select_type = comp.select_user_bydept()
        self.assertIn('李玲;王聪;张强', comp.get_attr("title"), msg='从部门中获取用户检验不通过')   
    
    def test_select_user_byonline_case(self):
        '''从在线用户中获取用户'''
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)
        select_type = comp.select_user_byonline()
        #self.assertEqual('checkbox', select_type, msg=name + '检验不通过')
        self.assertIsNotNone(comp.find_elem_visible('textarea[title="李玲"][name="用户选择框_名称_text"]'), msg='从在线用户中获取用户检验不通过')
      
     
    def test_select_user_bycontancts_case(self):
        '''从通讯录中获取用户'''
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)
        comp.select_user_bycontancts()
        self.assertIn('李玲', comp.get_attr("title"), msg='从通讯录中获取用户检验不通过')   
   
    def test_select_user_bysearch_case(self):
        '''从查询中获取用户'''
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)
        select_type = comp.select_user_bysearch()          
        self.assertIn('李玲', comp.get_attr("title"), msg='从通讯录中获取用户检验不通过')        
   
   
    def test_add_page_user_byroles_case(self):
        '''添加本页所有用户'''
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)
        comp.add_page_user_byroles()          
        self.assertIn('王聪;伟强', comp.get_attr("title"), msg='添加本页所有用户检验不通过') 
    
    
    def test_remove_all_user_byroles_case(self):
        '''移除所有用户'''
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)
        comp.remove_all_user_byroles()          
        self.assertIn('', comp.get_attr("title"), msg='在线用户中获取用户检验不通过') 
 
    def test_cleanup_user_case(self):
        '''清除已选用户'''
        name = '用户选择框_名称_text'
        comp = UserSelectPage(self.driver, name)
        comp.select_user_byroles() #打开 用户选择框
        comp.find_elem_is_clickable('textarea[name="'+name+'"] +span + span').click()#点击清除按钮
        self.assertIn('', comp.get_attr("title"), msg='清除已选用户检验不通过') 
                                   
    def init(self):
        '''类型、只读、隐藏属性测试'''
        self.test_type_case()
        self.test_readonly_case()
        self.test_refresh_recaculate_case()
        self.test_desription_case()
        self.test_not_null_case()
        self.test_hide_case()
        self.test_selected_radio_type_case()
        self.test_selected_checkbox_type_case()
        self.test_select_user_bydept_case()
        self.test_select_user_byonline_case()
        self.test_select_user_bycontancts_case()
        self.test_select_user_bysearch_case()    
        self.test_add_page_user_byroles_case()  
        self.test_remove_all_user_byroles_case()  
        self.test_cleanup_user_case()                   


            
        
if __name__ == '__main__':
    unittest.main()
