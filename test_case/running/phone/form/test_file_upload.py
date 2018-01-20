import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.file_upload_page import FileUploadPhonePage


class FileUploadPhoneTest(ComponentPhoneTest):
    '''手机端文件上传'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '文件上传'

    def test_type_case(self):
        '''文件上传类型'''
        print(os.getcwd ())
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传类型'
        compname = '文件上传_名称'
        target_element = comp.getcomp(compname)
        comp.scroll_to_target_element(target_element)
        type = target_element.get_attribute("fieldtype")
        self.assertEqual(type,"AttachmentUploadField", msg=name + '检验不通过')

    def test_uploadsize_case(self):
        '''文件上传控件上传大小限制'''
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传_限大小'
        compname = '文件上传_限大小'
        file_path = comp.get_file_path("大于100kb.doc")
        file_path2 = comp.get_file_path("小于100KB.txt")
        result = comp.file_upload(compname, file_path)
        self.assertIn("上传文件大小超出限制",result,msg=name + '检验不通过')
        #time.sleep(0.5)
        result2 =comp.file_upload(compname,file_path2)
        self.assertIn("上传完成", result2, msg=name + '检验不通过')
        # #time.sleep(0.5)
        # comp.open_file_to_preview('小于100KB.txt')
        # comp.switch_to_fileupload_iframe()
        # self.assertIn("小于100KB.txt",comp.get_preview_title(),msg=name + '检验不通过')

    def test_uploadtype_case(self):
        '''文件上传控件上传类型'''
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传控件上传类型'
        compname = '文件上传_格式'
        file_path = comp.get_file_path("大于100kb.doc")
        file_path2 = comp.get_file_path("小于100KB.txt")
        result = comp.file_upload(compname, file_path2)
        self.assertIn("文件类型(仅支持'doc,xls'格式)或大小错误", result, msg=name + '检验不通过')
        #time.sleep(0.5)
        result2 = comp.file_upload(compname, file_path)
        self.assertIn("上传完成", result2, msg=name + '检验不通过')
        # #time.sleep(0.5)
        # self.driver.find_element_by_link_text("大于100kb.doc").click()
        # comp.switch_to_another_window()
        # #time.sleep(0.5)
        # text2 = comp.find_elem('span.preview-header-name').text
        # #time.sleep(0.5)
        # self.assertIn("大于100kb.doc",text2,msg=name + '检验不通过')
        # comp.close_currentwindow()

    def test_uploadnum_case(self):
        '''文件上传控件上传数量'''
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传控件上传数量'
        compname = '文件上传_限数量1个'
        file_path = comp.get_file_path("大于100kb.doc")
        file_path2 = comp.get_file_path("小于100KB.txt")
        comp.file_upload(compname, file_path2)
        comp.click_fileupload_btn(compname)  # 點擊上傳按鈕
        text = comp.adjustalertexistence()
        self.assertEqual("文件上传超出数量限制。", text, msg=name + '检验不通过')

    def test_recalculation_case(self):
        '''文件上传控件刷新重计算'''
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传控件重计算'
        compname = '文件上传_重计算'
        compname2 = '文件上传_刷新'
        target = comp.getcomp(compname2)
        comp.scroll_to_target_element(target)
        file_path = comp.get_file_path("大于100kb.doc")
        bool1 = comp.check_existence(compname)
        self.assertTrue(bool1,msg=name + '检验不通过')
        comp.file_upload(compname2, file_path)
        #time.sleep(0.5)
        bool2 = comp.check_existence(compname)
        self.assertFalse(bool2, msg=name + '检验不通过')

    def test_notnull_case(self):
        '''文件上传控件非空校验'''
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传控件非空校验'
        btn = ButtonPhonePage(self.driver)
        btn.click_button('保存')
        #time.sleep(0.5)
        text1 = comp.get_msg()
        self.assertIn("文件上传_非空校验'必须填写！", text1, msg=name + '检验不通过')

    def test_discript_case(self):
        '''文件上传控件描述校验'''
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传_描述'
        compname = '文件上传_描述'
        target = comp.getcomp(compname)
        comp.scroll_to_target_element(target)
        bool = comp.is_desription_effect(compname)
        self.assertTrue(bool,msg=name + '检验不通过')

    def test_hidevalue_case(self):
        '''文件上传_隐藏显示值'''
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传_隐藏显示值'
        compname = '文件上传_隐藏显示值'
        target = comp.getcomp(compname)
        comp.scroll_to_target_element(target)
        bool = comp.check_existence(compname)
        self.assertFalse(bool,msg=name + '检验不通过')
        self.assertIn('控件已隐藏',comp.get_curpage_span(),msg=name + '检验不通过')

    def test_readonly_case(self):
        '''文件上传控件只读'''
        comp = FileUploadPhonePage(self.driver)
        name = '文件上传_条件只读'
        compname = '文件上传_条件只读'
        target = comp.getcomp(compname)
        comp.scroll_to_target_element(target)
        bool = comp.is_comp_readonly(compname)
        self.assertTrue(bool,msg=name + '检验不通过')
        text = comp.getcompatrr(compname, 'disabled')
        self.assertEqual('true', text, msg=name + '检验不通过')

    def init(self):
#         self.test_type_case()
#         self.test_recalculation_case()
#         self.test_notnull_case()
#         self.test_hidevalue_case()
#         self.test_readonly_case()
        self.test_discript_case()
#         self.test_uploadsize_case()
#         self.test_uploadtype_case()
#         self.test_uploadnum_case()


if __name__ == '__main__':
    unittest.main()