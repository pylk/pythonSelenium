import os
import sys
import time
import unittest

sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.gps_page import GPSPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage


class GPSPhoneTest(ComponentPhoneTest):
    '''GPS定位控件测试'''

    menu1 = '表单'
    menu2 = '表单控件'  # 主页打开菜单时使用
    menu3 = '手机端GPS定位'

    def test_type_case(self):
        '''GPS定位类型'''
        comp = GPSPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        name = 'GPS定位类型'
        compname = 'GPS定位_名称'
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        type = target_element.get_attribute("moduletype")
        self.assertEqual(type,"weixingpsfield", msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        compname = 'GPS定位_描述'
        comp = GPSPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        bool = comp.is_desription_effect(compname)
        self.assertTrue(bool, msg=compname + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        compname = 'GPS定位_隐藏时显示值'
        comp = GPSPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        bool = comp.is_comp_hide(compname)
        self.assertFalse(bool,msg=compname + '检验不通过')
        self.assertIn('控件已隐藏', comp.get_curpage_span(), msg=compname + '检验不通过')


    def init(self):
        '''所有测试'''
        self.test_type_case()
        self.test_desription_case()
        self.test_show_when_hide_case()


if __name__ == '__main__':
    unittest.main()
