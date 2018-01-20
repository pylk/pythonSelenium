from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.button_page  import ButtonPage
from selenium import webdriver


class SelectAboutPage(FormPage):
    driver = ''

    def __init__(self,driver):
        self.driver = driver


    def getcomp(self,name):
        '''根据控件名称获取控件'''
        a = self.find_elem('select[name="'+name+'"]')
        return a


    def add(self,name,value):
        '''根据控件名和value值选择选项'''
        name1 = name+"ms2side__sx"
        value = str(value)
        self.find_elem('select[name="' + name1 + '"]>option[value="'+value+'"]').click()
        #time.sleep(0.5)
        self.find_elem('select[name="' + name + '"] + span > table > tbody > tr > td.ms2side__options > table > tbody > tr:nth-child(1) > td > p').click()

    def testreadonly(self,name,value):
        '''根据控件名和value值选择选项---用于只读测试'''
        name1 = name + "ms2side__sx"
        value = str(value)
        try:
            self.find_elem('select[name="' + name1 + '"]>option[value="' + value + '"]').click()
            return "只读不生效"
        except Exception as e:
            return "只读生效"

    def checkadd(self,name):
        '''判断某左右选择框的值是否有选中'''
        css = name+"ms2side__dx"
        print("css----"+css)
        try:
            s = self.find_elem('select[name="'+css+'"]>option').text
            return s
        except Exception as e:
            return "没有值被选中"


    def check_existence(self,name):
        '''判断左右选择框是否存在'''
        if(self.find_elem('select[name="' + name + '"]')!=None):
            return True
        else:
            return False


