import os,sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page  import FormPage
from test_case.page_obj.form.form_page  import FormPhonePage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.main_page import MainPage


class FlowRemindHistoryPage(FormPage):
    '''流程催办历史控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def check_title(self):
        '''获取控件title是否存在'''
        try:
            self.element.find_element_by_css_selector('div.field-title')
            return True
        except Exception as ex:
            print('流程催办历史控件获取控件title异常：%s' %ex)
            return False
    
    def get_table_head_first_td_text(self):
        '''获取控件table head里第一个td的text值'''
        try:
            return self.element.find_element_by_css_selector('table > thead > tr > th:nth-child(1)').text
        except Exception as ex:
            print('流程催办历史控件获取控件table head里第一个td的text值异常：%s' %ex)
            return ''
    
    def get_table_tbody_first_td_text(self):
        '''获取控件table tbody里第一个td的text值'''
        try:
            return self.element.find_element_by_css_selector('table > tbody:nth-child(3) > tr > td:nth-child(1)').text
        except Exception as ex:
            print('流程催办历史控件获取控件table tbody里第一个td的text值异常：%s' %ex)
            return ''
    
    def get_description_text(self):
        '''获取描述文本'''
        try:
            return self.element.find_element_by_css_selector('div.field-title').text
        except Exception as ex:
            print('流程催办历史获取描述文本异常：%s' %ex)
            return ''


class FlowRemindHistoryPhonePage(FormPhonePage):
    '''流程催办历史控件手机端'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def get_table_head_first_td_text(self):
        '''获取控件table head里第一个td的text值'''
        try:
            return self.element.find_element_by_css_selector('table[name="'+self.comp_name+'"] > thead > tr > th:nth-child(1)').text
        except Exception as ex:
            print('流程催办历史控件获取控件table head里第一个td的text值异常：%s' %ex)
            return ''
    
    def get_table_tbody_first_td_text(self):
        '''获取控件table tbody里第一个td的text值'''
        try:
            return self.element.find_element_by_css_selector('table[name="'+self.comp_name+'"] > tbody > tr > td:nth-child(1)').text
        except Exception as ex:
            print('流程催办历史控件获取控件table tbody里第一个td的text值异常：%s' %ex)
            return ''
    