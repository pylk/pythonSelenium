import os
import sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage


class FlowhistoryPage(FormPage):
    '''流程历史控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def check_title(self):
        '''获取控件title是否存在'''
        try:
            self.element.find_element_by_css_selector('li > div.field-title')
            return True
        except Exception as ex:
            print('流程历史控件获取控件title异常：%s' %ex)
            return False
    
    def get_table_head_first_td_text(self):
        '''获取控件table head里第一个td的text值'''
        try:
            return self.element.find_element_by_css_selector('li > table > thead > tr > th:nth-child(1)').text
        except Exception as ex:
            print('流程历史控件获取控件table head里第一个td的text值异常：%s' %ex)
            return ''
    
    def get_table_tbody_first_td_text(self):
        '''获取控件table tbody里第一个td的text值'''
        try:
            return self.element.find_element_by_css_selector('li > table > tbody:nth-child(3) > tr > td:nth-child(1)').text
        except Exception as ex:
            print('流程历史控件获取控件table tbody里第一个td的text值异常：%s' %ex)
            return ''
    
    def check_flow_img(self):
        '''获取流程图'''
        try:
            self.find_elem('li > img')
            return True
        except Exception as ex:
            print('流程历史控件获取div异常：%s' %ex)
            return False
        
    def get_description_text(self):
        '''获取描述文本'''
        try:
            return self.element.find_element_by_css_selector('li > div.field-title').text
        except Exception as ex:
            print('流程历史获取描述文本异常：%s' %ex)
            return ''


class FlowhistoryPhonePage(FormPhonePage):
    '''流程历史控件手机端'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def check_title(self):
        '''获取控件title是否存在'''
        try:
            text = self.find_element('label[for="'+self.comp_name+'"]').text
            return (text == self.comp_name)
        except Exception as ex:
            print('流程历史控件获取控件title异常：%s' %ex)
            return False
    
    def get_table_head_first_td_text(self):
        '''获取控件table head里第一个td的text值'''
        try:
            return self.element.find_element_by_css_selector('table[name="'+self.comp_name+'"] > thead > tr > th:nth-child(1)').text
        except Exception as ex:
            print('流程历史控件获取控件table head里第一个td的text值异常：%s' %ex)
            return ''
    
    def get_table_tbody_first_td_text(self):
        '''获取控件table tbody里第一个td的text值'''
        try:
            return self.element.find_element_by_css_selector('table[name="'+self.comp_name+'"] > tbody > tr > td:nth-child(1)').text
        except Exception as ex:
            print('流程历史控件获取控件table tbody里第一个td的text值异常：%s' %ex)
            return ''
    
    def check_flow_img(self):
        '''获取流程图'''
        try:
            self.find_elem('div[name="'+self.comp_name+'"] li > img')
            return True
        except Exception as ex:
            print('流程历史控件获取div异常：%s' %ex)
            return False
        
    def is_desription_effect(self,compname):
        '''判断描述是否生效'''
        # 获取所有label值，判断是否存在传入的名称的lable
        elem = self.find_element('[name="'+compname+'"]')
        discript = elem.get_attribute('discript')
        label = self.find_element('label[for="'+self.comp_name+'"]').text
        return (label == discript)
