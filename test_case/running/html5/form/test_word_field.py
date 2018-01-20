import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.word_page import WordPage
from test_case.page_obj.button_page import ButtonPage


class WordTest(ComponentTest):
    '''Word控件测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = 'Word控件'
    
    def test_type_case(self):
        '''名称'''
        name = 'word控件_名称'
        comp = WordPage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.get_the_div_hide(), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.get_the_div_img(), msg=name + '检验不通过')
        self.assertIn('/share/images/view/genericword.jpg', comp.get_the_div_img_src(), msg=name + '检验不通过')
        comp.click_img()
        self.assertEqual('word编辑对话框', comp.get_out_win_title(), msg=name + '检验不通过')
        
    def test_embed_case(self):
        '''嵌入式'''
        name = 'word控件_嵌入在页面显示'
        comp = WordPage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.get_the_div_iframe(), msg=name + '检验不通过')
        mp = MainPage(self.driver)
        comp.switch_to_the_iframe(comp.get_the_div_iframe())
        self.assertEqual('word文档', comp.get_word_text(), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = 'word控件_重计算'
        comp = WordPage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.get_the_div_hide(), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.get_the_div_img(), msg=name + '检验不通过')
        self.assertIn('/share/images/view/genericword.jpg', comp.get_the_div_img_src(), msg=name + '检验不通过')
        input = InputPage(self.driver, '单行文本刷新')
        input.send_keys_trigger_refresh('hide')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = 'word控件_隐藏时显示值'
        comp = WordPage(self.driver, name)
        comp.from_scroll_to('700')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('隐藏时显示值'), msg=name + '检验不通过')
        
    def test_show_when_print_case(self):
        '''打印隐藏时显示值'''
        name = 'word控件_打印隐藏时显示值'
        comp = WordPage(self.driver, '')
        comp.open_and_switch_to_print_page()
        #time.sleep(0.5)
        comp.window_scroll_to('1000')
        self.assertEqual('none', comp.find_element_by_css_selector('input[name="'+name+'"]'), msg=name + '检验不通过')
        self.assertTrue(comp.show_when_print('打印隐藏时显示值'), msg=name + '检验不通过')
        comp.close_currentwindow()
    
    def test_readonly_case(self):
        '''只读条件'''
        name = 'word控件_只读条件'
        comp = WordPage(self.driver, name)
        comp.from_scroll_to('700')
        comp.click_img()
        #time.sleep(0.5)
        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()
        
        self.assertFalse(comp.is_edit_in_div_page(), msg=name + '检验不通过')
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_embed_case()
#         self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_show_when_hide_case()
#         self.test_show_when_print_case()
        self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
