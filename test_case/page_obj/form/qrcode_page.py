import os,sys
sys.path.append('../../../')

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.main_page import MainPage


class QrcodePage(FormPage):
    '''二维码控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def get_canvas_height(self):
        '''获取canvas高度'''
        canvas = self.find_elem('input[name="'+self.comp_name+'"] + div > canvas')
        return canvas.get_attribute('height')
        
    def switch_key(self):
        '''焦点切换功能'''
        self.element.click()
        active_element_1 = self.get_active_element()
        self.element.send_keys(Keys.TAB)
#         self.element.send_keys(Keys.ENTER)
        active_element_2 = self.get_active_element()
        return active_element_1 == active_element_2
    
    def show_when_hide(self, text):
        elems = self.find_elems('span')
        for elem in elems:
            text1 = elem.text
            if text1 == text:
                return True
        return False
    
    def show_when_print(self, text):
        elems = self.find_elems('p')
        for elem in elems:
            text1 = elem.text
            if text1 == text:
                return True
        return False
    
class QrcodePhonePage(FormPhonePage):
    '''phone二维码控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def get_canvas_height(self):
        '''获取canvas高度'''
        canvas = self.find_element('input[name="'+self.comp_name+'"] + div canvas')
        return canvas.get_attribute('height')
        
    def switch_key(self):
        '''焦点切换功能'''
        self.element.click()
        active_element_1 = self.get_active_element()
        self.element.send_keys(Keys.TAB)
#         self.element.send_keys(Keys.ENTER)
        active_element_2 = self.get_active_element()
        return active_element_1 == active_element_2
    
    def show_when_hide(self, text):
        elems = self.find_elems('span')
        for elem in elems:
            text1 = elem.text
            if text1 == text:
                return True
        return False
    
    
