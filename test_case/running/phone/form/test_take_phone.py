import os
import sys
import time
import unittest

sys.path.append('../../../../')
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.form.take_phone_page import TakephotoPhonePage
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.view.list_view_page import ListViewPhonePage


class TakephotoPhoneTest(ComponentPhoneTest):
    '''在线拍照测试'''

    menu1 = '表单'
    menu2 = '表单控件'  # 主页打开菜单时使用
    menu3 = '手机端在线拍照'

    def test_type_case(self):
        '''在线拍照控件类型'''
        comp = TakephotoPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        name = '在线拍照类型'
        compname = '在线拍照_名称'
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        type = target_element.get_attribute("fieldtype")
        self.assertEqual(type,"OnLineTakePhotoField", msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        compname = '在线拍照_描述'
        comp = TakephotoPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        bool = comp.is_desription_effect(compname)
        self.assertTrue(bool, msg=compname + '检验不通过')


    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        compname = '在线拍照_重计算'
        comp = TakephotoPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        bool1 = comp.is_comp_hide(compname)
        self.assertTrue(bool1,msg=compname + '检验不通过')
        inputtext_name = '单行文本刷新'
        textInput = InputPhonePage(self.driver, inputtext_name)
        textInput.send_keys_trigger_refresh('hide')
        bool = comp.is_comp_hide(compname)
        self.assertFalse(bool,msg=compname + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        compname = '在线拍照_隐藏时显示值'
        comp = TakephotoPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        bool = comp.is_comp_hide(compname)
        self.assertFalse(bool,msg=compname + '检验不通过')
        self.assertIn('控件已隐藏', comp.get_curpage_span(), msg=compname + '检验不通过')

    def test_readonly_case(self):
        '''在线拍照_只读条件'''
        comp = TakephotoPhonePage(self.driver)
        name = '在线拍照_只读条件'
        compname = '在线拍照_只读条件'
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target = comp.getcomp(compname)
        comp.scroll_to_target_element(target)
        bool = comp.is_comp_readonly(compname)
        self.assertTrue(bool,msg=name + '检验不通过')

    def init(self):
        '''所有测试'''
        self.test_type_case()
        self.test_refresh_calculate_case()
        self.test_desription_case()
        self.test_show_when_hide_case()
        self.test_readonly_case()


if __name__ == '__main__':
    unittest.main()
