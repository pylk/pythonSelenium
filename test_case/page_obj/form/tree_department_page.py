import os,sys
sys.path.append('../../../')
import time
from .text_page import TextPage
from .text_page import TextPhonePage
from test_case.page_obj.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_case.page_obj.button_page import ButtonPhonePage


class TreeDepartmentSuperPage(object):
    '''树形部门选择框控件手机端和PC端共同方法'''






class TreeDepartmentPage(TextPage,TreeDepartmentSuperPage):
    '''树形部门选择框控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.driver.find_element_by_name('show_'+comp_name)
        self.dialog = self.find_elem(('input[name="'+self.comp_name+'"]+span'))

    def get_dept(self):
         return self.driver.find_element_by_name('show_'+self.comp_name)
     
    def add_dept_buttion(self):
        self.dialog.click()
        
    def clean_button(self):
        '''清除按钮 '''       
        self.find_elem('input[name="'+self.comp_name+'"]+span+span').click()
   
    def open_dept_dialog(self): 
        '''打开树形部门弹出框'''
        self.add_dept_buttion()
        #time.sleep(0.5)
        mainpage=MainPage(self.driver)
        mainpage.switch_to_div_iframe()
        toptree=self.find_elem('#deplist>ul>li[data-level="1"] span.wtree-adron > i')
        toptree.click()

    def select_dept_save(self):
         '''选择前2个部门，点击【保存】'''
         self.open_dept_dialog()
         #time.sleep(0.5)
         self.find_elems('input[type=checkbox]')[0].click()
         self.find_elems('input[type=checkbox]')[1].click()
         self.find_elem('#btn-save').click()
               
    def select_dept(self):
         '''弹出框 选择2个部门，点击【保存】并且切换到页签的iframe'''
         self.select_dept_save()
         mainpage=MainPage(self.driver)
         
         mainpage.switch_to_parent()
         mainpage.switch_to_iframe()
         return  self.element.get_attribute('value')
         
    def beyond_dept_num(self):      
        '''选择2个部门，获取返回信息'''        
        self.select_dept_save()
        try:
            error_msg=self.get_alert_text()
            self.click_alert_dismiss()
            return error_msg
        except Exception as e:
            print(e)   
                     
    def  close_dept(self):
        '''关闭按钮 '''
        self.open_dept_dialog()
        #time.sleep(0.5)
        self.find_elem('#btnbarDiv > div:nth-child(2)').click()
        try:
            save_button=self.find_elem('#btn-save').get_attribute("class");
            if save_button == 'btnbarDiv':
                 return "failed"
#         mainpage=MainPage(self.driver)        
#         mainpage.switch_to_parent()
#         mainpage.switch_to_iframe()
        except Exception as e:
           print(e)
           return "closed"


class TreeDepartmentPhonePage(TextPhonePage,TreeDepartmentSuperPage):
    '''手机端树形部门选择框控件'''

    def __init__(self, driver):
        self.driver = driver

    def get_tree_elem(self,compname):
        '''获取树形部门选择框控件元素'''
        tree_elem = 'input[name="'+compname+'"]'
        return tree_elem

    def get_dept(self,comp_name):
        tree_elem = self.find_elem_visible('input[name="' + comp_name + '"]+span[title="请选择"]')
        return tree_elem

    def is_comp_readonly(self,compname):
        '''判断树形部门选择框控件是否只读'''
        try:
            WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.get_tree_elem(compname))))
            return False
        except TimeoutException:
            print('find_elem获取 %s 元素超时' %compname)
            return True

    def is_comp_hide(self,compname):
        '''判断树形部门选择框控件是否隐藏'''
        try:
            WebDriverWait(self.driver, timeout=3).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.get_tree_elem(compname))))
            return True
        except TimeoutException:
            print('获取 %s 超时' %compname)
            return False

    def go_to_depts(self,compname):
        '''树形部门选择框选择部门'''
        self.find_elem_is_clickable('input[name="'+compname+'"]+span[title="请选择"]').click()
        self.switch_to_phone_iframe() #切到iframe 手机端
        self.find_elem_is_clickable('i.wtree-arrow').click() #点击展开顶级部门

    def select_depts(self,compname,lis):
        '''开始选择部门'''
        self.go_to_depts(compname)
        for li in lis:
            self.find_elem_is_clickable('li[data-name="'+li+'"]>div.wtree-deptlist-box>input.wtree-deptlist-input').click()
        bt = ButtonPhonePage(self.driver)
        bt.click_iframe_button('保存')
        self.driver.switch_to.default_content()

    def select_depts_no_save(self,compname,lis):
        '''开始选择部门不保存'''
        self.go_to_depts(compname)
        for li in lis:
            self.find_elem('li[data-name="'+li+'"]>div.wtree-deptlist-box>input.wtree-deptlist-input').click()


    def get_select_depts(self,compname):
        '''正常情况下获取已选的部门'''
        val = self.find_element('label[for="'+compname+'"]+div>div>input.contactField').get_attribute("value")
        return val

    def get_select_depts_readonly(self,compname):
        '''只读情况下获取已选的部门'''
        target = self.find_element('div#'+compname+'_show')
        self.scroll_to_target_element(target)
        val = target.text
        return val







    


    