import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.page_obj.button_page import ButtonPage
from test_case.running.html5.form.component_test import ComponentTest
from test_case.page_obj.form.file_upload_page import FileUploadPage



class FileUploadTest(ComponentTest):
    '''文件上传'''
    
    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '文件上传'

    def test_type_case(self):
        '''文件上传类型'''
        print(os.getcwd ())
        comp = FileUploadPage(self.driver)
        name = '文件上传类型'
        compname = '文件上传_名称'
        self.scroll_to('0')
        a = comp.getcomp(compname)
        type = a.get_attribute("fieldtype")
        self.assertEqual(type,"AttachmentUploadField", msg=name + '检验不通过')

    def test_uploadsize_case(self):
        '''文件上传控件上传大小限制'''
        comp = FileUploadPage(self.driver)
        name = '文件上传_限大小'
        compname = '文件上传_限大小'
        file_path = comp.get_file_path("大于100kb.doc")
        file_path2 = comp.get_file_path("小于100KB.txt")
        text = comp.getlimitSize(compname)
        self.assertIn("单个文件大小限制：100.00K", text, msg=name + '检验不通过')
        #time.sleep(0.5)
        comp.wait_loading_hide()
        result = comp.file_upload(compname, file_path)
        self.assertIn("上传文件大小超出限制",result,msg=name + '检验不通过')
        #time.sleep(0.5)
        comp.wait_loading_hide()
        result2 =comp.file_upload(compname,file_path2)
        self.assertIn("上传完成", result2, msg=name + '检验不通过')
        # time.sleep(10)   #必须，等待文件完成转换
        # self.driver.find_element_by_link_text("小于100KB.txt").click()
        # time.sleep(0.2) #切换不能太快
        # comp.switch_to_another_window()
        # text2 = comp.find_elem('span.preview-header-name').text
        # #time.sleep(0.5)
        # comp.close_currentwindow()
        # self.assertIn("小于100KB.txt",text2,msg=name + '检验不通过')

    def test_uploadtype_case(self):
        '''文件上传控件上传类型'''
        comp = FileUploadPage(self.driver)
        name = '文件上传控件上传类型'
        compname = '文件上传_格式'
        file_path = comp.get_file_path("大于100kb.doc")
        file_path2 = comp.get_file_path("小于100KB.txt")
        attr = comp.getcompatrr(compname,'customizetype')
        self.assertEqual('doc;xls',attr,msg=name + '检验不通过')
        comp.wait_loading_hide()
        result = comp.file_upload(compname, file_path2)
        self.assertIn("文件类型(仅支持'doc,xls'格式)或大小错误", result, msg=name + '检验不通过')
        #time.sleep(0.5)
        comp.wait_loading_hide()
        result2 = comp.file_upload(compname, file_path)
        self.assertIn("上传完成", result2, msg=name + '检验不通过')
        # time.sleep(10)   #必须，等待文件完成转换
        # self.driver.find_element_by_link_text("大于100kb.doc").click()
        # comp.switch_to_another_window()
        # #time.sleep(0.5)
        # text2 = comp.find_elem_visible('span.preview-header-name').text
        # #time.sleep(0.5)
        # self.assertIn("大于100kb.doc",text2,msg=name + '检验不通过')
        # comp.close_currentwindow()

    def test_uploadnum_case(self):
        '''文件上传控件上传数量'''
        comp = FileUploadPage(self.driver)
        name = '文件上传控件上传数量'
        compname = '文件上传_限数量1个'
        file_path = comp.get_file_path("大于100kb.doc")
        file_path2 = comp.get_file_path("小于100KB.txt")
        attr = comp.getcompatrr(compname, 'limitnumber')
        self.assertEqual('1', attr, msg=name + '检验不通过')
        comp.wait_loading_hide()
        comp.file_upload(compname, file_path2)
        comp.click_fileupload_btn(compname) #點擊上傳按鈕
        text = comp.adjustalertexistence()
        self.assertEqual("文件上传超出数量限制。",text,msg=name + '检验不通过')

    def test_recalculation_case(self):
        '''文件上传控件刷新重计算'''
        comp = FileUploadPage(self.driver)
        name = '文件上传控件重计算'
        compname = '文件上传_重计算'
        compname2 = '文件上传_刷新'
        comp.scroll_to_file_upload_btn(compname2)
        comp.hide_activity_box()
        file_path = comp.get_file_path("大于100kb.doc") #返回大于100kb.doc的路径
        bool1 = comp.check_existence(compname) #判断文件上传控件是否存在
        self.assertTrue(bool1,msg=name + '检验不通过')
        comp.wait_loading_hide()
        comp.file_upload(compname2, file_path)
        comp.wait_refresh_loading_back_show_then_hide()
        bool2 = comp.upload_btn_is_invisibility(compname)
        self.assertTrue(bool2, msg=name + '检验不通过')

    def test_notnull_case(self):
        '''文件上传控件非空校验'''
        comp = FileUploadPage(self.driver)
        name = '文件上传控件非空校验'
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        #time.sleep(0.5)
        text1 = comp.get_msg()
        self.assertIn("文件上传_非空校验'必须填写！", text1, msg=name + '检验不通过')

    def test_discript_case(self):
        '''文件上传控件描述校验'''
        name = '文件上传_描述'
        compname = '文件上传_描述'
        comp = FileUploadPage(self.driver)
        self.scroll_to('1200')
        text = comp.getcompatrr(compname,'discript')
        self.assertEqual('文件上传_描述',text,msg=name + '检验不通过')

    def test_hidevalue_case(self):
        '''文件上传_隐藏显示值'''
        self.scroll_to('1250')
        comp = FileUploadPage(self.driver)
        name = '文件上传_隐藏显示值'
        compname = '文件上传_隐藏显示值'
        bool = comp.check_existence(compname)
        self.assertFalse(bool,msg=name + '检验不通过')
        textcomp = self.driver.find_element_by_xpath('//input[@name="文件上传_隐藏显示值"]/parent::span')
        text = textcomp.text
        self.assertEqual('控件已隐藏',text,msg=name + '检验不通过')

    def test_readonly_case(self):
        '''文件上传控件只读'''
        self.scroll_to('1200')
        comp = FileUploadPage(self.driver)
        name = '文件上传_条件只读'
        compname = '文件上传_条件只读'
        bool = comp.find_elem('span[name="' + compname + '"]').is_displayed()
        self.assertFalse(bool,msg=name + '检验不通过')
        text = comp.getcompatrr(compname, 'disabled')
        self.assertEqual('true', text, msg=name + '检验不通过')

    def test_sort_case(self):
        '''文件上传控件排序'''
        comp = FileUploadPage(self.driver)
        name = '文件上传_文件排序'
        compname = '文件上传_文件排序'
        file_path = comp.get_file_path("大于100kb.doc")
        file_path2 = comp.get_file_path("小于100KB.txt")
        comp.scroll_to_file_upload_btn(compname)
        comp.hide_activity_box()
        comp.wait_loading_hide()
        comp.file_upload(compname,file_path) #上传文件大于100kb.doc
        #time.sleep(0.5)
        comp.wait_loading_hide()
        comp.file_upload(compname, file_path2)
        #time.sleep(0.5)
        text = comp.get_first_item_text(compname) #上传控件的第一个上传文件的text
        self.assertIn('大于100kb.doc',text,msg=name + '检验不通过')
        comp.click_fiest_item_down(compname)
        #time.sleep(0.5)
        text1 = comp.get_first_item_text(compname) #上传控件的第一个上传文件的text
        self.assertIn('小于100KB.txt', text1, msg=name + '检验不通过')

    def init(self):
#         self.test_type_case()
#         self.test_recalculation_case()
#         self.test_notnull_case()
#         self.test_hidevalue_case()
#         self.test_readonly_case()
#         self.test_sort_case()
#         self.test_discript_case()
        self.test_uploadsize_case()
#         self.test_uploadtype_case()
#         self.test_uploadnum_case()


if __name__ == '__main__':
    unittest.main()
