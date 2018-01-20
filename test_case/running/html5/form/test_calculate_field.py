import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.calculate_page import CalculatePage


class CalculateTest(ComponentTest):
    '''计算脚本测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '计算脚本'
    
    def test_type_case(self):
        '''名称'''
        name = '计算脚本_普通字符串'
        comp = CalculatePage(self.driver)
        self.assertEqual('普通字符串', comp.get_text_by_css_selector('span.calctext-field'), msg=name + '检验不通过')
        
    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '计算脚本_重计算'
        comp = CalculatePage(self.driver)
        input = InputPage(self.driver, '计算脚本_单行文本刷新')
        input.send_keys_trigger_refresh('refresh_calculate')
        self.assertTrue(comp.has_the_text('refresh_calculate生效'), msg=name + '检验不通过')

    def test_show_when_print_case(self):
        '''打印时显示值'''
        name = '计算脚本_打印时显示值'
        comp = CalculatePage(self.driver)
        comp.open_and_switch_to_print_page()
#         time.sleep(0.5)
        self.assertEqual('普通字符串', comp.get_text_by_css_selector('span.calctext-field'), msg=name + '检验不通过')
#         comp.close_currentwindow()
    
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_refresh_calculate_case()
        self.test_show_when_print_case()
        
        
if __name__ == '__main__':
    unittest.main()
