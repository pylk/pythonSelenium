import os
import sys
import time
import unittest
sys.path.append('../../../../')
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.record_page import RecordPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage


class RecordPhoneTest(ComponentPhoneTest):
    '''微信录音控件测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'  #主页打开菜单时使用
    menu3 = '微信录音'
    
    def test_type_case(self):
        '''控件属性'''
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()
        name = '微信录音控件_名称'
        #time.sleep(0.5)
        comp = RecordPhonePage(self.driver, name)
        self.assertNotEqual('none', comp.get_the_div(), msg=name + '检验不通过')
        self.assertNotEqual('none', comp.get_the_audio(), msg=name + '检验不通过')
        self.assertEqual('none', comp.check_del_function(), msg=name + '检验不通过') #删除后音频文件不存在

    def test_desription_case(self):
        '''描述'''
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()
        name = '微信录音控件_描述'
        #time.sleep(0.5)
        comp = RecordPhonePage(self.driver, name)
        self.assertTrue(comp.is_desription_effect(name), msg=name + '检验不通过')
        
    def test_readonly_case(self):
        '''控件属性'''
        lp = ListViewPhonePage(self.driver)
        lp.open_fisrt_doc()
        name = '微信录音控件_只读条件'
        comp = RecordPhonePage(self.driver, name)
        #time.sleep(0.5)
        self.assertFalse(comp.check_del_icon(), msg=name + '检验不通过') #删除后音频文件不存在
        
    def init(self):
        '''所有测试'''
#         self.test_type_case()
#         self.test_desription_case()
        self.test_readonly_case()
        
        
if __name__ == '__main__':
    unittest.main()
