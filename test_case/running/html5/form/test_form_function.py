import os,sys
sys.path.append('../../../../')
import time
import unittest
from test_case.running.html5.app_test import AppTest
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.view.list_view_page import ListViewPage


class FormTest(AppTest):
    '''表单功能测试'''
    
    menu1 = '表单'
    menu2 = '表单功能'

    
    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.3)
        mp.switch_to_iframe()
    
    def test_style_lib(self):
        '''样式库使用'''
        menu3 = '表单_样式库'
        self.open_menu3(menu3)
        fp = FormPage(self.driver)
        self.assertIn('background-color:yellow', fp.get_style_lib(), msg='样式库使用检验不通过')
    
    def test_watermark_not(self):
        '''不显示水印'''
        menu3 = '表单_是否显示水印_否'
        self.open_menu3(menu3)
        
        lp = FormPage(self.driver)
        self.assertFalse(lp.is_show_watermark(), msg='不显示水印检验不通过')
    
    def test_watermark_show(self):
        '''显示水印'''
        menu3 = '表单_是否显示水印_是'
        self.open_menu3(menu3)
        
        fp = FormPage(self.driver)
        self.assertTrue(fp.is_show_watermark(), msg='显示水印检验不通过')
    
    def test_open_not(self):
        '''是否可打开脚本_否'''
        menu3 = '表单_是否可打开脚本_否'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        lp.find_elem('.listDataTr>.listDataTrTd').click() #点击第一行数据
        btn = ButtonPage(self.driver)
        fp = FormPage(self.driver)
        #time.sleep(0.5)
        self.assertEqual('你不能执行此操作', fp.is_alert_exist(), msg='是否可打开脚本_否检验不通过')
        fp.click_alert_accept()
        
    def test_open_yes(self):
        '''是否可打开脚本_是'''
        menu3 = '表单_是否可打开脚本_是'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        lp.click_row()
        btn = ButtonPage(self.driver)
        self.assertNotEqual('none', btn.get_button(btn.save), msg='是否可打开脚本_是检验不通过')
        
    def test_edit_not(self):
        '''是否可编辑脚本_否'''
        menu3 = '表单_是否可编辑脚本_否'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        lp.click_row()
        btn = ButtonPage(self.driver)
        
        comp = InputPage(self.driver, '文本一')
        self.assertTrue(comp.readonly_test(), msg= '是否可编辑脚本_否检验不通过')
        
    def test_edit_yes(self):
        '''是否可编辑脚本_是'''
        menu3 = '表单_是否可编辑脚本_是'
        self.open_menu3(menu3)
        lp = ListViewPage(self.driver)
        lp.click_row()
        btn = ButtonPage(self.driver)
        self.assertNotEqual('none', btn.get_button(btn.save), msg='是否可编辑脚本_是检验不通过')

    def init(self):
#         self.test_style_lib()
#         self.test_watermark_not()
#         self.test_watermark_show()
        self.test_open_not()
#         self.test_open_yes()
#         self.test_edit_not()
#         self.test_edit_yes()
        
    def setUp(self):
        mp = MainPage(self.driver)
        mp.refresh_main()
        if self.menu1 != '':
            mp.open_menu(self.menu1)
        #time.sleep(0.3)
        
        if self.menu2 != '':
            mp.open_menu(self.menu2)
        #time.sleep(0.3)
        
    def scroll_to(self, y):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        script = 'var $con = $("#_contentTable");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        time.sleep(0.1) #必须
    
if __name__ == '__main__':
    unittest.main()