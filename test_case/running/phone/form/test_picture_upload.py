import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.file_upload_page import FileUploadPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage


class PictureUploadTest(ComponentPhoneTest):
    '''手机端图片上传'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '手机端图片上传'

    def test_type_case(self):
        '''图片上传类型'''
        comp = FileUploadPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        name = '图片上传类型'
        compname = '图片上传_名称'
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        type = target_element.get_attribute("fieldtype")
        self.assertEqual(type,"ImageUploadField", msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        compname = '图片上传_描述'
        comp = FileUploadPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        bool = comp.is_desription_effect(compname)
        self.assertTrue(bool, msg=compname + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        compname = '图片上传_隐藏时显示值'
        comp = FileUploadPhonePage(self.driver)
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        bool = comp.is_picturecomp_hide(compname)
        self.assertFalse(bool,msg=compname + '检验不通过')
        self.assertIn('控件已隐藏', comp.get_curpage_span(), msg=compname + '检验不通过')

    def test_readonly_case(self):
        '''图片上传控件只读'''
        comp = FileUploadPhonePage(self.driver)
        name = '图片上传_只读'
        compname = '图片上传_只读'
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()  # 打开记录
        target = comp.getcomp(compname)
        comp.scroll_to_target_element(target)
        bool = comp.is_comp_readonly(compname)
        self.assertTrue(bool,msg=name + '检验不通过')


    def init(self):
        self.test_type_case()
        self.test_readonly_case()
        self.test_show_when_hide_case()
        self.test_desription_case()

if __name__ == '__main__':
    unittest.main()



