import time
import os,sys
sys.path.append('../../../')
from .text_page import TextPage
from test_case.page_obj.form.form_page import FormPhonePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.form.input_page import InputPhonePage

class TabPhonePage(FormPhonePage):
    '''手机端选项卡控件'''

    def switch_tabpage(self,tabtitle):
        self.wait_msg_show_then_hide()
        self.find_element('a[title="'+tabtitle+'"]').click()

    def click_view_title(self,viewtitle):
        '''点击，进入视图'''
        self.find_element('div[title="'+viewtitle+'"]').click()

    def is_tab_viewname_visit(self,viewname,timeout=3):
        '''选项卡绑定的视图是否可见，可见返回Ture ，不可见返回 False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[title="'+viewname+'"]')))
            return True
        except:
            return False

    def get_tab_view_record_num(self,viewname):
        '''获取选项卡绑定视图的记录数'''
        return self.find_element('div[title="'+viewname+'"]+div>span').text

    def setvalue(self,viewname,inputcompname,val):
        self.click_view_title(viewname)
        self.wait_Tabloading_show_then_hide()
        btn = ButtonPhonePage(self.driver)
        btn.click_button('新建')
        inputtext = InputPhonePage(self.driver,inputcompname)
        inputtext.set_val(val)
        btn.click_button('保存')
        self.wait_msg_show_then_hide()
        btn.click_button('返回')
        self.wait_Tabloading_show_then_hide()
        self.driver.back()
        self.wait_elem_show_then_hide('.weui_mask_transparent')
        self.wait_Tabloading_show_then_hide()


    def del_val(self,viewname):
        '''删除选项卡视图记录'''
        self.click_view_title(viewname)
        self.wait_Tabloading_show_then_hide()
        btn = ButtonPhonePage(self.driver)
        lis = self.find_elements('input[name="_selects"]')
        for li in lis:
            li.click()
        btn.click_button('删除')
        self.accept_alert()  # 接受警告框
        self.wait_Tabloading_show_then_hide()
        self.driver.back()
        self.wait_elem_show_then_hide('.weui_mask_transparent')
        self.wait_Tabloading_show_then_hide()

    def clera_value(self):
        '''恢复包含元素数据'''
        btn = ButtonPhonePage(self.driver)
        self.click_view_title('非父子视图')
        self.wait_Tabloading_show_then_hide()
        lis = self.find_elements('input[name="_selects"]')
        num = 0
        if len(lis)>=7:
            for li in lis:
                num+=1
                if num>=7:
                    li.click()
            btn.click_button('删除')
            self.accept_alert() #接受警告框
            self.wait_elem_show_then_hide('.weui_mask_transparent')
            self.driver.back()
            self.wait_elem_show_then_hide('.weui_mask_transparent')
        else:
            self.driver.back()
            self.wait_elem_show_then_hide('.weui_mask_transparent')




    def is_lable_visit(self,lablenamae,timeout=3):
        '''判断当前页的lable是否可见，可见返回Ture ，不可见返回 False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[for="'+lablenamae+'"]')))
            return True
        except:
            return False


    def is_comp_hide(self, tabtitle, timeout=3):
        '''页签是否隐藏判断元素是否可见，可见返回Ture ，不可见返回 False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="'+tabtitle+'"]')))
            return True
        except:
            return False

    def is_comp_readonly(self, compname):
        '''判断页签是否只读,  只读则返回Ture,   非只读返回False'''
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="'+compname+'"]')))
            return False
        except TimeoutException:
            print('find_elem获取 %s 元素超时')
            return True


class TabPage(TextPage):
    '''选项卡控件'''

    comp_name = ''
    driver = ''
    element = ''
    
    def __init__(self, driver, tab_name=''):
        '''类初始化执行'''
        self.driver = driver
        self.tab_name = tab_name
        self.element = self.get_component()

        
    def find_tab_by_title(self): 
        '''根据title找到tab'''
        try:
            return self.find_elem('a[title="'+self.tab_name+'"]')
        except Exception as ex:
            print('获取控件异常：%s' %ex)
            return ''        
         
   
         
    def tab_switch(self):
        self.find_tab_by_title().click()


    def find_tab_collapse(self,num): 
        '''获取第n个折叠视图'''
        try:
            print("testadddddd===%s")
            return self.find_elem('#_formHtml > ul > li:nth-child('+num+')>div')
            
        except Exception as ex:
            print('获取控件异常：%s' %ex)
            return ''    

    def click_tab_collapse(self,num): 
        '''点击第n个折叠视图'''
        self.find_tab_collapse(num).click()        
 
    
    def get_tab_item_by_name(self,comp_name):
        '''根据名称获取控件'''
        print('获取测试控件：%s' %comp_name)
        try:
            return self.driver.find_element_by_name(comp_name)
        except Exception as ex:
            print('获取控件异常：%s' %ex)
        

