import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
os.sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.date_field_page import DateFieldPage
from datetime import timedelta, datetime


class DateFieldTest(ComponentTest):
    '''日期选择框测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '日期选择框'  #主页打开菜单时使用
     
    def test_case_imited(self):
        '''限制_刷新_重计算'''
#         self.scroll_to('460')
        #time.sleep(0.5)
        state_date = '开始日期'
        comp = DateFieldPage(self.driver, state_date)
        #点击日期确认按钮     
        today =  datetime.today().strftime('%Y-%m-%d')
        yesterday =(datetime.today() + timedelta(-1)).strftime('%Y-%m-%d')
         
        
        start_time = comp.get_now_date(today)  
        self.assertEqual(today, start_time, msg=state_date + '检验不通过')
        end_date = '结束日期'
        comp = DateFieldPage(self.driver, end_date)
        #结束时间只能选择开始时间之后是数据，所以开始时间之前的时间为day disabled，开始之后是day active
        todayStatus = comp.get_end_date_status(end_date,today)
        self.assertIn("day active", todayStatus, msg=end_date + '检验不通过')       
        yesterdayStatus = comp.get_end_date_status(end_date,yesterday)     
        self.assertIn("day disabled", yesterdayStatus, msg=end_date + '检验不通过')
     
    def test_type_case(self):
        '''类型'''
#         self.scroll_to('0')
        name = '日期选择框_名称'
        comp = DateFieldPage(self.driver, name)
        self.assertEqual('text', comp.get_attr('type'), msg=name + '检验不通过')
        self.assertEqual('form-control Wdate', comp.get_attr('class'), msg=name + '检验不通过')
        self.assertEqual('DateField', comp.get_attr('fieldtype'), msg=name + '检验不通过')
 
    def test_readonly_case(self):
        '''显示只读和条件只读'''
#         self.scroll_to('0')
        name = '日期选择框_显示只读'
        comp = DateFieldPage(self.driver, name)
        self.assertTrue(comp.readonly_test(), msg=name + '检验不通过')
         
#         self.scroll_to('800')
        name = '日期选择框_只读条件'
        comp = DateFieldPage(self.driver, name)
        self.assertTrue(comp.readonly_test(), msg=name + '检验不通过')
         
    def test_hide_case(self):
        '''显示隐藏和条件隐藏'''
#         self.scroll_to('0')
        name = '日期选择框_显示隐藏'
        comp = DateFieldPage(self.driver, name)
        self.assertEqual('hidden', comp.get_attr('type'), msg=name + '检验不通过')
         
         
         
    def test_only_value_case(self):
        '''只读时仅显示值'''
        self.scroll_to('0')
        name = '日期选择框_只读时仅显示值'
        comp = DateFieldPage(self.driver, name)
        self.assertTrue(comp.only_value(), msg=name + '检验不通过')
 
    def test_desription_case(self):
        '''描述'''
        self.scroll_to('550')
        name = '日期选择框_描述'
        comp = DateFieldPage(self.driver, name)
        self.assertEqual('日期选择框_描述', comp.get_attr('discript'), msg=name + '检验不通过')
 
    def test_value_case(self):
        '''值'''
        self.scroll_to('550')
        name = '日期选择框_值脚本'
        comp = DateFieldPage(self.driver, name)
        self.assertEqual(datetime.today().strftime('%Y-%m-%d'), comp.get_attr('value'), msg=name + '检验不通过')
 
 
    def test_not_null_case(self):
        '''非空校验'''
        self.scroll_to('550')
        name = '日期选择框_非空校验'
        comp = DateFieldPage(self.driver, name)
        self.assertIn("'日期选择框_非空校验'必须填写", comp.set_val_save_get_msg(''), msg=name + '检验不通过')
         
    def test_show_when_hide_case(self):

        name = '日期选择框_隐藏时显示值'
        comp = DateFieldPage(self.driver, name)
        comp.from_scroll_to('600')
        self.assertEqual('hidden', comp.get_attr('type'), msg=name + '检验不通过')
        self.assertIn("控件已隐藏",comp.get_curpage_span(), msg=name + '检验不通过')
 
    def test_format_case(self):
        '''显示只读和条件只读'''
        self.scroll_to('0')
        name = '日期选择框_格式年'
        comp = DateFieldPage(self.driver, name)
        self.assertEqual('yyyy',comp.get_attr('datefmt'), msg=name + '检验不通过')
 
        name = '日期选择框_格式年月'
        comp = DateFieldPage(self.driver, name)
        self.assertEqual('yyyy-MM-dd',comp.get_attr('datefmt'), msg=name + '检验不通过')     
         
        name = '日期选择框_格式年到秒'
        comp = DateFieldPage(self.driver, name)
        self.assertEqual('yyyy-MM-dd HH:mm:ss',comp.get_attr('datefmt'), msg=name + '检验不通过')   
         
        name = '日期选择框_格式时分秒'
        comp = DateFieldPage(self.driver, name)
        self.assertEqual('HH:mm:ss',comp.get_attr('datefmt'), msg=name + '检验不通过') 

    #def test_print_hide_case(self):
    #         '''打印时隐藏条件'''
    #         self.scroll_to('1000')
    #         name = '日期选择框_打印时隐藏条件'
    #         comp = DateFieldPage(self.driver, name)
    #         self.assertIsNone(comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
    #         
    #     def test_show_when_print_case(self):
    #         '''打印隐藏时显示值'''
    #         self.scroll_to('1000')
    #         name = '日期选择框_打印隐藏时显示值'
    #         comp = DateFieldPage(self.driver, name)
    #         self.assertEqual("打印隐藏时显示值", comp.get_text_by_css_selector('#toAll p'), msg=name + '检验不通过')
              
          
        
    def init(self):
        self.test_case_imited()
        '''类型、只读、隐藏属性测试'''
        self.test_type_case()
        self.test_readonly_case()       
        self.test_hide_case()
        self.test_only_value_case()
        self.test_desription_case()
        self.test_value_case()
        self.test_not_null_case()
        self.test_format_case()
        self.test_show_when_hide_case()
        
if __name__ == '__main__':
    unittest.main()
