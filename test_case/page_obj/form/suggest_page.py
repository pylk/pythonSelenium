import time
from .text_page import TextPage
from .text_page import TextPhonePage
from selenium.webdriver import ActionChains

class SuperSuggestPage(object):
    
    def smart_set_value(self, ipname):
        '''给智能提示框的文本框输入值'''
        sas = self.driver.find_element_by_name(ipname)
        sas.send_keys('2')
        #time.sleep(0.5)

    def is_exist_typeahead(self):
        '''判断是否出现消息提示False表示不存在，Ture表示存在'''
        return self.is_element_visible('.typeahead.dropdown-menu[role="listbox"]')

    def get_value_case_return(self, tfname):
        tf = self.driver.find_element_by_name(tfname)
        return tf.get_attribute('value') == '2'



class SuggestPage(TextPage, SuperSuggestPage):
    '''智能提示框控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def select_prompt_opt(self,ipname):
        '''选择提示选择项'''
        self.find_elem_is_clickable('input[name="'+ipname+'"]+.typeahead.dropdown-menu[role="listbox"]').click()


class SuggestPhonePage(TextPhonePage, SuperSuggestPage):
    '''手机端智能提示框控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def set_val(self, val):
        self.element.send_keys(val)
        time.sleep(0.5)
        self.find_elem('.typeahead').click()
        time.sleep(0.5)
