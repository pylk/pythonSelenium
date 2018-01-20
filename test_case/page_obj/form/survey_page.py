import os,sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.main_page import MainPage


class SuperSurveyPage(object):

    def get_the_div(self):
        '''获取the div'''
        try:
            return self.find_elem('input[name="'+self.comp_name+'"] + div')
        except Exception as ex:
            print('调查问卷获取div异常：%s' %ex)
            return 'none'
    
    def get_the_div_text(self):
        '''获取the div 内容'''
        try:
            return self.get_the_div().text
        except Exception as ex:
            print('调查问卷获取内容异常：%s' %ex)
            return ''

    def the_check_is_enabled(self):
        '''复选框是否只读'''
        try:
            the_div = self.get_the_div()
            checkbox = the_div.find_element_by_css_selector('input[type="checkbox"]')
            if checkbox:
                return checkbox.is_enabled()
        except Exception as ex:
            print('调查问卷只读获取checkbox是否只读异常：%s' %ex)
            return 'none'
        

class SurveyPage(FormPage, SuperSurveyPage):
    '''调查问卷控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()


class SurveyPhonePage(FormPhonePage, SuperSurveyPage):
    '''调查问卷手机端控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

