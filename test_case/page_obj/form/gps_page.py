import os,sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GPSPhonePage(FormPhonePage):
    '''手机端GPS定位控件'''

    def __init__(self,driver):
        self.driver = driver

    def getcomp(self,name):
        '''根据控件名称获取控件'''
        a = self.find_elem('input[name="'+name+'"]')
        return a

    def is_comp_hide(self, compname, timeout=3):
        '''判断在线拍照控件是否隐藏判断元素是否可见，返回Ture or False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[for="'+compname+'"]+div.flexright')))
            return True
        except:
            return False


class GPSPage(FormPage):
    '''GPS定位控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def get_gps_div(self):
        '''获取gps控件 div'''
        return self.find_elem('input[name="'+self.comp_name+'"] + div')
    
    def is_gps_elem_invisibility(self):
        '''判断gps控件元素是否不可见'''
        return self.is_elem_invisibility('input[name="'+self.comp_name+'"] + div')
