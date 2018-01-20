import os,sys
sys.path.append('../../../')

import time
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.main_page import MainPage


class MapPage(FormPage):
    '''地图控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def get_the_map_iframe(self):
        '''获取地图iframe'''
        iframe = self.element.parent.find_element_by_css_selector('iframe')
        return iframe
    
    def is_map_page(self):
        '''是否地图页面'''
        return self.find_elem('#mapbutton') != 'none' and self.find_elem('#map') != 'none'
    
    def get_type_out_btn(self):
        return self.find_elem('input[type="button"][name="btnSelectDept"]')
    
    def click_out_btn(self):
        btn = self.get_type_out_btn()
        self.scroll_to_viewport_4_form(btn)
        btn.click()
    
    def show_when_hide(self, text):
        '''是否显示了隐藏时显示值'''
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
    
