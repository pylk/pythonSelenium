import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.file_upload_page import FileUploadPage


class PictureUploadTest(ComponentTest):
    '''图片上传'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '图片上传'

    def test_type_case(self):
        '''图片上传类型'''
        comp = FileUploadPage(self.driver)
        name = '图片上传类型'
        compname = '图片上传_名称'
        self.scroll_to('0')
        a = comp.getcomp(compname)
        type = a.get_attribute("fieldtype")
        self.assertEqual(type,"ImageUploadField", msg=name + '检验不通过')

    def test_uploadsize_case(self):
        '''图片上传控件_限制大小'''
        comp = FileUploadPage(self.driver)
        name = '图片上传控件_限制大小'
        compname = '图片上传控件_限制大小'
        file_path = comp.get_file_path("大于50KB.jpg")
        file_path2 = comp.get_file_path("小于50KB.jpg")
        text = comp.get_picture_limitSize(compname)
        self.assertIn("单个文件大小限制：50.00K", text, msg=name + '检验不通过')
        #time.sleep(0.5)
        result = comp.picture_upload(compname, file_path)
        self.assertIn("上传文件大小超出限制",result,msg=name + '检验不通过')
        #time.sleep(0.5)
        result2 =comp.picture_upload(compname,file_path2)
        self.assertIn("上传完成", result2, msg=name + '检验不通过')
        bool = comp.open_picture(compname,file_path2)
        #time.sleep(0.5)
        self.assertTrue(bool,msg=name + '检验不通过')

    def test_uploadnum_case(self):
        '''图片上传控件上传数量'''
        comp = FileUploadPage(self.driver)
        name = '图片上传控件上传数量'
        compname = '图片上传控件_最大上传数量'
        comp.scroll_to_pic_upload_btn(compname)
        comp.hide_activity_box() #隐藏操作按钮栏
        file_path = comp.get_file_path("大于50KB.jpg")
        file_path2 = comp.get_file_path("小于50KB.jpg")
        attr = comp.getcompatrr(compname, 'limitnumber')
        self.assertEqual('1', attr, msg=name + '检验不通过')
        comp.picture_upload(compname, file_path2) #上传图片
        comp.click_pictureupload_btn(compname)
        text = comp.adjustalertexistence()
        self.assertEqual("文件上传超出数量限制。",text,msg=name + '检验不通过')

    def test_recalculation_case(self):
        '''图片上传控件刷新重计算'''
        self.scroll_to('800')
        #time.sleep(0.5)
        comp = FileUploadPage(self.driver)
        name = '图片上传控件刷新重计算'
        compname = '图片上传_重计算'
        compname2 = '图片上传_刷新'
        file_path = comp.get_file_path("小于50KB.jpg")
        bool1 = comp.check_pic_box_existence(compname)
        self.assertTrue(bool1,msg=name + '检验不通过')
        comp.picture_upload(compname2, file_path)
        comp.wait_refresh_loading_back_show_then_hide()
        bool2 = comp.pic_upload_btn_is_invisibility(compname)
        self.assertTrue(bool2, msg=name + '检验不通过')

    def test_discript_case(self):
        '''图片上传控件描述校验'''
        comp = FileUploadPage(self.driver)
        name = '图片上传控件描述校验'
        compname = '图片上传_描述'
        comp.scroll_to_pic_upload_btn(compname)
        text = comp.getcompatrr(compname,'discript')
        self.assertEqual('图片上传_描述测试',text,msg=name + '检验不通过')

    def test_hidevalue_case(self):
        '''图片上传_隐藏时显示值'''
        self.scroll_to('850')
        comp = FileUploadPage(self.driver)
        name = '图片上传_隐藏时显示值'
        compname = '图片上传_隐藏时显示值'
        bool = comp.pic_upload_btn_is_invisibility(compname)
        self.assertTrue(bool,msg=name + '检验不通过')
        self.assertTrue(comp.show_when_hide('该控件已隐藏'),msg=name + '检验不通过')

    def test_readonly_case(self):
        '''图片上传_只读'''
        comp = FileUploadPage(self.driver)
        name = '图片上传_只读'
        compname = '图片上传_只读'
        comp.scroll_to_pic_upload_btn(compname)
        bool = comp.find_elem('span[name="' + compname + '"]').is_displayed()
        self.assertFalse(bool,msg=name + '检验不通过')
        text = comp.getcompatrr(compname, 'disabled')
        self.assertEqual('true', text, msg=name + '检验不通过')

    def test_windowsize_size(self):
        comp = FileUploadPage(self.driver)
        name = '图片上传_显示大小'
        compname = '图片上传控件_显示大小'
        type = comp.find_elem('span[name="'+compname+'"]+div.upload-box > div > div.uploadinput').get_attribute('style')
        self.assertIn('height: 80px; width: 80px;',type,msg=name + '检验不通过')

    def init(self):
#         self.test_type_case()
#         self.test_recalculation_case()
#         self.test_hidevalue_case()
#         self.test_readonly_case()
#         self.test_discript_case()
        self.test_uploadsize_case()
#         self.test_uploadnum_case()
#         self.test_windowsize_size()


if __name__ == '__main__':
    unittest.main()









