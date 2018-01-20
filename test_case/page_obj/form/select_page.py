import os,sys
sys.path.append('../../../')
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.form.form_page import FormPhonePage


class SuperSelectPage(object):
    
    def set_val(self, val):
        '''设置控件值'''
        try:
            Select(self.find_element('select[name="'+self.comp_name+'"]')).select_by_value(val)
        except Exception as ex:
            print('设置单选框值异常%s' % ex)
        

class SelectPage(FormPage, SuperSelectPage):
    '''下拉选择框控件'''
    comp_name = ''
    driver = ''
    elements = ''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def get_component(self):
        '''根据名称获取控件'''
        print('获取测试控件：%s' % self.comp_name)
        return self.driver.find_element_by_name(self.comp_name)

    def readonlyshowvalonly(self):
        """下拉框控件显示为只读"""
        readonly = self.get_attr('readonly')
        disabled = self.get_attr('disabled')
        readonlyshowvalonly = self.get_attr('readonlyshowvalonly')
        return readonly == 'true' or disabled == 'true' or readonlyshowvalonly == 'true'

    def notnull_test(self):
        '''触发保存、获取提醒消息并返回'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        #time.sleep(0.1)
        return self.get_msg()


class SelectPhonePage(FormPhonePage, SuperSelectPage):
    '''下拉选择框控件'''
    comp_name = ''
    driver = ''
    elements = ''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()