import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.calculate_page import CalculatePhonePage


class CalculatePhoneTest(ComponentPhoneTest):
    '''手机端计算脚本测试'''

    menu1 = '表单'
    menu2 = '表单控件'  # 主页打开菜单时使用
    menu3 = '计算脚本'

    def test_type_case(self):
        '''名称'''
        name = '计算脚本_普通字符串'
        comp = CalculatePhonePage(self.driver)
        self.assertIn('普通字符串', comp.get_curpage_span(), msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '计算脚本_重计算'
        comp = CalculatePhonePage(self.driver)
        input = InputPage(self.driver, '计算脚本_单行文本刷新')
        input.send_keys_trigger_refresh('refresh_calculate')
        self.assertIn('refresh_calculate生效', comp.get_curpage_span(), msg=name + '检验不通过')


    def init(self):
        '''所有测试'''
        self.test_type_case()
        self.test_refresh_calculate_case()



if __name__ == '__main__':
    unittest.main()
