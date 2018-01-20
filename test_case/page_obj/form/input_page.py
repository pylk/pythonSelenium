from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from test_case.page_obj.form.text_page import TextPage
from test_case.page_obj.form.text_page import TextPhonePage



class InputPage(TextPage):
    '''单行文本框控件'''
    
    comp_name = ''
    driver = ''
    element = ''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def show_when_print(self, text):
        elems = self.find_elems('p')
        for elem in elems:
            text1 = elem.text
            if text1 == text:
                return True
        return False

class InputPhonePage(TextPhonePage):
    '''单行文本框控件'''

    comp_name = ''
    driver = ''
    element = ''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def get_inputtext_value(self):
        '''获取单行文本框的值'''
        return self.element.get_attribute("value")
