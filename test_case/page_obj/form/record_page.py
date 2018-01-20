import os
import time
import sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage


class SuperRecordPage(object):
    
    def get_the_div(self):
        '''获取the div'''
        try:
            return self.find_elem('input[name="'+self.comp_name+'"] + div')
        except Exception as ex:
            print('微信录音获取div异常：%s' %ex)
            return 'none'
    
    def get_the_audio(self):
        '''获取音频文件'''
        try:
            the_div = self.get_the_div()
            return the_div.find_element_by_css_selector('audio')
        except Exception as ex:
            print('微信录音获取div异常：%s' %ex)
            return 'none'
    
    def check_del_function(self):
        '''微信录音功能验证'''
        try:
            self.wait_elem_show_then_hide('.weui_mask_transparent')
            the_div = self.get_the_div()
            record_del = the_div.find_element_by_css_selector('.btn-sound-delete')
            record_del.click()
            #time.sleep(0.5)
            the_div.find_element_by_css_selector('.btn-cancel').click()
            record_del.click()
            #time.sleep(0.5)
            the_div.find_element_by_css_selector('.btn-delete').click()
            return 'none'
        except Exception as ex:
            print('微信录音功能验证异常：%s' %ex)
            return ''
        
        try:
            self.get_the_audio()
            return ''
        except Exception as ex:
            print('微信录音获取div异常：%s' %ex)
            return 'none'
        
    def check_del_icon(self):
        '''微信录音删除图标是否显示'''
        try:
            the_div = self.get_the_div()
            record_del = the_div.find_element_by_css_selector('.btn-sound-delete')
            return record_del.is_displayed()
        except Exception as ex:
            print('微信录音功能验证异常：%s' %ex)
            return True
        

class RecordPage(FormPage, SuperRecordPage):
    '''微信录音控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    

class RecordPhonePage(FormPhonePage, SuperRecordPage):
    '''微信录音控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def is_desription_effect(self,compname):
        '''判断描述是否生效'''
        # 获取所有label值，判断是否存在传入的名称的lable
        elem = self.find_element('[name="'+compname+'"]')
        discript = elem.get_attribute('data-discription')
        dps = self.find_elements('div.formfield-wrap>label')
        for dp in dps:
            if dp.text == discript:
                # 判断label的text是否与discript属性相等
                return True
        return False

