from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from .text_page import TextPage
from .text_page import TextPhonePage


class SuperDepartmentPage(object):
    
    def set_val(self, val):
        '''设置控件值'''
        try:
            Select(self.find_element('select[name="'+self.comp_name+'"]')).select_by_visible_text(val)
        except Exception as ex:
            print('设置单选框值异常%s' % ex)
        

class DepartmentPage(TextPage, SuperDepartmentPage):
    '''部门选择框控件'''
    
    comp_name = ''
    driver = ''
    element = ''
    options = ''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def get_department_list(self):
        ''' 获取部门选择框的选项'''
        self.hide_activity_box()
        self.element.click()
        #self.show_elem_by_jq('div.activity-box')
        #time.sleep(0.5)
        return self.find_elems('select[name="'+self.comp_name+'"] option')
     
    def select_department_num(self,num):        
        ''' 获取某个部门的选择值'''
        self.hide_activity_box()
        deptlist = self.get_department_list()
        if deptlist:
            deptlist[num].click()
            return deptlist[num].text
        else:
             return ''
            
    def get_department_list_name(self):
        ''' 获取部门选择框的选项'''
        deptlist = self.get_department_list()
        dept_name=""
        for dept in deptlist:
            dept_name+=dept.text+';'
        return dept_name    

    def get_selected_depart_name(self):
        ''' 获取默认部门的值'''
        deptlist = self.get_department_list()
        dept_name=''
        for dept in deptlist:
            if dept.get_attribute('selected'):
                dept_name = dept.text
        return  dept_name


class DepartmentPhonePage(TextPhonePage, SuperDepartmentPage):
    '''手机端部门选择框控件'''

    comp_name = ''
    driver = ''
    element = ''
    options = ''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def is_department_clickable(self,name):
        '''判断部门选择框是否可点击，可点击返回Ture,不可返回False'''
        if self.find_elem_is_clickable('select[name="'+name+'"]',timeout=1)!=None:
            return True
        else:
            return False
            

    